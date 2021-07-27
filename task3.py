import traceback


class ListElemIsNotInt(Exception):
    def __init__(self, err_text):
        self.err_text = err_text


lst = []
while True:
    lst_item = input()
    if lst_item == 'q':
        break
    try:
        if not lst_item.isdigit():
            raise ListElemIsNotInt('Элемент списка не является числом')
        lst.append(int(lst_item))
    except ListElemIsNotInt:
        print(traceback.format_exc())

print(lst)
