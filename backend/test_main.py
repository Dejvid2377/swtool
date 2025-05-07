from models.rune import Rune

attributes = {
    'id': 1,
    'name': 'Swift',
    'power': 100,
    'type': 'Attack'
}


def create_rune():
    rune = Rune(attributes)
    rune.show_attributes()


if __name__ == "__main__":
    create_rune()
