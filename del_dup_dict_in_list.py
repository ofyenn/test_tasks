# del_dup_dict_in_list
#    Дано: Список dict-объектов вида вида {"key": "value"}, например
# [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {},
# {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}].
#    Напишите функцию, которая удаляет дубликаты из этого списка.
# Для примера выше возвращаемое значение может быть равно
# [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {},
# {"key2": "value2"}].
# Обязательное условие: функция не должна иметь сложность O(n^2).


def del_duplicator(ints_list):
    if not isinstance(ints_list, list):
        raise Exception("Variable not list")
    len_list = len(ints_list)
    if len_list < 2:
        return ints_list
    read_position = 1
    ins_pos = 1
    while read_position < len_list:
        if not ints_list[read_position] in ints_list[:ins_pos]:
            ints_list[ins_pos] = ints_list[read_position]
            ins_pos += 1
        read_position += 1
    ints_list = ints_list[:ins_pos]
    return(ints_list)


ints_list = [
             {"key1": "value1"},
             {"k1": "v1", "k2": "v2", "k3": "v3"},
             {},
             {},
             {"key1": "value1"},
             {"key1": "value1"},
             {"key2": "value2"},
             {"key2": "value2"}
             ]

if __name__ == '__mail__':
    answer = del_duplicator(ints_list)
    print(answer)
