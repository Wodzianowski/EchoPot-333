
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
import requests
from bs4 import BeautifulSoup
from collections import Counter

class EchoPotLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)

        self.add_widget(Label(text="🎰 EchoPot – EuroJackpot Analyzer", size_hint=(1, 0.1)))
        self.input = TextInput(text='10', hint_text="Ilość losowań", multiline=False, size_hint=(1, 0.1))
        self.add_widget(self.input)

        self.btn = Button(text="🔍 Analizuj", size_hint=(1, 0.15))
        self.btn.bind(on_press=self.analyze)
        self.add_widget(self.btn)

        self.output = Label(text="", size_hint=(1, 1))
        scroll = ScrollView(size_hint=(1, 1))
        scroll.add_widget(self.output)
        self.add_widget(scroll)

    def analyze(self, instance):
        try:
            ilosc = int(self.input.text)
        except:
            self.output.text = "❌ Wprowadź poprawną liczbę"
            return

        wyniki, euro = self.pobierz_wyniki(ilosc)
        if not wyniki:
            self.output.text = "❌ Nie udało się pobrać danych"
            return

        naj = Counter(wyniki).most_common(5)
        wynik = "📊 Najczęstsze liczby:
" + '\n'.join([f"{x[0]} – {x[1]} razy" for x in naj])
        typ = [str(x[0]) for x in naj] + ["+"] + [str(euro[0]), str(euro[1])]
        wynik += "\n\n🤖 Twój typ:\n" + ' '.join(typ)

        self.output.text = wynik

    def pobierz_wyniki(self, ilosc):
        url = "https://www.euro-millions.com/eurojackpot/results"
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers)
        soup = BeautifulSoup(resp.text, "html.parser")

        wyniki_all = []
        euro_all = []

        draws = soup.find_all('ul', class_='balls')[:ilosc]
        for block in draws:
            liczby = block.find_all('li')
            if len(liczby) >= 7:
                glowne = [int(li.text.strip()) for li in liczby[:5]]
                euro = [int(li.text.strip()) for li in liczby[5:7]]
                wyniki_all.extend(glowne)
                euro_all.extend(euro)
        return wyniki_all, euro_all

class EchoPotApp(App):
    def build(self):
        return EchoPotLayout()

if __name__ == "__main__":
    EchoPotApp().run()
