import tkinter as tk
from tkinter import messagebox, filedialog
import sqlite3
from PIL import Image, ImageTk

class VoterSignup:
    def __init__(self, master):
        
        self.master = master
        self.root = master
        self.root.title("Voter Signup")
        self.root.geometry("780x520")  # Set window size
        self.background_image = Image.open("miniproject\\register (1).png")
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.root, image=self.background_photo)
        self.background_label.place(relwidth=1, relheight=1)
        
        # Create the signup frame
        self.signup_frame = tk.Frame(self.root, bg="black")
        self.signup_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Labels and entries within the signup box
        self.label_name = tk.Label(self.signup_frame, text="Name:", font=("Helvetica", 12),bg="black", fg="white")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = tk.Entry(self.signup_frame, font=("Helvetica", 12))
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_roll = tk.Label(self.signup_frame, text="Roll Number:", font=("Helvetica", 12),bg="black", fg="white")
        self.label_roll.grid(row=0, column=2, padx=10, pady=10)
        self.entry_roll = tk.Entry(self.signup_frame, font=("Helvetica", 12))
        self.entry_roll.grid(row=0, column=3, padx=10, pady=10)
        
        self.label_pid = tk.Label(self.signup_frame, text="PID Number:", font=("Helvetica", 12),bg="black", fg="white")
        self.label_pid.grid(row=1, column=0, padx=10, pady=10)
        self.entry_pid = tk.Entry(self.signup_frame, font=("Helvetica", 12))
        self.entry_pid.grid(row=1, column=1, padx=10, pady=10)
        
        self.label_class = tk.Label(self.signup_frame, text="Class:", font=("Helvetica", 12),bg="black", fg="white")
        self.label_class.grid(row=1, column=2, padx=10, pady=10)
        self.entry_class = tk.Entry(self.signup_frame, font=("Helvetica", 12))
        self.entry_class.grid(row=1, column=3, padx=10, pady=10)
        
        self.label_branch = tk.Label(self.signup_frame, text="Branch:", font=("Helvetica", 12),bg="black", fg="white")
        self.label_branch.grid(row=2, column=0, padx=10, pady=10)
        self.entry_branch = tk.Entry(self.signup_frame, font=("Helvetica", 12))
        self.entry_branch.grid(row=2, column=1, padx=10, pady=10)
        
        self.label_email = tk.Label(self.signup_frame, text="Email:", font=("Helvetica", 12),bg="black", fg="white")
        self.label_email.grid(row=2, column=2, padx=10, pady=10)
        self.entry_email = tk.Entry(self.signup_frame, font=("Helvetica", 12))
        self.entry_email.grid(row=2, column=3, padx=10, pady=10)
        
        self.image_preview_label = tk.Label(self.signup_frame, text="Image Preview:", font=("Helvetica", 12),bg="black", fg="white")
        self.image_preview_label.grid(row=3, column=0, padx=10, pady=10)
        self.image_preview = tk.Label(self.signup_frame, bg="white")
        self.image_preview.grid(row=3, column=1, columnspan=2, padx=10, pady=10)
        
        self.submit_button = tk.Button(self.signup_frame, text="Submit", command=self.submit_form, font=("Helvetica", 12))
        self.submit_button.grid(row=4, column=2, padx=10, pady=10, sticky="e")
        
        self.back_button = tk.Button(self.signup_frame, text="Back", command=self.back_to_campus_voice, font=("Helvetica", 12))
        self.back_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        
        self.add_image_button = tk.Button(self.signup_frame, text="Add Image", command=self.add_image, font=("Helvetica", 12))
        self.add_image_button.grid(row=4, column=3, padx=10, pady=10, sticky="e")
        
        self.root.mainloop()

    def submit_form(self):
        name = self.entry_name.get()
        roll = self.entry_roll.get()
        pid = self.entry_pid.get()
        class_ = self.entry_class.get()
        branch = self.entry_branch.get()
        email = self.entry_email.get()

        # Validate the form data
        if not all([name, roll, pid, class_, branch, email]):
            messagebox.showerror("Error", "Please fill in all fields.")
            return None

        # Insert data into the database
        try:
            connection = sqlite3.connect("Kenny.db")
            cursor = connection.cursor()

            # Add the image column to the voters table if it doesn't exist
            cursor.execute("PRAGMA table_info(voters)")
            table_info = cursor.fetchall()
            image_column_exists = any(column[1] == "image" for column in table_info)
            if not image_column_exists:
                cursor.execute("ALTER TABLE voters ADD COLUMN image BLOB")

            # Insert data into the table
            cursor.execute("INSERT INTO voters (name, roll, pid, class_, branch, email, image) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (name, roll, pid, class_, branch, email, self.image_data))
            connection.commit()
            connection.close()

            messagebox.showinfo("Success", "Signup successful!")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def back_to_campus_voice(self):
        self.root.destroy()
        
    def add_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "rb") as file:
                self.image_data = file.read()
            # Display the image preview
            self.load_image_preview(file_path)

    def load_image_preview(self, file_path):
        image = Image.open(file_path)
        image.thumbnail((100, 100))  # Resize image to fit within 150x150
        photo = ImageTk.PhotoImage(image)
        self.image_preview.config(image=photo)
        self.image_preview.image = photo  # Keep reference to prevent garbage collection

if __name__ == "__main__":
    root = tk.Tk()
    app = VoterSignup(root)
    root.mainloop()