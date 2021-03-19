import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import StringProperty


Builder.load_file("design.kv")


class AppLayout(Widget):
    formatted_bitcoin = StringProperty("")
    formatted_etherium = StringProperty("")


class CryptoApp(App):
    def build(self):
        Clock.schedule_once(lambda dt: self.get_cryptos_info(), 1)
        return AppLayout()

    def get_cryptos_info(self):
        """Get the current price for Bitcoin and Ethereum."""

        API_KEY = "baf0940b-64a8-4015-a41c-3e2df1009ad9"
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        parameters = {"symbol": "BTC,ETH"}
        headers = {"Accepts": "application/json", "X-CMC_PRO_API_KEY": API_KEY}
        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            crypto_info = json.loads(response.text)["data"]

            bitcoin_price = crypto_info["BTC"]["quote"]["USD"]["price"]
            etherium_price = crypto_info["ETH"]["quote"]["USD"]["price"]

            self.root.formatted_bitcoin = f"Bitcoin: ${bitcoin_price:.2f}"
            self.root.formatted_etherium = f"Etherium: ${etherium_price:.2f}"
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


if __name__ == "__main__":
    CryptoApp().run()
