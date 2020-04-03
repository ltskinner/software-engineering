
class Image(object):
    """The RealSubject"""
    def __init__(self, filename):
        self._filename = filename

    def load_image_from_disk(self):
        print("loading:", self._filename)

    def display_image(self):
        print("display:", self._filename)


class Proxy(object):
    """The Proxy"""
    def __init__(self, subject):
        self._subject = subject
        self._proxy_state = None


class ProxyImage(Proxy):
    """The Subject"""
    # Notice we are hiding load_image_from_disk
    def display_image(self):
        if self._proxy_state is None:
            self._subject.load_image_from_disk()
            self._proxy_state = 1

        self._subject.display_image()

if __name__ == "__main__":
    image_1 = Image("image_1")
    image_2 = Image("image_2")

    proxy_image_1 = ProxyImage(image_1)
    proxy_image_2 = ProxyImage(image_2)

    for i in range(3):
        print("----------------------------")
        proxy_image_1.display_image()
        proxy_image_2.display_image()
