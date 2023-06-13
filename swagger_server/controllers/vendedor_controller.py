import connexion
import six

from swagger_server.models.juego import Juego  # noqa: E501
from swagger_server.models.pedido import Pedido  # noqa: E501
from swagger_server import util


def borrar_juego(id_juego):  # noqa: E501
    """Borrar el juego

    Borrar el juego # noqa: E501

    :param id_juego: Borra el juego por id
    :type id_juego: str

    :rtype: List[Juego]
    """
    return 'do some magic!'


def obtener_juego(id_juego):  # noqa: E501
    """Obtiene los juegos

    Obtiene los juegos # noqa: E501

    :param id_juego: Pasa el id del Juego
    :type id_juego: str

    :rtype: List[Juego]
    """
    return 'do some magic!'


def obtener_pedido(id_pedido=None):  # noqa: E501
    """Obtiene los pedidos

    Obtiene los pedidos # noqa: E501

    :param id_pedido: Pasa el id del Pedido
    :type id_pedido: str

    :rtype: List[Pedido]
    """
    return 'do some magic!'


def reemplazar_juego(id_juego, body=None):  # noqa: E501
    """Reemplaza el juego

    Reemplazar el juego # noqa: E501

    :param id_juego: Pasa el id del Juego
    :type id_juego: str
    :param body: Pedido para agregar
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Juego.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
