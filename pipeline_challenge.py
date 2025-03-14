# import python standard libraries
from pathlib import Path

# import local modules
from etl_challenge import process_data, reader_csv


def main():
    data = reader_csv(Path("sales.csv"))
    categorized_products = process_data(data)
    print(categorized_products)


if __name__ == "__main__":
    main()
