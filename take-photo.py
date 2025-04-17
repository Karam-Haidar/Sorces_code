from picamera2 import Picamera2
from PIL import Image, ImageTk
import tkinter as tk
import time

# Initialize camera
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)})
picam2.configure(config)
picam2.start()

# GUI window
window = tk.Tk()
window.title("Camera Preview")

label = tk.Label(window)
label.pack()

def update_frame():
    frame = picam2.capture_array()
    image = Image.fromarray(frame)
    tk_image = ImageTk.PhotoImage(image=image)
    label.config(image=tk_image)
    label.image = tk_image
    window.after(10, update_frame)

# Save photo when spacebar is pressed
def take_photo(event):
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    filename = f"photo_{timestamp}.jpg"
    frame = picam2.capture_array()
    Image.fromarray(frame).save(filename)
    print(f"Photo saved: {filename}")

# Bind spacebar
window.bind("<space>", take_photo)

# Start loop
update_frame()
window.mainloop()

# Cleanup
picam2.stop()
