from PIL import Image
import matplotlib.pyplot as plt

def resize_to_pattern(input_path, output_path, target_size=(400, 103)):
    try:
        img = Image.open(input_path)

        resized_img = img.resize(target_size, Image.LANCZOS)

        resized_img.save(output_path, quality=95)

        print("✅ Image resized successfully!")
        print(f"📐 New Size: {resized_img.size}")
        print(f"📍 Saved to: {output_path}")
        plt.imshow(resized_img)
        plt.title("Resized Image")
        plt.axis("off")
        plt.show()

    except Exception as e:
        print("❌ Error:", e)
input_path = "C:/Users/Kousimon/OneDrive/Desktop/Data Scientist/Numpy/WhatsApp Image 2025-05-30 at 14.27.45_233f0cb1.jpg"
output_path = "C:/Users/Kousimon/OneDrive/Desktop/Data Scientist/Numpy/WhatsApp Image 2025-05-30 at 14.27.45_233f0cb1.jpg"

resize_to_pattern(input_path, output_path, target_size=(400, 103))
