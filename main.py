import os
from PIL import Image
from moviepy.editor import VideoFileClip

supported_img_formats = ["gif", "jpg", "png", "tiff", "webp"]
supported_vid_formats = ['avi', 'mov', 'mp4','webm']
codecs = {
    'avi':'libxvid', 
    'mov':'libx264', 
    'mp4':'libx264',
    'webm':'libvpx',
}

def get_folder_size(folder_path):
    folder_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            folder_size += os.path.getsize(file_path)
    return folder_size

        
def compress_img(file_path, output_path, relative_path, file, quality):

    comp_factor = 100 // quality
    new_file_name = "compr_" + str(quality) + "_" + file
    storage_path = os.path.join(output_path, relative_path, new_file_name)

    try:
        with Image.open(file_path) as img:
            width, height = img.size
            new_size = (width//comp_factor, height//comp_factor)
            resized_image = img.resize(new_size)
            resized_image.save(storage_path, quality=quality)

        initial_size = os.path.getsize(file_path)
        final_size = os.path.getsize(storage_path)
        print(f"[Message] IMG: {file} | {int(final_size / initial_size * 100)}% compressed")
    except Exception as e:
        print(f"[ERROR]: {e}") 


def compress_vid(file_path, output_path, relative_path, file, quality):
    print("compressing vid")
    new_file_name = "compr_" + str(quality) + "_" + file
    storage_path = os.path.join(output_path, relative_path, new_file_name)

    try:
        codec = codecs[file.split('.')[-1]]
        video = VideoFileClip(file_path)
        video_resized = video.resize(round(quality/100, 2))
        video_resized.write_videofile(storage_path, codec=codec)
    except Exception as e:
        print("[ERROR]",e)


def compress_file(base_path, output_path, quality = 60):

    # Create a folder with the same name of input folder in result directory
    _, root_dir_name =  os.path.split(base_path)
    output_path = os.path.join(output_path, root_dir_name)
    try:
        os.mkdir(output_path)
    except Exception as e:
        print(f"[ERROR] {e}")

    # Iterate through the folder
    for root, dirs, files in os.walk(base_path):
        # print(root, " | ", dirs, " | ", files, end="\n\n")
        for dir in dirs:
            relative_path = os.path.relpath(root, base_path)
            try:
                os.mkdir(os.path.join(output_path, relative_path, dir))
                print(f"[MESSAGE] folder created {relative_path}/{dir}")
            except Exception as e:
                print(f"[ERROR] {e}")

        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(root, base_path) 

            if file.split(".")[-1] in supported_img_formats:
                compress_img(file_path, output_path, relative_path, file, quality)
            elif file.split(".")[-1] in supported_vid_formats:
                compress_vid(file_path, output_path, relative_path, file, quality)
            else:
                print(f"[WARNING] Unsupported file {file}")

    initial_folder_size = get_folder_size(base_path)
    final_folder_size = get_folder_size(output_path)

    print(f"[Message] {int(final_folder_size / initial_folder_size * 100)}% compressed")


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

    compress_file(r"C:\Users\Avinash.Dhakne\Desktop\Python-exe\Data-Compressor\data", r"C:\Users\Avinash.Dhakne\Desktop\Python-exe\Data-Compressor\Result", 20)
    # print(get_folder_size(r"C:\Users\Avinash.Dhakne\Desktop\Python-exe\Data-Compressor\data"))