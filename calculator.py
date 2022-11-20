from functools import reduce

def calculator():
    line = input("Введите арифметическое выражение, используя только + и * в качестве арифметических операторов: ")
    split_line = line.split("+")
    for a in split_line:
        if "*" in a:
            a_list = a.split("*")
            split_line.insert(split_line.index(a), reduce(lambda x, y: int(x) * int(y), a_list))
            split_line.pop(split_line.index(a))
    res_calc = reduce(lambda x, y: int(x) + int(y), split_line)
    result = f"{line} = {res_calc}"
    return print(result)

if __name__ == "__main__":
    calculator()
