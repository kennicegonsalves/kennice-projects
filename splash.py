import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from votersignup import VoterSignup
from voterpopup import VoterSignupPopup
/charis is great
class CampusVoice:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(background="white")

        window_width = 933
        window_height = 525
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.root.title("CampusVoice")

        self.image = Image.open(r'C:\\Users\\kenni\\OneDrive\\Desktop\\miniproject\\front.jpg')
        self.photo = ImageTk.PhotoImage(self.image)

        self.label_image = tk.Label(self.root, image=self.photo)
        self.label_image.place(x=0, y=0)

        self.heading = tk.Label(self.root, text="CampusVoice", font=("Helvetica", 40, "bold"), fg="black", bg="light blue")
        self.heading.place(relx=0.5, rely=0.05, anchor=CENTER)

        button_width = 15
        button_height = 2
        button_padding = 20
        button_y = 0.9 * window_height

        self.button_candidate = tk.Button(self.root, text="Candidate", width=button_width, height=button_height, bg="#4CAF50", fg="white", font=("Helvetica", 14, "bold"), relief=RAISED, borderwidth=3, command=self.open_candidate)
        self.button_candidate.place(relx=0.3, rely=button_y/window_height, anchor=CENTER)

        self.button_voter = tk.Button(self.root, text="Voter", width=button_width, height=button_height, bg="#2196F3", fg="white", font=("Helvetica", 14, "bold"), relief=RAISED, borderwidth=3, command=self.open_voter)
        self.button_voter.place(relx=0.7, rely=button_y/window_height, anchor=CENTER)

        self.root.mainloop()

    def open_candidate(self):
        self.root.destroy()

    def open_voter(self):
        self.voter_popup = VoterSignupPopup(self.root)

if __name__ == "__main__":
    app = CampusVoice()
