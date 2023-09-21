# coding: utf-8
import requests

class ConFirmaClient(object):
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.url = 'https://app.confirma.es'
        self.session = requests.Session()
        self.session.auth = (user, password)

    def create_signature(self, canal, tipo, tipofirma, datos):
        """
        :param canal: canal string
        :type canal: string
        :param tipo: string
        :type tipo: tipo de peticion
        :param tipofirma: string
        :type tipofirma: Simple o Multi
        :param datos: Dictionary
        :type datos: Dictionary of optional parameters
        :return: A dictionary with signature information
        :rtype: dict
        """
        url = '/'.join([self.url, 'ws_API.php'])

        json_data = {
            "canal": canal,
            "tipo": tipo,
            "tipofirma": tipofirma,
            "datos": datos
        }
        return self.session.post(
            url, json=json_data
        ).json()
