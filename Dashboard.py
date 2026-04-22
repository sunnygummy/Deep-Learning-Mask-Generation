import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess
import sys
import os

def run_script(script_name):
    subprocess.run([sys.executable, script_name, folder_path])

def select_directory():
    global folder_path
    folder_path = filedialog.askdirectory()
    if folder_path:
        label.config(text=f"Selected: {folder_path}")

root = tk.Tk()
root.title("Program Selector")
root.geometry("400x200")

scripts = [
    r"C:\Users\VLWeg\Desktop\Research\randombullshitgo\main.py",
    r"C:\Users\YourName\Projects\Vessels.py"
]
selected_script = tk.StringVar()
selected_script.set(scripts[0])

dropdown = ttk.Combobox(root, width=50, textvariable=selected_script, values=scripts, state="readonly")
dropdown.pack(pady=20)

select_button = tk.Button(root, text="Choose Folder", command=select_directory)
select_button.pack(pady=20)

label = tk.Label(root, text="No folder selected")
label.pack()

run_button = tk.Button(root, text="Run Program",command=lambda: run_script(selected_script.get()))
run_button.pack(pady=10)

root.mainloop()