import requests


class Notify:
    
    def __init__(self) -> None:
        self.__base_url = 'https://webhook.site'

    
    def send_event(self, data):
        requests.post(url=f'{self.__base_url}/e858ebb6-092a-4497-9ea3-cc19c33e4285', json=data)
        