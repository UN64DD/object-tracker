# object-tracker

Real-time object tracking using OpenCV's CamShift algorithm.

## Usage

```bash
python track.py                     # use webcam
python track.py -v path/to/video.mp4  # use video file
```

## Controls

- Press **i** — enter ROI selection mode, then click 4 corner points around the object
- Press **q** — quit

## How it works

1. Select a region of interest (ROI) by clicking 4 points around the object
2. An HSV histogram is computed from the selected region
3. CamShift (Continuously Adaptive Mean Shift) tracks the object frame by frame using back-projection
4. The tracked object is outlined with a green polygon
