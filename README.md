## Proyek Akhir: Analisis Dropout Mahasiswa di Jaya Jaya Maju Edutech

## Business Understanding

Perusahaan Edutech adalah sebuah perusahaan yang bergerak di bidang teknologi pendidikan. Fokus utama perusahaan ini adalah memberikan solusi pendidikan yang berbasis teknologi, termasuk sistem manajemen pembelajaran, analisis data pendidikan, dan pengembangan platform pembelajaran online. Dengan meningkatnya kebutuhan akan pendidikan yang dapat diakses secara fleksibel, perusahaan ini bertujuan untuk mengoptimalkan layanan pendidikan berbasis digital agar lebih mudah diakses oleh siswa, guru, dan institusi pendidikan.

### Permasalahan Bisnis

Perusahaan Edutech menghadapi tantangan dalam mengelola data akademik siswa dan menganalisis pola perilaku mereka, seperti memprediksi kemungkinan drop-out, kinerja akademik, serta faktor-faktor yang mempengaruhi keberhasilan mereka. Hal ini menjadi masalah karena kesulitan dalam memberikan perhatian yang tepat kepada siswa yang berisiko tinggi mengalami drop-out, serta memberikan rekomendasi personalisasi untuk meningkatkan kinerja akademik.
Tujuan utama dari proyek ini adalah mengembangkan model prediktif yang dapat membantu perusahaan untuk:
    - Memprediksi status siswa (Dropout, Enrolled, Graduate) berdasarkan data akademik dan perilaku mereka.
    - Membantu pengambil keputusan dalam mengidentifikasi siswa yang berisiko drop-out agar dapat diberikan intervensi yang tepat waktu.
    - Memberikan rekomendasi untuk meningkatkan tingkat kelulusan siswa dan keterlibatan mereka dalam kegiatan pembelajaran.

### Cakupan Proyek

Cakupan proyek ini meliputi beberapa tahap utama:

1. **Eksplorasi dan pembersihan data**
    Menyaring dan membersihkan data mahasiswa untuk memastikan kualitas analisis.
2. **Analisis eksploratif (EDA)**
    Menggunakan visualisasi dan statistik deskriptif untuk memahami pola dan insight dari data.
3. **Pemodelan prediktif**
    Membangun model prediktif menggunakan algoritma machine learning (seperti Logistic Regression, Random Forest, dan XGBoost) untuk memprediksi status siswa.
4. **Evaluasi model**
    Melakukan evaluasi terhadap model yang dibangun untuk memastikan akurasi, presisi, recall, dan f1-score yang baik.
5. **Pengembangan dashboard**
    Membuat dashboard visual untuk menampilkan hasil analisis model dan memudahkan pemantauan status siswa serta rekomendasi.
6. **Rekomendasi dan action items**
    Memberikan rekomendasi strategi dan kebijakan berdasarkan hasil analisis data.
7. **Pengembangan Prototipe Sistem Machine Learning**
    Membuat sistem prototipe berbasis web menggunakan Streamlit untuk memberikan rekomendasi dan prediksi kepada pengguna.

### Persiapan

- **Sumber data:**
`https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/students_performance/data.csv`

- **Setup environment:**
    - Buat dan aktifkan virtual environment
        ```
        pipenv install
        pipenv shell
        ```
    - Install library yang dibutuhkan
        ```bash
        pip install -r requirements.txt
        ```
    
- **Email dan password Metabase**
    - Email: ramaadjiprsty@gmail.com
    - password: root123

## Business Dashboard

Business dashboard yang telah dibuat menyajikan informasi secara real-time mengenai prediksi status siswa dan metrik-metrik penting lainnya. Dashboard ini memberikan tampilan visual tentang jumlah siswa yang berisiko drop-out, analisis kinerja akademik, serta distribusi data berdasarkan berbagai fitur.

### Isi Dashboard
Dashboard ini menyajikan berbagai metrik terkait kinerja siswa:
- Dropouts Based on Previous Educational Background: Menampilkan tren jumlah siswa putus sekolah berdasarkan latar belakang pendidikan sebelumnya. Grafik garis menunjukkan fluktuasi jumlah dan rata-rata nilai.
- Distribution of Student Status: Menggambarkan proporsi siswa dalam berbagai status (misalnya, Graduate, Dropout, Enrolled) dalam bentuk diagram lingkaran. Jumlah total siswa yang ditampilkan adalah 4,424.
- Scholarship and Dropout Status: Membandingkan jumlah siswa yang menerima beasiswa dengan status dropout mereka melalui diagram batang.
- Dropout Rate by Attending Time: Menunjukkan tingkat dropout berdasarkan waktu kehadiran (misalnya, daytime, evening) dalam bentuk diagram lingkaran. Tingkat dropout untuk daytime adalah 85.6% dan evening adalah 14.4%, dengan total 1,421 siswa.
- Father's Influence on Status: Memvisualisasikan pengaruh pekerjaan ayah (misalnya, Graduate, Dropout, Passed) terhadap status siswa melalui diagram batang bertumpuk.
- The Biggest Dropout Profiles by Parental Education: Menampilkan profil dropout terbesar berdasarkan tingkat pendidikan orang tua melalui diagram batang bertumpuk. Sumbu horizontal menunjukkan kombinasi tingkat pendidikan orang tua.
- Average Grade per Status: Membandingkan rata-rata nilai siswa berdasarkan status (Graduate, Dropout, Passed) melalui diagram batang.
- Dropout Rate by Age Group: Menyajikan tingkat dropout berdasarkan kelompok usia dalam bentuk diagram lingkaran. Distribusinya adalah: <20 (28.6%), 20-24 (38.7%), 25-29 (16.0%), 30-34 (10.7%), dan >34 (6.0%), dengan total 1,421 siswa.
Dropout Rate by Gender: Menggambarkan tingkat dropout berdasarkan jenis kelamin dalam bentuk diagram lingkaran. Tingkat dropout untuk Female adalah 50.7% dan Male adalah 49.3%, dengan total 1,421 siswa.

### Tujuan
- Memberikan insight cepat bagi pemangku kepentingan untuk mengidentifikasi area kinerja siswa yang memerlukan perhatian lebih.
- Memfasilitasi pengambilan keputusan strategis dalam meningkatkan retensi dan keberhasilan siswa berdasarkan data yang terukur.
- Memungkinkan pihak sekolah dan administrator untuk memantau tren putus sekolah secara berkala dan merancang intervensi yang tepat.

## Menjalankan Sistem Machine Learning
- **Menjalankan Streamlit untuk proses prediksi**
    - Buka file `app.py`
        - Jalankan kode dibawah ini 
            ```
            streamlit run app.py
            ```
        - Masukkan data entri yang dibutuhkan secara manual
        - Klik tombol prediksi, output yang keluar berupa prediksi status (Dropout/Graduate/Enrolled)

- **Link Prototype**
    - `https://ramaadjiprsty-students-dashboard-app-qeslo9.streamlit.app/`

## Conclusion
Melalui proyek ini, telah berhasil dikembangkan model prediktif yang membantu perusahaan Edutech dalam memprediksi status siswa dan memberikan rekomendasi untuk intervensi tepat waktu. Model ini telah dievaluasi dan menunjukkan kinerja yang baik dalam hal akurasi dan f1-score. Berikut adalah skor evaluasi untuk beberapa model yang telah diuji:

- Logistic Regression:
    - Accuracy: 77%
    - Precision (Dropout): 79%
    - Recall (Dropout): 76%
    - F1-Score (Dropout): 77%
    - Macro Avg F1-Score: 69%

- Random Forest:
    - Accuracy: 76%
    - Precision (Dropout): 78%
    - Recall (Dropout): 77%
    - F1-Score (Dropout): 77%
    - Macro Avg F1-Score: 67%

- XGBoost:
    - Accuracy: 76%
    - Precision (Dropout): 77%
    - Recall (Dropout): 75%
    - F1-Score (Dropout): 76%
    - Macro Avg F1-Score: 69%

Dari evaluasi ini, Logistic Regression menunjukkan performa yang lebih baik dengan nilai accuracy 77% dan f1-score tertinggi untuk kategori Dropout. Hal ini menjadikannya model yang lebih handal dalam memprediksi siswa yang berisiko drop-out.

Dengan adanya dashboard bisnis, perusahaan dapat memantau status siswa secara real-time dan membuat keputusan berbasis data untuk meningkatkan hasil pendidikan. Dashboard ini memberikan visualisasi yang memudahkan pemangku kepentingan dalam memantau prediksi status siswa dan membantu mereka mengambil langkah-langkah intervensi yang diperlukan.

Selain evaluasi model, analisis menyeluruh terhadap data menunjukkan bahwa terdapat beberapa faktor signifikan yang memengaruhi risiko dropout. Berdasarkan visualisasi dan segmentasi dalam dashboard:
- Mahasiswa dengan nilai akademik rendah, baik di semester pertama maupun kedua, - memiliki kecenderungan lebih tinggi untuk dropout.
- Tidak memiliki beasiswa berkorelasi kuat dengan status dropout.
- Mahasiswa kelas malam (evening) lebih rentan terhadap dropout dibandingkan kelas pagi.
- Mahasiswa yang menunggak pembayaran (debtor) memiliki proporsi dropout yang tinggi.
- Usia juga menjadi faktor penting: kelompok usia <25 tahun menyumbang sebagian besar dari total dropout.
- Mahasiswa yang berasal dari keluarga dengan pendidikan orang tua rendah, terutama ibu, juga lebih banyak ditemukan dalam kelompok dropout.

Dari sini, dapat disimpulkan bahwa karakteristik umum mahasiswa yang mengalami dropout adalah:

>   Mahasiswa muda (<25 tahun), tidak menerima beasiswa, memiliki nilai akademik rendah, berasal dari keluarga dengan pendidikan orang tua yang terbatas, mengikuti kelas malam, dan mengalami kendala finansial.

Dengan pemahaman ini, pihak institusi dapat melakukan intervensi yang lebih terarah, seperti pemberian bantuan belajar, beasiswa berbasis risiko, pendampingan mahasiswa baru, serta konseling finansial untuk mengurangi angka dropout dan meningkatkan keberhasilan studi mahasiswa.

### Rekomendasi Action Items

1. Dominasi Dropout oleh Mahasiswa dengan Latar Pendidikan Tertentu
    - Insight: Beberapa kategori Previous_qualification memiliki lonjakan dropout yang tinggi.
    - Action Items:
        - Lakukan remedial/preparatory program bagi mahasiswa dari latar belakang pendidikan rendah atau non-akademik.
        - Pertimbangkan uji diagnostik awal semester untuk mahasiswa dari sumber latar belakang berisiko.

2. Banyak Dropout Tidak Memegang Beasiswa
    - Insight: Sebagian besar mahasiswa dropout tidak memegang beasiswa.
    - Action Items:
        - Evaluasi dan perluas program beasiswa untuk mencakup lebih banyak mahasiswa berisiko tinggi.
        - Uji coba program insentif berbasis progres akademik (misalnya, cicilan biaya kuliah tergantung performa).

3. Mahasiswa Malam Lebih Rentan Dropout
    - Insight: Persentase mahasiswa malam (evening) lebih kecil tapi dropout rate-nya tinggi.
    - Action Items:
        - Sediakan dukungan belajar fleksibel untuk mahasiswa malam, seperti rekaman kuliah atau kelas hybrid.
        - Telusuri kebutuhan khusus mahasiswa malam — misalnya, mereka juga bekerja.

4. Masalah Keuangan Terhubung ke Dropout
    - Insight: Mahasiswa yang memiliki tunggakan lebih banyak ditemukan di kelompok dropout.
    - Action Items:
        - Terapkan program konseling finansial di awal semester.
        - Tawarkan skema pembayaran cicilan ringan atau diskon berdasarkan kebutuhan.

5. Profil Orang Tua Tertentu Dominan di Dropout
    - Insight: Dropout sering terjadi di mahasiswa dengan orang tua berpendidikan rendah.
    - Action Items:
        - Tambahkan program mentoring atau pendampingan bagi mahasiswa generasi pertama.
    - Bangun komunitas support untuk mahasiswa dengan latar belakang keluarga kurang mendukung akademik.

6. Kinerja Akademik Mahasiswa Dropout Lebih Rendah
    - Insight: Rata-rata nilai mahasiswa dropout jauh lebih rendah.
    - Action Items:
        - Buat intervensi belajar awal untuk mahasiswa dengan nilai masuk rendah.
        - Gunakan sistem early warning berdasarkan penurunan nilai di semester 1.

7. Dropout Tinggi pada Mahasiswa Muda (<25 tahun)
    - Insight: Kelompok usia <20 dan 20–24 menyumbang mayoritas dropout.
    - Action Items:
        - Sediakan orientasi akademik dan personal skill development bagi mahasiswa baru.
        - Bangun program peer mentoring oleh senior dari program studi yang sama.