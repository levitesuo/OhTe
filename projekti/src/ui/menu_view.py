from tkinter import ttk


class MenuView:
    def __init__(self, root, play_command, load_command, login_command):
        self._root = root
        self._frame = None
        self._play_command = play_command
        self._load_command = load_command
        self._login_command = login_command
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header = ttk.Label(master=self._frame,
                           text="Game of Life", font=("Noto Mono", 30, 'bold'))
        play_button = ttk.Button(
            master=self._frame, text="Play", command=self._play_command)
        load_button = ttk.Button(
            master=self._frame, text="Load", command=self._load_command)
        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._login_command)
        quit_button = ttk.Button(
            master=self._frame, text="Quit", command=quit)

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(0, weight=1)

        header.grid(row=3, column=0, pady=10)
        play_button.grid(row=4, column=0, pady=10)
        load_button.grid(row=5, column=0, pady=10)
        login_button.grid(row=6, column=0, pady=10)
        quit_button.grid(row=7, column=0, pady=10)

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')
