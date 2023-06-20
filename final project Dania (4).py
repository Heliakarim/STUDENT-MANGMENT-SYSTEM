import tkinter as tk


class Student:
    def __init__(self, name, age, percentage):
        self.name = name
        self.age = age
        self.percentage = percentage
        self.grade = ""

    def display_details(self):
        return f"Name: {self.name}\nAge: {self.age}\nPercentage: {self.percentage}\nGrade: {self.grade}"


class RegularStudent(Student):
    def __init__(self, name, age, percentage):
        super().__init__(name, age, percentage)
        self.grade = "Regular"


class HonorsStudent(Student):
    def __init__(self, name, age, percentage):
        super().__init__(name, age, percentage)
        self.grade = "Honors"


class TransferStudent(Student):
    def __init__(self, name, age, percentage):
        super().__init__(name, age, percentage)
        self.grade = "Transfer"


class StudentDatabase:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_student(self, student):
        with open(self.file_path, "a") as file:
            file.write(f"{student.name},{student.age},{student.grade},{student.percentage}\n")

    def get_student_details(self, name):
        with open(self.file_path, "r") as file:
            for line in file:
                student_data = line.strip().split(",")
                if student_data[0] == name:
                    if student_data[2] == "Regular":
                        student = RegularStudent(student_data[0], int(student_data[1]), float(student_data[3]))
                    elif student_data[2] == "Honors":
                        student = HonorsStudent(student_data[0], int(student_data[1]), float(student_data[3]))
                    elif student_data[2] == "Transfer":
                        student = TransferStudent(student_data[0], int(student_data[1]), float(student_data[3]))
                    else:
                        student = Student(student_data[0], int(student_data[1]), float(student_data[3]))
                    return student
        return None


def open_retrieve_window():
    retrieve_window = tk.Toplevel(window)
    retrieve_window.title("Retrieve Student Details")

    def retrieve_student_details():
        name = name_entry.get()
        try:
            retrieved_student = db.get_student_details(name)
            if retrieved_student:
                details_label.config(text=retrieved_student.display_details())
            else:
                details_label.config(text="Student not found.")
        except Exception as e:
            details_label.config(text=str(e), fg="red")

    name_label = tk.Label(retrieve_window, text="Student Name:")
    name_label.pack()

    name_entry = tk.Entry(retrieve_window)
    name_entry.pack()

    retrieve_button = tk.Button(retrieve_window, text="Retrieve Details", command=retrieve_student_details)
    retrieve_button.pack()

    details_label = tk.Label(retrieve_window, text="")
    details_label.pack()





def add_student():
    name = name_entry.get()
    age = age_entry.get()
    percentage = percentage_entry.get()
    grade = student_type_var.get()

    try:
        age = int(age)
        percentage = float(percentage)
    except ValueError:
        result_label.config(text="Invalid age or percentage.", fg="red")
        return

    if not name or not age or not percentage or not grade:
        result_label.config(text="Please fill in all fields.", fg="red")
        return

    try:
        if grade == "Regular":
            student = RegularStudent(name, age, percentage)
        elif grade == "Honors":
            student = HonorsStudent(name, age, percentage)
        elif grade == "Transfer":
            student = TransferStudent(name, age, percentage)
        else:
            result_label.config(text="Invalid grade type.", fg="red")
            return

        db.add_student(student)
        result_label.config(text="Student added successfully!", fg="green")
    except Exception as e:
        result_label.config(text=str(e), fg="red")

    # Clear entry fields
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    percentage_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)


# Usage example
file_path = "students.txt"
db = StudentDatabase(file_path)

# Create the main window
window = tk.Tk()
window.title("Student Database")

# Create and place the labels and entry fields
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_label = tk.Label(window, text="Age:")
age_label.grid(row=1, column=0, padx=10, pady=5)
age_entry = tk.Entry(window)
age_entry.grid(row=1, column=1, padx=10, pady=5)

student_type_label = tk.Label(window, text="Student Type:")
student_type_label.grid(row=2, column=0, padx=10, pady=5)
student_types = ["Regular", "Honors", "Transfer"]
student_type_var = tk.StringVar(window)
student_type_dropdown = tk.OptionMenu(window, student_type_var, *student_types)
student_type_dropdown.grid(row=2, column=1, padx=10, pady=5)

percentage_label = tk.Label(window, text="Percentage:")
percentage_label.grid(row=3, column=0, padx=10, pady=5)
percentage_entry = tk.Entry(window)
percentage_entry.grid(row=3, column=1, padx=10, pady=5)

grade_label = tk.Label(window, text="Grade:")
grade_label.grid(row=4, column=0, padx=10, pady=5)
grade_entry = tk.Entry(window)
grade_entry.grid(row=4, column=1, padx=10, pady=5)

# Create and place the buttons
add_button = tk.Button(window, text="Add Student", command=add_student, bg="yellow", fg="black")
add_button.grid(row=5, column=0, padx=10, pady=5)

retrieve_button = tk.Button(window, text="Retrieve Details", command=open_retrieve_window, bg="black", fg="yellow")
retrieve_button.grid(row=6, column=0, padx=10, pady=5)

exit_button = tk.Button(window, text="Exit", command=window.destroy, bg="red", fg="black")
exit_button.grid(row=6, column=1, padx=10, pady=5)

# Create and place the result label
result_label = tk.Label(window, text="")
result_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Start the main loop
window.mainloop()

