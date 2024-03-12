from tkinter import ttk


class BoardCreatorView:
    def __init__(self, root, create_board_command, back_to_menu_command):
        self._root = root
        self._frame = None
        self._create_board_command = create_board_command
        self._cancel_command = back_to_menu_command
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        header = ttk.Label(master=self._frame,
                           text="World generator", font=("Noto Mono", 20, 'bold'))
        size_select_lable = ttk.Label(master=self._root, text="World size: ")
        size_select = ttk.Combobox(values=["5x5", "9x9", "15x15", "50x50"])
        world_name_lable = ttk.Label(master=self._root, text="World name: ")
        name_box = ttk.Entry(master=self._root)
        generate_button = ttk.Button(
            master=self._frame, text="Generate")
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._cancel_command)
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(0, weight=1)

        header.grid(row=0, column=0, pady=10)
        size_select_lable.grid(row=1, column=0, pady=10, padx=10)
        size_select.grid(row=1, column=1, pady=10, padx=10)
        world_name_lable.grid(row=2, column=0, pady=10, padx=10)
        name_box.grid(row=2, column=1, pady=10, padx=10)
        generate_button.grid(row=3, column=1, pady=10, padx=10)
        cancel_button.grid(row=3, column=0, pady=10, padx=10)

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def clear(self):
        self._frame.destroy()
