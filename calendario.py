import calendar

# Obter o calendário do mês atual
cal = calendar.monthcalendar(2023, 3)

# Imprimir o calendário formatado
print(calendar.month_name[3], 2023)
print('Mo Tu We Th Fr Sa Su')
for week in cal:
    week_str = ''
    for day in week:
        if day == 0:
            week_str += '   '
        else:
            week_str += f'{day:2d} '
    print(week_str)
