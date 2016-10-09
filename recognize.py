#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import subprocess
# import os

def recognize():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("adjusting threshold based on ambient noise...")
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        recognized = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said: {}".format(recognized))
        # os.system("say '{}'".format(recognized))
        subprocess.run(["say", "{}".format(recognized)], stdout=subprocess.DEVNULL)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == '__main__':
    recognize()
