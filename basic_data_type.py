

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