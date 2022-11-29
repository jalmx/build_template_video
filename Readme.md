## Generate a video template

Generate a video with a song background and mark water with a final video to close

```
|-- Video main -------- + video final
<----- watermark ----->
<--song background --->
```

## Usage

```commandline
build_video.py video_path
```

Video result is `video_final.[ext]`


## Init project

```commandline
python3 -m venv venv
pip3 install -r requimerents.txt
```

## Requirements

```
moviepy
```