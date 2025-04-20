from PIL import Image, ImageDraw, ImageFont
import os


# Buka gambar dari folder input_images
image_path = "input_images/sample.jpg"
image = Image.open(image_path).convert("RGBA")

# Buat layer baru transparan untuk watermark
watermark_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(watermark_layer)

# Teks watermark
watermark_text = "© HPA IMG"

# (Optional) Gunakan font bawaan
# Jika kamu punya font TTF bisa gunakan: ImageFont.truetype("arial.ttf", 24)
font = ImageFont.truetype("fonts/arial.ttf", 36)

# Posisi watermark
bbox = draw.textbbox((0, 0), watermark_text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = image.width - text_width - 20 # 10px dari kanan
y = image.height - text_height - 20 # 10px dari bawah

# Tambahkan teks ke layer watermark
draw.text((x, y), watermark_text, font=font, fill=(255,255,255,128)) # 128 transparan setengah

# Gabungkan layer watermark dengan gambar asli
combined = Image.alpha_composite(image, watermark_layer)

# Simpan hasil
output_path = "Watermarked_images/sample_watermarked.png"
combined.save(output_path)

print("watermark berhasil ditambahkan")
# #tampilkan ukuran gambar
# print("Ukuran gambar : ", image.size)

# #tampilkan gambar (kalau di os-mu support)
# image.show()