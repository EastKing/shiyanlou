#!/usr/bin/env python3

class Screen(object):
    @property
    def width(self):
        return self._width

    def a(self):
        return self.__doc__

if __name__ == '__main__':
    s=Screen()
    s.a()




