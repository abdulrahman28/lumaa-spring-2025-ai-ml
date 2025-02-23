from datacleaning import clean as cln
from movie_recommendation import recommend
import random as rd
import tkinter as tk
from tkinter import messagebox, scrolledtext
from time import time


def on_recommend():
    """Handle the recommendation process when the button is pressed."""
    user_input = user_input_text.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Input Error", "Please enter a movie description.")
        return
    
    start_time = time()
    recommendations = recommend(user_input, movie_df, rd.randint(3,5), True)
    
    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.tag_configure("bold", font=("Times New Roman", 12, "bold"))  # Define bold style
    output_text.tag_configure("bold1", font=("Times New Roman", 12))  # Define bold style
    output_text.tag_configure("bold2", font=("Times New Roman", 10, "bold"))  # Define bold style
    
    if recommendations.empty:
        messagebox.showinfo("No Recommendations", "No movies found that match your description.")
    else:
        
        # Display the header first
        output_text.insert(tk.END, f"Execution time: {(time() - start_time):.2f} s\n\n", "bold2")
        output_text.insert(tk.END, f"{'ID':<7} {'Title':<100} Description\n", "bold")
        output_text.insert(tk.END, "-" * 200 + "\n\n")

        # Iterate through each row and print with spacing
        for _, row in recommendations.iterrows():
            
            output_text.insert(tk.END, f"{row['ID']:<1}. ", "bold")
            output_text.insert(tk.END, f"{row['Title']:<1}: ", "bold")  # Apply bold to title
            output_text.insert(tk.END, f"{row['Description']}\n\n", "bold1")  # Normal text for description
            
            
            #output_text.insert(tk.END, f"{row['ID']:<1}. {row['Title']:<1}: {row['Description']}\n\n")  # Extra space added
            
        output_text.insert(tk.END, "-" * 200 + "\n")


fln = 'movies.csv' # Filename of the the dataset from Kaggle public repository
    
# Load dataset
movie_df = cln(fln) # Clean the dataset and return Title and Description

# Create the main window
root = tk.Tk()
root.title("Lumaa Intern Challenge Movie Recommendation System")

# Create and place widgets
tk.Label(root, text="Enter a short description of your preferred movie:").pack(pady=10)

user_input_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=1)
user_input_text.pack(pady=10)

recommend_button = tk.Button(root, text="Get Recommendations", command=on_recommend)
recommend_button.pack(pady=10)

tk.Label(root, text="Recommended Movies:").pack(pady=10)

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=200, height=30)
output_text.pack(pady=10)

# Start the GUI event loop
root.mainloop()
