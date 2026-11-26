import tkinter as tk
from tkinter import ttk

class LabelNameLabelFrame(tk.LabelFrame):
    def __init__(self, master, settings, mxr, colors, button_width, entry_width):
        super().__init__(master, text= 'Label/Bookmark', background= colors['labelframe'][0], fg= colors['labelframe'][1], font= ('Candara', 10, 'bold'),)

        self.frame_label_bookmark_top= tk.Frame(master= self, background= colors['labelframe'][0])
        self.frame_label_bookmark_base= tk.Frame(master= self, background= colors['labelframe'][0])
        
        self.intvar_label_type= tk.IntVar()
        self.radiobutton_label= ttk.Radiobutton(
            master= self.frame_label_bookmark_top, text= 'Label', value= 0, variable= self.intvar_label_type, style= 'radiobutton_3.TRadiobutton')
        self.radiobutton_bookmark= ttk.Radiobutton(
            master= self.frame_label_bookmark_top, text= 'Bookmark', value= 1, variable= self.intvar_label_type, style= 'radiobutton_3.TRadiobutton')
        self.button_label_channel_1_ckeck= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Channel 1', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.add_labelname(label_type= self.intvar_label_type.get(), channel= 1, content= self.strvar_label_channel_1.get())
            )
        self.strvar_label_channel_1= tk.StringVar()
        self.entry_label_channel_1= ttk.Entry(
            master= self.frame_label_bookmark_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_label_channel_1, justify= 'center')
        self.button_label_channel_1_delete= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Delete', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.delete_labelname(label_type= self.intvar_label_type.get(), channel= 1)
            )
        self.button_label_channel_2_ckeck= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Channel 2', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.add_labelname(label_type= self.intvar_label_type.get(), channel= 2, content= self.strvar_label_channel_2.get())
            )
        self.strvar_label_channel_2= tk.StringVar()
        self.entry_label_channel_2= ttk.Entry(
            master= self.frame_label_bookmark_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_label_channel_2, justify= 'center')
        self.button_label_channel_2_delete= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Delete', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.delete_labelname(label_type= self.intvar_label_type.get(), channel= 2)
            )
        self.button_label_channel_3_ckeck= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Channel 3', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.add_labelname(label_type= self.intvar_label_type.get(), channel= 3, content= self.strvar_label_channel_3.get())
            )
        self.strvar_label_channel_3= tk.StringVar()
        self.entry_label_channel_3= ttk.Entry(
            master= self.frame_label_bookmark_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_label_channel_3, justify= 'center')
        self.button_label_channel_3_delete= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Delete', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.delete_labelname(label_type= self.intvar_label_type.get(), channel= 3)
            )
        self.button_label_channel_4_ckeck= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Channel 4', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.add_labelname(label_type= self.intvar_label_type.get(), channel= 4, content= self.strvar_label_channel_4.get())
            )
        self.strvar_label_channel_4= tk.StringVar()
        self.entry_label_channel_4= ttk.Entry(
            master= self.frame_label_bookmark_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_label_channel_4, justify= 'center')
        self.button_label_channel_4_delete= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Delete', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.delete_labelname(label_type= self.intvar_label_type.get(), channel= 4)
            )
        self.button_label_wmemory_1_ckeck= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Wme 1', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.add_labelname(label_type= self.intvar_label_type.get(), channel= 5, content= self.strvar_label_wmemory_1.get())
            )
        self.strvar_label_wmemory_1= tk.StringVar()
        self.entry_label_wmemory_1= ttk.Entry(
            master= self.frame_label_bookmark_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_label_wmemory_1, justify= 'center')
        self.button_label_wmemory_1_delete= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Delete', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.delete_labelname(label_type= self.intvar_label_type.get(), channel= 5)
            )
        self.button_label_wmemory_2_ckeck= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Wme 2', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.add_labelname(label_type= self.intvar_label_type.get(), channel= 6, content= self.strvar_label_wmemory_2.get())
            )
        self.strvar_label_wmemory_2= tk.StringVar()
        self.entry_label_wmemory_2= ttk.Entry(
            master= self.frame_label_bookmark_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_label_wmemory_2, justify= 'center')
        self.button_label_wmemory_2_delete= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Delete', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.delete_labelname(label_type= self.intvar_label_type.get(), channel= 6)
            )
        self.button_label_wmemory_3_ckeck= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Wme 3', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.add_labelname(label_type= self.intvar_label_type.get(), channel= 7, content= self.strvar_label_wmemory_3.get())
            )
        self.strvar_label_wmemory_3= tk.StringVar()
        self.entry_label_wmemory_3= ttk.Entry(
            master= self.frame_label_bookmark_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_label_wmemory_3, justify= 'center')
        self.button_label_wmemory_3_delete= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Delete', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.delete_labelname(label_type= self.intvar_label_type.get(), channel= 7)
            )
        self.button_label_wmemory_4_ckeck= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Wme 4', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.add_labelname(label_type= self.intvar_label_type.get(), channel= 8, content= self.strvar_label_wmemory_4.get())
            )
        self.strvar_label_wmemory_4= tk.StringVar()
        self.entry_label_wmemory_4= ttk.Entry(
            master= self.frame_label_bookmark_base, width= max(10, int(entry_width*0.4)), textvariable= self.strvar_label_wmemory_4, justify= 'center')
        self.button_label_wmemory_4_delete= ttk.Button(
            master= self.frame_label_bookmark_base, text= 'Delete', width= button_width,  padding= 1,
            style= 'normal_height.TButton',
            command= lambda: mxr.delete_labelname(label_type= self.intvar_label_type.get(), channel= 8)
            )
        ################################################

        ### Weight        
        self.rowconfigure(0, weight= 1, uniform= 'row')
        self.rowconfigure(1, weight= 4, uniform= 'row')
        self.columnconfigure(0, weight= 1, uniform= 'col')

        self.frame_label_bookmark_top.rowconfigure(0, weight= 1, uniform= 'row')
        self.frame_label_bookmark_top.columnconfigure(0, weight= 1, uniform= 'col')
        self.frame_label_bookmark_top.columnconfigure(1, weight= 5, uniform= 'col')

        for i in range(4):
            self.frame_label_bookmark_base.rowconfigure(i, weight= 1, uniform= 'row')
        for j in range(6):
            if j%3 == 0:
                self.frame_label_bookmark_base.columnconfigure(j, weight= 2, uniform= 'col')
            elif j%3 == 1:
                self.frame_label_bookmark_base.columnconfigure(j, weight= 5, uniform= 'col')
            else:
                self.frame_label_bookmark_base.columnconfigure(j, weight= 1, uniform= 'col')
        ###########################

        ## Grid  ==============================================================================================================================================
        self.frame_label_bookmark_top.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.frame_label_bookmark_base.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')

        self.radiobutton_label.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
        self.radiobutton_bookmark.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'nesw')

        self.button_label_channel_1_ckeck.grid(row= 0, column= 0, padx= 5, pady= 5, sticky= 'ew')
        self.entry_label_channel_1.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.button_label_channel_1_delete.grid(row= 0, column= 2, padx= 5, pady= 5, sticky= 'ew')

        self.button_label_channel_2_ckeck.grid(row= 1, column= 0, padx= 5, pady= 5, sticky= 'ew')
        self.entry_label_channel_2.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.button_label_channel_2_delete.grid(row= 1, column= 2, padx= 5, pady= 5, sticky= 'ew')

        self.button_label_channel_3_ckeck.grid(row= 2, column= 0, padx= 5, pady= 5, sticky= 'ew')
        self.entry_label_channel_3.grid(row= 2, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.button_label_channel_3_delete.grid(row= 2, column= 2, padx= 5, pady= 5, sticky= 'ew')

        self.button_label_channel_4_ckeck.grid(row= 3, column= 0, padx= 5, pady= 5, sticky= 'ew')
        self.entry_label_channel_4.grid(row= 3, column= 1, padx= 2, pady= 2, sticky= 'ew')
        self.button_label_channel_4_delete.grid(row= 3, column= 2, padx= 5, pady= 5, sticky= 'ew')

        self.button_label_wmemory_1_ckeck.grid(row= 0, column= 3, padx= 5, pady= 5, sticky= 'ew')
        self.entry_label_wmemory_1.grid(row= 0, column= 4, padx= 2, pady= 2, sticky= 'ew')
        self.button_label_wmemory_1_delete.grid(row= 0, column= 5, padx= 5, pady= 5, sticky= 'ew')

        self.button_label_wmemory_2_ckeck.grid(row= 1, column= 3, padx= 5, pady= 5, sticky= 'ew')
        self.entry_label_wmemory_2.grid(row= 1, column= 4, padx= 2, pady= 2, sticky= 'ew')
        self.button_label_wmemory_2_delete.grid(row= 1, column= 5, padx= 5, pady= 5, sticky= 'ew')

        self.button_label_wmemory_3_ckeck.grid(row= 2, column= 3, padx= 5, pady= 5, sticky= 'ew')
        self.entry_label_wmemory_3.grid(row= 2, column= 4, padx= 2, pady= 2, sticky= 'ew')
        self.button_label_wmemory_3_delete.grid(row= 2, column= 5, padx= 5, pady= 5, sticky= 'ew')

        self.button_label_wmemory_4_ckeck.grid(row= 3, column= 3, padx= 5, pady= 5, sticky= 'ew')
        self.entry_label_wmemory_4.grid(row= 3, column= 4, padx= 2, pady= 2, sticky= 'ew')
        self.button_label_wmemory_4_delete.grid(row= 3, column= 5, padx= 5, pady= 5, sticky= 'ew')
        ###########################

        ## settings  ==============================================================================================================================================
        settings.apply('Label_Setup_Config', {
            'LabelTypeChoice': self.intvar_label_type, 
            'ChannelLabel_1': self.strvar_label_channel_1, 
            'ChannelLabel_2': self.strvar_label_channel_2, 
            'ChannelLabel_3': self.strvar_label_channel_3, 
            'ChannelLabel_4': self.strvar_label_channel_4, 
            'WmemoryLabel_1': self.strvar_label_wmemory_1, 
            'WmemoryLabel_2': self.strvar_label_wmemory_2, 
            'WmemoryLabel_3': self.strvar_label_wmemory_3, 
            'WmemoryLabel_4': self.strvar_label_wmemory_4, 
        })
        ###########################

        ## return  ==============================================================================================================================================
    def get_value(self):
        content= [
            self.strvar_label_channel_1.get(), 
            self.strvar_label_channel_2.get(), 
            self.strvar_label_channel_3.get(), 
            self.strvar_label_channel_4.get(), 
            self.strvar_label_wmemory_1.get(), 
            self.strvar_label_wmemory_2.get(), 
            self.strvar_label_wmemory_3.get(), 
            self.strvar_label_wmemory_4.get(), 
        ]
        return [self.intvar_label_type.get(), content]