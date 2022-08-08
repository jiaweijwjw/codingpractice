
class BitsAndBinary():
    def __init__(self) -> None:
        pass

    def convert_decimal_to_base(self, dec, base):
        if dec == 0:
            return [0]
        digits = []
        while dec:
            digits.append(int(dec%base))
            dec //= base
        return digits[::-1]

    def convert_base_to_decimal(self, num, base):
        return int(str(num), base)

    def convert_base_to_base(self, num, base, new_base):
        dec = self.convert_base_to_decimal(str(num), base)
        return self.convert_decimal_to_base(dec, new_base)


if __name__ == "__main__":
    obj = BitsAndBinary()
    print(obj.convert_decimal_to_base(8, 2))
    print(obj.convert_base_to_decimal(1000, 2))
    print(obj.convert_base_to_base(7, 10, 4))