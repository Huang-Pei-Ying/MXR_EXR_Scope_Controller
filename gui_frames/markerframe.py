import tkinter as tk
from tkinter import ttk
import utils

class MarkerLabelFrame(tk.LabelFrame):
    def __init__(self, master, settings, colors, button_width, entry_width):
        super().__init__(master, text= 'Marker', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)

        self.frame_marker_left= tk.Frame(master= self, background= colors['labelframe'][0])
        self.frame_marker_right= tk.Frame(master= self, background= colors['labelframe'][0])
        self.button_delete_measurement= ttk.Button(
            master= self.frame_marker_left, text= 'Delete Measurement', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_add_marker= ttk.Button(
            master= self.frame_marker_left, text= 'Add Marker', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_delete_marker= ttk.Button(
            master= self.frame_marker_left, text= 'Delete Marker', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.boolvar_multi_color_marker= tk.BooleanVar()
        self.checkbutton_multi_color_marker= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Multi-Color Marker', variable= self.boolvar_multi_color_marker, style= 'checkbutton_1.TCheckbutton', 
        )
        self.boolvar_measurement_1= tk.BooleanVar()
        self.checkbutton_marker_1= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 1', variable= self.boolvar_measurement_1, style= 'checkbutton_2.TCheckbutton', 
        )
        self.boolvar_measurement_2= tk.BooleanVar()
        self.checkbutton_marker_2= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 2', variable= self.boolvar_measurement_2, style= 'checkbutton_2.TCheckbutton', 
        )
        self.boolvar_measurement_3= tk.BooleanVar()
        self.checkbutton_marker_3= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 3', variable= self.boolvar_measurement_3, style= 'checkbutton_2.TCheckbutton', 
        )
        self.boolvar_measurement_4= tk.BooleanVar()
        self.checkbutton_marker_4= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 4', variable= self.boolvar_measurement_4, style= 'checkbutton_2.TCheckbutton', 
        )
        self.boolvar_measurement_5= tk.BooleanVar()
        self.checkbutton_marker_5= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 5', variable= self.boolvar_measurement_5, style= 'checkbutton_2.TCheckbutton', 
        )
        self.boolvar_measurement_6= tk.BooleanVar()
        self.checkbutton_marker_6= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 6', variable= self.boolvar_measurement_6, style= 'checkbutton_2.TCheckbutton', 
        )
        self.boolvar_measurement_7= tk.BooleanVar()
        self.checkbutton_marker_7= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 7', variable= self.boolvar_measurement_7, style= 'checkbutton_2.TCheckbutton', 
        )
        self.boolvar_measurement_8= tk.BooleanVar()
        self.checkbutton_marker_8= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 8', variable= self.boolvar_measurement_8, style= 'checkbutton_2.TCheckbutton', 
        )
        self.boolvar_measurement_9= tk.BooleanVar()
        self.checkbutton_marker_9= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 9', variable= self.boolvar_measurement_9, style= 'checkbutton_2.TCheckbutton', 
        )
        self.boolvar_measurement_10= tk.BooleanVar()
        self.checkbutton_marker_10= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 10', variable= self.boolvar_measurement_10, style= 'checkbutton_2.TCheckbutton', 
        )
        self.boolvar_measurement_11= tk.BooleanVar()
        self.checkbutton_marker_11= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 11', variable= self.boolvar_measurement_11, style= 'checkbutton_2.TCheckbutton', 
        )
        self.boolvar_measurement_12= tk.BooleanVar()
        self.checkbutton_marker_12= ttk.Checkbutton(
            master= self.frame_marker_right, text= 'Measurement 12', variable= self.boolvar_measurement_12, style= 'checkbutton_2.TCheckbutton', 
        )
        ################################################

        ### Weight        
        self.rowconfigure(0, weight= 1, uniform= 'row')
        self.columnconfigure(0, weight= 1, uniform= 'col')
        self.columnconfigure(1, weight= 2, uniform= 'col')

        for i in range(3):
            self.frame_marker_left.rowconfigure(i, weight= 1, uniform= 'row')
        self.frame_marker_left.columnconfigure(0, weight= 1, uniform= 'col')
        for i in range(7):
            self.frame_marker_right.rowconfigure(i, weight= 1, uniform= 'row')
        self.frame_marker_right.columnconfigure(0, weight= 1, uniform= 'col')
        self.frame_marker_right.columnconfigure(1, weight= 1, uniform= 'col')
        ###########################

        ## Grid  ==============================================================================================================================================
        self.frame_marker_left.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_marker_right.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'nesw')

        self.button_delete_measurement.grid(row= 0, column= 0, padx= 15, pady= 15, sticky= 'nesw')
        self.button_add_marker.grid(row= 1, column= 0, padx= 15, pady= 15, sticky= 'nesw')
        self.button_delete_marker.grid(row= 2, column= 0, padx= 15, pady= 15, sticky= 'nesw')

        self.checkbutton_multi_color_marker.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw', columnspan= 2)

        self.checkbutton_marker_1.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_marker_2.grid(row= 2, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_marker_3.grid(row= 3, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_marker_4.grid(row= 4, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_marker_5.grid(row= 5, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_marker_6.grid(row= 6, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_marker_7.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_marker_8.grid(row= 2, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_marker_9.grid(row= 3, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_marker_10.grid(row= 4, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_marker_11.grid(row= 5, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_marker_12.grid(row= 6, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        ###########################

        ## settings  ==============================================================================================================================================
        settings.apply('Measurement', {
            'MultiColorChoice': self.boolvar_multi_color_marker, 
            'Measurement_1': self.boolvar_measurement_1, 
            'Measurement_2': self.boolvar_measurement_2, 
            'Measurement_3': self.boolvar_measurement_3, 
            'Measurement_4': self.boolvar_measurement_4, 
            'Measurement_5': self.boolvar_measurement_5, 
            'Measurement_6': self.boolvar_measurement_6, 
            'Measurement_7': self.boolvar_measurement_7, 
            'Measurement_8': self.boolvar_measurement_8, 
            'Measurement_9': self.boolvar_measurement_9, 
            'Measurement_10': self.boolvar_measurement_10, 
            'Measurement_11': self.boolvar_measurement_11, 
            'Measurement_12': self.boolvar_measurement_12, 
        })
