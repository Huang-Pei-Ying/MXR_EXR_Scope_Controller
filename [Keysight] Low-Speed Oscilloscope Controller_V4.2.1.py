import pyvisa
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog, ttk
import configparser
import os
from decimal import Decimal
import re
import time


# 第一個視窗取得scope id並開啟主視窗
def show_main_window(old_scope_ids):
    # 取得scope id
    selected_value = str_scope_id.get()

    # 新增scope id
    if selected_value and selected_value not in old_scope_ids:
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read(os.path.join(os.path.dirname(__file__), 'InitConfig_setup.ini'), encoding='utf-8',)
        config.set('Scope_IDs', f'ID_{len(old_scope_ids)-1}', selected_value)

        # 寫回ini
        with open(os.path.join(os.path.dirname(__file__), 'InitConfig_setup.ini'), 'w') as configfile:
            config.write(configfile)
        
    # 關閉第一個視窗
    id_window.destroy()
    
    # 創建主視窗
    main_window(scope_id= selected_value)
    

# =====================================================================================================================================================
def main_window(scope_id):

    def initialize():
        config_initial = configparser.ConfigParser()
        config_initial.optionxform = str
        config_initial.read(os.path.join(os.path.dirname(__file__), 'InitConfig_setup.ini'), encoding='UTF-8',)

        select_VoltScale = config_initial['Scale_Offset_Selected_Values']['VoltScale']
        select_VoltOffset = config_initial['Scale_Offset_Selected_Values']['VoltOffset']
        TimebaseScale = config_initial['Scale_Offset_Config']['TimebaseScale']
        TimebaseOffset = config_initial['Scale_Offset_Config']['TimebaseOffset']
        select_TriggerLevel = config_initial['Scale_Offset_Selected_Values']['TriggerLevel']
        TriggerChan = config_initial['Scale_Offset_Config']['TriggerChan']

        DeltaStartEdge = config_initial['Delta_Setup_Config']['DeltaStartEdge']
        DeltaStartNum = config_initial['Delta_Setup_Config']['DeltaStartNum']
        DeltaStartPosition = config_initial['Delta_Setup_Config']['DeltaStartPosition']
        DeltaStopEdge = config_initial['Delta_Setup_Config']['DeltaStopEdge']
        DeltaStopNum = config_initial['Delta_Setup_Config']['DeltaStopNum']
        DeltaStopPosition = config_initial['Delta_Setup_Config']['DeltaStopPosition']

        select_GeneralTopPercent = config_initial['Threshold_Selected_Values']['GeneralTopPercent']
        select_GeneralMiddlePercent = config_initial['Threshold_Selected_Values']['GeneralMiddlePercent']
        select_GeneralBasePercent = config_initial['Threshold_Selected_Values']['GeneralBasePercent']
        select_GeneralTop = config_initial['Threshold_Selected_Values']['GeneralTop']
        select_GeneralMiddle = config_initial['Threshold_Selected_Values']['GeneralMiddle']
        select_GeneralBase = config_initial['Threshold_Selected_Values']['GeneralBase']
        select_RFTopPercent = config_initial['Threshold_Selected_Values']['RFTopPercent']
        select_RFBasePercent = config_initial['Threshold_Selected_Values']['RFBasePercent']
        select_RFTop = config_initial['Threshold_Selected_Values']['RFTop']
        select_RFBase = config_initial['Threshold_Selected_Values']['RFBase']
        SamplingRate = config_initial['Acquisition']['SamplingRate']
        MemoryDepth = config_initial['Acquisition']['MemoryDepth']

        ChanLabel1 = config_initial['Lable_Setup_Config']['ChanLabel1']
        ChanLabel2 = config_initial['Lable_Setup_Config']['ChanLabel2']
        ChanLabel3 = config_initial['Lable_Setup_Config']['ChanLabel3']
        ChanLabel4 = config_initial['Lable_Setup_Config']['ChanLabel4']

        ChanSingle = config_initial['Chan_Delta']['ChanSingle']
        ChanStart = config_initial['Chan_Delta']['ChanStart']
        ChanStop = config_initial['Chan_Delta']['ChanStop']

        SaveImgFolder = config_initial['Save_Setup_Config']['SaveImgFolder']
        SaveImgPCFolder = config_initial['Save_Setup_Config']['SaveImgPCFolder']
        SaveImgName = config_initial['Save_Setup_Config']['SaveImgName']
        SaveWMeFolder = config_initial['Save_Setup_Config']['SaveWMeFolder']
        SaveWMePCFolder = config_initial['Save_Setup_Config']['SaveWMePCFolder']
        SaveWMeName = config_initial['Save_Setup_Config']['SaveWMeName']

        LoadWMe1 = config_initial['Load_WMemory_Setup_Config']['LoadWMe1']
        LoadWMe2 = config_initial['Load_WMemory_Setup_Config']['LoadWMe2']
        LoadWMe3 = config_initial['Load_WMemory_Setup_Config']['LoadWMe3']
        LoadWMe4 = config_initial['Load_WMemory_Setup_Config']['LoadWMe4']

        str_volt_scale.set(value= select_VoltScale)
        str_volt_offset.set(value= select_VoltOffset)
        str_time_scale.set(value= TimebaseScale)
        str_time_offset.set(value= TimebaseOffset)
        str_trigger_level.set(value= select_TriggerLevel)
        str_trigger_chan.set(value= TriggerChan)

        start_rf.set(value= DeltaStartEdge)
        start_num.set(value= DeltaStartNum)
        start_pos.set(value= DeltaStartPosition)
        stop_rf.set(value= DeltaStopEdge)
        stop_num.set(value= DeltaStopNum)
        stop_pos.set(value= DeltaStopPosition)

        str_gen_top_percent.set(value= select_GeneralTopPercent)
        str_gen_mid_percent.set(value= select_GeneralMiddlePercent)
        str_gen_base_percent.set(value= select_GeneralBasePercent)
        str_gen_top.set(value= select_GeneralTop)
        str_gen_mid.set(value= select_GeneralMiddle)
        str_gen_base.set(value= select_GeneralBase)
        str_rf_top_percent.set(value= select_RFTopPercent)
        str_rf_base_percent.set(value= select_RFBasePercent)
        str_rf_top.set(value= select_RFTop)
        str_rf_base.set(value= select_RFBase)
        str_sampling_rate.set(value= SamplingRate)
        str_memory_depth.set(value= MemoryDepth)

        str_label_1.set(value= ChanLabel1)
        str_label_2.set(value= ChanLabel2)
        str_label_3.set(value= ChanLabel3)
        str_label_4.set(value= ChanLabel4)

        int_ch_single.set(value= int(ChanSingle))
        int_ch_delta_start.set(value= int(ChanStart))
        int_ch_delta_stop.set(value= int(ChanStop))

        str_image_folder.set(value= SaveImgFolder)
        str_image_folder.set(value= SaveImgFolder)
        str_image_pc_folder.set(value= SaveImgPCFolder)
        str_image.set(value= SaveImgName)
        str_WMe_folder.set(value= SaveWMeFolder)
        str_WMe_pc_folder.set(value= SaveWMePCFolder)
        str_WMe.set(value= SaveWMeName)

        str_WMe1.set(value= LoadWMe1)
        str_WMe2.set(value= LoadWMe2)
        str_WMe3.set(value= LoadWMe3)
        str_WMe4.set(value= LoadWMe4)

        # return scope_ids

    class MXR:

        def __init__(self, scope_id):
            rm = pyvisa.ResourceManager()
            self.inst = rm.open_resource(f'TCPIP0::KEYSIGH-{scope_id}::inst0::INSTR')
            idn = self.inst.query('*IDN?').strip()
            print(f'Connect successfully! / {idn}')

        def sampling_rate_acquire(self, rate): # 科學記號
            self.inst.write(f':ACQuire:SRATe:ANALog {rate}')
            time.sleep(0.05)

        def memory_depth_acquire(self, points_value: int):
            self.inst.write(f':ACQuire:POINts:ANALog {points_value}')
            time.sleep(0.05)
        
        def RF_threshold(self, rf_top, rf_base, rf_top_percent, rf_base_percent):
            if int_rf_thres.get() == 1:
                self.inst.write(f':MEASure:THResholds:RFALl:METHod ALL,PERCent')
                time.sleep(0.05)
                self.inst.write(f':MEASure:THResholds:RFALl:PERCent ALL,{rf_top_percent},{(float(rf_top_percent)+float(rf_base_percent))/2},{rf_base_percent}')
                time.sleep(0.05)
            elif int_rf_thres.get() == 2:
                self.inst.write(f':MEASure:THResholds:RFALl:METHod ALL,ABSolute')
                time.sleep(0.05)
                self.inst.write(f':MEASure:THResholds:RFALl:ABSolute ALL,{rf_top},{(float(rf_top)+float(rf_base))/2},{rf_base}')
                time.sleep(0.05)

        def gen_threshold(self, g_top, g_middle, g_base, g_top_percent, g_middle_percent, g_base_percent):
            if int_gen_thres.get() == 1:
                do_the_judge= False
                if float(g_top_percent) <= float(g_middle_percent):
                    g_top_percent= Decimal(g_middle_percent) + Decimal('0.1')
                    cbb_gen_top_percent.config(foreground= 'red')
                    cbb_gen_mid_percent.config(foreground= 'red')
                    do_the_judge= True
                if float(g_middle_percent) <= float(g_base_percent):
                    g_base_percent= Decimal(g_middle_percent) - Decimal('0.1')
                    cbb_gen_base_percent.config(foreground= 'red')
                    cbb_gen_mid_percent.config(foreground= 'red')
                    do_the_judge= True
                if not do_the_judge:
                    cbb_gen_top_percent.config(foreground= 'black')
                    cbb_gen_mid_percent.config(foreground= 'black')
                    cbb_gen_base_percent.config(foreground= 'black')

                self.inst.write(f':MEASure:THResholds:GENeral:METHod ALL,PERCent')
                time.sleep(0.05)
                self.inst.write(f':MEASure:THResholds:GENeral:PERCent ALL,{g_top_percent},{g_middle_percent},{g_base_percent}')
                time.sleep(0.05)
            elif int_gen_thres.get() == 2:
                do_the_judge= False
                if float(g_top) <= float(g_middle):
                    g_top= Decimal(g_middle) + Decimal('0.01')
                    cbb_gen_top.config(foreground= 'red')
                    cbb_gen_mid.config(foreground= 'red')
                    do_the_judge= True
                if float(g_middle) <= float(g_base):
                    g_base= Decimal(g_middle) - Decimal('0.01')
                    cbb_gen_base.config(foreground= 'red')
                    cbb_gen_mid.config(foreground= 'red')
                    do_the_judge= True
                if not do_the_judge:
                    cbb_gen_top.config(foreground= 'black')
                    cbb_gen_mid.config(foreground= 'black')
                    cbb_gen_base.config(foreground= 'black')

                self.inst.write(f':MEASure:THResholds:GENeral:METHod ALL,ABSolute')
                time.sleep(0.05)
                self.inst.write(f':MEASure:THResholds:GENeral:ABSolute ALL,{g_top},{g_middle},{g_base}')
                time.sleep(0.05)

        def volt_check(self, scale, offset): # 科學記號
            display_dict= self.judge_chan_wme()
            for chan in display_dict['CHANnel']:
                self.inst.write(f':CHANnel{chan}:SCALe {scale}')
                time.sleep(0.05)
                self.inst.write(f':CHANnel{chan}:OFFSet {offset}')
                time.sleep(0.05)
            for wme in display_dict['WMEMory']:
                self.inst.write(f':WMEMory{wme}:YRANge {float(scale)*8}')
                time.sleep(0.05)
                self.inst.write(f':WMEMory{wme}:YOFFset {offset}')
                time.sleep(0.05)

        def timebase_position_check(self, position): # 科學記號
            self.inst.write(f':TIMebase:POSition {position}')
            time.sleep(0.05)

        def timebase_scale_check(self, scale): # 科學記號
            self.inst.write(f':TIMebase:SCALe {scale}')
            time.sleep(0.05)

        def trig_check(self, chan, level):
            res= self.inst.query(f':CHANnel{chan}:DISPlay?')
            time.sleep(0.05)
            if not res == '1\n':
                self.inst.write(f':CHANnel{chan}:DISPlay ON')
                time.sleep(0.05)
            self.inst.write(f':TRIGger:EDGE:SOURce CHANnel{chan}')
            time.sleep(0.05)
            self.inst.write(f':TRIGger:LEVel CHANnel{chan},{level}')
            time.sleep(0.05)
            if not res == '1\n':
                self.inst.write(f':CHANnel{chan}:DISPlay OFF')
                time.sleep(0.05)

        def display_Chan(self, chan):
            res= self.inst.query(f':CHANnel{chan}:DISPlay?')
            time.sleep(0.05)
            if res == '1\n':
                self.inst.write(f':CHANnel{chan}:DISPlay OFF')
                time.sleep(0.05)
            else:
                self.inst.write(f':CHANnel{chan}:DISPlay ON')
                time.sleep(0.05)

        def display_WMemory(self, chan):
            res= self.inst.query(f':WMEMory{chan}:DISPlay?')
            time.sleep(0.05)
            if res == '1\n':
                self.inst.write(f':WMEMory{chan}:DISPlay OFF')
                time.sleep(0.05)
            else:
                self.inst.write(f':WMEMory{chan}:DISPlay ON')
                time.sleep(0.05)
                
        def called_meas_function(self, chan, command_templates: dict):
            display_dict= self.judge_chan_wme()
            for key in command_templates:
                if chan in display_dict[key]:
                    self.inst.write(command_templates[key].format(chan))
                    time.sleep(0.05)            
        
        def freq(self, chan):
            command_templates = {
                'CHANnel': ':MEASure:FREQuency CHANnel{}',
                'WMEMory': ':MEASure:FREQuency WMEMory{}'
            }            
            self.called_meas_function(chan= chan, command_templates= command_templates)

        def period(self, chan):
            command_templates = {
                'CHANnel': ':MEASure:PERiod CHANnel{}',
                'WMEMory': ':MEASure:PERiod WMEMory{}'
            }            
            self.called_meas_function(chan= chan, command_templates= command_templates)
    
        def dutycycle(self, chan):
            command_templates = {
                'CHANnel': ':MEASure:DUTYcycle CHANnel{}',
                'WMEMory': ':MEASure:DUTYcycle WMEMory{}'
            }            
            self.called_meas_function(chan= chan, command_templates= command_templates)

        def slewrate(self, chan, direction):
            display_dict= self.judge_chan_wme()
            for cha in display_dict['CHANnel']:
                if cha == chan:
                    self.inst.write(f':MEASure:SLEWrate CHANnel{cha},{direction}')
                    time.sleep(0.05)
                    self.inst.write(f':MEASure:NAME MEAS1,"{direction} Slew Rate({cha})"')
                    time.sleep(0.05)
            for wme in display_dict['WMEMory']:
                if wme == chan:
                    self.inst.write(f':MEASure:SLEWrate WMEMory{wme},{direction}')
                    time.sleep(0.05)
                    self.inst.write(f':MEASure:NAME MEAS1,"{direction} Slew Rate(m{wme})"')
                    time.sleep(0.05)

        def tH(self, chan):
            command_templates = {
                'CHANnel': ':MEASure:PWIDth CHANnel{}',
                'WMEMory': ':MEASure:PWIDth WMEMory{}'
            }            
            self.called_meas_function(chan= chan, command_templates= command_templates)  

        def tL(self, chan):
            command_templates = {
                'CHANnel': ':MEASure:NWIDth CHANnel{}',
                'WMEMory': ':MEASure:NWIDth WMEMory{}'
            }            
            self.called_meas_function(chan= chan, command_templates= command_templates)  

        def tR(self, chan):
            command_templates = {
                'CHANnel': ':MEASure:RISetime CHANnel{}',
                'WMEMory': ':MEASure:RISetime WMEMory{}'
            }            
            self.called_meas_function(chan= chan, command_templates= command_templates)              

        def tF(self, chan):
            command_templates = {
                'CHANnel': ':MEASure:FALLtime CHANnel{}',
                'WMEMory': ':MEASure:FALLtime WMEMory{}'
            }            
            self.called_meas_function(chan= chan, command_templates= command_templates)              

        def VIH(self, chan):
            command_templates = {
                'CHANnel': ':MEASure:VTOP CHANnel{}',
                'WMEMory': ':MEASure:VTOP WMEMory{}'
            }            
            self.called_meas_function(chan= chan, command_templates= command_templates)              

        def VIL(self, chan):
            command_templates = {
                'CHANnel': ':MEASure:VBASe CHANnel{}',
                'WMEMory': ':MEASure:VBASe WMEMory{}'
            }            
            self.called_meas_function(chan= chan, command_templates= command_templates)              

        def tSU_tHO(self, edge_1, num_1, pos_1, edge_2, num_2, pos_2, chan, chan_start, chan_stop):
            displayed_dict= self.judge_chan_wme()
            for format in displayed_dict:
                for channel in displayed_dict[format]:
                    if chan_start == channel:
                        res_start= f'{format}'
                    if chan_stop == channel:
                        res_stop= f'{format}'

            if chan == 2:
                self.inst.write(f':MEASure:DELTatime:DEFine {edge_1},{num_1},{pos_1},{edge_2},{num_2},{pos_2}')
                time.sleep(0.05)
                self.inst.write(f':MEASure:DELTatime {res_start}{chan_start}, {res_stop}{chan_stop}')
                time.sleep(0.05)
            else:
                pass

        def run(self):
            self.inst.write(':RUN')
            time.sleep(0.05)

        def stop(self):
            self.inst.write(':STOP')
            time.sleep(0.05)

        def single(self):
            self.inst.write(':SINGLE')
            time.sleep(0.05)

        def autoscale(self):
            self.inst.write(':AUToscale')
            time.sleep(0.05)

        def clear_diaplay(self):
            self.inst.write(':CDISplay')
            time.sleep(0.05)

        def default(self):
            self.inst.write(':SYSTem:PRESet DEFault')
            time.sleep(0.05)

        def trig_type(self):
            res= self.inst.query(f':TRIGger:SWEep?')
            time.sleep(0.05)
            if res == 'AUTO\n':
                self.inst.write(':TRIGger:SWEep TRIGgered')
                time.sleep(0.05)
            else:
                self.inst.write(':TRIGger:SWEep AUTO')
                time.sleep(0.05)

        def trig_slope(self):
            res= self.inst.query(f':TRIGger:EDGE:SLOPe?')
            time.sleep(0.05)
            if res == 'POS\n':
                self.inst.write(':TRIGger:EDGE:SLOPe NEGative')
                time.sleep(0.05)
            else:
                self.inst.write(':TRIGger:EDGE:SLOPe POSitive')
                time.sleep(0.05)
                
        def delete_item(self):
            tuple_marker = (boolvar_marker_1, boolvar_marker_2, boolvar_marker_3, boolvar_marker_4, boolvar_marker_5, boolvar_marker_6, 
                            # boolvar_marker_7, boolvar_marker_8, boolvar_marker_9, boolvar_marker_10, boolvar_marker_11, boolvar_marker_12, 
                            )
            for i, boolvar in enumerate(tuple_marker):
                if boolvar.get():
                    self.inst.write(f'MEASurement{i+1}:CLEar')
                    time.sleep(0.05)

        def add_marker(self):
            tuple_marker = (boolvar_marker_1, boolvar_marker_2, boolvar_marker_3, boolvar_marker_4, boolvar_marker_5, boolvar_marker_6, 
                            # boolvar_marker_7, boolvar_marker_8, boolvar_marker_9, boolvar_marker_10, boolvar_marker_11, boolvar_marker_12, 
                            )
        
            for i, boolvar in enumerate(tuple_marker):
                self.inst.write(f':MARKer:MEASurement:MEASurement MEASurement{i+1},OFF')
                time.sleep(0.05)

            for i, boolvar in enumerate(tuple_marker):
                if boolvar.get():
                    self.inst.write(f':MARKer:MEASurement:MEASurement MEASurement{i+1},ON')
                    time.sleep(0.05)
        
        def delete_marker(self):
            tuple_marker = (boolvar_marker_1, boolvar_marker_2, boolvar_marker_3, boolvar_marker_4, boolvar_marker_5, boolvar_marker_6, 
                            # boolvar_marker_7, boolvar_marker_8, boolvar_marker_9, boolvar_marker_10, boolvar_marker_11, boolvar_marker_12, 
                            )
        
            for i, boolvar in enumerate(tuple_marker):
                if boolvar.get():
                    self.inst.write(f':MARKer:MEASurement:MEASurement MEASurement{i+1},OFF')
                    time.sleep(0.05)

        def add_label(self, chan, label):
            display_dict= self.judge_chan_wme()
            if label == '':
                self.inst.write(f':DISPlay:LABel OFF')
                time.sleep(0.05)
            else:
                self.inst.write(f':DISPlay:LABel ON')
                time.sleep(0.05)
                for cha in display_dict['CHANnel']:
                    if cha == chan:
                        self.inst.write(f':CHANnel{chan}:LABel "{label}"')
                        time.sleep(0.05)
                for wme in display_dict['WMEMory']:
                    if wme == chan:
                        self.inst.write(f':WMEMory{chan}:LABel "{label}"')
                        time.sleep(0.05)

        def load_wmemory(self, chan, folder, wme_name):
            self.inst.write(f':WMEMory:TIETimebase 1')
            time.sleep(0.05)
            self.inst.write(f':DISPlay:SCOLor WMEMory1,17,100,100')
            time.sleep(0.05)
            self.inst.write(f':DISPlay:SCOLor WMEMory2,38,100,84')
            time.sleep(0.05)
            self.inst.write(f':DISPlay:SCOLor WMEMory3,60,80,100')
            time.sleep(0.05)
            self.inst.write(f':DISPlay:SCOLor WMEMory4,94,100,100')
            time.sleep(0.05)
            self.inst.write(f':DISK:LOAD "C:/Users/Administrator/Desktop/{folder}/{wme_name}.h5",WMEMory{chan},OFF')
            time.sleep(0.05)
        
        def clear_wmemory(self, chan, string):
            self.inst.write(f':WMEMory{chan}:CLEar')
            time.sleep(0.05)
            string.set('')

        def save_waveform_scope(self, folder, image_name):
            # 清空狀態
            self.inst.write('*CLS')
            time.sleep(0.05)

            # error messenge
                # 113 This directory is not valid.
                # -256 File name not found
                # -257 File name error
                # -410 Query INTERRUPTED
                # -420 Query UNTERMINATED
                # 0 No error

            # CDIRectory會害存圖卡死 orz

            # 資料夾是否存在
            self.inst.query(f':DISK:DIRectory? "C:/Users/Administrator/Desktop/{folder}"')
            time.sleep(0.05)
            error_messenge=self.inst.query(f':SYSTem:ERRor?')
            time.sleep(0.05)
            # print(error_messenge)
            if error_messenge == '-256\n' or error_messenge == '113\n' or error_messenge == '-257\n':
                ask_scp_root = tk.Tk()
                ask_scp_root.withdraw()  # 隱藏主視窗
                ask_scp_result = messagebox.askyesno("Warning", f"資料夾不存在，是否新增？")
                ask_scp_root.destroy()
                
                if not ask_scp_result:
                    ask_scp_root = tk.Tk()
                    ask_scp_root.withdraw()  # 隱藏主視窗
                    messagebox.showinfo("Warning", f'檔案未儲存')
                    # print("檔案未保存。")
                    return     
                # 新建資料夾
                folder= folder.replace("/", "\\")
                # print(folder)
                temp_list= folder.split('\\')
                path= 'C:/Users/Administrator/Desktop'
                for i in temp_list:
                    path= f'{path}/{i}'
                    self.inst.write(f':DISK:MDIRectory "{path}"')
                    time.sleep(0.05)
        
            # 資料夾全部內容
            folder_content= self.inst.query(f':DISK:DIRectory? "C:/Users/Administrator/Desktop/{folder}"')
            time.sleep(0.05)
            # 使用正則表達式來匹配所有 .png 檔案名稱
            png_files = re.findall(r'\b[\w-]+\.(?:png)\b', folder_content)

            for file_name in png_files:
                if f'{image_name}.png' == file_name:
                    ask_scp_root = tk.Tk()
                    ask_scp_root.withdraw()  # 隱藏主視窗
                    ask_scp_result = messagebox.askyesno("Warning", f"檔案已經存在，是否覆蓋？")
                    ask_scp_root.destroy()
                    
                    if not ask_scp_result:
                        # print("檔案未保存。")
                        ask_scp_root = tk.Tk()
                        ask_scp_root.withdraw()  # 隱藏主視窗
                        messagebox.showinfo("Warning", f'檔案未儲存')
                        return     

            self.inst.write(f':DISK:SAVE:IMAGe "C:/Users/Administrator/Desktop/{folder}/{image_name}",PNG,SCReen,OFF,NORMal,OFF')
            time.sleep(0.05)

        def save_waveform_pc(self, folder, pc_folder, file_name):            

            full_path = rf"C:/Users/Administrator/Desktop/{folder}/{file_name}.png"
            full_path = full_path.replace('\\', '/')
            # print(full_path)
            data = b''
            message = f':DISK:GETFILE? "{full_path}"'
            data = self.inst.query_binary_values(message=message, datatype='B', header_fmt='ieee', container=bytes)
            time.sleep(0.05)

            if not os.path.exists(pc_folder):
                ask_root = tk.Tk()
                ask_root.withdraw()  # 隱藏主視窗
                ask_result = messagebox.askyesno("Warning", f"資料夾不存在，是否新增？")
                ask_root.destroy()
                
                if not ask_result:
                    ask_root = tk.Tk()
                    ask_root.withdraw()  # 隱藏主視窗
                    messagebox.showinfo("Warning", f'檔案未儲存')
                    # print("檔案未保存。")
                    return     
                os.mkdir(pc_folder) 

            if os.path.exists(f"{pc_folder}/{file_name}.png"):
                ask_root = tk.Tk()
                ask_root.withdraw()  # 隱藏主視窗
                ask_result = messagebox.askyesno("Warning", f"檔案已經存在，是否覆蓋？")
                ask_root.destroy()
                
                if not ask_result:
                    # print("檔案未保存。")
                    ask_root = tk.Tk()
                    ask_root.withdraw()  # 隱藏主視窗
                    messagebox.showinfo("Warning", f'檔案未儲存')
                    return     
           
            with open(f"{pc_folder}/{file_name}.png", 'wb') as f:
                f.write(data)

        def save_wmemory_scope(self, chan, folder, wme_name):
            # 清空狀態
            self.inst.write('*CLS')
            time.sleep(0.05)
            # error messenge
                # 113 This directory is not valid.
                # -256 File name not found
                # -257 File name error
                # -410 Query INTERRUPTED
                # -420 Query UNTERMINATED
                # 0 No error

            # 資料夾是否存在
            self.inst.query(f':DISK:DIRectory? "C:/Users/Administrator/Desktop/{folder}"')
            time.sleep(0.05)
            error_messenge=self.inst.query(f':SYSTem:ERRor?')
            time.sleep(0.05)
            # print(error_messenge)
            if error_messenge == '-256\n' or error_messenge == '113\n' or error_messenge == '-257\n':
                ask_scp_root = tk.Tk()
                ask_scp_root.withdraw()  # 隱藏主視窗
                ask_scp_result = messagebox.askyesno("Warning", f"資料夾不存在，是否新增？")
                ask_scp_root.destroy()
                
                if not ask_scp_result:
                    ask_scp_root = tk.Tk()
                    ask_scp_root.withdraw()  # 隱藏主視窗
                    messagebox.showinfo("Warning", f'檔案未儲存')
                    # print("檔案未保存。")
                    return     
                # 新建資料夾
                folder= folder.replace("/", "\\")
                # print(folder)
                temp_list= folder.split('\\')
                path= 'C:/Users/Administrator/Desktop'
                for i in temp_list:
                    path= f'{path}/{i}'
                    self.inst.write(f':DISK:MDIRectory "{path}"')
                    time.sleep(0.05)
        
            # 資料夾全部內容
            folder_content= self.inst.query(f':DISK:DIRectory? "C:/Users/Administrator/Desktop/{folder}"')
            time.sleep(0.05)
            # 使用正則表達式來匹配所有 .png 檔案名稱
            h5_files = re.findall(r'\b[\w-]+\.(?:h5)\b', folder_content)

            for file_name in h5_files:
                if f'{wme_name}.h5' == file_name:
                    ask_scp_root = tk.Tk()
                    ask_scp_root.withdraw()  # 隱藏主視窗
                    ask_scp_result = messagebox.askyesno("Warning", f"檔案已經存在，是否覆蓋？")
                    ask_scp_root.destroy()
                    
                    if not ask_scp_result:
                        # print("檔案未保存。")
                        ask_scp_root = tk.Tk()
                        ask_scp_root.withdraw()  # 隱藏主視窗
                        messagebox.showinfo("Warning", f'檔案未儲存')
                        return     

            self.inst.write(f':DISK:SAVE:WAVeform CHANnel{chan},"C:/Users/Administrator/Desktop/{folder}/{wme_name}",H5,OFF')
            time.sleep(0.05)

        def save_wmemory_pc(self, folder, pc_folder, file_name):
            full_path = f"C:/Users/Administrator/Desktop/{folder}/{file_name}.h5"
            data = b''
            message = ':DISK:GETFILE? "' + full_path + '"'
            data = self.inst.query_binary_values(message= message, datatype= 'B', header_fmt= 'ieee', container= bytes)
            time.sleep(0.05)
            
            if not os.path.exists(pc_folder):
                ask_root = tk.Tk()
                ask_root.withdraw()  # 隱藏主視窗
                ask_result = messagebox.askyesno("Warning", f"資料夾不存在，是否新增？")
                ask_root.destroy()
                
                if not ask_result:
                    ask_root = tk.Tk()
                    ask_root.withdraw()  # 隱藏主視窗
                    messagebox.showinfo("Warning", f'檔案未儲存')
                    # print("檔案未保存。")
                    return     
                os.mkdir(pc_folder) 

            if os.path.exists(f"{pc_folder}/{file_name}.h5"):
                ask_root = tk.Tk()
                ask_root.withdraw()  # 隱藏主視窗
                ask_result = messagebox.askyesno("Warning", f"檔案已經存在，是否覆蓋？")
                ask_root.destroy()
                
                if not ask_result:
                    # print("檔案未保存。")
                    ask_root = tk.Tk()
                    ask_root.withdraw()  # 隱藏主視窗
                    messagebox.showinfo("Warning", f'檔案未儲存')
                    return     
           
            with open(f"{pc_folder}/{file_name}.h5", 'wb') as f:
                f.write(data)

        def judge_chan_wme(self):
            display_dict= {'CHANnel': [],'WMEMory': []}
            for i in range(1, 5):
                chan_res= self.inst.query(f':CHANnel{i}:DISPlay?')
                time.sleep(0.05)
                wme_res= self.inst.query(f':WMEMory{i}:DISPlay?')
                time.sleep(0.05)

                if chan_res == '1\n' and not wme_res == '1\n':
                    display_dict['CHANnel'].append(i)
                    # return 'CHANnel'
                if not chan_res == '1\n' and wme_res == '1\n':
                    display_dict['WMEMory'].append(i)
                    # return 'WMEMory'
                if chan_res == '1\n' and wme_res == '1\n':
                    display_dict['CHANnel'].append(i)
                    display_dict['WMEMory'].append(i)

            return display_dict

        def get_results(self):
            meas_name= ['', '', '']
            mean= ['', '', '']
            all_results= self.inst.query(f':MEASure:RESults?')
            time.sleep(0.05)
            for index, value in enumerate(all_results.split(',')):
                if divmod(index, 7)[1] == 0:
                    try:
                        meas_name[divmod(index, 7)[0]]= value
                    except:
                        # l_meas_name_1.config(text=f'484超過3個??')
                        continue
                    if value[0] == 'V':  # 0: Voltage, 1: Time, 2: Slew Rate, 3: Frequency, 4: Duty cycle
                        measurement_type = 0 
                    elif 'Slew Rate' in value:
                        measurement_type = 2
                    elif 'Freq' in value:
                        measurement_type = 3
                    elif 'Duty cycle' in value:
                        measurement_type = 4
                    elif value == '\n':
                        meas_name[divmod(index, 7)[0]] = ''
                        continue
                    else:
                        measurement_type = 1
                if divmod(index, 7)[1] == 2:
                    if measurement_type == 0:
                        final_result= self.judge_volt_unit(value= value)
                    elif measurement_type == 1:
                        slew= False
                        final_result= self.judge_time_unit(value= value, slew= slew)
                    elif measurement_type == 2:
                        slew= True
                        final_result= self.judge_time_unit(value= value, slew= slew)
                    elif measurement_type == 3:
                        final_result= self.judge_freq_unit(value= value)
                    elif measurement_type == 4:
                        final_result = f"{float(value):.2f}"+' %'

                    try:
                        mean[divmod(index, 7)[0]]= final_result
                    except:
                        continue

            l_meas_name_1.config(text=f'{meas_name[0]}')
            text_mean_1.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
            text_mean_1.delete(1.0, tk.END)  # 清空當前內容
            text_mean_1.insert(tk.END, f"{mean[0]}")
            text_mean_1.config(state=tk.DISABLED)  # 設置為只讀狀態

            l_meas_name_2.config(text=f'{meas_name[1]}')
            text_mean_2.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
            text_mean_2.delete(1.0, tk.END)  # 清空當前內容
            text_mean_2.insert(tk.END, f"{mean[1]}")
            text_mean_2.config(state=tk.DISABLED)  # 設置為只讀狀態

            l_meas_name_3.config(text=f'{meas_name[2]}')
            text_mean_3.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
            text_mean_3.delete(1.0, tk.END)  # 清空當前內容
            text_mean_3.insert(tk.END, f"{mean[2]}")
            text_mean_3.config(state=tk.DISABLED)  # 設置為只讀狀態

        def judge_time_unit(self, value, slew):
            pattern = r'([+-]?\d*\.?\d+)E([+-]?\d+)'
            match = re.search(pattern, value)
            # 提取基數和指數
            base = float(match.group(1))
            exponent = int(match.group(2))
            if slew:
                if exponent == 3:
                    return f"{base} V/ms"
                elif exponent == 4:
                    return f"{base * 10} V/ms"
                elif exponent == 5:
                    return f"{base * 100} V/ms"
                elif exponent == 6:
                    return f"{base} V/us"
                elif exponent == 7:
                    return f"{base * 10} V/us"
                elif exponent == 8:
                    return f"{base * 100} V/us"
                elif exponent == 9:
                    return f"{base} V/ns"
                elif exponent == 10:
                    return f"{base * 10} V/ns"
                elif exponent == 11:
                    return f"{base * 100} V/ns"
                else:
                    # 如果指數不在指定的範圍内，返回原始字串
                    return f"{base} V/s"
            else:
                if exponent == -9:
                    return f"{base} ns"
                elif exponent == -8:
                    return f"{base * 10} ns"
                elif exponent == -7:
                    return f"{base * 100} ns"
                elif exponent == -6:
                    return f"{base} us"
                elif exponent == -5:
                    return f"{base * 10} us"
                elif exponent == -4:
                    return f"{base * 100} us"
                elif exponent == -3:
                    return f"{base} ms"
                elif exponent == -2:
                    return f"{base * 10} ms"
                elif exponent == -1:
                    return f"{base * 100} ms"
                elif exponent == -12:
                    return f"{base} ps"
                elif exponent == -11:
                    return f"{base * 10} ps"
                elif exponent == -10:
                    return f"{base * 100} ps"
                else:
                    # 如果指數不在指定的範圍内，返回原始字串
                    return f'{base} s'
                
        def judge_volt_unit(self, value):
            pattern = r'([+-]?\d*\.?\d+)E([+-]?\d+)'
            match = re.search(pattern, value)
            # 提取基數和指數
            base = float(match.group(1))
            exponent = int(match.group(2))
            # 基于不同的指数值进行不同的转换
            if exponent == -3:
                return f"{base} mV"
            elif exponent == -2:
                return f"{base * 10} mV"
            elif exponent == -1:
                return f"{base * 100} mV"
            else:
                # 如果指数不在指定的范围内，返回原始文本
                return f"{base} V"

        def judge_freq_unit(self, value):
            pattern = r'([+-]?\d*\.?\d+)E([+-]?\d+)'
            match = re.search(pattern, value)
            # 提取基數和指數
            base = float(match.group(1))
            exponent = int(match.group(2))
            # 基于不同的指数值进行不同的转换
            if exponent == 9:
                return f"{base} GHz"
            elif exponent == 8:
                return f"{base * 100} MHz"
            elif exponent == 7:
                return f"{base * 10} MHz"
            elif exponent == 6:
                return f"{base} MHz"
            elif exponent == 5:
                return f"{base * 100} kHz"
            elif exponent == 4:
                return f"{base * 10} kHz"
            elif exponent == 3:
                return f"{base} kHz"
            elif exponent == 2:
                return f"{base * 100} Hz"
            elif exponent == 1:
                return f"{base * 10} Hz"
            else:
                # 如果指数不在指定的范围内，返回原始文本
                return f"{base} Hz"

    def clear(string):
        string.set('')

    def close_window():
        if messagebox.askyesno('Message', 'Exit?'):
            config = configparser.ConfigParser()
            config.optionxform = str
            config.read( os.path.join(os.path.dirname(__file__), 'InitConfig_setup.ini'), encoding='utf-8',)
            
            # config.set('Scope_ID', 'ID', str_scope_id.get())

            config.set('Scale_Offset_Selected_Values', 'VoltScale', str_volt_scale.get())
            config.set('Scale_Offset_Selected_Values', 'VoltOffset', str_volt_offset.get())
            config.set('Scale_Offset_Config', 'TimebaseScale', str_time_scale.get())
            config.set('Scale_Offset_Config', 'TimebaseOffset', str_time_offset.get())
            config.set('Scale_Offset_Selected_Values', 'TriggerLevel', str_trigger_level.get())
            config.set('Scale_Offset_Config', 'TriggerChan', str_trigger_chan.get())
            
            config.set('Delta_Setup_Config', 'DeltaStartEdge', start_rf.get())
            config.set('Delta_Setup_Config', 'DeltaStartNum', start_num.get())
            config.set('Delta_Setup_Config', 'DeltaStartPosition', start_pos.get())
            config.set('Delta_Setup_Config', 'DeltaStopEdge', stop_rf.get())
            config.set('Delta_Setup_Config', 'DeltaStopNum', stop_num.get())
            config.set('Delta_Setup_Config', 'DeltaStopPosition', stop_pos.get())

            config.set('Threshold_Selected_Values', 'GeneralTopPercent', str_gen_top_percent.get())
            config.set('Threshold_Selected_Values', 'GeneralMiddlePercent', str_gen_mid_percent.get())
            config.set('Threshold_Selected_Values', 'GeneralBasePercent', str_gen_base_percent.get())
            config.set('Threshold_Selected_Values', 'GeneralTop', str_gen_top.get())
            config.set('Threshold_Selected_Values', 'GeneralMiddle', str_gen_mid.get())
            config.set('Threshold_Selected_Values', 'GeneralBase', str_gen_base.get())
            config.set('Threshold_Selected_Values', 'RFTopPercent', str_rf_top_percent.get())
            config.set('Threshold_Selected_Values', 'RFBasePercent', str_rf_base_percent.get())
            config.set('Threshold_Selected_Values', 'RFTop', str_rf_top.get())
            config.set('Threshold_Selected_Values', 'RFBase', str_rf_base.get())
            config.set('Acquisition', 'SamplingRate', str_sampling_rate.get())
            config.set('Acquisition', 'MemoryDepth', str_memory_depth.get())

            config.set('Lable_Setup_Config', 'ChanLabel1', str_label_1.get())
            config.set('Lable_Setup_Config', 'ChanLabel2', str_label_2.get())
            config.set('Lable_Setup_Config', 'ChanLabel3', str_label_3.get())
            config.set('Lable_Setup_Config', 'ChanLabel4', str_label_4.get())

            config.set('Chan_Delta', 'ChanSingle', str(int_ch_single.get()))
            config.set('Chan_Delta', 'ChanStart', str(int_ch_delta_start.get()))
            config.set('Chan_Delta', 'ChanStop', str(int_ch_delta_stop.get()))

            config.set('Save_Setup_Config', 'SaveImgFolder', str_image_folder.get())
            config.set('Save_Setup_Config', 'SaveImgPCFolder', str_image_pc_folder.get())
            config.set('Save_Setup_Config', 'SaveImgName', str_image.get())
            config.set('Save_Setup_Config', 'SaveWMeFolder', str_WMe_folder.get())
            config.set('Save_Setup_Config', 'SaveWMePCFolder', str_WMe_pc_folder.get())
            config.set('Save_Setup_Config', 'SaveWMeName', str_WMe.get())

            config.set('Load_WMemory_Setup_Config', 'LoadWMe1', str_WMe1.get())
            config.set('Load_WMemory_Setup_Config', 'LoadWMe2', str_WMe2.get())
            config.set('Load_WMemory_Setup_Config', 'LoadWMe3', str_WMe3.get())
            config.set('Load_WMemory_Setup_Config', 'LoadWMe4', str_WMe4.get())

            config.write(open(os.path.join(os.path.dirname(__file__), 'InitConfig_setup.ini'), 'w'))

            # formatted_time= self.current_time()
            # print(f'\n{formatted_time} [GUI Message] Window Closed.')
            window.destroy()

    
    def combo_ini():
        config_initial = configparser.ConfigParser()
        config_initial.optionxform = str
        config_file = os.path.join(os.path.dirname(__file__), 'InitConfig_setup.ini')
        config_initial.read(config_file, encoding='UTF-8')
        
        # Scale
        VoltScale_options = config_initial['Scale_Offset_Config'].get('VoltScale', '').split(',')
        VoltOffset_options = config_initial['Scale_Offset_Config'].get('VoltOffset', '').split(',')
        TriggerLevel_options = config_initial['Scale_Offset_Config'].get('TriggerLevel', '').split(',')

        # Threshold
        GeneralTopPercent_options = config_initial['Threshold_Setup_Config'].get('GeneralTopPercent', '').split(',')
        GeneralMiddlePercent_options = config_initial['Threshold_Setup_Config'].get('GeneralMiddlePercent', '').split(',')
        GeneralBasePercent_options = config_initial['Threshold_Setup_Config'].get('GeneralBasePercent', '').split(',')
        GeneralTop_options = config_initial['Threshold_Setup_Config'].get('GeneralTop', '').split(',')
        GeneralMiddle_options = config_initial['Threshold_Setup_Config'].get('GeneralMiddle', '').split(',')
        GeneralBase_options = config_initial['Threshold_Setup_Config'].get('GeneralBase', '').split(',')
        RFTopPercent_options = config_initial['Threshold_Setup_Config'].get('RFTopPercent', '').split(',')
        RFBasePercent_options = config_initial['Threshold_Setup_Config'].get('RFBasePercent', '').split(',')
        RFTop_options = config_initial['Threshold_Setup_Config'].get('RFTop', '').split(',')
        RFBase_options = config_initial['Threshold_Setup_Config'].get('RFBase', '').split(',')
        # 從這裡返回值供其他部分調用
        return {
            'VoltScale': VoltScale_options, 
            'VoltOffset': VoltOffset_options, 
            'TriggerLevel': TriggerLevel_options, 
            'GeneralTopPercent': GeneralTopPercent_options,
            'GeneralMiddlePercent': GeneralMiddlePercent_options, 
            'GeneralBasePercent': GeneralBasePercent_options, 
            'GeneralTop': GeneralTop_options, 
            'GeneralMiddle': GeneralMiddle_options, 
            'GeneralBase': GeneralBase_options, 
            'RFTopPercent': RFTopPercent_options, 
            'RFBasePercent': RFBasePercent_options, 
            'RFTop': RFTop_options, 
            'RFBase': RFBase_options, 
            
            'config_file': config_file,  # 儲存config文件路徑以便後續使用

            'selected_values': {
                'VoltScale': config_initial['Scale_Offset_Selected_Values'].get('VoltScale', ''),
                'VoltOffset': config_initial['Scale_Offset_Selected_Values'].get('VoltOffset', ''),
                'TriggerLevel': config_initial['Scale_Offset_Selected_Values'].get('TriggerLevel', ''),
                'GeneralTopPercent': config_initial['Threshold_Selected_Values'].get('GeneralTopPercent', ''),
                'GeneralMiddlePercent': config_initial['Threshold_Selected_Values'].get('GeneralMiddlePercent', ''),
                'GeneralBasePercent': config_initial['Threshold_Selected_Values'].get('GeneralBasePercent', ''),
                'GeneralTop': config_initial['Threshold_Selected_Values'].get('GeneralTop', ''),
                'GeneralMiddle': config_initial['Threshold_Selected_Values'].get('GeneralMiddle', ''),
                'GeneralBase': config_initial['Threshold_Selected_Values'].get('GeneralBase', ''),
                'RFTopPercent': config_initial['Threshold_Selected_Values'].get('RFTopPercent', ''),
                'RFBasePercent': config_initial['Threshold_Selected_Values'].get('RFBasePercent', ''),
                'RFTop': config_initial['Threshold_Selected_Values'].get('RFTop', ''),
                'RFBase': config_initial['Threshold_Selected_Values'].get('RFBase', ''),
                }        
        }

    def add_option(combobox, combobox_value, options, config_file, section, key, selected_section):
        new_option = combobox_value.get().strip()
        if new_option and new_option not in options:
            options.append(new_option)
            combobox['values'] = options
            save_to_ini(config_file, section, key, options, selected_section, combobox.get())

    def delete_option(combobox, combobox_value, options, config_file, section, key, selected_section):
        selected_option = combobox_value.get().strip()
        if selected_option in options:
            options.remove(selected_option)
            combobox['values'] = options
            combobox_value.set('')  # 清空當前選擇
            save_to_ini(config_file, section, key, options, selected_section, combobox.get())

    def save_to_ini(config_file, section, key, updated_options, selected_section, selected_value):
        config = configparser.ConfigParser()
        config.optionxform = str  # 保持大小寫
        config.read(config_file)
        if section not in config:
            config.add_section(section)
        
        # 更新指定的選項值
        config[section][key] = ','.join(updated_options)

        if selected_section not in config:
            config.add_section(selected_section)
        
        config[selected_section][key] = selected_value
        
        # 寫回INI文件
        with open(config_file, 'w') as configfile:
            config.write(configfile)


    class ToolTip:
        def __init__(self, widget, text):
            self.widget = widget
            self.text = text
            self.tip_window = None
            self.widget.bind("<Enter>", self.show_tip)
            self.widget.bind("<Leave>", self.hide_tip)

        def show_tip(self, event=None):
            "Display text in tooltip window"
            if self.tip_window or not self.text:
                return
            x, y, cx, cy = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + 57
            y += self.widget.winfo_rooty() + 21
            self.tip_window = tw = tk.Toplevel(self.widget)
            tw.wm_overrideredirect(True)
            tw.wm_geometry("+%d+%d" % (x, y))
            label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                            background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                            font=("tahoma", "8", "normal"))
            label.pack(ipadx=1)

        def hide_tip(self, event=None):
            if self.tip_window:
                self.tip_window.destroy()
                self.tip_window = None


    # 獲取ini數據
    config_data = combo_ini()
    # general_top_percent_options = config_data['GeneralTopPercent']
    config_file_path = config_data['config_file']


    def commbobox_function(combobox, combobox_var, ini_dict_key, ini_option_section, ini_option_key, ini_selected_section):
        combobox['values'] = config_data[ini_dict_key]  # 設置初始選項
        combobox.bind('<Return>', lambda event: add_option(combobox, combobox_var, config_data[ini_dict_key], config_file_path, ini_option_section, ini_option_key, ini_selected_section))
        combobox.bind('<Delete>', lambda event: delete_option(combobox, combobox_var, config_data[ini_dict_key], config_file_path, ini_option_section, ini_option_key, ini_selected_section))

    def select_folder(entry_var):
        # 打開檔案瀏覽器以選擇資料夾
        folder_selected = filedialog.askdirectory()
        # 將選擇的資料夾路徑填入 Entry
        entry_var.set(folder_selected)



    window = tk.Tk()
    window.title('[Keysight] Low-Speed Oscilloscope Controller')
    # window.geometry('1500x760+2+2')
    window.geometry('+2+2')
    window.configure(bg= '#E9F4FF')

    bg_color_1= '#c4cdd8'
    bg_color_2= '#b0c8db'

    # Measurement Frame ===================================================================================================================================

    label_frame_meas_item= tk.LabelFrame(window, text= 'Measurement', background= bg_color_1, fg= '#506376', font= ('Candara', 10, 'bold'),)

    b_freq = tk.Button(label_frame_meas_item, text='Frequency', width= 20, height= 2, command= lambda: mxr.freq(chan= int_ch_single.get()))
    b_period = tk.Button(label_frame_meas_item, text='Period', width= 20, height= 2, command= lambda: mxr.period(chan= int_ch_single.get()))
    b_dutycycle = tk.Button(label_frame_meas_item, text='Duty Cycle', width= 20, height= 2, command= lambda: mxr.dutycycle(chan= int_ch_single.get()))
    b_tSU = tk.Button(label_frame_meas_item, text='Delta Time', width= 20, height= 2, command= lambda: mxr.tSU_tHO(edge_1= start_rf.get(), num_1= start_num.get(), pos_1= start_pos.get(), edge_2= stop_rf.get(), num_2= stop_num.get(), pos_2= stop_pos.get(), chan= int_ch.get(), chan_start= int_ch_delta_start.get(), chan_stop= int_ch_delta_stop.get()))
    b_tH = tk.Button(label_frame_meas_item, text='tH', width= 20, height= 2, command= lambda: mxr.tH(chan= int_ch_single.get()))
    b_tL = tk.Button(label_frame_meas_item, text='tL', width= 20, height= 2, command= lambda: mxr.tL(chan= int_ch_single.get()))
    b_tR = tk.Button(label_frame_meas_item, text='tR', width= 20, height= 2, command= lambda: mxr.tR(chan= int_ch_single.get()))
    b_tF= tk.Button(label_frame_meas_item, text='tF', width= 20, height= 2, command= lambda: mxr.tF(chan= int_ch_single.get()))
    b_VIH = tk.Button(label_frame_meas_item, text='VIH', width= 20, height= 2, command= lambda: mxr.VIH(chan= int_ch_single.get()))
    b_VIL= tk.Button(label_frame_meas_item, text='VIL', width= 20, height= 2, command= lambda: mxr.VIL(chan= int_ch_single.get()))
    b_slewrate_tR = tk.Button(label_frame_meas_item, text='Slew Rate tR', width= 20, height= 2, command= lambda: mxr.slewrate(chan= int_ch_single.get(), direction= 'RISing'))
    b_slewrate_tF = tk.Button(label_frame_meas_item, text='Slew Rate tF', width= 20, height= 2, command= lambda: mxr.slewrate(chan= int_ch_single.get(), direction= 'FALLing'))


    # Scale / Offset Frame ===================================================================================================================================

    label_frame_scale= tk.LabelFrame(window, text= 'Scale / Offset', background= bg_color_1, fg= '#506376', font= ('Candara', 10, 'bold'),)

    l_volt_scale = tk.Label(label_frame_scale, text= 'Voltage Scale (V)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_volt_scale = tk.StringVar()
    cbb_volt_scale = ttk.Combobox(label_frame_scale, width= 7, textvariable= str_volt_scale)
    commbobox_function(combobox= cbb_volt_scale, combobox_var= str_volt_scale, ini_dict_key= 'VoltScale', ini_option_section= 'Scale_Offset_Config', ini_option_key= 'VoltScale', ini_selected_section= 'Scale_Offset_Selected_Values')

    l_volt_offset = tk.Label(label_frame_scale, text= 'Voltage Offset (V)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_volt_offset = tk.StringVar()
    cbb_volt_offset = ttk.Combobox(label_frame_scale, width= 7, textvariable= str_volt_offset)
    commbobox_function(combobox= cbb_volt_offset, combobox_var= str_volt_offset, ini_dict_key= 'VoltOffset', ini_option_section= 'Scale_Offset_Config', ini_option_key= 'VoltOffset', ini_selected_section= 'Scale_Offset_Selected_Values')

    b_volt_scale = tk.Button(label_frame_scale, text= 'Volt Check', width= 10, height= 1, command= lambda: mxr.volt_check(scale= str_volt_scale.get(), offset= str_volt_offset.get()))

    l_trigger_level = tk.Label(label_frame_scale, text= 'Trigger level (V)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_trigger_level = tk.StringVar()
    cbb_trigger_level = ttk.Combobox(label_frame_scale, width= 7, textvariable= str_trigger_level)
    commbobox_function(combobox= cbb_trigger_level, combobox_var= str_trigger_level, ini_dict_key= 'TriggerLevel', ini_option_section= 'Scale_Offset_Config', ini_option_key= 'TriggerLevel', ini_selected_section= 'Scale_Offset_Selected_Values')

    l_trigger_chan = tk.Label(label_frame_scale, text= 'Trigger Channel', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_trigger_chan = tk.StringVar()
    cb_trigger_chan = ttk.Combobox(label_frame_scale, width= 7, textvariable= str_trigger_chan, values= [1, 2, 3, 4])

    b_str_trigger_check = tk.Button(label_frame_scale, text= 'Trig Check', width= 10, height= 1, command= lambda: mxr.trig_check(chan= str_trigger_chan.get(), level= str_trigger_level.get()))

    l_time_scale = tk.Label(label_frame_scale, text= 'Timebase Scale (sec)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_time_scale = tk.StringVar()
    e_time_scale = tk.Entry(label_frame_scale, width= 7, textvariable= str_time_scale)

    l_time_offset = tk.Label(label_frame_scale, text= 'Timebase Offset (sec)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_time_offset = tk.StringVar()
    e_time_offset = tk.Entry(label_frame_scale, width= 7, textvariable= str_time_offset)

    b_time_scale_check = tk.Button(label_frame_scale, text= 'Time scale Check', height= 1, command= lambda: mxr.timebase_scale_check(scale= str_time_scale.get()))
    b_time_position_check = tk.Button(label_frame_scale, text= 'Time posi Check', height= 1, command= lambda: mxr.timebase_position_check(position= str_time_offset.get()))

    # Delta Setup Frame ===================================================================================================================================

    label_frame_delta= tk.LabelFrame(window, text= 'Delta Setup', background= bg_color_2, fg= '#506376', font= ('Candara', 10, 'bold'),)

    l_start = tk.Label(label_frame_delta, text= 'Delta Start', background= 'yellow', fg= '#0D325C', font= ('Candara', 11,),)

    start_rf = tk.StringVar()
    cb_start_rf = ttk.Combobox(label_frame_delta, width= 11, textvariable= start_rf, values= ['RISING', 'FALLING'])

    start_num = tk.StringVar()
    cb_start_num = tk.Entry(label_frame_delta, width= 11, textvariable= start_num)
    
    start_pos = tk.StringVar()
    cb_start_pos = ttk.Combobox(label_frame_delta, width= 11, textvariable= start_pos, values= ['UPPER', 'MIDDLE', 'LOWER'])
    
    l_stop = tk.Label(label_frame_delta, text= 'Delta Stop', background= 'yellow', fg= '#0D325C', font= ('Candara', 11,),)

    stop_rf = tk.StringVar()
    cb_stop_rf = ttk.Combobox(label_frame_delta, width= 11, textvariable= stop_rf, values= ['RISING', 'FALLING'])
    
    stop_num = tk.StringVar()
    cb_stop_num = tk.Entry(label_frame_delta, width= 11, textvariable= stop_num)
    
    stop_pos = tk.StringVar()
    cb_stop_pos = ttk.Combobox(label_frame_delta, width= 11, textvariable= stop_pos, values= ['UPPER', 'MIDDLE', 'LOWER'])
    

    # Threshold Frame ===================================================================================================================================

    label_frame_thres= tk.LabelFrame(window, text= 'Threshold', background= bg_color_1, fg= '#506376', font= ('Candara', 10, 'bold'),)

    int_gen_thres = tk.IntVar()    
    rb_gen_threshold_1= tk.Radiobutton(label_frame_thres, text= 'Gen Thres Top (%)', variable= int_gen_thres, value= 1, background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)

    str_gen_top_percent = tk.StringVar()
    cbb_gen_top_percent = ttk.Combobox(label_frame_thres, width= 8, textvariable= str_gen_top_percent)
    commbobox_function(combobox= cbb_gen_top_percent, combobox_var= str_gen_top_percent, ini_dict_key= 'GeneralTopPercent', ini_option_section= 'Threshold_Setup_Config', ini_option_key= 'GeneralTopPercent', ini_selected_section= 'Threshold_Selected_Values')
    
    l_gen_threshold_1= tk.Label(label_frame_thres, text= '            Gen Thres Middle (%)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_gen_mid_percent = tk.StringVar()
    cbb_gen_mid_percent = ttk.Combobox(label_frame_thres, width= 8, textvariable= str_gen_mid_percent)
    commbobox_function(combobox= cbb_gen_mid_percent, combobox_var= str_gen_mid_percent, ini_dict_key= 'GeneralMiddlePercent', ini_option_section= 'Threshold_Setup_Config', ini_option_key= 'GeneralMiddlePercent', ini_selected_section= 'Threshold_Selected_Values')

    l_gen_threshold_2= tk.Label(label_frame_thres, text= '        Gen Thres Base (%)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_gen_base_percent = tk.StringVar()
    cbb_gen_base_percent = ttk.Combobox(label_frame_thres, width= 8, textvariable= str_gen_base_percent)
    commbobox_function(combobox= cbb_gen_base_percent, combobox_var= str_gen_base_percent, ini_dict_key= 'GeneralBasePercent', ini_option_section= 'Threshold_Setup_Config', ini_option_key= 'GeneralBasePercent', ini_selected_section= 'Threshold_Selected_Values')

    rb_gen_threshold_2= tk.Radiobutton(label_frame_thres, text= 'Gen Thres Top (V)', variable= int_gen_thres, value= 2, background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)
    rb_gen_threshold_2.select()

    str_gen_top = tk.StringVar()
    cbb_gen_top = ttk.Combobox(label_frame_thres, width= 8, textvariable= str_gen_top)
    commbobox_function(combobox= cbb_gen_top, combobox_var= str_gen_top, ini_dict_key= 'GeneralTop', ini_option_section= 'Threshold_Setup_Config', ini_option_key= 'GeneralTop', ini_selected_section= 'Threshold_Selected_Values')

    l_gen_threshold_4= tk.Label(label_frame_thres, text= '            Gen Thres Middle (V)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_gen_mid = tk.StringVar()
    cbb_gen_mid = ttk.Combobox(label_frame_thres, width= 8, textvariable= str_gen_mid)
    commbobox_function(combobox= cbb_gen_mid, combobox_var= str_gen_mid, ini_dict_key= 'GeneralMiddle', ini_option_section= 'Threshold_Setup_Config', ini_option_key= 'GeneralMiddle', ini_selected_section= 'Threshold_Selected_Values')

    l_gen_threshold_5= tk.Label(label_frame_thres, text= '        Gen Thres Base (V)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_gen_base = tk.StringVar()
    cbb_gen_base = ttk.Combobox(label_frame_thres, width= 8, textvariable= str_gen_base)
    commbobox_function(combobox= cbb_gen_base, combobox_var= str_gen_base, ini_dict_key= 'GeneralBase', ini_option_section= 'Threshold_Setup_Config', ini_option_key= 'GeneralBase', ini_selected_section= 'Threshold_Selected_Values')
    b_gen_check = tk.Button(
        label_frame_thres, text= 'Gen Thres Check', command= lambda: mxr.gen_threshold(
            g_top= cbb_gen_top.get(), g_middle= cbb_gen_mid.get(), g_base= cbb_gen_base.get(), g_top_percent= cbb_gen_top_percent.get(), g_middle_percent= cbb_gen_mid_percent.get(), g_base_percent= cbb_gen_base_percent.get(), 
            )
        )

    int_rf_thres = tk.IntVar()    
    rb_rf_threshold_1= tk.Radiobutton(label_frame_thres, text= 'tRtF Thres Top (%)', variable= int_rf_thres, value= 1, background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)

    l_rf_threshold_1= tk.Label(label_frame_thres, text= '       tRtF Thres Base (%)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_rf_top_percent = tk.StringVar()
    cbb_rf_top_percent = ttk.Combobox(label_frame_thres, width= 8, textvariable= str_rf_top_percent)
    commbobox_function(combobox= cbb_rf_top_percent, combobox_var= str_rf_top_percent, ini_dict_key= 'RFTopPercent', ini_option_section= 'Threshold_Setup_Config', ini_option_key= 'RFTopPercent', ini_selected_section= 'Threshold_Selected_Values')

    str_rf_base_percent = tk.StringVar()
    cbb_rf_base_percent = ttk.Combobox(label_frame_thres, width= 8, textvariable= str_rf_base_percent)
    commbobox_function(combobox= cbb_rf_base_percent, combobox_var= str_rf_base_percent, ini_dict_key= 'RFBasePercent', ini_option_section= 'Threshold_Setup_Config', ini_option_key= 'RFBasePercent', ini_selected_section= 'Threshold_Selected_Values')

    rb_rf_threshold_2= tk.Radiobutton(label_frame_thres, text= 'tRtF Thres Top (V)', variable= int_rf_thres, value= 2, background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)
    rb_rf_threshold_2.select()

    l_rf_threshold_2= tk.Label(label_frame_thres, text= '       tRtF Thres Base (V)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_rf_top = tk.StringVar()
    cbb_rf_top = ttk.Combobox(label_frame_thres, width= 8, textvariable= str_rf_top)
    commbobox_function(combobox= cbb_rf_top, combobox_var= str_rf_top, ini_dict_key= 'RFTop', ini_option_section= 'Threshold_Setup_Config', ini_option_key= 'RFTop', ini_selected_section= 'Threshold_Selected_Values')

    str_rf_base = tk.StringVar()
    cbb_rf_base = ttk.Combobox(label_frame_thres, width= 8, textvariable= str_rf_base)
    commbobox_function(combobox= cbb_rf_base, combobox_var= str_rf_base, ini_dict_key= 'RFBase', ini_option_section= 'Threshold_Setup_Config', ini_option_key= 'RFBase', ini_selected_section= 'Threshold_Selected_Values')

    b_rf_check = tk.Button(
        label_frame_thres, text= 'RF Thres Check', command= lambda: mxr.RF_threshold(
            rf_top= cbb_rf_top.get(), rf_base= cbb_rf_base.get(), rf_top_percent= cbb_rf_top_percent.get(), rf_base_percent= cbb_rf_base_percent.get(),
            )
        )

    l_sampling_rate = tk.Label(label_frame_thres, text= '※ Sampling Rate', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)
    str_sampling_rate = tk.StringVar()
    e_sampling_rate = tk.Entry(label_frame_thres, width= 10, textvariable= str_sampling_rate)
    b_sampling_rate_check = tk.Button(label_frame_thres, text= 'Check', height= 1, command= lambda: mxr.sampling_rate_acquire(rate= str_sampling_rate.get()))

    l_memory_depth = tk.Label(label_frame_thres, text= '※ Memory Depth', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)
    str_memory_depth = tk.StringVar()
    e_memory_depth = tk.Entry(label_frame_thres, width= 10, textvariable= str_memory_depth)
    b_memory_depth_check = tk.Button(label_frame_thres, text= 'Check', height= 1, command= lambda: mxr.memory_depth_acquire(points_value= str_memory_depth.get()))


    # Label Frame ===================================================================================================================================

    label_frame_label= tk.LabelFrame(window, text= 'Label', background= bg_color_2, fg= '#506376', font= ('Candara', 10, 'bold'),)

    str_label_1 = tk.StringVar()
    e_label_1 = tk.Entry(label_frame_label, width= 50, textvariable= str_label_1)

    b_lable1 = tk.Button(label_frame_label, text= 'Chan1_label', command= lambda: mxr.add_label(chan= 1, label= str_label_1.get().rstrip('\n')))
    b_clear1 = tk.Button(label_frame_label, text= 'Clear', command= lambda: clear(string= str_label_1))

    str_label_2 = tk.StringVar()
    e_label_2 = tk.Entry(label_frame_label, width= 50, textvariable= str_label_2)

    b_lable2 = tk.Button(label_frame_label, text= 'Chan2_label', command= lambda: mxr.add_label(chan= 2, label= (str_label_2.get().rstrip('\n'))))
    b_clear2 = tk.Button(label_frame_label, text= 'Clear', command= lambda: clear(string= str_label_2))

    str_label_3 = tk.StringVar()
    e_label_3 = tk.Entry(label_frame_label, width= 50, textvariable= str_label_3)

    b_lable3 = tk.Button(label_frame_label, text= 'Chan3_label', command= lambda: mxr.add_label(chan= 3, label= (str_label_3.get().rstrip('\n'))))
    b_clear3 = tk.Button(label_frame_label, text= 'Clear', command= lambda: clear(string= str_label_3))

    str_label_4 = tk.StringVar()
    e_label_4 = tk.Entry(label_frame_label, width= 50, textvariable= str_label_4)

    b_lable4 = tk.Button(label_frame_label, text= 'Chan4_label', command= lambda: mxr.add_label(chan= 4, label= (str_label_4.get().rstrip('\n'))))
    b_clear4 = tk.Button(label_frame_label, text= 'Clear', command= lambda: clear(string= str_label_4))


    # Control Frame ===================================================================================================================================

    label_frame_control= tk.LabelFrame(window, text= 'Control', background= bg_color_2, fg= '#506376', font= ('Candara', 10, 'bold'),)

    b_run = tk.Button(label_frame_control, text='RUN', width= 20, height= 2, command= lambda: mxr.run())

    b_stop = tk.Button(label_frame_control, text='STOP', width= 20, height= 2, command= lambda: mxr.stop())

    b_single = tk.Button(label_frame_control, text='SINGLE', width= 20, height= 2, command= lambda: mxr.single())

    b_clear_display = tk.Button(label_frame_control, text='Clear', width= 8, height= 2, command= lambda: mxr.clear_diaplay())

    b_autoscale = tk.Button(label_frame_control, text='Auto Scale', width= 20, height= 2, command= lambda: mxr.autoscale())

    b_default = tk.Button(label_frame_control, text='Default', width= 20, height= 2, command= lambda: mxr.default())

    b_trigger = tk.Button(label_frame_control, text='Trigger Type', width= 20, height= 2, command= lambda: mxr.trig_type())

    b_del = tk.Button(label_frame_control, text='Delete item', width= 20, height= 2, command= lambda: mxr.delete_item())

    b_add_marker = tk.Button(label_frame_control, text='Add Marker', width= 20, height= 2, command= lambda: mxr.add_marker())

    b_del_marker = tk.Button(label_frame_control, text='Del Marker', width= 20, height= 2, command= lambda: mxr.delete_marker())

    b_trig_slope = tk.Button(label_frame_control, text= 'Trig Slope', width= 8, height= 2, command= lambda: mxr.trig_slope())

    boolvar_marker_1 = tk.BooleanVar()    
    cb_marker_1= tk.Checkbutton(label_frame_control, text= 'Meas 1', variable= boolvar_marker_1, background= bg_color_2, fg= '#0D325C')

    boolvar_marker_2 = tk.BooleanVar()    
    cb_marker_2= tk.Checkbutton(label_frame_control, text= 'Meas 2', variable= boolvar_marker_2, background= bg_color_2, fg= '#0D325C')

    boolvar_marker_3 = tk.BooleanVar()    
    cb_marker_3= tk.Checkbutton(label_frame_control, text= 'Meas 3', variable= boolvar_marker_3, background= bg_color_2, fg= '#0D325C')

    boolvar_marker_4 = tk.BooleanVar()    
    cb_marker_4= tk.Checkbutton(label_frame_control, text= 'Meas 4', variable= boolvar_marker_4, background= bg_color_2, fg= '#0D325C')

    boolvar_marker_5 = tk.BooleanVar()    
    cb_marker_5= tk.Checkbutton(label_frame_control, text= 'Meas 5', variable= boolvar_marker_5, background= bg_color_2, fg= '#0D325C')

    boolvar_marker_6 = tk.BooleanVar()    
    cb_marker_6= tk.Checkbutton(label_frame_control, text= 'Meas 6', variable= boolvar_marker_6, background= bg_color_2, fg= '#0D325C')

    # boolvar_marker_7 = tk.BooleanVar()    
    # cb_marker_7= tk.Checkbutton(label_frame_control, text= 'Meas7', variable= boolvar_marker_7)

    # boolvar_marker_8 = tk.BooleanVar()    
    # cb_marker_8= tk.Checkbutton(label_frame_control, text= 'Meas8', variable= boolvar_marker_8)

    # boolvar_marker_9 = tk.BooleanVar()    
    # cb_marker_9= tk.Checkbutton(label_frame_control, text= 'Meas9', variable= boolvar_marker_9)

    # boolvar_marker_10 = tk.BooleanVar()    
    # cb_marker_10= tk.Checkbutton(label_frame_control, text= 'Meas10', variable= boolvar_marker_10)

    # boolvar_marker_11 = tk.BooleanVar()    
    # cb_marker_11= tk.Checkbutton(label_frame_control, text= 'Meas11', variable= boolvar_marker_11)

    # boolvar_marker_12 = tk.BooleanVar()    
    # cb_marker_12= tk.Checkbutton(label_frame_control, text= 'Meas12', variable= boolvar_marker_12)


    # Channel Frame ===================================================================================================================================

    label_frame_chan= tk.LabelFrame(window, text= 'Channel', background= bg_color_1, fg= '#506376', font= ('Candara', 10, 'bold'),)

    b_Chan1 = tk.Button(label_frame_chan, text='Chan1', width= 20, height= 2, command= lambda: mxr.display_Chan(chan= 1))
    b_Chan2 = tk.Button(label_frame_chan, text='Chan2', width= 20, height= 2, command= lambda: mxr.display_Chan(chan= 2))
    b_Chan3 = tk.Button(label_frame_chan, text='Chan3', width= 20, height= 2, command= lambda: mxr.display_Chan(chan= 3))
    b_Chan4 = tk.Button(label_frame_chan, text='Chan4', width= 20, height= 2, command= lambda: mxr.display_Chan(chan= 4))
    b_WMe1 = tk.Button(label_frame_chan, text='WMemory1', width= 20, height= 2, command= lambda: mxr.display_WMemory(chan= 1))
    b_WMe2 = tk.Button(label_frame_chan, text='WMemory2', width= 20, height= 2, command= lambda: mxr.display_WMemory(chan= 2))
    b_WMe3 = tk.Button(label_frame_chan, text='WMemory3', width= 20, height= 2, command= lambda: mxr.display_WMemory(chan= 3))
    b_WMe4 = tk.Button(label_frame_chan, text='WMemory4', width= 20, height= 2, command= lambda: mxr.display_WMemory(chan= 4))

    int_ch = tk.IntVar()    
    rb_ch_single = tk.Radiobutton(label_frame_chan, text= 'Chan', variable= int_ch, value= 1, background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)
    rb_ch_single.select()
    int_ch_single = tk.IntVar()
    cb_ch_single = ttk.Combobox(label_frame_chan, width= 5, textvariable= int_ch_single, values= [1, 2, 3, 4])

    rb_ch_delta = tk.Radiobutton(label_frame_chan, text= 'Chan', variable= int_ch, value= 2, background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)
    int_ch_delta_start = tk.IntVar()
    cb_ch_delta_start = ttk.Combobox(label_frame_chan, width= 5, textvariable= int_ch_delta_start, values= [1, 2, 3, 4])

    l_arrow = tk.Label(label_frame_chan, text= '      ↓', background= bg_color_1, fg= '#0D325C', font= ('Calibri', 11, 'bold'),)
    l_ch_delta_stop = tk.Label(label_frame_chan, text= 'Chan', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)
    int_ch_delta_stop = tk.IntVar()
    cb_ch_delta_stop = ttk.Combobox(label_frame_chan, width= 5, textvariable= int_ch_delta_stop, values= [1, 2, 3, 4])

    b_get_results = tk.Button(label_frame_chan, text= 'Get Results\n(只能取3個)', width= 10, command= lambda: mxr.get_results())
    l_meas_name_1 = tk.Label(label_frame_chan, text= '', background= bg_color_1, fg= '#516464', font= ('Candara', 11, 'bold'),)
    text_mean_1 = tk.Text(label_frame_chan, width= 20, height= 1, background= '#DBE4F0', fg= '#375050', font= ('Calibri', 11, 'bold'),)
    text_mean_1.config(state=tk.DISABLED)
    l_meas_name_2 = tk.Label(label_frame_chan, text= '', background= bg_color_1, fg= '#516464', font= ('Candara', 11, 'bold'),)
    text_mean_2 = tk.Text(label_frame_chan, width= 20, height= 1, background= '#DBE4F0', fg= '#375050', font= ('Calibri', 11, 'bold'),)
    text_mean_2.config(state=tk.DISABLED)
    l_meas_name_3 = tk.Label(label_frame_chan, text= '', background= bg_color_1, fg= '#516464', font= ('Candara', 11, 'bold'),)
    text_mean_3 = tk.Text(label_frame_chan, width= 20, height= 1, background= '#DBE4F0', fg= '#375050', font= ('Calibri', 11, 'bold'),)
    text_mean_3.config(state=tk.DISABLED)


    # Save Frame ===================================================================================================================================

    label_frame_save= tk.LabelFrame(window, text= 'Save', background= bg_color_2, fg= '#506376', font= ('Candara', 10, 'bold'),)

    str_image_folder = tk.StringVar()
    e_image_folder = tk.Entry(label_frame_save, width= 45, textvariable= str_image_folder)

    l_image_folder = tk.Label(label_frame_save, text= 'Image Scope folder [填Desktop之後的資料夾路徑]', background= bg_color_2, fg= '#0D325C', font= ('Candara', 10,),)

    str_image_pc_folder = tk.StringVar()
    e_image_pc_folder = tk.Entry(label_frame_save, width= 45, textvariable= str_image_pc_folder)

    l_image_pc_folder = tk.Label(label_frame_save, text= 'Image PC folder [筆電的資料夾路徑]', background= bg_color_2, fg= '#0D325C', font= ('Candara', 10,),)

    b_image_pc_browse = tk.Button(label_frame_save, text= 'Browse', width= 10, command= lambda: select_folder(entry_var= str_image_pc_folder))
    
    str_image = tk.StringVar()
    e_image = tk.Entry(label_frame_save, width= 45, textvariable= str_image)

    l_imagename = tk.Label(label_frame_save, text= '(填 圖檔名)', background= bg_color_2, fg= '#0D325C', font= ('Candara', 10,),)

    b_image_save_scope = tk.Button(label_frame_save, text= 'Save Image-Scope', command= lambda: mxr.save_waveform_scope(folder= str_image_folder.get(), image_name= str_image.get()))
    b_image_save_pc = tk.Button(label_frame_save, text= 'Save Image-PC', command= lambda: mxr.save_waveform_pc(folder= str_image_folder.get(), file_name= str_image.get(), pc_folder= str_image_pc_folder.get()))

    str_WMe_folder = tk.StringVar()
    e_WMe_folder = tk.Entry(label_frame_save, width= 45, textvariable= str_WMe_folder)

    l_WMe_folder = tk.Label(label_frame_save, text= 'WMemory Scope folder [填Desktop之後的資料夾路徑]', background= bg_color_2, fg= '#0D325C', font= ('Candara', 10,),)

    str_WMe_pc_folder = tk.StringVar()
    e_WMe_pc_folder = tk.Entry(label_frame_save, width= 45, textvariable= str_WMe_pc_folder)

    l_WMe_pc_folder = tk.Label(label_frame_save, text= 'WMemory PC folder [筆電的資料夾路徑]', background= bg_color_2, fg= '#0D325C', font= ('Candara', 10,),)

    b_WMe_pc_browse = tk.Button(label_frame_save, text= 'Browse', width= 10, command= lambda: select_folder(entry_var= str_WMe_pc_folder))

    str_WMe = tk.StringVar()
    e_WMe = tk.Entry(label_frame_save, width= 45, textvariable= str_WMe)

    l_WMename = tk.Label(label_frame_save, text= '(填 WMe檔名)', background= bg_color_2, fg= '#0D325C', font= ('Candara', 10,),)

    b_WMe_save_scpoe = tk.Button(label_frame_save, text= 'Save WMe-Scope', command= lambda: mxr.save_wmemory_scope(chan= int_ch_single.get(), folder= str_WMe_folder.get(), wme_name= str_WMe.get()))
    b_WMe_save_pc = tk.Button(label_frame_save, text= 'Save WMe-PC', command= lambda: mxr.save_wmemory_pc(folder= str_WMe_folder.get(), file_name= str_WMe.get(), pc_folder= str_WMe_pc_folder.get()))


    # Load WMemory Frame ===================================================================================================================================

    label_frame_load_wme= tk.LabelFrame(window, text= 'Load WMemory', background= bg_color_1, fg= '#506376', font= ('Candara', 10, 'bold'),)

    str_WMe1 = tk.StringVar()
    e_WMe1 = tk.Entry(label_frame_load_wme, width= 50, textvariable= str_WMe1)

    b_WMe1_load = tk.Button(label_frame_load_wme, text= 'load WMemory1', command= lambda: mxr.load_wmemory(chan= 1, folder= str_WMe_folder.get(), wme_name= str_WMe1.get()))
    b_wme_clear1 = tk.Button(label_frame_load_wme, text= 'Clear', command= lambda: mxr.clear_wmemory(chan= 1, string= str_WMe1))

    str_WMe2 = tk.StringVar()
    e_WMe2 = tk.Entry(label_frame_load_wme, width= 50, textvariable= str_WMe2)
    
    b_WMe2_load = tk.Button(label_frame_load_wme, text= 'load WMemory2', command= lambda: mxr.load_wmemory(chan= 2, folder= str_WMe_folder.get(), wme_name= str_WMe2.get()))
    b_wme_clear2 = tk.Button(label_frame_load_wme, text= 'Clear', command= lambda: mxr.clear_wmemory(chan= 2, string= str_WMe2))

    str_WMe3 = tk.StringVar()
    e_WMe3 = tk.Entry(label_frame_load_wme, width= 50, textvariable= str_WMe3)

    b_WMe3_load = tk.Button(label_frame_load_wme, text= 'load WMemory3', command= lambda: mxr.load_wmemory(chan= 3, folder= str_WMe_folder.get(), wme_name= str_WMe3.get()))
    b_wme_clear3 = tk.Button(label_frame_load_wme, text= 'Clear', command= lambda: mxr.clear_wmemory(chan= 3, string= str_WMe3))

    str_WMe4 = tk.StringVar()
    e_WMe4 = tk.Entry(label_frame_load_wme, width= 50, textvariable= str_WMe4)
    
    b_WMe4_load = tk.Button(label_frame_load_wme, text= 'load WMemory4', command= lambda: mxr.load_wmemory(chan= 4, folder= str_WMe_folder.get(), wme_name= str_WMe4.get()))
    b_wme_clear4 = tk.Button(label_frame_load_wme, text= 'Clear', command= lambda: mxr.clear_wmemory(chan= 4, string= str_WMe4))


    # Grid ===================================================================================================================================
    # LabelFrame grid
    label_frame_meas_item.grid(row= 0, column= 0, padx= 5, pady= 3, columnspan= 2, sticky= 'nsew')
    label_frame_scale.grid(row= 1, column= 0, padx= 5, pady= 3, sticky= 'nsew')
    label_frame_delta.grid(row= 1, column= 1, padx= 5, pady= 3, sticky= 'nsew')
    label_frame_thres.grid(row= 2, column= 0, padx= 5, pady= 3, rowspan= 2, columnspan= 2, sticky= 'nsew')
    label_frame_label.grid(row= 4, column= 0, padx= 5, pady= 3, columnspan= 2, sticky= 'nsew')

    label_frame_control.grid(row= 0, column= 2, padx= 5, pady= 3, sticky= 'nsew')
    label_frame_chan.grid(row= 1, column= 2, padx= 5, pady= 3, sticky= 'nsew')
    label_frame_save.grid(row= 2, column= 2, padx= 5, pady= 3, sticky= 'nsew')
    label_frame_load_wme.grid(row= 3, column= 2, padx= 5, pady= 3, rowspan= 2, sticky= 'nsew')

    # Meas grid
    b_freq.grid(row= 0, column= 0, padx= 5, pady= 5)
    b_period.grid(row= 0, column= 1, padx= 5, pady= 5)
    b_dutycycle.grid(row= 0, column= 2, padx= 5, pady= 5)
    b_tSU.grid(row= 0, column= 3, padx= 5, pady= 5)
    b_tH.grid(row= 1, column= 0, padx= 5, pady= 5)
    b_tL.grid(row= 1, column= 1, padx= 5, pady= 5)
    b_tR.grid(row= 1, column= 2, padx= 5, pady= 5)
    b_tF.grid(row= 1, column= 3, padx= 5, pady= 5)
    b_VIH.grid(row= 2, column= 0, padx= 5, pady= 5)
    b_VIL.grid(row= 2, column= 1, padx= 5, pady= 5)
    b_slewrate_tR.grid(row= 2, column= 2, padx= 5, pady= 5)
    b_slewrate_tF.grid(row= 2, column= 3, padx= 5, pady= 5)

    # Scale grid
    l_volt_scale.grid(row= 0, column= 0, padx= 5, pady= 4, sticky= 'w') 
    cbb_volt_scale.grid(row= 0, column= 1, padx= 5, pady= 4)
    l_volt_offset.grid(row= 1, column= 0, padx= 5, pady= 4, sticky= 'w') 
    cbb_volt_offset.grid(row= 1, column= 1, padx= 5, pady= 4)
    b_volt_scale.grid(row= 2, column= 0, padx= 5, pady= 4, sticky= 'e')
    l_trigger_level.grid(row= 3, column= 0, padx= 5, pady= 4, sticky= 'w') 
    cbb_trigger_level.grid(row= 3, column= 1, padx= 5, pady= 4)
    l_trigger_chan.grid(row= 4, column= 0, padx= 5, pady= 4, sticky= 'w') 
    cb_trigger_chan.grid(row= 4, column= 1, padx= 5, pady= 4)
    b_str_trigger_check.grid(row= 4, column= 2, padx= 5, pady= 4)
    l_time_scale.grid(row= 0, column= 2, padx= 5, pady= 4, sticky= 'w') 
    e_time_scale.grid(row= 0, column= 3, padx= 5, pady= 4)
    l_time_offset.grid(row= 1, column= 2, padx= 5, pady= 4, sticky= 'w') 
    e_time_offset.grid(row= 1, column= 3, padx= 5, pady= 4)
    b_time_scale_check.grid(row= 2, column= 2, padx= 5, pady= 4)
    b_time_position_check.grid(row= 2, column= 3, padx= 5, pady= 4)

    # Delta grid
    l_start.grid(row= 0, column= 0, padx= 5, pady= 5)
    cb_start_rf.grid(row= 1, column= 0, padx=5, pady= 5)
    cb_start_num.grid(row= 2, column= 0, padx=5, pady= 5)
    cb_start_pos.grid(row= 3, column= 0, padx=5, pady= 5)
    l_stop.grid(row= 0, column= 1, padx= 5, pady= 5)
    cb_stop_rf.grid(row= 1, column= 1, padx=5, pady= 5)
    cb_stop_num.grid(row= 2, column= 1, padx=5, pady= 5)
    cb_stop_pos.grid(row= 3, column= 1, padx=5, pady= 5)

    # Thres grid
    rb_gen_threshold_1.grid(row= 0, column= 0, padx= 5, pady= 3)
    cbb_gen_top_percent.grid(row= 0, column= 1, sticky= 'w')
    l_gen_threshold_1.grid(row= 1, column= 0, padx= 5, pady= 3)
    cbb_gen_mid_percent.grid(row= 1, column= 1, sticky= 'w')
    l_gen_threshold_2.grid(row= 2, column= 0, padx= 5, pady= 3)
    cbb_gen_base_percent.grid(row= 2, column= 1, sticky= 'w')
    rb_gen_threshold_2.grid(row= 3, column= 0, padx= 5, pady= 3) 
    cbb_gen_top.grid(row= 3, column= 1, sticky= 'w')
    l_gen_threshold_4.grid(row= 4, column= 0, padx= 5, pady= 3) 
    cbb_gen_mid.grid(row= 4, column= 1, sticky= 'w')
    l_gen_threshold_5.grid(row= 5, column= 0, padx= 5, pady= 3) 
    cbb_gen_base.grid(row= 5, column= 1, sticky= 'w')
    b_gen_check.grid(row= 0, column= 2, padx= 5, pady= 3, sticky= 'e')
    rb_rf_threshold_1.grid(row= 0, column= 3, padx= 5, pady= 3)
    l_rf_threshold_1.grid(row= 1, column= 3, padx= 5, pady= 3) 
    cbb_rf_top_percent.grid(row= 0, column= 4, sticky= 'w')
    cbb_rf_base_percent.grid(row= 1, column= 4, sticky= 'w')
    rb_rf_threshold_2.grid(row= 2, column= 3, padx= 5, pady= 3) 
    l_rf_threshold_2.grid(row= 3, column= 3, padx= 5, pady= 3) 
    cbb_rf_top.grid(row= 2, column= 4, sticky= 'w')
    cbb_rf_base.grid(row= 3, column= 4, sticky= 'w')
    b_rf_check.grid(row= 0, column= 5, padx= 5, pady= 3, sticky= 'e')

    l_sampling_rate.grid(row= 4, column= 3)
    e_sampling_rate.grid(row= 4, column= 4)
    b_sampling_rate_check.grid(row= 4, column= 5)
    l_memory_depth.grid(row= 5, column= 3)
    e_memory_depth.grid(row= 5, column= 4)
    b_memory_depth_check.grid(row= 5, column= 5)

    # Label grid
    e_label_1.grid(row= 0, column= 0, padx= 5, pady= 3, columnspan= 2)
    b_lable1.grid(row= 0, column= 2, padx= 5, pady= 3)
    b_clear1.grid(row= 0, column= 3, padx= 5, pady= 3)
    e_label_2.grid(row= 1, column= 0, padx= 5, pady= 3, columnspan= 2)
    b_lable2.grid(row= 1, column= 2, padx= 5, pady= 3)
    b_clear2.grid(row= 1, column= 3, padx= 5, pady= 3)
    e_label_3.grid(row= 2, column= 0, padx= 5, pady= 3, columnspan= 2)
    b_lable3.grid(row= 2, column= 2, padx= 5, pady= 3)
    b_clear3.grid(row= 2, column= 3, padx= 5, pady= 3)
    e_label_4.grid(row= 3, column= 0, padx= 5, pady= 3, columnspan= 2)
    b_lable4.grid(row= 3, column= 2, padx= 5, pady= 3)
    b_clear4.grid(row= 3, column= 3, padx= 5, pady= 3)

    # Control grid
    b_run.grid(row= 0, column= 0, padx= 5, pady= 5, rowspan= 2)
    b_stop.grid(row= 0, column= 1, padx= 5, pady= 5, rowspan= 2)
    b_single.grid(row= 0, column= 2, padx= 5, pady= 5, rowspan= 2)
    b_clear_display.grid(row= 0, column= 3, padx= 5, pady= 5, rowspan= 2)
    b_autoscale.grid(row= 2, column= 0, padx= 5, pady= 5, rowspan= 2)
    b_default.grid(row= 2, column= 1, padx= 5, pady= 5, rowspan= 2)
    b_trigger.grid(row= 2, column= 2, padx= 5, pady= 5, rowspan= 2)
    b_del.grid(row= 4, column= 0, padx= 5, pady= 5, rowspan= 2)
    b_add_marker.grid(row= 4, column= 1, padx= 5, pady= 5, rowspan= 2)
    b_del_marker.grid(row= 4, column= 2, padx= 5, pady= 5, rowspan= 2)
    b_trig_slope.grid(row= 2, column= 3, padx= 5, pady= 5, rowspan= 2)
    cb_marker_1.grid(row= 0, column= 4, padx= 5) 
    cb_marker_2.grid(row= 1, column= 4, padx= 5) 
    cb_marker_3.grid(row= 2, column= 4, padx= 5) 
    cb_marker_4.grid(row= 3, column= 4, padx= 5) 
    cb_marker_5.grid(row= 4, column= 4, padx= 5) 
    cb_marker_6.grid(row= 5, column= 4, padx= 5) 
    # cb_marker_7.grid(row= 0, column= 5, sticky= 'w',) 
    # cb_marker_8.grid(row= 1, column= 5, sticky= 'w',) 
    # cb_marker_9.grid(row= 2, column= 5, sticky= 'w',) 
    # cb_marker_10.grid(row= 3, column= 5, sticky= 'w',) 
    # cb_marker_11.grid(row= 4, column= 5, sticky= 'w',) 
    # cb_marker_12.grid(row= 5, column= 5, sticky= 'w',) 

    # Chan grid
    b_Chan1.grid(row= 0, column= 0, padx= 5, pady= 5, rowspan= 2, columnspan= 2, sticky= 'w')
    b_Chan2.grid(row= 0, column= 2, padx= 5, pady= 5, rowspan= 2, columnspan= 2, sticky= 'w')
    b_Chan3.grid(row= 0, column= 4, padx= 5, pady= 5, rowspan= 2, columnspan= 2, sticky= 'w')
    b_Chan4.grid(row= 0, column= 6, padx= 5, pady= 5, rowspan= 2, columnspan= 2, sticky= 'w')
    b_WMe1.grid(row= 2, column= 0, padx= 5, pady= 5, rowspan= 2, columnspan= 2, sticky= 'w')
    b_WMe2.grid(row= 2, column= 2, padx= 5, pady= 5, rowspan= 2, columnspan= 2, sticky= 'w')
    b_WMe3.grid(row= 2, column= 4, padx= 5, pady= 5, rowspan= 2, columnspan= 2, sticky= 'w')
    b_WMe4.grid(row= 2, column= 6, padx= 5, pady= 5, rowspan= 2, columnspan= 2, sticky= 'w')
    rb_ch_single.grid(row= 4, column= 0, sticky= 'e')
    cb_ch_single.grid(row= 4, column= 1, sticky= 'w')
    rb_ch_delta.grid(row= 4, column= 2, sticky= 'e')
    cb_ch_delta_start.grid(row= 4, column= 3, sticky= 'w')
    l_arrow.grid(row= 5, column= 2, sticky= 'e')
    l_ch_delta_stop.grid(row= 6, column= 2, sticky= 'e')
    cb_ch_delta_stop.grid(row= 6, column= 3, sticky= 'w')
    b_get_results.grid(row= 4, column= 4, rowspan= 2)
    l_meas_name_1.grid(row= 4, column= 5, sticky= 'w')
    text_mean_1.grid(row= 4, column= 6, sticky= 'w')
    l_meas_name_2.grid(row= 5, column= 5, sticky= 'w')
    text_mean_2.grid(row= 5, column= 6, sticky= 'w')
    l_meas_name_3.grid(row= 6, column= 5, sticky= 'w')
    text_mean_3.grid(row= 6, column= 6, sticky= 'w')

    # Save grid
    e_image_folder.grid(row= 0, column= 0, padx= 5, pady= 3)
    l_image_folder.grid(row=0, column= 1, columnspan= 3, sticky= 'w', padx= 5, pady= 3)
    e_image_pc_folder.grid(row= 1, column= 0, padx= 5, pady= 3)
    b_image_pc_browse.grid(row= 1, column= 1, sticky= 'w', padx= 5, pady= 3)
    l_image_pc_folder.grid(row= 1, column= 2, columnspan= 3, sticky= 'w', padx= 5, pady= 3)
    e_image.grid(row= 2, column= 0, padx= 5, pady= 3)
    l_imagename.grid(row= 2, column= 1, sticky= 'w')
    b_image_save_scope.grid(row=2, column= 2, padx= 5, pady= 3, sticky= 'w')
    b_image_save_pc.grid(row= 2, column= 3, sticky= 'w', padx= 5, pady= 3)
    
    e_WMe_folder.grid(row= 3, column= 0, padx= 5, pady= 3)
    l_WMe_folder.grid(row=3, column= 1, columnspan= 3, sticky= 'w', padx= 5, pady= 3)
    e_WMe_pc_folder.grid(row= 4, column= 0, sticky= 'w', padx= 5, pady= 3)
    b_WMe_pc_browse.grid(row= 4, column= 1, sticky= 'w', padx= 5, pady= 3)
    l_WMe_pc_folder.grid(row= 4, column= 2, sticky= 'w', padx= 5, pady= 3, columnspan= 2)
    e_WMe.grid(row= 5, column= 0, sticky= 'w', padx= 5, pady= 3)
    l_WMename.grid(row= 5, column= 1, sticky= 'w')
    b_WMe_save_scpoe.grid(row= 5, column= 2, padx= 5, pady= 3)
    b_WMe_save_pc.grid(row= 5, column= 3, padx= 5, pady= 3)
    
    #LoadWMe grid
    e_WMe1.grid(row= 0, column= 0, padx= 5, pady= 3)
    b_WMe1_load.grid(row=0, column= 1, padx= 5, pady= 3)
    b_wme_clear1.grid(row= 0, column= 2, padx= 5, pady= 3)
    e_WMe2.grid(row= 1, column= 0, padx= 5, pady= 3)
    b_WMe2_load.grid(row=1, column= 1, padx= 5, pady= 3)
    b_wme_clear2.grid(row= 1, column= 2, padx= 5, pady= 3)
    e_WMe3.grid(row= 2, column= 0, padx= 5, pady= 3)
    b_WMe3_load.grid(row=2, column= 1, padx= 5, pady= 3)
    b_wme_clear3.grid(row= 2, column= 2, padx= 5, pady= 3)
    e_WMe4.grid(row= 3, column= 0, padx= 5, pady= 3)
    b_WMe4_load.grid(row=3, column= 1, padx= 5, pady= 3)
    b_wme_clear4.grid(row= 3, column= 2, padx= 5, pady= 3)


    # ToolTip(b_tSU, 'Channel記得勾對欸')
    ToolTip(cbb_volt_scale, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cbb_volt_offset, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cbb_trigger_level, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cb_start_rf, '嗚啦!')
    ToolTip(cb_start_num, '呀哈!')
    ToolTip(cb_start_pos, '噗嚕!')
    ToolTip(cb_stop_rf, '噗嚕!')
    ToolTip(cb_stop_num, '嗚啦!')
    ToolTip(cb_stop_pos, '呀哈!')
    ToolTip(cbb_gen_top_percent, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cbb_gen_mid_percent, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cbb_gen_base_percent, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cbb_gen_top, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cbb_gen_mid, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cbb_gen_base, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cbb_rf_top_percent, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cbb_rf_base_percent, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cbb_rf_top, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(cbb_rf_base, '可用滑鼠滾輪選擇\n新增選項: 輸入後按Enter\n刪除選項: 選擇後按Delete')
    ToolTip(e_label_4, '133 221 333 123 111')
    ToolTip(b_autoscale, '好的不得了')
    ToolTip(cb_marker_2, '防塵套不要亂丟!')
    ToolTip(cb_marker_5, '不要亂動我的程式ˋˊ')
    ToolTip(cb_ch_single, '累')
    ToolTip(cb_ch_delta_start, '隨波逐流的')
    ToolTip(cb_ch_delta_stop, '人生')
    ToolTip(text_mean_3, '好忙好忙')
    ToolTip(e_image_folder, '自己乖乖打字')
    ToolTip(e_image, '蛤~~~!')
    ToolTip(b_image_save_scope, '會幫你新增資料夾')
    ToolTip(b_image_save_pc, '示波器有沒有檔案ㄏㄚˋ')
    ToolTip(e_WMe_folder, '自己乖乖打字')
    ToolTip(e_WMe, 'Channel要選對欸')
    ToolTip(b_WMe_save_scpoe, '會幫你新增資料夾')
    ToolTip(b_WMe_save_pc, '沒有檔案會出事ㄏㄚˋ')
    ToolTip(e_WMe1, '嗚!嗚啦啦一嗚啦~~')
    ToolTip(e_WMe2, '嗚啦啦一呀哈呀哈!')
    ToolTip(e_WMe4, '噗嚕!')

    initialize()

    window.protocol('WM_DELETE_WINDOW', close_window)

    mxr= MXR(scope_id= scope_id)

    window.mainloop()


# 選擇 Scope ID ============================================================================================================================================

config_initial = configparser.ConfigParser()
config_initial.optionxform = str
config_initial.read(os.path.join(os.path.dirname(__file__), 'InitConfig_setup.ini'), encoding='UTF-8',)

scope_ids= []
for i in range(len(config_initial['Scope_IDs'])):
    scope_ids.append(config_initial['Scope_IDs'][f'ID_{i}'])
scope_ids.append('')

id_window = tk.Tk()
id_window.title('[Keysight] Low-Speed Oscilloscope Controller')
id_window.resizable(width= False, height= False)
id_window.geometry('390x160+500+150')
id_window.configure(background= '#91B6E1')

l_scope_id = tk.Label(id_window, text= 'Enter Scope ID', background= '#91B6E1', fg= '#091E87', font= ('Candara', 12, 'bold'),)
str_scope_id = tk.StringVar()
cb_scope_id = ttk.Combobox(id_window, textvariable= str_scope_id, values= scope_ids)
b_scope_id = tk.Button(id_window, text= 'OK', width= 10, height= 2, command= lambda: show_main_window(old_scope_ids= scope_ids), )

l_ip = tk.Label(id_window, text= '★★★ 確認電腦IP與Scope在同一網域 ★★★', background= '#91B6E1', fg= '#F6044D', font= ('Candara', 14, 'bold'),)

l_scope_id.pack(padx= 5, pady= 5)
cb_scope_id.pack(padx= 5, pady= 5)
b_scope_id.pack(padx= 5, pady= 5)
l_ip.pack(padx= 5, pady= 5)

id_window.mainloop()

