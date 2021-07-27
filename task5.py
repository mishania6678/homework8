class Warehouse:
    products = {}

    @classmethod
    def add_product(cls, product_data: dict) -> None:
        Warehouse.products[cls.__name__] = product_data

    @classmethod
    def get_product_data(cls, formatted=False) -> dict:
        if not formatted:
            return Warehouse.products.get(cls.__name__)
        else:
            return cls._format_data(Warehouse.products.get(cls.__name__))

    @staticmethod
    def _format_data(data: dict) -> str:
        string = ''
        for key, val in data.items():
            if key == '__slots__':
                continue
            string += f'{key}: {val}\n'
        return string


class OfficeEquipment:
    def __init__(self, amount: int, retail_price: int):
        self.amount = amount
        self.retail_price = retail_price


class PC(OfficeEquipment, Warehouse):
    def __init__(self, availability: bool, **kwargs):
        self.availability = availability
        if availability:
            OfficeEquipment.__init__(self, kwargs['amount'], kwargs['retail_price'])
            self.os = kwargs['os']
            self.cpu = kwargs['cpu']
            self.ram = kwargs['ram']
            self.system_type = kwargs['system_type']


class Tablet(OfficeEquipment, Warehouse):
    def __init__(self, availability: bool, **kwargs):
        self.availability = availability
        if availability:
            OfficeEquipment.__init__(self, kwargs['amount'], kwargs['retail_price'])
            self.os = kwargs['os']
            self.diagonal = kwargs['diagonal']
            self.memory = kwargs['memory']
            self.bluetooth = kwargs['bluetooth']


class Printer(OfficeEquipment, Warehouse):
    def __init__(self, availability: bool, **kwargs):
        self.availability = availability
        if availability:
            OfficeEquipment.__init__(self, kwargs['amount'], kwargs['retail_price'])
            self.printing_technology = kwargs['printing_technology']
            self.device_type = kwargs['device_type']
            self.black_and_white = kwargs['black_and_white']


def f(obj: Warehouse):
    obj.add_product(obj.__dict__)
    print(obj.get_product_data())
    print()
    print(obj.get_product_data(formatted=True))
    print('-' * 160, '\n')


f(PC(True, amount=50, retail_price=56800, os='windows', cpu='ADM Ryzen', ram=16, system_type='x64'))
f(Tablet(True, amount=15, retail_price=29000, os='ios', diagonal=34, memory=128, bluetooth=True))
f(Printer(False))
