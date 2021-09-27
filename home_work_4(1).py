

# Создайте программу которая рисует на экране прямоугольник
# из звёздочек заданной пользователем ширины и высоты


str = int(input("Enter how many stars:"))
print("* " * str)

for i in range(str - 2):
    print("* ", "  " * (str - 3), "*")
print("* " * str)


