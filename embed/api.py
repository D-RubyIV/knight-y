import requests


class EmbedApi:
    def __init__(self, port: int = 5000):
        self.url = "http://127.0.0.1:{}".format(port)

    def embed_tab(self, handle, **kwargs):
        """params: index
        new=False or True"""
        params = {"handle": handle}
        params.update(kwargs)
        path = "/embed"
        url = self.url + path
        response = requests.get(url, params=params)

    def unembed_tab(self, handle):
        params = {"handle": handle}
        path = "/unembed"
        url = self.url + path
        response = requests.get(url, params=params)
        print(response.text)