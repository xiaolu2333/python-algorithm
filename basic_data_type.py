

class change_two_vars:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print("init:    a={}  b={}".format(self.a, self.b))

    def feature(self):
        """解法一"""
        self.a, self.b = self.b, self.a
        print("feature: a={}  b={}".format(self.a, self.b))

    def exc_or(self):
        """解法二"""
        self.a = self.a ^ self.b
        self.b = self.a ^ self.b
        self.a = self.a ^ self.b
        print("exc_or:  a={}  b={}".format(self.a, self.b))


class frequently_used_bin_opts:
    def __init__(self, x):
        self.x = x
        print("init:    x={}  bin(x)={}".format(x, bin(self.x)))

    def reset_the_lowest_bit_1(self):
        print("old_bin(x)={}".format(bin(self.x)))
        self.x = self.x & (self.x - 1)
        print("reset_the_lowest_bit_1:    new_bin(x)={}".format(bin(self.x)))
        return self.x

    def get_the_lowest_bit_1(self):
        print("old_bin(x)={}".format(bin(self.x)))
        self.x = self.x & (~(self.x - 1))
        print("get_the_lowest_bit_1:    new_bin(x)={}".format(bin(self.x)))
        return self.x

    def swap_specified_bits(self):
        p = int(input("input a number:"))
        print("the binary is {}".format(bin(p)))
        i = int(input("enter a position:"))
        j = int(input("enter other position:"))
        #如果第i位和第j位上的数值相同那就没必要进行操作S
        if ((p>>i) & 1) != ((p>>j) & 1):
            p ^= ((1<<i) | (1<<j))
        print("binary format of x after swap bit of {0} and {1} is {2}".format(i, j, bin(p)))



