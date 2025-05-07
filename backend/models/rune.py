#
# This is a representation of the game rune item.
# Since single rune is presented by multiple
# parameters, initialize list will be passed
# in the class constructor.
#

class Rune:
    def __init__(self, attributes: dict):

        for key, value in attributes.items():
            setattr(self, key, value)

    def show_attributes(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")
