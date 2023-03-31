class BaseCallable:
    def __new__(cls, *args, **kwargs) -> None:
        return cls.eval(*args, **kwargs)

    @staticmethod
    def eval(*args, **kwargs):
        pass