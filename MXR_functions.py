import pyvisa
import time
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog, ttk



class MXR:

    def __init__(self, scope_ip, visa_lib= r'C:\Windows\System32\visa64.dll'):
        rm = pyvisa.ResourceManager(visa_lib)
        # self.inst = rm.open_resource(f'TCPIP0::KEYSIGH-{scope_id}::inst0::INSTR')
        try:
            self.inst = rm.open_resource(f'TCPIP0::{scope_ip}::inst0::INSTR')
            self.inst.timeout = 6000
            idn = self.inst.query('*IDN?').strip()
            print(f'Connect successfully! / {idn}')
            time.sleep(0.1)
            self.inst.write(f':ANALyze:AEDGes 0')
            time.sleep(0.05)
        except:
            warning_root = tk.Tk()
            warning_root.withdraw()  # 隱藏主視窗
            connection_fail = messagebox.showinfo("Error", f"Connection Failed.")
            close_window()
            # sys.exit()

    def acquire_sampling_rate(self, rate): # 科學記號
        self.inst.write(f':ACQuire:SRATe:ANALog {rate}')
        time.sleep(0.05)

    def acquire_memory_depth(self, points_value: int):
        self.inst.write(f':ACQuire:POINts:ANALog {points_value}')
        time.sleep(0.05)

    def add_bookmark(self, choose_type, bookmark, chan):
        if choose_type == 1:
            self.inst.write(f':DISPlay:BOOKmark:DELete:ALL')
            time.sleep(0.05)
            self.add_label(chan= chan, label= bookmark)
            return
        else:
            self.inst.write(f':DISPlay:LABel OFF')
            time.sleep(0.05)
            if bookmark == '':
                self.inst.write(f':DISPlay:BOOKmark{chan}:DELete')

            else:
                display_dict= self.judge_channal_wmemory()    
                try:
                    is_meas_area= self.inst.query(':MEASure:NAME? MEAS1') 
                    time.sleep(0.05)
                except:
                    is_meas_area= 0
                is_marker_area= self.inst.query(':MARKer1:ENABle?') 
                time.sleep(0.05)
                if not is_meas_area == '"no meas"\n' or is_marker_area == '1\n':
                    interval= 5
                else:
                    interval= 3.5
                    
                bookmark_display_list= []
                count= 0
                for cha in display_dict['CHANnel']:
                    if cha == chan:
                        self.inst.write(f':DISPlay:BOOKmark{chan}:DELete')
                        time.sleep(0.05)
                        self.inst.write(f':DISPlay:BOOKmark{chan}:SET NONE,"{bookmark}",CHANnel{chan},"",1')
                        time.sleep(0.05)
                        self.inst.write(f':DISPlay:BOOKmark{chan}:XPOSition {0.01}')
                        time.sleep(0.05)
                        bookmark_display_list.append(count)
                        self.inst.write(f':DISPlay:BOOKmark{chan}:YPOSition {2+interval*count}E-02')
                        time.sleep(0.05)
                    count+=1
                for wme in display_dict['WMEMory']:
                    if wme == chan-4:
                        self.inst.write(f':DISPlay:BOOKmark{chan}:DELete')
                        time.sleep(0.05)
                        self.inst.write(f':DISPlay:BOOKmark{chan}:SET NONE,"{bookmark}",WMEMory{chan-4},"",1')
                        time.sleep(0.05)
                        self.inst.write(f':DISPlay:BOOKmark{chan}:XPOSition {0.01}')
                        time.sleep(0.05)
                        bookmark_display_list.append(count)
                        self.inst.write(f':DISPlay:BOOKmark{chan}:YPOSition {2+interval*count}E-02')
                        time.sleep(0.05)
                    count+=1

    def add_label(self, chan, label):
        display_dict= self.judge_channal_wmemory()
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
                if wme == chan-4:
                    self.inst.write(f':WMEMory{chan-4}:LABel "{label}"')
                    time.sleep(0.05)

    def add_marker(self):
        tuple_marker = (boolvar_marker_1, boolvar_marker_2, boolvar_marker_3, boolvar_marker_4, boolvar_marker_5, boolvar_marker_6, 
                        boolvar_marker_7, boolvar_marker_8, boolvar_marker_9, boolvar_marker_10, boolvar_marker_11, boolvar_marker_12, 
                        )
        
        # ans= self.inst.query(':MARKer2:COLor?')
        # print(ans)
        
        multe_color_list= [
            '#FFFF8A00',  # 橘
            '#FFFFE4C4',  # 膚
            '#FFFFA8BD',  # 粉
            '#FF99DAE8',  # 淡藍
            '#FFC0C0C0',  # 灰
            '#FF8FBC8F'  # 灰綠

            '#FFFF8A00',  # 橘
            '#FFFDF5E6',  # 淡膚
            '#FFFF00FF',  # 亮粉
            '#FF00FFFF',  # 水藍
            '#FFE6E6FA',  # 灰
            '#FFB8FFBA',  # 淡綠
        ]
        single_color_list= [
            '#FFFF8A00',  # 橘
            '#FFFF8A00',  # 橘
            '#FFFF8A00',  # 橘
            '#FFFF8A00',  # 橘
            '#FFFF8A00',  # 橘
            '#FFFF8A00'  # 橘

            '#FFFF8A00',  # 橘
            '#FFFF8A00',  # 橘
            '#FFFF8A00',  # 橘
            "#FFFF8A00",  # 橘
            '#FFFF8A00',  # 橘
            '#FFFF8A00',  # 橘
        ]

        if boolvar_marker_color.get() == True:
            color_list= multe_color_list
        else:
            color_list= single_color_list

        for i, boolvar in enumerate(tuple_marker):
            self.inst.write(f':MARKer:MEASurement:MEASurement MEAS{i+1},OFF')
            time.sleep(0.05)

        c=0
        for i, boolvar in enumerate(tuple_marker):
            if boolvar.get():
                self.inst.write(f"SYSTem:CONTrol 'MeasSetupSrc1EdgeByRef -{i+1} on'")
                time.sleep(0.05)
                self.inst.write(f"SYSTem:CONTrol 'DoMeas -{i+1}'")
                time.sleep(0.05)
                self.inst.write(f':MARKer:MEASurement:MEASurement MEAS{i+1},ON')
                time.sleep(0.05)
                self.inst.write(f':MARKer{2*c+1}:COLor "{color_list[c]}"')
                time.sleep(0.05)
                self.inst.write(f':MARKer{2*c+2}:COLor "{color_list[c]}"')
                time.sleep(0.05)
                c+=1

    def autoscale(self):
        self.inst.write(':AUToscale')
        time.sleep(0.05)

    def call_measurement_delta_time(self, edge_1, num_1, pos_1, edge_2, num_2, pos_2, chan, chan_start, chan_stop, modify_name, timing_name):
        displayed_dict= self.judge_channal_wmemory()
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
            
            if modify_name:
                if 'CHAN' in res_start and 'CHAN' in res_stop:
                    self.inst.write(f':MEASure:NAME MEAS1,"{timing_name}({chan_start}-{chan_stop})"')
                    time.sleep(0.05)
                elif 'CHAN' in res_start and 'WMEM' in res_stop:
                    self.inst.write(f':MEASure:NAME MEAS1,"{timing_name}({chan_start}-m{chan_stop})"')
                    time.sleep(0.05)
                elif 'WMEM' in res_start and 'CHAN' in res_stop:
                    self.inst.write(f':MEASure:NAME MEAS1,"{timing_name}(m{chan_start}-{chan_stop})"')
                    time.sleep(0.05)
                else:
                    self.inst.write(f':MEASure:NAME MEAS1,"{timing_name}(m{chan_start}-m{chan_stop})"')
                    time.sleep(0.05)
            
        else:
            pass

    def call_measurement_dutycycle(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:DUTYcycle CHANnel{}',
            'WMEMory': ':MEASure:DUTYcycle WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)

    def call_measurement_frequency(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:FREQuency CHANnel{}',
            'WMEMory': ':MEASure:FREQuency WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)

    def call_measurement_function(self, chan, command_templates: dict):
        display_dict= self.judge_channal_wmemory()
        for key in command_templates:
            if chan in display_dict[key]:
                self.inst.write(command_templates[key].format(chan))
                time.sleep(0.05)            
    
    def call_measurement_NCJitter(self, chan, direction):
        display_dict= self.judge_channal_wmemory()
        for cha in display_dict['CHANnel']:
            if cha == chan:
                self.inst.write(f':MEASure:NCJitter CHANnel{cha},{direction},1,1')
                time.sleep(0.05)
        for wme in display_dict['WMEMory']:
            if wme == chan:
                self.inst.write(f':MEASure:NCJitter WMEMory{cha},{direction},1,1')
                time.sleep(0.05)

    def call_measurement_period(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:PERiod CHANnel{}',
            'WMEMory': ':MEASure:PERiod WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)

    def call_measurement_slewrate(self, chan, direction):
        display_dict= self.judge_channal_wmemory()
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

    def call_measurement_tH(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:PWIDth CHANnel{}',
            'WMEMory': ':MEASure:PWIDth WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)  

    def call_measurement_tL(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:NWIDth CHANnel{}',
            'WMEMory': ':MEASure:NWIDth WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)  

    def call_measurement_tR(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:RISetime CHANnel{}',
            'WMEMory': ':MEASure:RISetime WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)              

    def call_measurement_tF(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:FALLtime CHANnel{}',
            'WMEMory': ':MEASure:FALLtime WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)              

    def call_measurement_VIH(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:VTOP CHANnel{}',
            'WMEMory': ':MEASure:VTOP WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)              

    def call_measurement_VIL(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:VBASe CHANnel{}',
            'WMEMory': ':MEASure:VBASe WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)              

    def call_measurement_VPP(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:VPP CHANnel{}',
            'WMEMory': ':MEASure:VPP WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)   

    def call_measurement_VMAX(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:VMAX CHANnel{}',
            'WMEMory': ':MEASure:VMAX WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)   
        
    def call_measurement_VMIN(self, chan):
        command_templates = {
            'CHANnel': ':MEASure:VMIN CHANnel{}',
            'WMEMory': ':MEASure:VMIN WMEMory{}'
        }            
        self.call_measurement_function(chan= chan, command_templates= command_templates)   
        
    def check_intensity_setting(self, intensity_value):
        self.inst.write(f'SYSTem:CONTrol "WaveformBrt -1 {intensity_value}"')
        time.sleep(0.05)

    def check_timebase_offset(self, position): # 科學記號
        self.inst.write(f':TIMebase:POSition {position}')
        time.sleep(0.05)

    def check_timebase_scale(self, scale): # 科學記號
        self.inst.write(f':TIMebase:SCALe {scale}')
        time.sleep(0.05)

    def check_trigger_setting(self, chan, level):
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

    def check_voltage(self, scale, offset): # 科學記號
        display_dict= self.judge_channal_wmemory()
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

    def clear_diaplay(self):
        self.inst.write(':CDISplay')
        time.sleep(0.05)

    def clear_wmemory(self, chan, string):
        self.inst.write(f':WMEMory{chan}:CLEar')
        time.sleep(0.05)
        string.set('')

    def default(self):
        self.inst.write(':SYSTem:PRESet DEFault')
        time.sleep(0.05)

    def delete_bookmark(self, chan, choose_type):
        if choose_type == 1:
            self.inst.write(f':DISPlay:LABel OFF')
            time.sleep(0.05)
        else:
            self.inst.write(f':DISPlay:BOOKmark{chan}:DELete')
            time.sleep(0.05)

    def display_channel(self, chan, bookmark, choose_type):
        res= self.inst.query(f':CHANnel{chan}:DISPlay?')
        time.sleep(0.05)
        if res == '1\n':
            self.inst.write(f':CHANnel{chan}:DISPlay OFF')
            time.sleep(0.05)
            try:
                self.inst.write(f':DISPlay:BOOKmark{chan}:DELete')
                time.sleep(0.05)
            except:
                pass
        else:
            self.inst.write(f':CHANnel{chan}:DISPlay ON')
            time.sleep(0.05)
            self.add_bookmark(choose_type= choose_type,bookmark= bookmark, chan= chan)

    def delete_marker(self):
        tuple_marker = (boolvar_marker_1, boolvar_marker_2, boolvar_marker_3, boolvar_marker_4, boolvar_marker_5, boolvar_marker_6, 
                        boolvar_marker_7, boolvar_marker_8, boolvar_marker_9, boolvar_marker_10, boolvar_marker_11, boolvar_marker_12, 
                        )
    
        for i, boolvar in enumerate(tuple_marker):
            if boolvar.get():
                self.inst.write(f':MARKer:MEASurement:MEASurement MEASurement{i+1},OFF')
                time.sleep(0.05)

    def delete_measurement(self):
        tuple_marker = (boolvar_marker_1, boolvar_marker_2, boolvar_marker_3, boolvar_marker_4, boolvar_marker_5, boolvar_marker_6, 
                        boolvar_marker_7, boolvar_marker_8, boolvar_marker_9, boolvar_marker_10, boolvar_marker_11, boolvar_marker_12, 
                        )
        for i, boolvar in enumerate(tuple_marker):
            if boolvar.get():
                self.inst.write(f'MEASurement{i+1}:CLEar')
                time.sleep(0.05)

    def display_wmemory(self, chan, bookmark, choose_type):
        res= self.inst.query(f':WMEMory{chan}:DISPlay?')
        time.sleep(0.05)
        if res == '1\n':
            self.inst.write(f':WMEMory{chan}:DISPlay OFF')
            time.sleep(0.05)
            try:
                self.inst.write(f':DISPlay:BOOKmark{chan+4}:DELete')
                time.sleep(0.05)
            except:
                pass
        else:
            self.inst.write(f':WMEMory{chan}:DISPlay ON')
            time.sleep(0.05)
            self.add_bookmark(choose_type= choose_type, bookmark= bookmark, chan= chan+4)
    
    def extract_result(self):
        meas_name= ['', '', '', '', '', '', '', '', '', '', '', '']
        result1= ['', '', '', '', '', '', '', '', '', '', '', '']
        result2= ['', '', '', '', '', '', '', '', '', '', '', '']
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
            
            if intvar_result_type.get() == 1:  # 選擇Mean Value
                if divmod(index, 7)[1] == 4:
                    if measurement_type == 0:
                        final_result_1= self.judge_unit_voltage(value= value)
                        final_result_2= ''
                    elif measurement_type == 1:
                        slew= False
                        final_result_1= self.judge_unit_time(value= value, slew= slew)
                        final_result_2= ''
                    elif measurement_type == 2:
                        slew= True
                        final_result_1= self.judge_unit_time(value= value, slew= slew)
                        final_result_2= ''
                    elif measurement_type == 3:
                        final_result_1= self.judge_unit_frequency(value= value)
                        final_result_2= ''
                    elif measurement_type == 4:
                        final_result_1 = f"{float(value):.3f}"+' %'
                        final_result_2= ''

                    try:
                        result1[divmod(index, 7)[0]]= final_result_1
                        result2[divmod(index, 7)[0]]= final_result_2
                    except:
                        continue

            elif intvar_result_type.get() == 2:  # 選擇Min & Max Value
                if divmod(index, 7)[1] == 2:
                    if measurement_type == 0:
                        final_result_1= self.judge_unit_voltage(value= value)
                    elif measurement_type == 1:
                        slew= False
                        final_result_1= self.judge_unit_time(value= value, slew= slew)
                    elif measurement_type == 2:
                        slew= True
                        final_result_1= self.judge_unit_time(value= value, slew= slew)
                    elif measurement_type == 3:
                        final_result_1= self.judge_unit_frequency(value= value)
                    elif measurement_type == 4:
                        final_result_1 = f"{float(value):.3f}"+' %'

                    try:
                        result1[divmod(index, 7)[0]]= final_result_1
                    except:
                        continue

                if divmod(index, 7)[1] == 3:
                    if measurement_type == 0:
                        final_result_2= self.judge_unit_voltage(value= value)
                    elif measurement_type == 1:
                        slew= False
                        final_result_2= self.judge_unit_time(value= value, slew= slew)
                    elif measurement_type == 2:
                        slew= True
                        final_result_2= self.judge_unit_time(value= value, slew= slew)
                    elif measurement_type == 3:
                        final_result_2= self.judge_unit_frequency(value= value)
                    elif measurement_type == 4:
                        final_result_2 = f"{float(value):.3f}"+' %'

                    try:
                        result2[divmod(index, 7)[0]]= final_result_2
                    except:
                        continue

        label_measurement_name_1.config(text=f'{meas_name[0]}')
        text_result_mean_1.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_1.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_1.insert(tk.END, f"{result1[0]}")
        text_result_mean_1.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_1.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_1.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_1.insert(tk.END, f"{result2[0]}")
        text_result_minmax_1.config(state=tk.DISABLED)  # 設置為只讀狀態

        label_measurement_name_2.config(text=f'{meas_name[1]}')
        text_result_mean_2.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_2.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_2.insert(tk.END, f"{result1[1]}")
        text_result_mean_2.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_2.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_2.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_2.insert(tk.END, f"{result2[1]}")
        text_result_minmax_2.config(state=tk.DISABLED)  # 設置為只讀狀態
        
        label_measurement_name_3.config(text=f'{meas_name[2]}')
        text_result_mean_3.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_3.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_3.insert(tk.END, f"{result1[2]}")
        text_result_mean_3.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_3.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_3.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_3.insert(tk.END, f"{result2[2]}")
        text_result_minmax_3.config(state=tk.DISABLED)  # 設置為只讀狀態
        
        label_measurement_name_4.config(text=f'{meas_name[3]}')
        text_result_mean_4.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_4.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_4.insert(tk.END, f"{result1[3]}")
        text_result_mean_4.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_4.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_4.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_4.insert(tk.END, f"{result2[3]}")
        text_result_minmax_4.config(state=tk.DISABLED)  # 設置為只讀狀態
        
        label_measurement_name_5.config(text=f'{meas_name[4]}')
        text_result_mean_5.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_5.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_5.insert(tk.END, f"{result1[4]}")
        text_result_mean_5.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_5.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_5.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_5.insert(tk.END, f"{result2[4]}")
        text_result_minmax_5.config(state=tk.DISABLED)  # 設置為只讀狀態
        
        label_measurement_name_6.config(text=f'{meas_name[5]}')
        text_result_mean_6.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_6.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_6.insert(tk.END, f"{result1[5]}")
        text_result_mean_6.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_6.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_6.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_6.insert(tk.END, f"{result2[5]}")
        text_result_minmax_6.config(state=tk.DISABLED)  # 設置為只讀狀態
        
        label_measurement_name_7.config(text=f'{meas_name[6]}')
        text_result_mean_7.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_7.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_7.insert(tk.END, f"{result1[6]}")
        text_result_mean_7.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_7.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_7.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_7.insert(tk.END, f"{result2[6]}")
        text_result_minmax_7.config(state=tk.DISABLED)  # 設置為只讀狀態
        
        label_measurement_name_8.config(text=f'{meas_name[7]}')
        text_result_mean_8.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_8.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_8.insert(tk.END, f"{result1[7]}")
        text_result_mean_8.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_8.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_8.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_8.insert(tk.END, f"{result2[7]}")
        text_result_minmax_8.config(state=tk.DISABLED)  # 設置為只讀狀態
        
        label_measurement_name_9.config(text=f'{meas_name[8]}')
        text_result_mean_9.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_9.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_9.insert(tk.END, f"{result1[8]}")
        text_result_mean_9.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_9.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_9.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_9.insert(tk.END, f"{result2[8]}")
        text_result_minmax_9.config(state=tk.DISABLED)  # 設置為只讀狀態
        
        label_measurement_name_10.config(text=f'{meas_name[9]}')
        text_result_mean_10.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_10.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_10.insert(tk.END, f"{result1[9]}")
        text_result_mean_10.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_10.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_10.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_10.insert(tk.END, f"{result2[9]}")
        text_result_minmax_10.config(state=tk.DISABLED)  # 設置為只讀狀態
        
        label_measurement_name_11.config(text=f'{meas_name[10]}')
        text_result_mean_11.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_11.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_11.insert(tk.END, f"{result1[10]}")
        text_result_mean_11.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_11.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_11.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_11.insert(tk.END, f"{result2[10]}")
        text_result_minmax_11.config(state=tk.DISABLED)  # 設置為只讀狀態
        
        label_measurement_name_12.config(text=f'{meas_name[11]}')
        text_result_mean_12.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_mean_12.delete(1.0, tk.END)  # 清空當前內容
        text_result_mean_12.insert(tk.END, f"{result1[11]}")
        text_result_mean_12.config(state=tk.DISABLED)  # 設置為只讀狀態
        text_result_minmax_12.config(state=tk.NORMAL)  # 先啟用Text小部件的編輯狀態
        text_result_minmax_12.delete(1.0, tk.END)  # 清空當前內容
        text_result_minmax_12.insert(tk.END, f"{result2[11]}")
        text_result_minmax_12.config(state=tk.DISABLED)  # 設置為只讀狀態
        
    def judge_channal_wmemory(self):
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

    def judge_unit_frequency(self, value):
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

    def judge_unit_time(self, value, slew):
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
            elif exponent == 12:
                return f"{base} V/ps"
            elif exponent == 13:
                return f"{base * 10} V/ps"
            elif exponent == 14:
                return f"{base * 100} V/ps"
            elif exponent == 15:
                return f"{base} V/fs"
            elif exponent == 16:
                return f"{base * 10} V/fs"
            elif exponent == 17:
                return f"{base * 100} V/fs"
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
            elif exponent == -15:
                return f"{base} fs"
            elif exponent == -14:
                return f"{base * 10} fs"
            elif exponent == -13:
                return f"{base * 100} fs"
            else:
                # 如果指數不在指定的範圍内，返回原始字串
                return f'{base} s'
            
    def judge_unit_voltage(self, value):
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

    def load_setup(self, folder, scope_segment, setup_name, choose_type, file_path_choice, g_top, g_middle, g_base, g_top_percent, g_middle_percent, g_base_percent, rf_top, rf_base, rf_top_percent, rf_base_percent):
        
        if file_path_choice == 2: # Server
            
            if strvar_setupfile_interface.get() == 'User':
                total_folder_path = folder
            elif strvar_setupfile_interface.get() == '':
                total_folder_path = folder
            else: 
                total_folder_path = f'{scope_segment}:/#_Eric Team/02_Penny/Setup_Files_Collection/{strvar_setupfile_interface.get()}/{strvar_setupfile_class.get()}'

        else: # Desktop
            total_folder_path = f"C:/Users/Administrator/Desktop/{folder}"

        # 記錄示波器timebase設定
        time_position= self.inst.query(':TIMebase:POSition?').rstrip('\n')
        time.sleep(0.05)
        time_scale= self.inst.query(':TIMebase:SCALe?').rstrip('\n')
        time.sleep(0.05)

        # 記錄示波器voltage設定
        temp_voltscale_dict= {}
        temp_voltoffset_dict= {}
        display_dict= self.judge_channal_wmemory()
        for chan in display_dict['CHANnel']:
            volt_scale= self.inst.query(f':CHANnel{chan}:SCALe?')
            time.sleep(0.05)
            temp_voltscale_dict[chan]= volt_scale
            volt_offset= self.inst.query(f':CHANnel{chan}:OFFSet?')
            time.sleep(0.05)
            temp_voltoffset_dict[chan]= volt_offset
        for wme in display_dict['WMEMory']:
            volt_scale= self.inst.query(f':WMEMory{wme}:YRANge?').rstrip('\n')
            time.sleep(0.05)
            temp_voltscale_dict[wme]= float(volt_scale)/8
            volt_offset= self.inst.query(f':WMEMory{wme}:YOFFset?').rstrip('\n')
            time.sleep(0.05)
            temp_voltoffset_dict[wme]= volt_offset

        # 記錄示波器trigger設定
        trig_chan= self.inst.query(f':TRIGger:EDGE:SOURce?').rstrip('\n')
        time.sleep(0.05)
        trig_chan= trig_chan.lstrip("CHAN")
        trig_level= self.inst.query(f':TRIGger:LEVel? CHANnel{trig_chan}').rstrip('\n')
        time.sleep(0.05)

        # 呼叫設定檔
        self.inst.write(f':DISK:LOAD "{total_folder_path}/{setup_name}.set"')
        time.sleep(0.05)

        # 依據勾選狀態修改數值
        if boolvar_setup_timebase.get() == True:
            # 依照示波器畫面的timebase
            self.check_timebase_scale(scale= time_scale)
            self.check_timebase_offset(position= time_position)
        if boolvar_setup_volt.get() == True:
            display_dict= self.judge_channal_wmemory()
            # 依照示波器畫面的Voltage
            for chan in display_dict['CHANnel']:
                self.inst.write(f':CHANnel{chan}:SCALe {temp_voltscale_dict[chan]}')
                time.sleep(0.05)
                self.inst.write(f':CHANnel{chan}:OFFSet {temp_voltoffset_dict[chan]}')
                time.sleep(0.05)
            for wme in display_dict['WMEMory']:
                self.inst.write(f':WMEMory{wme}:YRANge {float(temp_voltscale_dict[wme])*8}')
                time.sleep(0.05)
                self.inst.write(f':WMEMory{wme}:YOFFset {temp_voltoffset_dict[wme]}')
                time.sleep(0.05)

            # 依照示波器畫面的trigger
            res= self.inst.query(f':CHANnel{trig_chan}:DISPlay?')
            time.sleep(0.05)
            if not res == '1\n':
                self.inst.write(f':CHANnel{trig_chan}:DISPlay ON')
                time.sleep(0.05)
            self.inst.write(f':TRIGger:EDGE:SOURce CHANnel{trig_chan}')
            time.sleep(0.05)
            self.inst.write(f':TRIGger:LEVel CHANnel{trig_chan},{trig_level}')
            time.sleep(0.05)
            if not res == '1\n':
                self.inst.write(f':CHANnel{trig_chan}:DISPlay OFF')
                time.sleep(0.05)

            # self.volt_check(scale= volt_scale, offset= volt_offset)
            # self.trig_check(chan= trig_chan, level= trig_level)
            
            # 依照GUI的threshold
            self.set_general_threshold(g_top= g_top, g_middle= g_middle, g_base= g_base, g_top_percent= g_top_percent, g_middle_percent= g_middle_percent, g_base_percent= g_base_percent)
            self.set_risefall_threshold(rf_top= rf_top, rf_base= rf_base, rf_top_percent= rf_top_percent, rf_base_percent= rf_base_percent)

        if boolvar_setup_label.get() == True:
            # 依照GUI的label
            label_content = [
                strvar_label_1, strvar_label_2, strvar_label_3, strvar_label_4, 
                strvar_label_5, strvar_label_6, strvar_label_7, strvar_label_8, 
                ]
            for i in range(8):
                self.add_bookmark(choose_type= choose_type, bookmark= label_content[i].get().rstrip('\n'), chan= i+1)

    def load_wmemory(self, chan, folder, wme_name, file_path_choice):
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
        
        if file_path_choice == 2:
            total_folder_path = folder
        else:
            total_folder_path = f"C:/Users/Administrator/Desktop/{folder}"

        self.inst.write(f':DISK:LOAD "{total_folder_path}/{wme_name}.h5",WMEMory{chan},OFF')
        time.sleep(0.05)

    def measure_all_edge(self):
        ans= self.inst.query(':ANALyze:AEDGes?')
        time.sleep(0.05)
        if ans == '0\n':
            button_measure_all_edge['text'] = "Meas All Edge: ON"
            self.inst.write(f':ANALyze:AEDGes 1')
            time.sleep(0.05)
        else:
            button_measure_all_edge['text'] = "Meas All Edge: OFF"
            self.inst.write(f':ANALyze:AEDGes 0')
            time.sleep(0.05)
    
    def run(self):
        self.inst.write(':RUN')
        time.sleep(0.05)

    def save_pc_image(self, pc_folder, file_name):
        screen_data = np.array(self.inst.query_binary_values(":DISPlay:DATA? PNG", datatype = 's', container = bytes))
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
        temp_img_name= ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        temp_folder= fr'{os.path.dirname(__file__)}/Temp'
        if not os.path.exists(temp_folder):
            os.mkdir(temp_folder) 
            
        f_img = open(f"{temp_folder}/{temp_img_name}.png", "wb")
        f_img.write(bytearray(screen_data))
        f_img.close()

        rgba_to_rgb_composite(f"{temp_folder}/{temp_img_name}.png", f"{pc_folder}/{file_name}.png", background=(0,0,0))

    def save_pc_waveform(self, folder, pc_folder, file_name):            

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

    def save_pc_wmemory(self, folder, pc_folder, file_name, ext_type):
        if ext_type == 1:
            ext = 'h5'
        else:
            ext = 'set'

        full_path = f"C:/Users/Administrator/Desktop/{folder}/{file_name}.{ext}"
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

        if os.path.exists(f"{pc_folder}/{file_name}.{ext}"):
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
        
        with open(f"{pc_folder}/{file_name}.{ext}", 'wb') as f:
            f.write(data)

    def save_scope_file(self, chan, folder, current_file_name, ext_type, path_choice):
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

        if path_choice == 2:
            folder_total_path = folder
        else:
            folder_total_path = f"C:/Users/Administrator/Desktop/{folder}"

        # 資料夾是否存在
        self.inst.query(f':DISK:DIRectory? "{folder_total_path}"')
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
            folder_total_path= folder_total_path.replace("/", "\\")
            # print(folder_total_path)
            split_folder_list= folder_total_path.split('\\')

            folder= split_folder_list[0]
            for split in split_folder_list[1:]:
                folder= f'{folder}\\{split}'
                self.inst.query(f':DISK:DIRectory? "{folder}"')
                time.sleep(0.05)
                response= self.inst.query(f':SYSTem:ERRor?')
                time.sleep(0.05)
                # print(response)
                if response == '-256\n' or response == '113\n' or response == '-257\n':
                    self.inst.write(f':DISK:MDIRectory "{folder}"')
                    time.sleep(0.05)

        # 資料夾全部內容
        folder_content= self.inst.query(f':DISK:DIRectory? "{folder_total_path}"')
        time.sleep(0.05)

        # 判斷存.h5或.set
        if ext_type == 1:
            # 使用正則表達式來匹配所有 .h5 檔案名稱
            files = re.findall(r'\b[\w-]+\.(?:h5)\b', folder_content)
            ext= 'h5'
            command= f':DISK:SAVE:WAVeform CHANnel{chan},"{folder_total_path}/{current_file_name}",H5,OFF'
        else:
            # 使用正則表達式來匹配所有 .set 檔案名稱
            files = re.findall(r'\b[\w-]+\.(?:set)\b', folder_content)
            ext= 'set'
            command= f':DISK:SAVE:SETup "{folder_total_path}/{current_file_name}"'

        for file_name in files:
            if f'{current_file_name}.{ext}' == file_name:
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

        self.inst.write(command)
        time.sleep(0.05)

    def save_scope_image(self, folder, image_name, path_choice):
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

        if path_choice == 2:
            folder_total_path = folder
        else:
            folder_total_path = f"C:/Users/Administrator/Desktop/{folder}"

        # 資料夾是否存在
        self.inst.query(f':DISK:DIRectory? "{folder_total_path}"')
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
            folder_total_path= folder_total_path.replace("/", "\\")
            # print(folder_total_path)

            split_folder_list= folder_total_path.split('\\')

            folder= split_folder_list[0]
            for split in split_folder_list[1:]:
                folder= f'{folder}\\{split}'
                self.inst.query(f':DISK:DIRectory? "{folder}"')
                time.sleep(0.05)
                response= self.inst.query(f':SYSTem:ERRor?')
                time.sleep(0.05)
                # print(response)
                if response == '-256\n' or response == '113\n' or response == '-257\n':
                    self.inst.write(f':DISK:MDIRectory "{folder}"')
                    time.sleep(0.05)

        # 資料夾全部內容
        folder_content= self.inst.query(f':DISK:DIRectory? "{folder_total_path}"')
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

        self.inst.write(f':DISK:SAVE:IMAGe "{folder_total_path}/{image_name}",PNG,SCReen,OFF,NORMal,OFF')
        time.sleep(0.05)

    def set_general_threshold(self, g_top, g_middle, g_base, g_top_percent, g_middle_percent, g_base_percent):
        if intvar_general_threshold.get() == 1:
            do_the_judge= False
            if float(g_top_percent) <= float(g_middle_percent):
                g_top_percent= Decimal(g_middle_percent) + Decimal('0.1')
                combobox_general_percent_top.config(foreground= 'red')
                combobox_general_percent_middle.config(foreground= 'red')
                do_the_judge= True
            if float(g_middle_percent) <= float(g_base_percent):
                g_base_percent= Decimal(g_middle_percent) - Decimal('0.1')
                combobox_general_percent_base.config(foreground= 'red')
                combobox_general_percent_middle.config(foreground= 'red')
                do_the_judge= True
            if not do_the_judge:
                combobox_general_percent_top.config(foreground= 'black')
                combobox_general_percent_middle.config(foreground= 'black')
                combobox_general_percent_base.config(foreground= 'black')

            self.inst.write(f':MEASure:THResholds:GENeral:METHod ALL,PERCent')
            time.sleep(0.05)
            self.inst.write(f':MEASure:THResholds:GENeral:PERCent ALL,{g_top_percent},{g_middle_percent},{g_base_percent}')
            time.sleep(0.05)
        elif intvar_general_threshold.get() == 2:
            do_the_judge= False
            if float(g_top) <= float(g_middle):
                g_top= Decimal(g_middle) + Decimal('0.01')
                combobox_general_value_top.config(foreground= 'red')
                combobox_general_value_middle.config(foreground= 'red')
                do_the_judge= True
            if float(g_middle) <= float(g_base):
                g_base= Decimal(g_middle) - Decimal('0.01')
                combobox_general_value_base.config(foreground= 'red')
                combobox_general_value_middle.config(foreground= 'red')
                do_the_judge= True
            if not do_the_judge:
                combobox_general_value_top.config(foreground= 'black')
                combobox_general_value_middle.config(foreground= 'black')
                combobox_general_value_base.config(foreground= 'black')

            self.inst.write(f':MEASure:THResholds:GENeral:METHod ALL,ABSolute')
            time.sleep(0.05)
            self.inst.write(f':MEASure:THResholds:GENeral:ABSolute ALL,{g_top},{g_middle},{g_base}')
            time.sleep(0.05)

    def set_risefall_threshold(self, rf_top, rf_base, rf_top_percent, rf_base_percent):
        if intvar_risefall_threshold.get() == 1:
            self.inst.write(f':MEASure:THResholds:RFALl:METHod ALL,PERCent')
            time.sleep(0.05)
            self.inst.write(f':MEASure:THResholds:RFALl:PERCent ALL,{rf_top_percent},{(float(rf_top_percent)+float(rf_base_percent))/2},{rf_base_percent}')
            time.sleep(0.05)
        elif intvar_risefall_threshold.get() == 2:
            self.inst.write(f':MEASure:THResholds:RFALl:METHod ALL,ABSolute')
            time.sleep(0.05)
            self.inst.write(f':MEASure:THResholds:RFALl:ABSolute ALL,{rf_top},{(float(rf_top)+float(rf_base))/2},{rf_base}')
            time.sleep(0.05)

    def set_trigger_type(self):
        res= self.inst.query(f':TRIGger:SWEep?')
        time.sleep(0.05)
        if res == 'AUTO\n':
            self.inst.write(':TRIGger:SWEep TRIGgered')
            time.sleep(0.05)
        else:
            self.inst.write(':TRIGger:SWEep AUTO')
            time.sleep(0.05)

    def set_trigger_slope(self):
        res= self.inst.query(f':TRIGger:EDGE:SLOPe?')
        time.sleep(0.05)
        if res == 'POS\n':
            self.inst.write(':TRIGger:EDGE:SLOPe NEGative')
            time.sleep(0.05)
        else:
            self.inst.write(':TRIGger:EDGE:SLOPe POSitive')
            time.sleep(0.05)
    
    def single(self):
        self.inst.write(':SINGLE')
        time.sleep(0.05)

    def stop(self):
        self.inst.write(':STOP')
        time.sleep(0.05)

