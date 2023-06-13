# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.juego import Juego  # noqa: E501
from swagger_server.models.pedido import Pedido  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAdminsController(BaseTestCase):
    """AdminsController integration test stubs"""

    def test_borrar_juego(self):
        """Test case for borrar_juego

        Borrar el juego
        """
        response = self.client.open(
            '/v1/juego/{idJuego}/'.format(id_juego='id_juego_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cancelar_pedido(self):
        """Test case for cancelar_pedido

        Cancelar un pedido
        """
        query_string = [('id_pedido', 'id_pedido_example')]
        response = self.client.open(
            '/v1/pedido',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_crear_pedido(self):
        """Test case for crear_pedido

        Crea un pedido
        """
        body = Pedido()
        response = self.client.open(
            '/v1/pedido',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obtener_juego(self):
        """Test case for obtener_juego

        Obtiene los juegos
        """
        response = self.client.open(
            '/v1/juego/{idJuego}/'.format(id_juego='id_juego_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_obtener_pedido(self):
        """Test case for obtener_pedido

        Obtiene los pedidos
        """
        query_string = [('id_pedido', 'id_pedido_example')]
        response = self.client.open(
            '/v1/pedido',
            method='GET',
            query_string=query_string)
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

    def test_reemplazar_juego(self):
        """Test case for reemplazar_juego

        Reemplaza el juego
        """
        body = Juego()
        response = self.client.open(
            '/v1/juego/{idJuego}/'.format(id_juego='id_juego_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
