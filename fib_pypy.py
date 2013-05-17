import time
from array import array


class bigint:
    def __init__(self, n):
        if n == 0:
            self._digits = array('b', [0] * 8)
            self._length = 0
        else:
            s = str(n)
            self._digits = array('b', reversed([int(a) for a in s]))
            self._length = len(s)

    def __str__(self):
        # not optimal: only for tests
        return ''.join(str(a) for a in reversed(self._digits[:self._length])) or '0'

    def add(self, o):
        length = max(self._length, o._length)
        if len(self._digits) <= length:
            self._digits.extend([0] * len(self._digits))
        acc = 0
        i = 0
        while i < length:
            d1 = self._digits[i] if i < self._length else 0
            d2 = o._digits[i] if i < o._length else 0
            r = d1 + d2 + acc
            if r > 9:
                acc = 1
                r = r - 10
            else:
                acc = 0
            self._digits[i] = r
            i += 1
        if acc:
            self._digits[i] = 1
            self._length = i + 1
        else:
            self._length = i

    def has(self, d):
        length = d._length
        i = 0
        j = 0
        while i < self._length:
            if self._digits[i] == d._digits[j]:
                i += 1
                j += 1
            else:
                i = i - j + 1
                j = 0
            if j == length:
                return True
        return False

    
def fib():
    n1 = bigint(0)
    yield n1
    n2 = bigint(1)
    yield n2
    while True:
        n1, n2 = n2, n1
        n2.add(n1)
        yield n2


def main():
    # a = bigint(57)
    # print(a._digits)
    # print(a)
    # a.add(bigint(6))
    # print(a)
    # a.add(bigint(37))
    # print(a)
    # a.add(bigint(37))
    # print(a)
    # print(a.has(bigint(37)))
    # print(a.has(bigint(47)))
    # print(a.has(bigint(981)))
    # # return

    # g = fib()
    # for i in range(10):
    #     print(g.next())

    # warming jit
    for i, n in zip(range(1, 20000), fib()):
        pass
    print(i, len(str(n)))

    def f():
        d = bigint(31415926)
        g = fib()
        for i, n in enumerate(g, 1):
            if n.has(d):
                yield i

    g = f()
    ts = time.time()
    for i in range(5):
        print(g.next())
    te = time.time()
    print('took: {0:.2f} sec'.format(te-ts))


if __name__ == '__main__':
    main()
