import tkinter as tk
from tkinter import ttk

class ControlLabelFrame(tk.LabelFrame):
    def __init__(self, master, settings, mxr, colors, button_width, entry_width):
        super().__init__(master, text= 'Control', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)

        self.button_control_run = ttk.Button(
            master= self, text= 'RUN', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.run()
            )
        self.button_control_stop = ttk.Button(
            master= self, text= 'STOP', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.stop()
            )
        self.button_control_single = ttk.Button(
            master= self, text= 'Single', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.single()
            )
        self.button_control_autoscale = ttk.Button(
            master= self, text= 'Auto Scale', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.autoscale()
            )
        self.button_control_default = ttk.Button(
            master= self, text= 'Default', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.default()
            )
        self.button_control_cleardisplay = ttk.Button(
            master= self, text= 'Clear', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.clear_diaplay()
            )
        self.button_disable_button = ttk.Button(
            master= self, text= 'Disable', width= button_width,  padding= 2, 
            style= 'double_height.TButton',
            command= lambda: mxr.switch_button_state(button_list= [
                self.button_control_autoscale, 
                self.button_control_default, 
                self.button_control_cleardisplay, 
            ])
            )
        ################################################

        ### Weight        
        for i in range(2):
            self.rowconfigure(i, weight= 1, uniform= 'row')
        for j in range(4):
            self.columnconfigure(j, weight= 1, uniform= 'col')    
        ###########################

        ## Grid  ==============================================================================================================================================
        self.button_control_run.grid(row= 0, column= 0, padx= 5, pady= 5, sticky= 'nesw')
        self.button_control_stop.grid(row= 0, column= 1, padx= 5, pady= 5, sticky= 'nesw')
        self.button_control_single.grid(row= 0, column= 2, padx= 5, pady= 5, sticky= 'nes')

        self.button_control_autoscale.grid(row= 1, column= 0, padx= 5, pady= 5, sticky= 'nesw')
        self.button_control_default.grid(row= 1, column= 1, padx= 5, pady= 5, sticky= 'nesw')
        self.button_control_cleardisplay.grid(row= 1, column= 2, padx= 5, pady= 5, sticky= 'nesw')
        self.button_disable_button.grid(row= 1, column= 3, padx= 5, pady= 5, sticky= 'nesw')
        ###########################

        ## settings  ==============================================================================================================================================
