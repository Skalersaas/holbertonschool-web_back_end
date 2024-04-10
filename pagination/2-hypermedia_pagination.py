#!/usr/bin/env python3
"""
This file contains function that  return
a tuple of size two containing a start index and an end index
corresponding to the range of indexes to return
in a list for those particular pagination parameters.
"""
import csv
import math
from typing import List, Tuple, Dict


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
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            List[List]: _description_
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page_size > 0 and page > 0
        nameRange = index_range(page, page_size)
        try:
            return self.dataset()[nameRange[0]:nameRange[1]]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """_summary_

        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.

        Returns:
            Dict: _description_
        """
        nameList = self.get_page(page, page_size)
        total = math.ceil(len(self.dataset()) / page_size)
        return {
            'page_size': len(nameList),
            'page': page,
            'data': nameList,
            'next_page': page + 1 if page < total else None,
            'prev_page': page - 1 if page != 1 else None,
            'total_page': total
        }
