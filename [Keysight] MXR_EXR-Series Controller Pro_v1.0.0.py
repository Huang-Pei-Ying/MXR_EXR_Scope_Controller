import pyvisa
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog, ttk
import configparser
import os
import re
import time
import sys
import numpy as np
from PIL import Image
import random
import string
import ctypes
from tkinter import font
from pathlib import Path

from ini_setting import Settings
from gui_frames import ScaleLabelFrame, ThresholdLabelFrame, ChannelLabelFrame, ControlLabelFrame, AcquisitionLabelFrame, MeasurementLabelFrame, MarkerLabelFrame, LabelNameLabelFrame, SaveImageLabelFrame, SaveOthersLabelFrame, LoadWmemoryLabelFrame, LoadSetupLabelFrame
from scope_functions import MXR


window_name= '[Keysight] MXR/EXR-Series Controller Pro_v1.0.0'

def enable_dpi_awareness_windows():
    """Try to enable DPI awareness on Windows. Call BEFORE creating Tk()."""
    if sys.platform != "win32":
        return False
    try:
        user32 = ctypes.windll.user32
        if hasattr(user32, "SetProcessDpiAwarenessContext"):
            user32.SetProcessDpiAwarenessContext(ctypes.c_void_p(-4))
            return True
    except Exception:
        pass
    try:
        shcore = ctypes.windll.shcore
        shcore.SetProcessDpiAwareness(2)  # PROCESS_PER_MONITOR_DPI_AWARE
        return True
    except Exception:
        pass
    try:
        ctypes.windll.user32.SetProcessDPIAware()
        return True
    except Exception:
        pass
    return False

# DEVMODE for EnumDisplaySettings
class DEVMODEW(ctypes.Structure):
    _fields_ = [
        ("dmDeviceName", ctypes.c_wchar * 32),
        ("dmSpecVersion", ctypes.c_ushort),
        ("dmDriverVersion", ctypes.c_ushort),
        ("dmSize", ctypes.c_ushort),
        ("dmDriverExtra", ctypes.c_ushort),
        ("dmFields", ctypes.c_uint),
        ("dmOrientation", ctypes.c_short),
        ("dmPaperSize", ctypes.c_short),
        ("dmPaperLength", ctypes.c_short),
        ("dmPaperWidth", ctypes.c_short),
        ("dmScale", ctypes.c_short),
        ("dmCopies", ctypes.c_short),
        ("dmDefaultSource", ctypes.c_short),
        ("dmPrintQuality", ctypes.c_short),
        ("dmColor", ctypes.c_short),
        ("dmDuplex", ctypes.c_short),
        ("dmYResolution", ctypes.c_short),
        ("dmTTOption", ctypes.c_short),
        ("dmCollate", ctypes.c_short),
        ("dmFormName", ctypes.c_wchar * 32),
        ("dmLogPixels", ctypes.c_ushort),
        ("dmBitsPerPel", ctypes.c_uint),
        ("dmPelsWidth", ctypes.c_uint),
        ("dmPelsHeight", ctypes.c_uint),
        ("dmDisplayFlags", ctypes.c_uint),
        ("dmDisplayFrequency", ctypes.c_uint),
        ("dmICMMethod", ctypes.c_uint),
        ("dmICMIntent", ctypes.c_uint),
        ("dmMediaType", ctypes.c_uint),
        ("dmDitherType", ctypes.c_uint),
        ("dmReserved1", ctypes.c_uint),
        ("dmReserved2", ctypes.c_uint),
        ("dmPanningWidth", ctypes.c_uint),
        ("dmPanningHeight", ctypes.c_uint),
    ]

def get_primary_physical_resolution_enumdisplay():
    """Return (width, height) of primary display using EnumDisplaySettings (fallback to GetSystemMetrics)."""
    try:
        user32 = ctypes.windll.user32
        enum = user32.EnumDisplaySettingsW
        enum.argtypes = [ctypes.c_wchar_p, ctypes.c_uint, ctypes.POINTER(DEVMODEW)]
        ENUM_CURRENT_SETTINGS = -1
        dm = DEVMODEW()
        dm.dmSize = ctypes.sizeof(DEVMODEW)
        ok = enum(None, ENUM_CURRENT_SETTINGS, ctypes.byref(dm))
        if ok:
            return int(dm.dmPelsWidth), int(dm.dmPelsHeight)
    except Exception:
        pass
    try:
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    except Exception:
        return (800, 600)

# ---------- reference list & helper ----------
REFERENCE_RESO = [
    (2560, 1600),  # primary requested reference
    (1920, 1200),
    (1920, 1080),
    (1366, 768),
    (3840, 2160),
    (1280, 800),
]

def pick_reference_by_aspect(mw, mh, refs=REFERENCE_RESO):
    target_ar = mw / mh
    best = None
    best_diff = 1e9
    for (rw, rh) in refs:
        ar = rw / rh
        diff = abs(ar - target_ar)
        if diff < best_diff:
            best_diff = diff
            best = (rw, rh)
    return best


def choose_available_font(root, preferred_list, fallback="TkDefaultFont"):
    avail = set(font.families(root))
    for fam in preferred_list:
        if fam in avail:
            return fam
    return fallback

# 第一個視窗取得scope id並開啟主視窗
def show_main_window(old_scope_ips):
    # 取得scope id
    selected_value = str_scope_ip.get()

    # 新增scope id
    if selected_value and selected_value not in old_scope_ips:
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read(os.path.join(os.path.dirname(__file__), 'InitConfig_setup_new.ini'), encoding='utf-8',)
        config.set('Scope_IPs', f'IP_{len(old_scope_ips)-1}', selected_value)

        # 寫回ini
        with open(os.path.join(os.path.dirname(__file__), 'InitConfig_setup_new.ini'), 'w') as configfile:
            config.write(configfile)
        
    # 關閉第一個視窗
    id_window.destroy()
    
    # 創建主視窗
    main_window(scope_ip= selected_value)
    

# =====================================================================================================================================================
def main_window(scope_ip):

    def clear(string):
        string.set('')

    def close_window():
        if messagebox.askyesno('Message', 'Exit?'):
            settings.save()
            window.destroy()
            sys.exit()

    class ToolTip:
        def __init__(self, widget, text):
            self.widget = widget
            self.text = text
            self.tip_window = None
            self.widget.bind("<Enter>", self.show_tip)
            self.widget.bind("<Leave>", self.hide_tip)

        def show_tip(self, event= None):
            "Display text in tooltip window"
            if self.tip_window or not self.text:
                return
            x, y, cx, cy = self.widget.bbox("insert")
            if not x == None:
                x += self.widget.winfo_rootx() + 57
                y += self.widget.winfo_rooty() + 21
                self.tip_window = tw = tk.Toplevel(self.widget)
                tw.wm_overrideredirect(True)
                tw.wm_geometry("+%d+%d" % (x, y))
                label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                                background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                                font=("tahoma", "8", "normal"))
                label.pack(ipadx=1)
            else:
                return

        def hide_tip(self, event=None):
            if self.tip_window:
                self.tip_window.destroy()
                self.tip_window = None


    # 整個程式只讀取一次 INI
    settings = Settings(f"{os.path.join(os.path.dirname(__file__), 'InitConfig_setup_new.ini')}")

    # Get physical resolution (prefer EnumDisplaySettings)
    if sys.platform == "win32":
        phys_w, phys_h = get_primary_physical_resolution_enumdisplay()
    else:
        # non-windows: fallback to tkinter reported screen size later
        phys_w, phys_h = None, None
    print("physical resolution (fallback) ->", phys_w, phys_h)


    window = tk.Tk()
    window.title(window_name)

    # If physical resolution not available (non-windows), use Tk reported screen
    # 取得螢幕解析度（像素）
    tk_screen_w = window.winfo_screenwidth()
    tk_screen_h = window.winfo_screenheight()
    print("Tk reported screen ->", tk_screen_w, tk_screen_h)

    if not phys_w or not phys_h:
        screen_w, screen_h = tk_screen_w, tk_screen_h
    else:
        screen_w, screen_h = phys_w, phys_h

    # pick reference by aspect and compute scale (resolution-primary)
    ref_w, ref_h = pick_reference_by_aspect(screen_w, screen_h)
    res_scale = min(screen_w / ref_w, screen_h / ref_h)
    if res_scale <= 0:
        res_scale = 1.0

    print("selected ref:", (ref_w, ref_h), "res_scale:", round(res_scale, 3))

    
    # 設定style ========================================================================================================================================================================
    style = ttk.Style(window)
    # style.theme_use('alt')

    # 顏色表 (name -> (bg, fg, select))
    colors = {
        'window': ('#084F6A', '#000000', '#000000'), 
        'labelframe': ("#011E25", '#9DB5B2', '#000000'), 
        'label': ('#011E25', '#DAF0EE', '#000000'), 
        'button': ('#8CC6D0', '#0B3041', '#000000'), 
        'special_button': ('#61CBF4', '#FFFFFF', '#000000'), 
        'entry': ('#EAF4F6', '#0B3041', '#000000'), 
        'combobox': ('#F2F2F2', '#0B3041', '#000000'), 
        'radiobutton_1': ('#011E25', '#F6C6AD', '#8CC6D0'),  # 淺橘
        'radiobutton_2': ('#011E25', '#F2CFEE', '#8CC6D0'),  # 淺粉
        'radiobutton_3': ('#011E25', '#E59EDD', '#8CC6D0'),  # 桃紅
        'checkbutton_1': ('#011E25', '#FFFFB3', '#EAF4F6'),  # 黃
        'checkbutton_2': ('#011E25', '#83CBEB', '#EAF4F6')   # 藍
    }

    base_font_size= 10
    
    # 設定label style
    label_style= {
        'calibri_bold': ('Calibri', 'bold'), 
        'calibri_normal': ('Candara', 'normal'), 
        'candara_bold': ('Calibri', 'bold'), 
        'candara_normal': ('Candara', 'normal'), 
    }
    for name, (font_name, weight) in label_style.items():
        ui_label_font= font.Font(root= window, family= font_name, size= max(8, int(round(base_font_size * res_scale))), weight= weight)
        style_name = f"label_{name}.TLabel"
        # configure the style; some themes ignore background for TLabel
        style.configure(style_name, background= colors['label'][0], foreground= colors['label'][1], font= ui_label_font, padding= 1)

    # 設定button style
    ui_button_font= font.Font(root= window, family= f'Calibri', size= max(8, int(round(base_font_size * res_scale))))
    style.configure('normal_height.TButton', background= colors['button'][0], foreground= colors['button'][1], font= ui_button_font, padding= 1)
    style.map('normal_height.TButton', background=[('active',colors['button'][0])])
    style.configure('double_height.TButton', background= colors['button'][0], foreground= colors['button'][1], font= ui_button_font, padding= 2)
    style.configure('special.TButton', background= colors['special_button'][0], foreground= colors['special_button'][1], font= ui_button_font, padding= 2)

    # 設定entry style
    ui_entry_font= font.Font(root= window, family= f'Calibri', size= max(10, int(round((base_font_size-1) * res_scale))))
    style.configure('TEntry', background= colors['entry'][0], foreground= colors['entry'][1], font= ui_entry_font, padding= 1)

    # 設定combobox style
    ui_combobox_font= font.Font(root= window, family= f'Calibri', size= max(10, int(round((base_font_size-1) * res_scale))))
    style.configure('TCombobox', background= colors['combobox'][0], foreground= colors['combobox'][1], font= ui_combobox_font, padding= 1)

    # 設定radiobutton style
    ui_radiobutton_font= font.Font(root= window, family= f'Calibri', size= max(8, int(round(base_font_size * res_scale))))
    for i in range(1, 4):
        style.configure(f'radiobutton_{i}.TRadiobutton', background= colors[f'radiobutton_{i}'][0], foreground= colors[f'radiobutton_{i}'][1], font= ui_radiobutton_font, padding= 1)

    # 設定checkbutton style
    ui_checkbutton_font= font.Font(root= window, family= f'Calibri', size= max(8, int(round(base_font_size * res_scale))))
    for i in range(1, 3):
        style.configure(f'checkbutton_{i}.TCheckbutton', background= colors[f'checkbutton_{i}'][0], foreground= colors[f'checkbutton_{i}'][1], font= ui_checkbutton_font, padding= 1)


    # 設定按鈕大小, 初始按鈕尺寸以 dpi_scale 調整（width/height 為字元/行數）
    def set_button_size(base_btn_w, base_btn_h):
        btn_w = max(4, int(round(base_btn_w * res_scale)))
        btn_h = max(1, int(round(base_btn_h * res_scale)))

        return btn_w, btn_h
    
    def set_entry_width(base_entry_width):
        entry_w = max(10, int(round(base_entry_width * res_scale)))
        return entry_w
    
    # =============================================================================================================================================================================

    # initial window size (occupy a ratio of monitor)
    win_w = int(screen_w * 0.9)
    win_h = int(screen_h * 0.7)
    window.geometry(f"{win_w}x{win_h}")
    window.minsize(360, 240)

    # # window.geometry('1500x760+2+2')
    window.geometry('+2+2')
    window.configure(bg= colors['window'][0])
    # window.resizable(True, True)

    window.rowconfigure(0 , weight= 1, uniform= 'row')
    window.columnconfigure(0 , weight= 2, uniform= 'col')
    window.columnconfigure(1 , weight= 5, uniform= 'col')

    frame_left= tk.Frame(master= window, background= colors['window'][0])
    frame_right= tk.Frame(master= window, background= colors['window'][0])

    frame_left.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    frame_right.grid(row= 0, column= 1, padx= 2, pady= 2, sticky= 'nesw')

    # Left Area  ==============================================================================================================================================
    
    # Scale/Offset/Trigger  ===================================================================================================================================
    entry_width_scale_area= set_entry_width(base_entry_width= 20)
    button_width_scale_area, button_height_scale_area= set_button_size(base_btn_w= 20, base_btn_h= 1)

    scale_frame = ScaleLabelFrame(master= frame_left, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)
    threshold_frame = ThresholdLabelFrame(master= frame_left, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)
    channel_frame = ChannelLabelFrame(master= frame_left, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)
    control_frame = ControlLabelFrame(master= frame_left, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)
    acquisition_frame = AcquisitionLabelFrame(master= frame_left, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)

    # Right Area  ==============================================================================================================================================
    frame_right_top= tk.Frame(master= frame_right, background= colors['window'][0])
    frame_right_bottom_left= tk.Frame(master= frame_right, background= colors['window'][0])
    frame_right_bottom_right= tk.Frame(master= frame_right, background= colors['window'][0])

    measurement_frame= MeasurementLabelFrame(master= frame_right_top, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)
    marker_frame= MarkerLabelFrame(master= frame_right_bottom_left, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)
    labelname_frame= LabelNameLabelFrame(master= frame_right_bottom_left, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)
    saveimage_frame= SaveImageLabelFrame(master= frame_right_bottom_left, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)
    saveothers_frame= SaveOthersLabelFrame(master= frame_right_bottom_right, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)
    loadwmemory_frame= LoadWmemoryLabelFrame(master= frame_right_bottom_right, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)
    loadsetup_frame= LoadSetupLabelFrame(master= frame_right_bottom_right, settings= settings, colors= colors, button_width= button_width_scale_area, entry_width= entry_width_scale_area)

    ################################################
    # Weight  ==============================================================================================================================================
    frame_left.rowconfigure(0, weight= 4, uniform= 'row')  # scale/offset/trigger
    frame_left.rowconfigure(1, weight= 4, uniform= 'row')  # threshold
    frame_left.rowconfigure(2, weight= 2, uniform= 'row')  # channel
    frame_left.rowconfigure(3, weight= 2, uniform= 'row')  # control
    frame_left.rowconfigure(4, weight= 2, uniform= 'row')  # acquisition

    frame_left.columnconfigure(0, weight= 1, uniform= 'col')

    frame_right.rowconfigure(0, weight= 2, uniform= 'row')  # right top
    frame_right.rowconfigure(1, weight= 3, uniform= 'row')  # right bottom

    frame_right.columnconfigure(0, weight= 1, uniform= 'col')  # right bottom left
    frame_right.columnconfigure(1, weight= 1, uniform= 'col')  # right bottom right

    frame_right_top.rowconfigure(0, weight= 1, uniform= 'row')  # measurement
    frame_right_top.columnconfigure(0, weight= 1, uniform= 'col')

    frame_right_bottom_left.rowconfigure(0, weight= 2, uniform= 'row')  # marker
    frame_right_bottom_left.rowconfigure(1, weight= 2, uniform= 'row')  # label/bookmark
    frame_right_bottom_left.rowconfigure(2, weight= 1, uniform= 'row')  # save image
    frame_right_bottom_left.columnconfigure(0, weight= 1, uniform= 'col')

    frame_right_bottom_right.rowconfigure(0, weight= 2, uniform= 'row')  # save others
    frame_right_bottom_right.rowconfigure(1, weight= 2, uniform= 'row')  # load waveform
    frame_right_bottom_right.rowconfigure(2, weight= 3, uniform= 'row')  # load setup
    frame_right_bottom_right.columnconfigure(0, weight= 1, uniform= 'col')
    ###########################
    
    # Grid  ==============================================================================================================================================
    scale_frame.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    threshold_frame.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    channel_frame.grid(row= 2, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    control_frame.grid(row= 3, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    acquisition_frame.grid(row= 4, column= 0, padx= 2, pady= 2, sticky= 'nesw')

    frame_right_top.grid(row= 0, column= 0, padx= 2, pady= 2, columnspan= 2, sticky= 'nesw')
    frame_right_bottom_left.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    frame_right_bottom_right.grid(row= 1, column= 1, padx= 2, pady= 2, sticky= 'nesw')

    measurement_frame.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    
    marker_frame.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    labelname_frame.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    saveimage_frame.grid(row= 2, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    
    saveothers_frame.grid(row= 0, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    loadwmemory_frame.grid(row= 1, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    loadsetup_frame.grid(row= 2, column= 0, padx= 2, pady= 2, sticky= 'nesw')
    ###########################






    # ToolTip(combobox_voltage_scale, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(combobox_voltage_offset, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(combobox_trigger_level, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(button_waveform_intensity, '可用滑鼠滾輪調整數字大小')
    # ToolTip(combobox_start_risefall, '嗚啦!')
    # ToolTip(combobox_start_N, '呀哈!')
    # ToolTip(combobox_stop_risefall, '噗嚕!')
    # ToolTip(combobox_general_percent_top, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(combobox_general_percent_middle, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(combobox_general_percent_base, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(combobox_general_value_top, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(combobox_general_value_middle, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(combobox_general_value_base, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(combobox_risefall_percent_top, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(combobox_risefall_percent_base, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(combobox_risefall_value_top, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(combobox_risefall_value_base, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    # ToolTip(entry_label_4, '133 221 333 123 111')
    # ToolTip(entry_label_6, '電倉鼠!')
    # ToolTip(button_autoscale, '好的不得了')
    # ToolTip(button_clear_display, '嗚嚕嗚啦')
    # ToolTip(button_default, '6666')
    # ToolTip(checkbutton_marker_2, '防塵套不要亂丟')
    # ToolTip(checkbutton_marker_9, '花椒串')
    # ToolTip(combobox_channel_single, '累')
    # ToolTip(combobox_channel_delta_start, '隨波逐流的')
    # ToolTip(combobox_channel_delta_stop, '人生')
    # # ToolTip(e_image_folder, '自己打字，按按鈕會幫你新增資料夾')
    # ToolTip(entry_image, '嗚哩哩')
    # ToolTip(entry_image_pc_folder, '可以直接存電腦啦~')
    # ToolTip(entry_wmemory_folder, '自己打字，按按鈕會幫你新增資料夾')
    # ToolTip(entry_other_file, 'Channel要選對欸')
    # ToolTip(entry_wmemory_pc_folder, '示波器有沒有先存檔ㄏㄚˋ')
    # ToolTip(entry_wmemory_2, '呀哈呀哈')
    # ToolTip(entry_wmemory_4, '噗嚕!')

    # ToolTip(text_result_mean_3, '取小數點後三位')
    # ToolTip(text_result_minmax_7, '無條件捨去')
    # ToolTip(text_result_minmax_9, '芭樂綠茶')
    # ToolTip(text_result_mean_12, '多多檢查')
    

    # button_load_setup_standard_load = ttk.Button(
    #     master= frame_load_setup_4, text= 'Load', width= button_width_scale_area,  padding= 1, 
    #     # command= lambda: mxr.load_setup(
    #     #     folder= strvar_wmemory_folder.get(), 
    #     #     setup_name= strvar_setup.get(), 
    #     #     scope_segment= segment_list[0],
    #     # # time_scale= str_time_scale.get(), time_position= str_time_offset.get(), 
    #     #     choose_type= intvar_label_type.get(), 
    #     #     file_path_choice = intvar_wmemory_path_choice.get(), 
    #     # # volt_scale= str_volt_scale.get(), volt_offset= str_volt_offset.get(), 
    #     # # trig_chan= str_trigger_chan.get(), trig_level= str_trigger_level.get(),
    #     #     g_top= combobox_general_value_top.get(), g_middle= combobox_general_value_middle.get(), g_base= combobox_general_value_base.get(), 
    #     #     g_top_percent= combobox_general_percent_top.get(), g_middle_percent= combobox_general_percent_middle.get(), g_base_percent= combobox_general_percent_base.get(), 
    #     #     rf_top= combobox_risefall_value_top.get(),  rf_base= combobox_risefall_value_base.get(), 
    #     #     rf_top_percent= combobox_risefall_percent_top.get(), rf_base_percent= combobox_risefall_percent_base.get()
    #     #     )
    #     )
    # button_load_setup_standard_load.grid(row= 0, column= 3, padx= 5, pady= 2, sticky= 'ew')
    
    # # cbb_setupfile_interface.config(values= setupfile_interface_list)
    # combobox_load_setup_standard_interface.bind("<<ComboboxSelected>>", lambda e: select_load_setup_standard_interface(e, pc_segment= disk_segment))
    # combobox_load_setup_standard_subfolder.bind("<<ComboboxSelected>>", lambda e: select_load_setup_standard_subfolder(e, pc_segment= disk_segment))

    window.protocol('WM_DELETE_WINDOW', close_window)

    # mxr= MXR(scope_ip= scope_ip)

    try:
        scope = MXR(scope_ip= scope_ip)
    except ConnectionError as e:
        messagebox.showerror('Error', str(e), parent= window)
        close_window()
    else:
        # 連線成功後執行主程式的其他工作    
        window.mainloop()

# 選擇 Scope IP ============================================================================================================================================

config_initial = configparser.ConfigParser()
config_initial.optionxform = str
config_initial.read(os.path.join(os.path.dirname(__file__), 'InitConfig_setup_new.ini'), encoding='UTF-8',)

scope_ips= []
for i in range(len(config_initial['Scope_IPs'])):
    scope_ips.append(config_initial['Scope_IPs'][f'IP_{i}'])
scope_ips.append('')

# Enable DPI awareness on Windows BEFORE creating Tk
dpi_awared = enable_dpi_awareness_windows()
print("enable_dpi_awareness_windows ->", dpi_awared)

id_window = tk.Tk()
id_window.title(window_name)
id_window.resizable(width= False, height= False)
id_window.geometry('+500+150')
id_window.configure(background= '#91B6E1')

l_scope_ip = tk.Label(id_window, text= 'Enter Scope IP', background= '#91B6E1', fg= '#091E87', font= ('Candara', 12, 'bold'),)
str_scope_ip = tk.StringVar()
cb_scope_ip = ttk.Combobox(id_window, textvariable= str_scope_ip, values= scope_ips)
b_scope_ip = tk.Button(id_window, text= 'OK', width= 10, height= 2, command= lambda: show_main_window(old_scope_ips= scope_ips), )

l_ip = tk.Label(id_window, text= '★★★ 確認電腦IP與Scope在同一網域 ★★★', background= '#91B6E1', fg= '#F6044D', font= ('Candara', 14, 'bold'),)

l_scope_ip.pack(padx= 5, pady= 5)
cb_scope_ip.pack(padx= 5, pady= 5)
b_scope_ip.pack(padx= 5, pady= 5)
l_ip.pack(padx= 5, pady= 5)

id_window.mainloop()
