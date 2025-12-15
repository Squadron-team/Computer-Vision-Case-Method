# Laporan PBL Machine Learning

**Overview:**
- ML model : Logistic regression
- Studi kasus : deteksi struk palsu bank BNI
- Peran ML : klasifikasi karakter dari proses OCR

---

## Alur kerja Machine Learning

1. [Pengumpulan data](#1-pengumpulan-data)
2. [Data preprocessing & ekstraksi fitur](#2-data-preprocessing--ekstraksi-fitur)
3. [Pembagian data (data splitting)](#3-pembagian-data-data-splitting)
4. [Pemodelan klasifikasi](#3-pembagian-data-data-splitting)
5. [Evaluasi model](#5-evaluasi-model)
6. [Pengujian dan integrasi dengan sistem utama](#6-pengujian-dan-integrasi-dengan-sistem-utama)


### 1. Pengumpulan data

Data yang dikumpulkan berasal dari beberapa gambar struk Bank BNI. Data ini mencakup gambar struk transfer yang dilakukan dengan menggunakan Bank BNI. Total terdapat kurang lebih gambar dengan sejumlah 70 gambar. 

Dari beberapa gambar yang diperoleh, proses selanjutnya adalah pengambilan gambar yang mengandung karakter alfanumerik dan juga beberapa simbol. Proses ini akan dilakukan dengan melakukan proses croping pada gambar yang ada sehingga output akhirnya berupa beberapa gambar kecil yang mencakup karakter alfa numerik dan simbol.

### 2. Data preprocessing & ekstraksi fitur

Data preprocessing dilakukan agar data input konsisten dan memudahkan proses pemodelan pada model machine learning. Proses ini terdiri dari beberapa tahap yang mencakup:
- Konversi gambar ke grayscale
- Penentuan threshold
- Menentukan bounding box
- Melakukan proses resizing untuk konsistensi ukuran
- Menambahkan padding pada gambar yang ramping
- Mengubah data gambar menjadi flattened (1D array)

Proses tersebut membuat gambar yang semula memiliki format RGB bisa diolah dengan mudah oleh model machine learning. Bentuk akhir dari tahapan ini adalah gambar berubah menjadi sebuah vektor dengan 1D array. Data tersebut akan menjadi fitur dari gambar yang mana fitur ini menyimpan data untuk tiap-tiap pixel gambar. Hal itu juga sekalian menjadi proses dari ekstraksi fitur yang merubah data gambar berdimensi tinggi menjadi flat.

### 3. Pembagian data (data splitting)

Data yang sudah disiapkan akan dibagi menjadi data training dan evaluasi. Proporsi yang ditentukan adalah 80% akan digunakan sebagai data training dan sisanya menjadi data evaluasi. 

### 4. Pemodelan klasifikasi

Pemodelan dilakukan dengan menggunakan model Logistic regression yang sangat ideal dengan kondisi input data. Model logistic regression memungkinkan model memiliki pembobotan tersendiri pada tiap-tiap pixel yang telah di flattening. Tiap karakter memiliki porsi pixel yang berbeda-beda namun logistc regression mampu melakukan generalisasi data sehingga mampu melakukan klasifikasi dengan baik.

### 5. Evaluasi model

Evaluasi model dilakukan dengan melakukan perbandingan dan konsistensi antara data training dan testing. Hasilnya diperoleh model logistic regression mampu menghasilkan akurasi lebih dari 90%.

### 6. Pengujian dan integrasi dengan sistem utama

Integrasi dengan sistem utama adalah integrasi dengan sistem deteksi struk palsu. Pada sistem utama, hasil dari deteksi karakter yang ada akan digunakan sebagai bahan pemrosesan lanjutan untuk evaluasi apakah suatu gambar tersebut merupakan gambar/struk palsu atau bukan.

