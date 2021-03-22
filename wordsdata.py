class Words:
    """A sample Employee class"""

    def __init__(self, palabra , significado):
        self.palabra = palabra
        self.significado = significado

    @property

    def __repr__(self):
        return "Words('{}', '{}')".format(self.palabra, self.significado)
