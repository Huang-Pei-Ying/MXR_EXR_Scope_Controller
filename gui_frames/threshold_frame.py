import tkinter as tk
from tkinter import ttk
import utils

class ThresholdLabelFrame(tk.LabelFrame):
    def __init__(self, master, settings, colors, button_width, entry_width):
        super().__init__(master, text= 'Threshold', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)


        # general threshold - value ######
        self.button_general_threshold_value = ttk.Button(
            master= self, text= 'General - Value (V)', width= button_width,  padding= 2, 
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        
        ## general threshold - value Top
        self.label_general_threshold_value_top= tk.Label(
            master= self, text= 'Top (V)', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            )
        self.strvar_general_threshold_value_top= tk.StringVar()
        self.combobox_general_threshold_value_top = ttk.Combobox(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_general_threshold_value_top, style= 'TCombobox', justify= 'center')
        
        ## general threshold - value Middle
        self.label_general_threshold_value_middle= tk.Label(
            master= self, text= 'Middle (V)', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            )
        self.strvar_general_threshold_value_middle= tk.StringVar()
        self.combobox_general_threshold_value_middle = ttk.Combobox(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_general_threshold_value_middle, style= 'TCombobox', justify= 'center')
        
        ## general threshold - value Base
        self.label_general_threshold_value_base= tk.Label(
            master= self, text= 'Base (V)', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            )
        self.strvar_general_threshold_value_base= tk.StringVar()
        self.combobox_general_threshold_value_base = ttk.Combobox(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_general_threshold_value_base, style= 'TCombobox', justify= 'center')

        # general threshold - percent ######
        self.button_general_threshold_percent = ttk.Button(
            master= self, text= 'General - Percentage (%)', width= button_width,  padding= 2, 
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        
        ## general threshold - percent Top
        self.label_general_threshold_percent_top= tk.Label(
            master= self, text= 'Top (%)', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            )
        self.strvar_general_threshold_percent_top= tk.StringVar()
        self.combobox_general_threshold_percent_top = ttk.Combobox(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_general_threshold_percent_top, style= 'TCombobox', justify= 'center')
        
        ## general threshold - percent Middle
        self.label_general_threshold_percent_middle= tk.Label(
            master= self, text= 'Middle (%)', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            )
        self.strvar_general_threshold_percent_middle= tk.StringVar()
        self.combobox_general_threshold_percent_middle = ttk.Combobox(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_general_threshold_percent_middle, style= 'TCombobox', justify= 'center')
        
        ## general threshold - percent Base
        self.label_general_threshold_percent_base= tk.Label(
            master= self, text= 'Base (%)', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            )
        self.strvar_general_threshold_percent_base= tk.StringVar()
        self.combobox_general_threshold_percent_base = ttk.Combobox(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_general_threshold_percent_base, style= 'TCombobox', justify= 'center')
        
        # Rise/Fall threshold - value ######
        self.button_RF_threshold_value = ttk.Button(
            master= self, text= 'Ries/Fall - Value (V)', width= button_width,  padding= 2, 
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        
        ## Rise/Fall threshold - value Top
        self.label_RF_threshold_value_top= tk.Label(
            master= self, text= 'Top (V)', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            )
        self.strvar_RF_threshold_value_top= tk.StringVar()
        self.combobox_RF_threshold_value_top = ttk.Combobox(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_RF_threshold_value_top, style= 'TCombobox', justify= 'center')
        
        ## Rise/Fall threshold - value Base
        self.label_RF_threshold_value_base= tk.Label(
            master= self, text= 'Base (V)', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            )
        self.strvar_RF_threshold_value_base= tk.StringVar()
        self.combobox_RF_threshold_value_base = ttk.Combobox(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_RF_threshold_value_base, style= 'TCombobox', justify= 'center')

        # Rise/Fall threshold - percent ######
        self.button_RF_threshold_percent = ttk.Button(
            master= self, text= 'Ries/Fall - Percentage (%)', width= button_width,  padding= 2, 
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        
        ## Rise/Fall threshold - percent Top
        self.label_RF_threshold_percent_top= tk.Label(
            master= self, text= 'Top (%)', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            )
        self.strvar_RF_threshold_percent_top= tk.StringVar()
        self.combobox_RF_threshold_percent_top = ttk.Combobox(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_RF_threshold_percent_top, style= 'TCombobox', justify= 'center')
        
        ## Rise/Fall threshold - percent Base
        self.label_RF_threshold_percent_base= tk.Label(
            master= self, text= 'Base (%)', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            )
        self.strvar_RF_threshold_percent_base= tk.StringVar()
        self.combobox_RF_threshold_percent_base = ttk.Combobox(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_RF_threshold_percent_base, style= 'TCombobox', justify= 'center')
        ################################################

        ### Weight        
        for i in range(7):
            self.rowconfigure(i, weight= 1, uniform= 'row')
        for j in range(4):
            self.columnconfigure(j, weight= 1, uniform= 'col')    
        ###########################

        ## Grid  ==============================================================================================================================================
        self.button_general_threshold_value.grid(row= 0, column= 0, padx= 5, pady= 2, sticky= 'nesw', columnspan= 2)
        self.label_general_threshold_value_top.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_general_threshold_value_top.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.label_general_threshold_value_middle.grid(row= 2, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_general_threshold_value_middle.grid(row= 2, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.label_general_threshold_value_base.grid(row= 3, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_general_threshold_value_base.grid(row= 3, column= 1, padx= 2, pady= 2, sticky= 'ew')

        self.button_general_threshold_percent.grid(row= 0, column= 2, padx= 5, pady= 2, sticky= 'nesw', columnspan= 2)
        self.label_general_threshold_percent_top.grid(row= 1, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_general_threshold_percent_top.grid(row= 1, column= 3, padx= 2, pady= 2, sticky= 'ew')
        self.label_general_threshold_percent_middle.grid(row= 2, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_general_threshold_percent_middle.grid(row= 2, column= 3, padx= 2, pady= 2, sticky= 'ew')
        self.label_general_threshold_percent_base.grid(row= 3, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_general_threshold_percent_base.grid(row= 3, column= 3, padx= 2, pady= 2, sticky= 'ew')

        self.button_RF_threshold_value.grid(row= 4, column= 0, padx= 2, pady= 5, sticky= 'nesw', columnspan= 2)
        self.label_RF_threshold_value_top.grid(row= 5, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_RF_threshold_value_top.grid(row= 5, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.label_RF_threshold_value_base.grid(row= 6, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_RF_threshold_value_base.grid(row= 6, column= 1, padx= 2, pady= 2, sticky= 'ew')

        self.button_RF_threshold_percent.grid(row= 4, column= 2, padx= 5, pady= 2, sticky= 'nesw', columnspan= 2)
        self.label_RF_threshold_percent_top.grid(row= 5, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_RF_threshold_percent_top.grid(row= 5, column= 3, padx= 2, pady= 2, sticky= 'ew')
        self.label_RF_threshold_percent_base.grid(row= 6, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_RF_threshold_percent_base.grid(row= 6, column= 3, padx= 2, pady= 2, sticky= 'ew')
        ###########################

        ## settings  ==============================================================================================================================================
        settings.apply('Threshold_Selected_Values', {
            'GeneralTopPercent': self.strvar_general_threshold_percent_top, 
            'GeneralMiddlePercent': self.strvar_general_threshold_percent_middle, 
            'GeneralBasePercent': self.strvar_general_threshold_percent_base, 
            'GeneralTopValue': self.strvar_general_threshold_value_top, 
            'GeneralMiddleValue': self.strvar_general_threshold_value_middle, 
            'GeneralBaseValue': self.strvar_general_threshold_value_base, 
            'RFTopPercent': self.strvar_RF_threshold_percent_top, 
            'RFBasePercent': self.strvar_RF_threshold_percent_base, 
            'RFTopValue': self.strvar_RF_threshold_value_top, 
            'RFBaseValue': self.strvar_RF_threshold_value_base, 
        })

        # combobox options
        settings.setup_combobox(combobox= self.combobox_general_threshold_percent_top, combobox_var= self.strvar_general_threshold_percent_top, key= "GeneralTopPercent",)
        settings.setup_combobox(combobox= self.combobox_general_threshold_percent_middle, combobox_var= self.strvar_general_threshold_percent_middle, key= "GeneralMiddlePercent",)
        settings.setup_combobox(combobox= self.combobox_general_threshold_percent_base, combobox_var= self.strvar_general_threshold_percent_base, key= "GeneralBasePercent",)
        settings.setup_combobox(combobox= self.combobox_general_threshold_value_top, combobox_var= self.strvar_general_threshold_value_top, key= "GeneralTopValue",)
        settings.setup_combobox(combobox= self.combobox_general_threshold_value_middle, combobox_var= self.strvar_general_threshold_value_middle, key= "GeneralMiddleValue",)
        settings.setup_combobox(combobox= self.combobox_general_threshold_value_base, combobox_var= self.strvar_general_threshold_value_base, key= "GeneralBaseValue",)
        settings.setup_combobox(combobox= self.combobox_RF_threshold_percent_top, combobox_var= self.strvar_RF_threshold_percent_top, key= "RFTopPercent",)
        settings.setup_combobox(combobox= self.combobox_RF_threshold_percent_base, combobox_var= self.strvar_RF_threshold_percent_base, key= "RFBasePercent",)
        settings.setup_combobox(combobox= self.combobox_RF_threshold_value_top, combobox_var= self.strvar_RF_threshold_value_top, key= "RFTopValue",)
        settings.setup_combobox(combobox= self.combobox_RF_threshold_value_base, combobox_var= self.strvar_RF_threshold_value_base, key= "RFBaseValue",)
