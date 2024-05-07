
from tkinter import Tk
from ui.ui import UI


def main():
    '''
    The main loop of the program.
    '''
    window = Tk()
    window.geometry('500x500')
    window.title("Game of life")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
