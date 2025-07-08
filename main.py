import tkinter as tk
from tkinter import messagebox, font
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Number Guessing Game ✨")
        self.root.geometry("500x400")
        self.root.configure(bg="#FFE6E8")  # Light pink background
        
        # Custom font
        self.custom_font = font.Font(family="Comic Sans MS", size=12)
        self.title_font = font.Font(family="Comic Sans MS", size=16, weight="bold")
        
        # Game variables
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        # UI Elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(
            self.root, 
            text="🌸 Guess the Number (1-100) 🌸", 
            font=self.title_font, 
            bg="#FFE6E8", 
            fg="#FF69B4"
        )
        title_label.pack(pady=10)
        
        # Instruction
        instruction = tk.Label(
            self.root, 
            text="I'm thinking of a number between 1 and 100.\nCan you guess what it is?",
            font=self.custom_font,
            bg="#FFE6E8",
            fg="#555555"
        )
        instruction.pack(pady=5)
        
        # Guess entry
        self.guess_entry = tk.Entry(
            self.root, 
            font=self.custom_font, 
            width=10, 
            justify="center",
            bd=2,
            relief="ridge"
        )
        self.guess_entry.pack(pady=15)
        self.guess_entry.bind("<Return>", self.check_guess)
        
        # Submit button
        submit_btn = tk.Button(
            self.root, 
            text="Submit Guess", 
            command=self.check_guess,
            font=self.custom_font,
            bg="#FF69B4",
            fg="white",
            activebackground="#FF1493",
            padx=10,
            pady=5,
            bd=0
        )
        submit_btn.pack(pady=5)
        
        # Attempts counter
        self.attempts_label = tk.Label(
            self.root, 
            text="Attempts: 0", 
            font=self.custom_font,
            bg="#FFE6E8",
            fg="#FF69B4"
        )
        self.attempts_label.pack(pady=5)
        
        # Hint label
        self.hint_label = tk.Label(
            self.root, 
            text="", 
            font=self.custom_font,
            bg="#FFE6E8",
            fg="#FF69B4"
        )
        self.hint_label.pack(pady=5)
        
        # Restart button (initially hidden)
        self.restart_btn = tk.Button(
            self.root, 
            text="Play Again", 
            command=self.restart_game,
            font=self.custom_font,
            bg="#FFB6C1",
            fg="white",
            activebackground="#FF69B4",
            padx=10,
            pady=5,
            bd=0,
            state=tk.DISABLED
        )
        self.restart_btn.pack(pady=10)
        
    def check_guess(self, event=None):
        guess = self.guess_entry.get()
        
        try:
            guess = int(guess)
            if guess < 1 or guess > 100:
                messagebox.showwarning("Invalid Input", "Please enter a number between 1 and 100!")
                return
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number!")
            return
        
        self.attempts += 1
        self.attempts_label.config(text=f"Attempts: {self.attempts}")
        
        if guess < self.secret_number:
            self.hint_label.config(text="Too low! Try a higher number. 🌱")
            self.guess_entry.delete(0, tk.END)
        elif guess > self.secret_number:
            self.hint_label.config(text="Too high! Try a lower number. ☁️")
            self.guess_entry.delete(0, tk.END)
        else:
            self.hint_label.config(text=f"🎉 Correct! You guessed it in {self.attempts} attempts! 🎉")
            self.guess_entry.config(state=tk.DISABLED)
            self.restart_btn.config(state=tk.NORMAL)
            
            # Show celebration message
            messagebox.showinfo(
                "Congratulations!", 
                f"You found the number {self.secret_number} in {self.attempts} guesses!\n\n🌟 Great job! 🌟"
            )
    
    def restart_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.attempts_label.config(text="Attempts: 0")
        self.hint_label.config(text="")
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_entry.delete(0, tk.END)
        self.restart_btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()