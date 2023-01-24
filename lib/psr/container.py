""" PHP PSR-11 Container interface port (see https://www.php-fig.org/psr/psr-11/). """

import typing


# Metadata
__version__ = '1.1.0'
__all__ = (
  # Metadata
  '__version__',
  # Contract
  'ContainerInterface',
  'ContainerExceptionInterface',
  'NotFoundExceptionInterface',
)


# Contract
class ContainerInterface:
    """ Describes the interface of a container that exposes methods to read its entries. """
    def get(self, id_: typing.Union[str, type]) -> object:
        """
        Finds an entry of the container by its identifier and returns it.

        :param id_: Identifier of the entry to look for.

        :raise NotFoundExceptionInterface:  No entry was found for **this** identifier.
        :raise ContainerExceptionInterface: Error while retrieving the entry.

        :return: mixed Entry.
        """
        raise NotImplementedError

    def has(self, id_: typing.Union[str, type]) -> bool:
        """
        Returns true if the container can return an entry for the given identifier.
        Returns false otherwise.

        `has(id_)` returning true does not mean that `get(id_)` will not raise an exception.
        It does however mean that `get(id_)` will not raise a `NotFoundExceptionInterface`.

        :param id_: Identifier of the entry to look for.

        :return: bool
        """
        raise NotImplementedError


class ContainerExceptionInterface:
    """ Base interface representing a generic exception in a container. """


class NotFoundExceptionInterface(ContainerExceptionInterface):
    """ No entry was found in the container. """
