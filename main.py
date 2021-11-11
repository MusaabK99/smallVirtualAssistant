import pyttsx3
import speech_recognition as sr


def speak(audio):
    engine = pyttsx3.init()

    # getter method (gets the current value of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male vooice [1]= female voice in set property .
    engine.setProperty('voice', voices[1].id)

    # Method for the speaking of the assistant
    engine.say(audio)

    # Blocks while processing all the currently queued commands
    engine.runAndWait()


def hello():
    speak("Hello , How can i help you ?")


def takeCommand():
    meme = sr.Recognizer()

    # from the speech_Recogition module we will use the microphone module for listening the command

    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before a phrase is considered complete

        meme.pause_threshold = 0.7
        audio = meme.listen(source)

        # now we will be using the try and catch method so that if sound is recognized it is good else we will have exception handling

        try:
            print("Recognizing")

            # for Listening the command in indian english we can also use 'hi-In' for hindi Recognizing

            Query = meme.recognize_google(audio, language='en-US')
            print("the command is printed=", Query)
        except Exception as e:
            print(e)
            print("what can you say it again ? ")
            return "None"
        return Query


def take_Query():
    hello()

    while(True):
        query = takeCommand().lower()
        if "tell me your name" in query:
            speak("Hi i am your desktop Assistant meme")

        # this will exit and terminate the program
        elif "bye" in query:
            speak("Bye my love ")
            exit()


if __name__ == '__main__':

    # main method for executing the functions

    take_Query()
