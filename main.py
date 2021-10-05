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
    assert get_base_16_from_2("0") == "0"
    assert get_base_16_from_2("2") == "Eroare! Numarul introdus este incorect"
    assert get_base_16_from_2("1010") == "A"
    assert get_base_16_from_2("111") == "7"
    assert get_base_16_from_2("10000") == "10"
    assert get_base_16_from_2("1111") == "F"
    assert get_base_16_from_2("0101100001111101010001110101") == "587D475"


def get_n_choose_k(n, k):
    """
    Calculeaza combinari de n luate cate k

    Args:
    n -> int
    k -> int

    Returns: int
    """

    if n < 0 or k < 0:
        return -1

    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def test_get_n_choose_k():
    assert get_n_choose_k(5, 2) == 10
    assert get_n_choose_k(-5, 2) == -1
    assert get_n_choose_k(0, 0) == 1


def is_palindrome(n):
    length = len(n)
    ans = True
    for i in range(length // 2):
        if n[i] != n[length - i - 1]:
            ans = False

    return ans


def test_is_palindrome():
    assert is_palindrome("329847") == False
    assert is_palindrome("gg") == True
    assert is_palindrome("99") == True
    assert is_palindrome("2") == True
    assert is_palindrome("-2") == False
    assert is_palindrome("232") == True


def main():
    usage = """
Meniu:
1 - Transforma un numar din baza 2 in baza 16
2 - Calculeaza combinari de n luate cate k
3 - Determina daca un numar/string este palindrom

Teste:
t1 - Ruleaza testele pentru functia get_base_16_from_2
t2 - Ruleaza testele pentru functia get_n_choose_k
t3 - Ruleaza testele pentru functia is_palindrome

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
            ans = get_n_choose_k(n, k)
            if ans == -1:
                print("Eroare! Numarul introdus nu este pozitiv")
            else:
                print("Raspuns: ", ans)
        elif option == "3":
            n = input("Intorduceti un numar/string: ")
            ans = is_palindrome(n)
            if ans:
                print("Este palindrom!")
            else:
                print("Nu este palindrom!")

        elif option == "t1":
            print("Se ruleaza testele...")
            test_get_base_16_from_2()
            print("Toate testele au fost rulate cu succes")
        elif option == "t2":
            print("Se ruleaza testele...")
            test_get_n_choose_k()
            print("Toate testele au fost rulate cu succes")
        elif option == "t3":
            print("Se ruleaza testele...")
            test_is_palindrome()
            print("Toate testele au fost rulate cu succes")

        else:
            print("Optiune inexistenta! Introduceti m pentru meniu")


if __name__ == "__main__":
    main()
