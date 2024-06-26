from typing import List

from utils.customer import Customer
from utils.item import Item, ItemType
from utils.market import Market
from utils.seller import Seller
from utils.storage import Storage


def setup_sellers1():
    seller_1 = Seller(1, Storage.inventory_from_list([Item(item_type=ItemType.ENGINE, quantity=1_000_000)]))
    return [seller_1]


def setup_sellers2():
    seller_1 = Seller(1, Storage.inventory_from_list([Item(item_type=ItemType.ENGINE, quantity=5)]))
    seller_2 = Seller(2, Storage.inventory_from_list([Item(item_type=ItemType.ENGINE, quantity=10)]))
    seller_3 = Seller(3, Storage.inventory_from_list([Item(item_type=ItemType.ENGINE, quantity=40)]))
    return [seller_1, seller_2, seller_3]


def setup_customers():
    customer_1 = Customer(1, Storage.inventory_from_list([Item(item_type=ItemType.ENGINE, quantity=10)]))
    customer_2 = Customer(2, Storage.inventory_from_list([Item(item_type=ItemType.ENGINE, quantity=15)]))
    customer_3 = Customer(3, Storage.inventory_from_list([Item(item_type=ItemType.ENGINE, quantity=30)]))
    return [customer_1, customer_2, customer_3]


def find_sellers(market: Market, item_type: ItemType) -> List[Seller]:
    return market.get_available_sellers(item_type)


def print_performance(customers: List[Customer], market: Market, operation_type: str) -> None:
    str_format = '-^80'
    print(f"{'Start Customers':{str_format}}")
    print(*customers, sep='\n')
    print(f"{'Start Market':{str_format}}")
    print(*market.sellers, sep='\n')
    if operation_type == "synch":
        market.synch_simulation(customers)
    else:
        market.thread_simulation(customers)
    print(f"{'Transactions Logs':{str_format}}")
    print(*market.transactions, sep='\n')
    print(f"{'AFTER':{str_format}}")
    print(f"{'Finish Customers':{str_format}}")
    print(*customers, sep='\n')
    print(f"{'Finish Market':{str_format}}")
    print(*market.sellers, sep='\n')


def main():
    customers1 = setup_customers()
    sellers1 = setup_sellers2()
    market1 = Market(sellers1)
    print_performance(customers1, market1, "thread")
    # ======================================
    print("\n\n\n")
    # ======================================
    customers2 = setup_customers()
    sellers2 = setup_sellers2()
    market2 = Market(sellers2)
    print_performance(customers2, market2, "synch")


if __name__ == "__main__":
    main()
