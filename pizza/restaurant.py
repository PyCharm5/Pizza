schet = 0
chek = []

mass = list(map(str, input().split()))
enter = int(input('Сколько внесено:  '))

def do_chek(mass, schet):
    chek.append("="*30)
    chek.append("Ваш чек:")
    for eat in set(mass):
        chek.append(f"{eat}: {rest_menu.get(eat)} руб. Х {mass.count(eat)} шт.")
    chek.append("")
    chek.append(f"Итого к оплате: {summ(mass, schet)} руб.")
    chek.append(f"Внесено: {enter} руб.")
    chek.append(f"Сдача: {enter - summ(mass, schet)} руб.")
    chek.append("=" * 30)
