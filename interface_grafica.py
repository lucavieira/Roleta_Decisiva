import tkinter as tk
from random import random


class Interface:
    def __init__(self, master=None):
        self.primeriocontainer = tk.Frame(master)
        self.primeriocontainer['pady'] = 30
        self.primeriocontainer.pack()
