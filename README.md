# Image-Based Fake Mobile Banking Receipt Detection 🔎

A case study to detect whether a mobile banking receipt image is genuine or fake.
For this case study, we chose a receipt format from **Bank Nasional Indonesia (BNI)**, specifically **Wondr**: https://wondr.bni.co.id/.

This project is actually part of our main mobile app, **Rukunin**, a mobile tool designed to help residents and local leaders manage administration, finances, events, and day-to-day neighborhood tasks.

You can find our main project, Rukunin, here:

👉🏻 https://github.com/Squadron-team/Rukunin-App

## Development

This detection project focuses on several types of receipt inconsistencies, such as:
1. A different total amount than expected
2. Incorrect or modified fields in the receipt
3. Changes in the overall receipt layout

For image processing, we experimented with:
- Object segmentation
- Optical Character Recognition (OCR)
- Layout matching


For machine learning, we tested several classical ML algorithms:
- Support Vector Machine (SVM)
- k-Nearest Neighbor (KNN)
- Logistic Regression

## Deployment

In this case study, we also experimented with deploying both the model and image-processing pipeline directly to the target device.
Since our main app runs on mobile and the computation is not too heavy, running everything **fully on-device** is the best approach for both performance and privacy.

Our mobile app is built with the Flutter framework. We deployed the model using [ONNX](https://onnx.ai/), and we implemented communication between Dart and Android Kotlin using FFI and platform channels to perform the computer vision tasks natively.

## Future Direction

We plan to expand this case study by improving robustness across more receipt formats, adding more advanced image-processing techniques, and evaluating real-world performance on different mobile devices.
We also aim to refine the model so it can generalize better, reduce false positives, and integrate seamlessly into the Rukunin app’s workflow.

This repository will continue to grow as we explore more techniques and strengthen our approach to on-device computer vision.
