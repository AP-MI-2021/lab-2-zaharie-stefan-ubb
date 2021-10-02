from math import factorial


def get_base_16_from_2(num_in_base_2):
    """
    Primeste un numar in baza 2 si returneaza acelasi numar in baza 16

    Args:
    num_in_base_2 -> str

    Returns: str
    """

    # Verifica daca numarul introdus este corect
    for c in num_in_base_2:
        if (c != "0") and (c != "1"):
            return "Eroare! Numarul introdus este incorect"

    # Caz particular
    if num_in_base_2 == "0":
        return "0"

    num_in_base_10 = int(num_in_base_2, 2)
    remainder_stack = []
    while num_in_base_10 > 0:
        remainder_stack.append(num_in_base_10 % 16)
        num_in_base_10 //= 16

    digits = "0123456789ABCDEF"
    num_in_base_16 = []
    while remainder_stack:
        num_in_base_16.append(digits[remainder_stack.pop()])
    return "".join(num_in_base_16)


def test_get_base_16_from_2():
    pass


def get_n_choose_k(n, k):
    """
    Calculeaza combinari de n luate cate k

    Args:
    n -> int
    k -> int

    Returns: int
    """

    return factorial(n) / (factorial(k) * factorial(n - k))


def test_get_n_choose_k():
    pass


def main():
    usage = """
Meniu:
1 - Transforma un numar din baza 2 in baza 16
2 - Calculeaza combinari de n luate cate k

Teste:
t1 - Ruleaza testele pentru functia get_base_16_from_2
t2 - Ruleaza testele pentru functia get_n_choose_k

m - Afiseaza acest meniu
x - Iesire
"""
    print(usage)

    shouldRun = True
    while shouldRun:
        option = input("Introduceti o optiune: ")

        if option == "m":
            print(usage)
        elif option == "x":
            shouldRun = False
            print("La revedere!")

        elif option == "1":
            num_in_base_2 = input("Intorduceti un numar in baza 2: ")
            print("Raspuns: ", get_base_16_from_2(num_in_base_2))
        elif option == "2":
            n = int(input("Introduceti n: "))
            k = int(input("Introduceti k: "))
            print("Raspuns: ", get_n_choose_k(n, k))

        elif option == "t1":
            print("Se ruleaza testele...")
            test_get_base_16_from_2()
            print("Toate testele au fost rulate cu succes")
        elif option == "t2":
            print("Se ruleaza testele...")
            test_get_n_choose_k()
            print("Toate testele au fost rulate cu succes")

        else:
            print("Optiune inexistenta! Introduceti m pentru meniu")


if __name__ == "__main__":
    main()
