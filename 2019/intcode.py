# SPDX-License-Identifier: MIT
# Copyright (c) 2020 Akumatic

class InvalidOpcode(Exception):
    pass

class IndexError(Exception):
    pass

class Data:
    def __init__(self, vals: list):
        self._data = {i:vals[i] for i in range(len(vals))}

    def __getitem__(self, idx):
        if idx < 0:
            raise IndexError("Negative Index")
        if idx in self._data:
            return self._data[idx]
        self._data[idx] = 0
        return 0

    def __setitem__(self, idx, val):
        if idx < 0:
            raise IndexError("Negative Index")
        self._data[idx] = val

    def toList(self):
        return list(self._data.values())

    def maxIdx(self):
        return max(self._data.keys())

class Computer:
    def __init__(self,
            vals: list,
            base: int = 0,
            input: int = 0,
            wait_for_input: bool = False
        ):
        self._val_backup = vals.copy()
        self.reset(base=base, input=input, wait_for_input=wait_for_input)
        
    def reset(self, vals = None, base = 0, input = 0, wait_for_input = False):
        if vals is not None:
            self._val_backup = vals
        self.data: Data = Data(self._val_backup)
        self.base: int = base
        self.input: int = None if wait_for_input else input
        self.pointer: int = 0
        self.base: int = base
        self.input: int = input
        self.output: list = list()
        self.opcode: tuple = None
        self.stop = False
        self.wait = False
    
    # # # # # # # # # # #
    # opcode functions  #
    # # # # # # # # # # #

    # opcode 99
    def __terminate(self):
        self.stop = True

    # opcode 1
    def __add(self, a: int, b: int, c: int):
        self.data[c] = self.data[a] + self.data[b]
        self.pointer += 4

    # opcode 2
    def __multiply(self, a: int, b: int, c: int): # 2
        self.data[c] = self.data[a] * self.data[b]
        self.pointer += 4

    # opcode 3
    def __input(self, a: int): # 3
        self.data[a] = self.input
        self.pointer += 2

    # opcode 4
    def __output(self, a: int): # 4
        self.data[0] = self.data[a]
        self.output.append(self.data[0])
        self.pointer += 2

    # opcode 5
    def __jump_if_true(self, a: int, b: int): # 5
        if self.data[a]:
            self.pointer = self.data[b]
        else:
            self.pointer += 3

    # opcode 6
    def __jump_if_false(self, a: int, b: int): # 6
        if not self.data[a]:
            self.pointer = self.data[b]
        else:
            self.pointer += 3

    # opcode 7
    def __less_than(self, a: int, b: int, c: int): # 7
        self.data[c] = int(self.data[a] < self.data[b])
        self.pointer += 4

    # opcode 8
    def __equals(self, a: int, b: int, c: int): # 8
        self.data[c] = int(self.data[a] == self.data[b])
        self.pointer += 4

    # opcode 9
    def __adjust_base(self, a: int): # 9
        self.base += self.data[a]
        self.pointer += 2

    # # # # # # # # # # # # #
    # operational functions # 
    # # # # # # # # # # # # #

    def __setOpcode(self):
        self.opcode = (
            self.data[self.pointer] % 100,
            self.data[self.pointer] // 100 % 10,
            self.data[self.pointer] // 1000 % 10,
            self.data[self.pointer] // 10000 % 10
        )

    def __getParameter(self, n: int):
        params = list()
        for i in range(1, n + 1):
            params.append(
                self.data[self.pointer + i] if self.opcode[i] == 0 else \
                self.pointer + i if self.opcode[i] == 1 else \
                self.data[self.pointer + i] + self.base
            )
        return params

    def run(self):
        while not self.stop:
            self.__setOpcode()

            if self.opcode[0] == 99:
                self.__terminate()

            elif self.opcode[0] == 1: # add
                self.__add(*self.__getParameter(3))

            elif self.opcode[0] == 2: # multiply
                self.__multiply(*self.__getParameter(3))

            elif self.opcode[0] == 3: # input
                if self.input is not None:
                    if self.wait:
                        self.wait = False
                    self.__input(*self.__getParameter(1))
                    self.input = None
                else:
                    self.wait = True
                    return

            elif self.opcode[0] == 4: # output
                self.__output(*self.__getParameter(1))

            elif self.opcode[0] == 5: # jump if true
                self.__jump_if_true(*self.__getParameter(2))

            elif self.opcode[0] == 6: # jump if false
                self.__jump_if_false(*self.__getParameter(2))

            elif self.opcode[0] == 7: # less than
                self.__less_than(*self.__getParameter(3))

            elif self.opcode[0] == 8: # equals
                self.__equals(*self.__getParameter(3))

            elif self.opcode[0] == 9: # adjust base
                self.__adjust_base(*self.__getParameter(1))

            else:
                raise InvalidOpcode