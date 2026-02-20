import logging

from rich.logging import RichHandler


def setup_logging(verbose: bool = False) -> None:
    """
    Configures the root logger with RichHandler.

    Args:
        verbose: If True, sets the log level to DEBUG. Otherwise, INFO.
    """
    level = logging.DEBUG if verbose else logging.INFO

    # Configure the root logger
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )
