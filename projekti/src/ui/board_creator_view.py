from tkinter import ttk


class BoardCreatorView:
    def __init__(self, root, create_board_command, back_to_menu_command):
        self._root = root
        self._frame = None
        self._create_board_command = create_board_command
        self._cancel_command = back_to_menu_command
        self._header = None
        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)
        self._header = ttk.Label(master=self._root,
                                 text="World generator", font=("Noto Mono", 20, 'bold'))
        size_select_lable = ttk.Label(master=self._frame, text="World size:")
        size_select = ttk.Combobox(master=self._frame, state='readonly', values=[
            "5x5", "9x9", "15x15", "50x50"])
        world_name_lable = ttk.Label(master=self._frame, text="World name:")
        name_box = ttk.Entry(master=self._frame)
        generate_button = ttk.Button(
            master=self._frame, text="Generate", command=self._create_board_command)
        cancel_button = ttk.Button(
            master=self._frame, text="Cancel", command=self._cancel_command)

        self._frame.grid_columnconfigure(0, weight=3)
        self._frame.grid_rowconfigure(0, weight=3)

        self._header.place(relx=0.5, rely=0.3, anchor='c')
        size_select_lable.grid(row=1, column=0)
        size_select.grid(row=1, column=1, pady=10, padx=10)
        world_name_lable.grid(row=2, column=0, pady=10, padx=10)
        name_box.grid(row=2, column=1, pady=10, padx=10)
        cancel_button.grid(row=3, column=0, pady=10, padx=10)
        generate_button.grid(row=3, column=1, pady=10, padx=10)

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def clear(self):
        self._frame.destroy()
        self._header.destroy()
