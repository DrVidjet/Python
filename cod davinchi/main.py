import tkinter as tk
from logging import disable
from tkinter import Label, PhotoImage, Entry
from tkinter.constants import OUTSIDE, CENTER

from nltk.sem.chat80 import country

clicks = 0

class CountryData:
    def __init__(self, name, inflation, exchangerate, unemployment, realestateyield, avgsalary):
        self.name = name
        self.inflation = inflation
        self.exchangerate = exchangerate
        self.unemployment = unemployment
        self.realestateyield = realestateyield
        self.avgsalary = avgsalary

def on_buttonadd_click():
    global clicks



    if clicks > 10:
        buttonadd["state"] = "disabled"
        sorry = Label(font=("Arial", 12),
                      text="Приносим наши глубочайшие извинения, но для стабильной работы программы\n"
                           " мы отключили возможность добавления больше 5 стран в выборку :(\n")
        sorry.place(x=0, y=20)
    else:
        #labeln = Label(font=("Arial", 14), text="Название")
        #labeli = Label(font=("Arial", 14), text="Уровень инфляции")
        #labele = Label(font=("Arial", 14), text="Название")
        #labelu = Label(font=("Arial", 14), text="Название")
        #labelr = Label(font=("Arial", 14), text="Название")
        #labela = Label(font=("Arial", 14), text="Название")

        entryn = Entry(font=("Arial", 14), width=15)
        entryi = Entry(font=("Arial", 14), width=5)
        entrye = Entry(font=("Arial", 14), width=5)
        entryu = Entry(font=("Arial", 14), width=5)
        entryr = Entry(font=("Arial", 14), width=5)
        entrya = Entry(font=("Arial", 14), width=5)
        entryn.place(y=clicks*80, x=0)
        entryi.place(y=clicks*80, x=200)
        entrye.place(y=clicks*80, x=300)
        entryu.place(y=clicks*80, x=400)
        entryr.place(y=clicks*80, x=500)
        entrya.place(y=clicks*80, x=600)
    clicks += 1

def on_buttondel_click():
    print("Hello")



def on_warning_click():
    warning.destroy()

warning = tk.Tk()
up = Label(font=("Arial", 30), text="Здравствуйте!")
label = Label(font=("Arial", 13), text="Добро пожаловать в программу 'Код давинчи'! Она призвана помочь в анализе экономики\n"
               "     конткретной страны посредством сравнения с экономикой других стран из конфигурируемой выборки с \n"
               "помощью специально выведенной для этого формулы. Приятного использования!\n"
)
warningbutton = tk.Button(warning, font=("Arial", 20), text="Вперед!", command=on_warning_click, width=20)

warning.title("")
warning.geometry("850x400+400+200")
warning.minsize(850,400)

up.place(x=280,y=0)
label.place(x=0, y=100)
warningbutton.place(x=250, y=250)

warning.mainloop()

app = tk.Tk()
app.title("Код Давинчи")
app.geometry("800x800+400+100")
app.minsize(800, 800)

countries = []
for country in countries:
    other_object.add(country)

buttonadd = tk.Button(app, font=("Arial", 12), text="Добавить страну", command=on_buttonadd_click, width=20)
buttondel = tk.Button(app, font=("Arial", 12), text="Убрать страну", command=on_buttondel_click, width=20)
entry = Entry(font=("Arial", 14), width=15)

buttonadd.place(x=20, y=20)
buttondel.place(x=590, y=20)
#entry.pack(anchor="w", pady=5)

app.mainloop()

#height_lb = Label(
#    frame,
#    text = "Добро пожаловать в программу 'Код давинчи'! Она призвана помочь в анализе экономики"
#           "конткретной страны по средством сравнения с экономикой других стран из выборки с "
#           "помощью специально выведенной для этого формулы. Приятного использования!"
#)
#height_lb.grid(row=3, column=1)





#count = input("Введите количество стран для сравнительной выборки: ")

#country = {}

#for i in range(int(count)):
#    inp = input("Введите следующие данные для {0} страны по порядку через запятую:\n"
#    "Название страны, уровень инфляции, курс национальной валюты к доллару США, уровень безработицы, "
#    "доходность от недвижимости, средняя зарплата в национальной страны:\n".format(i+1))
#    inp = inp.split(" ")
#    name = inp[0]
#    inp = list(map(float, inp[1:]))
#    inp.insert(0, name)
#    country[i] = CountryData(inp[0], inp[1], inp[2], inp[3], inp[4], inp[5])
#    print(vars(country[i]))