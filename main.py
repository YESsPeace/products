'''
You don't understand that, because I'm actually noob and I don't understand how work this framework "kivy".
So if you want it, you can't tell me about non-correct using products of the framework <3
'''

from kivy.app import App

from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.uix.modalview import ModalView

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout


class MyApp(App):

    def build(self):

        def deleting(instrance):
            product_name = self.delete_input.text

            for i in range(len(self.product_list)):
                if str(product_name).lower() + '\n' == str(self.product_list[i][1]).lower():
                    del self.product_list[i]
                print(self.product_list)

            file = open('files.txt', 'w')
            file.write('')
            file.close()

            file = open('files.txt', 'a+')
            for k in self.product_list:

                new_line = k[0][0] + '.' + k[0][1] + '.' + k[0][2] + '$' + k[1]

                file.write(new_line)



        def btn_delete_pressed(instrance):
            delete_fl = FloatLayout(size_hint=(1, 1))

            delete_fl.add_widget( ModalView(background_color=[.2, .2, .2, .75]) )

            new_fl = FloatLayout(size_hint=(.6, .5), pos_hint={'x':.2, 'y':.4})

            self.delete_input = TextInput(text='Впишите продукт, который хотите удалить',
                                       multiline=True, font_size = 30,
                                     size_hint=(1, 1), pos_hint={'x':0, 'y':0})
            new_fl.add_widget(self.delete_input)

            new_fl.add_widget(
                Button( text='Выйти',
                    size_hint=(0.5, 0.2), pos_hint={'x':.5, 'y':.0},
                    on_press=btn_exit_pressed, font_size = 24
                )
            )

            new_fl.add_widget(
                Button(text='удалить',
                       size_hint=(.5, .2), pos_hint={'x': .0, 'y': .0},
                       on_press=deleting, font_size = 24
                       )
            )

            delete_fl.add_widget(new_fl)
            big_al.add_widget(delete_fl)

        def btn_exit_pressed(instrance):
            big_al.clear_widgets()
            big_al.add_widget(bl)
            bl.clear_widgets()
            bl.add_widget(btn1)
            bl.add_widget(btn2)

        def adding(instance):
            a = self.textinput.text.split('-')

            my_file = open('files.txt', 'a+')
            my_file.write(a[1])
            my_file.write('$')
            my_file.write(a[0])
            my_file.write('\n')

            my_file.close()



        def btn1_pressed(instance):
            self.textinput = TextInput(text='Название продукта-Дата',
                                       multiline=True, focus=False , font_size = 30)

            bl.clear_widgets()
            bl.add_widget(self.textinput)
            bl.add_widget(btn_add)
            bl.add_widget(btn_exit)

        def btn2_pressed(instrance):
            bl.clear_widgets()
            gl = GridLayout(cols=2)

            try:
                my_file = open('files.txt', 'r')
                s = []

                for line in my_file:
                    a = line.split('$')
                    a[0] = a[0].split('.')
                    s.append(a)
                my_file.close()

                s.sort(key=lambda list: int(list[0][2][-2:] + list[0][1] + list[0][0]))
                self.product_list = s

                count = 0
                for k in s:
                    if count < 6:
                        gl.add_widget(Label(text=k[1], font_size = 30))

                        al = AnchorLayout(anchor_x='right', anchor_y='top')
                        al.add_widget(Label(text=k[0][0] + '.' + k[0][1] + '.' + k[0][2], font_size = 30))
                        al.add_widget(
                            Button(
                                text='X', font_size=26,
                                on_press=btn_delete_pressed,
                                size_hint=(0.2, 0.4), pos_hint={'x':.8, 'y':.6}
                            )
                        )

                        gl.add_widget(al)
                        count +=1
                    else: break

            except FileNotFoundError:
                bl.add_widget(Label(text='Извините, файл не открывается или не создан.'))

            bl.add_widget(gl)
            bl.add_widget(btn_exit)


        bl = BoxLayout(orientation='vertical')
        big_al = AnchorLayout(anchor_x='center', anchor_y='center')

        btn1 = Button(text='Добавить Продукт', font_size = 30)
        btn2 = Button(text='Расписание порчи продуктов', font_size = 30)

        btn_exit = Button(text='Выйти', font_size = 30, size_hint=(1, .3))
        btn_add = Button(text='Добавить', font_size = 30, size_hint=(1, .3))

        btn1.bind(on_press=btn1_pressed)
        btn2.bind(on_press=btn2_pressed)

        btn_add.bind(on_press=adding)
        btn_exit.bind(on_press=btn_exit_pressed)

        bl.add_widget(btn1)
        bl.add_widget(btn2)

        big_al.add_widget(bl)

        return big_al

if __name__ == '__main__':
    MyApp().run()
