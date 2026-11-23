import tkinter as tk
from tkinter import ttk
import utils

class SaveImageLabelFrame(tk.LabelFrame):
    def __init__(self, master, settings, colors, button_width, entry_width):
        super().__init__(master, text= 'Save Image - in PC', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)

        self.label_save_img_pcfolder= tk.Label(
            master= self, text= 'PC Folder', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_save_img_pcfolder= tk.StringVar()
        self.entry_save_img_pcfolder= ttk.Entry(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_save_img_pcfolder)
        self.button_browse_img_pcfolder= ttk.Button(
            master= self, text= 'Browse', width= button_width,  padding= 1,
            # style= 'normal_height.TButton',
            # command= lambda: mxr.
            )
        self.label_save_img_name= tk.Label(
            master= self, text= 'File Name', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_save_img_name= tk.StringVar()
        self.entry_save_img_name= ttk.Entry(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_save_img_name)
        self.button_save_img_name= ttk.Button(
            master= self, text= 'Save', width= button_width,  padding= 1,
            # style= 'normal_height.TButton',
            # command= lambda: mxr.
            )
        ################################################

        ### Weight        
        self.rowconfigure(0, weight= 1, uniform= 'row')
        self.rowconfigure(1, weight= 1, uniform= 'row')
        self.columnconfigure(0, weight= 1, uniform= 'col')
        self.columnconfigure(1, weight= 5, uniform= 'col')
        self.columnconfigure(2, weight= 1, uniform= 'col')
        ###########################

        ## Grid  ==============================================================================================================================================
        self.label_save_img_pcfolder.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.entry_save_img_pcfolder.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.button_browse_img_pcfolder.grid(row= 0, column= 2, padx= 5, pady= 5, sticky= 'ew')
        
        self.label_save_img_name.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.entry_save_img_name.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.button_save_img_name.grid(row= 1, column= 2, padx= 5, pady= 5, sticky= 'ew')
        ###########################

        ## settings  ==============================================================================================================================================
        settings.apply('Save_Img_Setup_Config', {
            'SaveImgPCFolder': self.strvar_save_img_pcfolder, 
            'SaveImgName': self.strvar_save_img_name, 
        })
