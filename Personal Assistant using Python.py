# Importing Libraries for the code
import pyttsx3                                      # Import module for text-to-speech synthesis
import webbrowser                                   # Import module for opening web browsers
import random                                       # Import module for generating random numbers or selecting random items
import speech_recognition as sr                     # Import module for speech recognition
import wikipedia                                    # Import module for accessing Wikipedia articles
import datetime                                     # Import module for working with dates and times
import wolframalpha                                 # Import module for querying the Wolfram Alpha computational knowledge engine
import os                                           # Import module for interacting with the operating system
import sys                                          # Import module for system-specific parameters and functions
import yagmail                                      # Import module for sending emails using Gmail
import pygame                                       # Import module for creating games and multimedia applications
import keyring                                      # Import module for accessing the system keyring services

engine = pyttsx3.init('sapi5')                                  # Initialize the text-to-speech engine using the 'sapi5' speech API
client = wolframalpha.Client('YOUR_CLIENT_ID')                  # Create a client object for accessing the Wolfram Alpha API with your client ID
voices = engine.getProperty('voices')                           # Get the available voices for the text-to-speech engine
engine.setProperty('voice', voices[len(voices)-1].id)           # Set the voice property of the engine to the last available voice

def speak(audio):
    print('Computer: ' + audio)                                 # Print the spoken text with a prefix 'Computer:'
    engine.say(audio)                                           # Use the text-to-speech engine to speak the provided audio
    engine.runAndWait()                                         # Wait for the speech to finish before continuing

def greetMe():
    currentH = int(datetime.datetime.now().hour)                # Get the current hour of the day
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')                                  # If it's morning (between 0 and 12), greet with 'Good Morning!'
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')                                # If it's afternoon (between 12 and 18), greet with 'Good Afternoon!'
    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')                                  # If it's evening (after 18), greet with 'Good Evening!'

greetMe()                                                           # Greet the user based on the current time
speak('Hello Sir, I am your Personal Assistant LARVIS!')            # Introduce the personal assistant
speak('How may I help you?')                                        # Ask for user's assistance

def myCommand():
    r = sr.Recognizer()                                             # Create a speech recognition object
    with sr.Microphone() as source:                                 # Use the microphone as the audio source
        print("Listening...")
        r.pause_threshold =  1                                      # Set the pause threshold for speech recognition
        audio = r.listen(source)                                    # Listen to the audio input
    try:
        query = r.recognize_google(audio, language='en-in')                 # Use Google's speech recognition to convert audio to text
        print('User: ' + query + '\n')                                      # Print the recognized query
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')             # Inform the user if speech recognition fails
        query = str(input('Command: '))                                             # Prompt the user to provide the command by typing it
    return query                                                                    # Return the recognized or typed query

if __name__ == '__main__':
    while True:                                         # Run an infinite loop
        query = myCommand()                             # Get the user's command/query
        query = query.lower()                           # Convert the query to lowercase for easier comparison
        
        if 'open youtube' in query:                             # Check if the query contains the phrase 'open youtube'
            speak('okay')                                       # Respond to the user
            webbrowser.open('www.youtube.com')                  # Open the YouTube website
        
        elif 'open google' in query:                            # Check if the query contains the phrase 'open google'
            speak('okay')                                       # Respond to the user
            webbrowser.open('www.google.co.in')                 # Open the Google website
        
        elif 'open gmail' in query:                             # Check if the query contains the phrase 'open gmail'
            speak('okay')                                       # Respond to the user
            webbrowser.open('www.gmail.com')                    # Open the Gmail website
        
        elif "what\'s up" in query or 'how are you' in query:                                                   # Check if the query contains the phrases 'what's up' or 'how are you'
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']            # List of possible responses
            speak(random.choice(stMsgs))                                                                        # Randomly select and speak one of the responses
        
        elif 'email' in query:                                                                          # Check if the query contains the word 'email'
            speak('Who is the recipient? ')
            Recipient_Username=input("Enter the Recipient\'s Email ID:")                                # Prompt user to enter the recipient's email ID
            speak('Who is the sender? ')
            speak('Enter a Email Id who\'s less secure app permission is provided by Google')           # Prompt user to enter the sender's email ID with less secure app permission
            Your_Username=input("Enter your emaild id:")                                                # Prompt user to enter their email ID
            Stored_password = keyring.get_password('my_app', Your_Username)                             # Retrieve stored password using keyring library
            message = input("Enter your message:")                                                      # Prompt user to enter the email message
            try:
                sender=yagmail.SMTP(Your_Username)                                                                  # Create a yagmail SMTP object using the sender's email ID
                sender.send(to=Recipient_Username,subject='This is an automated mail',contents=message)             # Send the email
            except:
                speak("Sorry I am unable to send your message at this moment!")                                     # Notify the user if the email sending fails

        elif 'nothing' in query or 'abort' in query or 'stop' in query:                     # Check if the query contains keywords indicating the user wants to abort or stop
            speak('okay')                                                                   # Confirm the action
            speak('Bye Sir, have a good day.')                                              # Say goodbye message
            sys.exit()                                                                      # Exit the program
        
        elif 'hello' in query:                                  # Check if the query contains the keyword 'hello'
            speak('Hello Sir')                                  # Greet the user with a 'Hello Sir' message
        
        elif 'bye' in query:                                    # Check if the query contains the keyword 'bye'
            speak('Bye Sir, have a good day.')                  # Speak a farewell message to the user
            sys.exit()                                          # Terminate the program
        
        elif 'play music' in query:                                                                 # Check if the query contains the keyword 'play music'
            pygame.init()                                                                           # Initialize the pygame module
            user_choice = input("Do you want to specify a directory path? (yes/no): ")              # Prompt the user for directory path preference
            if user_choice.lower() == "yes":                                                        # If the user chooses to specify a directory path
                path = input("Enter the directory path: ")                                          # Prompt the user to enter the directory path
            else:                                                                                   # If the user chooses not to specify a directory path
                path = os.path.join(os.environ["USERPROFILE"],"Music")                              # Set the default directory path to the user's Music folder
            music_files = os.listdir(path)                                                          # Get the list of music files in the specified directory
            if len(music_files) == 0:                                                               # If no music files are found in the specified directory
                print("No music files found in the specified directory.")                           # Print a message indicating no music files are found
                pygame.quit()                                                                       # Quit the pygame module
                exit()                                                                              # Exit the program
            random_music = random.choice(music_files)                                               # Select a random music file from the list
            pygame.mixer.music.load(os.path.join(path, random_music))                               # Load the selected music file
            pygame.mixer.music.play()                                                               # Start playing the music
            while True:                                                                             # Loop to wait for user input to stop the music
                user_input = input("Enter 'stop' to stop the music: ")                              # Prompt the user to enter 'stop' to stop the music
                if user_input.lower() == "stop":                                                    # If the user enters 'stop'
                    pygame.mixer.music.stop()                                                       # Stop the music
                    break                                                                           # Break the loop
            pygame.quit()                                                                           # Quit the pygame module
        
        else:                                                                       # If none of the specific commands are matched
            query = query                                                           # Assign the query to itself
            speak('Searching...')                                                   # Speak a message indicating that the program is searching for the query
            try:
                try:
                    res = client.query(query)                                       # Query the Wolfram Alpha API
                    results = next(res.results).text                                # Get the text result from the API response
                    speak('Got it.')                                                # Speak a message indicating successful retrieval of information
                    speak('WOLFRAM-ALPHA says - ')                                  # Speak a message indicating the response is from Wolfram Alpha
                    speak(results)                                                  # Speak the results obtained from Wolfram Alpha
                except:
                    results = wikipedia.summary(query, sentences=5)                 # Get a summary of the query from Wikipedia
                    speak('Got it.')                                                # Speak a message indicating successful retrieval of information
                    speak('WIKIPEDIA says - ')                                      # Speak a message indicating the response is from Wikipedia
                    speak(results)                                                  # Speak the summary obtained from Wikipedia
            except:
                webbrowser.open('https://www.google.com/search?q='+query)           # If no specific result is found, open a Google search with the query
        
        speak('Next Command! Sir!')                                 # Prompt for the next command from the user
