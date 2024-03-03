import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class VoterLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Voter Login")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = 550
        window_height = 250
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.root.configure(background="white")

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

        self.icon = Image.open(r"C:\Users\kenni\OneDrive\Desktop\miniproject\voterlogin.jpg")
        self.icon = self.icon.resize((200, 200), Image.BILINEAR) 
        self.icon = ImageTk.PhotoImage(self.icon)
        self.label_icon = tk.Label(self.root, image=self.icon, bg="white")
        self.label_icon.grid(row=0, column=2, rowspan=3, padx=10, pady=10) 

        self.root.mainloop()

    def submit_form(self):
        pid = self.entry_pid.get()
        email = self.entry_email.get()

        if pid and email:
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def back_to_campus_voice(self):
        self.root.destroy()

if __name__ == "__main__":
    app = VoterLogin()
