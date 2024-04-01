#!/usr/bin/env python3

"""
    Adds 'get_page' method to server class    
"""

import csv
import math
from typing import List, Tuple

class Server:
    """
        Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
            Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]


        return self.__dataset
    
    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
            Calculates the size and end index range for a page with page_size
        """
        nextPageStartIndex = page * page_size
        return nextPageStartIndex - page_size, nextPageStartIndex
    
    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
            Get itema for the given page number

            Args:
                page (int): page number
                page_size (int): number of items per page
            Returns:
            (List[List]): a list of items
            ([]): an empty list if the input is out of range
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        startIndex, endIndex = self.index_range(page, page_size)
        return self.dataset()[startIndex:endIndex]
