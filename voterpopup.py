import tkinter as tk

class VoterSignupPopup:
    def __init__(self, master):
        self.master = master
        self.master.title("Voter Options")
        self.master.geometry("300x150")
        self.master.configure(background="white")

        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        x = (screen_width - 300) // 2  
        y = (screen_height - 150) // 2  

        self.master.geometry(f"300x150+{x}+{y}")

        label = tk.Label(self.master, text="Choose an option:", font=("Helvetica", 12), bg="white")
        label.pack(pady=10)

        signup_button = tk.Button(self.master, text="Signup", command=self.open_voter_signup, font=("Helvetica", 12))
        signup_button.pack(pady=5)

        login_button = tk.Button(self.master, text="Login", command=self.open_voter_login, font=("Helvetica", 12))
        login_button.pack(pady=5)

    def open_voter_signup(self):
        self.master.destroy() 

    def open_voter_login(self):
        self.master.destroy() 

if __name__ == "__main__":
    root = tk.Tk()
    app = VoterSignupPopup(root)
    root.mainloop()
