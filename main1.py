from PIL import Image, ImageDraw, ImageFont
import os

# === Input watermark form user ===
watermark_text = input("Input your text for watermark : ")

# === Load font ===
font_path = "fonts/SpecialGothicExpandedOne-Regular.ttf"
font_size = 36
font = ImageFont.truetype(font_path, font_size)

# === Folder input/output ===
input_folder = "input_images"
output_folder = "watermarked_images"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# === Proses semua gambar di folder ===
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png",".jpg",".jpeg")):
        # Open image
        images_path = os.path.join(input_folder, filename)
        image = Image.open(images_path).convert("RGBA")

        # Buat layer watermark
        watermark_layer = Image.new("RGBA", image.size,  (255,255,255,0))
        draw = ImageDraw.Draw(watermark_layer)

        # Hitung posisi watermark
        bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = image.width - text_width - 20
        y = image.height - text_height - 20

        # Tambahkan teks watermark
        draw.text((x, y), watermark_text, font=font, fill=(255,255,255,128))

        # Gabungkan dan simpan
        combined = Image.alpha_composite(image, watermark_layer)
        output_path = os.path.join(output_folder, f"watermarked_{filename.split('.')[0]}.png")
        combined.save(output_path)

        print(f"✅ Watermark berhasil: {filename}")