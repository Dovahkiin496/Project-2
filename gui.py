from tkinter import *
import os.path
import csv


class GUI:
    """
    Class that creates the gui window where the user can input values and perform operations.
    """
    def __init__(self, window):
        """
        init function that defines what will be within the gui window, such as buttons or labels.
        :param window: An instance of the gui class
        """
        self.window = window

        self.frame_zero = Frame(self.window)
        self.label_zero = Label(self.frame_zero, text="Voter ID:")
        self.entry_zero = Entry(self.frame_zero, width=50)
        self.label_zero.pack(padx=5, side="left")
        self.entry_zero.pack(padx=5, side="left")
        self.frame_zero.pack(anchor="w", pady=10)

        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first, text='First Nominee:')
        self.label_second = Label(self.frame_first, text="Erik Rosario (Democrat)")
        self.label_first.pack(padx=5, side='left')
        self.label_second.pack(padx=30, side='left')
        self.frame_first.pack(anchor='w', pady=10)

        self.frame_second = Frame(self.window)
        self.label_third = Label(self.frame_second, text='Second Nominee:')
        self.label_fourth = Label(self.frame_second, text="Mari Sherman (Republican)")
        self.label_third.pack(padx=5, side='left')
        self.label_fourth.pack(padx=25, side='left')
        self.frame_second.pack(anchor='w', pady=10)

        self.frame_third = Frame(self.window)
        self.label_fifth = Label(self.frame_third, text='Third Nominee:')
        self.label_sixth = Label(self.frame_third, text="David Bass (Libertarian)")
        self.label_fifth.pack(padx=5, side='left')
        self.label_sixth.pack(padx=10, side='left')
        self.frame_third.pack(anchor='w', pady=10)

        self.frame_choice = Frame(self.window)
        self.label_choice = Label(self.frame_choice, text='Nominee Selection:\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_Nominee_1 = Radiobutton(self.frame_choice, text='Nominee 1', variable=self.radio_1, value=1)
        self.radio_Nominee_2 = Radiobutton(self.frame_choice, text='Nominee 2', variable=self.radio_1, value=2)
        self.radio_Nominee_3 = Radiobutton(self.frame_choice, text='Nominee 3', variable=self.radio_1, value=3)
        self.label_choice.pack(side='left', padx=0)
        self.radio_Nominee_1.pack(side='left')
        self.radio_Nominee_2.pack(side='left')
        self.radio_Nominee_3.pack(side='left')
        self.frame_choice.pack(anchor='w', pady=10)

        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result, text="Welcome, Voter. Please enter your voter ID before voting.")
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        self.frame_id = Frame(self.window)
        self.label_id = Label(self.frame_result, text="")
        self.label_id.pack(pady=10)
        self.frame_id.pack()

        self.frame_buttons = Frame(self.window)
        self.button_save = Button(self.frame_buttons, text='SAVE VOTE', command=self.save_selection)
        self.button_save.pack(pady=10)
        self.frame_buttons.pack()

    def save_selection(self):
        """

        """
        id = self.entry_zero.get()
        choice = self.radio_1.get()
        with open("ids.txt", "r") as ids:
            for line in ids:
                if id in line:
                    self.label_id.config(text="Vote has already been registered with this ID")
                    var = False
                else:
                    self.label_id.config(text="ID confirmed.")
                    var = True
        if var:
            if choice == 1:
                self.label_result.config(text=f"Nominee selected and saved. Your selection: Erik Rosario (Democrat)")
                if os.path.isfile("results.csv"):
                    with open("results.csv", "a", newline="") as results_file:
                        csv_writer = csv.writer(results_file)
                        output = ["Erik Rosario", "Democrat"]
                        csv_writer.writerow(output)
                else:
                    with open("results.csv", "w", newline="") as results_file:
                        csv_writer = csv.writer(results_file)
                        header = ["Nominee", "Party"]
                        output = ["Erik Rosario", "Democrat"]
                        csv_writer.writerow(header)
                        csv_writer.writerow(output)
            elif choice == 2:
                self.label_result.config(text=f"Nominee selected and saved. Your selection: Mari Sherman (Republican)")
                if os.path.isfile("results.csv"):
                    with open("results.csv", "a", newline="") as results_file:
                        csv_writer = csv.writer(results_file)
                        output = ["Mari Sherman", "Republican"]
                        csv_writer.writerow(output)
                else:
                    with open("results.csv", "w", newline="") as results_file:
                        csv_writer = csv.writer(results_file)
                        header = ["Nominee", "Party"]
                        output = ["Mari Sherman", "Republican"]
                        csv_writer.writerow(header)
                        csv_writer.writerow(output)
            elif choice == 3:
                self.label_result.config(text=f"Nominee selected and saved. Your selection: David Bass (Libertarian)")
                if os.path.isfile("results.csv"):
                    with open("results.csv", "a", newline="") as results_file:
                        csv_writer = csv.writer(results_file)
                        output = ["David Bass", "Libertarian"]
                        csv_writer.writerow(output)
                else:
                    with open("results.csv", "w", newline="") as results_file:
                        csv_writer = csv.writer(results_file)
                        header = ["Nominee", "Party"]
                        output = ["David Bass", "Libertarian"]
                        csv_writer.writerow(header)
                        csv_writer.writerow(output)
            else:
                self.label_result.config(text='No nominee selected')
            with open("ids.txt", "a") as ids:
                ids.write(f"\n{id}")
        if not var:
            self.label_result.config(text="Vote not registered")
