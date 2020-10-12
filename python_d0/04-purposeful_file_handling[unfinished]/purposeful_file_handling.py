import csv
from typing import List, Generator, Any

author = "courte_e"


def read_csv(filename: str, delimiter: str = ',', raise_on_error: bool = False) \
             -> Generator[List[Any], None, None]:
    f = open(filename, "r")
    t = f.read().split('\n')
    f.close()
    def gen():
        index = t[0].split(delimiter)
        il = len(index)
        yield index
        for i in t[1:]:
            d = i.split(delimiter)
            if len(d) < il and raise_on_error is True:
                raise ValueError
            yield map(str, d + [None] * (len(d) - il))
    return gen()


def create_csv(filename: str, fieldnames: List[str], data: List[List[Any]]):
    f = open(filename, "w")
    f.write('\n'.join([','.join(fieldnames)] + [','.join(i) for i in data]))
    f.close()
    return


data = [['1', '2'], ['3', '1']]
create_csv('my.csv', ['id', 'value'], data)
print('\n'.join(read_csv('my.csv')))
