# There is a circle road with N petrol pumps. The petrol pumps are numbered 0 to (N−1) (both inclusive). 
# For each petrol pump, you will receive two pieces of information (separated by a single space):  
# The amount of petrol the petrol pump will give you 
# The distance from that petrol pump to the next petrol pump (kilometers) 
# You are a truck driver, and you want to go all around the circle. 
# You know that the truck consumes 1 liter of petrol per 1 kilometer, and its tank has infinite petrol capacity. 
# In the beginning, the tank is empty, 
# but you start your journey at a petrol pump so you can fill it with the given amount of petrol. 
# Your task is to calculate the first petrol pump from where the truck will be able to complete the circle. 
# You never miss filling its tank at a petrol pump. 

from collections import deque

number_of_pumps = int(input())
pumps = deque()

for _ in range(number_of_pumps):
    fuel, distance = map(int, input().split())
    pumps.append((fuel, distance))

starting_position = 0
stops = 0

while stops < number_of_pumps:
    tank_fuel = 0
    for fuel, distance in pumps:
        tank_fuel += fuel
        if tank_fuel < distance:
            starting_position += 1
            pumps.rotate(-1)
            stops = 0
            break
        tank_fuel -= distance
        stops += 1

print(starting_position)
