from tkinter import ttk


class LoginView:
    def __init__(self, root, login_command, register_command, back_to_menu_command):
        self._root = root
        self._frame = None
        self._login_command = login_command
        self._register_command = register_command
        self._cancel_command = back_to_menu_command
        self._header = None
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)
        self._header = ttk.Label(master=self._root,
                                 text="Login", font=("Noto Mono", 20, 'bold'))
        size_select_lable = ttk.Label(master=self._frame, text="Username:")
        username_box = ttk.Entry(master=self._frame)
        world_name_lable = ttk.Label(master=self._frame, text="Password:")
        password_box = ttk.Entry(master=self._frame)
        submit_button = ttk.Button(
            master=self._frame, text="Login", command=self._login_command)
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._cancel_command)
        register_button = ttk.Button(
            master=self._frame, text="Register", command=self._register_command)

        self._frame.grid_columnconfigure(0, weight=3)
        self._frame.grid_rowconfigure(0, weight=3)

        self._header.place(relx=0.5, rely=0.3, anchor='c')
        size_select_lable.grid(row=1, column=0)
        username_box.grid(row=1, column=1, pady=10, padx=10)
        world_name_lable.grid(row=2, column=0, pady=10, padx=10)
        password_box.grid(row=2, column=1, pady=10, padx=10)
        cancel_button.grid(row=3, column=0, pady=10, padx=10)
        submit_button.grid(row=3, column=1, pady=10, padx=10)
        register_button.grid(row=4, column=0, pady=10, padx=10)

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def clear(self):
        self._frame.destroy()
        self._header.destroy()
