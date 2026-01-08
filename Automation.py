import tkinter as tk
from tkinter import Entry, Label, Button
import webbrowser

#Define the main window
root=tk.Tk()
root.title("Your AI Assistant")

#Adding a background color
root.configure(bg='steelblue')

#Define the Function to automate youtude search
def search_youtube():
    query=entry.get()
    url=f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

#Define the Function to automate google search
def search_google():
    query=entry.get()
    url=f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

#Define the Function to automate instagram search
def search_instagram():
    Username=entry.get().replace('@', "") #Ensure username is clean of '@'
    url=f"www.instagram.com/{Username}/"
    webbrowser.open(url)

#Define the function to automate tiktok search
def search_tiktok():
    query = entry.get()
    url=f"https://www.tiktok.com/search?q={query}"
    webbrowser.open(url)

#create input field, Labels, and butons
Label(root, text="Enter your command:").pack(pady=10)
entry=Entry(root, width=50)
entry.pack(pady=10)
Button(root, text="Search on YouTube", command=search_youtube).pack(pady=5)
Button(root, text="Search on Google", command=search_google).pack(pady=5)
Button(root, text="Search on Instagram", command=search_instagram).pack(pady=5)
Button(root, text="Search on TikTok", command=search_tiktok).pack(pady=5)

#Run the GUI event Loop
root.mainloop()
