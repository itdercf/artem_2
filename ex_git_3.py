max_m = 0
day = ""
sum_lipki = 0
sum_distance = 0
punkt_sending = {}
sum_mass_punkt_sending = 0
sum_mass_punkt_naznach = 0
punkt_sending_set = set()
punkt_naznach = {}
punkt_naznach_set = set()
sum_fuel_punkt_naznach = 0
fuel = {}
n_list = []
max_sr_fuel = 0
punkt_naznach_fuel_max = ""
f = open("B:\git\перевозки.txt", 'r')
for i in f:
    n = 0
    l = []
    l = i.split()
    if (int(l[6]) > max_m):
        day = ""
        day = day + l[0] + ' ' + l[1] 
        max_m = int(l[6])
    punkt_sending_set.add(l[2])
    punkt_naznach_set.add(l[3])
    for i in punkt_sending_set:
        if l[2] == i:
            sum_mass_punkt_sending += int(l[6])
            punkt_sending[i] = sum_mass_punkt_sending
    for i in punkt_naznach_set:
        if l[3] == i:
            sum_mass_punkt_naznach += int(l[6])
            punkt_naznach[i] = sum_mass_punkt_naznach
    for i in punkt_naznach_set:
            if l[3] == i:
                 n += 1
                 sum_fuel_punkt_naznach += (int(l[5]) / n)
                 fuel[i] = sum_fuel_punkt_naznach
    for i in punkt_naznach_set:
         if fuel[i] > max_sr_fuel:
              max_sr_fuel = fuel[i]
              punkt_naznach_fuel_max = ""
              punkt_naznach_fuel_max = i

                 
f.close()
print(f"{day} перевезнено больше всего грузов, суммарная масса равна {max_m}")
print(f"суммарная масса грузов, доставленных в Липки, равна {sum_lipki}")
print(f"{sum_distance} - суммарное расстояние за 1 октября, которое проехал грузовой автомобиль")
print(f"{len(punkt_sending)} - общее число пунктов отправления, \n {punkt_sending}")
print(f"{len(punkt_naznach)} - общее число пунктов назначения, \n {punkt_naznach}")
print(f"{punkt_naznach_fuel_max} - пункт назначения  с наибольшим средним расходом бензина")
