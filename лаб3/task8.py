money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
while money_capital > 0:
    spend = spend + spend * increase
    money_capital = money_capital+salary-spend
    if money_capital > 0:
      month = month+1

# TODO Оформить решение

print(month)
