import json
from datetime import date
from controller import register_user, login_user, is_valid_age, do_chek, load_promo_codes, save_promo_codes, make_promo
from model import load_menu, display_menu, choose_items, choose_additives, display_products
from view import price_print
import getpass


if __name__ == "__main__":
    action = input("Введите 'register' для регистрации или 'login' для входа: ").strip().lower()
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")  #getpass.getpass(prompt='Password: ', stream=None)
    menu = open('menu.json', 'r')
    products = open('products.json', 'r')
    menu_additives = open('additives.json', 'r')
    users = open('users.json', 'r')
    chek = open('chek.txt', 'w', encoding='utf-8')


    if action == 'register':
        age = input("Введите возраст: ")
        while not is_valid_age(age):
            print("Возраст должен быть положительным целым числом. Попробуйте снова.")
            age = input("Введите возраст: ")
        register_user(username, password, int(age))
    elif action == 'login':
        login_user(username, password)
    else:
        print("Неверное действие.")

    menu = load_menu('menu.json')
    additives = load_menu('additives.json')
    with open('users.json', 'r') as file:
        user_data = json.load(file)
    # Запрос возраста у пользователя
    age = user_data[username]['age']

    isAdmin = user_data[username]['isAdmin']
    if isAdmin:
        choose = bool(input('Проверить остатки продуктов?  '))
        if choose:
            with open('products.json', 'r', encoding='utf-8') as file:
                menu = json.load(file)
                display_products(menu)
        else:
            # Отображение меню
            display_menu(menu)

            # Выбор позиций из меню
            mass_eats = []
            total_price = choose_items(menu, age, mass_eats)
            total_price += choose_additives(mass_eats, total_price)

            #do_chek(mass_eats, total_price, int(input("Введите внесённую сумму:  ")))

            price_print(total_price, mass_eats, do_chek(mass_eats, total_price, int(input("Введите внесённую сумму:  "))))


