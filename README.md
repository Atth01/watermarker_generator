# Image Watermarker

Project ini adalah aplikasi untuk menambahkan watermark berupa teks pada gambar. Gambar yang sudah diberi watermark akan disimpan di folder `watermarked_images/`.

## Fitur

- Input teks watermark langsung dari terminal.
- Watermark otomatis ditambahkan ke semua gambar di folder `input_images/`.
- Gambar hasil watermark disimpan di folder `watermarked_images/`.

## Instalasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/username/image-watermarker.git
   cd image-watermarker
2. Install dependencies:
   pip install -r requirements.txt
3. Siapkan font .ttf yang kamu inginkan, simpan di folder fonts/.
4. Tempatkan gambar yang ingin diberi watermark di folder input_images/.
5. Jalankan, python main.py (untuk versi tanpa input) dan main1.py (versi dengan bisa input)
6. Masukkan teks watermark saat diminta. Hasil gambar dengan watermark akan disimpan di watermarked_images/.
