import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

# Sample malicious hashes (MD5)
MALICIOUS_HASHES = {
    "44d88612fea8a8f36de82e1278abb02f",  # EICAR test file
    "e99a18c428cb38d5f260853678922e03"   # Add more as needed
}

def calculate_md5(file_path):
    try:
        with open(file_path, "rb") as f:
            file_hash = hashlib.md5()
            while chunk := f.read(4096):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to read file:\n{e}")
        return None

def scan_file():
    file_path = filedialog.askopenfilename(title="Select a file to scan")
    if file_path:
        file_hash = calculate_md5(file_path)
        if file_hash:
            if file_hash in MALICIOUS_HASHES:
                result_label.config(text="⚠️ INFECTED FILE DETECTED", fg="#ff4c4c", bg="#ffe6e6")
            else:
                result_label.config(text="✅ File is SAFE", fg="#4caf50", bg="#e6ffe6")
            file_path_label.config(text=file_path)
            with open("scan_log.txt", "a") as log:
                log.write(f"{result_label.cget('text')}: {file_path}\n")
        else:
            result_label.config(text="Error scanning file.", fg="orange", bg="#fff3e6")

# GUI Setup
root = tk.Tk()
root.title("🛡️ Colorful Antivirus Scanner")
root.geometry("600x350")
root.configure(bg="#f0f8ff")

# Title
title_label = tk.Label(root, text="🛡️ Colorful Antivirus Scanner", font=("Helvetica", 20, "bold"), bg="#f0f8ff", fg="#333")
title_label.pack(pady=20)

# Scan Button
scan_button = tk.Button(root, text="🔍 Select File to Scan", command=scan_file,
                        font=("Helvetica", 14), bg="#4a90e2", fg="white", activebackground="#357ab7", padx=20, pady=10)
scan_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"), width=40, height=2)
result_label.pack(pady=20)

# File Path Label
file_path_label = tk.Label(root, text="", font=("Helvetica", 10), bg="#f0f8ff", wraplength=500)
file_path_label.pack(pady=5)

# Footer
footer = tk.Label(root, text="Developed for LA2 - Advanced Operating Systems", font=("Helvetica", 10), bg="#f0f8ff", fg="#666")
footer.pack(side="bottom", pady=10)

root.mainloop()