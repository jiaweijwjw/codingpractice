import enum

class Color(enum.Enum):
    red = 0
    white = 1
    blue = 2

for color in Color:
    print(color) # Color.red, Color.white, Color.blue
    print(color.name) # red, white, blue
    print(color.value) # 0, 1, 2

print(Color["red"]) # Color.red
print(Color(0)) # Color.red
print(Color["red"].value) # 0
print(Color(0).name) # red

new_color = Color.white
print(new_color) # Color.white

# basically you can just use the Color.color as a "state"
# but if you want to compare with other values, you can use the name or value property