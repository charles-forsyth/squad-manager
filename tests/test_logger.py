import logging
from unittest.mock import patch

from squad_manager.utils.logger import setup_logging


def test_setup_logging_configures_root_logger() -> None:
    """Test that setup_logging configures the root logger appropriately."""
    with patch("squad_manager.utils.logger.logging.basicConfig") as mock_basic_config:
        setup_logging(verbose=False)

        mock_basic_config.assert_called_once()
        kwargs = mock_basic_config.call_args.kwargs

        assert kwargs.get("level") == logging.INFO, "Default log level should be INFO"
        assert "handlers" in kwargs, "Handlers should be configured"
        has_rich = any("RichHandler" in str(type(h)) for h in kwargs["handlers"])
        assert has_rich, "RichHandler should be used"


def test_setup_logging_verbose_mode() -> None:
    """Test that setup_logging sets log level to DEBUG when verbose=True."""
    with patch("squad_manager.utils.logger.logging.basicConfig") as mock_basic_config:
        setup_logging(verbose=True)

        mock_basic_config.assert_called_once()
        kwargs = mock_basic_config.call_args.kwargs

        assert kwargs.get("level") == logging.DEBUG, "Verbose log level should be DEBUG"
