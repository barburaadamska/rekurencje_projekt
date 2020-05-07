# Napisz funkcję, której zadaniem jest mnożenie rekurencyjne elementów dwóch list
# (przykład: [1,2,3,4] oraz [2,4,6,8] dają [2,8,18,32]). Jako argument funkcja
# powinna przyjmować dwie listy (i może, nie musi, coś jeszcze jeśli autor czuję
# taką potrzebę). Zwracać powinna listę z przemnożonymi elementami. Listy powinny
# być tej samej długości. Zaprezentuj działanie funkcji na trzech różnych przykładach.

import random

def generate_list(number_of_elements):
    # generator listy
    list = []
    for i in range(number_of_elements):
        list.append(random.randint(0, 10))
    return list


# def multi_lists(user_list1, user_list2, multiplied):
#     if not user_list1:
#         return "Nie można wykonać mnożenia. Listy puste."
#     else:
#         # dla list o nierównej długości
#         if not len(user_list1) == len(user_list2):
#             return "Nie mozna wykonac mnozenia. Listy roznej dlugosci."
#         else:
#             multiplied.append(user_list1[0] * user_list2[0])
#             # warunek stopu
#             if len(user_list1) == 1:
#                 return multiplied
#             else:
#                 return multi_lists(user_list1[1:], user_list2[1:], multiplied)


# def multi_vol2(user_list1, user_list2):
#     if not user_list1:
#         return []
#     else:
#         if not len(user_list1) == len(user_list2):
#             return []
#         else:
#             if len(user_list1) == 1:
#                 return [user_list1[0] * user_list2[0]]
#             else:
#                 return [user_list1[0] * user_list2[0]] + multi_vol2(user_list1[1:], user_list2[1:])



# def multi_vol2(user_list1, user_list2):
#     if not user_list1 or (not len(user_list1) == len(user_list2)):
#         return []
#     else:
#         return [user_list1[0] * user_list2[0]] + multi_vol2(user_list1[1:], user_list2[1:])


for i in range(3):
    # wygenerowanie list
    user_elements = int(input("Ile elementow maja miec Twoje listy? "))
    lista1, lista2 = generate_list(user_elements), generate_list(user_elements)
    wynik = []

    # wyświetlenie wyniku
    print("Pierwsza lista to: ", lista1)
    print("Druga lista to: ", lista2)
    print("Wynik to:", multi_vol2(lista1, lista2))
    print()

# # Napisz funkcję, która odwraca łańcuch znaków, np. "znaków" zamienia na "wókanz". Funkcja ma pobierać stringa
# # i zwracać jego odwróconą wersję. Zaprezentuj działanie funkcji na trzech różnych stringach (o różnych
# # zawartościach i długościach).
#
# def reversed_string(user_string):
#     return user_string[::-1]
#
# for i in range(3):
#     sprawdzenie = input("Jaki string chcesz odwrocic? ")
#     user_reversed = reversed_string(sprawdzenie)
#     print(user_reversed)

# # Napisz funkcję dysjunkcja(zmiennaP, zmiennaQ), która jest funkcją dysjunkcji i zwraca „True” lub ”False”.
# # Funkcja pobiera może pobierać (wybierz jedno): dwa inty (0 i 1), dwa stringi („0”, „1”) lub „True” i ”False”.
# # Zaprezentuj działanie funkcji dla wszystkich możliwych kombinacji.
#
# def disjunction(P_var, Q_var):
#     if P_var and Q_var:
#         return False
#     else:
#         return True
#
# # dla obu fałszywych
# p = True
# q = True
#
# print("Gdy p = 01i q = 1:", disjunction(p, q))
#
#
# # dla jednej prawdziwej wartosci
#
# r = True
# s = False
#
# print("Gdy r = 1 i s = 0:", disjunction(r, s))
#
#
# # dla obu prawdziwych
#
# t = False
# u = False
#
# print("Gdy t = 0 i u = 0:", disjunction(t, u))
#
# for p in [True, False]:
#     for q in [True, False]:
#         print("p = {}, q = {}, dysjunkcja = {}".format(p, q, disjunction(p, q)))