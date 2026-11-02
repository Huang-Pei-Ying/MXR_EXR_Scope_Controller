import configparser


class Settings:
    def __init__(self, file_path):
        self.config = configparser.ConfigParser()
        loaded_files = self.config.read(file_path, encoding="utf-8")

        if not loaded_files:
            raise FileNotFoundError(f"找不到設定檔：{file_path}")

    def apply(self, section, tk_vars):
        """將指定區段的設定值，填入對應的 Tkinter 變數。"""
        if not self.config.has_section(section):
            return

        for key, var in tk_vars.items():
            if self.config.has_option(section, key):
                var.set(self.config.get(section, key))