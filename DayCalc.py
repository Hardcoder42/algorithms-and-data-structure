days = input('Введите количество суток: ')
hours = int(days) * 24
min = int(hours) * 60
sec = int(min) * 60

info = f"{days} суток = {hours} часов = {min} минут = {sec} секунд"
print(info)