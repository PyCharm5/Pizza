file = open('chek.txt', 'w', encoding='utf-8')

def price_print(total_price, mass_eats, chek):
    print(f"\nИтоговая цена: {total_price} руб. Заказано: {', '.join(mass_eats)}")

    for el in chek:
        file.writelines(el)
        file.writelines("\n")
        print(el)