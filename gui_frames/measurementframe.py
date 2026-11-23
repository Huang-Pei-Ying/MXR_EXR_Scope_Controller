import tkinter as tk
from tkinter import ttk
import utils

class MeasurementLabelFrame(tk.LabelFrame):
    def __init__(self, master, settings, colors, button_width, entry_width):
        super().__init__(master, text= 'Measurement', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)

        self.frame_measurement_top= tk.Frame(master= self, background= colors['labelframe'][0])
        self.frame_measurement_middle= tk.Frame(master= self, background= colors['labelframe'][0])
        self.frame_measurement_base= tk.Frame(master= self, background= colors['labelframe'][0])

        self.frame_measurement_top_left= tk.Frame(master= self.frame_measurement_top, background= colors['labelframe'][0])
        self.frame_measurement_top_right= tk.Frame(master= self.frame_measurement_top, background= colors['labelframe'][0])

        self.frame_measurement_base_left= tk.Frame(master= self.frame_measurement_base, background= colors['labelframe'][0])
        self.frame_measurement_base_middle= tk.Frame(master= self.frame_measurement_base, background= colors['labelframe'][0])
        self.frame_measurement_base_right= tk.Frame(master= self.frame_measurement_base, background= colors['labelframe'][0])
        
        self.button_show_result_table= ttk.Button(
            master= self.frame_measurement_top_left, text= 'Show Results Table', width= button_width,  padding= 2,
            # style= 'special.TButton',
            # command= lambda: mxr.
            )

        self.intvar_measurement_channel= tk.IntVar()
        self.radiobutton_single_channel= ttk.Radiobutton(
            master= self.frame_measurement_top_left, text= 'Single Channel', value= 1, variable= self.intvar_measurement_channel, style= 'radiobutton_1.TRadiobutton', 
        )
        self.radiobutton_double_channels= ttk.Radiobutton(
            master= self.frame_measurement_base_left, text= 'Double Channels', value= 2, variable= self.intvar_measurement_channel, style= 'radiobutton_1.TRadiobutton', 
        )

        self.strvar_measurement_single_channel= tk.StringVar()
        self.combobox_measurement_single_channel= ttk.Combobox(
            master= self.frame_measurement_top_left, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_measurement_single_channel, style= 'TCombobox', justify= 'center', 
            values= ['1', '2', '3', '4']
            )
        
        self.button_measurement_frequency= ttk.Button(
            master= self.frame_measurement_top_right, text= 'Frequency', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_period= ttk.Button(
            master= self.frame_measurement_top_right, text= 'Period', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_dutycycle= ttk.Button(
            master= self.frame_measurement_top_right, text= 'Duty Cycle', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_tH= ttk.Button(
            master= self.frame_measurement_top_right, text= 'High time', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_tL= ttk.Button(
            master= self.frame_measurement_top_right, text= 'Low time', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_tR= ttk.Button(
            master= self.frame_measurement_top_right, text= 'Rising time', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_tF= ttk.Button(
            master= self.frame_measurement_top_right, text= 'Falling time', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_slewR= ttk.Button(
            master= self.frame_measurement_top_right, text= 'Slew Rate-Falling', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_slewF= ttk.Button(
            master= self.frame_measurement_top_right, text= 'Slew Rate-Rising', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_perper= ttk.Button(
            master= self.frame_measurement_top_right, text= '1 per-per', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_VIH= ttk.Button(
            master= self.frame_measurement_top_right, text= 'VIH', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_VIL= ttk.Button(
            master= self.frame_measurement_top_right, text= 'VIL', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_VPP= ttk.Button(
            master= self.frame_measurement_top_right, text= 'VPP', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_Vmax= ttk.Button(
            master= self.frame_measurement_top_right, text= 'Vmax', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        self.button_measurement_Vmin= ttk.Button(
            master= self.frame_measurement_top_right, text= 'Vmin', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )

        self.label_delta_setting= tk.Label(
            master= self.frame_measurement_middle, text= f'{100*"-"} Delta Setting {100*"-"}', 
            background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 

        self.boolvar_modify_delta_name= tk.BooleanVar()
        checkbutton_modify_delta_name= ttk.Checkbutton(
            master= self.frame_measurement_base_left, text= 'Modify Name', variable= self.boolvar_modify_delta_name, style= 'checkbutton_1.TCheckbutton',
        )
        self.strvar_modify_delta_name= tk.StringVar()
        combobox_modify_delta_name= ttk.Combobox(
            master= self.frame_measurement_base_left, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_modify_delta_name, style= 'TCombobox', justify= 'center', 
            values= ['Setup time', 'Hold time']
            )
        self.label_delta_start= tk.Label(
            master= self.frame_measurement_base_middle, text= 'Start', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.label_delta_arrow= tk.Label(
            master= self.frame_measurement_base_middle, text= '↓', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.label_delta_stop= tk.Label(
            master= self.frame_measurement_base_middle, text= 'Stop', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.label_delta_channel= tk.Label(
            master= self.frame_measurement_base_middle, text= 'Channel', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_delta_channel_start= tk.StringVar()
        self.combobox_delta_channel_start= ttk.Combobox(
            master= self.frame_measurement_base_middle, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_delta_channel_start, style= 'TCombobox', justify= 'center', 
            values= ['1', '2', '3', '4']
            )
        self.label_delta_channel_arrow= tk.Label(
            master= self.frame_measurement_base_middle, text= '↓', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_delta_channel_stop= tk.StringVar()
        self.combobox_delta_channel_stop= ttk.Combobox(
            master= self.frame_measurement_base_middle, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_delta_channel_stop, style= 'TCombobox', justify= 'center', 
            values= ['1', '2', '3', '4']
            )
        self.button_deita_channel_switch= ttk.Button(
            master= self.frame_measurement_base_middle, text= 'Switch', width= button_width,  padding= 1,
            # style= 'normal_height.TButton',
            command= lambda: utils.switch_string(var_1= self.strvar_delta_channel_start, var_2= self.strvar_delta_channel_stop)
            )
        self.label_delta_transition= tk.Label(
            master= self.frame_measurement_base_middle, text= 'Transition', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_delta_transition_start= tk.StringVar()
        combobox_delta_transition_start= ttk.Combobox(
            master= self.frame_measurement_base_middle, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_delta_transition_start, style= 'TCombobox', justify= 'center', 
            values= ['Rising', 'Falling']
            )
        self.label_delta_transition_arrow= tk.Label(
            master= self.frame_measurement_base_middle, text= '↓', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_delta_transition_stop= tk.StringVar()
        combobox_delta_transition_stop= ttk.Combobox(
            master= self.frame_measurement_base_middle, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_delta_transition_stop, style= 'TCombobox', justify= 'center', 
            values= ['Rising', 'Falling']
            )
        self.button_deita_transition_switch= ttk.Button(
            master= self.frame_measurement_base_middle, text= 'Switch', width= button_width,  padding= 1,
            # style= 'normal_height.TButton',
            command= lambda: utils.switch_string(var_1= self.strvar_delta_transition_start, var_2= self.strvar_delta_transition_stop)
            )
        
        self.label_delta_edge= tk.Label(
            master= self.frame_measurement_base_middle, text= 'Edge No.', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.intvar_delta_edge_start= tk.IntVar()
        self.entry_delta_edge_start = ttk.Entry(
            master= self.frame_measurement_base_middle, width= max(10, int(entry_width*0.4)), textvariable= self.intvar_delta_edge_start, justify= 'center')
        self.label_delta_edge_arrow= tk.Label(
            master= self.frame_measurement_base_middle, text= '↓', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.intvar_delta_edge_stop= tk.IntVar()
        self.entry_delta_edge_stop = ttk.Entry(
            master= self.frame_measurement_base_middle, width= max(10, int(entry_width*0.4)), textvariable= self.intvar_delta_edge_stop, justify= 'center')
        self.button_deita_edge_switch= ttk.Button(
            master= self.frame_measurement_base_middle, text= 'Switch', width= button_width,  padding= 1,
            # style= 'normal_height.TButton',
            command= lambda: utils.switch_string(var_1= self.intvar_delta_edge_start, var_2= self.intvar_delta_edge_stop)
            )
        self.label_delta_position= tk.Label(
            master= self.frame_measurement_base_middle, text= 'Position', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_delta_position_start= tk.StringVar()
        self.combobox_delta_position_start= ttk.Combobox(
            master= self.frame_measurement_base_middle, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_delta_position_start, style= 'TCombobox', justify= 'center', 
            values= ['Upper', 'Middle', 'Lower']
            )
        self.label_delta_position_arrow= tk.Label(
            master= self.frame_measurement_base_middle, text= '↓', background= colors['label'][0], fg= colors['label'][1], font= ('Candara', 11,),
            ) 
        self.strvar_delta_position_stop= tk.StringVar()
        self.combobox_delta_position_stop= ttk.Combobox(
            master= self.frame_measurement_base_middle, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_delta_position_stop, style= 'TCombobox', justify= 'center', 
            values= ['Upper', 'Middle', 'Lower']
            )
        self.button_deita_position_switch= ttk.Button(
            master= self.frame_measurement_base_middle, text= 'Switch', width= button_width,  padding= 1,
            # style= 'normal_height.TButton',
            command= lambda: utils.switch_string(var_1= self.strvar_delta_position_start, var_2= self.strvar_delta_position_stop)
            )
        self.button_measurement_deltatime= ttk.Button(
            master= self.frame_measurement_base_right, text= 'Delta time', width= button_width,  padding= 2,
            # style= 'double_height.TButton',
            # command= lambda: mxr.
            )
        ################################################

        ### Weight      
        self.rowconfigure(0, weight= 4, uniform= 'row')
        self.rowconfigure(1, weight= 1, uniform= 'row')
        self.rowconfigure(2, weight= 5, uniform= 'row')
        self.columnconfigure(0, weight= 4, uniform= 'col')

        self.frame_measurement_top.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_measurement_top.columnconfigure(0, weight= 1, uniform= 'col')
        self.frame_measurement_top.columnconfigure(1, weight= 3, uniform= 'col')

        self.frame_measurement_middle.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_measurement_middle.columnconfigure(0, weight= 1, uniform= 'col')

        self.frame_measurement_base.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_measurement_base.columnconfigure(0, weight= 2, uniform= 'col')
        self.frame_measurement_base.columnconfigure(1, weight= 6, uniform= 'col')
        self.frame_measurement_base.columnconfigure(2, weight= 1, uniform= 'col')

        self.frame_measurement_top_left.rowconfigure(0, weight= 3, uniform= 'row')
        self.frame_measurement_top_left.rowconfigure(1, weight= 1, uniform= 'row')
        self.frame_measurement_top_left.columnconfigure(0, weight= 1, uniform= 'col')
        self.frame_measurement_top_left.columnconfigure(1, weight= 1, uniform= 'col')

        for i in range(3):
            self.frame_measurement_top_right.rowconfigure(i, weight= 1, uniform= 'row')
        for j in range(5):
            self.frame_measurement_top_right.columnconfigure(j, weight= 1, uniform= 'col')
        
        self.frame_measurement_base_left.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_measurement_base_left.rowconfigure(1, weight= 5, uniform= 'row')
        self.frame_measurement_base_left.columnconfigure(0, weight= 1, uniform= 'col')
        self.frame_measurement_base_left.columnconfigure(1, weight= 1, uniform= 'col')

        for i in range(5):
            self.frame_measurement_base_middle.rowconfigure(i, weight= 1, uniform= 'row')
        self.frame_measurement_base_middle.columnconfigure(0, weight= 2, uniform= 'col')
        for j in range(1, 5):
            self.frame_measurement_base_middle.columnconfigure(j, weight= 3, uniform= 'col')

        self.frame_measurement_base_right.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_measurement_base_right.columnconfigure(0, weight= 1, uniform= 'col')
        ###########################

        ## Grid  ==============================================================================================================================================
        self.frame_measurement_top.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_measurement_middle.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_measurement_base.grid(row= 2, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        
        self.frame_measurement_top_left.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_measurement_top_right.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'nesw')

        self.frame_measurement_base_left.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_measurement_base_middle.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_measurement_base_right.grid(row= 0, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        
        self.button_show_result_table.grid(row= 0, column= 0, padx= 30, pady= 20, sticky= 'nesw', columnspan= 2)
        self.radiobutton_single_channel.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_measurement_single_channel.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'nesw')

        self.button_measurement_frequency.grid(row= 0, column= 0, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_period.grid(row= 0, column= 1, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_dutycycle.grid(row= 0, column= 2, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_tH.grid(row= 0, column= 3, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_tL.grid(row= 0, column= 4, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_tR.grid(row= 1, column= 0, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_tF.grid(row= 1, column= 1, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_slewR.grid(row= 1, column= 2, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_slewF.grid(row= 1, column= 3, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_perper.grid(row= 1, column= 4, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_VIH.grid(row= 2, column= 0, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_VIL.grid(row= 2, column= 1, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_VPP.grid(row= 2, column= 2, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_Vmax.grid(row= 2, column= 3, padx= 5, pady= 5, sticky= 'nesw')
        self.button_measurement_Vmin.grid(row= 2, column= 4, padx= 5, pady= 5, sticky= 'nesw')
        
        self.label_delta_setting.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')

        self.radiobutton_double_channels.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw', columnspan= 2)
        checkbutton_modify_delta_name.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        combobox_modify_delta_name.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'ew')

        self.label_delta_start.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.label_delta_arrow.grid(row= 2, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.label_delta_stop.grid(row= 3, column= 0, padx= 2, pady= 2, sticky= 'nesw')

        self.label_delta_channel.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_delta_channel_start.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.label_delta_channel_arrow.grid(row= 2, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_delta_channel_stop.grid(row= 3, column= 1, padx= 2, pady= 2, sticky= 'nesw')
        self.button_deita_channel_switch.grid(row= 4, column= 1, padx= 5, pady= 5, sticky= 'nesw')

        self.label_delta_transition.grid(row= 0, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        combobox_delta_transition_start.grid(row= 1, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        self.label_delta_transition_arrow.grid(row= 2, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        combobox_delta_transition_stop.grid(row= 3, column= 2, padx= 2, pady= 2, sticky= 'nesw')
        self.button_deita_transition_switch.grid(row= 4, column= 2, padx= 5, pady= 5, sticky= 'nesw')

        self.label_delta_edge.grid(row= 0, column= 3, padx= 2, pady= 2, sticky= 'nesw')
        self.entry_delta_edge_start.grid(row= 1, column= 3, padx= 2, pady= 2, sticky= 'nesw')
        self.label_delta_edge_arrow.grid(row= 2, column= 3, padx= 2, pady= 2, sticky= 'nesw')
        self.entry_delta_edge_stop.grid(row= 3, column= 3, padx= 2, pady= 2, sticky= 'nesw')
        self.button_deita_edge_switch.grid(row= 4, column= 3, padx= 5, pady= 5, sticky= 'nesw')

        self.label_delta_position.grid(row= 0, column= 4, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_delta_position_start.grid(row= 1, column= 4, padx= 2, pady= 2, sticky= 'nesw')
        self.label_delta_position_arrow.grid(row= 2, column= 4, padx= 2, pady= 2, sticky= 'nesw')
        self.combobox_delta_position_stop.grid(row= 3, column= 4, padx= 2, pady= 2, sticky= 'nesw')
        self.button_deita_position_switch.grid(row= 4, column= 4, padx= 5, pady= 5, sticky= 'nesw')

        self.button_measurement_deltatime.grid(row= 0, column= 0, padx= 30, pady= 50, sticky= 'nesw')
            ###########################

        ## settings  ==============================================================================================================================================
        settings.apply('Channel', {
            'ChannelTypeChoice': self.intvar_measurement_channel, 
            'ChannelSingle': self.strvar_measurement_single_channel, 
        })
        settings.apply('Delta_Setup_Config', {
            'IsDeltaChannelName': self.boolvar_modify_delta_name, 
            'DeltaChannelName': self.strvar_modify_delta_name, 
            'DeltaStartChannel': self.strvar_delta_channel_start, 
            'DeltaStartEdge': self.strvar_delta_transition_start, 
            'DeltaStartNum': self.intvar_delta_edge_start, 
            'DeltaStartPosition': self.strvar_delta_position_start, 
            'DeltaStopChannel': self.strvar_delta_channel_stop, 
            'DeltaStopEdge': self.strvar_delta_transition_stop, 
            'DeltaStopNum': self.intvar_delta_edge_stop, 
            'DeltaStopPosition': self.strvar_delta_position_stop, 
        })
