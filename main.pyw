import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder


API_KEY = "baf0940b-64a8-4015-a41c-3e2df1009ad9"

Builder.load_file("design.kv")


class AppLayout(Widget):
    print("Things")



class CryptoApp(App):
    def build(self):
        return AppLayout()


if __name__ == "__main__":
    CryptoApp().run()