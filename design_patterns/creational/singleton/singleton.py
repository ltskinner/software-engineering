
class OJFactory(object):
    _instance = None

    def __init__(self):
        if OJFactory._instance is not None:
            print("umwhat")
        else:
            OJFactory._instance = self

    @staticmethod
    def instance():
        if OJFactory._instance is None:
            OJFactory()
        return OJFactory._instance

    def get_juice(self):
        return "fresh squeezed pulp"

    def unload_trucks(self):
        return "does the weatherman or the investor know the weather better?"


if __name__ == "__main__":
    oj = OJFactory()
    print(oj.instance())

    oj2 = OJFactory()
    print(oj2.instance())
