# sprawdz, czy dany element znajduje sie w liscie

import random

def generate_list(number_of_elements):
    list = []
    for i in range(number_of_elements):
        list.append(random.randint(0, 10))
    return list


def sprawdzanie(user_element, user_list):        # JUŻ DZIAŁA, JEST GITUWENCKA
    if len(user_list) == 0:
        return False
    if len(user_list) >= 1:
        if user_list[0] == user_element:
            return True
        else:
            return sprawdzanie(user_element, user_list[1:])


def sprawdzanie(user_element, user_list):  # TO TEŻ DZIAŁA, ALE LEPIEJ XD
    if not user_list:
        return False
    else:
        if user_list[0] == user_element:
            return True
        else:
            return sprawdzanie(user_element, user_list[1:])


for i in range(3):
    user_elements = int(input("Ile elementow ma miec Twoja lista? "))
    user_list = generate_list(user_elements)
    print("Twoja lista to:", user_list)

    to_check = int(input("Jaki element chcesz sprawdzic? "))
    sprawdzona = sprawdzanie(to_check, user_list)
    print(sprawdzona)
