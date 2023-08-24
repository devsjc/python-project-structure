"""Config struct for application running."""

import os
from typing import get_type_hints

import structlog

log = structlog.getLogger()


class _EnvParseMixin:
    """Mixin to parse environment variables into class fields."""

    def __init__(self) -> None:
        for field, _ in get_type_hints(self).items():
            # Skip item if not upper case
            if not field.isupper():
                continue

            # Log Error if required field not supplied
            default_value = getattr(self, field, None)
            if default_value is None and os.environ.get(field) is None:
                log.warn(
                    event="environment variable not set",
                    variable=field,
                )
                default_value = ""
            # Cast env var value to string
            value = str(os.environ.get(field, default_value))
            self.__setattr__(field, value)


class AppConfig(_EnvParseMixin):
    """Config for app."""

    API_KEY: str
    API_SECRET: str
