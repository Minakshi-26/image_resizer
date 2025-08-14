import os
from PIL import Image

input_folder = os.path.join(os.getcwd(), "images")
output_folder = os.path.join(os.getcwd(), "resized")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

try:
    width = int(input("Enter new width: "))
    height = int(input("Enter new height: "))
    new_size = (width, height)
except ValueError:
    print("Invalid input! Using default size 800x600.")
    new_size = (800, 600)

convert_format = input("Convert all images to (jpg/png/jpeg) or leave blank: ").lower()
if convert_format not in ["jpg", "png", "jpeg", ""]:
    print("Invalid format! Original format will be kept.")
    convert_format = ""

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(input_folder, filename)
        try:
            img = Image.open(img_path)

            img.thumbnail(new_size)

            name, ext = os.path.splitext(filename)
            if convert_format:
                save_path = os.path.join(output_folder, f"{name}.{convert_format}")
            else:
                save_path = os.path.join(output_folder, filename)

            img.save(save_path)
            print(f"{filename} resized and saved.")
        except Exception as e:
            print(f"Skipping {filename}: {e}")

print("All images processed successfully!")

