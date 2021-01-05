# Belajar Dengan Jenius Python

## Penulis : Gun Gun Febrianza

## *Operating System*

Sistem operasi adalah sekumpulan program yang mengendalikan perangkat keras komputer dan sumber perangkat lunak yang ada di dalamnya. 

<img src="../../../assets/OperatingSystem.png" style="zoom:55%;" />

Setiap sistem operasi juga menyediakan **interface** :

1. **Graphical User Interface** (**GUI**)

2. **Command-line Interface** (**CLI**)

3. **Mobile User Interface (Mobile UI)**

<img src="../../../assets/UserInterface.png" style="zoom:55%;" />



### Processor Management

Pada sistem operasi kita dapat melakukan **multitasking** yaitu mengeksekusi lebih dari satu program sekaligus (simultan). Sebagai contoh kita dapat membuka program untuk mengelola dokumen, melakukan **streaming** musik dan program lainnya.

**Multitasking** dapat dilakukan pada :

1. Modern **Operating System**

2. Sistem komputer memiliki cukup memori untuk menyimpan data pada **primary memory** (**RAM**)

### Memory Management

**Management Memory** dilakukan untuk memastikan sekumpulan program dapat berjalan dalam satu waktu. Salah satu metode **memory management** disebut dengan **paging**. Sebuah **memory** dapat direcah menjadi sekumpulan block dengan ukuran **fixed** yang disebut dengan **page**.

Pada **Modern Operating System** ukuran dari **memory pages** sebesar 4 **kilobytes** (KB). Ketika suatu program berjalan, maka **memory** yang dibutuhkan untuk menjalankan program tersebut akan dibuat.

Sistem operasi akan menentukan alokasi jumlah **pages** yang dibutuhkan untuk menjalankan program tersebut. Ketika suatu program telah selesai digunakan maka alokasi **pages** akan dibebaskan kembali agar dapat digunakan oleh program lainnya.

<img src="../../../assets/Pages1.png" style="zoom:85%;" />

Pada ilustrasi **page** di atas program A membutuhkan 2 **page** yaitu **page** 0 dan 1 dan program B membutuhkan 3 **page** yaitu **page** 2, **page** 3 dan **page** 4. 

Jika program A selesai dan kita mengeksekusi program C yang membutuhkan 3 ****page**** saat program B masih berjalan, maka **page** 0, **page**  1 dan **page** 6 akan digunakan oleh program C seperti pada gambar di bawah ini :

<img src="../../../assets/Pages2.png" style="zoom:85%;" />

Setiap **pages** yang digunakan oleh program bersifat **contiguos**, dapat berurutan atau acak. Sistem operasi akan menentukan **page** mana yang akan digunakan dan membaca kembali data ketika dibutuhkan.



### Input or Output (I/O) Management 

Perangkat **input** dan **output** disebut dengan **peripherals**, sekumpulan perangkat keras yang terhubung pada sistem komputer. Sistem operasi dapat berinteraksi dengan **peripherals** dengan memanggil sekumpulan program yang ada di dalam **device driver**.

### *A*pplication Management

Sistem operasi memiliki sebuah **Application Programming Interface** (API) yang dapat diprogram dan digunakan oleh suatu aplikasi dan **hardware** untuk berinteraksi dengan sistem operasi itu sendiri. 

### *S*ecurity Management

Sistem operasi memiliki manajemen sistem keamanan dasar seperti :

1. Manajemen **user**.

2. Manajemen akses level untuk setiap **user**.

3. **Auditing logs** untuk setiap **file** yang dibuat, diakses, diubah dan dihapus oleh setiap **user**.

### Operating System Classification

Terdapat banyak sekali sistem operasi yang ada hari ini mulai dari sistem operasi *Unix*, *Windows*, *Linux*, OS X dan sebagainya. 

Masing masing sistem operasi memiliki kelebihan dan kekurangan. Saat ini sistem operasi telah didominasi oleh 32 Bit dan 64 Bit *Operating System*. 

Pada sistem operasi 32 bit penggunaan kapasitas RAM dibatasi sampai 4096 MB RAM, 2^32 = 4,294,967,296 *bytes* untuk setiap *process*. Pada sistem operasi 64 bit penggunaan kapasitas RAM dibatasi sampai 16 Exabytes 2^64 = 18,446,744,073,709,551,616 *bytes*. 

-------

