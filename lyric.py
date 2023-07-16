import tkinter as tk
from tkinter import *
from lyrics_extractor import SongLyrics

window = Tk()  # Creating the window
window.geometry('600x600')  # Setting the window size
window.title('LYRICS')  # Setting the window title

head = Label(window, text="Enter the song you want lyrics for", font=('Calibri', 15))  # Creating a label
head.pack(pady=20)

result = StringVar()  # Ensuring result is of string type
song = StringVar()  # Ensuring song is of string type

def get_lyrics():
    song_name = song.get()  # Getting the value of the song
    api_key = "AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg"
    engine_id = "aa2313d6c88d1bf22"
    extract_lyrics = SongLyrics(api_key, engine_id)  # Creating an instance of SongLyrics
    song_lyrics = extract_lyrics.get_lyrics(song_name)  # Getting the lyrics for the given song
    result.set(song_lyrics)  # Setting the result

entry = Entry(window, textvariable=song, font=('Calibri', 12))  # Creating an entry field to input the song name
entry.pack()

message = Message(window, textvariable=result, bg="light grey", font=('Calibri', 12))  # Displaying the lyrics
message.pack(side=TOP, anchor=W, fill=BOTH, expand=1)

button = Button(window, text="GO", command=get_lyrics, font=('Calibri', 12))  # Creating a button to trigger lyrics extraction
button.pack()

window.mainloop()
