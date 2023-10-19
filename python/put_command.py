import cv2
import numpy

img = cv2.imread('python/test.png')
file_path = "python/cmd.mcfunction"
file_path = "C:/Users/Owner/AppData/Roaming/.minecraft/saves/aaae/datapacks/dot/data/dot_pack/functions/cmd.mcfunction"

max_y, max_x, max_z = 0, 0, 0
for i, item in enumerate(img):
    for j, item2 in enumerate(item):
        if 1 <= i <= 20 and 1 <= j <= 62 and i != 0 and i != 63 and j != 0 and j != 21:
            if list(item2) == [0, 0, 0]:
                if max_y < i:
                    max_y = i
                if max_x < j:
                    max_x = j
        if 43 <= i <= 62 and 1 <= j <= 62 and i != 42 and i != 63 and j != 0 and j != 63:
            if list(item2) == [0, 0, 0]:
                if max_z < j:
                    max_z = j

view1 = [1, 1]
view2 = [22, 1]
view3 = [43, 1]

model_list = []
for y, y2 in enumerate(reversed(range(max_y))):
    model_list.append([])
    for x in range(max_x):
        model_list[y].append([])
        for z in range(max_z):
            if list(img[view1[0]+y2][view1[1]+x]) == [0, 0, 0] and list(img[view2[0]+z][view2[1]+x]) == [0, 0, 0] and list(img[view3[0]+y2][view3[1]+z]) == [0, 0, 0]:
                model_list[y][x].append(True)
            else:
                model_list[y][x].append(False)

print(y, x, z)
command_list = []
for y, item_y in enumerate(model_list):
    for x, item_x in enumerate(item_y):
        for z, item_z in enumerate(item_x):
            if item_z:
                command_list.append(f"setblock {x} {y} {z} minecraft:stone")
            else:
                command_list.append(f"setblock {x} {y} {z} minecraft:air")

with open(file_path, mode='w') as f:
    f.write('\n'.join(command_list))