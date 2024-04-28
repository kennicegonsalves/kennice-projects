import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

class VoterSignup:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Voter Signup")
        self.root.geometry("900x300") 
        self.root.configure(background="white")

        self.label_name = tk.Label(self.root, text="Name:", bg="white", font=("Helvetica", 12))
        self.label_name.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_name = tk.Entry(self.root, font=("Helvetica", 12), bg="light blue")
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_roll = tk.Label(self.root, text="Roll Number:", bg="white", font=("Helvetica", 12))
        self.label_roll.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.entry_roll = tk.Entry(self.root, font=("Helvetica", 12), bg="light blue")
        self.entry_roll.grid(row=0, column=3, padx=10, pady=10)

        self.label_pid = tk.Label(self.root, text="PID Number:", bg="white", font=("Helvetica", 12))
        self.label_pid.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_pid = tk.Entry(self.root, font=("Helvetica", 12), bg="light blue")
        self.entry_pid.grid(row=1, column=1, padx=10, pady=10)

        self.label_class = tk.Label(self.root, text="Class:", bg="white", font=("Helvetica", 12))
        self.label_class.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.entry_class = tk.Entry(self.root, font=("Helvetica", 12), bg="light blue")
        self.entry_class.grid(row=1, column=3, padx=10, pady=10)

        self.label_branch = tk.Label(self.root, text="Branch:", bg="white", font=("Helvetica", 12))
        self.label_branch.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_branch = tk.Entry(self.root, font=("Helvetica", 12), bg="light blue")
        self.entry_branch.grid(row=2, column=1, padx=10, pady=10)

        self.label_email = tk.Label(self.root, text="Email:", bg="white", font=("Helvetica", 12))
        self.label_email.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.entry_email = tk.Entry(self.root, font=("Helvetica", 12), bg="light blue")
        self.entry_email.grid(row=2, column=3, padx=10, pady=10)

        self.icon = Image.open(r"C:\Users\kenni\OneDrive\Desktop\miniproject\votersignup.png")
        self.icon = self.icon.resize((200, 200), Image.BILINEAR) 
        self.icon = ImageTk.PhotoImage(self.icon)

        self.label_icon = tk.Label(self.root, image=self.icon, bg="white")
        self.label_icon.grid(row=0, column=4, rowspan=3, padx=10, pady=10) 

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_form, font=("Helvetica", 12))
        self.submit_button.grid(row=3, column=2, padx=10, pady=10, sticky="e")

        self.back_button = tk.Button(self.root, text="Back", command=self.back_to_campus_voice, font=("Helvetica", 12))
        self.back_button.grid(row=3, column=1, padx=10, pady=10, sticky="e")

        self.root.grid_rowconfigure(4, weight=1) 
        self.root.grid_columnconfigure(5, weight=1) 

        self.root.mainloop()

    def submit_form(self):
        name = self.entry_name.get()
        roll = self.entry_roll.get()
        pid = self.entry_pid.get()
        class_ = self.entry_class.get()
        branch = self.entry_branch.get()
        email = self.entry_email.get()
        connection = sqlite3.connect("Kenny.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS  voters(name TEXT, roll INT,pid INT,class_ TEXT,branch TEXT,email TEXT )")
        cursor.execute("INSERT INTO users (name,roll,pid,class_,branch,email) VALUES (?, ?, ?, ?, ?, ?)",(name, roll, pid, class_, branch, email))
        print("Smooth operator")
        connection.commit()
        
        if name and roll and pid and class_ and branch and email:
            messagebox.showinfo("Success", "Signup successful!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def back_to_campus_voice(self):
        self.root.destroy()

if __name__ == "__main__":
    app = VoterSignup()
