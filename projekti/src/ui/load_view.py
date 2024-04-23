from tkinter import ttk
import customtkinter as cttk
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
        maps = [m.get_grid() for m in gol_service.get_boards()]
        print([m['name'] for m in maps])
        for m in maps:
            sub_frame = ttk.Frame(master=self._frame)
            lable = ttk.Label(master=sub_frame, text=f"{m['name']}")
            lable.pack(side='left')
            button = ttk.Button(master=sub_frame, text='load',
                                command=lambda: self._pygame_command(m['grid_id']))
            button.pack(side='right')
            sub_frame.pack(side='top')

    def pack(self):
        self._frame.pack()

    def clear(self):
        self._frame.destroy()
