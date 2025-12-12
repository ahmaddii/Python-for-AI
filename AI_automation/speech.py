import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use the microphone as source
with sr.Microphone() as source:
    print("Adjusting for ambient noise... Please wait 1 second")
    r.adjust_for_ambient_noise(source, duration=1)

    print("Say something:")
    audio = r.listen(source)

# Convert speech to text using Google API
try:
    text = r.recognize_google(audio)
    print("You said:", text)

    # Optional: save to a file
    with open("transcription.txt", "w") as f:
        f.write(text)

except sr.UnknownValueError:
    print("Sorry, could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
