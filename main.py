import os
from PIL import Image
from moviepy.editor import VideoFileClip

supported_img_formats = ['.ico', ".gif", ".jpg", ".png", ".tiff", ".webp"]
supported_vid_formats = ['.avi', '.mov', '.mp4','.ogg','.webm','.wmv','.mkv']

def compress_img(img_path, output_path, compression_factor, base_path):

    image_name = os.path.basename(img_path)
    output_name = "COMP_" + compression_factor + "_" + image_name

    relative_path = os.path.relpath(img_path, base_path)
    output_path = os.path.join(output_path, relative_path, output_name)

    try: 
        initial_img_size = os.path.getsize(img_path)
    except Exception as e:
        print(f"[ERROR] {e}")

    try: 
        with Image.open(img_path) as img:
            img.save(output_path, quality=compression_factor)
        output_img_size = os.path.getsize(output_path)

        print(f"[MESSAGE] compressed IMG: {output_path} | {initial_img_size} --> {output_img_size} | final size: {output_img_size/initial_img_size * 100}%")
    except Exception as e:
        print(f"[ERROR] {e}")

def compress_vid(vid_path, output_path, compression_factor, base_path):
    video_name = os.path.basename(vid_path)
    output_name = "COMP_" + compression_factor + "_" + video_name

    relative_path = os.path.relpath(vid_path, base_path)
    output_path = os.path.join(output_path, relative_path, output_name)

    try: 
        initial_vid_size = os.path.getsize(vid_path)
    except Exception as e:
        print(f"[ERROR] {e}")

    try:
        clip = VideoFileClip(vid_path)
        clip = clip.resize(compression_factor)
        clip.write_videofile(video_name)
        output_vid_size = os.path.getsize(output_path)
        print(f"[MESSAGE] compressed VID: {video_name} | {initial_vid_size} --> {output_vid_size} | final size: {output_vid_size/initial_vid_size * 100}%")
    except Exception as e:
        print(f"[ERROR] {e}")

def compress_file(input_path, output_path):

    # Create a folder with the same name of input folder in result directory
    _, root_dir_name =  os.path.split(input_path)
    output_path = os.path.join(output_path, root_dir_name)
    os.mkdir(output_path)

    # Iterate through the folder
    for root, dirs, files in os.walk(input_path):
        # print(root, " | ", dirs, " | ", files, end="\n\n")
        for dir in dirs:
            relative_path = os.path.relpath(root, input_path)
            try:
                os.mkdir(os.path.join(output_path, relative_path, dir))
                print(f"[MESSAGE] folder created {relative_path}")
            except Exception as e:
                print(f"[ERROR] {e}")

if __name__ == "__main__":
    # str = r"C:\Users\Avinash.Dhakne\Desktop\Python-exe\Data-Compressor\\['file_example_JPG_1MB', 'jpg'].jpeg"
    # print(os.path.basename(str))
    # print(str.split("\\")[-1])
    # print(os.path.split(str))
    # print(os.path.splitext(str))

    # compress_file(r"C:\Users\Avinash.Dhakne\Desktop\Python-exe\Data-Compressor")


    # Example usage
    # base_path = "/path/to/your/base/directory"
    # target_folder = "/path/to/your/target/folder"

    # relative_path =  os.path.relpath(r"C:\Users\Avinash.Dhakne\Desktop\Python-exe\Data-Compressor", r"C:\Users\Avinash.Dhakne\Desktop")

    # print("Relative Path:", relative_path)
    # print(os.path.join(r"C:\Users\Avinash.Dhakne\Desktop\Python-exe\Data-Compressor", relative_path, "test.txt"))

    compress_file(r"C:\Users\Avinash.Dhakne\Desktop\Python-exe\Data-Compressor\data", r"C:\Users\Avinash.Dhakne\Desktop\Python-exe\Data-Compressor\Result")