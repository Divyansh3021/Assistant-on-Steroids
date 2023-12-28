import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

def recognise_text(audio_file_path=None):
    """Recognizes text from either real-time audio or an existing audio file.

    Args:
        audio_file_path (str, optional): Path to an existing audio file. Defaults to None.

    Returns:
        str: The recognized text, or None if there was an error.
    """

    if audio_file_path:
        with sr.AudioFile(audio_file_path) as source:
            audio = r.record(source)  # Use record() for audio files
    else:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for noise
            print("Speak anything:")
            audio = r.listen(source)  # Use listen() for real-time input

    try:
        text = r.recognize_google(audio)  # Use Google Speech Recognition
        print("You said:", text)
        return text

    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from speech recognition service; {0}".format(e))

    return None

# Example usage:
# For real-time audio:
# text = recognise_text()

# For existing audio file:
# audio_file_path = "speech_recog_test.wav"  # Replace with actual path
# text = recognise_text(audio_file_path)
