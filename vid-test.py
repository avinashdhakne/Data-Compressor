from moviepy.editor import *

def compress_video(input_path, output_path, curr_codecs, quality = 50):
    # Importing the module
    if curr_codecs == '':
        print(input_path)
        return
    try:
        video = VideoFileClip(input_path)
        video_resized = video.resize(round(quality/100, 2))
        video_resized.write_videofile(output_path, codec=curr_codecs)
    except Exception as e:
        print("ERROR",e,end="\n\n\n\n")

if __name__ == "__main__":

    codecs = {
    "mp4":"libx264",
    "ogv":"libtheora",
    "webm":"libvpx",
    "ogg":"libvorbis",
    "mp3":"pcm_s16le",
    "wav":"libvorbis",
    "m4a":"libfdk_aac",
    "avi":"",
    "mov":"",
    "wmv":"",
    "mkv":""
    }
    
    for root, dirs, files in os.walk(r"data\Sample videos"):
        for file in files: 
            compress_video(os.path.join(root, file), os.path.join(r"Result", file), codecs[file.split(".")[-1]])
            