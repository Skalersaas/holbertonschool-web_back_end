"""
This file contains function that  return
a tuple of size two containing a start index and an end index
corresponding to the range of indexes to return
in a list for those particular pagination parameters.
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    '''method'''
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert page > 0
        assert page_size > 0
        nameRange = index_range(page, page_size)
        return self.dataset()[nameRange[0]:nameRange[1]]
serv = Server()
serv.get_page(1, 5)