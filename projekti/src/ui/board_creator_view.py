from tkinter import ttk
from services import gol_service


class BoardCreatorView:
    def __init__(self, root, create_board_command, back_to_menu_command, pygame_handler):
        self._root = root
        self._frame = None
        self._create_board_command = create_board_command
        self._cancel_command = back_to_menu_command
        self._pygame_command = pygame_handler
        self._header = None
        self._size_select = None
        self._world_name = None
        self._initialize()

    def pack(self):
        self._frame.place(relx=.5, rely=.5, anchor='c')

    def clear(self):
        self._frame.destroy()
        self._header.destroy()

    def _handle_generation(self):
        size = self._size_select.get()
        name = self._world_name.get()
        gol_service.create_board(size, name)
        self._pygame_command()

    def _initialize_header(self):
        self._header = ttk.Label(master=self._root,
                                 text="World generator",
                                 font=("Noto Mono", 20, 'bold')
                                 )
        self._header.place(relx=0.5, rely=0.3, anchor='c')

    def _initialize_size_selector(self):
        size_select_lable = ttk.Label(master=self._frame, text="World size:")
        self._size_select = ttk.Combobox(master=self._frame,
                                         state='readonly',
                                         values=["5x5", "9x9", "15x15", "50x50"])
        size_select_lable.grid(row=1, column=0)
        self._size_select.grid(row=1, column=1, pady=10, padx=10)

    def _initialize_world_name(self):
        world_name_lable = ttk.Label(master=self._frame, text="World name:")
        self._world_name = ttk.Entry(master=self._frame)

        world_name_lable.grid(row=2, column=0, pady=10, padx=10)
        self._world_name.grid(row=2, column=1, pady=10, padx=10)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._frame)

        self._initialize_header()
        self._initialize_size_selector()
        self._initialize_world_name()

        generate_button = ttk.Button(
            master=self._frame,
            text="Generate",
            command=self._handle_generation
        )
        cancel_button = ttk.Button(
            master=self._frame,
            text="Cancel",
            command=self._cancel_command
        )

        self._frame.grid_columnconfigure(0, weight=3)
        self._frame.grid_rowconfigure(0, weight=3)

        cancel_button.grid(row=3, column=0, pady=10, padx=10)
        generate_button.grid(row=3, column=1, pady=10, padx=10)
