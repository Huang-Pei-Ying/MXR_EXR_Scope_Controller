import tkinter as tk
from tkinter import ttk
import utils

class LoadWmemoryLabelFrame(tk.LabelFrame):
    def __init__(self, master, settings, colors, button_width, entry_width):
        super().__init__(master, text= 'Load Wmemory', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)

        self.frame_load_waveform_top= tk.Frame(master= self, background= colors['labelframe'][0])
        self.frame_load_waveform_base= tk.Frame(master= self, background= colors['labelframe'][0])

        self.intvar_load_waveform_savelocation= tk.IntVar()
        self.radiobutton_load_waveform_scopedesktop= ttk.Radiobutton(
            master= self.frame_load_waveform_top, text= 'Scope Desktop', value= 0, variable= self.intvar_load_waveform_savelocation, style= 'radiobutton_2.TRadiobutton')
        self.radiobutton_load_waveform_server= ttk.Radiobutton(
            master= self.frame_load_waveform_top, text= 'Server', value= 1, variable= self.intvar_load_waveform_savelocation, style= 'radiobutton_2.TRadiobutton')
        
        self.strvar_load_waveform_server_segment= tk.StringVar()
        self.combobox_load_waveform_server_segment= ttk.Combobox(
            master= self.frame_load_waveform_top, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_load_waveform_server_segment, style= 'TCombobox', justify= 'center')
        utils.execute_combobox_function(
            combobox= self.combobox_load_waveform_server_segment, combobox_var= self.strvar_load_waveform_server_segment, ini_dict_key= 'LoadWMemoryServerCode', ini_option_section= 'Load_WMemory_Setup_Config', ini_option_key= 'LoadWMemoryServerCode', ini_selected_section= 'Load_WMemory_Selected_Values')

        self.label_load_waveform_scopefolder= tk.Label(
            master= self.frame_load_waveform_base, text= 'Folder', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_load_waveform_scopefolder= tk.StringVar()
        self.entry_load_waveform_scopefolder= ttk.Entry(
            master= self.frame_load_waveform_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_load_waveform_scopefolder)
        self.button_load_waveform_browse_scopefolder= ttk.Button(
            master= self.frame_load_waveform_base, text= 'Browse', width= button_width,  padding= 1,
            # style= 'normal_height.TButton',
            # command= lambda: mxr.
            )

        self.label_load_waveform_wmemory= tk.Label(
            master= self.frame_load_waveform_base, text= 'Wmemory', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_load_waveform_wmemory= tk.StringVar()
        self.combobox_load_waveform_wmemory= ttk.Combobox(
            master= self.frame_load_waveform_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_load_waveform_wmemory, style= 'TCombobox', justify= 'center', 
            values= ['1', '2', '3', '4']
            )

        self.label_load_waveform_filename= tk.Label(
            master= self.frame_load_waveform_base, text= 'File Name', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_load_waveform_filename= tk.StringVar()
        self.entry_load_waveform_filename= ttk.Entry(
            master= self.frame_load_waveform_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_load_waveform_filename)
        self.button_load_waveform_filename_load= ttk.Button(
            master= self.frame_load_waveform_base, text= 'Load', width= button_width,  padding= 1,
            # style= 'normal_height.TButton',
            # command= lambda: mxr.
            )
        self.button_load_waveform_filename_clear= ttk.Button(
            master= self.frame_load_waveform_base, text= 'Clear', width= button_width,  padding= 1,
            # style= 'normal_height.TButton',
            # command= lambda: mxr.
            )
        ################################################

        ### Weight        
        self.rowconfigure(0, weight= 1, uniform= 'row')
        self.rowconfigure(1, weight= 2, uniform= 'row')
        self.columnconfigure(0, weight= 1, uniform= 'col')

        self.frame_load_waveform_top.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_load_waveform_top.columnconfigure(0, weight= 2, uniform= 'col')
        self.frame_load_waveform_top.columnconfigure(1, weight= 1, uniform= 'col')
        self.frame_load_waveform_top.columnconfigure(2, weight= 5, uniform= 'col')

        self.frame_load_waveform_base.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_load_waveform_base.rowconfigure(1, weight= 1, uniform= 'row')
        self.frame_load_waveform_base.columnconfigure(0, weight= 2, uniform= 'col')
        self.frame_load_waveform_base.columnconfigure(1, weight= 2, uniform= 'col')
        self.frame_load_waveform_base.columnconfigure(2, weight= 2, uniform= 'col')
        self.frame_load_waveform_base.columnconfigure(3, weight= 4, uniform= 'col')
        self.frame_load_waveform_base.columnconfigure(4, weight= 1, uniform= 'col')
        self.frame_load_waveform_base.columnconfigure(5, weight= 1, uniform= 'col')
        ###########################

        ## Grid  ==============================================================================================================================================
        self.frame_load_waveform_top.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_load_waveform_base.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')

        self.radiobutton_load_waveform_scopedesktop.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.radiobutton_load_waveform_server.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_load_waveform_server_segment.grid(row= 0, column= 2, padx= 2, pady= 2, sticky= 'w')

        self.label_load_waveform_scopefolder.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.entry_load_waveform_scopefolder.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'ew', columnspan= 3)
        self.button_load_waveform_browse_scopefolder.grid(row= 0, column= 4, padx= 2, pady= 6, sticky= 'ew', columnspan= 2)

        self.label_load_waveform_wmemory.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_load_waveform_wmemory.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'ew')
        
        self.label_load_waveform_filename.grid(row= 1, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        self.entry_load_waveform_filename.grid(row= 1, column= 3, padx= 2, pady= 2, sticky= 'ew')
        self.button_load_waveform_filename_load.grid(row= 1, column= 4, padx= 2, pady= 2, sticky= 'ew')
        self.button_load_waveform_filename_clear.grid(row= 1, column= 5, padx= 2, pady= 2, sticky= 'ew')

        ###########################

        ## settings  ==============================================================================================================================================
        settings.apply('Load_WMemory_Setup_Config', {
            'LoadWMemoryLocation': self.intvar_load_waveform_savelocation, 
            'LoadWMemoryServerCode': self.strvar_load_waveform_server_segment, 
            'LoadWMemoryFolder': self.strvar_load_waveform_scopefolder, 
            'LoadWMemoryChannel': self.strvar_load_waveform_wmemory, 
            'LoadWMemoryFileName': self.strvar_load_waveform_filename, 
        })
