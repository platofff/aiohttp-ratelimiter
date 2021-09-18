from asyncio.coroutines import iscoroutinefunction
from typing import Callable, Any, Union
from asyncio import iscoroutinefunction
from sys import getsizeof


none = lambda: None
IntOrFloat = Union[int, float]


class MemorySafeDict:
    """
    MemorySafeDict acts as a defaultdict, but it allows you to specify the max ammount of memory it can use and it will never throw a MemoryError
    """
    
    def __init__(self, dictionary: dict = None, default: Callable = None, max_memory: IntOrFloat = None, main = None) -> None: ...

    def set_max_memory(self, size: IntOrFloat) -> None: ...

    def append_nested_dict(self, dictionary: MemorySafeDict) -> None:
        """
        This method adds any nested MemorySafeDict to a list so it can add it to the total size.
        Not adding your nested dict could make your max memory not effective.
        Don't use this unless you are using the max_memory feature.
        """

    def __missing__(self, key) -> None: ...

    def __getitem__(self, key) -> Any: ...

    def __setitem__(self, key, value) -> None: ...
             
    def __repr__(self) -> str: ...

    def __iter__(self): ...

    def __call__(self):
        """
        Calls all callable values in the dict.
        """
    
    def __delitem__(self, key) -> None: ...

    def __len__(self) -> int: ...

    def pop(self, key) -> None: ...

    def keys(self): ...

    def values(self): ...

    def update(self, dictionary: dict) -> None: ...

    def any(self) -> bool: ...

    def getsize(self) -> IntOrFloat: ...

    def get(self, key) -> None: ...

    def clear(self) -> None: ...

    def sorted_values(self, reverse: bool = False) -> list: ...

    def sorted_keys(self, reverse: bool = False) -> list: ...

# Tesing performance
# import time

# def test():
#     start = time.time()
#     dict = MemorySafeDict(max_memory=1)
#     for i in range(100000000**100):
#         dict.update({i:i})
#     end = time.time()
#     print(end-start)

# test()