# Personal-Assistant



## Voice-Controlled Personal Assistant

This code represents a voice-controlled personal assistant called LARVIS (acronym for "Life Assistance and Response Virtual Intelligent System"). It allows users to interact with the assistant using voice commands to perform various tasks such as opening web pages, sending emails, retrieving information from the web, playing music, and more.

The code is written in Python and utilizes several libraries and APIs to enable different functionalities. Here's a brief overview of the key components:

### Libraries Used:
- `pyttsx3`: Library for text-to-speech synthesis.
- `webbrowser`: Library for web browsing functionality.
- `smtplib`: Library for sending emails.
- `random`: Library for generating random numbers and values.
- `speech_recognition`: Library for speech recognition.
- `wikipedia`: Library for querying information from Wikipedia.
- `datetime`: Library for working with dates and times.
- `wolframalpha`: Library for accessing the Wolfram|Alpha computational knowledge engine.
- `os`: Library for interacting with the operating system.
- `sys`: Library for system-specific parameters and functions.
- `playsound`: Library for playing sound files.
- `yagmail`: Library for sending emails using Gmail.
- `pygame`: Library for game development and multimedia applications.

### Functionality:
1. **Text-to-Speech**: The `pyttsx3` library is used to convert text into speech. The assistant speaks out the responses or prompts to the user's commands.

2. **Wolfram|Alpha Integration**: The assistant can access the Wolfram|Alpha computational knowledge engine using the `wolframalpha` library. It can provide answers to queries using this powerful API.

3. **Speech Recognition**: The `speech_recognition` library enables the assistant to recognize and convert speech input into text. The assistant listens to the user's voice commands and processes them accordingly.

4. **Web Browsing**: The `webbrowser` library is used to open web pages. The assistant can open YouTube, Google, Gmail, and perform web searches based on the user's commands.

5. **Email Sending**: The `smtplib` and `yagmail` libraries enable the assistant to send emails. Users can dictate the recipient and content of the email, and the assistant automates the sending process.

6. **Music Playback**: The `pygame` library is used to play random music files from a specified folder. The assistant can start playing music and stop it when requested.

7. **Wikipedia Integration**: The `wikipedia` library allows the assistant to retrieve information from Wikipedia. It can provide summaries for specific queries.

8. **Greeting and Conversation**: The assistant greets the user based on the current time and engages in basic conversation, responding to general greetings or questions.

### Usage:
To use the personal assistant, you can run the code in a Python environment, such as Jupyter Notebook or a command-line interface. The assistant listens for voice commands, processes them, and performs the requested tasks accordingly.

Please note that some functionalities, such as email sending or music playback, may require additional configurations or specific paths to be set within the code.

Feel free to explore and modify the code to customize the assistant's behavior and add more functionalities as per your requirements.

**Note:** Remember to replace `'YOUR_APP_ID'` and `'PLEASE_ENTER_YOUR_MUSIC_FOLDER_PATH'` with your own values or paths as indicated in the code comments.

Have fun experimenting with your voice-controlled personal assistant, LARVIS!
