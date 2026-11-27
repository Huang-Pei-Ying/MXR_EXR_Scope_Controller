import tkinter as tk
from tkinter import ttk

class ResultsWindow:
    def __init__(self, parent, mxr):
        self.window = tk.Toplevel(parent)
        self.window.title("Results")
        self.window.geometry("1100x600")
        self.window.configure(bg="#bdbdbd")

        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, weight=1)

        title = tk.Label(
            self.window,
            text="Results",
            font=("Candara", 34, "bold"),
            fg="#777777",
            bg="#bdbdbd",
            anchor="w",
        )
        title.grid(row=0, column=0, sticky="ew", padx=12, pady=(0, 10))

        table_frame = tk.Frame(self.window, bg="#bdbdbd")
        table_frame.grid(row=1, column=0, sticky="nsew", padx=12, pady=5)
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        columns = ("measurement", "current", "mean", "min", "max", "count")

        style = ttk.Style(self.window)
        style.configure(
            "Results.Treeview",
            font=("Candara", 14),
            rowheight=38,
            background="#eee8e2",
            fieldbackground="#eee8e2",
            foreground="#292929",
        )
        style.configure(
            "Results.Treeview.Heading",
            font=("Candara", 16, "bold"),
            background="#e5ddd5",
            foreground="#873600",
            padding=10,
        )

        self.table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Results.Treeview",
        )

        headings = {
            "measurement": "Measurement",
            "current": "Current",
            "mean": "Mean",
            "min": "Min",
            "max": "Max",
            "count": "Count",
        }

        widths = {
            "measurement": 220,
            "current": 180,
            "mean": 180,
            "min": 150,
            "max": 150,
            "count": 150,
        }

        for column in columns:
            self.table.heading(column, text=headings[column])
            self.table.column(
                column,
                width=widths[column],
                minwidth=100,
                anchor="center",
            )

        # 從 function.py 取得資料
        for row in mxr.extract_results():
            self.table.insert("", "end", values=row)

        vertical_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.table.yview,
        )
        horizontal_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.table.xview,
        )

        self.table.configure(
            yscrollcommand=vertical_scrollbar.set,
            xscrollcommand=horizontal_scrollbar.set,
        )

        self.table.grid(row=0, column=0, sticky="nsew")
        vertical_scrollbar.grid(row=0, column=1, sticky="ns")
        horizontal_scrollbar.grid(row=1, column=0, sticky="ew")

        close_button = tk.Button(
            self.window,
            text="Close",
            font=("Candara", 16),
            fg="white",
            bg="#001f24",
            activebackground="#123940",
            activeforeground="white",
            relief="flat",
            padx=35,
            pady=10,
            command=self.window.destroy,
        )
        close_button.grid(row=2, column=0, sticky="e", padx=25, pady=20)
