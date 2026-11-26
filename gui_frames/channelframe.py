import tkinter as tk
from tkinter import ttk

class ChannelLabelFrame(tk.LabelFrame):
    def __init__(self, master, root, settings, mxr, colors, button_width, entry_width):
        super().__init__(master, text= 'Channel', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)

        self.root = root

        self.button_channel_1 = ttk.Button(
            master= self, text= 'Channel 1', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.call_channel_and_label(root= self.root, channel= 1)
            )
        self.button_channel_2 = ttk.Button(
            master= self, text= 'Channel 2', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.call_channel_and_label(root= self.root, channel= 2)
            )
        self.button_channel_3 = ttk.Button(
            master= self, text= 'Channel 3', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.call_channel_and_label(root= self.root, channel= 3)
            )
        self.button_channel_4 = ttk.Button(
            master= self, text= 'Channel 4', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.call_channel_and_label(root= self.root, channel= 4)
            )
        self.button_wmemory_1 = ttk.Button(
            master= self, text= 'Wmemory 1', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.call_channel_and_label(root= self.root, channel= 5)
            )
        self.button_wmemory_2 = ttk.Button(
            master= self, text= 'Wmemory 2', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.call_channel_and_label(root= self.root, channel= 6)
            )
        self.button_wmemory_3 = ttk.Button(
            master= self, text= 'Wmemory 3', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.call_channel_and_label(root= self.root, channel= 7)
            )
        self.button_wmemory_4 = ttk.Button(
            master= self, text= 'Wmemory 4', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.call_channel_and_label(root= self.root, channel= 8)
            )
        ################################################

        ### Weight        
        ###########################
        for i in range(2):
            self.rowconfigure(i, weight= 1, uniform= 'row')
        for j in range(4):
            self.columnconfigure(j, weight= 1, uniform= 'col')    
        ## Grid  ==============================================================================================================================================
        self.button_channel_1.grid(row= 0, column= 0, padx= 5, pady= 5, sticky= 'nesw')
        self.button_channel_2.grid(row= 0, column= 1, padx= 5, pady= 5, sticky= 'nesw')
        self.button_channel_3.grid(row= 0, column= 2, padx= 5, pady= 5, sticky= 'nesw')
        self.button_channel_4.grid(row= 0, column= 3, padx= 5, pady= 5, sticky= 'nesw')
        self.button_wmemory_1.grid(row= 1, column= 0, padx= 5, pady= 5, sticky= 'nesw')
        self.button_wmemory_2.grid(row= 1, column= 1, padx= 5, pady= 5, sticky= 'nesw')
        self.button_wmemory_3.grid(row= 1, column= 2, padx= 5, pady= 5, sticky= 'nesw')
        self.button_wmemory_4.grid(row= 1, column= 3, padx= 5, pady= 5, sticky= 'nesw')
        ###########################

        ## settings  ==============================================================================================================================================
