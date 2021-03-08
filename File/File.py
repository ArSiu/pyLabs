from enum import Enum


class Type(Enum):
    FTP = 0
    FTPS = 1
    SFTP = 2


class File:
    def __init__(self, type: Type, name: str = 0):
        self.type = type
        self.name = name
