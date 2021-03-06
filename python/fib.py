'''

Algorithmen und Datenstrukturen in Python
=========================================

Implementierungen von Norman Markgraf aus dem Jahr 2018

Rekursive und iterative Berechnung der n-ten Fibonacci-Zahl.


'''


def fib_recursive(n: int) -> int:
    """Rekursive Funktion zur Berechnung der *n*-ten Fibonacci-Zahl.

    :param: n
    """
    if n < 2:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """Iterative Funktion zur Berechnung der *n*-ten Fibonacci-Zahl.

    :param: n
    """
    f = 1
    fv = 1
    for i in range(1, n):
        t = f
        f = fv + t
        fv = t
    return f


def main(fib, n):
    print(fib(n))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--recursive", help="Rekursiver Fibonacci",
                        action="store_true")
    parser.add_argument("-i", "--iterative", help="Iterativer Fibonacci",
                        action="store_true")
    parser.add_argument("n", help="n", type=int)
    args = parser.parse_args()
    main(fib_recursive if args.recursive else fib_iterative, args.n)
