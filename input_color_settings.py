color_set_file = open('color_settings.txt', 'r+')

color_list = ''

for line in color_set_file:
    color_list += line

color_list = color_list.split('$')

for i in range(len(color_list)):
    color_list[i] = color_list[i].split('\n')
    for k in range(1, len(color_list[i])):
        color_list[i][k] = color_list[i][k].split(':')
        try:
            color_list[i][k][1] = color_list[i][k][1].split(',')
            for j in range(len(color_list[i][k][1])):
                color_list[i][k][1][j] = float(color_list[i][k][1][j])
        except ValueError:
            continue
        except IndexError:
            continue

print(color_list)

btn1_color = color_list[0][1][1]
btn2_color = color_list[0][2][1]
btn_exit_color = color_list[0][3][1]
btn_add_color = color_list[0][4][1]
window_color = color_list[0][5][1]
gridlayout_color = color_list[0][6][1]
btn_delete_color = color_list[0][7][1]

print(
    btn1_color,
    btn2_color,
    btn_exit_color,
    btn_add_color,
    window_color,
    gridlayout_color,
    btn_delete_color,
    sep = ' |'
)