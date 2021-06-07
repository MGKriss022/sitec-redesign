from django.db import models
import requests
from bs4 import BeautifulSoup

class NotConnectedException(Exception):
    def __init__(self, message='Not connected to API.'):
        self.message = message
        super().__init__(self.message)



class SitecApi:

    BASE_URL = 'https://sitec.tijuana.tecnm.mx/'
    PANEL_URL = BASE_URL + 'panel/'
    REINSCRIPTION_URL = BASE_URL + 'reinscripcion/'
    CYCLE_ADVANCE_URL = BASE_URL + 'avance-ciclo/'
    KARDEX_URL = BASE_URL + 'kardex/'
    LOG_URL = BASE_URL + 'log/'
    LOGIN_URL = BASE_URL + 'wp-content/themes/fuente/base/validacion.php'

    is_connected = False
    headers = { 'User-Agent': 'Mozilla/5.0'}

    def __init__(self):
        self.session = requests.Session()

    def login(self, control_number, password, captcha):
        response = self.session.post(self.LOGIN_URL, data={
            'numero_control': control_number,
            'clave': password,
            'g-recaptcha-response': captcha
        })
        if response.status_code == 200:
            self.is_connected = True

    def retrieve_panel_data(self):
        if not self.is_connected:
            raise NotConnectedException()

        html = self.session.get(self.PANEL_URL).text
        soup = BeautifulSoup(html, 'html.parser')
        personal_information_html = soup.find_all('div', class_='student-school-info-escolar')[0]
        personal_information = {}
        for div in personal_information_html.find_all('div'):
            name = div.get('class')[0]
            title = div.find('strong').text
            value = div.find('span').text
            personal_information[name] = {
                'title': title,
                'value': value
            }
        return personal_information
        


    def retrieve_reinscription_data(self):
        pass

    def retrieve_cycle_advance_data(self):
        pass

    def retrieve_kardes_data(self):
        pass

    def retrieve_log_data(self):
        pass

