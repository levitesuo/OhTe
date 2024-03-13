
from tkinter import Tk
from ui.ui import UI
from initialize_database import initialize_database


def main():
    initialize_database()
    window = Tk()
    window.geometry('500x500')
    window.title("Game of life")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
