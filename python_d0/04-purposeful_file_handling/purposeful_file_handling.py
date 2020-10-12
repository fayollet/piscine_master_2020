import csv
from typing import List, Generator, Any

author = "courte_e"

def read_csv(filename: str, delimiter: str = ',', raise_on_error: bool = False) -> Generator[List[Any], None, None]:
    pass
    
def create_csv(filename: str, fieldnames: List[str] , data: List[List[Any]]):
data = [['1', '2'], ['3', '1']]
stage.create_csv('my.csv', ['id', 'value'], data)
print('\n'.join(stage.read_csv('my.csv')))
