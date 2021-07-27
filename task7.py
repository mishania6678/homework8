class ComplexNumber:
    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __add__(self, other):
        return self.complex_num + other.complex_num

    def __mul__(self, other):
        return self.complex_num * other.complex_num


a = ComplexNumber(2 + 3j)
b = ComplexNumber(3 + 2j)
print(f'{a + b}\n{a * b}')
