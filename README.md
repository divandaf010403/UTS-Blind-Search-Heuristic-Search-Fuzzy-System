# Kecerdasan Buatan - AI-Mitra

## Identitas
**Nama:** [Divanda Firdaus]  
**NIM:** [32602500023]  
**Mata Kuliah:** Kecerdasan Buatan

## Deskripsi Tugas

Repository ini berisi implementasi dari tiga komponen utama mata kuliah Kecerdasan Buatan:

1. **Blind Search** (2 algoritma): DFS dan UCS
2. **Heuristic Search** (1 algoritma): A*
3. **Fuzzy Logic System** untuk sistem tip restoran

## Struktur File

```
├── README.md                 # File penjelasan ini
├── graph_data.py             # Data sumber terpusat untuk algoritma search
├── dfs.py                    # Implementasi Depth-First Search
├── ucs.py                    # Implementasi Uniform Cost Search
├── astar.py                  # Implementasi A* Search
└── fuzzy_tip_system.py       # Implementasi Sistem Fuzzy Logic untuk Tip
```

## Data Sumber Terpusat

### [`graph_data.py`](graph_data.py) - Centralized Graph Data

File ini berisi data graf yang digunakan oleh semua algoritma search untuk konsistensi data:

**Data yang tersedia:**
- **Unweighted Graph** - untuk DFS
- **Weighted Graph** - untuk UCS dan A*
- **Heuristics Data** - untuk A*
- **Grid Data** - untuk contoh A* grid-based
- **Test Nodes** - Start (A) dan Goal (I)

**Keuntungan:**
- Konsistensi data across semua algoritma
- Mudah dimodifikasi dan dikelola
- Centralized source of truth

## 1. Blind Search Algorithms

### 1.1 Depth-First Search (DFS) - [`dfs.py`](dfs.py)

DFS adalah algoritma pencarian yang menjelajahi sebanyak mungkin di setiap cabang sebelum kembali (backtracking).

**Fitur:**
- Implementasi iteratif menggunakan stack
- Implementasi rekursif
- Menggunakan data terpusat dari [`graph_data.py`](graph_data.py)
- Menampilkan graf data yang digunakan

**Cara menjalankan:**
```bash
python dfs.py
```

**Hasil:** Path dari A ke I: `['A', 'C', 'F', 'I']`

### 1.2 Uniform Cost Search (UCS) - [`ucs.py`](ucs.py)

UCS adalah algoritma pencarian yang memperhitungkan biaya (cost) dari setiap jalur dan selalu memilih jalur dengan biaya terendah.

**Fitur:**
- Menggunakan priority queue untuk efisiensi
- Mengembalikan jalur optimal dengan biaya terendah
- Menggunakan data terpusat dari [`graph_data.py`](graph_data.py)
- Menampilkan graf berbobot dan semua kemungkinan jalur

**Cara menjalankan:**
```bash
python ucs.py
```

**Hasil:** Jalur optimal A→C→F→G→I dengan total cost 7

## 2. Heuristic Search Algorithm

### 2.1 A* (A-Star) Search - [`astar.py`](astar.py)

A* adalah algoritma pencarian yang menggunakan fungsi heuristik untuk memperkirakan biaya dari node saat ini ke tujuan.

**Fitur:**
- Menggunakan fungsi f(n) = g(n) + h(n)
- Support untuk Euclidean dan Manhattan distance
- Menggunakan data terpusat dari [`graph_data.py`](graph_data.py)
- Contoh implementasi pada graf dan grid

**Cara menjalankan:**
```bash
python astar.py
```

**Hasil:** Jalur optimal A→C→F→G→I dengan total cost 7

## 3. Fuzzy Logic System for Restaurant Tip

### 3.1 Sistem Fuzzy Tip Restoran - [`fuzzy_tip_system.py`](fuzzy_tip_system.py)

Sistem ini menghitung persentase tip berdasarkan kualitas makanan dan pelayanan menggunakan logika fuzzy.

**Spesifikasi Sistem:**

**Variabel Input:**
- **Food Quality** (0-10): Bad (0,0,5), Good (5,10,10)
- **Service Quality** (0-10): Poor (0,0,5), Excellent (5,10,10)

**Variabel Output:**
- **Tip Percentage** (0-20): Low (0,0,10), High (10,20,20)

**Aturan Fuzzy:**
1. IF Service is Poor OR Food is Bad THEN Tip is Low
2. IF Service is Excellent AND Food is Good THEN Tip is High

**Proses Fuzzy Logic:**
1. **Fuzzification:** Mengubah input crisp menjadi nilai keanggotaan fuzzy
2. **Rule Evaluation:** Menerapkan aturan fuzzy untuk mendapatkan output fuzzy
3. **Defuzzification:** Mengubah output fuzzy menjadi nilai crisp menggunakan metode centroid

**Cara menjalankan:**
```bash
python fuzzy_tip_system.py
```

## Hasil Test Case

**Soal:** Hitung berapa persen Tip jika Food Quality = 7 dan Service Quality = 3

**Hasil:** 4.13%

**Proses Perhitungan:**
1. **Fuzzification:**
   - Food Quality 7: Bad=0.000, Good=0.400
   - Service Quality 3: Poor=0.400, Excellent=0.000

2. **Rule Evaluation:**
   - Rule 1 (Service Poor OR Food Bad): max(0.400, 0.000) = 0.400
   - Rule 2 (Service Excellent AND Food Good): min(0.000, 0.400) = 0.000

3. **Output Memberships:**
   - Low: 0.400
   - High: 0.000

4. **Defuzzification (Centroid):** 4.13%

## Tambahan Test Cases

| Food Quality | Service Quality | Tip (%) |
|-------------|----------------|---------|
| 2           | 2              | 3.77    |
| 8           | 8              | 16.23   |
| 5           | 5              | 0.00    |
| 9           | 1              | 3.50    |
| 1           | 9              | 3.50    |

## Cara Menjalankan Semua Program

1. Pastikan Python terinstal di sistem Anda
2. Clone atau download repository ini
3. Jalankan setiap file secara individual:

```bash
# Data terpusat (opsional, untuk melihat graf data)
python graph_data.py

# Blind Search Algorithms
python dfs.py
python ucs.py

# Heuristic Search Algorithm
python astar.py

# Fuzzy Logic System
python fuzzy_tip_system.py
```

## Perbandingan Hasil Algoritma Search

Dengan data graf yang sama dari A ke I:

| Algoritma | Jalur Ditemukan | Cost | Karakteristik |
|-----------|----------------|------|---------------|
| DFS | A→C→F→I | - | Tidak mempertimbangkan bobot |
| UCS | A→C→F→G→I | 7 | Jalur dengan cost minimum |
| A* | A→C→F→G→I | 7 | Jalur optimal dengan heuristik |

## Kesimpulan

Semua implementasi telah berhasil dibuat sesuai dengan persyaratan tugas:

1. ✅ **DFS** - Algoritma blind search dengan pendekatan depth-first
2. ✅ **UCS** - Algoritma blind search dengan pertimbangan biaya
3. ✅ **A*** - Algoritma heuristic search dengan fungsi heuristik
4. ✅ **Fuzzy Logic System** - Sistem lengkap untuk perhitungan tip restoran

Sistem fuzzy logic berhasil menghitung tip sebesar **4.13%** untuk input Food Quality = 7 dan Service Quality = 3 sesuai dengan test case yang diberikan.

---

**Catatan:** Ganti `[Your Name]` dan `[Your NIM]` dengan identitas Anda yang sebenarnya.