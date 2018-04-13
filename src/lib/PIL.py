#!/usr/bin/env python3
# vim: set fileencoding=utf-8 :

import image as _image

__appname__     = "PIL"
__author__      = "Marco Sirabella"
__copyright__   = ""
__credits__     = ["Marco Sirabella"]  # Authors and bug reporters
__license__     = "GPL"
__version__     = "1.0"
__maintainers__ = "Marco Sirabella"
__email__       = "marco@sirabella.org"
__status__      = "Prototype"  # "Prototype", "Development" or "Production"
__module__      = "PIL"


class PixelAccess(dict):
    def __new__(cls, parent):
        return dict.__new__(cls)

    def __init__(self, parent):
        for x in range(parent.size[0]):
            for y in range(parent.size[1]):
                dict.__setitem__(self, (x, y), parent._image.getPixel(x, y))

        self._parent = parent

    def __setitem__(self, key, value):
        p = self._parent._image.getPixel(*key)
        p.setRed(value[0])
        p.setGreen(value[1])
        p.setBlue(value[2])
        self._parent._image.updatePixel(p)


class Image():
    def __init__(self, _Image):
        self._image = _Image
        self.size = (self._image.getWidth(), self._image.getHeight())

        self.pixels = PixelAccess(self)

    def open(filename):
        cls = Image
        self = cls(_Image=_image.Image(filename))
        return self

    def load(self):
        return self.pixels

    def show(self):
        win = _image.ImageWin(*self.size)
        self._image.draw(win)
