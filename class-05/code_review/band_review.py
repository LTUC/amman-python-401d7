class Band:
    instances = []

    def __init__(self):
        Band.instances.append(self)

    @classmethod
    def to_list(cls):
        return cls.instances


