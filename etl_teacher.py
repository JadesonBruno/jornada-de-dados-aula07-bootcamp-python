import csv
from pathlib import Path
from typing import Dict, Iterator, List


def reader_csv(path: Path) -> List[Dict]:
    """
    Function that reads a CSV and returns a
    dictionary list
    """
    with open(file=path, mode="r", encoding="utf-8") as file:
        reader: Iterator[Dict[str, str]] = csv.DictReader(file)
        dict_list: List[Dict[str, str]] = list(reader)

    return dict_list


def filter_completed_deliveries(list: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """
    Function that filter product when
    Delivery = True
    """
    filtered_list = [
        product_dict for product_dict in list if product_dict.get("entregue") == "True"
    ]

    return filtered_list


def add_values(list: List[Dict[str, str]]) -> float:
    """
    Function that sum product when
    Delivery = True
    """
    sum_price = sum(float(price.get("price")) for price in list)

    return sum_price
