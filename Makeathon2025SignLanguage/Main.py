import numpy as np
import mediapipe as mp
from Function import *
import time
import serial
from deep_translator import GoogleTranslator
import speech_recognition as sr
import sys
from gtts import gTTS
import os
import locale
import pygame
import atexit
import threading

langCode = "zh-CN"
langName = "Chinese"

# Set the default encoding to UTF-8 (for Python 3.x)
sys.stdout.reconfigure(encoding='utf-8')

# Check the system's current locale
print("Current Locale:", locale.getdefaultlocale())
# Initialize pygame mixer for audio playback
pygame.mixer.init()
# Create translations folder if it doesn't exist
translations_folder = "translations"
if not os.path.exists(translations_folder):
    os.makedirs(translations_folder)

# Function to generate speech


def generate_speech(language, translated_text):
    language_to_accent_map = {
        'English': 'en',
        'Spanish': 'es',
        'Chinese': 'zh-CN',
        'Hindi': 'hi',
    }
    accent = language_to_accent_map.get(language, 'en')  # Default to English (US)

    # Get the next available file number for the MP3 file
    existing_files = os.listdir(translations_folder)
    mp3_files = [f for f in existing_files if f.endswith('.mp3')]
    file_number = len(mp3_files) + 1
    temp_filename = os.path.join(translations_folder, f"temp_audio_{file_number}.mp3")

    # Create speech using gTTS
    tts = gTTS(text=translated_text, lang=accent, slow=False)
    tts.save(temp_filename)  # Save speech to a file

    return temp_filename

# Function to play the audio


def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Wait for audio to finish playing

# Function to run TTS in a separate thread to avoid freezing


def speak_translated_text(language, translated_text):
    if not translated_text:
        print("No text to speak.")
        return

    def run_speech():
        file_path = generate_speech(language, translated_text)  # Generate speech file
        play_audio(file_path)  # Play the generated speech

    # Create and start a new thread
    threading.Thread(target=run_speech, daemon=True).start()

# Function to remove all MP3 files in the translations folder when the program exits


def cleanup_mp3_files():
    arduino.write('~'.encode())
    try:
        # Stop playback and unload any loaded music file
        pygame.mixer.music.stop()
        pygame.mixer.quit()

        for mp3_file in os.listdir(translations_folder):
            if mp3_file.endswith(".mp3"):
                file_path = os.path.join(translations_folder, mp3_file)
                os.remove(file_path)

        print("Cleanup complete: All MP3 files deleted.")
    except Exception as e:
        print(f"Error cleaning up files: {e}")



recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen_and_translate():
    print(f"Listening for a response in {langName}...")
    
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds
            print("Processing response...")
            chinese_text = recognizer.recognize_google(audio, language=langCode)
            print(f"Detected Speech ({langName}): {chinese_text}")

            # Translate Chinese to English
            translated_response = GoogleTranslator(source=langCode, target="en").translate(chinese_text)
            print(f"Translated Response (English): {translated_response}")
            speak_translated_text("English", translated_response)
            arduino.write(translated_response.encode())
            time.sleep(5)
            arduino.write('~'.encode())

        except sr.UnknownValueError:
            print("Sorry, couldn't understand the response.")
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")




# Set the cleanup function to run when the program is closed
atexit.register(cleanup_mp3_files)

last_update = time.time()
last_letter = None
true_last_letter = None
wrist_data = []
wrist_data_y = [] 
stored_phrase = ''


def check_for_gestures():
    global wrist_data, true_last_letter, stored_phrase
    if true_last_letter == '' and wrist_data:
        xmax = max(wrist_data, key=lambda x: x[0])
        xmin = min(wrist_data, key=lambda x: x[0])
        ymax = max(wrist_data_y, key=lambda y: y[0])
        ymin = min(wrist_data_y, key=lambda y: y[0])
        diff = xmax[0] - xmin[0]
        diff2 = ymax[0] - ymin[0]
        swipe_threshold_send = .15
        swipe_threshold_back = .3
        swipe_threshold_y = .2
        
        #send
        if diff > swipe_threshold_send and diff2 > swipe_threshold_send:
            timediff = xmax[1] - xmin[1]
            timediff2 = ymax[1] - ymin[1]
            if timediff < 0 and timediff2 > 0:
                print("Right down Swipe")
                translated_text = GoogleTranslator(source="en", target=langCode).translate(stored_phrase)
                print(f"Translated Text: {translated_text}")
                speak_translated_text(langName, translated_text)
                arduino.write('~'.encode())
                stored_phrase = ""
                listen_and_translate()
            wrist_data.clear()

        #backspace
        if diff > swipe_threshold_back:
            timediff = xmax[1] - xmin[1]        
            if timediff > 0:
                print("Left Swipe")
                speak_translated_text("English", "Backspace")
                arduino.write('*'.encode())
                stored_phrase = stored_phrase[:-1]
            wrist_data.clear()
            
        if diff2 > swipe_threshold_y:
            timediff = ymax[1] - ymin[1]
            if timediff < 0:
                print("Up Swipe - Add space")
                speak_translated_text("English", "Space")
                arduino.write(' '.encode())
                stored_phrase = stored_phrase + " "
            # else:
            #     print("Down Swipe")
                # arduino.write(' '.encode())
                # stored_phrase = stored_phrase + ""
            wrist_data_y.clear()


arduino = serial.Serial(port='COM7', baudrate=9600, timeout=1)  # Adjust COM port as needed
# arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Adjust baud rate if necessary
time.sleep(2)  # Allow connection to establish

holy_hands = mp.solutions.hands
cap = cv.VideoCapture(0)


def push_letter(letter):
    global stored_phrase
    arduino.write(letter.encode())
    stored_phrase += letter
    print(letter)


with holy_hands.Hands(max_num_hands=1) as hands:
    index_cord = []  # This list stores values for pointer
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        # To improve performance, optionally mark the image as not writeable
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

        # Images shape
        imgH, imgW = image.shape[:2]
        string = ''
        hand_cordinate = []
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # swipe gestures
                wrist = hand_landmarks.landmark[0]
                wrist_data.append((wrist.x, time.time()))
                wrist_data_y.append((wrist.y, time.time()))
                
                current_time = time.time()
                wrist_data = [i for i in wrist_data if current_time - i[1] < 2]
                wrist_data_y = [i for i in wrist_data_y if current_time - i[1] < 2]

                check_for_gestures()

                # Get Hand Cordinates (HC values)
                for index, landmark in enumerate(hand_landmarks.landmark):
                    x_cordinate, y_cordinate = int(landmark.x * imgW), int(landmark.y * imgH)
                    hand_cordinate.append([index, x_cordinate, y_cordinate])
                hand_cordinate = np.array(hand_cordinate)
                # Working on image
                string = persons_input(hand_cordinate)
                image = get_fram(image, hand_cordinate, string)
        # check how long it has been since letter changed
        if string.strip() != last_letter:
            last_update = time.time()
            true_last_letter = string.strip()
            if string.strip():
                last_letter = string.strip()
        if time.time() - last_update > 1:
            push_letter(last_letter)
            speak_translated_text("English", last_letter)
            last_update = time.time()
        # For pointer
        if string == " D":
            index_cord.append([15, hand_cordinate[8][1], hand_cordinate[8][2]])
        if string == " I" or string == " J":
            index_cord.append([15, hand_cordinate[20][1], hand_cordinate[20][2]])
        for val in index_cord:
            image = cv.circle(image, (val[1], val[2]), val[0], (255, 255, 255), 1)
            val[0] = val[0] - 1
            if val[0] <= 0:
                index_cord.remove(val)
        # Flip the image horizontally for a selfie-view display.
        cv.imshow('Sign Language detection', cv.flip(image, 1))

        if cv.waitKey(5) & 0xFF in [ord('x'), ord('q')]:
            break
cap.release()

arduino.close()
