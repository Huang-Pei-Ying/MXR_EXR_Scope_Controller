import tkinter as tk
from tkinter import ttk
import utils

class LoadSetupLabelFrame(tk.LabelFrame):
    def __init__(self, master, root, settings, mxr, colors, button_width, entry_width):
        super().__init__(master, text= 'Load Setup File', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)

        self.root = root

        self.frame_load_setup_1= tk.Frame(master= self, background= colors['labelframe'][0])
        self.frame_load_setup_2= tk.Frame(master= self, background= colors['labelframe'][0])
        self.frame_load_setup_3= tk.Frame(master= self, background= colors['labelframe'][0])
        self.frame_load_setup_4= tk.Frame(master= self, background= colors['labelframe'][0])

        self.intvar_load_setup_call_file_type= tk.IntVar()
        self.radiobutton_load_setup_user_defined= ttk.Radiobutton(
            master= self.frame_load_setup_1, text= 'User-defined', value= 0, variable= self.intvar_load_setup_call_file_type, style= 'radiobutton_3.TRadiobutton', )
        self.radiobutton_load_setup_standard= ttk.Radiobutton(
            master= self.frame_load_setup_1, text= 'Standard', value= 1, variable= self.intvar_load_setup_call_file_type, style= 'radiobutton_3.TRadiobutton',)

        self.intvar_load_setup_loadlocation= tk.IntVar()
        self.radiobutton_load_setup_location_scope= ttk.Radiobutton(
            master= self.frame_load_setup_1, text= 'Scope Desktop', value= 0, variable= self.intvar_load_setup_loadlocation, style= 'radiobutton_2.TRadiobutton')
        self.radiobutton_load_setup_location_server= ttk.Radiobutton(
            master= self.frame_load_setup_1, text= 'Server', value= 1, variable= self.intvar_load_setup_loadlocation, style= 'radiobutton_2.TRadiobutton')
        self.strvar_load_setup_location_server= tk.StringVar()
        self.combobox_load_setup_location_server= ttk.Combobox(
            master= self.frame_load_setup_1, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_load_setup_location_server, style= 'TCombobox', justify= 'center')

        self.label_load_setup_user_defined_folder= tk.Label(
            master= self.frame_load_setup_2, text= 'Folder', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_load_setup_user_defined_folder= tk.StringVar()
        self.entry_load_setup_user_defined_folder= ttk.Entry(
            master= self.frame_load_setup_2, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_load_setup_user_defined_folder)
        self.button_load_setup_user_defined_browse= ttk.Button(
            master= self.frame_load_setup_2, text= 'Browse', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: utils.browse_folder(entry_var= self.strvar_load_setup_user_defined_folder, target_entry= self.entry_load_setup_user_defined_folder)
            )

        self.label_load_setup_user_defined_filename= tk.Label(
            master= self.frame_load_setup_2, text= 'File Name', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_load_setup_user_defined_filename= tk.StringVar()
        self.entry_load_setup_user_defined_filename= ttk.Entry(
            master= self.frame_load_setup_2, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_load_setup_user_defined_filename)
        self.button_load_setup_user_defined_load= ttk.Button(
            master= self.frame_load_setup_2, text= 'Load', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.load_setup(
                root= self.root, 
                user_choice= self.intvar_load_setup_call_file_type.get(), 
                location_choice= self.intvar_load_setup_loadlocation.get(), 
                server_code= self.strvar_load_setup_location_server.get(), 
                interface= self.strvar_load_setup_standard_interface.get(), 
                sub= self.strvar_load_setup_standard_subfolder.get(), 
                folder_path= self.strvar_load_setup_user_defined_folder.get(), 
                setup_name= self.strvar_load_setup_user_defined_filename.get(), 
                is_keep_timebase= self.boolvar_modify_timebase.get(), 
                is_keep_voltage= self.boolvar_modify_voltage.get(), 
                is_keep_labelname= self.boolvar_modify_label.get(), 
            ))

        self.boolvar_modify_label= tk.BooleanVar()
        self.checkbutton_modify_label= ttk.Checkbutton(
            master= self.frame_load_setup_3, text= 'Label', variable= self.boolvar_modify_label, style= 'checkbutton_1.TCheckbutton')
        self.boolvar_modify_timebase= tk.BooleanVar()
        self.checkbutton_modify_timebase= ttk.Checkbutton(
            master= self.frame_load_setup_3, text= 'Time', variable= self.boolvar_modify_timebase, style= 'checkbutton_1.TCheckbutton')
        self.boolvar_modify_voltage= tk.BooleanVar()
        self.checkbutton_modify_voltage= ttk.Checkbutton(
            master= self.frame_load_setup_3, text= 'Voltage', variable= self.boolvar_modify_voltage, style= 'checkbutton_1.TCheckbutton')
        
        self.strvar_load_setup_standard_interface= tk.StringVar()
        self.combobox_load_setup_standard_interface= ttk.Combobox(
            master= self.frame_load_setup_4, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_load_setup_standard_interface, style= 'TCombobox', justify= 'center', )
        
        self.strvar_load_setup_standard_subfolder= tk.StringVar()
        self.combobox_load_setup_standard_subfolder= ttk.Combobox(
            master= self.frame_load_setup_4, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_load_setup_standard_subfolder, style= 'TCombobox', justify= 'center')

        self.strvar_load_setup_standard_files= tk.StringVar()
        self.combobox_load_setup_standard_files= ttk.Combobox(
            master= self.frame_load_setup_4, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_load_setup_standard_files, style= 'TCombobox', justify= 'center')

        self.button_load_setup_standard_load= ttk.Button(
            master= self.frame_load_setup_4, text= 'Load', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.load_setup(
                root= self.root, 
                user_choice= self.intvar_load_setup_call_file_type.get(), 
                location_choice= self.intvar_load_setup_loadlocation.get(), 
                server_code= self.strvar_load_setup_location_server.get(), 
                interface= self.strvar_load_setup_standard_interface.get(), 
                sub= self.strvar_load_setup_standard_subfolder.get(), 
                folder_path= self.strvar_load_setup_user_defined_folder.get(), 
                setup_name= self.strvar_load_setup_standard_files.get(), 
                is_keep_timebase= self.boolvar_modify_timebase.get(), 
                is_keep_voltage= self.boolvar_modify_voltage.get(), 
                is_keep_labelname= self.boolvar_modify_label.get(), 
            ))
        ################################################

        ### Weight  ==============================================================================================================================================   
        self.rowconfigure(0, weight= 2, uniform= 'row')
        self.rowconfigure(1, weight= 2, uniform= 'row')
        self.rowconfigure(2, weight= 1, uniform= 'row')
        self.rowconfigure(3, weight= 1, uniform= 'row')
        self.columnconfigure(0, weight= 1, uniform= 'col')

        self.frame_load_setup_1.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_load_setup_1.rowconfigure(1, weight= 1, uniform= 'row')
        self.frame_load_setup_1.columnconfigure(0, weight= 2, uniform= 'col')
        self.frame_load_setup_1.columnconfigure(1, weight= 1, uniform= 'col')
        self.frame_load_setup_1.columnconfigure(2, weight= 5, uniform= 'col')

        self.frame_load_setup_2.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_load_setup_2.rowconfigure(1, weight= 1, uniform= 'row')
        self.frame_load_setup_2.columnconfigure(0, weight= 1, uniform= 'col')
        self.frame_load_setup_2.columnconfigure(1, weight= 6, uniform= 'col')
        self.frame_load_setup_2.columnconfigure(2, weight= 1, uniform= 'col')

        self.frame_load_setup_3.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_load_setup_3.columnconfigure(0, weight= 1, uniform= 'col')
        self.frame_load_setup_3.columnconfigure(1, weight= 1, uniform= 'col')
        self.frame_load_setup_3.columnconfigure(2, weight= 5, uniform= 'col')

        self.frame_load_setup_4.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_load_setup_4.columnconfigure(0, weight= 1, uniform= 'col')
        self.frame_load_setup_4.columnconfigure(1, weight= 4, uniform= 'col')
        self.frame_load_setup_4.columnconfigure(2, weight= 2, uniform= 'col')
        self.frame_load_setup_4.columnconfigure(3, weight= 1, uniform= 'col')
        ###########################

        ## Grid  ==============================================================================================================================================
        self.frame_load_setup_1.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_load_setup_2.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_load_setup_3.grid(row= 2, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_load_setup_4.grid(row= 3, column= 0, padx= 2, pady= 2, sticky= 'nesw')

        self.radiobutton_load_setup_user_defined.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.radiobutton_load_setup_standard.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'nesw', columnspan= 2)

        self.radiobutton_load_setup_location_scope.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.radiobutton_load_setup_location_server.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_load_setup_location_server.grid(row= 1, column= 2, padx= 2, pady= 2, sticky= 'w')

        self.label_load_setup_user_defined_folder.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.entry_load_setup_user_defined_folder.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.button_load_setup_user_defined_browse.grid(row= 0, column= 2, padx= 2, pady= 2, sticky= 'ew')

        self.label_load_setup_user_defined_filename.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.entry_load_setup_user_defined_filename.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.button_load_setup_user_defined_load.grid(row= 1, column= 2, padx= 2, pady= 2, sticky= 'ew')

        self.checkbutton_modify_label.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_modify_timebase.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.checkbutton_modify_voltage.grid(row= 0, column= 2, padx= 2, pady= 2, sticky= 'nesw')

        self.combobox_load_setup_standard_interface.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'ew')
        self.combobox_load_setup_standard_subfolder.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.combobox_load_setup_standard_files.grid(row= 0, column= 2, padx= 2, pady= 2, sticky= 'ew')
        self.button_load_setup_standard_load.grid(row= 0, column= 3, padx= 2, pady= 2, sticky= 'ew')
        ###########################

        ## settings  ==============================================================================================================================================
        settings.apply('Load_SetupFile_Setup_Config', {
            'LoadSetupFile_Type': self.intvar_load_setup_call_file_type, 
            'LoadSetupFileLocation': self.intvar_load_setup_loadlocation, 
            'LoadSetupFileFolder': self.strvar_load_setup_user_defined_folder, 
            'LoadSetupFileFileName': self.strvar_load_setup_user_defined_filename, 
            'LoadSetupFileSubLabel': self.boolvar_modify_label, 
            'LoadSetupFileSubTime': self.boolvar_modify_timebase, 
            'LoadSetupFileSubVoltage': self.boolvar_modify_voltage, 
            'LoadSetupFileInterface': self.strvar_load_setup_standard_interface, 
            'LoadSetupFileClass': self.strvar_load_setup_standard_subfolder, 
            'LoadSetupFileName': self.strvar_load_setup_standard_files,
        })
        settings.apply('Load_SetupFile_Selected_Values', {
            'LoadSetupFileServerCode': self.strvar_load_setup_location_server, 
        })

        # combobox options
        settings.setup_combobox(combobox= self.combobox_load_setup_location_server, combobox_var= self.strvar_load_setup_location_server, key= "LoadSetupFileServerCode",)

        ## else  ==============================================================================================================================================
        user_defined_list= [
            self.label_load_setup_user_defined_folder, 
            self.label_load_setup_user_defined_filename, 
            self.entry_load_setup_user_defined_folder, 
            self.entry_load_setup_user_defined_filename, 
            self.button_load_setup_user_defined_browse, 
            self.button_load_setup_user_defined_load,
        ]
        standard_list= [
            # self.checkbutton_modify_label, 
            # self.checkbutton_modify_timebase, 
            # self.checkbutton_modify_voltage, 
            self.combobox_load_setup_standard_interface, 
            self.combobox_load_setup_standard_subfolder, 
            self.combobox_load_setup_standard_files, 
            self.button_load_setup_standard_load, 
        ]      
        
        utils.block_by_choice(var_value= self.intvar_load_setup_call_file_type.get(), user_defined_list= user_defined_list, standard_list= standard_list)            
        
        self.radiobutton_load_setup_user_defined.config(command= lambda: utils.block_by_choice(var_value= self.intvar_load_setup_call_file_type.get(), user_defined_list= user_defined_list, standard_list= standard_list))
        self.radiobutton_load_setup_standard.config(command= lambda: utils.block_by_choice(var_value= self.intvar_load_setup_call_file_type.get(), user_defined_list= user_defined_list, standard_list= standard_list)
                                                        )
        interface_options = utils.search_every_interface()
        self.combobox_load_setup_standard_interface.config(values= interface_options)
        
        sub_options = utils.search_every_sub(interface= self.strvar_load_setup_standard_interface.get())
        self.combobox_load_setup_standard_subfolder.config(values= sub_options)

        setupfiles_options = utils.search_every_setupfiles(interface= self.strvar_load_setup_standard_interface.get(), sub= self.strvar_load_setup_standard_subfolder.get())
        self.combobox_load_setup_standard_subfolder.config(values= setupfiles_options)

        utils.move_mouse_entry_end(entry= self.entry_load_setup_user_defined_folder)