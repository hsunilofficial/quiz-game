import tkinter as tk  # Importing Tkinter for GUI components
from tkinter import messagebox  # Importing messagebox for pop-up alerts
import time  # Importing time module for timer functionality

# List of coding challenges with questions and correct answers
challenges = [
    {"question": "Print 'Hello, World!' in Python", "answer": "print('Hello, World!')"},
    {"question": "Create a list of numbers from 1 to 5", "answer": "numbers = [1, 2, 3, 4, 5]"},
    {"question": "Define a function that returns the square of a number", "answer": "def square(x): return x * x"},
    {"question": "Assign the value 10 to a variable named 'x'", "answer": "x = 10"},
    {"question": "Write a loop that prints numbers 1 to 5", "answer": "for i in range(1, 6): print(i)"},
    {"question": "Create a dictionary with keys 'name' and 'age'", "answer": "person = {'name': 'Alice', 'age': 25}"},
    {"question": "Write an if statement that checks if x is greater than 5", "answer": "if x > 5: print('x is greater than 5')"},
    {"question": "Concatenate two strings 'Hello' and 'World'", "answer": "greeting = 'Hello' + ' ' + 'World'"},
    {"question": "Create a list and add an element 'Python' to it", "answer": "my_list = []; my_list.append('Python')"}
]

class CodingGame:
    def __init__(self, root):
        self.root = root  # Assign the root window
        self.root.title("Coding Game")  # Set window title
        
        self.current_question = 0  # Index for tracking the current question
        self.score = 0  # Variable to store player's score
        self.time_limit = 30  # Time limit per question in seconds
        
        # Create a label to display the current coding challenge
        self.label = tk.Label(root, text=challenges[self.current_question]['question'], wraplength=400, font=("Arial", 12))
        self.label.pack(pady=10)
        
        # Create an entry box for user input
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=5)
        
        # Submit button to check the user's answer
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack(pady=5)
        
        # Hint button to provide a hint for the current question
        self.hint_button = tk.Button(root, text="Hint", command=self.show_hint)
        self.hint_button.pack(pady=5)
        
        # Timer label to display remaining time
        self.timer_label = tk.Label(root, text=f"Time Left: {self.time_limit}s", font=("Arial", 10))
        self.timer_label.pack(pady=5)
        
        self.update_timer()  # Start the countdown timer
        
    def check_answer(self):
        user_answer = self.entry.get().strip()  # Get the user's input and remove extra spaces
        correct_answer = challenges[self.current_question]['answer']  # Get the correct answer
        
        if user_answer == correct_answer:
            self.score += 1  # Increment score if answer is correct
            messagebox.showinfo("Correct!", "Good job! Moving to the next challenge.")  # Display success message
            self.next_question()  # Move to the next question
        else:
            messagebox.showerror("Incorrect", "Try again!")  # Display error message if incorrect
    
    def next_question(self):
        self.current_question += 1  # Increment question index
        self.time_limit = 30  # Reset timer for the next question
        
        if self.current_question < len(challenges):  # Check if more questions are available
            self.label.config(text=challenges[self.current_question]['question'])  # Update label with new question
            self.entry.delete(0, tk.END)  # Clear entry box for new input
        else:
            messagebox.showinfo("Game Over", f"Congratulations! You completed all challenges. Final Score: {self.score}")  # Display final score
            self.root.quit()  # Close the game window
    
    def show_hint(self):
        correct_answer = challenges[self.current_question]['answer']  # Get correct answer
        hint = correct_answer[:len(correct_answer)//2] + "..."  # Generate a partial hint
        messagebox.showinfo("Hint", f"Try something like: {hint}")  # Display the hint
    
    def update_timer(self):
        if self.time_limit > 0:
            self.time_limit -= 1  # Decrease the time limit by 1 second
            self.timer_label.config(text=f"Time Left: {self.time_limit}s")  # Update timer label
            self.root.after(1000, self.update_timer)  # Call this function again after 1 second
        else:
            messagebox.showerror("Time's Up!", "You ran out of time!")  # Display time's up message
            self.next_question()  # Move to the next question

if __name__ == "__main__":  # Check if script is run directly
    root = tk.Tk()  # Create Tkinter root window
    game = CodingGame(root)  # Initialize the game
    root.mainloop()  # Run the Tkinter event loop
