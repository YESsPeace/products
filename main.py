'''
You don't understand that, because I'm actually noob and I don't understand how work this framework "kivy".
So if you want it, you can't tell me about non-correct using products of the framework <3
'''

from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.uix.modalview import ModalView
from CustomModules import CustomGraphics

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout

from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

class MyApp(App):

    def build(self):

        def btn_settings_pressed(instrance):
            pass

#______________________________________Color_Settings___________________________________________________________________
        try:
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
            color_set_file.close()
        except FileNotFoundError:
            color_list = open('color_settings.txt', 'a+')

            color_list.write('default_color_day:' + '\n')
            color_list.write('    btn: .47058823529, .2862745098, .42745098039, 1' + '\n')
            color_list.write('    window: .2, .2, .2, 1' + '\n')
            color_list.write('    layout: .72156862745, .53725490196, .67843137255, 1' + '\n')

            color_list.write('$default_color_night:' + '\n')
            color_list.write('    btn:' + '\n')
            color_list.write('    window:' + '\n')
            color_list.write('    layout:' + '\n')

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
        color_set_file.close()

        btn_color = color_list[0][1][1]
        window_color = color_list[0][2][1]
        layout_color = color_list[0][3][1]
#______________________________________Color_Settings___________________________________________________________________

        def deleting(instrance):

            product_name = s[int(str(btn_delete_text)[-2])][1]
            print(product_name)
            print(self.product_list)

            for i in range(len(self.product_list)):
                try:
                    if str(product_name).lower() == str(self.product_list[i][1]).lower():
                        del self.product_list[i]
                        print(self.product_list)
                except IndexError:
                    print(self.product_list)
                    continue

            file = open('files.txt', 'w')
            file.write('')
            file.close()

            file = open('files.txt', 'a+')
            for k in self.product_list:

                new_line = k[0][0] + '.' + k[0][1] + '.' + k[0][2] + '$' + k[1]

                file.write(new_line)

        def btn_delete_pressed(instance):
            print(s)
            global delete_fl, btn_delete_text

            btn_delete_text = instance.text
            print(btn_delete_text)

            delete_fl = FloatLayout()

            delete_fl.add_widget(ModalView(background_color=[.2, .2, .2, .75], ))

            new_fl = FloatLayout(size_hint=(.6, .5), pos_hint={'x':.2, 'y':.4})

            accept = Label(text='Подтвердите', font_size=60, pos_hint={'x':.0, 'y':.0})
            CustomGraphics.SetBG(accept, bg_color=[layout_color[0], layout_color[1], layout_color[2],
                                               layout_color[3]])
            new_fl.add_widget(accept)

            new_fl.add_widget(
                Button( text='Выйти',
                    size_hint=(0.5, 0.2), pos_hint={'x':.5, 'y':.0},
                    on_press= btn_exit_moadl_view_pressed, font_size = 45
                )
            )

            new_fl.add_widget(
                Button(text='удалить',
                       size_hint=(.5, .2), pos_hint={'x': .0, 'y': .0},
                       on_press=deleting, font_size = 45
                       )
            )

            delete_fl.add_widget(new_fl)
            big_al.add_widget(delete_fl)

        def btn_exit_moadl_view_pressed(instrance):
            big_al.remove_widget(delete_fl)
            return btn2_pressed(instrance)

        def btn_exit_pressed(instrance):
            big_al.clear_widgets()
            big_al.add_widget(bl)
            bl.clear_widgets()
            bl.add_widget(fl_al)
            bl.add_widget(btn1)
            bl.add_widget(btn2)

        def adding(instance):
            print(self.textinput.text)
            print(self.textinput.text.split())
            a = self.textinput.text.split()

            my_file = open('files.txt', 'a+')
            my_file.write(a[-1])
            my_file.write('$')
            a_to_write_name = ''

            for i in range(len(a) -1):
                a_to_write_name += str(a[i]) + ' '

            my_file.write(a_to_write_name)
            my_file.write('\n')

            my_file.close()

        def btn1_pressed(instance):
            self.textinput = TextInput(text='Впишите название продукта и дату через пробел',
                                       multiline=True, focus=False , font_size = 40)

            bl.clear_widgets()
            bl.add_widget(self.textinput)
            bl.add_widget(btn_add)
            bl.add_widget(btn_exit)

        def btn2_pressed(instrance):
            global s

            bl.clear_widgets()
            gl = GridLayout(cols=2, size_hint_y=None, spacing=5, row_default_height = 200)
            gl.bind(minimum_height=gl.setter('height'))
            scrollBar = ScrollView(size_hint=(1, 1), size=(Window.width, Window.height))
            scrollBar.add_widget(gl)

            try:
                my_file = open('files.txt', 'r+')
                s = []

                for line in my_file:
                    a = line.split('$')

                    count_dut = 0
                    for h in range(len(a[0])):
                        if a[0][h] == '.': count_dut += 1
                    if not count_dut == 0:
                        a[0] = a[0].split('.')
                        s.append(a)
                my_file.close()
                print(s)

                s.sort(key=lambda list: int(list[0][2][-2:] + list[0][1] + list[0][0]))
                self.product_list = s
                print(s)

                if s == []:
                    bl.add_widget(Label(text='Извините, файл создан, но пуст.'))
                    bl.add_widget(btn_exit)
                    return


                idintif = 0
                for k in s:
                    lb = Label( text=k[1][:-1], font_size = 60, size_hint_y=None, height = 200)
                    CustomGraphics.SetBG(lb, bg_color=[layout_color[0], layout_color[1], layout_color[2], layout_color[3]])
                    gl.add_widget(lb)

                    al = AnchorLayout(anchor_x='right', anchor_y='top', size_hint_y=None, height = 200)
                    al.add_widget(Label( text=k[0][0] + '.' + k[0][1] + '.' + k[0][2], font_size = 60 ))
                    al.add_widget(
                        Button(
                            text='X' + '[' + str(idintif) + ']', font_size=40,
                            on_press=btn_delete_pressed,
                            size_hint=(None, None), pos_hint={'x':.8, 'y':.8},
                            size=[75, 75], background_color=(btn_color[0], btn_color[1], btn_color[2], btn_color[3]),
                            opacity = 50, background_normal = ''
                        )
                    )
                    idintif += 1
                    CustomGraphics.SetBG(al, bg_color=[layout_color[0], layout_color[1], layout_color[2], layout_color[3]], background_normal = '')
                    gl.add_widget(al)

            except FileNotFoundError:
                bl.add_widget(Label(text='Извините, файл не открывается или не создан.'))

            bl.add_widget(scrollBar)
            bl.add_widget(btn_exit)

        bl = BoxLayout(orientation='vertical', spacing=5, padding=5)
        big_al = AnchorLayout(anchor_x='center', anchor_y='center', )
        fl_al = FloatLayout(size_hint=(1, .3))

        btn1 = Button(text='Добавить Продукт', font_size = 60, background_color=(btn_color[0], btn_color[1], btn_color[2], btn_color[3]), background_normal = '')
        btn2 = Button(text='Расписание порчи продуктов', font_size = 60, background_color=(btn_color[0], btn_color[1], btn_color[2], btn_color[3]), background_normal = '')

        btn_exit = Button(text='Выйти', font_size = 60, size_hint=(1, .3), background_color=(btn_color[0], btn_color[1], btn_color[2], btn_color[3]), background_normal = '')
        btn_add = Button(text='Добавить', font_size = 60, size_hint=(1, .3), background_color=(btn_color[0], btn_color[1], btn_color[2], btn_color[3]), background_normal = '')

        btn_settings = Button( text='Настройки', font_size = 60, background_color=(btn_color[0], btn_color[1], btn_color[2], btn_color[3]), background_normal = '' , on_press=btn_settings_pressed, size_hint=(0.5, 1), pos_hint={'x':.0, 'y':.0} )

        Window.clearcolor =(window_color[0], window_color[1], window_color[2], window_color[3])

        btn1.bind(on_press=btn1_pressed)
        btn2.bind(on_press=btn2_pressed)

        btn_add.bind(on_press=adding)
        btn_exit.bind(on_press=btn_exit_pressed)

        bl.add_widget(fl_al)
        bl.add_widget(btn1)
        bl.add_widget(btn2)

        fl_al.add_widget(btn_settings)

        big_al.add_widget(bl)

        return big_al

if __name__ == '__main__':
    MyApp().run()