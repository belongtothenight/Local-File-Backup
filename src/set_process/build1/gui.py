
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x810")
window.configure(bg = "#0336BB")


canvas = Canvas(
    window,
    bg = "#0336BB",
    height = 810,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    570.0,
    68.0,
    anchor="nw",
    text="File Copying",
    fill="#FFFFFF",
    font=("ABeeZee", 50 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=106.0,
    y=179.0,
    width=300.0,
    height=50.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=570.0,
    y=179.0,
    width=300.0,
    height=50.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=570.0,
    y=627.0,
    width=300.0,
    height=50.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=1034.0,
    y=179.0,
    width=300.0,
    height=50.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=1204.0,
    y=344.0,
    width=180.0,
    height=60.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=1204.0,
    y=455.0,
    width=180.0,
    height=60.0
)

canvas.create_text(
    172.0,
    184.0,
    anchor="nw",
    text="Single File",
    fill="#000000",
    font=("Alatsi", 30 * -1)
)

canvas.create_text(
    570.0,
    184.0,
    anchor="nw",
    text="Single Folder",
    fill="#000000",
    font=("Alatsi Regular", 30 * -1)
)

canvas.create_text(
    570.0,
    631.0,
    anchor="nw",
    text="COPY",
    fill="#000000",
    font=("Alatsi Regular", 30 * -1)
)

canvas.create_text(
    1034.0,
    184.0,
    anchor="nw",
    text="Multi Folder",
    fill="#000000",
    font=("Alatsi Regular", 30 * -1)
)

canvas.create_text(
    56.0,
    336.0,
    anchor="nw",
    text="Source",
    fill="#FFFFFF",
    font=("Alatsi Regular", 30 * -1)
)

canvas.create_text(
    1204.0,
    344.0,
    anchor="nw",
    text="Browse",
    fill="#FFFFFF",
    font=("Alatsi Regular", 30 * -1)
)

canvas.create_text(
    1204.0,
    455.0,
    anchor="nw",
    text="Browse",
    fill="#FFFFFF",
    font=("Alatsi Regular", 30 * -1)
)

canvas.create_text(
    56.0,
    447.0,
    anchor="nw",
    text="Destination",
    fill="#FFFFFF",
    font=("Alatsi Regular", 30 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    720.0,
    374.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_1.place(
    x=270.0,
    y=344.0,
    width=900.0,
    height=58.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    720.0,
    485.0,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    highlightthickness=0
)
entry_2.place(
    x=270.0,
    y=455.0,
    width=900.0,
    height=58.0
)
window.resizable(False, False)
window.mainloop()
