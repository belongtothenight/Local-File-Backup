import tkinter as tk
from os import system
from time import sleep

system('cls')

window_size = '960x540+480+270'
background_color = '#002EA4'
window_title = [
    'Local-File-Processor: Functionality Selection',
    'Local-File-Processor: File Copying'
]
canvas_title = [
    'Functionality Selection',
    'File Copying'
]
button_text = [[
    'COPY',
    'ARCHIVE',
    'UNPACK',
    'FILE LIST GENERATOR',
    'ROUTINE EXECUTION SCRIPT GENERATOR',
    'EXIT'
], [
    'Single File',
    'Single Folder',
    'Multiple Folders',
    'Back',
    'Exit',
    'Confirm',
    'Browse SRC',
    'Browse DST'
]
]


class Window(tk.Tk):
    status = [
        0,  # window number
        0,  # status number
        0, 0, 0, 0, 0, 0, 0, 0  # status count
    ]

    def __init__(self, size, color):
        '''Window Restart Refresh'''
        # self.status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # refresh status count
        import tkinter as tk  # enable reopening different windows

        '''Window Setting'''
        tk.Tk.__init__(self)
        self.geometry(size)
        self.title(window_title[0])
        # icon = PhotoImage(file='icon.png')
        # iconphoto(True, icon)
        self.config(background=color)
        self.resizable(False, False)

    '''window element'''

    def set_entry_window_element(self):
        canvas = tk.Canvas(
            self,
            bg=background_color,
            height=540,
            width=960,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_text(
            480,
            60,
            anchor="center",
            text=canvas_title[0],
            fill="#FFFFFF",
            font=("ABeeZee", 40)
        )
        button_1 = tk.Button(
            self,
            text='COPY',
            font=("Consolas", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(1)
        )
        button_1.place(
            x=480,
            y=140,
            width=800.0,
            height=50.0,
            anchor="center"
        )
        button_2 = tk.Button(
            self,
            text='ARCHIVE',
            font=("Consolas", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(2)
        )
        button_2.place(
            x=480,
            y=200,
            width=800.0,
            height=50.0,
            anchor="center"
        )
        button_3 = tk.Button(
            self,
            text='UNPACK',
            font=("Consolas", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(3)
        )
        button_3.place(
            x=480,
            y=260,
            width=800.0,
            height=50.0,
            anchor="center"
        )
        button_4 = tk.Button(
            self,
            text='FILE LIST GENERATOR',
            font=("Consolas", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(4)
        )
        button_4.place(
            x=480,
            y=320,
            width=800.0,
            height=50.0,
            anchor="center"
        )
        button_5 = tk.Button(
            self,
            text='ROUTINE EXECUTION SCRIPT GENERATOR',
            font=("Consolas", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(5)
        )
        button_5.place(
            x=480,
            y=380,
            width=800.0,
            height=50.0,
            anchor="center"
        )
        button_6 = tk.Button(
            self,
            text='EXIT',
            font=("Consolas", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(6)
        )
        button_6.place(
            x=480,
            y=480,
            width=800.0,
            height=50.0,
            anchor="center"
        )

    def set_copy_window_element(self):
        self.update()
        canvas = tk.Canvas(
            self,
            bg=background_color,
            height=540,
            width=960,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.place(x=0, y=0)
        canvas.create_text(
            480,
            60,
            anchor="center",
            text=canvas_title[1],
            fill="#FFFFFF",
            font=("ABeeZee", 40)
        )
        canvas.create_text(
            110,
            240,
            anchor="center",
            text="SRC",
            fill="#FFFFFF",
            font=("Consolas", 25, 'bold')
        )
        canvas.create_text(
            110,
            340,
            anchor="center",
            text="DST",
            fill="#FFFFFF",
            font=("Consolas", 25, 'bold')
        )
        button_1 = tk.Button(
            self,
            text='Single File',
            font=("Carlito", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(1)
        )
        button_1.place(
            x=130,
            y=120,
            width=200.0,
            height=50.0,
            anchor="nw"
        )
        button_2 = tk.Button(
            self,
            text='Single Folder',
            font=("Carlito", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(2)
        )
        button_2.place(
            x=380,
            y=120,
            width=200.0,
            height=50.0,
            anchor="nw"
        )
        button_3 = tk.Button(
            self,
            text='Multi Folder',
            font=("Carlito", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(3)
        )
        button_3.place(
            x=630,
            y=120,
            width=200.0,
            height=50.0,
            anchor="nw"
        )
        button_4 = tk.Button(
            self,
            text='Back',
            font=("Carlito", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(4)
        )
        button_4.place(
            x=260,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        button_5 = tk.Button(
            self,
            text='Exit',
            font=("Carlito", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(5)
        )
        button_5.place(
            x=460,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        button_6 = tk.Button(
            self,
            text='Confirm',
            font=("Carlito", 25, 'bold'),
            fg='#FFFFFF',
            bg='#002EA4',
            activeforeground='#002EA4',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(6)
        )
        button_6.place(
            x=660,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        button_7 = tk.Button(
            self,
            text='Browse',
            font=("Carlito", 25, 'bold'),
            fg='#FFFFFF',
            bg='#FFA216',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(7)
        )
        button_7.place(
            x=835,
            y=240,
            width=150.0,
            height=50.0,
            anchor="center"
        )
        button_8 = tk.Button(
            self,
            text='Browse',
            font=("Carlito", 25, 'bold'),
            fg='#FFFFFF',
            bg='#FFA216',
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(8)
        )
        button_8.place(
            x=835,
            y=340,
            width=150.0,
            height=50.0,
            anchor="center"
        )
        entry_1 = tk.Entry(
            self,
            font=("Cascadia Code", 15),
            # textvariable=src
        )
        entry_1.place(
            x=460,
            y=240,
            width=600.0,
            height=50.0,
            anchor="center"
        )
        entry_2 = tk.Entry(
            font=("Cascadia Code", 15),
            # textvariable=dst
        )
        entry_2.place(
            x=460,
            y=340,
            width=600.0,
            height=50.0,
            anchor="center"
        )

    '''widget operation'''

    def button_action(self):
        # Handling actions inside GUI
        print("[LOG] Clicked Window/Button/Window Name/Button Name: "
              + str(self.status[0]) + "/" + str(self.status[1]) + "/"
              + str(canvas_title[self.status[0]]) + "/" + str(button_text[self.status[0]][self.status[1]-1]))
        if self.status[0] == 0:
            if self.status[1] in [1, 2, 3, 4, 5, 6]:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
        elif self.status[0] == 1:
            if self.status[1] == 1:
                print("[LOG] 1")
            elif self.status[1] == 2:
                print("[LOG] 2")
            elif self.status[1] == 3:
                print("[LOG] 3")
            elif self.status[1] == 4:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
            elif self.status[1] == 5:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
            elif self.status[1] == 6:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
            elif self.status[1] == 7:
                print("[LOG] 7")
            elif self.status[1] == 8:
                print("[LOG] 8")

    def button_click(self, num):
        self.status[1] = num
        self.status[num+1] += 1
        print("[LOG] Button status: " + str(self.status))
        self.button_action()

    '''window operation'''

    def show_window(self):
        self.focus_force()
        self.mainloop()

    def close_window(self):
        self.destroy()


class WindowsProcess():
    status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self):
        pass

    def show_status(self):
        print("[LOG] Status: " + str(self.status))

    def entry_process(self):
        Window.status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        entry_window = Window(window_size, background_color)
        entry_window.set_entry_window_element()
        entry_window.show_window()
        self.status = entry_window.status

    def copy_process(self):
        Window.status = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        copy_window = Window(window_size, background_color)
        copy_window.set_copy_window_element()
        copy_window.show_window()
        self.status = copy_window.status


def main():
    wp = WindowsProcess()
    wp.entry_process()
    wp.show_status()
    if wp.status[1] == 1:
        wp.copy_process()
        wp.show_status()
        while wp.status[1] == 4:
            # back button of copy window
            main()
            break


if __name__ == '__main__':
    main()
    system('cmd /k')  # disable if not executed in cmd

'''
https://stackoverflow.com/questions/10039485/tkinter-runtimeerror-maximum-recursion-depth-exceeded
'''
