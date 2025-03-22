import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showerror("Error", "Please enter a valid URL or text")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img = img.resize((250, 250), Image.Resampling.LANCZOS)
    img = ImageTk.PhotoImage(img)
    
    qr_label.config(image=img)
    qr_label.image = img
    
    global generated_qr
    generated_qr = qr.make_image(fill="black", back_color="white")

def save_qr():
    if generated_qr is None:
        messagebox.showerror("Error", "No QR code to save")
        return
    
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        generated_qr.save(file_path)
        messagebox.showinfo("Success", "QR Code saved successfully!")

generated_qr = None

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")

label = tk.Label(root, text="Enter any URL or text:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

button_generate = tk.Button(root, text="Generate QR Code", command=generate_qr)
button_generate.pack(pady=5)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

button_save = tk.Button(root, text="Save QR Code", command=save_qr)
button_save.pack(pady=5)

root.mainloop()
