import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Keywords for screening
keywords = ["Python", "Java", "SQL", "Machine Learning", "HTML", "CSS"]

# Function to screen resume
def screen_resume():
    file_path = filedialog.askopenfilename(
        title="Select Resume File",
        filetypes=[("Text Files", "*.txt")]
    )

    if not file_path:
        return

    try:
        with open(file_path, "r") as file:
            content = file.read()

        matched_keywords = []

        for word in keywords:
            if word.lower() in content.lower():
                matched_keywords.append(word)

        result_text.delete("1.0", tk.END)

        if matched_keywords:
            result = "Matched Skills:\n\n" + "\n".join(matched_keywords)
        else:
            result = "No matching skills found."

        result_text.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI Window
root = tk.Tk()
root.title("Resume Screening System")
root.geometry("500x400")

title_label = tk.Label(
    root,
    text="Resume Screening System",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=10)

upload_button = tk.Button(
    root,
    text="Upload Resume",
    command=screen_resume,
    font=("Arial", 12),
    padx=10,
    pady=5
)
upload_button.pack(pady=10)

result_text = tk.Text(root, height=15, width=50)
result_text.pack(pady=10)

root.mainloop()
