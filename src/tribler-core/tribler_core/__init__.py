"""
Tribler is a privacy enhanced BitTorrent client with P2P content discovery.
"""
import os
import sys
from pathlib import Path

from tribler_common.logger import setup_logging

from tribler_core.config.tribler_config import TriblerConfig

dir_path = Path(__file__).parent.parent.parent

# Make sure AnyDex can be imported
sys.path.append(os.path.join(dir_path, "anydex"))

# Make sure IPv8 can be imported
sys.path.insert(0, os.path.join(dir_path, "pyipv8"))


def load_logger_config():
    """
    Loads tribler-core module logger configuration. Note that this function should be called explicitly to
    enable Core logs dump to a file in the log directory (default: inside state directory).
    """
    logger_config = os.path.join("tribler-core", __name__, "logger.yaml")
    setup_logging(config_path=logger_config, module='tribler-core', log_dir=TriblerConfig().get_log_dir())
