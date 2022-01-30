# class, object practice
class phone:
    def __init__(self, os, number, is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

phone1 = phone('ios', 123, True)
print(phone1.os)
print(phone1.number)
print(phone1.is_waterproof)