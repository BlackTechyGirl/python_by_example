import math

radius = int(input('radius: '))
depth = int(input('depth: '))
area = math.pi*(radius**2)
volume = area*depth
print(round(volume, 3))

