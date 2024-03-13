from tkinter import ttk
from services import gol_service


class RegisterView:
    def __init__(self, root, register_command, cancel_command):
        self._root = root
        self._frame = None
        self._register_command = register_command
        self._cancel_command = cancel_command
        self._header = None

        self._username_entry = None
        self._password_entry = None
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)
        self._header = ttk.Label(master=self._root,
                                 text="Register", font=("Noto Mono", 20, 'bold'))
        username_lable = ttk.Label(master=self._frame, text="Username:")
        self._username_entry = ttk.Entry(master=self._frame)
        password_lable = ttk.Label(master=self._frame, text="Password:")
        self._password_entry = ttk.Entry(master=self._frame)
        submit_button = ttk.Button(
            master=self._frame, text="Register", command=self._register_command)
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._cancel_command)

        self._frame.grid_columnconfigure(0, weight=3)
        self._frame.grid_rowconfigure(0, weight=3)

        self._header.place(relx=0.5, rely=0.3, anchor='c')
        username_lable.grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1, pady=10, padx=10)
        password_lable.grid(row=2, column=0, pady=10, padx=10)
        self._password_entry.grid(row=2, column=1, pady=10, padx=10)
        cancel_button.grid(row=3, column=0, pady=10, padx=10)
        submit_button.grid(row=3, column=1, pady=10, padx=10)

    def _create_user_handler(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        if len(username) == 0 or len(password) == 0:
            # Tähän pitäisi lisätä joku error viesti sitten kun jaksaa ihminen.
            return
        try:
            gol_service.register_user(username, password)
            self._create_user_handler()
        except:
            # TÄnne kans joku errorin tapanen :#
            return

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def clear(self):
        self._frame.destroy()
        self._header.destroy()
