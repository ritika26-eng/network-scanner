import tkinter as tk
from scanner import scan_port

root = tk.Tk()
root.title("Network Scanner")
root.geometry("500x450")
root.resizable(False, False)

# Title
title = tk.Label(
    root,
    text="Network Scanner",
    font=("Arial", 18, "bold")
)
title.pack(pady=10)

# IP input
ip_label = tk.Label(root, text="Enter IP Address:")
ip_label.pack()

ip_entry = tk.Entry(root, width=30)
ip_entry.pack(pady=5)

# Status label
status_label = tk.Label(root, text="", fg="blue")
status_label.pack(pady=5)

# Results box
results = tk.Text(root, height=15, width=55)
results.pack(pady=10)


def scan():
    host = ip_entry.get()

    if host == "":
        results.delete("1.0", tk.END)
        results.insert(tk.END, "Please enter an IP address.\n")
        return

    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443]

    results.delete("1.0", tk.END)
    status_label.config(text="Scanning...")

    for port in ports:
        output = scan_port(host, port)

        if "OPEN" in output:
            results.insert(tk.END, output + "\n", "open")
        else:
            results.insert(tk.END, output + "\n", "closed")

    status_label.config(text="Scan Complete ✔")


def clear():
    results.delete("1.0", tk.END)
    status_label.config(text="")
    ip_entry.delete(0, tk.END)


# Buttons
scan_button = tk.Button(root, text="Scan", command=scan, width=15)
scan_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear", command=clear, width=15)
clear_button.pack(pady=5)

# Color tags
results.tag_config("open", foreground="green")
results.tag_config("closed", foreground="red")

root.mainloop()