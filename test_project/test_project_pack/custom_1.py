class ItemNotAvailable(Exception):
    def __init__(self, message):
        super().__init__()
        return print(message)

