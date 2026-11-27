import pyvisa
import time
from decimal import Decimal
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog, ttk
import numpy as np
import os
import re
import random
import string
import utils


class MXR:

    def __init__(self, scope_ip, visa_lib= r'C:\Windows\System32\visa64.dll'):
        rm = pyvisa.ResourceManager(visa_lib)
        try:
            self.inst = rm.open_resource(f'TCPIP0::{scope_ip}::inst0::INSTR')
            self.inst.timeout = 6000
            idn = self.inst.query('*IDN?').strip()
            print(f'Connect successfully! / {idn}')
            time.sleep(0.1)
            self.inst.write(f':ANALyze:AEDGes 0')
            time.sleep(0.05)

        except Exception as e:
            raise ConnectionError(
                f'無法連接儀器 {scope_ip}: {e}'
            ) from e      
              
        # except:
        #     warning_root = tk.Tk()
        #     warning_root.withdraw()  # 隱藏主視窗
        #     connection_fail = messagebox.showinfo("Error", f"Connection Failed.")
        #     close_window()
        #     # sys.exit()

    def acquire_sampling_rate(self, sampling_rate: str): # 科學記號
        self.inst.write(f':ACQuire:SRATe:ANALog {sampling_rate}')
        time.sleep(0.05)

    def acquire_memory_depth(self, points_value: int):
        self.inst.write(f':ACQuire:POINts:ANALog {points_value}')
        time.sleep(0.05)

    def add_labelname(self, label_type: int, channel: int, content: str):
        
        display_dict= self.judge_channal_wmemory()
        
        if label_type == 0: # label
            self.inst.write(f':DISPlay:LABel ON')
            time.sleep(0.05)
            for cha in display_dict['CHANnel']:
                if channel == cha:
                    if content == '':
                        self.inst.write(f':CHANnel{channel}:LABel "{channel}"')
                    else:    
                        self.inst.write(f':CHANnel{channel}:LABel "{content}"')
                    time.sleep(0.05)
            for wme in display_dict['WMEMory']:
                if wme == channel-4:
                    if content == '':
                        self.inst.write(f':WMEMory{channel-4}:LABel "m{channel-4}"')
                    else:    
                        self.inst.write(f':WMEMory{channel-4}:LABel "{content}"')
                    time.sleep(0.05)

            self.inst.write(f':DISPlay:BOOKmark:DELete:ALL')
            time.sleep(0.05)

        elif label_type == 1: # bookmark
            interval= 5
            count= 0
            for cha in display_dict['CHANnel']:
                if cha == channel:
                    self.inst.write(f':DISPlay:BOOKmark{channel}:DELete')
                    time.sleep(0.05)
                    if content == '':
                        self.inst.write(f':DISPlay:BOOKmark{channel}:DELete')
                    else:
                        self.inst.write(f':DISPlay:BOOKmark{channel}:SET NONE,"{content}",CHANnel{channel},"",1')
                    time.sleep(0.05)
                    self.inst.write(f':DISPlay:BOOKmark{channel}:XPOSition {0.01}')
                    time.sleep(0.05)
                    self.inst.write(f':DISPlay:BOOKmark{channel}:YPOSition {2+interval*count}E-02')
                    time.sleep(0.05)
                count+=1
            for wme in display_dict['WMEMory']:
                if wme == channel-4:
                    self.inst.write(f':DISPlay:BOOKmark{channel}:DELete')
                    time.sleep(0.05)
                    if content == '':
                        self.inst.write(f':DISPlay:BOOKmark{channel}:DELete')
                    else:
                        self.inst.write(f':DISPlay:BOOKmark{channel}:SET NONE,"{content}",WMEMory{channel-4},"",1')
                    time.sleep(0.05)
                    self.inst.write(f':DISPlay:BOOKmark{channel}:XPOSition {0.01}')
                    time.sleep(0.05)
                    self.inst.write(f':DISPlay:BOOKmark{channel}:YPOSition {2+interval*count}E-02')
                    time.sleep(0.05)
                count+=1    
    
            self.inst.write(f':DISPlay:LABel OFF')
            time.sleep(0.05)
            
    def add_marker(self, is_multi_colors: bool, tuple_measurement_index: tuple):

        # ans= self.inst.query(':MARKer2:COLor?')
        # print(ans)
        
        multe_color_list= [
            '#FFFF8A00',  # 橘
            '#FFFFE4C4',  # 膚
            '#FFFFA8BD',  # 粉
            '#FF99DAE8',  # 淡藍
            '#FFC0C0C0',  # 灰
            '#FF8FBC8F',  # 灰綠

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
            '#FFFF8A00',  # 橘

            '#FFFF8A00',  # 橘
            '#FFFF8A00',  # 橘
            '#FFFF8A00',  # 橘
            "#FFFF8A00",  # 橘
            '#FFFF8A00',  # 橘
            '#FFFF8A00',  # 橘
        ]

        if is_multi_colors == True:
            color_list= multe_color_list
        else:
            color_list= single_color_list

        for i, boolvar in enumerate(tuple_measurement_index):
            self.inst.write(f':MARKer:MEASurement:MEASurement MEAS{i+1},OFF')
            time.sleep(0.05)

        c=0
        for i, boolvar in enumerate(tuple_measurement_index):
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

    def call_measurement_delta_time(self, is_double_channel: int, delta_start: dict, delta_stop: dict, is_modify_name: bool, timing_name: str):
        displayed_dict= self.judge_channal_wmemory()
        for format in displayed_dict:
            for channel in displayed_dict[format]:
                if channel == delta_start['channel']:
                    res_start= f'{format}'
                if channel == delta_stop['channel']:
                    res_stop= f'{format}'

        if is_double_channel == 2:
            self.inst.write(f":MEASure:DELTatime:DEFine {delta_start['transition']},{delta_start['number']},{delta_start['position']},{delta_stop['transition']},{delta_stop['number']},{delta_stop['position']}")
            time.sleep(0.05)
            self.inst.write(f":MEASure:DELTatime {res_start}{delta_start['channel']}, {res_stop}{delta_stop['channel']}")
            time.sleep(0.05)
            
            if is_modify_name:
                if 'CHAN' in res_start and 'CHAN' in res_stop:
                    self.inst.write(f':MEASure:NAME MEAS1,"{timing_name}({delta_start["channel"]}-{delta_stop["channel"]})"')
                    time.sleep(0.05)
                elif 'CHAN' in res_start and 'WMEM' in res_stop:
                    self.inst.write(f':MEASure:NAME MEAS1,"{timing_name}({delta_start["channel"]}-m{delta_stop["channel"]})"')
                    time.sleep(0.05)
                elif 'WMEM' in res_start and 'CHAN' in res_stop:
                    self.inst.write(f':MEASure:NAME MEAS1,"{timing_name}(m{delta_start["channel"]}-{delta_stop["channel"]})"')
                    time.sleep(0.05)
                else:
                    self.inst.write(f':MEASure:NAME MEAS1,"{timing_name}(m{delta_start["channel"]}-m{delta_stop["channel"]})"')
                    time.sleep(0.05)
            
    def call_measurement_dutycycle(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:DUTYcycle CHANnel{}',
            'WMEMory': ':MEASure:DUTYcycle WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)

    def call_measurement_frequency(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:FREQuency CHANnel{}',
            'WMEMory': ':MEASure:FREQuency WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)

    def call_measurement_function(self, channel, command_templates: dict):
        display_dict= self.judge_channal_wmemory()
        for key in command_templates:
            if channel in display_dict[key]:
                self.inst.write(command_templates[key].format(channel))
                time.sleep(0.05)            
    
    def call_measurement_NCJitter(self, channel, direction):
        display_dict= self.judge_channal_wmemory()
        for cha in display_dict['CHANnel']:
            if cha == channel:
                self.inst.write(f':MEASure:NCJitter CHANnel{cha},{direction},1,1')
                time.sleep(0.05)
        for wme in display_dict['WMEMory']:
            if wme == channel:
                self.inst.write(f':MEASure:NCJitter WMEMory{cha},{direction},1,1')
                time.sleep(0.05)

    def call_measurement_period(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:PERiod CHANnel{}',
            'WMEMory': ':MEASure:PERiod WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)

    def call_measurement_slewrate(self, channel, direction):
        display_dict= self.judge_channal_wmemory()
        for cha in display_dict['CHANnel']:
            if cha == channel:
                self.inst.write(f':MEASure:SLEWrate CHANnel{cha},{direction}')
                time.sleep(0.05)
                self.inst.write(f':MEASure:NAME MEAS1,"{direction} Slew Rate({cha})"')
                time.sleep(0.05)
        for wme in display_dict['WMEMory']:
            if wme == channel:
                self.inst.write(f':MEASure:SLEWrate WMEMory{wme},{direction}')
                time.sleep(0.05)
                self.inst.write(f':MEASure:NAME MEAS1,"{direction} Slew Rate(m{wme})"')
                time.sleep(0.05)

    def call_measurement_tH(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:PWIDth CHANnel{}',
            'WMEMory': ':MEASure:PWIDth WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)  

    def call_measurement_tL(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:NWIDth CHANnel{}',
            'WMEMory': ':MEASure:NWIDth WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)  

    def call_measurement_tR(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:RISetime CHANnel{}',
            'WMEMory': ':MEASure:RISetime WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)              

    def call_measurement_tF(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:FALLtime CHANnel{}',
            'WMEMory': ':MEASure:FALLtime WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)              

    def call_measurement_VIH(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:VTOP CHANnel{}',
            'WMEMory': ':MEASure:VTOP WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)              

    def call_measurement_VIL(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:VBASe CHANnel{}',
            'WMEMory': ':MEASure:VBASe WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)              

    def call_measurement_VPP(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:VPP CHANnel{}',
            'WMEMory': ':MEASure:VPP WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)   

    def call_measurement_VMAX(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:VMAX CHANnel{}',
            'WMEMory': ':MEASure:VMAX WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)   
        
    def call_measurement_VMIN(self, channel):
        command_templates = {
            'CHANnel': ':MEASure:VMIN CHANnel{}',
            'WMEMory': ':MEASure:VMIN WMEMory{}'
        }            
        self.call_measurement_function(channel= channel, command_templates= command_templates)   
        
    def clear_diaplay(self):
        self.inst.write(':CDISplay')
        time.sleep(0.05)

    def clear_wmemory(self, channel: str):
        self.inst.write(f':WMEMory{channel}:CLEar')
        time.sleep(0.05)
        # string.set('')

    def default(self):
        self.inst.write(':SYSTem:PRESet DEFault')
        time.sleep(0.05)

    def delete_labelname(self, label_type, channel):
        
        display_dict= self.judge_channal_wmemory()
        
        if label_type == 1: # label
            self.inst.write(f':DISPlay:LABel OFF')
            time.sleep(0.05)
        else: # bookmark
            for cha in display_dict['CHANnel']:
                if cha == channel:
                    self.inst.write(f':DISPlay:BOOKmark{channel}:DELete')
                    time.sleep(0.05)
            for wme in display_dict['WMEMory']:
                if wme == channel-4:
                    self.inst.write(f':DISPlay:BOOKmark{channel}:DELete')
                    time.sleep(0.05)

    def display_channel(self, channel):
        res= self.inst.query(f':CHANnel{channel}:DISPlay?')
        time.sleep(0.05)
        if res == '1\n':
            self.inst.write(f':CHANnel{channel}:DISPlay OFF')
            time.sleep(0.05)
        else:
            self.inst.write(f':CHANnel{channel}:DISPlay ON')
            time.sleep(0.05)
        
        return res

    def delete_marker(self, tuple_measurement_index: tuple):  
        for i, boolvar in enumerate(tuple_measurement_index):
            if boolvar.get():
                self.inst.write(f':MARKer:MEASurement:MEASurement MEASurement{i+1},OFF')
                time.sleep(0.05)

    def delete_measurement(self, tuple_measurement_index: tuple):
        for i, boolvar in enumerate(tuple_measurement_index):
            if boolvar.get():
                self.inst.write(f'MEASurement{i+1}:CLEar')
                time.sleep(0.05)

    def display_wmemory(self, wmemory):
        res= self.inst.query(f':WMEMory{wmemory-4}:DISPlay?')
        time.sleep(0.05)
        if res == '1\n':
            self.inst.write(f':WMEMory{wmemory-4}:DISPlay OFF')
            time.sleep(0.05)
        else:
            self.inst.write(f':WMEMory{wmemory-4}:DISPlay ON')
            time.sleep(0.05)
    
    def extract_results(self):

        return [
            ("Measurement 1", "12.5", "12.3", "11.8", "13.1", "20"),
            ("Measurement 2", "8.2", "8.5", "7.9", "9.0", "20"),
            ("Measurement 3", "25.1", "24.8", "23.5", "26.2", "20"),
        ]        
        # meas_name= ['', '', '', '', '', '', '', '', '', '', '', '']
        # result1= ['', '', '', '', '', '', '', '', '', '', '', '']
        # result2= ['', '', '', '', '', '', '', '', '', '', '', '']
        # all_results= self.inst.query(f':MEASure:RESults?')
        # time.sleep(0.05)
        # for index, value in enumerate(all_results.split(',')):
        #     if divmod(index, 7)[1] == 0:
        #         try:
        #             meas_name[divmod(index, 7)[0]]= value
        #         except:
        #             # l_meas_name_1.config(text=f'484超過3個??')
        #             continue
        #         if value[0] == 'V':  # 0: Voltage, 1: Time, 2: Slew Rate, 3: Frequency, 4: Duty cycle
        #             measurement_type = 0 
        #         elif 'Slew Rate' in value:
        #             measurement_type = 2
        #         elif 'Freq' in value:
        #             measurement_type = 3
        #         elif 'Duty cycle' in value:
        #             measurement_type = 4
        #         elif value == '\n':
        #             meas_name[divmod(index, 7)[0]] = ''
        #             continue
        #         else:
        #             measurement_type = 1
            
        #     if intvar_result_type.get() == 1:  # 選擇Mean Value
        #         if divmod(index, 7)[1] == 4:
        #             if measurement_type == 0:
        #                 final_result_1= self.judge_unit_voltage(value= value)
        #                 final_result_2= ''
        #             elif measurement_type == 1:
        #                 slew= False
        #                 final_result_1= self.judge_unit_time(value= value, slew= slew)
        #                 final_result_2= ''
        #             elif measurement_type == 2:
        #                 slew= True
        #                 final_result_1= self.judge_unit_time(value= value, slew= slew)
        #                 final_result_2= ''
        #             elif measurement_type == 3:
        #                 final_result_1= self.judge_unit_frequency(value= value)
        #                 final_result_2= ''
        #             elif measurement_type == 4:
        #                 final_result_1 = f"{float(value):.3f}"+' %'
        #                 final_result_2= ''

        #             try:
        #                 result1[divmod(index, 7)[0]]= final_result_1
        #                 result2[divmod(index, 7)[0]]= final_result_2
        #             except:
        #                 continue

        #     elif intvar_result_type.get() == 2:  # 選擇Min & Max Value
        #         if divmod(index, 7)[1] == 2:
        #             if measurement_type == 0:
        #                 final_result_1= self.judge_unit_voltage(value= value)
        #             elif measurement_type == 1:
        #                 slew= False
        #                 final_result_1= self.judge_unit_time(value= value, slew= slew)
        #             elif measurement_type == 2:
        #                 slew= True
        #                 final_result_1= self.judge_unit_time(value= value, slew= slew)
        #             elif measurement_type == 3:
        #                 final_result_1= self.judge_unit_frequency(value= value)
        #             elif measurement_type == 4:
        #                 final_result_1 = f"{float(value):.3f}"+' %'

        #             try:
        #                 result1[divmod(index, 7)[0]]= final_result_1
        #             except:
        #                 continue

        #         if divmod(index, 7)[1] == 3:
        #             if measurement_type == 0:
        #                 final_result_2= self.judge_unit_voltage(value= value)
        #             elif measurement_type == 1:
        #                 slew= False
        #                 final_result_2= self.judge_unit_time(value= value, slew= slew)
        #             elif measurement_type == 2:
        #                 slew= True
        #                 final_result_2= self.judge_unit_time(value= value, slew= slew)
        #             elif measurement_type == 3:
        #                 final_result_2= self.judge_unit_frequency(value= value)
        #             elif measurement_type == 4:
        #                 final_result_2 = f"{float(value):.3f}"+' %'

        #             try:
        #                 result2[divmod(index, 7)[0]]= final_result_2
        #             except:
        #                 continue
        
    def judge_channal_wmemory(self):
        display_dict= {'CHANnel': [],'WMEMory': []}
        for i in range(1, 5):
            channel_res= self.inst.query(f':CHANnel{i}:DISPlay?')
            time.sleep(0.05)
            wme_res= self.inst.query(f':WMEMory{i}:DISPlay?')
            time.sleep(0.05)

            if channel_res == '1\n' and not wme_res == '1\n':
                display_dict['CHANnel'].append(i)
                # return 'CHANnel'
            if not channel_res == '1\n' and wme_res == '1\n':
                display_dict['WMEMory'].append(i)
                # return 'WMEMory'
            if channel_res == '1\n' and wme_res == '1\n':
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

    def load_setup(self, root, user_choice: int, location_choice: int, server_code: str, interface: str, sub: str, folder_path: str, setup_name: str, is_keep_timebase: bool, is_keep_voltage: bool, is_keep_labelname: bool):
        
        if user_choice == 0:  # User defined
            if location_choice == 1: # Server
                path = fr'{folder_path}'
                total_folder_path= f"{server_code}:" + path[2:]
            else: # Desktop
                total_folder_path = f"C:/Users/Administrator/Desktop/{folder_path}"
        else:  # standard
            total_folder_path = f'{server_code}:/#_Eric Team/02_Penny/Setup_Files_Collection/{interface}/{sub}'

        if is_keep_timebase:
            # 記錄示波器timebase設定
            time_position= self.inst.query(':TIMebase:POSition?').rstrip('\n')
            time.sleep(0.05)
            time_scale= self.inst.query(':TIMebase:SCALe?').rstrip('\n')
            time.sleep(0.05)

        if is_keep_voltage:
            # 記錄示波器voltage設定
            temp_voltscale_dict= {}
            temp_voltoffset_dict= {}
            display_dict= self.judge_channal_wmemory()
            for channel in display_dict['CHANnel']:
                volt_scale= self.inst.query(f':CHANnel{channel}:SCALe?')
                time.sleep(0.05)
                temp_voltscale_dict[channel]= volt_scale
                volt_offset= self.inst.query(f':CHANnel{channel}:OFFSet?')
                time.sleep(0.05)
                temp_voltoffset_dict[channel]= volt_offset
            for wme in display_dict['WMEMory']:
                volt_scale= self.inst.query(f':WMEMory{wme}:YRANge?').rstrip('\n')
                time.sleep(0.05)
                temp_voltscale_dict[wme]= float(volt_scale)/8
                volt_offset= self.inst.query(f':WMEMory{wme}:YOFFset?').rstrip('\n')
                time.sleep(0.05)
                temp_voltoffset_dict[wme]= volt_offset

            # 記錄示波器trigger設定
            trig_channel= self.inst.query(f':TRIGger:EDGE:SOURce?').rstrip('\n')
            time.sleep(0.05)
            trig_channel= trig_channel.lstrip("CHAN")
            trig_level= self.inst.query(f':TRIGger:LEVel? CHANnel{trig_channel}').rstrip('\n')
            time.sleep(0.05)

        # 呼叫設定檔
        self.inst.write(f':DISK:LOAD "{total_folder_path}/{setup_name}.set"')
        time.sleep(0.05)

        # 依據勾選狀態修改數值
        if is_keep_timebase:
            # 依照示波器畫面的timebase
            self.set_timebase_scale(timebase_scale= time_scale)
            self.set_timebase_offset(timebase_position= time_position)

        if is_keep_voltage:
            display_dict= self.judge_channal_wmemory()
            # 依照示波器畫面的Voltage
            for channel in display_dict['CHANnel']:
                self.inst.write(f':CHANnel{channel}:SCALe {temp_voltscale_dict[channel]}')
                time.sleep(0.05)
                self.inst.write(f':CHANnel{channel}:OFFSet {temp_voltoffset_dict[channel]}')
                time.sleep(0.05)
            for wme in display_dict['WMEMory']:
                self.inst.write(f':WMEMory{wme}:YRANge {float(temp_voltscale_dict[wme])*8}')
                time.sleep(0.05)
                self.inst.write(f':WMEMory{wme}:YOFFset {temp_voltoffset_dict[wme]}')
                time.sleep(0.05)

            # 依照示波器畫面的trigger
            res= self.inst.query(f':CHANnel{trig_channel}:DISPlay?')
            time.sleep(0.05)
            if not res == '1\n':
                self.inst.write(f':CHANnel{trig_channel}:DISPlay ON')
                time.sleep(0.05)
            self.inst.write(f':TRIGger:EDGE:SOURce CHANnel{trig_channel}')
            time.sleep(0.05)
            self.inst.write(f':TRIGger:LEVel CHANnel{trig_channel},{trig_level}')
            time.sleep(0.05)
            if not res == '1\n':
                self.inst.write(f':CHANnel{trig_channel}:DISPlay OFF')
                time.sleep(0.05)
            
            # 依照GUI的threshold
            # self.set_general_threshold(g_top= g_top, g_middle= g_middle, g_base= g_base, g_top_percent= g_top_percent, g_middle_percent= g_middle_percent, g_base_percent= g_base_percent)
            # self.set_risefall_threshold(rf_top= rf_top, rf_base= rf_base, rf_top_percent= rf_top_percent, rf_base_percent= rf_base_percent)

        label_type= root.labelnameframe.LabelNameLabelFrame.get_value()[0]
        label_content= root.labelnameframe.LabelNameLabelFrame.get_value()[1]
        if is_keep_labelname == True:
            # 依照GUI的label
            for i in range(8):
                self.add_labelname(
                    label_type= label_type, 
                    channel= i+1, 
                    content= label_content[i].rstrip('\n')
                )

    def load_wmemory(self, location_choice: int, server_code: str, folder_path: str, channel: str, wme_name: str):
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
        
        if location_choice == 1:
            total_folder_path = f"{server_code}:" + folder_path[2:]
        else:
            total_folder_path = f"C:/Users/Administrator/Desktop/{folder_path}"

        self.inst.write(f':DISK:LOAD "{total_folder_path}/{wme_name}.h5",WMEMory{channel},OFF')
        time.sleep(0.05)

    def measure_all_edge(self, button):
        ans= self.inst.query(':ANALyze:AEDGes?')
        time.sleep(0.05)
        if ans == '0\n':
            button['text'] = "Meas All Edge: ON"
            self.inst.write(f':ANALyze:AEDGes 1')
            time.sleep(0.05)
        else:
            button['text'] = "Meas All Edge: OFF"
            self.inst.write(f':ANALyze:AEDGes 0')
            time.sleep(0.05)
    
    def run(self):
        self.inst.write(':RUN')
        time.sleep(0.05)

    def save_pc_image(self, pc_folder_path: str, img_name: str):
        screen_data = np.array(self.inst.query_binary_values(":DISPlay:DATA? PNG", datatype = 's', container = bytes))
        time.sleep(0.05)

        is_save= utils.asking_is_folder_exist(folder_path= pc_folder_path)
        if not is_save:
            return
        is_save= utils.asking_is_cover_imgfile(folder_path= pc_folder_path, img_name= img_name)   
        if not is_save:
            return

        temp_img_name= ''.join(random.choices(string.ascii_letters + string.digits, k=8))

        temp_folder= fr'{os.path.dirname(__file__)}/Temp'
        if not os.path.exists(temp_folder):
            os.mkdir(temp_folder) 
            
        f_img = open(f"{temp_folder}/{temp_img_name}.png", "wb")
        f_img.write(bytearray(screen_data))
        f_img.close()

        utils.rgba_to_rgb_composite(f"{temp_folder}/{temp_img_name}.png", f"{pc_folder_path}/{img_name}.png", background=(0,0,0))

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

    def save_scope_file(self, location_choice: int, folder_path: str, channel: str, ext_type: int, current_file_name: str):
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

        if location_choice == 1: # Server
            folder_total_path = folder_path
        else: # Scope
            folder_total_path = f"C:/Users/Administrator/Desktop/{folder_path}"

        # 資料夾是否存在
        self.inst.query(f':DISK:DIRectory? "{folder_total_path}"')
        time.sleep(0.05)
        error_messenge=self.inst.query(f':SYSTem:ERRor?')
        time.sleep(0.05)
        # print(error_messenge)
        if error_messenge == '-256\n' or error_messenge == '113\n' or error_messenge == '-257\n':
            res= utils.asking_window(content= '資料夾不存在，是否新增？')
            if not res:
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
        if ext_type == 0:
            # 使用正則表達式來匹配所有 .h5 檔案名稱
            files = re.findall(r'\b[\w-]+\.(?:h5)\b', folder_content)
            ext= 'h5'
            command= f':DISK:SAVE:WAVeform CHANnel{channel},"{folder_total_path}/{current_file_name}",H5,OFF'
        else:
            # 使用正則表達式來匹配所有 .set 檔案名稱
            files = re.findall(r'\b[\w-]+\.(?:set)\b', folder_content)
            ext= 'set'
            command= f':DISK:SAVE:SETup "{folder_total_path}/{current_file_name}"'

        for file_name in files:
            if f'{current_file_name}.{ext}' == file_name:
                res= utils.asking_window(content= '檔案已經存在，是否覆蓋？')
                if not res:
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

    def set_general_numberic_threshold(self, numberic_dictionary: dict, combobox_dictionary: dict):
            do_the_judge= False
            if float(numberic_dictionary['top']) <= float(numberic_dictionary['middle']):
                numberic_dictionary['top']= Decimal(numberic_dictionary['middle']) + Decimal('0.01')
                combobox_dictionary['top'].config(foreground= 'red')
                combobox_dictionary['middle'].config(foreground= 'red')
                do_the_judge= True
            if float(numberic_dictionary['middle']) <= float(numberic_dictionary['base']):
                numberic_dictionary['base']= Decimal(numberic_dictionary['middle']) - Decimal('0.01')
                combobox_dictionary['base'].config(foreground= 'red')
                combobox_dictionary['middle'].config(foreground= 'red')
                do_the_judge= True
            if not do_the_judge:
                combobox_dictionary['top'].config(foreground= 'black')
                combobox_dictionary['middle'].config(foreground= 'black')
                combobox_dictionary['base'].config(foreground= 'black')

            self.inst.write(f':MEASure:THResholds:GENeral:METHod ALL,ABSolute')
            time.sleep(0.05)
            self.inst.write(f':MEASure:THResholds:GENeral:ABSolute ALL,{numberic_dictionary["top"]},{numberic_dictionary["middle"]},{numberic_dictionary["base"]}')
            time.sleep(0.05)

    def set_general_percentage_threshold(self, percentage_dictionary: dict, combobox_dictionary: dict):
            do_the_judge= False
            if float(percentage_dictionary['top']) <= float(percentage_dictionary['middle']):
                percentage_dictionary['top']= Decimal(percentage_dictionary['middle']) + Decimal('0.1')
                combobox_dictionary['top'].config(foreground= 'red')
                combobox_dictionary['middle'].config(foreground= 'red')
                do_the_judge= True
            if float(percentage_dictionary['middle']) <= float(percentage_dictionary['base']):
                percentage_dictionary['base']= Decimal(percentage_dictionary['middle']) - Decimal('0.1')
                combobox_dictionary['base'].config(foreground= 'red')
                combobox_dictionary['middle'].config(foreground= 'red')
                do_the_judge= True
            if not do_the_judge:
                combobox_dictionary['top'].config(foreground= 'black')
                combobox_dictionary['middle'].config(foreground= 'black')
                combobox_dictionary['base'].config(foreground= 'black')

            self.inst.write(f':MEASure:THResholds:GENeral:METHod ALL,PERCent')
            time.sleep(0.05)
            self.inst.write(f':MEASure:THResholds:GENeral:PERCent ALL,{percentage_dictionary["top"]},{percentage_dictionary["middle"]},{percentage_dictionary["base"]}')
            time.sleep(0.05)

    def set_intensity_setting(self, intensity_value):
        self.inst.write(f'SYSTem:CONTrol "WaveformBrt -1 {intensity_value}"')
        time.sleep(0.05)

    def set_risefall_numberic_threshold(self, numberic_dictionary: dict):
            self.inst.write(f':MEASure:THResholds:RFALl:METHod ALL,ABSolute')
            time.sleep(0.05)
            self.inst.write(f':MEASure:THResholds:RFALl:ABSolute ALL,{numberic_dictionary["top"]},{(float(numberic_dictionary["top"])+float(numberic_dictionary["base"]))/2},{numberic_dictionary["base"]}')
            time.sleep(0.05)

    def set_risefall_percentage_threshold(self, percentage_dictionary: dict):
            self.inst.write(f':MEASure:THResholds:RFALl:METHod ALL,PERCent')
            time.sleep(0.05)
            self.inst.write(f':MEASure:THResholds:RFALl:PERCent ALL,{percentage_dictionary["top"]},{(float(percentage_dictionary["top"])+float(percentage_dictionary["base"]))/2},{percentage_dictionary["base"]}')
            time.sleep(0.05)

    def set_timebase_offset(self, timebase_position): # 科學記號
        self.inst.write(f':TIMebase:POSition {timebase_position}')
        time.sleep(0.05)

    def set_timebase_scale(self, timebase_scale): # 科學記號
        self.inst.write(f':TIMebase:SCALe {timebase_scale}')
        time.sleep(0.05)

    def set_trigger_channel(self, trigger_channel):
        
        # 取得原Trigger channel & Trigger level
        current_channel= self.inst.query(f':TRIGger:EDGE:SOURce?')
        time.sleep(0.05)
        current_level= self.inst.query(f':TRIGger:LEVel? {current_channel}')
        time.sleep(0.05)
        
        is_displayed= self.inst.query(f':CHANnel{trigger_channel}:DISPlay?')
        time.sleep(0.05)
        if not is_displayed == '1\n':
            self.inst.write(f':CHANnel{trigger_channel}:DISPlay ON')
            time.sleep(0.05)

        self.inst.write(f':TRIGger:EDGE:SOURce CHANnel{trigger_channel}')
        time.sleep(0.05)
        self.inst.write(f':TRIGger:LEVel CHANnel{trigger_channel},{current_level}')
        time.sleep(0.05)

        if not is_displayed == '1\n':
            self.inst.write(f':CHANnel{trigger_channel}:DISPlay OFF')
            time.sleep(0.05)

    def set_trigger_level(self, trigger_level):
        
        # 取得原Trigger channel
        current_channel= self.inst.query(f':TRIGger:EDGE:SOURce?')
        time.sleep(0.05)

        is_displayed= self.inst.query(f':{current_channel}:DISPlay?')
        time.sleep(0.05)
        if not is_displayed == '1\n':
            self.inst.write(f':{current_channel}:DISPlay ON')
            time.sleep(0.05)

        self.inst.write(f':TRIGger:EDGE:SOURce {current_channel}')
        time.sleep(0.05)
        self.inst.write(f':TRIGger:LEVel {current_channel},{trigger_level}')
        time.sleep(0.05)

        if not is_displayed == '1\n':
            self.inst.write(f':{current_channel}:DISPlay OFF')
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
    
    def set_trigger_mode(self):
        res= self.inst.query(f':TRIGger:SWEep?')
        time.sleep(0.05)
        if res == 'AUTO\n':
            self.inst.write(':TRIGger:SWEep TRIGgered')
            time.sleep(0.05)
        else:
            self.inst.write(':TRIGger:SWEep AUTO')
            time.sleep(0.05)

    def set_voltage_scale(self, voltage_scale): 
        display_dict= self.judge_channal_wmemory()
        for channel in display_dict['CHANnel']:
            self.inst.write(f':CHANnel{channel}:SCALe {voltage_scale}')
            time.sleep(0.05)
        for wme in display_dict['WMEMory']:
            self.inst.write(f':WMEMory{wme}:YRANge {float(voltage_scale)*8}')
            time.sleep(0.05)

    def set_voltage_offset(self, voltage_offset): # 科學記號
        display_dict= self.judge_channal_wmemory()
        for channel in display_dict['CHANnel']:
            self.inst.write(f':CHANnel{channel}:OFFSet {voltage_offset}')
            time.sleep(0.05)
        for wme in display_dict['WMEMory']:
            self.inst.write(f':WMEMory{wme}:YOFFset {voltage_offset}')
            time.sleep(0.05)

    def single(self):
        self.inst.write(':SINGLE')
        time.sleep(0.05)

    def stop(self):
        self.inst.write(':STOP')
        time.sleep(0.05)


    ### 整合功能
    def set_all_scale(self, voltage_scale: str, voltage_offset: str, timebase_scale: str, timebase_position: str, trigger_channel: str, trigger_level: str):
        # Voltage
        display_dict= self.judge_channal_wmemory()
        for channel in display_dict['CHANnel']:
            self.inst.write(f':CHANnel{channel}:SCALe {voltage_scale}')
            time.sleep(0.05)
            self.inst.write(f':CHANnel{channel}:OFFSet {voltage_offset}')
            time.sleep(0.05)
        for wme in display_dict['WMEMory']:
            self.inst.write(f':WMEMory{wme}:YRANge {float(voltage_scale)*8}')
            time.sleep(0.05)
            self.inst.write(f':WMEMory{wme}:YOFFset {voltage_offset}')
            time.sleep(0.05)
        
        # Timebase
        self.inst.write(f':TIMebase:SCALe {timebase_scale}')
        time.sleep(0.05)
        self.inst.write(f':TIMebase:POSition {timebase_position}')
        time.sleep(0.05)
        
        # Trigger
        is_displayed= self.inst.query(f':{trigger_channel}:DISPlay?')
        time.sleep(0.05)
        if not is_displayed == '1\n':
            self.inst.write(f':{trigger_channel}:DISPlay ON')
            time.sleep(0.05)

        self.inst.write(f':TRIGger:EDGE:SOURce {trigger_channel}')
        time.sleep(0.05)
        self.inst.write(f':TRIGger:LEVel {trigger_channel},{trigger_level}')
        time.sleep(0.05)

        if not is_displayed == '1\n':
            self.inst.write(f':{trigger_channel}:DISPlay OFF')
            time.sleep(0.05)

    def call_channel_and_label(self, root, channel: int):
        
        display_dict= self.judge_channal_wmemory()

        for cha in display_dict['CHANnel']:
            if cha == channel:
                res= self.display_channel(channel= cha)
                if res == '1\n':
                    try:
                        self.delete_labelname(label_type= root.labelnameframe.LabelNameLabelFrame.get_value()[0], channel= channel)
                    except:
                        pass
                else: 
                    self.add_labelname(label_type= root.labelnameframe.LabelNameLabelFrame.get_value()[0], channel= channel, content= root.labelnameframe.LabelNameLabelFrame.get_value()[1][channel-1])
        for wme in display_dict['WMEMory']:
            if wme == channel-4:
                res= self.display_wmemory(wmemory= wme)
                if res == '1\n':
                    try:
                        self.delete_labelname(label_type= root.labelnameframe.LabelNameLabelFrame.get_value()[0], channel= channel)
                    except:
                        pass
                else: 
                    self.add_labelname(label_type= root.labelnameframe.LabelNameLabelFrame.get_value()[0], channel= channel, content= root.labelnameframe.LabelNameLabelFrame.get_value()[1][channel-1])
