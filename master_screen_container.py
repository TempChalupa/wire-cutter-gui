from tkinter import *
from subprocess import call
import test
import threading

final_length = None
final_pcs = None


def starting_screen():

    def next_screen():
        window.destroy()
        length_screen()

    window = Tk()
    window.geometry("480x320")
    window.resizable(False, False)
    window.attributes("-fullscreen", True)

    title_frame = Frame(window)
    title_frame.pack(side="top", fill="x")
    title = Label(title_frame, text="Wire Cutter", font=("Arial", 50))
    title.pack()

    button_frame = Frame(window)
    button_frame.pack(side="bottom", fill="x")
    start_button = Button(button_frame, text="Start", font=("Arial", 50), command=next_screen)
    start_button.pack(fill="x", expand=True)

    window.mainloop()


def length_screen():
    def append_number(number):
        current_text = entry.get()
        entry.delete(0, END)
        entry.insert(0, current_text + number)

    def next_screen():
        global final_length
        final_length = (entry.get())
        if float(final_length) / 1 != 0:
            print(f"{final_length} in")
            window.destroy()
            number_screen()
        elif final_length is None:
            pass

    def backspace():
        current_text = entry.get()
        entry.delete(0, END)
        entry.insert(0, current_text[:-1])

    # Create the main window
    window = Tk()
    window.title("length screen")
    window.geometry("480x320")
    window.resizable(FALSE, FALSE)
    window.attributes("-fullscreen", True)

    # Create and place the Entry widget
    entry = Entry(window, font=("Arial", 24), width=20)
    entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    # Create and place the label
    label = Label(window, text="in", font=("Arial", 24))
    label.grid(row=0, column=3, sticky="ew")

    # Create and place number buttons
    button1 = Button(window, text="1", font=("Arial", 18), width=6, height=2, command=lambda: append_number("1"))
    button1.grid(row=1, column=0, padx=5, pady=5)

    button2 = Button(window, text="2", font=("Arial", 18), width=6, height=2, command=lambda: append_number("2"))
    button2.grid(row=1, column=1, padx=5, pady=5)

    button3 = Button(window, text="3", font=("Arial", 18), width=6, height=2, command=lambda: append_number("3"))
    button3.grid(row=1, column=2, padx=5, pady=5)

    button4 = Button(window, text="4", font=("Arial", 18), width=6, height=2, command=lambda: append_number("4"))
    button4.grid(row=1, column=3, padx=5, pady=5)

    button5 = Button(window, text="5", font=("Arial", 18), width=6, height=2, command=lambda: append_number("5"))
    button5.grid(row=2, column=0, padx=5, pady=5)

    button6 = Button(window, text="6", font=("Arial", 18), width=6, height=2, command=lambda: append_number("6"))
    button6.grid(row=2, column=1, padx=5, pady=5)

    button7 = Button(window, text="7", font=("Arial", 18), width=6, height=2, command=lambda: append_number("7"))
    button7.grid(row=2, column=2, padx=5, pady=5)

    button8 = Button(window, text="8", font=("Arial", 18), width=6, height=2, command=lambda: append_number("8"))
    button8.grid(row=2, column=3, padx=5, pady=5)

    button9 = Button(window, text="9", font=("Arial", 18), width=6, height=2, command=lambda: append_number("9"))
    button9.grid(row=3, column=0, padx=5, pady=5)

    button0 = Button(window, text="0", font=("Arial", 18), width=6, height=2, command=lambda: append_number("0"))
    button0.grid(row=3, column=1, padx=5, pady=5)

    buttonDot = Button(window, text=".", font=("Arial", 18), width=6, height=2, command=lambda: append_number("."))
    buttonDot.grid(row=3, column=2, padx=5, pady=5)

    buttonEnter = Button(window, text="Enter", font=("Arial", 18), width=6, height=2, command=next_screen)
    buttonEnter.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

    # Create and place the Backspace button
    backspace_button = Button(window, text="⌫", command=backspace, font=("Arial", 18), width=6, height=2)
    backspace_button.grid(row=3, column=3, columnspan=2, padx=5, pady=5, sticky="nsew")

    # Adjust column weights for resizing
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)

    # Adjust row weights for resizing
    for row in range(1, 5):
        window.grid_rowconfigure(row, weight=1)

    window.mainloop()


def number_screen():

    def append_number(number):
        current_text = entry.get()
        entry.delete(0, END)
        entry.insert(0, current_text + number)

    def next_screen():
        global final_pcs
        final_pcs = (entry.get())
        if float(final_pcs) / 1 != 0:
            print(f"{final_pcs} pcs")
            window.destroy()
            confirmation_screen()
        elif final_pcs is None:
            pass

    def backspace():
        current_text = entry.get()
        entry.delete(0, END)
        entry.insert(0, current_text[:-1])

    def back():
        window.destroy()
        length_screen()

    # Create the main window
    window = Tk()
    window.title("number screen")
    window.geometry("480x320")
    window.resizable(FALSE, FALSE)
    window.attributes("-fullscreen", True)

    # Create and place the Entry widget
    entry = Entry(window, font=("Arial", 24), width=20)
    entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    # Create and place the label
    label = Label(window, text="pcs", font=("Arial", 24))
    label.grid(row=0, column=3, sticky="ew")

    # Create and place number buttons
    button1 = Button(window, text="1", font=("Arial", 18), width=6, height=2, command=lambda: append_number("1"))
    button1.grid(row=1, column=0, padx=5, pady=5)

    button2 = Button(window, text="2", font=("Arial", 18), width=6, height=2, command=lambda: append_number("2"))
    button2.grid(row=1, column=1, padx=5, pady=5)

    button3 = Button(window, text="3", font=("Arial", 18), width=6, height=2, command=lambda: append_number("3"))
    button3.grid(row=1, column=2, padx=5, pady=5)

    button4 = Button(window, text="4", font=("Arial", 18), width=6, height=2, command=lambda: append_number("4"))
    button4.grid(row=1, column=3, padx=5, pady=5)

    button5 = Button(window, text="5", font=("Arial", 18), width=6, height=2, command=lambda: append_number("5"))
    button5.grid(row=2, column=0, padx=5, pady=5)

    button6 = Button(window, text="6", font=("Arial", 18), width=6, height=2, command=lambda: append_number("6"))
    button6.grid(row=2, column=1, padx=5, pady=5)

    button7 = Button(window, text="7", font=("Arial", 18), width=6, height=2, command=lambda: append_number("7"))
    button7.grid(row=2, column=2, padx=5, pady=5)

    button8 = Button(window, text="8", font=("Arial", 18), width=6, height=2, command=lambda: append_number("8"))
    button8.grid(row=2, column=3, padx=5, pady=5)

    button9 = Button(window, text="9", font=("Arial", 18), width=6, height=2, command=lambda: append_number("9"))
    button9.grid(row=3, column=0, padx=5, pady=5)

    button0 = Button(window, text="0", font=("Arial", 18), width=6, height=2, command=lambda: append_number("0"))
    button0.grid(row=3, column=1, padx=5, pady=5)

    buttonEnter = Button(window, text="Enter", font=("Arial", 18), width=6, height=2, command=next_screen)
    buttonEnter.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

    # Create and place the Backspace button
    backspace_button = Button(window, text="⌫", command=backspace, font=("Arial", 18), width=6, height=2)
    backspace_button.grid(row=3, column=2, padx=5, pady=5)

    back_button = Button(window, text="Back", command=back, font=("Arial", 18), width=6, height=2)
    back_button.grid(row=3, column=3, padx=5, pady=5)

    # Adjust column weights for resizing
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)
    window.grid_columnconfigure(2, weight=1)
    window.grid_columnconfigure(3, weight=1)

    # Adjust row weights for resizing
    for row in range(1, 5):
        window.grid_rowconfigure(row, weight=1)

    window.mainloop()


def confirmation_screen():

    def next_screen():
        window.destroy()
        running_screen()

    def back():
        window.destroy()
        number_screen()

    window = Tk()
    window.geometry("480x320")
    window.resizable(FALSE, FALSE)
    window.attributes("-fullscreen", True)

    label1 = Label(window, text=f"Length: {final_length} in", font=("Arial", 24))
    label1.grid(row=0, column=0, columnspan=2, pady=25, sticky="w")

    label2 = Label(window, text=f"Number of Wires: {final_pcs} pcs", font=("Arial", 24))
    label2.grid(row=1, column=0, columnspan=2, pady=25, sticky="w")

    buttonEnter = Button(window, text="Confirm", font=("Arial", 18), width=6, height=2, command=next_screen)
    buttonEnter.grid(row=2, column=1, columnspan=1, padx=5, pady=5, sticky="ew")

    back_button = Button(window, text="Back", font=("Arial", 18), width=6, height=2, command=back)
    back_button.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky="ew")

    window.grid_rowconfigure(0, weight=0)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=0)

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    window.mainloop()


def running_screen():

    def task_wrapper():
        test.main()
        window.after(0, lambda: (window.destroy(), cutting_complete_screen()))

    window = Tk()
    window.geometry("480x320")
    window.resizable(FALSE, FALSE)
    window.attributes("-fullscreen", True)

    label_frame = Frame(window)
    label_frame.pack(fill="both", expand=True)
    running = Label(label_frame, text="Running...", font=("Arial", 50))
    running.pack(fill="both", expand=True)

    task_thread = threading.Thread(target=task_wrapper)
    task_thread.start()

    window.mainloop()


def cutting_complete_screen():

    def shutdown_button():
        window.destroy()
        shutdown_confirmation()

    def continue_button():
        window.destroy()
        length_screen()

    window = Tk()
    window.geometry("480x320")
    window.resizable(FALSE, FALSE)
    window.attributes("-fullscreen", True)

    label1 = Label(window, text="Cutting Complete", font=("Arial", 24))
    label1.grid(row=0, column=0, columnspan=2, pady=25, sticky="ew")

    continue_button = Button(window, text="Continue", font=("Arial", 18), width=6, height=6, command=continue_button)
    continue_button.grid(row=2, column=1, columnspan=1, padx=5, pady=5, sticky="ew")

    shutdown_button = Button(window, text="Shutdown", font=("Arial", 18), width=6, height=6, command=shutdown_button)
    shutdown_button.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky="ew")

    window.grid_rowconfigure(0, weight=0)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=0)

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    window.mainloop()


def shutdown_confirmation():

    def no_button():
        window.destroy()
        cutting_complete_screen()

    def shutdown_sequence_temp():
        window.destroy()

    window = Tk()
    window.geometry("480x320")
    window.resizable(FALSE, FALSE)
    window.attributes("-fullscreen", True)

    label1 = Label(window, text="Confirm Shutdown?", font=("Arial", 24))
    label1.grid(row=0, column=0, columnspan=2, pady=25, sticky="ew")

    buttonEnter = Button(window, text="Yes", font=("Arial", 18), width=6, height=6, command=shutdown_sequence_temp)
    buttonEnter.grid(row=2, column=1, columnspan=1, padx=5, pady=5, sticky="ew")

    back_button = Button(window, text="No", font=("Arial", 18), width=6, height=6, command=no_button)
    back_button.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky="ew")

    window.grid_rowconfigure(0, weight=0)
    window.grid_rowconfigure(1, weight=1)
    window.grid_rowconfigure(2, weight=0)

    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    window.mainloop()


def shutdown_sequence():
    # below is the bash command to shut down pi, right now this function is a placeholder
    # sudo shutdown --poweroff
    print("Shutting Down")


starting_screen()


