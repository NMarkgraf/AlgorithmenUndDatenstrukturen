'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Einfacher UPN Taschenrechner mit Stack

'''

from lists import Stack
import readchar


class UPNcalc:

    stack = Stack()  # Unser eigener Stack aus lists!

    def __init__(self):
        self.base = 10

    def main(self):
        while (True):
            x = 0
            y = 0
            n = 0
            m = 0
            c = readchar.readchar()
            flag = True

            while (c in ["0", "1", "2", "3", "4",
                         "5", "6", "7", "8", "9", "."]):
                print(c, end='', flush=True)
                n += 1
                if (c == "."):
                    flag = False
                else:
                    if flag:
                        x = x * self.base + int(c)
                    else:
                        m += 1
                        y = y * self.base + int(c)
                c = readchar.readchar()

            if (n > 0):
                print(" ", end="", flush=True)
                if (m > 0):
                    x += y / (10**m)
                self.stack.push(x)

            if (c == "+"):
                print("+ ", end='', flush=True)
                self.stack.push(self.stack.pop() + self.stack.pop())
            else:
                if (c == "-"):
                    print("- ", end='', flush=True)
                    t = self.stack.pop()
                    self.stack.push(self.stack.pop() - t)
                else:
                    if (c == "*"):
                        print("* ", end='', flush=True)
                        self.stack.push(self.stack.pop() * self.stack.pop())
                    else:
                        if (c == "/"):
                            print("/ ", end='', flush=True)
                            t = self.stack.pop()
                            if t:
                                self.stack.push(self.stack.pop() / t)
                        else:
                            if (c == "~"):
                                print("~ ", end='', flush=True)
                                self.stack.push(-1*self.stack.pop())
            if (c in ['\x0d', '\x0a']):
                break
        print("= " + str(self.stack.pop()))


def main():
    calculator = UPNcalc()
    calculator.main()


if __name__ == "__main__":
    main()
