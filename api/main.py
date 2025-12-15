import cv2
import numpy as np
from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile
from services.layout_aware_receipt_verification import layout_aware_receipt_verification
from utils.ml_model_loader import load_model

ml_models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # STARTUP
    
    
    ml_models["logistic_regression"] = load_model()
    
    yield
    
    # SHUTDOWN
    
    ml_models.clear()
    print("[Shutdown] Resources released.")

app = FastAPI(
    title="Fake Receipt Detection API", 
    version="1.0.0",
    lifespan=lifespan
)

@app.get("/")
def app_root() -> dict[str, str]:
    return {
        "message": "Hello World!"
    }

@app.post("/detect-fake-receipt")
async def detect_fake_receipt(
    image: UploadFile,
    expected_amount: str
):
    image_bytes = await image.read()
    
    # Decode image
    np_arr = np.frombuffer(image_bytes, np.uint8)
    image_np = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    if image_np is None:
        return {"error": "Invalid image"}
    
    
    verification, lines_data = layout_aware_receipt_verification(
        image=image_np,
        expected_amount={"total_amount": expected_amount.lower()},
    )

    return {
        "message": "success",
        "image_filename": image.filename,
        "expected_amount": expected_amount,
        "verification": verification,
        "lines_data": lines_data
    }
