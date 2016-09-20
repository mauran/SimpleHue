"""
Simple Phillips Hue Client
"""
import requests
import json

class SimpleHUE:
    base_url = ''
    username = ''

    def __init__(self, base_url, username):
        self.base_url = base_url
        self.username = username

        if not self.base_url:
            raise Exception('Hue Bridge IP not set')

        if not self.username:
            raise Exception('Username not set')

    def get_lights(self):
        response = requests.get(self.__request_url()).json()
        return response

    def turn_on(self, id):
        body = {'on': True}
        body = json.dumps(body)
        response = requests.put(self.__request_url() + '/' + str(id) + '/state', data=body).json()
        return response


    def turn_of(self, id):
        body = {'on': False}
        body = json.dumps(body)
        response = requests.put(self.__request_url() + '/' + str(id) + '/state', data=body).json()
        return response


    def set_color(self, id, sat, brightness, hue):
        body = {'on': True, 'sat': sat, 'bri': brightness, 'hue': hue}
        body = json.dumps(body)
        response = requests.put(self.__request_url() + '/' + str(id) + '/state', data=body).json()
        return response

    def __request_url(self):
        request_url = self.base_url + '/api/' + self.username + '/lights'
        return  request_url

