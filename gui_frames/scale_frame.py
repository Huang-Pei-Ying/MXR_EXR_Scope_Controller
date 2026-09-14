import tkinter as tk
from tkinter import ttk




# Scale/Offset/Trigger  ===================================================================================================================================
labelframe_scale_offset_trigger= tk.LabelFrame(master= frame_left, text= 'Scale/Offset/Trigger', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)


frame_scalearea_top= tk.Frame(master= labelframe_scale_offset_trigger, background= colors['labelframe'][0])
# voltage_scale
button_voltage_scale = ttk.Button(
    master= frame_scalearea_top, text= 'Voltage Scale (V)', width= button_width_scale_area,  padding= 1, 
    style= 'normal_height.TButton',
    # command= lambda: mxr.
    )

strvar_voltage_scale= tk.StringVar()
combobox_voltage_scale = ttk.Combobox(
    frame_scalearea_top, width= max(10, int(entry_width_scale_area*0.4)), textvariable= strvar_voltage_scale, style= 'TCombobox', justify= 'center')
execute_commbobox_function(combobox= combobox_voltage_scale, combobox_var= strvar_voltage_scale, ini_dict_key= 'VoltScale', ini_option_section= 'Scale_Offset_Config', ini_option_key= 'VoltScale', ini_selected_section= 'Scale_Offset_Selected_Values')

# voltage_offset
button_voltage_offset = ttk.Button(
    master= frame_scalearea_top, text= 'Voltage Offset (V)', width= button_width_scale_area,  padding= 1,
    # style= 'normal_height.TButton',
    # command= lambda: mxr.
    )

strvar_voltage_offset= tk.StringVar()
combobox_voltage_offset = ttk.Combobox(
    frame_scalearea_top, width= max(10, int(entry_width_scale_area*0.4)), textvariable= strvar_voltage_offset, style= 'TCombobox', justify= 'center')
execute_commbobox_function(combobox= combobox_voltage_offset, combobox_var= strvar_voltage_offset, ini_dict_key= 'VoltOffset', ini_option_section= 'Scale_Offset_Config', ini_option_key= 'VoltOffset', ini_selected_section= 'Scale_Offset_Selected_Values')

# timebase scale
button_timebase_scale = ttk.Button(
    master= frame_scalearea_top, text= 'Timebase Scale (sec)', width= button_width_scale_area, padding= 1,
    # style= 'normal_height.TButton',
    # command= lambda: mxr.
    )

strvar_timebase_scale= tk.StringVar()
entry_timebase_scale = ttk.Entry(master= frame_scalearea_top, width= max(10, int(entry_width_scale_area*0.4)), textvariable= strvar_timebase_scale, style= 'TEntry', justify= 'center')

# timebase offset
button_timebase_offset= ttk.Button(
    master= frame_scalearea_top, text= 'Timebase Offset (sec)', width= button_width_scale_area, padding= 1, 
    # style= 'normal_height.TButton',
    # command= lambda: mxr.
    )

strvar_timebase_offset= tk.StringVar()
entry_timebase_offset = ttk.Entry(master= frame_scalearea_top, width= max(10, int(entry_width_scale_area*0.4)), textvariable= strvar_timebase_offset, style= 'TEntry', justify= 'center')

# trigger channel
button_trigger_channel = ttk.Button(
    master= frame_scalearea_top, text= 'Trigger Channel', width= button_width_scale_area, padding= 1,
    # style= 'normal_height.TButton',
    # command= lambda: mxr.
    )

strvar_trigger_channel= tk.StringVar()
combobox_trigger_channel = ttk.Combobox(
    frame_scalearea_top, width= max(10, int(entry_width_scale_area*0.4)), textvariable= strvar_trigger_channel, style= 'TCombobox', justify= 'center', values= ['1', '2', '3', '4'])

# trigger level
button_trigger_level = ttk.Button(
    master= frame_scalearea_top, text= 'Trigger Level (V)', width= button_width_scale_area, padding= 1, 
    # style= 'normal_height.TButton', 
    # command= lambda: mxr.
    )

strvar_trigger_level= tk.StringVar()
combobox_trigger_level = ttk.Combobox(
    frame_scalearea_top, width= max(10, int(entry_width_scale_area*0.4)), textvariable= strvar_trigger_level, style= 'TCombobox', justify= 'center')
execute_commbobox_function(combobox= combobox_trigger_level, combobox_var= strvar_trigger_level, ini_dict_key= 'TriggerLevel', ini_option_section= 'Scale_Offset_Config', ini_option_key= 'TriggerLevel', ini_selected_section= 'Scale_Offset_Selected_Values')

frame_scalearea_bottom= tk.Frame(master= labelframe_scale_offset_trigger, background= colors['labelframe'][0])
# buttons
button_trigger_mode = ttk.Button(
    master= frame_scalearea_bottom, text= 'Trigger Mode', width= button_width_scale_area, padding= 2, 
    # style= 'double_height.TButton', 
    # command= lambda: mxr.
    )
button_trigger_slope = ttk.Button(
    master= frame_scalearea_bottom, text= 'Trigger Slope', width= button_width_scale_area, padding= 2, 
    # style= 'double_height.TButton', 
    # command= lambda: mxr.
    )
button_set_all = ttk.Button(
    master= frame_scalearea_bottom, text= 'All Set', width= button_width_scale_area, padding= 2, 
    # style= 'special.TButton', 
    # command= lambda: mxr.
    )

################################################

### scale/offset/trigger
labelframe_scale_offset_trigger.rowconfigure(0, weight= 3, uniform= 'row')
labelframe_scale_offset_trigger.rowconfigure(1, weight= 1, uniform= 'row')
labelframe_scale_offset_trigger.columnconfigure(0, weight= 1, uniform= 'col')

for i in range(4):
    frame_scalearea_top.rowconfigure(i, weight= 1, uniform= 'row')
for j in range(4):
    if j % 2 == 0:
        frame_scalearea_top.columnconfigure(j, weight= 2, uniform= 'col')
    else:
        frame_scalearea_top.columnconfigure(j, weight= 1, uniform= 'col')

frame_scalearea_bottom.rowconfigure(0, weight= 1, uniform= 'row')
frame_scalearea_bottom.columnconfigure(0, weight= 1, uniform= 'col')
frame_scalearea_bottom.columnconfigure(1, weight= 1, uniform= 'col')
frame_scalearea_bottom.columnconfigure(2, weight= 1, uniform= 'col')
###########################

labelframe_scale_offset_trigger.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')

## Scale/Offset/Trigger  ==============================================================================================================================================
frame_scalearea_top.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
frame_scalearea_bottom.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
### top area
button_voltage_scale.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'ew')
combobox_voltage_scale.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'ew')
button_timebase_scale.grid(row= 0, column= 2, padx= 2, pady= 2, sticky= 'ew')
entry_timebase_scale.grid(row= 0, column= 3, padx= 2, pady= 2, sticky= 'ew')
button_voltage_offset.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'ew')
combobox_voltage_offset.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'ew')
button_timebase_offset.grid(row= 1, column= 2, padx= 2, pady= 2, sticky= 'ew')
entry_timebase_offset.grid(row= 1, column= 3, padx= 2, pady= 2, sticky= 'ew')
button_trigger_channel.grid(row= 2, column= 0, padx= 2, pady= 2, sticky= 'ew')
combobox_trigger_channel.grid(row= 2, column= 1, padx= 2, pady= 2, sticky= 'ew')
button_trigger_level.grid(row= 3, column= 0, padx= 2, pady= 2, sticky= 'ew')
combobox_trigger_level.grid(row= 3, column= 1, padx= 2, pady= 2, sticky= 'ew')
### bottom area
button_trigger_mode.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'w')
button_trigger_slope.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'w')
button_set_all.grid(row= 0, column= 2, padx= 2, pady= 2, sticky= 'w')
###########################
