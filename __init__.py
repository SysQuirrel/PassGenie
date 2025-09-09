"""
PasswordGenie - A secure password and passphrase generator
"""

__version__ = "1.0.0"
__author__ = "SysQuirrel"
__description__ = "A secure password and passphrase generator with web interface"

from .code.password_generator import generate_password, random_passphrase_generator

__all__ = [
    'generate_password',
    'random_passphrase_generator'
]
