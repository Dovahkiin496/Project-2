from gui import *


def main():
    """
    A function that initializes the gui so the user can actually utilize it.
    """
    window = Tk()
    window.title('Voting System')
    window.geometry('400x350')
    window.resizable(False, False)

    widgets = GUI(window)
    window.mainloop()


if __name__ == '__main__':
    main()
