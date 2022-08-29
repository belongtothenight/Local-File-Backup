import tkinter as tk
import lfb_lib as ll
from tkinter import filedialog
from os import system, getcwd
from os.path import isfile, isdir, exists
from time import sleep

system('cls')

window_size = '960x540+480+270'
window_hight = 540
window_width = 960
wwh = window_width / 2  # 480
background_color = '#002EA4'
orange_color = '#FFA216'
white_color = '#FFFFFF'
window_title = [
    'Local-File-Processor: Functionality Selection',
    'Local-File-Processor: File Copying',
    'Local-File-Processor: File Archiving',
    'Local-File-Processor: File Unpacking',
    'Local-File-Processor: File List Generator',
    'Local-File-Processor: Routine Execution Script Generator'
    'Local-File-Processor: Settings'
]
canvas_title = [
    'Functionality Selection',
    'File Copying',
    'File Archiving',
    'File Unpacking',
    'File List Generator',
    'Routine Execution Script Generator'
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
    'Browse',
    'Browse'
], [
    'Back',
    'Exit',
    'Confirm',
    'Browse',
    'Browse'
]
]
# log = []

'''Defaul Variables'''
# Filter Array
filter_1 = [
    True,
    [None],  # ['.txt'],
    [['07-31'], ['log_2022-07-31_1.txt']],
    [16000, 48000],
    [None, None],  # use time.mktime(9-tuple) to generate time code
    [None, None],  # use time.mktime(9-tuple) to generate time code
    [None, None]  # use time.mktime(9-tuple) to generate time code
]  # for filter_file
filter_2 = [
    True,
    None,  # not implemented
    [[None], ['src']],
    None,  # not implemented
    [None, None],  # use time.mktime(9-tuple) to generate time code
    [None, None],  # use time.mktime(9-tuple) to generate time code
    [None, None]  # use time.mktime(9-tuple) to generate time code
]  # for filter_folder

# Global Flag Variable
print_flag = [
    True,  # print in main
    True,  # print in processes of lib file
    True  # print in sub-functions of lib file
]
file_log_flag = [
    True,  # src file log flag associate with functions
    True,  # file log file of random location
    True,  # execution log flag
]

# Function Enable Array
function_enable = [
    ['Single_file_copy', True],  # single file copy
    ['Single_folder_copy', True],  # single folder copy
    ['Multi_folder_copy', True],  # multi file copy
    ['Single_file_archive', True],  # single file archive
    ['Single_folder_archive', True],  # single folder archive
    ['Multi_folder_archive', True],  # multi file archive
    ['Single_file_unpack', True],  # single file unpack
    ['Single_folder_unpack', True],  # single folder unpack
    ['Multi_folder_unpack', True]  # multi file unpack
]


class MainProcess():
    def __init__(self):
        # self.progress = 0
        # self.log = []
        pass

    def single_file_copy(self):
        pass

    def single_folder_copy(self):
        pass

    def multi_folder_copy(self):
        pass

    def single_file_archive(self):
        pass

    def single_folder_archive(self):
        pass

    def multi_folder_archive(self):
        pass

    def single_file_unpack(self):
        pass

    def single_folder_unpack(self):
        pass

    def multi_folder_unpack(self):
        pass

    def file_log_generation(self, filename, location, dst_path):
        log = []
        file_info, log = ll.get_file_info(
            location, dst_path, log, [None], print_flag[2])
        if file_log_flag[1]:
            ll.export_file_log(filename, file_info, dst_path)

    def process_file_generation(self):
        pass

    def routine_execution_script_generation(self):
        pass


class Window(tk.Tk, MainProcess):
    status = [
        0,  # window number
        0,  # status number
        0, 0, 0, 0, 0, 0, 0, 0  # status count
    ]
    mode_selection = 3  # 1: single file, 2: single folder, 3: multiple folders

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
        self.src = tk.StringVar()
        self.dst = tk.StringVar()
        self.filename = tk.StringVar(self, value='accessible_files')

    '''window element'''

    def set_entry_window_element(self):
        self.canvas = tk.Canvas(
            self,
            bg=background_color,
            height=window_hight,
            width=window_width,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            wwh,
            60,
            anchor="center",
            text=canvas_title[0],
            fill="#FFFFFF",
            font=("ABeeZee", 40)
        )
        self.button_1 = tk.Button(
            self,
            text=button_text[0][0],
            font=("Consolas", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(1)
        )
        self.button_1.place(
            x=wwh,
            y=140,
            width=800.0,
            height=50.0,
            anchor="center"
        )
        self.button_2 = tk.Button(
            self,
            text=button_text[0][1],
            font=("Consolas", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(2)
        )
        self.button_2.place(
            x=wwh,
            y=200,
            width=800.0,
            height=50.0,
            anchor="center"
        )
        self.button_3 = tk.Button(
            self,
            text=button_text[0][2],
            font=("Consolas", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(3)
        )
        self.button_3.place(
            x=wwh,
            y=260,
            width=800.0,
            height=50.0,
            anchor="center"
        )
        self.button_4 = tk.Button(
            self,
            text=button_text[0][3],
            font=("Consolas", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(4)
        )
        self.button_4.place(
            x=wwh,
            y=320,
            width=800.0,
            height=50.0,
            anchor="center"
        )
        self.button_5 = tk.Button(
            self,
            text=button_text[0][4],
            font=("Consolas", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(5)
        )
        self.button_5.place(
            x=wwh,
            y=380,
            width=800.0,
            height=50.0,
            anchor="center"
        )
        self.button_6 = tk.Button(
            self,
            text=button_text[0][5],
            font=("Consolas", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(6)
        )
        self.button_6.place(
            x=wwh,
            y=480,
            width=800.0,
            height=50.0,
            anchor="center"
        )

    def set_copy_window_element(self):
        self.update()
        self.canvas = tk.Canvas(
            self,
            bg=background_color,
            height=window_hight,
            width=window_width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            wwh,
            60,
            anchor="center",
            text=canvas_title[1],
            fill=white_color,
            font=("ABeeZee", 40)
        )
        self.canvas.create_text(
            110,
            240,
            anchor="center",
            text="SRC",
            fill=white_color,
            font=("Consolas", 25, 'bold')
        )
        self.canvas.create_text(
            110,
            340,
            anchor="center",
            text="DST",
            fill=white_color,
            font=("Consolas", 25, 'bold')
        )
        self.button_1 = tk.Button(
            self,
            text=button_text[1][0],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(1)
        )
        self.button_1.place(
            x=wwh-250,
            y=150,
            width=250.0,
            height=50.0,
            anchor='center'
        )
        self.button_2 = tk.Button(
            self,
            text=button_text[1][1],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(2)
        )
        self.button_2.place(
            x=wwh,
            y=150,
            width=250.0,
            height=50.0,
            anchor='center'
        )
        self.button_3 = tk.Button(
            self,
            text=button_text[1][2],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(3)
        )
        self.button_3.place(
            x=wwh+250,
            y=150,
            width=250.0,
            height=50.0,
            anchor='center'
        )
        self.button_4 = tk.Button(
            self,
            text=button_text[1][3],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(4)
        )
        self.button_4.place(
            x=260,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_5 = tk.Button(
            self,
            text=button_text[1][4],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(5)
        )
        self.button_5.place(
            x=460,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_6 = tk.Button(
            self,
            text=button_text[1][5],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(6)
        )
        self.button_6.place(
            x=660,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_7 = tk.Button(
            self,
            text=button_text[1][6],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=orange_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(7)
        )
        self.button_7.place(
            x=835,
            y=240,
            width=150.0,
            height=50.0,
            anchor="center"
        )
        self.button_8 = tk.Button(
            self,
            text=button_text[1][7],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=orange_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(8)
        )
        self.button_8.place(
            x=835,
            y=340,
            width=150.0,
            height=50.0,
            anchor="center"
        )
        self.entry_1 = tk.Entry(
            self,
            font=("Cascadia Code", 15),
            textvariable=self.src
        )
        self.entry_1.place(
            x=460,
            y=240,
            width=600.0,
            height=50.0,
            anchor="center"
        )
        self.entry_2 = tk.Entry(
            font=("Cascadia Code", 15),
            textvariable=self.dst
        )
        self.entry_2.place(
            x=460,
            y=340,
            width=600.0,
            height=50.0,
            anchor="center"
        )

    def set_archive_window_element(self):
        self.update()
        self.canvas = tk.Canvas(
            self,
            bg=background_color,
            height=window_hight,
            width=window_width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            wwh,
            60,
            anchor="center",
            text=canvas_title[2],
            fill=white_color,
            font=("ABeeZee", 40)
        )
        self.canvas.create_text(
            110,
            240,
            anchor="center",
            text="SRC",
            fill=white_color,
            font=("Consolas", 25, 'bold')
        )
        self.canvas.create_text(
            110,
            340,
            anchor="center",
            text="DST",
            fill=white_color,
            font=("Consolas", 25, 'bold')
        )
        self.button_1 = tk.Button(
            self,
            text=button_text[1][0],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(1)
        )
        self.button_1.place(
            x=wwh-250,
            y=150,
            width=250.0,
            height=50.0,
            anchor='center'
        )
        self.button_2 = tk.Button(
            self,
            text=button_text[1][1],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(2)
        )
        self.button_2.place(
            x=wwh,
            y=150,
            width=250.0,
            height=50.0,
            anchor='center'
        )
        self.button_3 = tk.Button(
            self,
            text=button_text[1][2],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(3)
        )
        self.button_3.place(
            x=wwh+250,
            y=150,
            width=250.0,
            height=50.0,
            anchor='center'
        )
        self.button_4 = tk.Button(
            self,
            text=button_text[1][3],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(4)
        )
        self.button_4.place(
            x=260,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_5 = tk.Button(
            self,
            text=button_text[1][4],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(5)
        )
        self.button_5.place(
            x=460,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_6 = tk.Button(
            self,
            text=button_text[1][5],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(6)
        )
        self.button_6.place(
            x=660,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_7 = tk.Button(
            self,
            text=button_text[1][6],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=orange_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(7)
        )
        self.button_7.place(
            x=835,
            y=240,
            width=150.0,
            height=50.0,
            anchor="center"
        )
        self.button_8 = tk.Button(
            self,
            text=button_text[1][7],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=orange_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(8)
        )
        self.button_8.place(
            x=835,
            y=340,
            width=150.0,
            height=50.0,
            anchor="center"
        )
        self.entry_1 = tk.Entry(
            self,
            font=("Cascadia Code", 15),
            textvariable=self.src
        )
        self.entry_1.place(
            x=460,
            y=240,
            width=600.0,
            height=50.0,
            anchor="center"
        )
        self.entry_2 = tk.Entry(
            font=("Cascadia Code", 15),
            textvariable=self.dst
        )
        self.entry_2.place(
            x=460,
            y=340,
            width=600.0,
            height=50.0,
            anchor="center"
        )

    def set_unpack_window_element(self):
        self.update()
        self.canvas = tk.Canvas(
            self,
            bg=background_color,
            height=window_hight,
            width=window_width,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            wwh,
            60,
            anchor="center",
            text=canvas_title[2],
            fill=white_color,
            font=("ABeeZee", 40)
        )
        self.canvas.create_text(
            110,
            240,
            anchor="center",
            text="SRC",
            fill=white_color,
            font=("Consolas", 25, 'bold')
        )
        self.canvas.create_text(
            110,
            340,
            anchor="center",
            text="DST",
            fill=white_color,
            font=("Consolas", 25, 'bold')
        )
        self.button_1 = tk.Button(
            self,
            text=button_text[1][0],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(1)
        )
        self.button_1.place(
            x=wwh-250,
            y=150,
            width=250.0,
            height=50.0,
            anchor='center'
        )
        self.button_2 = tk.Button(
            self,
            text=button_text[1][1],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(2)
        )
        self.button_2.place(
            x=wwh,
            y=150,
            width=250.0,
            height=50.0,
            anchor='center'
        )
        self.button_3 = tk.Button(
            self,
            text=button_text[1][2],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(3)
        )
        self.button_3.place(
            x=wwh+250,
            y=150,
            width=250.0,
            height=50.0,
            anchor='center'
        )
        self.button_4 = tk.Button(
            self,
            text=button_text[1][3],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(4)
        )
        self.button_4.place(
            x=260,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_5 = tk.Button(
            self,
            text=button_text[1][4],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(5)
        )
        self.button_5.place(
            x=460,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_6 = tk.Button(
            self,
            text=button_text[1][5],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(6)
        )
        self.button_6.place(
            x=660,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_7 = tk.Button(
            self,
            text=button_text[1][6],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=orange_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(7)
        )
        self.button_7.place(
            x=835,
            y=240,
            width=150.0,
            height=50.0,
            anchor="center"
        )
        self.button_8 = tk.Button(
            self,
            text=button_text[1][7],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=orange_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(8)
        )
        self.button_8.place(
            x=835,
            y=340,
            width=150.0,
            height=50.0,
            anchor="center"
        )
        self.entry_1 = tk.Entry(
            self,
            font=("Cascadia Code", 15),
            textvariable=self.src
        )
        self.entry_1.place(
            x=460,
            y=240,
            width=600.0,
            height=50.0,
            anchor="center"
        )
        self.entry_2 = tk.Entry(
            font=("Cascadia Code", 15),
            textvariable=self.dst
        )
        self.entry_2.place(
            x=460,
            y=340,
            width=600.0,
            height=50.0,
            anchor="center"
        )

    def set_file_list_generator_window_element(self):
        self.canvas = tk.Canvas(
            self,
            bg=background_color,
            height=window_hight,
            width=window_width,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.canvas.create_text(
            wwh,
            60,
            anchor="center",
            text=canvas_title[4],
            fill="#FFFFFF",
            font=("ABeeZee", 40)
        )
        self.canvas.create_text(
            150,
            140,
            anchor="center",
            text="Filename",
            fill=white_color,
            font=("Consolas", 25, 'bold')
        )
        self.canvas.create_text(
            800,
            140,
            anchor="center",
            text=".csv",
            fill=white_color,
            font=("Consolas", 25, 'bold')
        )
        self.canvas.create_text(
            110,
            240,
            anchor="center",
            text="SRC",
            fill=white_color,
            font=("Consolas", 25, 'bold')
        )
        self.canvas.create_text(
            110,
            340,
            anchor="center",
            text="DST",
            fill=white_color,
            font=("Consolas", 25, 'bold')
        )
        self.button_4 = tk.Button(
            self,
            text=button_text[1][3],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(4)
        )
        self.button_4.place(
            x=260,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_5 = tk.Button(
            self,
            text=button_text[1][4],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(5)
        )
        self.button_5.place(
            x=460,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_6 = tk.Button(
            self,
            text=button_text[1][5],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=background_color,
            activeforeground=background_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(6)
        )
        self.button_6.place(
            x=660,
            y=480,
            width=200.0,
            height=50.0,
            anchor="center"
        )
        self.button_7 = tk.Button(
            self,
            text=button_text[1][6],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=orange_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(7)
        )
        self.button_7.place(
            x=835,
            y=240,
            width=150.0,
            height=50.0,
            anchor="center"
        )
        self.button_8 = tk.Button(
            self,
            text=button_text[1][7],
            font=("Carlito", 25, 'bold'),
            fg=white_color,
            bg=orange_color,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            command=lambda: self.button_click(8)
        )
        self.button_8.place(
            x=835,
            y=340,
            width=150.0,
            height=50.0,
            anchor="center"
        )
        self.entry_1 = tk.Entry(
            self,
            font=("Cascadia Code", 15),
            textvariable=self.src
        )
        self.entry_1.place(
            x=460,
            y=240,
            width=600.0,
            height=50.0,
            anchor="center"
        )
        self.entry_2 = tk.Entry(
            font=("Cascadia Code", 15),
            textvariable=self.dst
        )
        self.entry_2.place(
            x=460,
            y=340,
            width=600.0,
            height=50.0,
            anchor="center"
        )
        self.entry_3 = tk.Entry(
            font=("Cascadia Code", 15),
            textvariable=self.filename
        )
        self.entry_3.place(
            x=250,
            y=140,
            width=510.0,
            height=50.0,
            anchor="w"
        )

    def set_routine_execution_script_generator_window_element(self):
        pass

    '''widget operation'''

    def path_selection(self, value1, value2):
        if value1 == 1 and value2 == 1:
            self.src = filedialog.askopenfile(
                initialdir=getcwd(),
                title='Local-File-Processor: Select File',
                filetypes=(('All Files', '*.*'), ('Text Files', '*.txt'))
            )
            self.src = self.src.name
            self.entry_1.insert(0, self.src)
        elif (value1 == 1 and value2 == 2) or (value1 == 1 and value2 == 3):
            self.src = filedialog.askdirectory(
                initialdir=getcwd(),
                title='Local-File-Processor: Select Folder'
            )
            self.entry_1.insert(0, self.src)
        elif value1 == 2 and value2 == 1:
            self.dst = filedialog.askdirectory(
                initialdir=getcwd(),
                title='Local-File-Processor: Select Folder'
            )
            self.entry_2.insert(0, self.dst)

    def button_action(self):
        # Handling actions inside GUI
        # print("[LOG] Clicked Window/Button/Window Name/Button Name: "
        #   + str(self.status[0]) + "/" + str(self.status[1]) + "/"
        #   + str(canvas_title[self.status[0]]) + "/" + str(button_text[self.status[0]-2][self.status[1]-1]))
        if self.status[0] == 0:
            # entry window
            if self.status[1] in [1, 2, 3, 4, 5, 6]:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
        elif self.status[0] == 1:
            # copy window
            if self.status[1] == 1:
                if self.status[2] % 2 == 1:
                    self.button_1.config(bg=orange_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 1
                else:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 0
            elif self.status[1] == 2:
                if self.status[3] % 2 == 1:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=orange_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 2
                else:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 0
            elif self.status[1] == 3:
                if self.status[4] % 2 == 1:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=orange_color)
                    self.mode_selection = 3
                else:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 0
            elif self.status[1] == 4:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
            elif self.status[1] == 5:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
            elif self.status[1] == 6:
                try:
                    a = exists(self.src)
                except:
                    a = False
                try:
                    b = exists(self.dst)
                except:
                    b = False
                if a and b:
                    self.destroy()
            elif self.status[1] == 7:
                if self.mode_selection == 0:
                    pass
                elif self.mode_selection == 1:
                    self.path_selection(1, 1)
                elif self.mode_selection == 2:
                    self.path_selection(1, 2)
                elif self.mode_selection == 3:
                    self.path_selection(1, 3)
            elif self.status[1] == 8:
                self.path_selection(2, 1)
        elif self.status[0] == 2:
            # archive window
            if self.status[1] == 1:
                if self.status[2] % 2 == 1:
                    self.button_1.config(bg=orange_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 1
                else:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 0
            elif self.status[1] == 2:
                if self.status[3] % 2 == 1:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=orange_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 2
                else:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 0
            elif self.status[1] == 3:
                if self.status[4] % 2 == 1:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=orange_color)
                    self.mode_selection = 3
                else:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 0
            elif self.status[1] == 4:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
            elif self.status[1] == 5:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
            elif self.status[1] == 6:
                try:
                    a = exists(self.src)
                except:
                    a = False
                try:
                    b = exists(self.dst)
                except:
                    b = False
                if a and b:
                    self.destroy()
            elif self.status[1] == 7:
                if self.mode_selection == 0:
                    pass
                elif self.mode_selection == 1:
                    self.path_selection(1, 1)
                elif self.mode_selection == 2:
                    self.path_selection(1, 2)
                elif self.mode_selection == 3:
                    self.path_selection(1, 3)
            elif self.status[1] == 8:
                self.path_selection(2, 1)
        elif self.status[0] == 3:
            # archive window
            if self.status[1] == 1:
                if self.status[2] % 2 == 1:
                    self.button_1.config(bg=orange_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 1
                else:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 0
            elif self.status[1] == 2:
                if self.status[3] % 2 == 1:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=orange_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 2
                else:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 0
            elif self.status[1] == 3:
                if self.status[4] % 2 == 1:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=orange_color)
                    self.mode_selection = 3
                else:
                    self.button_1.config(bg=background_color)
                    self.button_2.config(bg=background_color)
                    self.button_3.config(bg=background_color)
                    self.mode_selection = 0
            elif self.status[1] == 4:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
            elif self.status[1] == 5:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
            elif self.status[1] == 6:
                try:
                    a = exists(self.src)
                except:
                    a = False
                try:
                    b = exists(self.dst)
                except:
                    b = False
                if a and b:
                    self.destroy()
            elif self.status[1] == 7:
                if self.mode_selection == 0:
                    pass
                elif self.mode_selection == 1:
                    self.path_selection(1, 1)
                elif self.mode_selection == 2:
                    self.path_selection(1, 2)
                elif self.mode_selection == 3:
                    self.path_selection(1, 3)
            elif self.status[1] == 8:
                self.path_selection(2, 1)
        elif self.status[0] == 4:
            # copy window
            if self.status[1] == 4:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
            elif self.status[1] == 5:
                print("[LOG] Closed " + canvas_title[self.status[0]] + " Window")
                self.destroy()
            elif self.status[1] == 6:
                self.src = self.entry_1.get()
                self.dst = self.entry_2.get()
                self.filename = self.entry_3.get()
                if self.filename == '':
                    c = False
                else:
                    c = True
                try:
                    a = exists(self.src)
                except:
                    a = False
                try:
                    b = exists(self.dst)
                except:
                    b = False
                if a and b and c:
                    # start updating progress bar
                    MainProcess.file_log_generation(
                        self, self.filename, self.src, self.dst)
            elif self.status[1] == 7:
                self.path_selection(1, 2)
            elif self.status[1] == 8:
                self.path_selection(2, 1)
        elif self.status[0] == 5:
            pass

    def button_click(self, num):
        self.status[1] = num
        self.status[num+1] += 1
        print("[LOG] Button status: " + str(self.status))
        self.button_action()

    '''window operation'''

    def show_window(self):
        self.focus_force()
        self.mainloop()


class WindowsProcess():
    status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    filename = None
    src = None
    dst = None

    def show_status(self):
        print("[LOG] Status: " + str(self.status))

    def show_path(self):
        print("[LOG] Source: " + str(self.src))
        print("[LOG] Destination: " + str(self.dst))

    def show_data_file_list_generator(self):
        print("[LOG] Status: " + str(self.status))
        print("[LOG] Filename: " + str(self.filename))
        print("[LOG] Source: " + str(self.src))
        print("[LOG] Destination: " + str(self.dst))

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
        self.src = copy_window.src
        self.dst = copy_window.dst

    def archive_process(self):
        Window.status = [2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        archive_window = Window(window_size, background_color)
        archive_window.set_archive_window_element()
        archive_window.show_window()
        self.status = archive_window.status
        self.src = archive_window.src
        self.dst = archive_window.dst

    def unpack_process(self):
        Window.status = [3, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        unpack_window = Window(window_size, background_color)
        unpack_window.set_unpack_window_element()
        unpack_window.show_window()
        self.status = unpack_window.status
        self.src = unpack_window.src
        self.dst = unpack_window.dst

    def file_list_generator_process(self):
        Window.status = [4, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        file_list_generator_window = Window(window_size, background_color)
        file_list_generator_window.set_file_list_generator_window_element()
        file_list_generator_window.show_window()
        self.status = file_list_generator_window.status
        self.filename = file_list_generator_window.filename
        self.src = file_list_generator_window.src
        self.dst = file_list_generator_window.dst

    def routine_execution_script_generator_process(self):
        Window.status = [5, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        routine_execution_script_generator_window = Window(
            window_size, background_color)
        routine_execution_script_generator_window.set_routine_execution_script_generator_window_element()
        routine_execution_script_generator_window.show_window()
        self.status = routine_execution_script_generator_window.status
        self.dst = routine_execution_script_generator_window.dst


def main():
    wp = WindowsProcess()
    wp.entry_process()
    wp.show_status()
    wp.show_path()
    if wp.status[1] == 1:
        wp.copy_process()
        wp.show_status()
        wp.show_path()
        while wp.status[1] == 4:
            # back button of copy window
            main()
            break
    elif wp.status[1] == 2:
        wp.archive_process()
        wp.show_status()
        wp.show_path()
        while wp.status[1] == 4:
            # back button of copy window
            main()
            break
    elif wp.status[1] == 3:
        wp.unpack_process()
        wp.show_status()
        wp.show_path()
        while wp.status[1] == 4:
            # back button of copy window
            main()
            break
    elif wp.status[1] == 4:
        wp.file_list_generator_process()
        wp.show_data_file_list_generator()
        while wp.status[1] == 4:
            # back button of copy window
            main()
            break
    elif wp.status[1] == 5:
        wp.routine_execution_script_generator_process()
        wp.show_status()
        wp.show_path()
        while wp.status[1] == 4:
            # back button of copy window
            main()
            break


if __name__ == '__main__':
    main()
    # system('cmd /k')  # disable if not executed in cmd

'''
https://stackoverflow.com/questions/10039485/tkinter-runtimeerror-maximum-recursion-depth-exceeded
'''
