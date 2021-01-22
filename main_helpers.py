import sys
import pathlib

def resource_path(relative_path):
    """ Get absolute path to resource,"""
    base_path = pathlib.Path(__file__).parent.absolute()
    return pathlib.Path(base_path, relative_path)