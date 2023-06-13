import connexion
import six

from swagger_server.models.juego import Juego  # noqa: E501
from swagger_server.models.pedido import Pedido  # noqa: E501
from swagger_server import util


def obtener_juego(id_juego):  # noqa: E501
    """Obtiene los juegos

    Obtiene los juegos # noqa: E501

    :param id_juego: Pasa el id del Juego
    :type id_juego: str

    :rtype: List[Juego]
    """
    return 'do some magic!'


def obtener_total(total):  # noqa: E501
    """Obtiene el valor total de los juegos

    Obtiene el valor total de los juegos # noqa: E501

    :param total: Pasa el id de la cuenta
    :type total: int

    :rtype: List[Pedido]
    """
    return 'do some magic!'
