# Belajar Dengan Jenius Python

## Penulis : Gun Gun Febrianza

## *Computer Organization*

Komputer terdiri dari sekumpulan *logical unit* :

### *Input Unit*

Terdiri dari sekumpulan **input device** untuk memproduksi informasi yaitu *keyboard, touchscreen, webcam, microphone, barcode scanner* dan *mouse devices.*

### *Output Unit*

Terdiri dari sekumpulan **output device** untuk menampilkan informasi yaitu *screen monitor, speaker, printer* hingga ke *oculus rift*. 

<img src="../../../assets/OculustRift.png" style="zoom:80%;" />

### *Memory Unit*

*Memory unit* seringkali disebut *memory, primary memory* atau **RAM (Random Access Memory).** Informasi yang tersimpan dalam *memory unit* bersifat **volatile**, artinya informasi akan hilang jika komputer dimatikan. 

*Memory unit* menjadi tempat untuk mempertahankan informasi setelah melalui *input unit*, sehingga langsung tersedia untuk diproses oleh *processor* jika dibutuhkan untuk memproduksi hasil pada *Ouput Unit*.

### *Central Processing Unit (CPU)*

**CPU** (**Central Processing Unit**) akan memberi sinyal pada *input unit* saat informasi dalam *memory unit* dibutuhkan untuk diproses melakukan suatu kalkulasi dan memberikan sinyal kepada *output unit* saat informasi dalam *memory unit* siap untuk digunakan pada *output device*.

#### Processor

Industri komputer menggunakan istilah terminologi **Central Processing Unit** pada awal tahun **1960**, namun secara tradisional terminologi **CPU** mengacu pada  sebutan untuk **processor**. 

Seluruh modern **CPU** adalah **Microprocessor** yang berarti mereka tersimpan di dalam sebuah **chip** tunggal **Integrated Circuit**. 

**Processor** adalah sebuah otak dari komputer yang mengendalikan operasi berbagai komponen dalam sistem komputer. Sebuah **CPU** membutuhkan dua hal yaitu program atau aplikasi dan data. 

#### *Arithmetic and Logic Unit (ALU)*

Fungsi dari *ALU* adalah untuk melakukan kalkulasi seperti penjumlahan, pengurangan, perkalian dan pembagian. 

*ALU* memiliki mekanisme untuk membuat keputusan yang dapat membuat komputer misal, membandingkan dua buah data dalam *memori unit* apakah data tersebut setara (*equal*) atau tidak. 

Kini ALU (*Arithmetic and Logic Unit*) dikembangkan sebagai *next logical unit* untuk *CPU*.

#### Von Neumann Architecture

Desain operasional dasar sebuah sistem komputer disebut dengan **architecture**. Seluruh arsitektur komputer yang ada saat ini tidak lepas dari seorang pioner komputer bernama **John von Neumann**. 

Dalam sebuah sistem **Von Neumann** terdapat tiga komponen utama yaitu **central processing unit (CPU)**, **physical memory**, dan **input** atau **output (IO)**. **Central Processing Unit** (**CPU**) akan menerima data dari **memory** dan **input**. 

Elemen kunci dari **Von Neumann Architecture (VNA)** adalah :

1. Data & Instruksi disimpan dalam bilangan biner (**binary**).

2. Data & Instruksi disimpan dalam main **memory**.

3. Instruksi diambil (**fetched**) dari **memory** satu persatu dalam satu waktu secara berurutan.

4. **Processor** melakukan **decode** pada instruksi dan mengeksekusinya sebelum mengambil instruksi selanjutnya.

5. Aktivitas ini terus dilakukan sampai tidak ada lagi instruksi yang tersedia.

Dalam **Von Neumann Architecture (VNA)** dalam sebuah **processor** terdapat 5 spesial **register** :

**1.**  **Program Counter (PC)**

Menyimpan **memory address** dari instruksi selanjutnya yang akan diambil dari **main memory**.

**2.**  **Memory Address Register (MAR)**

Menyimpan **memory address** dari instruksi saat ini yang sedang dieksekusi. 

**3.**  **Memory Buffer Register (MBR)**

Menyimpan data yang akan ditransfer menuju **main memory**.

**4.**  **Current Instruction Register (CIR)**

Menyimpan instruksi yang saat ini telah di decode dan di eksekusi.

**5.**  **Accumulator (ACC)**

Menyimpan data yang telah diproses, hasil dari sebuah komputasi. 

#### CPU Register

Fungsi dasar **CPU** adalah melakukan **fetch**, **decode**, dan **execute** setiap instruksi yang berada di dalam **Read-only Memory (ROM)** ataupun **Random Access Memory (RAM)**. **CPU** akan melakukan **fetch** data dari sebuah memori eksternal dan mengirimkanya kedalam internal memory yang disebut dengan **register**. 

**Register** adalah sebuah **high-speed memory** yang ada di dalam internal CPU. **Register** digunakan ***processor\*** untuk menyimpan sebuah hasil komputasi sementara yang ukurannya terbatas. Data yang tersimpan dapat berupa : 

**1.**  Alamat dari instruksi bahasa mesin selanjutnya yang akan dieksekusi.

**2.**  Instruksi bahasa mesin saat ini yang sedang di **decode**.

**3.**  Hasil komputasi.

#### Instruction Set Architecture (ISA)

Sebuah **CPU** memiliki kemampuan untuk memahami perintah yang disebut dengan **machine instruction** dan setiap **CPU** memiliki **instruction set architecture (ISA)** yang berbeda-beda. **Instruction Set Architecture** adalah spesifikasi formal sebuah CPU, bagaimana sebuah **CPU** berinteraksi dengan **memory**, dan kapabilitas **I/O**. 

#### Multi-core Processor

Kebanyakan komputer hari ini telah memiliki lebih dari satu *CPU* sehingga dapat melakukan banyak sekali operasi secara simultan. Sebuah **Multi-core processor** memiliki lebih dari satu *processor* dalam satu **IC Chip** tunggal. 

Sebagai contoh **dual-core processor** artinya terdapat dua *processor* dalam 1 *IC Chip* dan *quad-core* artinya terdapat 4 *processor* dalam **1** **IC Chip**.

### *Secondary Storage Unit*

Sebuah data atau program yang sudah tidak lagi aktif digunakan biasanya akan atau dapat disimpan kedalam *storage devices* seperti *hard drive*, sampai data tersebut dibutuhkan kembali. 

Informasi yang tersimpan di dalam *secondary storage device* bersifat persisten. Informasi tetap terjaga meskipun komputer dimatikan. Informasi yang dapat disimpan dalam *hard drives* dalam *dekstop* komputer bisa sangat besar melebihi 16 *Terabyte*. 

---------------------

