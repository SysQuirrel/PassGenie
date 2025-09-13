"""
PasswordGenie - A secure password and passphrase generator
"""

__version__ = "1.0.0"
__author__ = "SysQuirrel"
__description__ = "A secure password and passphrase generator with web interface"

# Import main functions to make them available at package level
from .generator import generate_password, random_passphrase_generator

# Define what gets imported with "from src import *"
__all__ = [
    'generate_password',
    'random_passphrase_generator'
]
