import tkinter as tk
from tkinter import ttk

class ScaleLabelFrame(tk.LabelFrame):
    def __init__(self, master, settings, mxr, colors, button_width, entry_width):
        super().__init__(master, text= 'Scale/Offset/Trigger', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)
                
        self.frame_scalearea_top= tk.Frame(master= self, background= colors['labelframe'][0])
        # voltage_scale
        self.button_voltage_scale = ttk.Button(
            master= self.frame_scalearea_top, 
            text= 'Voltage Scale (V)', 
            width= button_width,  
            padding= 1, 
            style= 'normal_height.TButton',
            command= lambda: mxr.set_voltage_scale(voltage_scale= self.strvar_voltage_scale.get())
            )

        self.strvar_voltage_scale= tk.StringVar(master= self)
        self.combobox_voltage_scale = ttk.Combobox(
            master= self.frame_scalearea_top, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_voltage_scale, style= 'TCombobox', justify= 'center')

        # voltage_offset
        self.button_voltage_offset = ttk.Button(
            master= self.frame_scalearea_top, text= 'Voltage Offset (V)', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.set_voltage_offset(voltage_offset= self.strvar_voltage_offset.get())
            )

        self.strvar_voltage_offset= tk.StringVar()
        self.combobox_voltage_offset = ttk.Combobox(
            master= self.frame_scalearea_top, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_voltage_offset, style= 'TCombobox', justify= 'center')

        # timebase scale
        self.button_timebase_scale = ttk.Button(
            master= self.frame_scalearea_top, text= 'Timebase Scale (sec)', width= button_width, padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.set_timebase_scale(timebase_scale= self.strvar_timebase_scale.get())
            )

        self.strvar_timebase_scale= tk.StringVar()
        self.entry_timebase_scale = ttk.Entry(master= self.frame_scalearea_top, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_timebase_scale, style= 'TEntry', justify= 'center')

        # timebase offset
        self.button_timebase_offset= ttk.Button(
            master= self.frame_scalearea_top, text= 'Timebase Offset (sec)', width= button_width, padding= 1, 
            style= 'normal_height.TButton',
            command= lambda: mxr.set_timebase_offset(timebase_position= self.strvar_timebase_offset.get())
            )

        self.strvar_timebase_offset= tk.StringVar()
        self.entry_timebase_offset = ttk.Entry(master= self.frame_scalearea_top, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_timebase_offset, style= 'TEntry', justify= 'center')

        # trigger channel
        self.button_trigger_channel = ttk.Button(
            master= self.frame_scalearea_top, text= 'Trigger Channel', width= button_width, padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.set_trigger_channel(trigger_channel= self.strvar_trigger_channel.get())
            )

        self.strvar_trigger_channel= tk.StringVar()
        self.combobox_trigger_channel = ttk.Combobox(
            master= self.frame_scalearea_top, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_trigger_channel, style= 'TCombobox', justify= 'center', values= ['1', '2', '3', '4'])

        # trigger level
        self.button_trigger_level = ttk.Button(
            master= self.frame_scalearea_top, text= 'Trigger Level (V)', width= button_width, padding= 1, 
            style= 'normal_height.TButton', 
            command= lambda: mxr.set_trigger_level(trigger_level= self.strvar_trigger_level.get())
            )

        self.strvar_trigger_level= tk.StringVar()
        self.combobox_trigger_level = ttk.Combobox(
            master= self.frame_scalearea_top, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_trigger_level, style= 'TCombobox', justify= 'center')

        self.frame_scalearea_bottom= tk.Frame(master= self, background= colors['labelframe'][0])
        # buttons
        self.button_trigger_mode = ttk.Button(
            master= self.frame_scalearea_bottom, text= 'Trigger Mode', width= button_width, padding= 2, 
            style= 'double_height.TButton', 
            command= lambda: mxr.set_trigger_mode()
            )
        self.button_trigger_slope = ttk.Button(
            master= self.frame_scalearea_bottom, text= 'Trigger Slope', width= button_width, padding= 2, 
            style= 'double_height.TButton', 
            command= lambda: mxr.set_trigger_slope()
            )
        self.button_set_all = ttk.Button(
            master= self.frame_scalearea_bottom, text= 'All Set', width= button_width, padding= 2, 
            style= 'special.TButton', 
            command= lambda: mxr.set_all_scale(
                voltage_scale= self.strvar_voltage_scale.get(), 
                voltage_offset= self.strvar_voltage_offset.get(), 
                timebase_scale= self.strvar_timebase_scale.get(), 
                timebase_position= self.strvar_timebase_offset.get(), 
                trigger_channel= self.strvar_trigger_channel.get(), 
                trigger_level= self.strvar_trigger_level.get()
            ))

        ################################################

        ### Weight  ==============================================================================================================================================
        self.rowconfigure(0, weight= 3, uniform= 'row')
        self.rowconfigure(1, weight= 1, uniform= 'row')
        self.columnconfigure(0, weight= 1, uniform= 'col')
        
        for i in range(4):
            self.frame_scalearea_top.rowconfigure(i, weight= 1, uniform= 'row')
        for j in range(4):
            if j % 2 == 0:
                self.frame_scalearea_top.columnconfigure(j, weight= 2, uniform= 'col')
            else:
                self.frame_scalearea_top.columnconfigure(j, weight= 1, uniform= 'col')

        self.frame_scalearea_bottom.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_scalearea_bottom.columnconfigure(0, weight= 1, uniform= 'col')
        self.frame_scalearea_bottom.columnconfigure(1, weight= 1, uniform= 'col')
        self.frame_scalearea_bottom.columnconfigure(2, weight= 1, uniform= 'col')
        ###########################

        ## Grid  ==============================================================================================================================================
        self.frame_scalearea_top.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_scalearea_bottom.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        ### top area
        self.button_voltage_scale.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'ew')
        self.combobox_voltage_scale.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.button_timebase_scale.grid(row= 0, column= 2, padx= 2, pady= 2, sticky= 'ew')
        self.entry_timebase_scale.grid(row= 0, column= 3, padx= 2, pady= 2, sticky= 'ew')
        self.button_voltage_offset.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'ew')
        self.combobox_voltage_offset.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.button_timebase_offset.grid(row= 1, column= 2, padx= 2, pady= 2, sticky= 'ew')
        self.entry_timebase_offset.grid(row= 1, column= 3, padx= 2, pady= 2, sticky= 'ew')
        self.button_trigger_channel.grid(row= 2, column= 0, padx= 2, pady= 2, sticky= 'ew')
        self.combobox_trigger_channel.grid(row= 2, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.button_trigger_level.grid(row= 3, column= 0, padx= 2, pady= 2, sticky= 'ew')
        self.combobox_trigger_level.grid(row= 3, column= 1, padx= 2, pady= 2, sticky= 'ew')
        ### bottom area
        self.button_trigger_mode.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'w')
        self.button_trigger_slope.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'w')
        self.button_set_all.grid(row= 0, column= 2, padx= 2, pady= 2, sticky= 'w')
        ###########################
        
        ## settings  ==============================================================================================================================================
        settings.apply('Scale_Offset_Selected_Values', {
            'VoltageScale': self.strvar_voltage_scale, 
            'VoltageOffset': self.strvar_voltage_offset, 
            'TriggerLevel': self.strvar_trigger_level, 
        })
        settings.apply('Scale_Offset_Config', {
            'TimebaseScale': self.strvar_timebase_scale, 
            'TimebaseOffset': self.strvar_timebase_offset, 
            'TriggerChannel': self.strvar_trigger_channel, 
        })
        
        # combobox options
        settings.setup_combobox(combobox= self.combobox_voltage_scale, combobox_var= self.strvar_voltage_scale, key= "VoltageScale",)
        settings.setup_combobox(combobox= self.combobox_voltage_offset, combobox_var= self.strvar_voltage_offset, key= "VoltageOffset",)
        settings.setup_combobox(combobox= self.combobox_trigger_level, combobox_var= self.strvar_trigger_level, key= "TriggerLevel",)
