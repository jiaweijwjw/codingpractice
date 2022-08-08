class Opposite():
    def __init__(self) -> None:
        pass

    def get_opposite1(self, num): # direct return opposite
        if num == 0:
            return 1
        else:
            return 0

    def get_opposite2(self, num): # checking Falsy values, logical operator
        return 1 if not num else 0

    def get_opposite3(self, num): # using XOR
        return num ^ 1

    def get_opposite4(self, num): # using remainder
        return 1 - num

    def get_opposite5(self, num): # using modulo
        return (num+1)%2

    def get_opposite6(self, num):
        return abs(num - 1)

    def get_opposite7(self, num):
        num_str = str(num)
        # not using if-else
        num_str = num_str.replace('1', '#')
        num_str = num_str.replace('0', '1')
        num_str = num_str.replace('#', '0')
        return int(num_str)

    def get_opposite8(self, num):
        return 1 // (num+1)

if __name__ == "__main__":
    opposite = Opposite()
    print(opposite.get_opposite1(0))
    print(opposite.get_opposite2(0))
    print(opposite.get_opposite3(0))
    print(opposite.get_opposite4(0))
    print(opposite.get_opposite5(0))
    print(opposite.get_opposite6(0))
    print(opposite.get_opposite7(0))
    print(opposite.get_opposite1(1))
    print(opposite.get_opposite2(1))
    print(opposite.get_opposite3(1))
    print(opposite.get_opposite4(1))
    print(opposite.get_opposite5(1))
    print(opposite.get_opposite6(1))
    print(opposite.get_opposite7(1))