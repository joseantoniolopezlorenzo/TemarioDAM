# -*- coding: utf-8 -*-
try:
    236 / 0
except NameError:
    print "Error, la variable no existe"
except (ValueError, OverflowError):
    print "Error de valor u overflow"
except Exception as ex:
    print "Error:", ex
else:
    print "Si no hay excepción"
finally:
    print "Continuando..."


class miExcepcion(Exception):
    def __init__(self, val):
        self.valor = val

    def __str__(self):
        return "Error:" + str(self.valor)


try:
    raise miExcepcion("Prueba")
except miExcepcion, e:
    print e
