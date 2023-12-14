import os # Импорт библиотек
from tkinter import *
from tkinter import font
from tkinter.messagebox import showinfo, showerror

def check_login(): # Проверяем наличие логина в файле
    if os.path.exists("text.txt"):
        file = open("text.txt", "r+")
        with open("text.txt", "r") as file:
            lines = file.readlines()
            login_input = login.get()
            for line in lines:
                if login_input in line:
                    return True
        return False

def check_users(): # Проверяем наличие данных в файле о пользователе
    if os.path.exists("text.txt"):
        file = open("text.txt", "r+")
        lines = file.readlines()
        login_input = login.get()
        password_input = password.get()
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2:
                stored_login, stored_password = parts
                if login_input == stored_login and password_input == stored_password:
                    return True
        return False
    
def registration_user(): # Регистрируем пользователя
    if not login.get() or not password.get():
        showerror("Ошибка", "Поля 'Логин' и 'Пароль' должны быть заполнены.")
    elif check_login():
        showerror("Ошибка", "Учетная запись с таким логином уже существует.")
    else:
        with open("text.txt", "a") as file:
            file.write(f"{login.get()}:{password.get()}\n")
        root.destroy()
        showinfo("Успех", "Регистрация успешно завершена. При следующем входе введите свои данные, чтобы войти в игру!")

def enter_users(): # Авторизуем пользователя
    def start_game(): # Запускаем игровое окно, если пользователь выполнил вход в свой аккаунт
        root.destroy()
        game = Tk()
        game.title("Игра")
        game.geometry("800x600")
        game.configure(background = "#fcfcfc")
        game.mainloop()
    
    if check_users():
        showinfo("Успех!", "Вы вошли в свой аккаунт")
        start_game()
    else:
        showerror("Ошибка", "Неверный логин или пароль.")

root = Tk() # Создаем окно
root.title("Окно регистрации пользователя") # Устанавливаем заголовок окна
root.geometry("800x600") # Устанавливаем размеры окна
root.configure(background = "#fa8d07")
font1 = font.Font(family = "Verdana", size = 17, weight = "normal", slant = "roman") # Настройка шрифта
llogin = Label(font = font1, anchor = W, background = "#fa8d07", text = "Введите логин") 
llogin.pack(padx = 6, pady = 6)
login = Entry(bd = 2)
login.pack(padx = 6, pady = 6)
lpassword = Label(font = font1, anchor = W, background = "#fa8d07", text = "Введите пароль") 
lpassword.pack(padx = 6, pady = 6)
password = Entry(bd = 2, show = "*")
password.pack(padx = 6, pady = 6)
btn1 = Button(text = "Вход", bg = "#121212", fg = "#FFFFFF", font = font1, command = enter_users)
btn1.pack(padx = 6, pady = 6) 
btn2 = Button(text = "Регистрация", bg = "#121212", fg = "#FFFFFF", font = font1, command = registration_user)
btn2.pack(padx = 6, pady = 6) 

root.mainloop()
