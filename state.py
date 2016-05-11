
class State:

    __left = 0
    __right = 1

    def __init__(self, leftState = False, rightState = False):
        """
        Manages the state of tree traversal: left, or right path
        :param leftState:
        :param rightState:
        """
        self.STATE = [leftState, rightState]

    @property
    def LEFT(self, item):
        if self.STATE.__contains__(item):
            return self.STATE[item]
        else:
            return None

    @LEFT.getter
    def LEFT(self):
        return self.STATE[self.__left]

    @LEFT.setter
    def LEFT(self, value):
        assert value.isinstance(bool)
        self.STATE[self.__left] = value

    @property
    def RIGHT(self, item):
        if self.STATE.__contains__(item):
            return self.STATE[item]
        else:
            return None

    @RIGHT.getter
    def RIGHT(self):
        return self.STATE[self.__right]

    @RIGHT.setter
    def RIGHT(self, value):
        assert value.isinstance(bool)
        self.STATE[self.__right] = value

if __name__ == '__main__':
    s = State(False, False)
    print s.LEFT
    print s.RIGHT
    s.LEFT = True
    s.RIGHT = True
    print s.LEFT
    print s.RIGHT