class SequenceList(object):
    """
    类名：SequenceList
    功能：定义顺序表数据结构
    释义：定义一个顺序表及其相关操作
    """

    def __init__(self):
        """
        功能：初始化顺序表函数
        """
        self.SeqList = []

    def CreateSequenceList(self):
        """
        功能：创建顺序表函数
        输入：数字元素
        """
        element = input("输入整型数据元素，按#结束:")
        while element != '#':
            self.SeqList.append(int(element)) # 尾插法
            element = input("输入整型数据元素，按#结束:")
        print("创建后，顺序表为：", self.SeqList)

    def FindElement(self):
        """
        功能：查找元素第一次出现的位置
        输入：数字元素
        """
        key = int(input("输入要查找位置的元素值："))
        if key in self.SeqList:
            posi = self.SeqList.index(key)
            print("查找成功！", self.SeqList[posi], "第一次出现在当前顺序表的第", (posi + 1), "位")
        else:
            print("查找失败！当前顺序表中不存在值为", key, "的元素")

    def InsertElement(self):
        """
        功能：定位插入元素(插入到指定位置前)
        输入：插入位置、数字元素
        """
        posi = int(input("待插入位置："))
        element = int(input("待插入的元素："))
        self.SeqList.insert(posi - 1, element)
        print("插入元素后，顺序表为：", self.SeqList)

    def DeleteElement(self):
        """
        功能：定位删除元素
        输入：待删除位置
        """
        posi = int(input("待删除位置："))
        print("正在删除", self.SeqList[posi - 1], "......")
        self.SeqList.remove(self.SeqList[posi - 1])
        print("删除元素后，顺序表为：", self.SeqList)

    def TraverseElement(self):
        sqlen = len(self.SeqList)
        print("即将遍历顺序表......")
        for i in range(0, sqlen):
            print("第", i + 1, "个元素的值为", self.SeqList[i])

class 