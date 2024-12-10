import json

log = open("log.txt", 'a', encoding='utf-8')
rest_menu = open('menu.json', 'r')
chek = open('chek.txt', 'a')

def is_valid_age(age):
    return age.isdigit() and int(age) > 0


# Функция для регистрации пользователя
def register_user(username, password, age):
    user_data = {}

    # Проверка, существует ли пользователь
    if username in user_data:
        print("Пользователь уже существует.")
        return False

    # Добавление нового пользователя
    user_data[username] = {
        "password": password,
        "age": age
    }

    # Сохранение данных в JSON файл
    with open('users.json', 'w') as file:
        json.dump(user_data, file)
    with open('log.txt', 'a') as log:
        log.write(f'{user_data[username]} - регистрация\n')
    print("Пользователь зарегистрирован.")
    return True


# Функция для входа пользователя
def login_user(username, password):


    with open('users.json', 'r') as file:
        user_data = json.load(file)

    # Проверка данных пользователя
    if username in user_data and user_data[username]["password"] == password:
        print("Вход выполнен успешно.")
        with open('log.txt', 'a', encoding='utf-8') as log:
            log.write(f'{username, user_data[username]} - вход\n')
        print(f"Возраст пользователя: {user_data[username]['age']}")
        return True
    else:
        print("Неверное имя пользователя или пароль.")
        return False

def do_chek(mass, schet, enter):
    mass_eat = mass
    mass = []
    mass.append("=" * 30)
    mass.append("Ваш чек:")
    #mass = mass[1:]
    for eat in set(mass_eat):
        mass.append(f"{eat}: {150} руб. Х {mass_eat.count(eat)} шт.")
    mass.append(f"Итого к оплате: {schet} руб.")
    mass.append(f"Внесено: {enter} руб.")
    mass.append(f"Сдача: {enter - schet} руб.")
    mass.append("=" * 30)
    return mass


def load_promo_codes(file_name):
    """Загружает промокоды из JSON файла, если файл существует."""
    try:
        with open(file_name, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}


def save_promo_codes(file_name, promo_codes):
    """Сохраняет промокоды в JSON файл."""
    with open(file_name, 'w') as json_file:
        json.dump(promo_codes, json_file, indent=4)


def make_promo():
    file_name = 'promo_codes.json'

    # Загружаем существующие промокоды
    promo_codes = load_promo_codes(file_name)

    # Запрашиваем у администратора название промокода
    print('Пожалуйста, соблюдайте этику и не пишите нецензурных слов.')
    promo = input('Напишите название промокода на английском языке: ')

    # Запрашиваем процент скидки
    discount = input('Введите процент скидки (например, 10 для 10%): ')

    # Проверяем, является ли введенное значение числом
    try:
        discount = float(discount)
        if discount < 0 or discount > 100:
            raise ValueError("Процент скидки должен быть в диапазоне от 0 до 100.")
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    # Добавляем новый промокод и его скидку в словарь
    promo_codes[promo] = discount

    # Сохраняем обновленный список промокодов в файл
    save_promo_codes(file_name, promo_codes)

    print(f'Промокод "{promo}" с скидкой {discount}% успешно добавлен.')


