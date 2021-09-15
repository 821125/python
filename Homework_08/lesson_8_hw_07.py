class MyComplex:
    def __init__(self, real, img=0):
        self.__complex = complex(real, img)

    def __add__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex + other
        return MyComplex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            other = other.__complex

        complex_ = self.__complex * other
        return MyComplex(complex_.real, int(complex_.imag))

    def __repr__(self):
        return self.__complex.__repr__()


n1 = 2j
n2 = 4j
cn1 = MyComplex(n1)
cn2 = MyComplex(n2)
print(cn1, cn2)
print(cn1 + cn2)
print(cn1 * cn2)
