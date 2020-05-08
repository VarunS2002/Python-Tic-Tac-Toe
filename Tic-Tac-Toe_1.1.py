from tkinter import *
from tkinter import messagebox
import webbrowser
import random


class Box:

    def __init__(self, root):

        # Setting Main Window Attributes

        self.root = root
        root.title("Tic-Tac-Toe")
        root.resizable(False, False)

        # Value Flag

        self.f = 0

        # Buttons List

        self.boxes = []

        # Game List

        self.data = ["", "", "", "", "", "", "", "", ""]

        # Default Value to Stop or Allow the Bot After Result

        self.continue_callback = True

        # Default Game Mode

        self.mode = "Player vs Computer"

        # Option Menu

        self.menubar = Menu(self.root)
        self.options = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Menu", menu=self.options)
        self.options.add_command(label=f"Choose Mode: {self.mode}", command=self.choose_mode)
        self.options.add_command(label="Restart Game", command=self.new)
        self.options.add_separator()
        self.options.add_command(label="About", command=self.about)
        self.options.add_command(label="Quit", command=self.close)

        # Setting Main Window Attributes

        self.root.config(menu=self.menubar)
        self.root.protocol('WM_DELETE_WINDOW', self.close)

    # Choose Mode Window

    def choose_window(self):
        self.window = Toplevel()
        self.window.title("Mode")
        self.window.resizable(False, False)
        self.window.geometry('220x50')
        self.window.attributes('-topmost', True)
        self.window.grab_set()
        self.window.focus_force()
        return self.window

    # Choose Mode PvC Button

    def do_pvc(self):
        self.mode = "Player vs Computer"
        self.new()
        self.window.destroy()

    # Choose Mode PvP Button

    def do_pvp(self):
        self.mode = "Player vs Player"
        self.new()
        self.window.destroy()

    # Choose Mode Function

    def choose_mode(self):
        self.window = self.choose_window()

        pvc = Button(self.window, command=self.do_pvc, text="Player vs Computer")
        pvc.pack(side='top', fill='both', expand='1')

        pvp = Button(self.window, command=self.do_pvp, text="Player vs Player")
        pvp.pack(side='top', fill='both', expand='1')

        self.window.mainloop()

    # Restart Game Function

    def new(self):

        # Resetting Data Variables

        self.data = ["", "", "", "", "", "", "", "", ""]
        self.f = 0
        self.continue_callback = True

        # Resetting Button Attributes

        for i in range(9):
            self.boxes[i].config(text="")
        for i in range(9):
            self.boxes[i].config(state=NORMAL)

        # Setting Option Menu Attributes

        self.options.entryconfig(self.options.index(0), label=f"Choose Mode: {self.mode}")

    # Check Result Function

    def check(self, index):

        if index == 0:
            if self.data[0] == self.data[1] == self.data[2]:
                self.result()
                return
            elif self.data[0] == self.data[3] == self.data[6]:
                self.result()
                return
            elif self.data[0] == self.data[4] == self.data[8]:
                self.result()
                return
        elif index == 1:
            if self.data[0] == self.data[1] == self.data[2]:
                self.result()
                return
            elif self.data[1] == self.data[4] == self.data[7]:
                self.result()
                return
        elif index == 2:
            if self.data[0] == self.data[1] == self.data[2]:
                self.result()
                return
            elif self.data[2] == self.data[5] == self.data[8]:
                self.result()
                return
            elif self.data[2] == self.data[4] == self.data[6]:
                self.result()
                return
        elif index == 3:
            if self.data[0] == self.data[3] == self.data[6]:
                self.result()
                return
            elif self.data[3] == self.data[4] == self.data[5]:
                self.result()
                return
        elif index == 4:
            if self.data[1] == self.data[4] == self.data[7]:
                self.result()
                return
            elif self.data[3] == self.data[4] == self.data[5]:
                self.result()
                return
            elif self.data[0] == self.data[4] == self.data[8]:
                self.result()
                return
            elif self.data[2] == self.data[4] == self.data[6]:
                self.result()
                return
        elif index == 5:
            if self.data[2] == self.data[5] == self.data[8]:
                self.result()
                return
            elif self.data[3] == self.data[4] == self.data[5]:
                self.result()
                return
        elif index == 6:
            if self.data[0] == self.data[3] == self.data[6]:
                self.result()
                return
            elif self.data[2] == self.data[4] == self.data[6]:
                self.result()
                return
            elif self.data[6] == self.data[7] == self.data[8]:
                self.result()
                return
        elif index == 7:
            if self.data[6] == self.data[7] == self.data[8]:
                self.result()
                return
            elif self.data[1] == self.data[4] == self.data[7]:
                self.result()
                return
        elif index == 8:
            if self.data[2] == self.data[5] == self.data[8]:
                self.result()
                return
            elif self.data[0] == self.data[4] == self.data[8]:
                self.result()
                return
            elif self.data[6] == self.data[7] == self.data[8]:
                self.result()
                return

        # Output if Match is Drawn

        if all(len(ele) != 0 for ele in self.data):
            messagebox.showinfo("Result", "Draw")

            # Setting Value to Stop the Bot after Result

            if self.mode == "Player vs Computer":
                self.continue_callback = False

    # Output the Winner

    def result(self):

        # Setting Value to Stop the Bot after Result

        if self.mode == "Player vs Computer":
            self.continue_callback = False

        # Displaying the Result

        if self.f == 0:
            if self.mode == "Player vs Computer":
                messagebox.showinfo("Result", "Computer won")
            elif self.mode == "Player vs Player":
                messagebox.showinfo("Result", "O won")
        elif self.f == 1:
            if self.mode == "Player vs Computer":
                messagebox.showinfo("Result", "You won")
            elif self.mode == "Player vs Player":
                messagebox.showinfo("Result", "X won")

        # Setting Button Attributes

        for i in range(9):
            self.boxes[i].config(state=DISABLED)

    # Choose Value Function

    def callback(self, index):

        if self.mode == "Player vs Computer":

            # Inputting User's Value

            if self.f == 0:
                if len(self.boxes[index]['text']) == 0:
                    self.boxes[index].config(text="X")
                    self.data[index] = "X"
                    self.f += 1

                # Calling Check Result Function

                self.check(index)

            # Stopping the Bot after Result

            if not self.continue_callback:
                return

            # Inputting Bot's Value

            if self.f == 1:
                while True:
                    random_index = random.randint(0, 8)
                    if len(self.boxes[random_index]['text']) == 0:
                        self.boxes[random_index].config(text="O")
                        self.data[random_index] = "O"
                        self.f -= 1

                        # Calling Check Result Function

                        self.check(random_index)

                        break
                    else:
                        continue

        elif self.mode == "Player vs Player":

            # Inputting User's Value

            if self.f == 0:
                if len(self.boxes[index]['text']) == 0:
                    self.boxes[index].config(text="X")
                    self.data[index] = "X"
                    self.f += 1
            elif self.f == 1:
                if len(self.boxes[index]['text']) == 0:
                    self.boxes[index].config(text="O")
                    self.data[index] = "O"
                    self.f -= 1

            # Calling Check Result Function

            self.check(index)

    # Releases

    def releases(self):
        webbrowser.open_new("https://github.com/VarunS2002/Python-Tic-Tac-Toe/releases/")
        self.info.attributes('-topmost', False)

    # Sources

    def sources(self):
        webbrowser.open_new("https://github.com/VarunS2002/Python-Tic-Tac-Toe/")
        self.info.attributes('-topmost', False)

    # About Window

    def about_window(self):
        self.info = Toplevel()
        self.info.title("About")
        self.info.resizable(False, False)
        self.info.geometry('220x100')
        self.info.attributes('-topmost', True)
        self.info.grab_set()
        self.info.focus_force()
        return self.info

    # About Function

    def about(self):
        self.info = self.about_window()

        version = Label(self.info, text="Version: 1.1")
        version.pack(side='top', pady="5")
        release = Button(self.info, text="Releases", fg="blue", cursor="hand2", borderwidth=0, command=self.releases)
        release.pack(side='top', pady="5")
        source = Button(self.info, text="Sources", fg="blue", cursor="hand2", borderwidth=0, command=self.sources)
        source.pack(side='top', pady="5")

        self.info.mainloop()

    # Quit Function

    @staticmethod
    def close():
        ask_quit = messagebox.askyesno("Quit", "Do you want to quit?")
        if ask_quit:
            quit()
        elif not ask_quit:
            pass

    # Grid Function

    def grid(self):

        i = 0

        for rowindex in range(3):

            for colindex in range(3):
                # Adding Button Objects to List

                self.boxes.append(i)

                # Creating Buttons

                self.boxes[i] = Button(self.root, width=8, height=4,
                                       command=lambda index=i: self.callback(index))
                self.boxes[i].grid(row=rowindex, column=colindex, sticky=N + S + E + W)

                # Increasing Value of i for Iteration

                i += 1


if __name__ == "__main__":
    master = Tk()
    box_instance = Box(master)
    box_instance.grid()
    master.mainloop()
