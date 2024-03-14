from tkinter import ttk
from services import gol_service


class MenuView:
    def __init__(self, root, play_command, load_command, login_command):
        self._root = root
        self._frame = None
        self._play_command = play_command
        self._load_command = load_command
        self._login_command = login_command
        self._initialize()

    def _logout_handler(self):
        gol_service.logout()
        self.clear()
        self._initialize()
        self.pack()

    def _initialize_header(self):
        header = ttk.Label(
            master=self._frame,
            text="Game of Life",
            font=("Noto Mono", 30, 'bold')
        )
        header.grid(row=0, column=0, pady=10)

    def _initialize_playbutton(self):
        play_button = ttk.Button(
            master=self._frame,
            text="Play",
            command=self._play_command
        )
        play_button.grid(row=1, column=0, pady=10)

    def _initialize_loadbutton(self):
        load_button = ttk.Button(
            master=self._frame,
            text="Load",
            command=self._load_command
        )
        load_button.grid(row=2, column=0, pady=10)

    def _initialize_loginbutton(self):
        if gol_service.user():
            logout_button = ttk.Button(
                master=self._frame,
                text="Logout",
                command=self._logout_handler
            )
            logout_button.grid(row=3, column=0, pady=10)
        else:
            login_button = ttk.Button(
                master=self._frame,
                text="Login",
                command=self._login_command
            )
            login_button.grid(row=3, column=0, pady=10)

    def _initialize_quitbutton(self):
        quit_button = ttk.Button(
            master=self._frame,
            text="Quit",
            command=quit
        )
        quit_button.grid(row=4, column=0, pady=10)

    def _initialize_userinfo(self):
        if gol_service.user():
            account_info = ttk.Label(
                master=self._frame,
                text=f"Logged in as: {gol_service.user().username}",
                font=("Noto Mono", 10)
            )

            account_info.grid(row=5, column=0, pady=10)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)

        self._initialize_header()
        self._initialize_playbutton()
        self._initialize_loadbutton()
        self._initialize_loginbutton()
        self._initialize_quitbutton()
        self._initialize_userinfo()

        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(0, weight=1)

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def clear(self):
        self._frame.destroy()
