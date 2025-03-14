import csv
from pathlib import Path
from typing import Dict, Iterator, List, Union


def reader_csv(path: Path) -> List[Dict]:
    """
    Function that reads a CSV and returns a
    dictionary list
    """
    with open(file=path, mode="r", encoding="utf-8") as file:
        reader: Iterator[Dict[str, str]] = csv.DictReader(file)
        dict_list: List[Dict[str, str]] = list(reader)

    return dict_list


def process_data(
    product_list: List[Dict[str, str]],
) -> Dict[str, Dict[str, Union[Dict[str, Union[str, int, float]], float]]]:
    """
    Function that processes the product data
    and calculates total sales by category.
    """
    process_data: Dict[
        str, Dict[str, Union[Dict[str, Union[str, int, float]], float]]
    ] = {}

    for item in product_list:
        categoria: str = item["Categoria"]
        produto_info: List[str, Union[str, int, float]] = {
            "Produto": item["Produto"],
            "Quantidade": int(item["Quantidade"]),
            "Venda": float(item["Venda"]),
            "Total": int(item["Quantidade"]) * float(item["Venda"]),
        }

        if categoria not in process_data:
            process_data[categoria] = {
                "Produtos": [produto_info],
                "Total_Vendas": produto_info.get("Total"),
            }
        else:
            process_data[categoria]["Produtos"].append(produto_info)
            process_data[categoria]["Total_Vendas"] += produto_info.get("Total")

    return process_data
