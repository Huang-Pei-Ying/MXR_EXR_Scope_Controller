import tkinter as tk
from tkinter import ttk
import utils

class SaveOthersLabelFrame(tk.LabelFrame):
    def __init__(self, master, settings, colors, button_width, entry_width):
        super().__init__(master, text= 'Save Others - in Scope', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)


        ################################################

        ### Weight        

        ###########################

        ## Grid  ==============================================================================================================================================

        ###########################

        ## settings  ==============================================================================================================================================
