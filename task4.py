class Warehouse:
    pass


class OfficeEquipment:
    def __init__(self, availability: bool, amount: int, retail_price: int):
        self.availability = availability
        self.amount = amount
        self.retail_price = retail_price


class PC(OfficeEquipment):
    def __init__(self, availability: bool, amount: int, retail_price: int,
                 os: str, cpu: str, ram: int, system_type: str):
        OfficeEquipment.__init__(self, availability, amount, retail_price)
        self.cpu = cpu
        self.ram = ram
        self.system_type = system_type
        self.os = os


class Tablet(OfficeEquipment):
    def __init__(self, availability: bool, amount: int, retail_price: int,
                 os: str, diagonal: int, memory: int, bluetooth: bool):
        OfficeEquipment.__init__(self, availability, amount, retail_price)
        self.os = os
        self.diagonal = diagonal
        self.memory = memory
        self.bluetooth = bluetooth


class Printer(OfficeEquipment):
    def __init__(self, availability: bool, amount: int, retail_price: int,
                 printing_technology: str, device_type: str, black_and_white: bool):
        OfficeEquipment.__init__(self, availability, amount, retail_price)
        self.printing_technology = printing_technology
        self.device_type = device_type
        self.black_and_white = black_and_white
