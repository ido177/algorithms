from time import time


def counter(char_list: list, max_val=2) -> list:
    dict_l_c = {key: char_list.count(key) for key in set(char_list)}
    amount = sorted(set(val for val in dict_l_c.values()))
    letters = [letter for letter in dict_l_c if dict_l_c[letter] == amount[-max_val]]
    return letters


test_list = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'z', 'q', 'f', 'f', 'f'] * 1000000

if __name__ == "__main__":
    start = time()
    print(*counter(test_list))
    end = time()
    print(end - start, 'sec')
