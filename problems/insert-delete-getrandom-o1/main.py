import random


class RandomizedSet:
    def __init__(self):
        self.val_map = {}
        self.val_list = []

    def insert(self, val: int) -> bool:
        if val in self.val_map:
            return False
        self.val_map[val] = len(self.val_list)
        self.val_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        index = self.val_map.get(val)
        if index != None:
            self.val_list[index] = self.val_list[-1]
            self.val_map[self.val_list[index]] = index
            self.val_list = self.val_list[:-1]
            del self.val_map[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.val_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

if __name__ == "__main__":
    a = RandomizedSet()
    assert a.insert(1) == True
    assert a.remove(2) == False
    assert a.insert(2) == True
    assert a.getRandom() == 2 or 1
    assert a.remove(1) == True
    assert a.insert(2) == False
    assert a.getRandom() == 2

    print("Passed")
