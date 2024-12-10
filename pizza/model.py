import json
from datetime import date

log = open("log.txt", 'a', encoding='utf-8')
def load_menu(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


# Функция для отображения меню
def display_menu(menu):
    print("Меню:")
    print("\nЕда:")
    for item in menu['food']:
        print(f"- {item['name']} (Цена: {item['price']} руб.)")

    print("\nБезалкогольные напитки:")
    for item in menu['non_alcoholic_drinks']:
        print(f"- {item['name']} (Цена: {item['price']} руб.)")

    print("\nАлкогольные напитки:")
    for item in menu['alcoholic_drinks']:
        print(f"- {item['name']} (Цена: {item['price']} руб.)")

# Функция для отображения меню
def display_add(menu):
    print("Меню:")
    print("\nЕда:")
    for item in menu['toppings']:
        print(f"- {item['name']} (Цена: {item['price']} руб.)")

# Функция для отображения меню
def display_products(menu):
    print("Кол-во продуктов:")
    for item in menu['toppings']:
        print(f"- {item['name']} (Кол-во: {item['count']} шт.)")


# Функция для выбора позиций из меню
def choose_items(menu, age, mass_eats):
    total_price = 0
    while True:
        item_name = input("\nВведите название позиции для заказа (или 'выход' для завершения, 'добавки' для заказа добавок): ").strip()

        if item_name.lower() == 'выход':
            break
        if item_name.lower() == 'добавки':
            choose_additives(mass_eats, total_price)

        # Проверка на наличие позиции в меню
        found = False
        for category in ['food', 'non_alcoholic_drinks', 'alcoholic_drinks']:
            for item in menu[category]:
                if item['name'].lower() == item_name.lower():
                    found = True
                    if category == 'alcoholic_drinks' and (date.today().year)-age < 18:
                        print("Вы не можете заказать алкогольные напитки, так как вам нет 18 лет.")
                    else:
                        total_price += item['price']
                        mass_eats.append(item['name'])
                        print(f"Вы добавили {item['name']} к заказу.")
                        log.write(f'{item["name"]} - добавлено в корзину\n')
                    break
            if found:
                break

        if not found:
            print("Эта позиция не найдена в меню. Попробуйте снова.")
    return total_price


def choose_additives(mass_eats, total_price):
    with open('additives.json', 'r', encoding='utf-8') as file:
        menu = json.load(file)
        display_add(menu)
    price = 0

    while True:

        item_name = input("\nВведите название позиции для заказа (или ' выход' для завершения): ").strip()

        if item_name.lower() == 'выход':
            break

        # Проверка на наличие позиции в меню
        found = False
        for item in menu['toppings']:
            if item['name'].lower() == item_name.lower():
                found = True

                price += item['price']
                mass_eats.append(item['name'])
                print(f"Вы добавили {item['name']} к заказу.")
                accounting(item['name'])
                log.write(f'{item["name"]} - добавлено в корзину\n')
                break
            if found:
                break

        if not found:
            print("Эта позиция не найдена в меню. Попробуйте снова.")
    return price

def accounting(product):
    with open('products.json', 'r', encoding='utf-8') as file:
        products = json.load(file)

    # Проверка на наличие позиции в меню
    found = False
    for item in products['toppings']:
        if item['name'].lower() == product.lower():
            found = True

            item['count'] -= 1
            break
        if found:
            break

    with open('products.json', 'w', encoding='utf-8') as file:
        json.dump(products, file, ensure_ascii=False, indent=4)