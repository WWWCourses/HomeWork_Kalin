#Задача 9. Да се напише програма, която да превръща температура от целзий в фаренхайт.
#Формулата е следната: T (° F) = T (° C) × 1.8 + 32, където c е температурата в целзий и f температурата в
#фаренхайт.
#Примерен изход:
#60°C is 140 in Fahrenheit
#45°F is 7 in Celsius

tc = float(input('Write temperture in Celsius:  '))
tf = tc * 1.8 + 32 
print(f'Tempeture in Fahrenheit is: ', tc)