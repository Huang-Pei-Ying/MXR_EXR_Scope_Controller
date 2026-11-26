import tkinter as tk
from tkinter import ttk
import utils

class AcquisitionLabelFrame(tk.LabelFrame):
    def __init__(self, master, settings, mxr, colors, button_width, entry_width):
        super().__init__(master, text= 'Acquisition', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)

        # sampling rate
        self.button_smapling_rate = ttk.Button(
            master= self, text= 'Sampling Rate (Sa/s)', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.acquire_sampling_rate(sampling_rate= self.strvar_smapling_rate.get())
            )

        self.strvar_smapling_rate= tk.StringVar()
        self.combobox_smapling_rate = ttk.Combobox(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_smapling_rate, style= 'TCombobox', justify= 'center', 
            values= ['16E+9', '8E+9', '4E+9', '2E+9']
            )
        self.button_smapling_rate_auto = ttk.Button(
            master= self, text= 'Auto Mode', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.acquire_sampling_rate(rate= 'AUTO')
            )
        # memory depth
        self.button_memory_depth = ttk.Button(
            master= self, text= 'Memory Depth (pts)', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.acquire_memory_depth(points_value= self.strvar_memory_depth.get())
            )
        self.strvar_memory_depth= tk.StringVar()
        self.entry_memory_depth = ttk.Entry(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_memory_depth, justify= 'center')
        self.button_memory_depth_auto = ttk.Button(
            master= self, text= 'Auto Mode', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.acquire_memory_depth(points_value= 'AUTO')
            )
        # waveform intensity
        self.button_waveform_intensity = ttk.Button(
            master= self, text= 'Waveform Intensity (%)', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.check_intensity_setting(intensity_value= self.strvar_waveform_intensity.get())
            )
        self.strvar_waveform_intensity= tk.StringVar()
        self.entry_waveform_intensity = ttk.Entry(
            master= self, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_waveform_intensity, justify= 'center')
        vcmd = (self.register(lambda new_value: utils.validate_number(new_value, self.entry_waveform_intensity)),"%P")
        self.entry_waveform_intensity.config(validate= "key", validatecommand= vcmd)

        self.button_set_to_fixty = ttk.Button(
            master= self, text= 'Set 50%', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: utils.set_to_fixty(entry= self.entry_waveform_intensity)
            )
        self.entry_waveform_intensity.bind("<MouseWheel>", lambda event: utils.on_mouse_wheel(event, self.entry_waveform_intensity))
        self.entry_waveform_intensity.bind("<Button-4>", lambda event: utils.change_intensity_by(entry= self.entry_waveform_intensity, step= 1)) 
        self.entry_waveform_intensity.bind("<Button-5>", lambda event: utils.change_intensity_by(entry= self.entry_waveform_intensity, step= -1))

        ################################################

        ### Weight        
        self.rowconfigure(0, weight= 1, uniform= 'row')
        self.rowconfigure(1, weight= 1, uniform= 'row')
        self.rowconfigure(2, weight= 1, uniform= 'row')
        self.columnconfigure(0, weight= 4, uniform= 'col')
        self.columnconfigure(1, weight= 2, uniform= 'col')
        self.columnconfigure(2, weight= 3, uniform= 'col')
        ###########################

        ## Grid  ==============================================================================================================================================
        self.button_smapling_rate.grid(row= 0, column= 0, padx= 10, pady= 5, sticky= 'nesw')
        self.combobox_smapling_rate.grid(row= 0, column= 1, padx= 2, pady= 5, sticky= 'nesw')
        self.button_smapling_rate_auto.grid(row= 0, column= 2, padx= 10, pady= 5, sticky= 'nesw')

        self.button_memory_depth.grid(row= 1, column= 0, padx= 10, pady= 5, sticky= 'nesw')
        self.entry_memory_depth.grid(row= 1, column= 1, padx= 2, pady= 5, sticky= 'nesw')
        self.button_memory_depth_auto.grid(row= 1, column= 2, padx= 10, pady= 5, sticky= 'nesw')
        
        self.button_waveform_intensity.grid(row= 2, column= 0, padx= 10, pady= 5, sticky= 'nesw')
        self.entry_waveform_intensity.grid(row= 2, column= 1, padx= 2, pady= 5, sticky= 'nesw')
        self.button_set_to_fixty.grid(row= 2, column= 2, padx= 10, pady= 5, sticky= 'nesw')
        ###########################

        ## settings  ==============================================================================================================================================
        settings.apply('Acquisition', {
            'SamplingRate': self.strvar_smapling_rate, 
            'MemoryDepth': self.strvar_memory_depth, 
            'WfmIntensity': self.strvar_waveform_intensity, 
        })
        utils.update_intensity_color(value= self.strvar_waveform_intensity.get(), entry= self.entry_waveform_intensity)
