import tkinter as tk

def create_transparent_window():
    root = tk.Tk()

    # Set the window title
    root.title("Aero-themed GUI Example")

    # Set the window size
    root.geometry("800x600")

    # Create a label with "Hello World" text
    label = tk.Label(root, text="Hello World", font=("Helvetica", 24))
    label.pack(padx=20, pady=50)

    # Load and display an imitation of the Windows 7 default startup background
    startup_background = tk.PhotoImage(file="bliss-600dpi.png")
    background_label = tk.Label(root, image=startup_background)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    background_label.lower()  # Place the background label behind other widgets

    # Set the window to be transparent (requires Windows OS)
    root.attributes("-alpha", 0.85)

    # Start the application's event loop
    root.mainloop()

# Call the function to create the transparent window
create_transparent_window()
