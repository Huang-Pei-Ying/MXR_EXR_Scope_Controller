











def delete_combobox_option(combobox, combobox_value, options, config_file, section, key, selected_section):
    selected_option = combobox_value.get().strip()
    if selected_option in options:
        options.remove(selected_option)
        combobox['values'] = options
        combobox_value.set('')  # 清空當前選擇
        save_option_to_ini(config_file, section, key, options, selected_section, combobox.get())

def move_mouse_entry_end(entry):
    """將 Entry 的內容視圖滾動到最後，並設置游標到最後一位"""
    entry.focus()           # 設置 Entry 欄位獲取焦點
    entry.icursor(tk.END)   # 將游標移動到文本的最後一位
    entry.xview_moveto(1)   # 滾動視圖到最後一部分，1 表比例最右邊

def on_mouse_wheel(event):
    try:
        value = int(entry_waveform_intensity.get())
    except ValueError:
        value = 0

    if event.delta > 0:
        value += waveform_intensity_step
    else:
        value -= waveform_intensity_step

    value = max(waveform_intensity_min_value, min(waveform_intensity_max_value, value))
    entry_waveform_intensity.delete(0, tk.END)
    entry_waveform_intensity.insert(0, str(value))
    update_intensity_color(value)

def recall_combobox_option_from_inifile():
    config_initial = configparser.ConfigParser()
    config_initial.optionxform = str
    config_file = os.path.join(os.path.dirname(__file__), 'InitConfig_setup_new.ini')
    config_initial.read(config_file, encoding='UTF-8')
    
    # Scale
    VoltScale_options = config_initial['Scale_Offset_Config'].get('VoltScale', '').split(',')
    VoltOffset_options = config_initial['Scale_Offset_Config'].get('VoltOffset', '').split(',')
    TriggerLevel_options = config_initial['Scale_Offset_Config'].get('TriggerLevel', '').split(',')

    # Threshold
    GeneralTopPercent_options = config_initial['Threshold_Setup_Config'].get('GeneralTopPercent', '').split(',')
    GeneralMiddlePercent_options = config_initial['Threshold_Setup_Config'].get('GeneralMiddlePercent', '').split(',')
    GeneralBasePercent_options = config_initial['Threshold_Setup_Config'].get('GeneralBasePercent', '').split(',')
    GeneralTopValue_options = config_initial['Threshold_Setup_Config'].get('GeneralTopValue', '').split(',')
    GeneralMiddleValue_options = config_initial['Threshold_Setup_Config'].get('GeneralMiddleValue', '').split(',')
    GeneralBaseValue_options = config_initial['Threshold_Setup_Config'].get('GeneralBaseValue', '').split(',')
    RFTopPercent_options = config_initial['Threshold_Setup_Config'].get('RFTopPercent', '').split(',')
    RFBasePercent_options = config_initial['Threshold_Setup_Config'].get('RFBasePercent', '').split(',')
    RFTopValue_options = config_initial['Threshold_Setup_Config'].get('RFTopValue', '').split(',')
    RFBaseValue_options = config_initial['Threshold_Setup_Config'].get('RFBaseValue', '').split(',')

    # Scope Segment
    SaveOthersScopeSegment_options = config_initial['Scope_Server_Segment'].get('SaveOthersScopeSegment', '').split(',')
    LoadWmemoryScopeSegment_options = config_initial['Scope_Server_Segment'].get('LoadWmemoryScopeSegment', '').split(',')
    LoadSetupScopeSegment_options = config_initial['Scope_Server_Segment'].get('LoadSetupScopeSegment', '').split(',')

    # 從這裡返回值供其他部分調用
    return {
        'VoltScale': VoltScale_options, 
        'VoltOffset': VoltOffset_options, 
        'TriggerLevel': TriggerLevel_options, 
        'GeneralTopPercent': GeneralTopPercent_options,
        'GeneralMiddlePercent': GeneralMiddlePercent_options, 
        'GeneralBasePercent': GeneralBasePercent_options, 
        'GeneralTopValue': GeneralTopValue_options, 
        'GeneralMiddleValue': GeneralMiddleValue_options, 
        'GeneralBaseValue': GeneralBaseValue_options, 
        'RFTopPercent': RFTopPercent_options, 
        'RFBasePercent': RFBasePercent_options, 
        'RFTopValue': RFTopValue_options, 
        'RFBaseValue': RFBaseValue_options, 
        'SaveOthersScopeSegment': SaveOthersScopeSegment_options,
        'LoadWmemoryScopeSegment': LoadWmemoryScopeSegment_options,
        'LoadSetupScopeSegment': LoadSetupScopeSegment_options,
        
        'config_file': config_file,  # 儲存config文件路徑以便後續使用

        'selected_values': {
            'VoltScale': config_initial['Scale_Offset_Selected_Values'].get('VoltScale', ''),
            'VoltOffset': config_initial['Scale_Offset_Selected_Values'].get('VoltOffset', ''),
            'TriggerLevel': config_initial['Scale_Offset_Selected_Values'].get('TriggerLevel', ''),
            'GeneralTopPercent': config_initial['Threshold_Selected_Values'].get('GeneralTopPercent', ''),
            'GeneralMiddlePercent': config_initial['Threshold_Selected_Values'].get('GeneralMiddlePercent', ''),
            'GeneralBasePercent': config_initial['Threshold_Selected_Values'].get('GeneralBasePercent', ''),
            'GeneralTopValue': config_initial['Threshold_Selected_Values'].get('GeneralTopValue', ''),
            'GeneralMiddleValue': config_initial['Threshold_Selected_Values'].get('GeneralMiddleValue', ''),
            'GeneralBaseValue': config_initial['Threshold_Selected_Values'].get('GeneralBaseValue', ''),
            'RFTopPercent': config_initial['Threshold_Selected_Values'].get('RFTopPercent', ''),
            'RFBasePercent': config_initial['Threshold_Selected_Values'].get('RFBasePercent', ''),
            'RFTopValue': config_initial['Threshold_Selected_Values'].get('RFTopValue', ''),
            'RFBaseValue': config_initial['Threshold_Selected_Values'].get('RFBaseValue', ''),
            'SaveOthersScopeSegment': config_initial['Scope_Server_Segment_Selected_Values'].get('SaveOthersScopeSegment', ''),
            'LoadWmemoryScopeSegment': config_initial['Scope_Server_Segment_Selected_Values'].get('LoadWmemoryScopeSegment', ''),
            'LoadSetupScopeSegment': config_initial['Scope_Server_Segment_Selected_Values'].get('LoadSetupScopeSegment', ''),
            }        
    }

def rgba_to_rgb_composite(in_path, out_path, background=(0, 0, 0)):
    img = Image.open(in_path)
    # 確保有 alpha 通道用 RGBA
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    # 建一個同尺寸的背景（含不透明 alpha）
    bg = Image.new('RGBA', img.size, background + (255,))
    # 將原圖疊在背景上，並去掉 alpha
    composed = Image.alpha_composite(bg, img).convert('RGB')
    composed.save(out_path, format='PNG')

def save_option_to_ini(config_file, section, key, updated_options, selected_section, selected_value):
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

def select_folder(entry_var, target_entry):
    # 打開檔案瀏覽器以選擇資料夾
    folder_selected = filedialog.askdirectory()
    # 將選擇的資料夾路徑填入 Entry
    entry_var.set(folder_selected)

    move_mouse_entry_end(entry= target_entry)

def select_load_setup_standard_subfolder(event, pc_segment):

    target_interface_subfolder_files= []

    strvar_load_setup_standard_files.set(value= '')

    # 示波器folder路徑
    setupfile_class_folderpath = f'{strvar_load_setup_loacation_server.get()}:\#_Eric Team\02_Penny\Setup_Files_Collection\{strvar_load_setup_standard_interface.get()}\{strvar_load_setup_standard_subfolder.get()}'
    # str_WMe_folder.set(value= setupfile_class_folderpath)

    # PC folder路徑
    pc_setupfile_class_folderpath = fr'{pc_segment}#_Eric Team\02_Penny\Setup_Files_Collection\{strvar_load_setup_standard_interface.get()}\{strvar_load_setup_standard_subfolder.get()}'

    # os.walk 會回傳 root (目前路徑), dirs (子資料夾名稱列表), files (檔案名稱列表)
    for root, dirs, files in os.walk(pc_setupfile_class_folderpath):
        for file in files:
            # 篩選.set
            if file.endswith('.set'):
                # 取得設定檔的絕對路徑
                file_path = os.path.join(root, file)
                target_interface_subfolder_files.append((os.path.basename(file_path)).rstrip('.set'))

    combobox_load_setup_standard_files.config(values= target_interface_subfolder_files)
    # adjust_entry(entry= e_WMe_folder)

def select_load_setup_standard_interface(event, pc_segment):
    
    target_interface_subfolder= []

    strvar_load_setup_standard_subfolder.set(value= '')

    if strvar_load_setup_standard_interface.get() == 'User':
        strvar_load_setup_standard_subfolder.set(value= '')
        combobox_load_setup_standard_subfolder.config(state= 'disabled')
    elif strvar_load_setup_standard_interface.get() == '':
        strvar_load_setup_standard_subfolder.set(value= '')
        combobox_load_setup_standard_subfolder.config(state= 'disabled')
    else: 
        combobox_load_setup_standard_subfolder.config(state= 'readonly')

        # 示波器folder路徑
        setupfile_interface_folderpath = fr'{strvar_load_setup_standard_interface.get()}:\#_Eric Team\02_Penny\Setup_Files_Collection\{strvar_load_setup_standard_interface.get()}'
        # str_WMe_folder.set(value= setupfile_interface_folderpath)

        # PC folder路徑
        pc_setupfile_interface_folderpath = fr'{pc_segment}#_Eric Team\02_Penny\Setup_Files_Collection\{strvar_load_setup_standard_interface.get()}'

        # os.walk 會回傳 root (目前路徑), dirs (子資料夾名稱列表), files (檔案名稱列表)
        for root, dirs, files in os.walk(pc_setupfile_interface_folderpath):
            for dir_name in dirs:
                # 取得子資料夾的絕對路徑
                dir_path = os.path.join(root, dir_name)
                target_interface_subfolder.append(os.path.basename(dir_path))

        combobox_load_setup_standard_subfolder.config(values= target_interface_subfolder)
        # adjust_entry(entry= e_WMe_folder)

def find_disk_segment(path):
    for seg in string.ascii_uppercase:
        disk = Path(f"{seg}:\\")
        
        if disk.exists():
            full_path = disk / path
            
            if full_path.is_dir():
                return disk
    return None

def set_to_fixty():
    value = 50
    entry_waveform_intensity.delete(0, tk.END)
    entry_waveform_intensity.insert(0, str(value))
    update_intensity_color(value)
    # mxr.check_intensity_setting(intensity_value= 50)

def switch_string(var_1, var_2):
    string_1= var_1.get()
    string_2= var_2.get()
    var_1.set(string_2)
    var_2.set(string_1)

def update_intensity_color(value):
    """根據數值改變文字顏色"""
    if value == 50:
        entry_waveform_intensity.config(foreground= colors['entry'][1])
    else:
        entry_waveform_intensity.config(foreground= "red")

def validate_number(new_value):
    """限制只能輸入數字 (允許空白)"""
    if new_value == "":  # 空白允許
        entry_waveform_intensity.config(foreground= "red")
        return True
    if new_value.isdigit():
        num = int(new_value)
        # 限制範圍
        if waveform_intensity_min_value <= num <= waveform_intensity_max_value:
            update_intensity_color(num)
        else:
            entry_waveform_intensity.config(foreground= "red")
        return True
    return False  # 阻擋非數字字元

# 獲取ini數據
config_data = recall_combobox_option_from_inifile()
# general_top_percent_options = config_data['GeneralTopPercent']
config_file_path = config_data['config_file']


def execute_commbobox_function(combobox, combobox_var, ini_dict_key, ini_option_section, ini_option_key, ini_selected_section):
    combobox['values'] = config_data[ini_dict_key]  # 設置初始選項
    combobox.bind('<Return>', lambda event: add_combobox_option(combobox, combobox_var, config_data[ini_dict_key], config_file_path, ini_option_section, ini_option_key, ini_selected_section))
    combobox.bind('<Delete>', lambda event: delete_combobox_option(combobox, combobox_var, config_data[ini_dict_key], config_file_path, ini_option_section, ini_option_key, ini_selected_section))

def add_combobox_option(combobox, combobox_value, options, config_file, section, key, selected_section):
    new_option = combobox_value.get().strip()
    if new_option and new_option not in options:
        options.append(new_option)
        combobox['values'] = options
        save_option_to_ini(config_file, section, key, options, selected_section, combobox.get())

def clear(string):
    string.set('')

