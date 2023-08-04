# Driver Drowsiness Detection

![Driver Drowsiness Detection](/path/to/driver-drowsiness-detection.jpg)

## Introduction

Driver Drowsiness Detection is a Python-based application that uses computer vision techniques and facial landmarks to detect signs of drowsiness in a driver. The application continuously analyzes the driver's face through a webcam and alerts them if they show signs of drowsiness or fatigue.

## How to Use

1. Clone the repository: `git clone https://github.com/your-username/driver-drowsiness-detection.git`
2. Install the required dependencies: `pip install opencv-python dlib imutils numpy matplotlib python-vlc`
3. Download the shape predictor file `shape_predictor_68_face_landmarks.dat` and place it in the `Assets` folder.
4. Run the script: `python drowsiness_detection.py`
5. The program will use the webcam to detect the driver's face and eyes. The drowsiness level and yawn detection status will be displayed on the screen. If drowsiness is detected, an alarm will play (`focus.mp3`). If frequent yawning or signs of drowsiness persist, an extended alarm will play (`take_a_break.mp3`) and a web browser will open to search for nearby hotels.

## Requirements

- Python 3.x
- OpenCV
- Dlib
- Imutils
- Numpy
- Matplotlib
- VLC (Python bindings)
- Webbrowser (Python standard library)

## How it Works

The application works as follows:

1. The program uses a pre-trained facial landmark detector to locate and track the driver's eyes and mouth.
2. The Eye Aspect Ratio (EAR) is calculated for each eye, and the average EAR is used to determine the drowsiness level. If the average EAR falls below a certain threshold (`close_thresh`), it indicates that the driver's eyes are closing, suggesting drowsiness.
3. The program also checks for yawns. If the mouth open ratio exceeds a certain threshold, it is considered a yawn.
4. If signs of drowsiness are detected, an alert sound (`focus.mp3`) is played to wake the driver up and prompt them to pay attention to the road.
5. If drowsiness persists or the driver shows signs of fatigue, an extended alert sound (`take_a_break.mp3`) is played, and a web browser is opened to search for nearby hotels where the driver can take a break.

## Customization

You can adjust the following parameters to fine-tune the system:

- `frame_thresh_1`, `frame_thresh_2`, `frame_thresh_3`: Threshold values for determining drowsiness levels (number of consecutive frames with low EAR).
- `close_thresh`: Threshold value for detecting closed eyes (drowsiness).
- `map_counter`: The number of consecutive drowsy events required to trigger the web browser to open and search for nearby hotels.

## Note

Please note that this system is intended for educational purposes and should not be used as a substitute for professional drowsiness detection systems. Always ensure safety while driving and take breaks when needed to prevent fatigue-related accidents.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to use, modify, and distribute the code as per the terms of the MIT License.
