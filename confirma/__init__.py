# coding: utf-8
import requests


class Document(object):
    read_required = True
    template_type = None
    template_reference = None
    template_code = None

    def __init__(self, **attrs):
        for k, v in attrs.items():
            setattr(self, k, v)

    def serialize(self):
        """
        :return: A document serialized in JSON
        :rtype: dict
        """
        return {
            "templateType": self.template_type,
            "templateReference": self.template_reference,
            "readRequired": self.read_required,
            "watermarkText": "Preview",
            "templateCode": self.template_code
        }


class Base64Document(Document):
    templateType = "base64"

    def __init__(self, content, **attrs):
        super(Base64Document, self).__init__(**attrs)
        self.content = content

    def serialize(self):
        result = super(Base64Document, self).serialize()
        result["templateReference"] = self.content
        return result

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
