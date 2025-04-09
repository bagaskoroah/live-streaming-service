# PacFlix: Video Streaming Service
PacFlix adalah sebuah layanan video streaming yang dibuat dengan Python berfokus pada pengelolaan jenis langganan (plan), benefit yang diperoleh setiap plan, serta sistem upgrade plan dan referral untuk pengguna baru.

# Tujuan Pengembangan Project
1. Membangun sistem manajemen langganan digital sederhana yang dapat melakukan tugas berupa:
   - Mensimulasikan pengelolaan plan, benefit, dan referral pengguna seperti yang dilakukan pada platform streaming modern.
   - Meningkatkan layanan plan
   - Menerapkan validasi referral untuk user baru
   - Menerapkan pemberian diskon berdasarkan durasi langganan.
2. Mengaplikasikan konsep OOP (Object-Oriented Programming) dalam konteks layanan pelanggan berbasis langganan.
3. Meningkatkan pemahaman tentang struktur data dictionary, pengolahan data dengan logika kondisional, serta penggunaan eksternal library seperti tabulate untuk representasi visual data yang lebih informatif.

# Deskripsi Program
Program ini merupakan simulasi sistem manajemen langganan layanan streaming PacFlix dengan menerapkan prinsip Object-Oriented Programming (OOP) dalam Python, program ini terdiri dari dua **kelas utama** dengan fungsi-fungsi yang merepresentasikan operasi umum pada platform streaming, seperti mengecek benefit langganan, upgrade plan, dan mendaftar dengan kode referral.

- Class 1: User

Kelas yang merepresentasikan pengguna yang sudah memiliki akun dan langganan aktif.

a. __init__(self, username, duration_plan, current_plan)
Inisialisasi objek User dengan nama, durasi langganan, dan jenis plan aktif.

b. check_benefit(self)
Menampilkan daftar lengkap benefit dari semua jenis plan (Basic, Standard, Premium).

c. check_plan(self, username)
Menampilkan detail plan dan daftar benefit sesuai dengan plan yang dimiliki pengguna tertentu.

d. upgrade_plan(self, current_plan, new_plan)
Melakukan proses upgrade plan jika memenuhi syarat tertentu seperti durasi langganan. Memberikan potongan harga jika berlaku.

- Class 2: NewUser

Kelas untuk pengguna baru yang belum berlangganan, memungkinkan memilih plan dan menggunakan kode referral.

a. __init__(self, username)
Inisialisasi objek NewUser dengan nama pengguna baru.

b. pick_plan(self, new_plan, code_referral)
Memilih jenis plan saat registrasi awal, dan mendapatkan potongan harga apabila referral code valid.

# Hasil Test Case

## Test Case 1: Mengecek benefit secara keseluruhan
Object => user_1 = User("Cahya", 24, "Standard Plan")
user_1.check_benefit()

![image](https://github.com/user-attachments/assets/21f06ae7-f402-4ecb-9053-90b0c9d6488c)

## Test Case 2: Mengecek benefit user berdasarkan input username
Object => user_1 = User("Cahya", 24, "Standard Plan")
user_1.check_plan(user_1.username)

![image](https://github.com/user-attachments/assets/ea39f245-83b5-4d7a-b535-81a8636da100)

## Test Case 3: Meningkatkan level plan
Object => user_1 = User("Cahya", 24, "Standard Plan")
user_1.upgrade_plan(user_1.current_plan, "Premium Plan")

![image](https://github.com/user-attachments/assets/bf63bb9e-aa02-4419-95e2-6e8b67b5079e)

## Test Case 4: Mengimplementasikan referral bagi user baru
faizal = NewUser("faizal_icikiwir")
faizal.pick_plan("Basic Plan", "shandy-2134")

![image](https://github.com/user-attachments/assets/77aacdb9-717a-4383-8978-3aaa7bee1ac9)

Apabila referral code tidak tersedia pada database tersimpan di dictionary:
faizal.pick_plan("Basic Plan", "indira-22gs")

![image](https://github.com/user-attachments/assets/f5126877-8b67-413b-9f70-032c273dd773)



# Saran Pengembangan
1. Membuat User Interface untuk layanan PacFlix agar lebih user-friendly.
2. Menyimpan data pengguna ke dalam suatu database.
3. Sistem registrasi dengan melalui input terminal sehingga program lebih dinamis.

# Kontak
Created by Bagaskoro Adi Hutomo

Email: bagaskoroah@email.com

Feel free to discuss and to pull request!
