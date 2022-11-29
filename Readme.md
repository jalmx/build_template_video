## Generate a video template

Generate a video with a song background and mark water with a final video to close

```
|-- Video main -------- + video final
<----- watermark ----->
<--song background --->
```

You need to change the code for next variables, for yours assets in `build_video.py`

```python
video_final = "final_video.mp4"  # video que se agrega al final
thumb_path = "thumb-fs8.png"  # watermark
sound_path = "song.mp3"  # cancion de fondo del video
```
## Usage

```commandline
build_video.py video_path
```

Video result is `[video_name]_final.[ext]`


## Init project

```commandline
python3 -m venv venv
pip3 install -r requimerents.txt
```

## Requirements

```
moviepy
```