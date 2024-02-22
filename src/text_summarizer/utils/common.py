import os
from box.exceptions import BoxValueError
import yaml
from text_summarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Read a YAML file and return a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.
    Raises:
        ValueError: If the YAML file is empty
    Returns:
        config_box (ConfigBox): The ConfigBox type
    """
    try:
        with open(path_to_yaml, "r", encoding="utf-8") as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError(f"yaml file {path_to_yaml} is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directory(path_to_directories: list, verbose=True):
    """Create a list of directories.

    Args:
        path_to_directories (list): List of directories to create.
        verbose (bool): If True, print a message.
    """
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f"directory {directory} created successfully")

@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"