"""Ports and domain models for the package_name package."""

import abc
import pathlib

# ------- Global constants ------- #

# ------- Domain models ------- #


class PersonData(abc.ABC):
    """Information about a person."""

    @abc.abstractmethod
    def name(self) -> str:
        """Return the name of the person."""
        pass

    @abc.abstractmethod
    def age(self) -> int:
        """Return the age of the person."""
        pass

# ------- Interfaces ------- #
# * Represent ports in the hexagonal architecture pattern


class StorerInterface(abc.ABC):
    """Generic interface for storing data."""

    @abc.abstractmethod
    def save(self, *, p: pathlib.Path) -> int:
        """Save the data at the given path to the store.

        :param p: The path to the data.
        :return: The number of bytes saved.
        """
        pass
