import pyttsx3                                                                                          # Library for text-to-speech synthesis
import webbrowser                                                                                       # Library for web browsing functionality
import smtplib                                                                                          # Library for sending emails
import random                                                                                           # Library for generating random numbers and values
import speech_recognition as sr                                                                         # Library for speech recognition
import wikipedia                                                                                        # Library for querying information from Wikipedia
import datetime                                                                                         # Library for working with dates and times
import wolframalpha                                                                                     # Library for accessing the Wolfram|Alpha computational knowledge engine
import os                                                                                               # Library for interacting with the operating system
import sys                                                                                              # Library for system-specific parameters and functions
from playsound import playsound                                                                         # Library for playing sound files
import yagmail                                                                                          # Library for sending emails using Gmail
import pygame                                                                                           # Library for game development and multimedia applications

# Initialize the pyttsx3 text-to-speech engine with the 'sapi5' speech synthesis engine
engine = pyttsx3.init('sapi5')

# Create a client object to access the Wolfram|Alpha API. Please create your APPID by going to Wolframalpha website
client = wolframalpha.Client('YOUR_APP_ID')

# Retrieve the list of available voices and set the last voice as the desired voice for speech synthesis
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

# Function to speak the given audio using the text-to-speech engine
def speak(audio):
    print('Computer: ' + audio)                                                                         # Print the spoken text as a message
    engine.say(audio)                                                                                   # Use the text-to-speech engine to speak the audio
    engine.runAndWait()                                                                                 # Wait until the speech synthesis is completed

# Function to greet the user based on the current time
def greetMe():
    currentH = int(datetime.datetime.now().hour)                                                        # Get the current hour of the day
    if currentH >= 0 and currentH < 12:                                                                 # Check if it is morning
        speak('Good Morning!')                                                                          # Speak the greeting for the morning

    if currentH >= 12 and currentH < 18:                                                                # Check if the current time is between 12 PM (noon) and 6 PM
        speak('Good Afternoon!')                                                                        # Greet the user with "Good Afternoon!"

    if currentH >= 18 and currentH !=0:                                                                 # Check if it is evening (between 6 PM and midnight)
        speak('Good Evening!')                                                                          # Speak the evening greeting

# Invoke the function to greet the user based on the current time
greetMe()

# Introducing the Personal Assistant and Asking for the user's request
speak('Hello Sir, I am your Personal Assistant LARVIS!')
speak('How may I help you?')

# Function to listen to user's voice command and convert it into text
def myCommand():
   
    r = sr.Recognizer()                                                                                 # Create a speech recognizer object
    with sr.Microphone() as source:                                                                     # Use the microphone as the audio source
        print("Listening...")                      
        r.pause_threshold =  1                                                                          # Setting the pause threshold for speech recognition
        audio = r.listen(source)                                                                        # Listening to the audio input
    try:
        query = r.recognize_google(audio, language='en-in')                                             # Convert the audio to text using Google Speech Recognition
        print('User: ' + query + '\n')                                                                  # Print the user's command
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))                                                                 # If speech recognition fails, prompt the user to enter the command manually

    return query
        
# Main program loop for the voice-controlled personal assistant.
if __name__ == '__main__':
    
    while True:
        query = myCommand();                                                                            # Continuously listen to the user's voice command
        query = query.lower()                                                                           # Convert it to lowercase
        
        # Open YouTube in the web browser
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        # Open Google in the web browser
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        # Open Gmail in the web browser
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        # Respond to a general greeting
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        # Send an email
        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()
            
            if 'friend' in recipient:                                                                   # Check if the word "friend" is present in the recipient    
                recognizer=sr.Recognizer()                                                              # Create a speech recognizer object
                with sr.Microphone() as source:                                                         # Use the microphone as the audio source
                    try:
                        speak('Clearing background noise..')
                        speak("Try saying message:")
                        try:
                            recognizer.adjust_for_ambient_noise(source,duration=1)                      # Adjust for background noise
                            speak("waiting for your message...")
                            recordedaudio=recognizer.listen(source)                                     # Listen to the audio input
                            speak('Done recording..!')
                            speak('Printing the message...')
                            text=recognizer.recognize_google(recordedaudio,language='en-US')            # Convert the audio to text
                            print('Your message:{}'.format(text))                                       # Print the captured message
                        except Exception as ex:
                            print(ex)                                                                   # Print any exception that occurs during audio processing
                        #Automate mails:
                        reciever='shubhamdiwadkar987@gmail.com'                                         # Set the email address of the recipient
                        message=text                                                                    # Assign the captured text (message) to the variable "message"
                        sender=yagmail.SMTP('shubhamdiwadkar952@gmail.com')                             # Create an SMTP object with the email address of the sender
                        sender.send(to=reciever,subject='This is an automated mail',contents=message)   # Send the email to the recipient with the subject and contents specified
                    except:                                                                             # Handle any exceptions that occur during the email sending process
                        speak('Sorry Sir! I am unable to send your message at this moment!')            # Notify the user if there was an issue sending the email


        # Stop the program if the user wants to exit
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        # Respond to a greeting
        elif 'hello' in query:
            speak('Hello Sir')

        # Stop the program if the user says goodbye
        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        # Play random music file
        elif 'play music' in query:
            pygame.init()                                                                               # Initialize Pygame
            path = "PLEASE_ENTER_YOUR_MUSIC_FOLDER_PATH"                                                # Path to your music folder
            music_files = os.listdir(path)                                                              # List all the music files in the directory
            random_music = random.choice(music_files)                                                   # Pick a random music file
            pygame.mixer.music.load(os.path.join(path, random_music))                                   # Load the music file
            pygame.mixer.music.play()                                                                   # Play the music file
            
            # Loop until the user enters 'stop'
            while True:
                user_input = input("Enter 'stop' to stop the music: ")                                  # Prompt the user to enter a command to stop the music
                if user_input.lower() == "stop":                                                        # Check if the user input (in lowercase) is equal to "stop"
                    pygame.mixer.music.stop()                                                           # Stop the music
                    break
            pygame.quit()                                                                               # Clean up Pygame

        # Perform a web search or provide information using Wolfram|Alpha and Wikipedia
        else:
            query = query                                                                               # Assign the query back to itself
            speak('Searching...')                                                                       # Notify the user that the program is searching for an answer to the query
            try:
                # Use Wolfram|Alpha for answering the query
                try:
                    res = client.query(query)                                                           # Sending the user's query to Wolfram|Alpha
                    results = next(res.results).text                                                    # Extract the text from the result
                    speak('WOLFRAM-ALPHA says - ')                                                      # Speak a prompt to indicate the source of the answer
                    speak('Got it.')                                                                    # Notify the user that an answer has been obtained
                    speak(results)                                                                      # Speak the answer obtained from Wolfram|Alpha
                    
                # Use Wikipedia for answering the query
                except:
                    results = wikipedia.summary(query, sentences=5)                                     # Retrieve a summary of the query from Wikipedia (limited to 5 sentences)
                    speak('Got it.')                                                                    # Notify the user that an answer has been obtained
                    speak('WIKIPEDIA says - ')                                                          # Speak a prompt to indicate that the following information is from Wikipedia
                    speak(results)                                                                      # Speak the obtained summary from Wikipedia
        
            # If unable to find information, perform a generic web search
            except:
                webbrowser.open('https://www.google.com/search?q='+query)                               # Open a web browser and perform a Google search with the query by constructing the URL
        
        speak('Next Command! Sir!')
