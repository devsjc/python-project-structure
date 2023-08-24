"""Ports and domain models for the package_name package."""

import abc
import dataclasses

# ------- Global constants ------- #
# * Constants that are used throughout the package

TIME_FMT = "%Y%m%dT%H%M"

# ------- Domain models ------- #
# Representations of data within the application domain


@dataclasses.dataclass
class PersonDataModel:
    """Struct representing format of data internal to the service."""
    forename: str
    surname: str
    age: int


# ------- Interfaces ------- #
# * Represent ports in the hexagonal architecture pattern

class FetcherInterface(abc.ABC):
    """Generic interface for fetching data."""

    @abc.abstractmethod
    def fetch(self) -> PersonDataModel:
        """Fetch a person and map it to the domain model.

        :return: The internal representation of the data.
        """
        pass


class StorerInterface(abc.ABC):
    """Generic interface for storing data."""

    @abc.abstractmethod
    def save(self, *, p: PersonDataModel) -> int:
        """Save the data at the given path to the store.

        :param p: The path to the data.
        :return: The number of bytes saved.
        """
        pass
