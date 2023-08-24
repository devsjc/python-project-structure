"""packagename.

Usage:
  packagename command
  packagename (-h | --help)
  packagename --version

Options:
    -h --help     Show this screen.
    --version     Show version.
"""

import contextlib
import datetime as dt
import importlib.metadata

import structlog
from docopt import docopt

__version__ = "local"

with contextlib.suppress(importlib.metadata.PackageNotFoundError):
    __version__ = importlib.metadata.version("package-name")

log = structlog.getLogger()


def run() -> None:
    """Run the CLI."""
    # Parse command line arguments from docstring
    arguments = docopt(__doc__, version=__version__)

    if arguments['command']:
        log.info(
            event="running command",
            arguments=arguments
        )


def main() -> None:
    """Entry point for the application CLI."""
    programStart = dt.datetime.now(tz=dt.timezone.utc)
    try:
        run()
    except Exception as e:
        log.error(
            event="error running package",
            error=str(e),
        )
    finally:
        programEnd = dt.datetime.now(tz=dt.timezone.utc)
        log.info(
            event="program finished",
            programStart=programStart.isoformat(),
            programEnd=programEnd.isoformat(),
            programDuration=str(programEnd - programStart),
        )
