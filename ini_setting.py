import configparser
from pathlib import Path


class Settings:

    # 選項名稱: (存放選項清單的區段, 存放目前選取值的區段)
    COMBO_SECTIONS = {
        "VoltageScale": ("Scale_Offset_Config", "Scale_Offset_Selected_Values"),
        "VoltageOffset": ("Scale_Offset_Config", "Scale_Offset_Selected_Values"),
        "TriggerLevel": ("Scale_Offset_Config", "Scale_Offset_Selected_Values"),

        "GeneralTopPercent": ("Threshold_Setup_Config", "Threshold_Selected_Values"),
        "GeneralMiddlePercent": ("Threshold_Setup_Config", "Threshold_Selected_Values"),
        "GeneralBasePercent": ("Threshold_Setup_Config", "Threshold_Selected_Values"),
        "GeneralTopValue": ("Threshold_Setup_Config", "Threshold_Selected_Values"),
        "GeneralMiddleValue": ("Threshold_Setup_Config", "Threshold_Selected_Values"),
        "GeneralBaseValue": ("Threshold_Setup_Config", "Threshold_Selected_Values"),
        "RFTopPercent": ("Threshold_Setup_Config", "Threshold_Selected_Values"),
        "RFBasePercent": ("Threshold_Setup_Config", "Threshold_Selected_Values"),
        "RFTopValue": ("Threshold_Setup_Config", "Threshold_Selected_Values"),
        "RFBaseValue": ("Threshold_Setup_Config", "Threshold_Selected_Values"),

        "SaveOtherServerCode": ("Save_Other_Setup_Config", "Save_Other_Selected_Values"),
        "LoadWMemoryServerCode": ("Load_WMemory_Setup_Config", "Load_WMemory_Selected_Values"),
        "LoadSetupFileServerCode": ("Load_SetupFile_Setup_Config", "Load_SetupFile_Selected_Values"),
    }

    def __init__(self, config_file=None):
        if config_file is None:
            config_file = (
                Path(__file__).resolve().parent
                / "InitConfig_setup_new.ini"
            )
        
        self.config_file = Path(config_file)

        self.config = configparser.ConfigParser()
        self.config.optionxform = str  # 保留 INI 鍵名大小寫，必須在 read() 前設定
        loaded_files = self.config.read(self.config_file, encoding="utf-8")

        if not loaded_files:
            raise FileNotFoundError(f"找不到設定檔：{self.config_file}")

        # 記錄各 Frame 傳入的 Tkinter 變數，供 save() 使用
        self.variables = {}

        # 讀取 Combobox 選項與目前選取值
        self.combo_options = {}
        self.selected_values = {}
        self._load_combobox_data()

    def _load_combobox_data(self):
        for key, (options_section, selected_section) in self.COMBO_SECTIONS.items():
            option_text = self.config.get(
                options_section, key, fallback=""
            )

            # 逗號分隔，並移除多餘空白及空項目
            self.combo_options[key] = [
                item.strip()
                for item in option_text.split(",")
                if item.strip()
            ]

            self.selected_values[key] = self.config.get(
                selected_section, key, fallback=""
            )

    def _ensure_section(self, section):
        if not self.config.has_section(section):
            self.config.add_section(section)

    def _write_config(self):
        with self.config_file.open("w", encoding="utf-8") as config_file:
            self.config.write(config_file)

    def apply(self, section, tk_vars):
        """將 INI 的值填入 Tkinter 變數，並註冊供 save() 寫回。"""
        self._ensure_section(section)
        self.variables.setdefault(section, {})

        for key, var in tk_vars.items():
            if self.config.has_option(section, key):
                var.set(self.config.get(section, key))

            # 記住 Tkinter 變數，關閉時讀取最新值
            self.variables[section][key] = var

    def setup_combobox(self, combobox, combobox_var, key):
        """設定 Combobox 選項，並綁定 Enter 新增、Delete 刪除。"""
        if key not in self.COMBO_SECTIONS:
            raise KeyError(f"未設定 Combobox 對應資料：{key}")

        options = self.combo_options[key]
        combobox["values"] = options

        selected_value = self.selected_values.get(key, "")
        if selected_value:
            combobox_var.set(selected_value)

        # 新增選項；傳入 key，避免每個 Frame 重複傳一串參數
        combobox.bind(
            "<Return>",
            lambda event: self.add_combobox_option(
                combobox, combobox_var, key
            ),
        )

        # 刪除選項
        combobox.bind(
            "<Delete>",
            lambda event: self.delete_combobox_option(
                combobox, combobox_var, key
            ),
        )

    def _save_combobox_data(self, key, selected_value):
        options_section, selected_section = self.COMBO_SECTIONS[key]

        self._ensure_section(options_section)
        self._ensure_section(selected_section)

        self.config.set(
            options_section,
            key,
            ",".join(self.combo_options[key]),
        )
        self.config.set(selected_section, key, selected_value)

        self.selected_values[key] = selected_value
        self._write_config()

    def add_combobox_option(self, combobox, combobox_var, key):
        new_option = combobox_var.get().strip()
        if not new_option:
            return "break"

        options = self.combo_options[key]

        if new_option not in options:
            options.append(new_option)

        combobox["values"] = options
        combobox_var.set(new_option)

        self._save_combobox_data(key, new_option)
        return "break"

    def delete_combobox_option(self, combobox, combobox_var, key):
        selected_option = combobox_var.get().strip()
        options = self.combo_options[key]

        if selected_option in options:
            options.remove(selected_option)

        combobox["values"] = options
        combobox_var.set("")

        # 刪除目前選項後，將目前選取值存成空字串
        self._save_combobox_data(key, "")
        return "break"
            
    def save(self):
        """將已記錄的 Tkinter 變數值寫回 INI。"""
        for section, tk_vars in self.variables.items():
            if not self.config.has_section(section):
                self.config.add_section(section)

            for key, var in tk_vars.items():
                self.config.set(section, key, str(var.get()))

        with open(self.config_file, "w", encoding="utf-8") as file:
            self.config.write(file)

    def get_options(self, section, key):
        text = self.config.get(section, key, fallback="")
        return [line.strip() for line in text.splitlines() if line.strip()]