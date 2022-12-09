file = open("info.txt", "r", encoding="utf-8")
info = file.read().split("\n")

num = 0
while num <= 99 or num > 999:
    num = int(input("Введіть значення від 100 до 999: "))
    if(num <= 99 or num > 999): 
        print("\nНеправильно введене число, потрібно вибрати від 100 до 999")

for time in info:
    value = time.split(" ")
    if(int(value[1]) > num):
        print(time)