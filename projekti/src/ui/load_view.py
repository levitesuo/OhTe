from tkinter import ttk
from tkinter import font
import customtkinter as cttk
from functools import partial
from services import gol_service


class LoadView:
    def __init__(self, root,  cancel_command, to_pygame_command):
        self._root = root
        self._frame = None
        self._cancel_command = cancel_command

        def _load_stage(stage_id):
            gol_service.load_board(stage_id)

            to_pygame_command()

        self._pygame_command = _load_stage

        self._initialize()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._initialize_header()
        self._initialize_load_list()
        self._initialize_cancel_button()

    def _initialize_header(self):
        header = ttk.Label(master=self._frame,
                           text="Load map",
                           font=("Noto Mono", 20, 'bold')
                           )
        header.pack(pady=10)

    def _initialize_load_list(self):
        maps = [mi.get_grid() for mi in gol_service.get_boards()]
        scroll_frame = cttk.CTkScrollableFrame(
            master=self._frame,
            width=400,
            height=350)
        scroll_frame.pack(pady=20)
        for m in maps:
            sub_frame = cttk.CTkFrame(master=scroll_frame)
            button = cttk.CTkButton(master=sub_frame,
                                    text=m['name'],
                                    corner_radius=2,
                                    width=200,
                                    fg_color='grey',
                                    hover_color="#ebebeb",
                                    text_color='black',
                                    font=(font.nametofont(
                                        "TkDefaultFont"), 15),
                                    command=partial(
                                        self._pygame_command, m['grid_id']))
            button.pack(side='right')
            sub_frame.pack(side='top', pady=5)

    def _initialize_cancel_button(self):
        cancel_button = ttk.Button(
            master=self._frame, text='cancel', command=self._cancel_command)
        cancel_button.pack()

    def pack(self):
        self._frame.pack()

    def clear(self):
        self._frame.destroy()
