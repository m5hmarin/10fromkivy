from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class SumApp(App):
    def calculate_sum(self, instance):
        try:
            num1 = float(self.text_input1.text)
            num2 = float(self.text_input2.text)
            result = num1 + num2
            self.result_label.text = "Результат: " + str(result)
        except ValueError:
            self.result_label.text = "Ошибка: Введите числа!"

    def build(self):
        layout = BoxLayout(orientation="vertical", padding=10)

        self.text_input1 = TextInput()
        self.text_input2 = TextInput()

        button = Button(text="Сложить")
        button.bind(on_press=self.calculate_sum)

        self.result_label = Label()

        layout.add_widget(self.text_input1)
        layout.add_widget(self.text_input2)
        layout.add_widget(button)
        layout.add_widget(self.result_label)

        return layout


if __name__ == "__main__":
    SumApp().run()
