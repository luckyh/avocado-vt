


class StoragePool(object):


    def __init__(self):
        pass

    def detect(self):
        pass

    def allocate(self):
        pass

    def recycle(self):
        pass


class MetaVolume(object):

    pass


class Volume(object):

    def __init__(self):
        self.driver = None #QemuImg

    @property
    def existed(self):
        pass

    def create(self):
        pass

    def delete(self):
        pass

    def erase(self):
        pass

    def backup(self):
        pass

    def restore(self):
        pass
