import tkinter as tk
from tkinter import ttk
import utils

class SaveOthersLabelFrame(tk.LabelFrame):
    def __init__(self, master, settings, colors, button_width, entry_width):
        super().__init__(master, text= 'Save Others - in Scope', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)

        self.frame_save_others_top= tk.Frame(master= self, background= colors['labelframe'][0])
        self.frame_save_others_base= tk.Frame(master= self, background= colors['labelframe'][0])
        
        self.intvar_save_others_savelocation= tk.IntVar()
        self.radiobutton_save_others_scopedesktop= ttk.Radiobutton(
            master= self.frame_save_others_top, text= 'Scope Desktop', value= 0, variable= self.intvar_save_others_savelocation, style= 'radiobutton_2.TRadiobutton')
        self.radiobutton_save_others_server= ttk.Radiobutton(
            master= self.frame_save_others_top, text= 'Server', value= 1, variable= self.intvar_save_others_savelocation, style= 'radiobutton_2.TRadiobutton')
        
        self.strvar_save_others_server_segment= tk.StringVar()
        self.combobox_save_others_server_segment= ttk.Combobox(
            master= self.frame_save_others_top, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_save_others_server_segment, style= 'TCombobox', justify= 'center')
        
        self.intvar_save_others_filetype= tk.IntVar()
        self.radiobutton_save_others_wfmfile= ttk.Radiobutton(
            master= self.frame_save_others_top, text= 'Waveform File', value= 0, variable= self.intvar_save_others_filetype, style= 'radiobutton_3.TRadiobutton')
        self.radiobutton_save_others_setupfile= ttk.Radiobutton(
            master= self.frame_save_others_top, text= 'Setup File', value= 1, variable= self.intvar_save_others_filetype, style= 'radiobutton_3.TRadiobutton')

        self.label_save_others_scopefolder= tk.Label(
            master= self.frame_save_others_base, text= 'Folder', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_save_others_scopefolder= tk.StringVar()
        self.entry_save_others_scopefolder= ttk.Entry(
            master= self.frame_save_others_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_save_others_scopefolder)
        self.button_save_others_browse_scopefolder= ttk.Button(
            master= self.frame_save_others_base, text= 'Browse', width= button_width,  padding= 1,
            # style= 'normal_height.TButton',
            # command= lambda: mxr.
            )

        self.label_save_others_channel= tk.Label(
            master= self.frame_save_others_base, text= 'Channel', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_save_others_channel= tk.StringVar()
        self.combobox_save_others_channel= ttk.Combobox(
            master= self.frame_save_others_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_save_others_channel, style= 'TCombobox', justify= 'center', 
            values= ['1', '2', '3', '4']
            )

        self.label_save_others_filename= tk.Label(
            master= self.frame_save_others_base, text= 'File Name', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_save_others_filename= tk.StringVar()
        self.entry_save_others_filename= ttk.Entry(
            master= self.frame_save_others_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_save_others_filename)
        self.button_save_others_filename_save= ttk.Button(
            master= self.frame_save_others_base, text= 'Save', width= button_width,  padding= 1,
            # style= 'normal_height.TButton',
            # command= lambda: mxr.
            )
        ################################################

        ### Weight        
        self.rowconfigure(0, weight= 1, uniform= 'row')
        self.rowconfigure(1, weight= 1, uniform= 'row')
        self.columnconfigure(0, weight= 1, uniform= 'col')

        self.frame_save_others_top.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_save_others_top.rowconfigure(1, weight= 1, uniform= 'row')
        self.frame_save_others_top.columnconfigure(0, weight= 2, uniform= 'col')
        self.frame_save_others_top.columnconfigure(1, weight= 1, uniform= 'col')
        self.frame_save_others_top.columnconfigure(2, weight= 5, uniform= 'col')

        self.frame_save_others_base.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_save_others_base.rowconfigure(1, weight= 1, uniform= 'row')
        self.frame_save_others_base.columnconfigure(0, weight= 1, uniform= 'col')
        self.frame_save_others_base.columnconfigure(1, weight= 1, uniform= 'col')
        self.frame_save_others_base.columnconfigure(2, weight= 1, uniform= 'col')
        self.frame_save_others_base.columnconfigure(3, weight= 3, uniform= 'col')
        self.frame_save_others_base.columnconfigure(4, weight= 1, uniform= 'col')
        ###########################

        ## Grid  ==============================================================================================================================================
        self.frame_save_others_top.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_save_others_base.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')

        self.radiobutton_save_others_scopedesktop.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.radiobutton_save_others_server.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_save_others_server_segment.grid(row= 0, column= 2, padx= 2, pady= 2, sticky= 'w')

        self.radiobutton_save_others_wfmfile.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.radiobutton_save_others_setupfile.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'nesw', columnspan= 2)

        self.label_save_others_scopefolder.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.entry_save_others_scopefolder.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'ew', columnspan= 3)
        self.button_save_others_browse_scopefolder.grid(row= 0, column= 4, padx= 2, pady= 2, sticky= 'ew')

        self.label_save_others_channel.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_save_others_channel.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'ew')
        
        self.label_save_others_filename.grid(row= 1, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        self.entry_save_others_filename.grid(row= 1, column= 3, padx= 2, pady= 2, sticky= 'ew')
        self.button_save_others_filename_save.grid(row= 1, column= 4, padx= 2, pady= 2, sticky= 'ew')
        ###########################

        ## settings  ==============================================================================================================================================
        settings.apply('Save_Other_Setup_Config', {
            'SaveOtherLocation': self.intvar_save_others_savelocation, 
            'SaveOtherFileType': self.intvar_save_others_filetype, 
            'SaveOtherFolder': self.strvar_save_others_scopefolder, 
            'SaveOtherChannel': self.strvar_save_others_channel, 
            'SaveOtherFileName': self.strvar_save_others_filename, 
        })
        settings.apply('Save_Other_Selected_Values', {
            'SaveOtherServerCode': self.strvar_save_others_server_segment, 
        })

        # combobox options
        settings.setup_combobox(combobox= self.combobox_save_others_server_segment, combobox_var= self.strvar_save_others_server_segment, key= "SaveOtherServerCode",)

        ## else  ==============================================================================================================================================
        utils.move_mouse_entry_end(entry= self.entry_save_others_scopefolder)