import traceback


class ZeroError(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


div1, div2 = int(input()), int(input())
try:
    if div2 == 0:
        raise ZeroError('Нельзя делить на ноль')
    print(div1 / div2)
except ZeroError:
    print(traceback.format_exc())

