from configparser import ConfigParser


class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Config(metaclass=Singleton):
  def __init__(self, path:str='assets/config.ini'):
    self.path = path
    self.config = ConfigParser()
    self.config.read(self.path)
