# /usr/bin/env python3
from os import path
from pathlib import Path

from moviepy.editor import *

HELP = """
Usage

    build_video.py video_path
    

Created by Xizuth
https://github.com/jalmx
Download from https://github.com/jalmx/build_template_video
"""


def generate_name(name_src: str):
    """
    Extract the name of video file
    """
    name = name_src.split(sep="/")[-1]
    name = name.split(sep=".")[0:-1]
    name = ".".join(name)

    return name


def sound_background(sound_path, duration_video, volume=0.5):
    """
    set sound loop for the time of all video
    """
    sound_bg = AudioFileClip(sound_path)
    sound_bg = afx.audio_loop(sound_bg, duration=duration_video)
    return sound_bg.volumex(volume)


def process_video(video_path, video_final, thumb_path, sound_path):
    clip_main = VideoFileClip(video_path)
    clip_final = VideoFileClip(video_final)
    clip_thumb = ImageClip(thumb_path, transparent=True)  # picture above screen

    result_video = CompositeVideoClip([clip_main, clip_thumb], size=clip_main.size).set_duration(
        clip_main.duration).fadeout(0.5)

    # sound_bg = AudioFileClip(sound_path).set_duration(result_video.duration).volumex(0.08)
    sound_bg = sound_background(sound_path, result_video.duration, volume=0.08)
    voice = clip_main.audio.volumex(2)

    sound_final = CompositeAudioClip([voice, sound_bg])

    result_video = result_video.set_audio(sound_final)

    final_clip = concatenate_videoclips([result_video, clip_final], method="compose")
    final_clip.write_videofile(f"{generate_name(video_path)}_final.mp4")


def main():
    if len(sys.argv) == 1:
        print("You should give a name of video o path from the video")
        exit(1)

    name_video = sys.argv[1]

    if not Path(name_video).is_file():
        print("Should be a video file")
        exit(1)

    video_path = path.abspath(Path(name_video))

    video_final = "final_video.mp4"  # video que se agrega al final
    thumb_path = "thumb-fs8.png"  # watermark
    sound_path = "song.mp3"  # cancion de fondo del video

    process_video(video_path, video_final, thumb_path, sound_path)


if __name__ == "__main__":
    main()
