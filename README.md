# Drowsiness-Detection




This Python script uses computer vision to detect eyes and trigger an alarm when the user's eyes are closed for a certain duration. It's designed to help prevent drowsiness, especially useful for drivers or people working long hours.

## Features

- Real-time eye detection using OpenCV
- Alarm triggering when eyes are closed for a specified duration
- Audio alarm using Pygame
- Visual feedback with bounding boxes around detected eyes

## Prerequisites

- Python 3.x
- OpenCV (cv2)
- Pygame

## Installation

1. Clone the repository or download the script.

2. Install the required libraries:
pip install opencv-python pygame

3. Ensure you have a working webcam connected to your computer.

4. Place your alarm sound file (MP3 format) in the same directory as the script or update the path in the code:

```pygame.mixer.music.load("/path/to/your/alram_sound.mp3")```


Run the script:
python drowsiness.py

The webcam will start and begin detecting your eyes.
If your eyes are closed for more than 2 seconds (adjustable), an alarm will sound.
To stop the program, press 'q' while the webcam window is active.

## How It Works

The script uses Haar cascades for eye detection.
It checks if exactly two eyes are detected in each frame.
If eyes are not detected for a specified duration (default 2 seconds), it triggers the alarm.
The alarm stops when eyes are detected again.

## Customization

You can adjust the EYE_AR_CONSEC_FRAMES variable to change the duration of eye closure before the alarm triggers.
Modify the Haar cascade parameters in the detectMultiScale function for different detection sensitivity.

## Functions

initialize_pygame(): Sets up Pygame for audio playback.
play_alarm(): Starts playing the alarm sound.
stop_alarm(): Stops the alarm sound.

## Notes

Ensure good lighting for accurate eye detection.
The system may have false positives or negatives depending on lighting conditions and individual facial features.
This system is for experimental purposes and should not be relied upon for critical safety applications without further development and testing.

## Troubleshooting

If you encounter issues with webcam access, ensure no other applications are using the camera.
If the alarm sound doesn't play, check the file path and ensure the audio file is in a supported format.

License
# MIT
Contact
M.Lohith - `mlohith1338@gmail.com`

This README includes the properly formatted code block for loading the audio file. All other sections remain the same, providing a comprehensive guide for  drowsiness detection alarm system.
