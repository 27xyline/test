#  Тут будет реализация Redis

class BaseCacheBackend:
    def __init__(self, backend):
        self.backend = backend
        self.cache = {}
