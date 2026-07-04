import tkinter as tk
import time

# Sentence to type
sentence = "Python programming is easy and fun."

start_time = None

# Start timer when typing begins
def start_typing(event):
    global start_time
    if start_time is None:
        start_time = time.time()

# Calculate typing speed and accuracy
def check_result():
    global start_time

    if start_time is None:
        return

    end_time = time.time()
    typed_text = entry.get()

    elapsed_time = end_time - start_time

    # Words Per Minute (WPM)
    words = len(typed_text.split())
    wpm = (words / elapsed_time) * 60

    # Accuracy
    correct_chars = 0
    for i in range(min(len(typed_text), len(sentence))):
        if typed_text[i] == sentence[i]:
            correct_chars += 1

    accuracy = (correct_chars / len(sentence)) * 100

    result.config(
        text=f"Time: {elapsed_time:.2f} sec\n"
             f"Speed: {wpm:.2f} WPM\n"
             f"Accuracy: {accuracy:.2f}%"
    )

# GUI
root = tk.Tk()
root.title("Typing Speed Test")
root.geometry("600x300")

tk.Label(root, text="Type the following sentence:",
         font=("Arial", 14)).pack(pady=10)

tk.Label(root, text=sentence,
         font=("Arial", 12),
         wraplength=550).pack()

entry = tk.Entry(root, width=60, font=("Arial", 14))
entry.pack(pady=20)

entry.bind("<KeyRelease>", start_typing)

tk.Button(root, text="Submit",
          command=check_result).pack()

result = tk.Label(root, text="", font=("Arial", 12))
result.pack(pady=20)

root.mainloop()