import tkinter as tk  
import random  #lib to generate random numbers and operations

root = tk.Tk()   
root.title("Math Quiz")   
root.geometry("600x400")  
root.configure(bg="black")  
 #gv to track and used for later func
difficulty = 1   
score = 0  # tracks total score
question_num = 0  # tracks current question number
num1 = 0   
num2 = 0   
current_operator = ""  # current operation (+ or -)
attempt = 1  # track first or second try for each question

def clear_screen():
    # removes all widgets from window so next screen can appear
    for widget in root.winfo_children():
        widget.destroy()

def randomInt(level):
    # returns a number depending on difficulty level
    if level == 1:
        return random.randint(0, 9)   
    
    
    
    elif level == 2:
        return random.randint(10, 99)   
    else:
        return random.randint(1000, 9999)   

def decideOperation():
    # randomly chooses plus or minus operators
    return random.choice(['+', '-'])

def displayMenu():
    # displays main menu with difficulty options
    clear_screen()
    tk.Label(root, text="MATH QUIZ\nChoose Difficulty", font=("Arial", 20), fg="yellow", bg="black").pack(pady=20)
    tk.Button(root, text="Easy", width=15, font=("Arial", 14), bg="yellow", fg="black", command=lambda: playquiz(1)).pack(pady=10)
    tk.Button(root, text="Moderate", width=15, font=("Arial", 14), bg="yellow", fg="black", command=lambda: playquiz(2)).pack(pady=10)
    tk.Button(root, text="Advanced", width=15, font=("Arial", 14), bg="yellow", fg="black", command=lambda: playquiz(3)).pack(pady=10)

def playquiz(level):
    # initializes quiz variables and starts first question
    global difficulty, score, question_num, attempt
    difficulty = level
    score = 0
    question_num = 1
    attempt = 1
    display_question()

def display_question(feedback=""):
    # shows current question and input box, optionally shows feedback
    global num1, num2, current_operator, attempt
    clear_screen()

    if attempt == 1:  # only generate new numbers on first try
        num1 = randomInt(difficulty)
        num2 = randomInt(difficulty)
        current_operator = decideOperation()

    tk.Label(root, text=f"Question {question_num}: {num1} {current_operator} {num2} = ?", font=("Arial", 18), fg="white", bg="black").pack(pady=20)
    
    if feedback:  # show feedback if provided
        tk.Label(root, text=feedback, font=("Arial", 14), fg="yellow", bg="black").pack(pady=10)

    # input box for answer
    answer_entry = tk.Entry(root, font=("Arial", 16), bg="white", fg="black", justify="center")
    answer_entry.pack(pady=10)
    # submit button calls check_answer with current input
    tk.Button(root, text="Submit", width=10, font=("Arial", 14), bg="yellow", fg="black", command=lambda: check_answer(answer_entry.get())).pack(pady=10)

def check_answer(user_input):
    # checks user's input against correct answer updates score and handles attempts
    global score, question_num, attempt
    try:
        user_answer = int(user_input)  # convert input to integer
    except ValueError:
        display_question("Enter a valid number!")  
        return

    correct_answer = num1 + num2 if current_operator == '+' else num1 - num2  # calculate correct answer

    if user_answer == correct_answer:  # correct answer
        gained = 10 if attempt == 1 else 5  # first try = 10, second try = 5 points
        score += gained
        feedback = f"Correct!! +{gained} points"
        question_num += 1
        attempt = 1
        if question_num <= 10:
            display_question(feedback)  # show next question
        else:
            display_results()  # quiz over
    else:  # wrong answer
        if attempt == 1:
            attempt += 1  # allow second try
            display_question("L! Try one more time.")
        else:  # second attempt wrong
            feedback = f"L again! Correct answer was {correct_answer}"
            question_num += 1
            attempt = 1
            if question_num <= 10:
                display_question(feedback)
            else:
                display_results()  # quiz over

def display_results():
    # shows final score and grade with option to play again
    clear_screen()
    tk.Label(root, text=f"Score: {score}/100", font=("Arial", 20), fg="white", bg="black").pack(pady=30)

    # calculate letter grade
    if score >= 90:
        grade = "a+"
    elif score >= 80:
        grade = "a"
    elif score >= 70:
        grade = "b"
    elif score >= 60:
        grade = "c"
    elif score >= 50:
        grade = "d"
    else:
        grade = "f"

    tk.Label(root, text=f"Your Grade: {grade}", font=("Arial", 18), fg="yellow", bg="black").pack(pady=20)
    tk.Button(root, text="Play Again", width=15, font=("Arial", 14), bg="yellow", fg="black", command=displayMenu).pack(pady=20)

displayMenu()  # show main menu when program starts
root.mainloop()  # keep window open and respond to user actions