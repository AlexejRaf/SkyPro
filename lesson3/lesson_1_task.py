#my_name = "Алексей"
#print(my_name)

#my_age = 26
#my_age = 29
#print(my_age)

#first_name = "Алексей"
#last_name = "Скрипников"

#print("Вас зовут", first_name, last_name)

#def print_greeting():
    #print("Привет, мир!")

#print_greeting()

#Lesson1 = "Ddfregfgredbdrtdrjhjhgjghfg"
#count = len(Lesson1)
#Lesson2 = "dfsdfesvcv"
#count2 = len(Lesson2)
#count3 = count + count2
#print(count3)

#result = round(10.25, 1)
#print(result)

distance = 450        # расстояние, км
fuel_consumption = 8.4  # расход топлива, л/100 км
fuel_price = 64.2     # цена топлива, руб./литр
passengers = 4        # количество пассажиров

# BEGIN (write your solution here)
fuel_volume = (fuel_consumption * distance) / 100
trip_cost = fuel_price * distance
cost_of_the_trip = trip_cost / passengers