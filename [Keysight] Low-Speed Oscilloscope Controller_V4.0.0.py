import pyvisa
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog, ttk
import configparser
import os
from decimal import Decimal


# 第一個視窗取得scope id並開啟主視窗
def show_main_window(old_scope_ids):
    # 取得scope id
    selected_value = str_scope_id.get()

    # 新增scope id
    if selected_value and selected_value not in old_scope_ids:
        config = configparser.ConfigParser()
        config.optionxform = str
        config.read( os.path.join(os.path.dirname(__file__), 'InitConfig_setup.ini'), encoding='utf-8',)
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
        
        # Scope_ID = config_initial['Scope_ID']['ID']

        # scope_ids= []
        # for i in range(len(config_initial['Scope_IDs'])):
        #     scope_ids.append(config_initial['Scope_IDs'][f'ID_{i}'])

        VoltScale = config_initial['Scale_Offset_Config']['VoltScale']
        VoltOffset = config_initial['Scale_Offset_Config']['VoltOffset']
        TimebaseScale = config_initial['Scale_Offset_Config']['TimebaseScale']
        TimebaseOffset = config_initial['Scale_Offset_Config']['TimebaseOffset']
        TriggerLevel = config_initial['Scale_Offset_Config']['TriggerLevel']
        TriggerChan = config_initial['Scale_Offset_Config']['TriggerChan']

        DeltaStartEdge = config_initial['Delta_Setup_Config']['DeltaStartEdge']
        DeltaStartNum = config_initial['Delta_Setup_Config']['DeltaStartNum']
        DeltaStartPosition = config_initial['Delta_Setup_Config']['DeltaStartPosition']
        DeltaStopEdge = config_initial['Delta_Setup_Config']['DeltaStopEdge']
        DeltaStopNum = config_initial['Delta_Setup_Config']['DeltaStopNum']
        DeltaStopPosition = config_initial['Delta_Setup_Config']['DeltaStopPosition']

        GeneralTopPercent = config_initial['Threshold_Setup_Config']['GeneralTopPercent']
        GeneralMiddlePercent = config_initial['Threshold_Setup_Config']['GeneralMiddlePercent']
        GeneralBasePercent = config_initial['Threshold_Setup_Config']['GeneralBasePercent']
        GeneralTop = config_initial['Threshold_Setup_Config']['GeneralTop']
        GeneralMiddle = config_initial['Threshold_Setup_Config']['GeneralMiddle']
        GeneralBase = config_initial['Threshold_Setup_Config']['GeneralBase']
        RFTopPercent = config_initial['Threshold_Setup_Config']['RFTopPercent']
        RFBasePercent = config_initial['Threshold_Setup_Config']['RFBasePercent']
        RFTop = config_initial['Threshold_Setup_Config']['RFTop']
        RFBase = config_initial['Threshold_Setup_Config']['RFBase']
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
        # str_scope_id.set(value= Scope_ID)

        str_volt_scale.set(value= VoltScale)
        str_volt_offset.set(value= VoltOffset)
        str_time_scale.set(value= TimebaseScale)
        str_time_offset.set(value= TimebaseOffset)
        str_trigger_level.set(value= TriggerLevel)
        str_trigger_chan.set(value= TriggerChan)

        start_rf.set(value= DeltaStartEdge)
        start_num.set(value= DeltaStartNum)
        start_pos.set(value= DeltaStartPosition)
        stop_rf.set(value= DeltaStopEdge)
        stop_num.set(value= DeltaStopNum)
        stop_pos.set(value= DeltaStopPosition)

        str_gen_top_percent.set(value= GeneralTopPercent)
        str_gen_mid_percent.set(value= GeneralMiddlePercent)
        str_gen_base_percent.set(value= GeneralBasePercent)
        str_gen_top.set(value= GeneralTop)
        str_gen_mid.set(value= GeneralMiddle)
        str_gen_base.set(value= GeneralBase)
        str_rf_top_percent.set(value= RFTopPercent)
        str_rf_base_percent.set(value= RFBasePercent)
        str_rf_top.set(value= RFTop)
        str_rf_base.set(value= RFBase)
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

    # def ensure_directory_exists(directory_path):
    #     if not os.path.exists(directory_path):
    #         os.makedirs(directory_path)
    #     return directory_path

    class MXR:

        def __init__(self, scope_id):
            rm = pyvisa.ResourceManager()
            self.inst = rm.open_resource(f'TCPIP0::KEYSIGH-{scope_id}::inst0::INSTR')
            idn = self.inst.query('*IDN?').strip()
            print(f'Connect successfully! / {idn}')

        def sampling_rate_acquire(self, rate): # 科學記號
            self.inst.write(f':ACQuire:SRATe:ANALog {rate}')

        def memory_depth_acquire(self, points_value: int):
            self.inst.write(f':ACQuire:POINts:ANALog {points_value}')
        
        def RF_threshold(self, rf_top, rf_base, rf_top_percent, rf_base_percent):
            if int_rf_thres.get() == 1:
                self.inst.write(f':MEASure:THResholds:RFALl:METHod ALL,PERCent')
                self.inst.write(f':MEASure:THResholds:RFALl:PERCent ALL,{rf_top_percent},{(float(rf_top_percent)+float(rf_base_percent))/2},{rf_base_percent}')
            # elif int_rf_thres.get() == 2:
            #     self.inst.write(f':MEASure:THResholds:RFALl:METHod ALL,T2080')
            #     # self.inst.write(f':MEASure:THResholds:RFALl:TOPBase:PERCent ALL,80,20')
            # elif int_rf_thres.get() == 3:
            #     self.inst.write(f':MEASure:THResholds:RFALl:METHod ALL,PERCent')
            #     self.inst.write(f':MEASure:THResholds:RFALl:PERCent ALL,70,50,30')
            elif int_rf_thres.get() == 2:
                self.inst.write(f':MEASure:THResholds:RFALl:METHod ALL,ABSolute')
                self.inst.write(f':MEASure:THResholds:RFALl:ABSolute ALL,{rf_top},{(float(rf_top)+float(rf_base))/2},{rf_base}')

        def gen_threshold(self, g_top, g_middle, g_base, g_top_percent, g_middle_percent, g_base_percent):
            if int_gen_thres.get() == 1:
                do_the_judge= False
                if float(g_top_percent) <= float(g_middle_percent):
                    g_top_percent= Decimal(g_middle_percent) + Decimal('0.1')
                    e_gen_top_percent.config(fg= 'red')
                    e_gen_mid_percent.config(fg= 'red')
                    do_the_judge= True
                    # str_gen_top.set(f'{g_top}')
                if float(g_middle_percent) <= float(g_base_percent):
                    g_base_percent= Decimal(g_middle_percent) - Decimal('0.1')
                    e_gen_base_percent.config(fg= 'red')
                    e_gen_mid_percent.config(fg= 'red')
                    do_the_judge= True
                    # str_gen_base.set(f'{g_base}')
                if not do_the_judge:
                    e_gen_top_percent.config(fg= 'black')
                    e_gen_mid_percent.config(fg= 'black')
                    e_gen_base_percent.config(fg= 'black')

                self.inst.write(f':MEASure:THResholds:GENeral:METHod ALL,PERCent')
                self.inst.write(f':MEASure:THResholds:GENeral:PERCent ALL,{g_top_percent},{g_middle_percent},{g_base_percent}')
            # elif int_gen_thres.get() == 2:
            #     self.inst.write(f':MEASure:THResholds:GENeral:METHod ALL,PERCent')
            #     self.inst.write(f':MEASure:THResholds:GENeral:PERCent ALL,80,50,20')
            # elif int_gen_thres.get() == 3:
            #     self.inst.write(f':MEASure:THResholds:GENeral:METHod ALL,PERCent')
            #     self.inst.write(f':MEASure:THResholds:GENeral:PERCent ALL,70,50,30')
            elif int_gen_thres.get() == 2:
                do_the_judge= False
                if float(g_top) <= float(g_middle):
                    g_top= Decimal(g_middle) + Decimal('0.01')
                    e_gen_top.config(fg= 'red')
                    e_gen_mid.config(fg= 'red')
                    do_the_judge= True
                    # str_gen_top.set(f'{g_top}')
                if float(g_middle) <= float(g_base):
                    g_base= Decimal(g_middle) - Decimal('0.01')
                    e_gen_base.config(fg= 'red')
                    e_gen_mid.config(fg= 'red')
                    do_the_judge= True
                    # str_gen_base.set(f'{g_base}')
                if not do_the_judge:
                    e_gen_top.config(fg= 'black')
                    e_gen_mid.config(fg= 'black')
                    e_gen_base.config(fg= 'black')

                self.inst.write(f':MEASure:THResholds:GENeral:METHod ALL,ABSolute')
                self.inst.write(f':MEASure:THResholds:GENeral:ABSolute ALL,{g_top},{g_middle},{g_base}')

        def volt_check(self, scale, offset): # 科學記號
            # res_ch1= self.inst.query(f':CHANnel1:DISPlay?')
            # res_ch2= self.inst.query(f':CHANnel2:DISPlay?')
            # res_ch3= self.inst.query(f':CHANnel3:DISPlay?')

            # display_on_list= [res_ch1, res_ch2, res_ch3]
            # for index, value in enumerate(display_on_list):
            #     if value == '1\n':
            #         self.inst.write(f':CHANnel{index+1}:SCALe {scale}')
            #         self.inst.write(f':CHANnel{index+1}:OFFSet {offset}')
            res= self.judge_chan_wme()
            for i in range(1, 5):
                if res == 'CHANnel':
                    self.inst.write(f':CHANnel{i}:SCALe {scale}')
                    self.inst.write(f':CHANnel{i}:OFFSet {offset}')
                else:
                    self.inst.write(f':WMEMory{i}:YRANge {float(scale)*8}')
                    self.inst.write(f':WMEMory{i}:YOFFset {offset}')
            # for i in range(1, 4):
            #     self.inst.write(f':WMEMory{i}:SCALe {scale}')
            #     self.inst.write(f':WMEMory{i}:YOFFset {offset}')   

        def timebase_position_check(self, position): # 科學記號
            self.inst.write(f':TIMebase:POSition {position}')

        def timebase_scale_check(self, scale): # 科學記號
            self.inst.write(f':TIMebase:SCALe {scale}')

        def trig_check(self, chan, level):
            self.inst.write(f':TRIGger:EDGE:SOURce CHANnel{chan}')
            self.inst.write(f':TRIGger:LEVel CHANnel{chan},{level}')

        def display_Chan(self, chan):
            res= self.inst.query(f':CHANnel{chan}:DISPlay?')
            if res == '1\n':
                self.inst.write(f':CHANnel{chan}:DISPlay OFF')
            else:
                self.inst.write(f':CHANnel{chan}:DISPlay ON')

        def display_WMemory(self, chan):
            res= self.inst.query(f':WMEMory{chan}:DISPlay?')
            if res == '1\n':
                self.inst.write(f':WMEMory{chan}:DISPlay OFF')
            else:
                self.inst.write(f':WMEMory{chan}:DISPlay ON')
                
        def freq(self, chan):
            res= self.judge_chan_wme()
            self.inst.write(f':MEASure:FREQuency {res}{chan}')

        def period(self, chan):
            res= self.judge_chan_wme()
            self.inst.write(f':MEASure:PERiod {res}{chan}')
    
        def dutycycle(self, chan):
            res= self.judge_chan_wme()
            self.inst.write(f':MEASure:DUTYcycle {res}{chan}')

        def slewrate(self, chan, direction):
            res= self.judge_chan_wme()
            self.inst.write(f':MEASure:SLEWrate {res}{chan},{direction}')
            if res == 'CHANnel':
                self.inst.write(f':MEASure:NAME MEAS1,"{direction} Slew Rate({chan})"')
            else:
                self.inst.write(f':MEASure:NAME MEAS1,"{direction} Slew Rate(m{chan})"')

        def tH(self, chan):
            res= self.judge_chan_wme()
            self.inst.write(f':MEASure:PWIDth {res}{chan},')

        def tL(self, chan):
            res= self.judge_chan_wme()
            self.inst.write(f':MEASure:NWIDth {res}{chan}')

        def tR(self, chan):
            res= self.judge_chan_wme()
            self.inst.write(f':MEASure:RISetime {res}{chan}')

        def tF(self, chan):
            res= self.judge_chan_wme()
            self.inst.write(f':MEASure:FALLtime {res}{chan}')

        def VIH(self, chan):
            res= self.judge_chan_wme()
            self.inst.write(f':MEASure:VTOP {res}{chan}')

        def VIL(self, chan):
            res= self.judge_chan_wme()
            self.inst.write(f':MEASure:VBASe {res}{chan}')

        def tSU_tHO(self, edge_1, num_1, pos_1, edge_2, num_2, pos_2, chan, chan_start, chan_stop):
            res= self.judge_chan_wme()
            if chan == 2:
                self.inst.write(f':MEASure:DELTatime:DEFine {edge_1},{num_1},{pos_1},{edge_2},{num_2},{pos_2}')
                self.inst.write(f':MEASure:DELTatime {res}{chan_start}, {res}{chan_stop}')
            # elif chan == 5:
            #     self.inst.write(f':MEASure:DELTatime:DEFine {edge_1},{num_1},{pos_1},{edge_2},{num_2},{pos_2}')
            #     self.inst.write(f':MEASure:DELTatime {res}2, {res}1')
            # elif chan == 6:
            #     self.inst.write(f':MEASure:DELTatime:DEFine {edge_1},{num_1},{pos_1},{edge_2},{num_2},{pos_2}')
            #     self.inst.write(f':MEASure:DELTatime {res}1, {res}3')
            # elif chan == 7:
            #     self.inst.write(f':MEASure:DELTatime:DEFine {edge_1},{num_1},{pos_1},{edge_2},{num_2},{pos_2}')
            #     self.inst.write(f':MEASure:DELTatime {res}3, {res}1')
            # elif chan == 8:
            #     self.inst.write(f':MEASure:DELTatime:DEFine {edge_1},{num_1},{pos_1},{edge_2},{num_2},{pos_2}')
            #     self.inst.write(f':MEASure:DELTatime {res}1, {res}1')
            # elif chan == 9:
            #     self.inst.write(f':MEASure:DELTatime:DEFine {edge_1},{num_1},{pos_1},{edge_2},{num_2},{pos_2}')
            #     self.inst.write(f':MEASure:DELTatime {res}2, {res}2')
            # elif chan == 10:
            #     self.inst.write(f':MEASure:DELTatime:DEFine {edge_1},{num_1},{pos_1},{edge_2},{num_2},{pos_2}')
            #     self.inst.write(f':MEASure:DELTatime {res}3, {res}3')
            # elif chan == 11:
            #     self.inst.write(f':MEASure:DELTatime:DEFine {edge_1},{num_1},{pos_1},{edge_2},{num_2},{pos_2}')
            #     self.inst.write(f':MEASure:DELTatime {res}2, {res}3')
            # elif chan == 12:
            #     self.inst.write(f':MEASure:DELTatime:DEFine {edge_1},{num_1},{pos_1},{edge_2},{num_2},{pos_2}')
            #     self.inst.write(f':MEASure:DELTatime {res}3, {res}2')
            else:
                pass

        def run(self):
            self.inst.write(':RUN')

        def stop(self):
            self.inst.write(':STOP')

        def single(self):
            self.inst.write(':SINGLE')

        def autoscale(self):
            self.inst.write(':AUToscale')

        def clear_diaplay(self):
            self.inst.write(':CDISplay')

        def default(self):
            self.inst.write(':SYSTem:PRESet DEFault')

        def trig_type(self):
            res= self.inst.query(f':TRIGger:SWEep?')
            if res == 'AUTO\n':
                self.inst.write(':TRIGger:SWEep TRIGgered')
            else:
                self.inst.write(':TRIGger:SWEep AUTO')

        def trig_slope(self):
            res= self.inst.query(f':TRIGger:EDGE:SLOPe?')
            if res == 'POS\n':
                self.inst.write(':TRIGger:EDGE:SLOPe NEGative')
            else:
                self.inst.write(':TRIGger:EDGE:SLOPe POSitive')
                
        def delete_item(self):
            tuple_marker = (boolvar_marker_1, boolvar_marker_2, boolvar_marker_3, boolvar_marker_4, boolvar_marker_5, boolvar_marker_6, 
                            # boolvar_marker_7, boolvar_marker_8, boolvar_marker_9, boolvar_marker_10, boolvar_marker_11, boolvar_marker_12, 
                            )
            for i, boolvar in enumerate(tuple_marker):
                if boolvar.get():
                    self.inst.write(f'MEASurement{i+1}:CLEar')

        def add_marker(self):
            tuple_marker = (boolvar_marker_1, boolvar_marker_2, boolvar_marker_3, boolvar_marker_4, boolvar_marker_5, boolvar_marker_6, 
                            # boolvar_marker_7, boolvar_marker_8, boolvar_marker_9, boolvar_marker_10, boolvar_marker_11, boolvar_marker_12, 
                            )
        
            for i, boolvar in enumerate(tuple_marker):
                self.inst.write(f':MARKer:MEASurement:MEASurement MEASurement{i+1},OFF')

            for i, boolvar in enumerate(tuple_marker):
                if boolvar.get():
                    self.inst.write(f':MARKer:MEASurement:MEASurement MEASurement{i+1},ON')
        
        def delete_marker(self):
            tuple_marker = (boolvar_marker_1, boolvar_marker_2, boolvar_marker_3, boolvar_marker_4, boolvar_marker_5, boolvar_marker_6, 
                            # boolvar_marker_7, boolvar_marker_8, boolvar_marker_9, boolvar_marker_10, boolvar_marker_11, boolvar_marker_12, 
                            )
        
            for i, boolvar in enumerate(tuple_marker):
                if boolvar.get():
                    self.inst.write(f':MARKer:MEASurement:MEASurement MEASurement{i+1},OFF')

        def add_label(self, chan, label):
            res= self.judge_chan_wme()
            if label == '':
                self.inst.write(f':DISPlay:LABel OFF')
            else:
                self.inst.write(f':DISPlay:LABel ON')
                self.inst.write(f':{res}{chan}:LABel "{label}"')

        def load_wmemory(self, chan, folder, wme_name):
            self.inst.write(f':WMEMory:TIETimebase 1')
            self.inst.write(f':DISPlay:SCOLor WMEMory1,17,100,100')
            self.inst.write(f':DISPlay:SCOLor WMEMory2,38,100,84')
            self.inst.write(f':DISPlay:SCOLor WMEMory3,60,80,100')
            self.inst.write(f':DISPlay:SCOLor WMEMory4,94,100,100')
            self.inst.write(f':DISK:LOAD "C:/Users/Administrator/Desktop/{folder}/{wme_name}.h5",WMEMory{chan},OFF')
        
        def clear_wmemory(self, chan, string):
            self.inst.write(f':WMEMory{chan}:CLEar')
            string.set('')

        def save_waveform_scope(self, folder, image_name):
            self.inst.write(f':DISK:SAVE:IMAGe "C:/Users/Administrator/Desktop/{folder}/{image_name}",PNG,SCReen,OFF,NORMal,OFF')

        def save_waveform_pc(self, folder, pc_folder, file_name):
            full_path = f"C:/Users/Administrator/Desktop/{folder}/{file_name}.png"
            data = b''
            message = ':DISK:GETFILE? "' + full_path + '"'
            data = self.inst.query_binary_values(message= message, datatype= 'B', header_fmt= 'ieee', container= bytes)
            
            # if ext == 'png':
            #     directory_path= ensure_directory_exists(directory_path= f"{pc_folder}")
            # else:
            #     directory_path= ensure_directory_exists(directory_path= f"{pc_folder}/wfm")

            if os.path.exists(f"{pc_folder}/{file_name}.png"):
                ask_root = tk.Tk()
                ask_root.withdraw()  # 隱藏主視窗，其實我們不需要完整的視窗
                ask_result = messagebox.askyesno("檔案已存在", f"檔案已經存在，是否覆蓋？")
                ask_root.destroy()
                
                if not ask_result:
                    # print("檔案未保存。")
                    return     
           
            with open(f"{pc_folder}/{file_name}.png", 'wb') as f:
                f.write(data)

        def save_wmemory_scope(self, chan, folder, wme_name):
            self.inst.write(f':DISK:SAVE:WAVeform CHANnel{chan},"C:/Users/Administrator/Desktop/{folder}/{wme_name}",H5,OFF')

        def save_wmemory_pc(self, folder, pc_folder, file_name):
            full_path = f"C:/Users/Administrator/Desktop/{folder}/{file_name}.h5"
            data = b''
            message = ':DISK:GETFILE? "' + full_path + '"'
            data = self.inst.query_binary_values(message= message, datatype= 'B', header_fmt= 'ieee', container= bytes)
            
            # if ext == 'png':
            #     directory_path= ensure_directory_exists(directory_path= f"{pc_folder}")
            # else:
            #     directory_path= ensure_directory_exists(directory_path= f"{pc_folder}/wfm")

            if os.path.exists(f"{pc_folder}/{file_name}.h5"):
                ask_root = tk.Tk()
                ask_root.withdraw()  # 隱藏主視窗，其實我們不需要完整的視窗
                ask_result = messagebox.askyesno("檔案已存在", f"檔案已經存在，是否覆蓋？")
                ask_root.destroy()
                
                if not ask_result:
                    # print("檔案未保存。")
                    return     
           
            with open(f"{pc_folder}/{file_name}.h5", 'wb') as f:
                f.write(data)

        def judge_chan_wme(self):
            for i in range(1, 5):
                chan_res= self.inst.query(f':CHANnel{i}:DISPlay?')
                wme_res= self.inst.query(f':WMEMory{i}:DISPlay?')

                if chan_res == '1\n' and not wme_res == '1\n':
                    return 'CHANnel'
                elif not chan_res == '1\n' and wme_res == '1\n':
                    return 'WMEMory'
                # else:
                #     continue

    def clear(string):
        string.set('')

    def close_window():
        if messagebox.askyesno('Message', 'Exit?'):
            config = configparser.ConfigParser()
            config.optionxform = str
            config.read( os.path.join(os.path.dirname(__file__), 'InitConfig_setup.ini'), encoding='utf-8',)
            
            # config.set('Scope_ID', 'ID', str_scope_id.get())

            config.set('Scale_Offset_Config', 'VoltScale', str_volt_scale.get())
            config.set('Scale_Offset_Config', 'VoltOffset', str_volt_offset.get())
            config.set('Scale_Offset_Config', 'TimebaseScale', str_time_scale.get())
            config.set('Scale_Offset_Config', 'TimebaseOffset', str_time_offset.get())
            config.set('Scale_Offset_Config', 'TriggerLevel', str_trigger_level.get())
            config.set('Scale_Offset_Config', 'TriggerChan', str_trigger_chan.get())
            
            config.set('Delta_Setup_Config', 'DeltaStartEdge', start_rf.get())
            config.set('Delta_Setup_Config', 'DeltaStartNum', start_num.get())
            config.set('Delta_Setup_Config', 'DeltaStartPosition', start_pos.get())
            config.set('Delta_Setup_Config', 'DeltaStopEdge', stop_rf.get())
            config.set('Delta_Setup_Config', 'DeltaStopNum', stop_num.get())
            config.set('Delta_Setup_Config', 'DeltaStopPosition', stop_pos.get())

            config.set('Threshold_Setup_Config', 'GeneralTopPercent', str_gen_top_percent.get())
            config.set('Threshold_Setup_Config', 'GeneralMiddlePercent', str_gen_mid_percent.get())
            config.set('Threshold_Setup_Config', 'GeneralBasePercent', str_gen_base_percent.get())
            config.set('Threshold_Setup_Config', 'GeneralTop', str_gen_top.get())
            config.set('Threshold_Setup_Config', 'GeneralMiddle', str_gen_mid.get())
            config.set('Threshold_Setup_Config', 'GeneralBase', str_gen_base.get())
            config.set('Threshold_Setup_Config', 'RFTopPercent', str_rf_top_percent.get())
            config.set('Threshold_Setup_Config', 'RFBasePercent', str_rf_base_percent.get())
            config.set('Threshold_Setup_Config', 'RFTop', str_rf_top.get())
            config.set('Threshold_Setup_Config', 'RFBase', str_rf_base.get())
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

    
    window = tk.Tk()
    window.title('[Keysight] Low-Speed Oscilloscope Controller')
    window.geometry('1405x760+2+2')
    window.configure(bg= '#E9F4FF')

    # # Style
    # button_style= ttk.Style()
    # button_style.theme_use('alt')
    # button_style.configure('TButton', relief= 'raised', font= ('Candara', 10, 'bold'))
    # button_style.map("TButton",
    #           foreground=[('!active', '#506376'),('pressed', '#193F6B'), ('active', '#506376')],
    #           background=[ ('!active','#ECF4FC'),('pressed', '#ECF4FC'), ('active', '#ECF4FC')],
    # )
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
    e_volt_scale = tk.Entry(label_frame_scale, width= 7, textvariable= str_volt_scale)

    l_volt_offset = tk.Label(label_frame_scale, text= 'Voltage Offset (V)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_volt_offset = tk.StringVar()
    e_volt_offset = tk.Entry(label_frame_scale, width= 7, textvariable= str_volt_offset)

    b_volt_scale = tk.Button(label_frame_scale, text= 'Volt Check', width= 10, height= 1, command= lambda: mxr.volt_check(scale= str_volt_scale.get(), offset= str_volt_offset.get()))

    l_trigger_level = tk.Label(label_frame_scale, text= 'Trigger level (V)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_trigger_level = tk.StringVar()
    e_trigger_level = tk.Entry(label_frame_scale, width= 7, textvariable= str_trigger_level)

    l_trigger_chan = tk.Label(label_frame_scale, text= 'Trigger Channel', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_trigger_chan = tk.StringVar()
    e_trigger_chan = tk.Entry(label_frame_scale, width= 7, textvariable= str_trigger_chan)

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
    e_gen_top_percent = tk.Entry(label_frame_thres, width= 8, textvariable= str_gen_top_percent)

    l_gen_threshold_1= tk.Label(label_frame_thres, text= '            Gen Thres Middle (%)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_gen_mid_percent = tk.StringVar()
    e_gen_mid_percent = tk.Entry(label_frame_thres, width= 8, textvariable= str_gen_mid_percent)

    l_gen_threshold_2= tk.Label(label_frame_thres, text= '        Gen Thres Base (%)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_gen_base_percent = tk.StringVar()
    e_gen_base_percent = tk.Entry(label_frame_thres, width= 8, textvariable= str_gen_base_percent)
    
    rb_gen_threshold_2= tk.Radiobutton(label_frame_thres, text= 'Gen Thres Top (V)', variable= int_gen_thres, value= 2, background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)
    rb_gen_threshold_2.select()

    str_gen_top = tk.StringVar()
    e_gen_top = tk.Entry(label_frame_thres, width= 8, textvariable= str_gen_top)

    l_gen_threshold_4= tk.Label(label_frame_thres, text= '            Gen Thres Middle (V)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_gen_mid = tk.StringVar()
    e_gen_mid = tk.Entry(label_frame_thres, width= 8, textvariable= str_gen_mid)

    l_gen_threshold_5= tk.Label(label_frame_thres, text= '        Gen Thres Base (V)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_gen_base = tk.StringVar()
    e_gen_base = tk.Entry(label_frame_thres, width= 8, textvariable= str_gen_base)

    b_gen_check = tk.Button(label_frame_thres, text= 'Gen Thres Check', command= lambda: mxr.gen_threshold(
        g_top= e_gen_top.get(), g_middle= e_gen_mid.get(), g_base= e_gen_base.get(), 
        g_top_percent= e_gen_top_percent.get(), g_middle_percent= e_gen_mid_percent.get(), g_base_percent= e_gen_base_percent.get(), 
        )
        )

    int_rf_thres = tk.IntVar()    
    rb_rf_threshold_1= tk.Radiobutton(label_frame_thres, text= 'tRtF Thres Top (%)', variable= int_rf_thres, value= 1, background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)

    l_rf_threshold_1= tk.Label(label_frame_thres, text= '       tRtF Thres Base (%)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_rf_top_percent = tk.StringVar()
    e_rf_top_percent = tk.Entry(label_frame_thres, width= 8, textvariable= str_rf_top_percent)

    str_rf_base_percent = tk.StringVar()
    e_rf_base_percent = tk.Entry(label_frame_thres, width= 8, textvariable= str_rf_base_percent)

    rb_rf_threshold_2= tk.Radiobutton(label_frame_thres, text= 'tRtF Thres Top (V)', variable= int_rf_thres, value= 2, background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)
    rb_rf_threshold_2.select()

    l_rf_threshold_2= tk.Label(label_frame_thres, text= '       tRtF Thres Base (V)', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11,),)

    str_rf_top = tk.StringVar()
    e_rf_top = tk.Entry(label_frame_thres, width= 8, textvariable= str_rf_top)

    str_rf_base = tk.StringVar()
    e_rf_base = tk.Entry(label_frame_thres, width= 8, textvariable= str_rf_base)

    b_rf_check = tk.Button(label_frame_thres, text= 'RF Thres Check', command= lambda: mxr.RF_threshold(
        rf_top= e_rf_top.get(), rf_base= e_rf_base.get(),
        rf_top_percent= e_rf_top_percent.get(), rf_base_percent= e_rf_base_percent.get(),
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
    # rb_ch_2 = tk.Radiobutton(label_frame_chan, text= 'Chan2 test', variable= int_ch, value= 2)
    # rb_ch_3 = tk.Radiobutton(label_frame_chan, text= 'Chan3 test', variable= int_ch, value= 3)
    rb_ch_delta = tk.Radiobutton(label_frame_chan, text= 'Chan', variable= int_ch, value= 2, background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)
    int_ch_delta_start = tk.IntVar()
    cb_ch_delta_start = ttk.Combobox(label_frame_chan, width= 5, textvariable= int_ch_delta_start, values= [1, 2, 3, 4])
    l_arrow = tk.Label(label_frame_chan, text= '      ↓', background= bg_color_1, fg= '#0D325C', font= ('Calibri', 11, 'bold'),)
    l_ch_delta_stop = tk.Label(label_frame_chan, text= 'Chan', background= bg_color_1, fg= '#0D325C', font= ('Candara', 11, 'bold'),)
    int_ch_delta_stop = tk.IntVar()
    cb_ch_delta_stop = ttk.Combobox(label_frame_chan, width= 5, textvariable= int_ch_delta_stop, values= [1, 2, 3, 4])

    # Save Frame ===================================================================================================================================

    label_frame_save= tk.LabelFrame(window, text= 'Save', background= bg_color_2, fg= '#506376', font= ('Candara', 10, 'bold'),)

    str_image_folder = tk.StringVar()
    e_image_folder = tk.Entry(label_frame_save, width= 50, textvariable= str_image_folder)
    # str_image_folder.set(f'{folder_name}')

    l_image_folder = tk.Label(label_frame_save, text= 'Waveform Scope folder [填Desktop之後的資料夾路徑]', background= bg_color_2, fg= '#0D325C', font= ('Candara', 10,),)

    str_image_pc_folder = tk.StringVar()
    e_image_pc_folder = tk.Entry(label_frame_save, width= 50, textvariable= str_image_pc_folder)
    # str_image_pc_folder.set(r"C:\Users\11102230\Desktop")

    l_image_pc_folder = tk.Label(label_frame_save, text= 'Waveform PC folder [填存在筆電的資料夾路徑]', background= bg_color_2, fg= '#0D325C', font= ('Candara', 10,),)

    str_image = tk.StringVar()
    e_image = tk.Entry(label_frame_save, width= 50, textvariable= str_image)

    l_imagename = tk.Label(label_frame_save, text= '(填 圖檔名)', background= bg_color_2, fg= '#0D325C', font= ('Candara', 10,),)

    b_image_save_scope = tk.Button(label_frame_save, text= 'Save Image-Scope', command= lambda: mxr.save_waveform_scope(folder= str_image_folder.get(), image_name= str_image.get()))
    b_image_save_pc = tk.Button(label_frame_save, text= 'Save Image-PC', command= lambda: mxr.save_waveform_pc(folder= str_image_folder.get(), file_name= str_image.get(), pc_folder= str_image_pc_folder.get()))

    str_WMe_folder = tk.StringVar()
    e_WMe_folder = tk.Entry(label_frame_save, width= 50, textvariable= str_WMe_folder)
    # str_WMe_folder.set(f'{folder_name}/waveform_files')

    l_WMe_folder = tk.Label(label_frame_save, text= 'WMemory Scope folder [填Desktop之後的資料夾路徑]', background= bg_color_2, fg= '#0D325C', font= ('Candara', 10,),)

    str_WMe_pc_folder = tk.StringVar()
    e_WMe_pc_folder = tk.Entry(label_frame_save, width= 50, textvariable= str_WMe_pc_folder)

    l_WMe_pc_folder = tk.Label(label_frame_save, text= 'WMemory PC folder [填存在筆電的資料夾路徑]', background= bg_color_2, fg= '#0D325C', font= ('Candara', 10,),)

    str_WMe = tk.StringVar()
    e_WMe = tk.Entry(label_frame_save, width= 50, textvariable= str_WMe)

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
    e_volt_scale.grid(row= 0, column= 1, padx= 5, pady= 4)
    l_volt_offset.grid(row= 1, column= 0, padx= 5, pady= 4, sticky= 'w') 
    e_volt_offset.grid(row= 1, column= 1, padx= 5, pady= 4)
    b_volt_scale.grid(row= 2, column= 0, padx= 5, pady= 4, sticky= 'e')
    l_trigger_level.grid(row= 3, column= 0, padx= 5, pady= 4, sticky= 'w') 
    e_trigger_level.grid(row= 3, column= 1, padx= 5, pady= 4)
    l_trigger_chan.grid(row= 4, column= 0, padx= 5, pady= 4, sticky= 'w') 
    e_trigger_chan.grid(row= 4, column= 1, padx= 5, pady= 4)
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
    e_gen_top_percent.grid(row= 0, column= 1, sticky= 'w')
    l_gen_threshold_1.grid(row= 1, column= 0, padx= 5, pady= 3)
    e_gen_mid_percent.grid(row= 1, column= 1, sticky= 'w')
    l_gen_threshold_2.grid(row= 2, column= 0, padx= 5, pady= 3)
    e_gen_base_percent.grid(row= 2, column= 1, sticky= 'w')
    rb_gen_threshold_2.grid(row= 3, column= 0, padx= 5, pady= 3) 
    e_gen_top.grid(row= 3, column= 1, sticky= 'w')
    l_gen_threshold_4.grid(row= 4, column= 0, padx= 5, pady= 3) 
    e_gen_mid.grid(row= 4, column= 1, sticky= 'w')
    l_gen_threshold_5.grid(row= 5, column= 0, padx= 5, pady= 3) 
    e_gen_base.grid(row= 5, column= 1, sticky= 'w')
    b_gen_check.grid(row= 0, column= 2, padx= 5, pady= 3, sticky= 'e')
    rb_rf_threshold_1.grid(row= 0, column= 3, padx= 5, pady= 3)
    l_rf_threshold_1.grid(row= 1, column= 3, padx= 5, pady= 3) 
    e_rf_top_percent.grid(row= 0, column= 4, sticky= 'w')
    e_rf_base_percent.grid(row= 1, column= 4, sticky= 'w')
    rb_rf_threshold_2.grid(row= 2, column= 3, padx= 5, pady= 3) 
    l_rf_threshold_2.grid(row= 3, column= 3, padx= 5, pady= 3) 
    e_rf_top.grid(row= 2, column= 4, sticky= 'w')
    e_rf_base.grid(row= 3, column= 4, sticky= 'w')
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
    b_Chan1.grid(row= 0, column= 0, padx= 5, pady= 5, rowspan= 2, columnspan= 2)
    b_Chan2.grid(row= 0, column= 2, padx= 5, pady= 5, rowspan= 2, columnspan= 2)
    b_Chan3.grid(row= 0, column= 4, padx= 5, pady= 5, rowspan= 2, columnspan= 2)
    b_Chan4.grid(row= 0, column= 6, padx= 5, pady= 5, rowspan= 2, columnspan= 2)
    b_WMe1.grid(row= 2, column= 0, padx= 5, pady= 5, rowspan= 2, columnspan= 2)
    b_WMe2.grid(row= 2, column= 2, padx= 5, pady= 5, rowspan= 2, columnspan= 2)
    b_WMe3.grid(row= 2, column= 4, padx= 5, pady= 5, rowspan= 2, columnspan= 2)
    b_WMe4.grid(row= 2, column= 6, padx= 5, pady= 5, rowspan= 2, columnspan= 2)
    rb_ch_single.grid(row= 4, column= 0, sticky= 'e')
    cb_ch_single.grid(row= 4, column= 1, sticky= 'w')
    rb_ch_delta.grid(row= 4, column= 2, sticky= 'e')
    cb_ch_delta_start.grid(row= 4, column= 3, sticky= 'w')
    l_arrow.grid(row= 5, column= 2, sticky= 'e')
    l_ch_delta_stop.grid(row= 6, column= 2, sticky= 'e')
    cb_ch_delta_stop.grid(row= 6, column= 3, sticky= 'w')

    # Save grid
    e_image_folder.grid(row= 0, column= 0, padx= 5, pady= 3)
    l_image_folder.grid(row=0, column= 1, columnspan= 3, sticky= 'w', padx= 5, pady= 3)
    e_image_pc_folder.grid(row= 1, column= 0, padx= 5, pady= 3)
    l_image_pc_folder.grid(row= 1, column= 1, columnspan= 3, sticky= 'w', padx= 5, pady= 3)
    e_image.grid(row= 2, column= 0, padx= 5, pady= 3)
    l_imagename.grid(row= 2, column= 1, sticky= 'w')
    b_image_save_scope.grid(row=2, column= 2, padx= 5, pady= 3, sticky= 'w')
    b_image_save_pc.grid(row= 2, column= 3, sticky= 'w', padx= 5, pady= 3)
    e_WMe_folder.grid(row= 3, column= 0, padx= 5, pady= 3)
    l_WMe_folder.grid(row=3, column= 1, columnspan= 3, sticky= 'w', padx= 5, pady= 3)
    e_WMe_pc_folder.grid(row= 4, column= 0, sticky= 'w', padx= 5, pady= 3, columnspan= 3, )
    l_WMe_pc_folder.grid(row= 4, column= 1, sticky= 'w', padx= 5, pady= 3, columnspan= 3, )

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

    # scope_ids= initialize()
    initialize()

    window.protocol('WM_DELETE_WINDOW', close_window)

    # mxr= MXR(scope_id= str_scope_id.get())
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

