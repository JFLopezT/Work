# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.juego import Juego  # noqa: E501
from swagger_server.models.pedido import Pedido  # noqa: E501
from swagger_server.test import BaseTestCase


class TestClienteController(BaseTestCase):
    """ClienteController integration test stubs"""

    def test_obtener_juego(self):
        """Test case for obtener_juego

        Obtiene los juegos
        """
        response = self.client.open(
            '/v1/juego/{idJuego}/'.format(id_juego='id_juego_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obtener_total(self):
        """Test case for obtener_total

        Obtiene el valor total de los juegos
        """
        response = self.client.open(
            '/v1/pedido/{total}/'.format(total=789),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
