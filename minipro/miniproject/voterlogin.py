import tkinter as tk
from tkinter import messagebox
import sqlite3
from PIL import Image, ImageTk
from subprocess import Popen

class VoterLogin:
    def __init__(self, master):
        self.master = master
        self.root = tk.Toplevel(master)  # Use Toplevel instead of Tk
        self.root.title("Voter Login")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 780
        window_height = 520
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.root.configure(background="white")  # Set background color to white

        self.label_pid = tk.Label(self.root, text="PID Number:", bg="white", font=("Helvetica", 12))
        self.label_pid.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_pid = tk.Entry(self.root, font=("Helvetica", 12), bg="light blue")
        self.entry_pid.grid(row=0, column=1, padx=10, pady=10)

        self.label_email = tk.Label(self.root, text="Email:", bg="white", font=("Helvetica", 12))
        self.label_email.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_email = tk.Entry(self.root, font=("Helvetica", 12), bg="light blue")
        self.entry_email.grid(row=1, column=1, padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_form, font=("Helvetica", 12))
        self.submit_button.grid(row=2, column=1, padx=10, pady=10, sticky="e")

        self.back_button = tk.Button(self.root, text="Back", command=self.back_to_campus_voice, font=("Helvetica", 12))
        self.back_button.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.icon = Image.open(r"miniproject\\voterlogin.jpg")
        self.icon = self.icon.resize((200, 200), Image.BILINEAR) 
        self.icon = ImageTk.PhotoImage(self.icon)
        self.label_icon = tk.Label(self.root, image=self.icon, bg="white")
        self.label_icon.grid(row=0, column=2, rowspan=3, padx=10, pady=10) 

    def submit_form(self):
        pid = self.entry_pid.get()
        email = self.entry_email.get()
        if not pid or not email:
            messagebox.showerror("Error", "Please enter both PID and email.")
            return

        # Connect to the SQLite database
        connection = sqlite3.connect("Kenny.db")
        cursor = connection.cursor()

        # Query the database for the provided PID and email
        cursor.execute("SELECT * FROM voters WHERE pid=? AND email=?", (pid, email))
        voter = cursor.fetchone()

        # Check if a matching record was found
        if voter:
            messagebox.showinfo("Success", "Login successful!")
            self.root.destroy()
            Popen(["python", "voterhome.py",   pid, email])
        else:
            messagebox.showerror("Error", "Invalid PID or email.")

        # Close the database connection
        connection.close()

    def back_to_campus_voice(self):
        self.root.destroy()
        
    
        
