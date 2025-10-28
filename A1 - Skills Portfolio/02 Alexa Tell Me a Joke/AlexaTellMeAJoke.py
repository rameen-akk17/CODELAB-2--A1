from tkinter import *
import random

# load jokes from a text fil and  each joke has a setup and punchline separated by ?
def load_jokes(file="randomJokes.txt"):
    jokes = []
    try:
        with open(file, "r") as f:
            for line in f:
                line = line.strip()  # remove extra spaces
                if "?" in line:
                    setup, punch = line.split("?", 1)  # split into setup and punchline
                    jokes.append((setup + "?", punch))
    except FileNotFoundError:
        # fallback joke if file not found
        jokes = [("Why did the code fail?", "Because the file wasn't found!")]
    return jokes

# pick a random joke and display the setup
def tellJoke():
    global current
    current = random.choice(all_jokes)  # select random joke
    output.config(text=current[0])       # show setup
    punchlineButton.config(state=NORMAL) # enable punchline button
    nextJokeButton.config(state=DISABLED) # disable next joke until punchline shown

# show the punchline of the current joke
def showPunchline():
    output.config(text=f"{current[0]}\n\n{current[1]}") # show setup + punchline
    punchlineButton.config(state=DISABLED)  # disable punchline button
    nextJokeButton.config(state=NORMAL)     # enable next joke button

# UI
root = Tk()
root.title("Alexa - Tell Me a Joke")
root.geometry("500x300")
root.configure(bg="black")
root.resizable(FALSE,FALSE)  # fix window size

# title label
Label(root, text="Alexa, tell me a Joke!", font=("Arial", 16, "bold"), fg="red").pack(pady=10)

# label to display joke text
output = Label(root, text="", wraplength=450, justify=LEFT, font=("Arial", 15), bg="#f8f8f8", fg="black")
output.pack(padx=20, pady=20, fill=BOTH, expand=True)

# frame to hold buttons
button_frame = Frame(root, bg="black")
button_frame.pack(pady=10)

# button to show punchline
punchlineButton = Button(button_frame, text="Show Punchline", fg='red', command=showPunchline, state=DISABLED)
punchlineButton.grid(row=0, column=0, padx=10)

# button to load a new joke
nextJokeButton = Button(button_frame, text="New Joke", fg='red', command=tellJoke)
nextJokeButton.grid(row=0, column=1, padx=10)

# quit button
Button(root, text="Quit", bg='black', fg='red', command=root.destroy).pack(pady=5)

# load jokes and start program 
all_jokes = load_jokes()
current = None

root.mainloop()