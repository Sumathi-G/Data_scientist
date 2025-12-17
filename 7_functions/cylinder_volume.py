
def find_cylinder_volume(radius, height):
    print("radius:", radius)
    print("height:", height)
    volume = 3.14*(radius**2)*height
    print(volume)
    return volume

r = input()
h = input()

a = input()
b = input()

print(find_cylinder_volume(r, h))
print(find_cylinder_volume(a, b))