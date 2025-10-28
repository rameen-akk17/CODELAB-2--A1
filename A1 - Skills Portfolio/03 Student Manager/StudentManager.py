from tkinter import *
from tkinter import ttk, messagebox

def load_students(filename="studentMarks.txt"):
    students = []
    try:
        with open(filename, "r") as f:
            lines = f.read().strip().split("\n")
            for line in lines[1:]:  # skip first line which might contain total count
                sid, name, c1, c2, c3, exam = line.split(",")
                coursework = int(c1) + int(c2) + int(c3)  # sum of all coursework components
                total = coursework + int(exam)  # total marks including exam
                percent = round((total / 160) * 100, 2)  # percentage out of 160
                grade = get_grades(percent)  # determinesletter grade
                students.append({
                    "id": sid,
                    "name": name,
                    "coursework": coursework,
                    "exam": int(exam),
                    "total": total,
                    "percent": percent,
                    "grade": grade
                })
    except FileNotFoundError:
        # show error popup if file does not exist
        messagebox.showerror("Error", "studentsMarks.txt not found")
    return students

# assign grade based on percentage
def get_grades(p):
    if p >= 70: return "A"
    elif p >= 60: return "B"
    elif p >= 50: return "C"
    elif p >= 40: return "D"
    else: return "F"

# show all student records and average percentage
def viewAll():
    output.delete("1.0", END)  # clear previous text in output box
    total_percent = 0
    for s in students_data:
        # insert each student's info into text widget
        output.insert(END, f"\nName: {s['name']}\n"
                           f"ID: {s['id']}\n"
                           f"Coursework Total: {s['coursework']}/60\n"
                           f"Exam Mark: {s['exam']}/100\n"
                           f"Overall %: {s['percent']}%\n"
                           f"Grade: {s['grade']}\n"
                           f"{'-'*40}\n")
        total_percent += s['percent']
    avg = round(total_percent / len(students_data), 2)  # calculate class average
    output.insert(END, f"\nStudents: {len(students_data)} | Average %: {avg}%\n")

# display info for selected student
def viewOne():
    name = dropdown.get()  # get name from dropdown
    if not name:  # if no selection, show warning
        messagebox.showwarning("Warning", "Please select a student")
        return
    output.delete("1.0", END)
    # search for student by name, return None if not found
    s = next((x for x in students_data if x['name'] == name), None)
    if s:
        output.insert(END, f"Name: {s['name']}\n"
                           f"ID: {s['id']}\n"
                           f"Coursework Total: {s['coursework']}/60\n"
                           f"Exam Mark: {s['exam']}/100\n"
                           f"Overall %: {s['percent']}%\n"
                           f"Grade: {s['grade']}\n")
    else:
        messagebox.showinfo("Invalid", "Student not found")

# show student with highest total score
def highest():
    s = max(students_data, key=lambda x: x['total'])  # find max based on total
    single(s, "Highest Score")

# show student with lowest total score
def lowest():
    s = min(students_data, key=lambda x: x['total'])  # find min based on total
    single(s, "Lowest Score")

# display a single student's info with a title
def single(s, title):
    output.delete("1.0", END)
    # title + student details
    output.insert(END, f"{title}\n{'-'*40}\n"
                       f"Name: {s['name']}\n"
                       f"ID: {s['id']}\n"
                       f"Coursework Total: {s['coursework']}/60\n"
                       f"Exam Mark: {s['exam']}/100\n"
                       f"Overall %: {s['percent']}%\n"
                       f"Grade: {s['grade']}\n")

# UI
root = Tk()
root.geometry("670x415")  # window size
root.title("Student Manager")
root.configure(bg="black")  # background color

# load student data from file
students_data = load_students()
# get list of student names for dropdown
students = [s['name'] for s in students_data]

# buttons to trigger functions
Button(root, text="View All Student Records", bg="white", fg="green", command=viewAll).grid(row=1, column=0, padx=10, pady=10)
Button(root, text="Show Highest Score", bg="white", fg="green", command=highest).grid(row=1, column=1, padx=10, pady=10)
Button(root, text="Show Lowest Score", bg="white", fg="green", command=lowest).grid(row=1, column=2, padx=10, pady=10)
Button(root, text="View Record", bg="white", fg="green", command=viewOne).grid(row=2, column=2, padx=10, pady=10)

# labels for UI headings
Label(root, text="Student Manager", font=("Arial", 16, "bold"), bg="black", fg="green").grid(row=0, column=1)
Label(root, text="View individual student record:", bg='black', fg="green").grid(row=2, column=0, padx=10, pady=10, sticky="e")

# dropdown menu for selecting student
dropdown = ttk.Combobox(root, values=students, width=20, state="readonly")
dropdown.grid(row=2, column=1, padx=10, pady=10)

# text widget to display student info
output = Text(root, width=80, height=15, bg="#f8f8f8", fg="black", font=('ariel', 12), wrap=WORD)
output.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# run the GUI loop
root.mainloop()