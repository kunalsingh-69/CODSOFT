import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 8:
        result_label.config(text="Password length should be at least 8")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    
    # Calculate complexity
    complexity = {
        "Uppercase": any(c.isupper() for c in password),
        "Lowercase": any(c.islower() for c in password),
        "Digits": any(c.isdigit() for c in password),
        "Special Characters": any(c in string.punctuation for c in password)
    }

    complexity_text = "\n".join(f"{key}: {'Yes' if value else 'No'}" for key, value in complexity.items())
    
    result_label.config(text=f"Generated Password: {password}\n\nComplexity:\n{complexity_text}")

# Set up the GUI window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

result_label = tk.Label(root, text="Generated Password: ")
result_label.pack()

# Run the GUI event loop
root.mainloop()

