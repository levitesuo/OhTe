from board import Board
from tkinter import Tk
from ui.ui import UI


def main():
    b = Board(3, "b")
    print(b)
    for i in range(3):
        for j in range(3):
            b.manipulate(i, j)
    print(b)
    b.step()
    print(b)
    b.step()
    print(b)
    window = Tk()
    window.geometry('500x500')
    window.title("Game of life")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
