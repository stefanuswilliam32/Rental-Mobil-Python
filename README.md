## Latar Belakang
Sistem Rental Mobil ini adalah aplikasi berbasis Python yang dirancang untuk mengelola penyewaan mobil. Aplikasi ini memiliki dua fungsi utama, yaitu sebagai antarmuka untuk pengguna yang ingin menyewa mobil dan sebagai alat bagi admin untuk mengelola armada mobil. Sistem ini menggunakan login khusus untuk admin yang dilindungi oleh kata sandi, yang memungkinkan admin mengakses berbagai fitur manajemen.

Database mobil pada sistem ini disimpan dalam bentuk dictionary, di mana setiap mobil memiliki atribut seperti model mobil, jenis transmisi (manual atau otomatis), warna, jenis bahan bakar, harga sewa per hari, status sewa (apakah mobil sedang disewa atau tersedia), serta jumlah hari mobil tersebut disewa. Untuk mempermudah pemahaman dan pengelolaan data, informasi mobil ditampilkan dalam bentuk tabel menggunakan tabulate.

Setelah admin berhasil login dengan kata sandi yang benar (default adalah Admin123), sistem akan menampilkan pilihan untuk melihat daftar mobil yang tersedia maupun yang sedang disewa. Admin juga dapat menambahkan mobil baru atau memperbarui informasi mobil yang ada, serta mengelola status sewa mobil. Fitur-fitur ini memudahkan pengelolaan armada mobil dan memastikan bahwa penyewaan dapat dilakukan dengan efisien.


### - Admin
Beberapa fitur yang dapat dijalankan sebagai admin yaitu
  -  Menamipilkan data semua atau berdasarkan primary key (plat mobil atay no Telpon customer).
  -  Menambah data mobil.
  -  Menghapus data mobil dan customer.
  -  Mengubah status mobil yang sendang dipinjam.
  -  Mematikan sistem.

### - Customer
Beberapa fitur yang dapat dijalankan sebagai customer yaitu
  - Membuat akun.
  - Login.
  - Melihat dan merubah data akun.
  - Mengganti no telpon dan password.
  - Melihat data mobil yang dapat difiler berdasarkan nama mobil, harga, transmisi, bahan bakar.
  - Meminjam mobil.
  - Melihat data mobil yang customer sedang pinjam.
