import tkinter as tk
from tkinter import messagebox
import datetime

hosts_path = r"C:\WINDOWS\System32\drivers\etc\hosts"  # For Windows
redirect = "127.0.0.1"
log_file = "blocker_log.txt"

def log_action(action, websites):
    with open(log_file, "a") as file:
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"{time} - {action}: {', '.join(websites)}\n")

def block_websites():
    websites = entry.get().split(",")
    with open(hosts_path, "r+") as file:
        content = file.read() 
        for site in websites:
            site = site.strip()
            if site and site not in content:
                file.write(f"{redirect} {site}\n")
    log_action("Blocked", websites)
    messagebox.showinfo("Success", "Websites blocked.")

def unblock_websites():
    websites = entry.get().split(",")
    with open(hosts_path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            if not any(site.strip() in line for site in websites):
                file.write(line)
        file.truncate()
    log_action("Unblocked", websites)
    messagebox.showinfo("Success", "Websites unblocked.")

root = tk.Tk()
root.title("Python Web Blocker")

label = tk.Label(root, text="Enter websites to block/unblock (comma separated):")
label.pack()

entry = tk.Entry(root, width=60)
entry.pack()

block_btn = tk.Button(root, text="Block", command=block_websites)
block_btn.pack(pady=5)

unblock_btn = tk.Button(root, text="Unblock", command=unblock_websites)
unblock_btn.pack()

root.mainloop()
