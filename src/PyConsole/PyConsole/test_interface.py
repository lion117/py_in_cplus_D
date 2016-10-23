def add(t_a, t_b):
    return t_a + t_b


def getCurrentDir():
    import os
    return os.getcwd()


def getWorkingDir():
    import os
    return os.path.dirname(os.getcwd()) + "/Bin"


class TestClass():
    _name = "default"

    def __init__(self, t_name):
        self._name = t_name

    def add(self, t_a, t_b):
        return t_a + t_b

    def getCurrentTime(self):
        import time
        return str(time.ctime())

    def whoAmI(self):
        print self._name


def getObjClass():
    return TestClass("t_name")


class ObjTest():
    def __init__(self):
        print "init object"


def getIntance():
    return ObjTest()
