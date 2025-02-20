import tkinter as tk
from tkinter import font, ttk

def show_font_preview():
    preview_window = tk.Tk()
    preview_window.title("Font Preview")
    preview_window.geometry("800x600")
    
    # Create a canvas with scrollbar
    canvas = tk.Canvas(preview_window)
    scrollbar = ttk.Scrollbar(preview_window, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Get all available fonts
    fonts = list(font.families())
    fonts.sort()  # Sort alphabetically

    # Sample text
    sample_text = "Hello World! 123"
    
    # Create labels with different fonts
    for font_name in fonts:
        try:
            label = tk.Label(
                scrollable_frame, 
                text=f"{font_name}: {sample_text}", 
                font=(font_name, 14)
            )
            label.pack(pady=5, padx=10, anchor="w")
        except:
            # Skip fonts that can't be rendered
            continue

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    preview_window.mainloop()

# Create a button to show the preview
root = tk.Tk()
preview_button = tk.Button(root, text="Show Font Preview", command=show_font_preview)
preview_button.pack(padx=20, pady=20)
root.mainloop()