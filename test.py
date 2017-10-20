base_point_x = 1
base_point_y = 1
width = 100
height = 200
g1 = {'x': base_point_x + width * 0.183, 'y': base_point_y + height * 0.211}
g2 = {'x': base_point_x + width * 0.519, 'y': base_point_y + height * 0.211}
g3 = {'x': base_point_x + width * 0.815, 'y': base_point_y + height * 0.211}
g4 = {'x': base_point_x + width * 0.183, 'y': base_point_y + height * 0.447}
g5 = {'x': base_point_x + width * 0.519, 'y': base_point_y + height * 0.447}
g6 = {'x': base_point_x + width * 0.815, 'y': base_point_y + height * 0.447}
g7 = {'x': base_point_x + width * 0.183, 'y': base_point_y + height * 0.658}
g8 = {'x': base_point_x + width * 0.519, 'y': base_point_y + height * 0.658}
g9 = {'x': base_point_x + width * 0.815, 'y': base_point_y + height * 0.658}
z = [g1, g2, g3, g6, g5, g7, g9]
print(g2['x']-g1['x'])
print(g1['x']-g9['x'])

moveX = []
moveY = []
for i in range(len(z)):
    if i == 0:
        continue
    X = z[i]['x'] - z[i - 1]['x']
    Y = z[i]['y'] - z[i - 1]['y']
    moveX.append(X)
    moveY.append(Y)
print(moveX)


