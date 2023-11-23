from PIL import Image
import os

def compress_image(input_path, output_path, quality=30):
    comp_factor = 100 // quality

    try:
        with Image.open(input_path) as img:
            width, height = img.size
            new_size = (width//comp_factor, height//comp_factor)
            resized_image = img.resize(new_size)
            resized_image.save(output_path, quality=quality)

        print(f"Image compressed successfully and saved at: {output_path}")
        print(os.path.getsize(input_path), "--> ", os.path.getsize(output_path), " | ", int(os.path.getsize(output_path)/os.path.getsize(input_path) * 100) )
        print("\n\n")
    except Exception as e:
        print(f"Error compressing image: {e}")    

if __name__ == "__main__":
    for root, dirs, files in os.walk(r"data\Sample images"):
        for file in files: 
            compress_image(os.path.join(root, file), os.path.join(r"Result", file))