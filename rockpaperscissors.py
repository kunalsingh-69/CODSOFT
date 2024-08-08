import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    outcomes = {
        ('rock', 'scissors'): 'User wins!',
        ('scissors', 'rock'): 'Computer wins!',
        ('paper', 'rock'): 'User wins!',
        ('rock', 'paper'): 'Computer wins!',
        ('scissors', 'paper'): 'User wins!',
        ('paper', 'scissors'): 'Computer wins!',
    }
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    return outcomes.get((user_choice, computer_choice), 'Error')

# Function to handle user choice and game logic
def user_choice(choice):
    global user_score , computer_score
    choices = ['rock', 'paper', 'scissors']
    user_choice= choice
    computer_choice = random.choice(choices)
    
        
    # Update computer choice label
    
    if computer_choice=="rock":
        computer_choice_label.config(image=rock_photo)
    elif  computer_choice=="paper":
        computer_choice_label.config(image=paper_photo)
    elif  computer_choice=="scissors":
        computer_choice_label.config(image=scissors_photo)
                   
        
    
    # Determine winner    
    result = determine_winner(user_choice, computer_choice)

    #update scores
    if result=='User wins!':
        user_score+=1
        user_score_label.config(text=f"User Score:{user_score}")
    elif result== 'Computer wins!':
        computer_score+=1
        computer_score_label.config(text=f"Computer Score:{computer_score}")    
    
    # Show result in a message box
    messagebox.showinfo("Result", result)

# Create main window
root = tk.Tk()
root.title("Rock Paper Scissors")
user_score=0
computer_score=0


result_label=tk.Label(root,text="",font=("Arial",12))
result_label.pack()

 
 #Load and display images
rock_image = Image.open("rock.png")
rock_image = rock_image.resize((100, 100))
rock_photo = ImageTk.PhotoImage(rock_image)

paper_image = Image.open("paper.png")
paper_image = paper_image.resize((100, 100))
paper_photo = ImageTk.PhotoImage(paper_image)

scissors_image = Image.open("scissors.png")
scissors_image = scissors_image.resize((100, 100))
scissors_photo = ImageTk.PhotoImage(scissors_image)

# Create and place widgets
tk.Button(root, image=rock_photo, command=lambda: user_choice('rock')).pack(side=tk.LEFT)
tk.Button(root, image=paper_photo, command=lambda: user_choice('paper')).pack(side=tk.LEFT)
tk.Button(root, image=scissors_photo, command=lambda: user_choice('scissors')).pack(side=tk.LEFT)


computer_choice_label = tk.Label(root, text=f"Computer chose: ")
computer_choice_label.pack(side=tk.RIGHT)

user_score_label=tk.Label(root,text=f"User Score:{user_score}")
user_score_label.pack(padx=10,pady=5)

computer_score_label=tk.Label(root,text=f"Computer score:{computer_score}")
computer_score_label.pack(padx=10,pady=5)
# Run the GUI event loop
root.mainloop()