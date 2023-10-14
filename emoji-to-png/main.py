import tkinter as tk
from PIL import Image, ImageTk, ImageFont, ImageDraw

def convert_emoji_to_png(emoji):
    # Set the font size and type
    font_size = 100
    font = ImageFont.truetype("arial.ttf", font_size)

    # Get the size of the text
    text_size = font.getbbox(emoji)

    # Create a new image with a white background
    image = Image.new("RGB", text_size, (255, 255, 255))

    # Draw the emoji on the image
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), emoji, font=font, fill=(0, 0, 0))

    return image

def on_convert_button_click():
    # Get the emoji from the text entry
    emoji = emoji_entry.get()

    # Convert the emoji to a PNG
    image = convert_emoji_to_png(emoji)

    # Display the PNG in the label
    photo = ImageTk.PhotoImage(image)
    image_label.configure(image=photo)
    image_label.image = photo

# Create the main window
window = tk.Tk()
window.title("Emoji to PNG Converter")

# Create the text entry
emoji_entry = tk.Entry(window)
emoji_entry.pack()

# Create the convert button
convert_button = tk.Button(window, text="Convert", command=on_convert_button_click)
convert_button.pack()

# Create the label to display the PNG
image_label = tk.Label(window)
image_label.pack()

# Run the main event loop
window.mainloop()
