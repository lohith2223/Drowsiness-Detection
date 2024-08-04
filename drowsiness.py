import cv2
import time
import pygame


def initialize_pygame():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(
            "/Users/lohithyadav/Desktop/dubbing/alram_sound.mp3")
        print("Pygame initialized and audio file loaded successfully.")
    except pygame.error as e:
        print(f"Error initializing Pygame or loading audio file: {e}")


def play_alarm():
    if not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)
        print("Playing alarm sound.")


def stop_alarm():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        print("Stopped alarm sound.")


# Initialize Pygame for playing alarm sound
initialize_pygame()

# Load the pre-trained Haar cascades for eye detection
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')

# Constants for determining eye closure
EYE_AR_CONSEC_FRAMES = 2  # Trigger alarm after 2 seconds of eye closure

# Start video capture
cap = cv2.VideoCapture(0)

# Initialize frame counters and timer
START_TIME = None
ALARM_ON = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    # Check if exactly two eyes are detected
    if len(eyes) == 2:
        if START_TIME is None:
            START_TIME = time.time()
        elif time.time() - START_TIME >= EYE_AR_CONSEC_FRAMES:
            if not ALARM_ON:
                ALARM_ON = True
                play_alarm()
                print("Triggering Phone Vibration")
    else:
        START_TIME = None
        if ALARM_ON:
            ALARM_ON = False
            stop_alarm()

    for (x, y, w, h) in eyes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Frame", frame)

    # Check if the user has pressed 'q' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pygame.mixer.quit()
