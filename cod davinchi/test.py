import tkinter as tk
from tkinter import messagebox


class CountryData:
    def __init__(self, name, inflation, exchangerate, unemployment, realestateyield, avgsalary):
        self.name = name
        self.inflation = inflation
        self.exchangerate = exchangerate
        self.unemployment = unemployment
        self.realestateyield = realestateyield
        self.avgsalary = avgsalary


class CountryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Country Data Manager")
        self.country_entries = []
        self.max_countries = 10
        self.row_height = 50

        # Изначальный размер окна
        self.root.geometry("1250x600")
        self.root.minsize(1100, 600)

        # Главный контейнер
        self.main_frame = tk.Frame(root)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Настройка сетки
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        # Кнопки управления
        self.control_frame = tk.Frame(self.main_frame)
        self.control_frame.grid(row=0, column=0, sticky="ew", pady=5)

        self.add_button = tk.Button(self.control_frame, text="Добавить страну", command=self.add_country)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.remove_button = tk.Button(self.control_frame, text="Убрать страну", command=self.remove_country)
        self.remove_button.pack(side=tk.LEFT, padx=5)

        # Поле для добавляемых стран
        self.entries_frame = tk.Frame(self.main_frame)
        self.entries_frame.grid(row=1, column=0, sticky="nsew")

        # Секция "Оцениваемая страна"
        self.evaluation_frame = tk.Frame(self.main_frame)
        self.evaluation_frame.grid(row=2, column=0, sticky="ew", pady=20)

        self.evaluation_label = tk.Label(self.evaluation_frame, text="Оцениваемая страна", font=("Arial", 14))
        self.evaluation_label.grid(row=0, column=0, columnspan=6, pady=5)

        self.evaluation_row = self.create_country_row(self.evaluation_frame, 1)
        self.calculate_button = tk.Button(
            self.evaluation_frame, text="Рассчитать", width=20, height=2, command=self.calculate
        )
        self.calculate_button.grid(row=2, column=0, columnspan=6, pady=10)

    def create_country_row(self, parent_frame, row_num):
        """Создает строку полей для ввода данных о стране."""
        fields = [
            ("Название", 20),
            ("Уровень инфляции", 10),
            ("Курс валюты", 10),
            ("Уровень безработицы", 10),
            ("Доходность от недвижимости", 10),
            ("Средняя зарплата", 10),
        ]
        entry_row = []
        for col, (label_text, width) in enumerate(fields):
            label = tk.Label(parent_frame, text=label_text)
            label.grid(row=row_num, column=col * 2, padx=5, pady=5, sticky="w")
            entry = tk.Entry(parent_frame, width=width)
            entry.grid(row=row_num, column=col * 2 + 1, padx=5, pady=5, sticky="w")
            entry_row.append((label, entry))

        return entry_row

    def add_country(self):
        """Добавляет строку для ввода новой страны."""
        if len(self.country_entries) >= self.max_countries:
            messagebox.showwarning("Лимит достигнут", "Вы не можете добавить больше 10 стран.")
            return

        row_num = len(self.country_entries) + 1
        row = self.create_country_row(self.entries_frame, row_num)
        self.country_entries.append(row)

    def remove_country(self):
        """Удаляет последнюю добавленную строку."""
        if not self.country_entries:
            messagebox.showwarning("Нет данных", "Нет строк для удаления.")
            return

        last_row = self.country_entries.pop()
        for label, entry in last_row:
            label.destroy()
            entry.destroy()

        # Перестроение оставшихся строк для предотвращения смещения
        for idx, row in enumerate(self.country_entries, start=1):
            for col, (label, entry) in enumerate(row):
                label.grid(row=idx, column=col * 2)
                entry.grid(row=idx, column=col * 2 + 1)

    def calculate(self):
        """Заглушка для функции расчета."""
        messagebox.showinfo("Рассчитать", "Функция расчета еще не реализована.")

    def get_country_data(self):
        """Получает данные о странах из введенных строк."""
        countries = []
        for entry_row in self.country_entries:
            try:
                # Extract data from entry fields
                name = entry_row[0][1].get()
                inflation = float(entry_row[1][1].get())
                exchangerate = float(entry_row[2][1].get())
                unemployment = float(entry_row[3][1].get())
                realestateyield = float(entry_row[4][1].get())
                avgsalary = float(entry_row[5][1].get())

                country = CountryData(
                    name, inflation, exchangerate, unemployment, realestateyield, avgsalary
                )
                countries.append(country)
            except ValueError:
                messagebox.showerror("Ошибка данных", "Убедитесь, что все числовые поля заполнены корректно.")
                return []

        return countries


if __name__ == "__main__":
    root = tk.Tk()
    app = CountryApp(root)
    root.mainloop()