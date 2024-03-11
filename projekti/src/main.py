from board import Board


def main():
    b = Board(3, "b")
    print(b)
    for i in range(2):
        for j in range(2):
            b.manipulate(i, j)
    print(b)
    b.step()
    print(b)


if __name__ == "__main__":
    main()
