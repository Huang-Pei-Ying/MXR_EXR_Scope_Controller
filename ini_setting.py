import configparser


class Settings:
    def __init__(self, file_path):
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.variables = {}
        self.config.optionxform = str  # 保留 INI 鍵名大小寫，必須在 read() 前設定
        loaded_files = self.config.read(self.file_path, encoding="utf-8")

        if not loaded_files:
            raise FileNotFoundError(f"找不到設定檔：{file_path}")

    def apply(self, section, tk_vars):
        """將指定區段的設定值，填入對應的 Tkinter 變數。"""
        if not self.config.has_section(section):
            self.config.add_section(section)

        self.variables.setdefault(section, {})

        for key, var in tk_vars.items():
            if self.config.has_option(section, key):
                var.set(self.config.get(section, key))

            # 記住 Tkinter 變數，關閉時讀取最新值
            self.variables[section][key] = var

    def save(self):
        """將已記錄的 Tkinter 變數值寫回 INI。"""
        for section, tk_vars in self.variables.items():
            if not self.config.has_section(section):
                self.config.add_section(section)

            for key, var in tk_vars.items():
                self.config.set(section, key, str(var.get()))

        with open(self.file_path, "w", encoding="utf-8") as file:
            self.config.write(file)