'''Prototype Pattern with Python Code
'''

import copy


class Prototype(object):
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    def clone(self, name, **attr):
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr)
        return obj


class Client(object):
    def main(self):
        class A:
            pass

        a = A()
        prototype = Prototype()

        prototype.register_object('a', a)
        b = prototype.clone('a', a=1, b=2, c=3)

        prototype.register_object('b', b)
        c = prototype.clone('b', c=5, d=6)

        print(b.a, b.b, b.c)
        print(c.a, c.b, c.c, c.d)


if __name__ == '__main__':
    Client().main()
