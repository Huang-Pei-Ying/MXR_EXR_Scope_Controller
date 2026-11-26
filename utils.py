from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
import os


def move_mouse_entry_end(entry):
    """將 Entry 的內容視圖滾動到最後，並設置游標到最後一位"""
    # entry.focus()           # 設置 Entry 欄位獲取焦點
    # entry.icursor(tk.END)   # 將游標移動到文本的最後一位
    # entry.xview_moveto(1)   # 滾動視圖到最後一部分，1 表比例最右邊
    def move():
        if not entry.winfo_exists():
            return

        entry.update_idletasks()       # 先完成尺寸與畫面更新
        entry.xview_moveto(1.0)        # 將水平視圖移到最右側
        entry.icursor(tk.END)          # 將游標放到文字末端

    entry.after(100, move)

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

def browse_folder(entry_var, target_entry):
    # 打開檔案瀏覽器以選擇資料夾
    folder_selected = filedialog.askdirectory()
    # 將選擇的資料夾路徑填入 Entry
    entry_var.set(folder_selected)

    move_mouse_entry_end(entry= target_entry)

def switch_string(var_1, var_2):
    string_1= var_1.get()
    string_2= var_2.get()
    var_1.set(string_2)
    var_2.set(string_1)

def clear(string):
    string.set('')

def asking_is_cover_imgfile(folder_path, img_name):
    if os.path.exists(f"{folder_path}/{img_name}.png"):
        res= asking_window(content= '檔案已經存在，是否覆蓋？')
        if not res: 
            return False
        else:
            return True
    else: 
        return True

def asking_is_folder_exist(folder_path):
    if not os.path.exists(folder_path):
        res= asking_window(content= '資料夾不存在，是否新增？')
        if not res: 
            return False
        else:
            os.mkdir(folder_path) 
            return True
    else:
        return True

def asking_window(content: str):
    ask_scp_root = tk.Tk()
    ask_scp_root.withdraw()  # 隱藏主視窗
    ask_scp_result = messagebox.askyesno("Warning", f"{content}")
    ask_scp_root.destroy()
    
    if not ask_scp_result:
        ask_scp_root = tk.Tk()
        ask_scp_root.withdraw()  # 隱藏主視窗
        messagebox.showinfo("Warning", f'檔案未儲存')
        # print("檔案未保存。")
        return False

def switch_button_state(button_list: list):
    for button in button_list:
        if button["state"] == 'normal':
            button.config(state="disabled")
        else:
            button.config(state="normal")

### 調整顏色密度
def on_mouse_wheel(event, entry):

    # Windows/macOS 通常用 event.delta 判斷滾輪方向
    step = 1 if event.delta > 0 else -1    # # 設定waveform intensity參數

    change_intensity_by(entry, step)

def change_intensity_by(entry, step):
    """依 step 增減 Entry 的數值，並限制在 0–100。"""

    min_value = 0
    max_value = 100

    # 讀取 Entry 目前的內容；空白或非整數時，從 0 開始
    try:
        value = int(entry.get())
    except (ValueError, TypeError):
        value = 0

    # 加上或減去 step
    value += step

    # 限制數值不能低於 0，也不能高於 100
    value = max(min_value, min(max_value, value))

    # 將新數值寫回 Entry
    entry.delete(0, "end")
    entry.insert(0, str(value))

    # 若有顏色更新函式，可在這裡呼叫
    update_intensity_color(value, entry)

def update_intensity_color(value, entry):
    """根據數值改變文字顏色"""
    if int(value) == 50:
        entry.config(foreground= '#0B3041')
    else:
        entry.config(foreground= "red")

def validate_number(new_value, entry):
    """限制只能輸入 0-100 的整數，並允許清空。"""

    if new_value == "":
        entry.config(foreground="red")
        return True

    if not new_value.isdigit():
        return False

    num = int(new_value)

    if 0 <= num <= 100:
        update_intensity_color(num, entry= entry)
        return True

    # entry.config(foreground="red")
    return True

def set_to_fixty(entry):
    value = 50
    entry.delete(0, tk.END)
    entry.insert(0, str(value))
    update_intensity_color(value, entry= entry)
    # mxr.check_intensity_setting(intensity_value= 50)

#####################################

### 呼叫設定檔
def block_by_choice(var_value, user_defined_list, standard_list):
    if var_value == 0: # User defined
        for i in standard_list:
            # if i
            # i.set(value= '')
            i.config(state= 'disabled')
        for j in user_defined_list:
            j.config(state= 'normal')
    else:
        for i in user_defined_list:
            # if i
            # i.set(value= '')
            i.config(state= 'disabled')
        for j in standard_list:
            j.config(state= 'normal')

def search_every_interface():
    # 讀取選項清單
    folders_path = Path(__file__).resolve().parent / "Setup_Files_Collection"

    # 只取第一層子資料夾名稱
    interface_options = sorted(
        folder.name
        for folder in folders_path.iterdir()
        if folder.is_dir()
    )
    return interface_options

def search_every_sub(interface):
    # 讀取選項清單
    folders_path = Path(__file__).resolve().parent / f"Setup_Files_Collection/{interface}"

    # 只取第2層子資料夾名稱
    sub_options = sorted(
        folder.name
        for folder in folders_path.iterdir()
        if folder.is_dir()
    )
    return sub_options

def search_every_setupfiles(interface, sub):
    # 讀取選項清單
    folders_path = Path(__file__).resolve().parent / f"Setup_Files_Collection/{interface}/{sub}"

    # 只取檔案名稱
    setupfiles_options = sorted(
        folder.name
        for folder in folders_path.iterdir()
        if folder.is_file()
    )
    return setupfiles_options

#####################################