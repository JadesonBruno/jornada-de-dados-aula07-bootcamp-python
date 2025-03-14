# import python standard libraries
from pathlib import Path

# import local modules
from etl_teacher import add_values, filter_completed_deliveries, reader_csv


def main():
    file_path = Path("teacher_sales.csv")
    products = reader_csv(path=file_path)
    products_deliveries = filter_completed_deliveries(list=products)
    print(products_deliveries)
    print(add_values(products_deliveries))


if __name__ == "__main__":
    main()
