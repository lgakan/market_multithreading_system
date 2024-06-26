from typing import List
from queue import PriorityQueue

from .seller import Seller
from .item import ItemType
from .seller_priority import SellerPriority


class SellerQueue:

    def __init__(self, item_type: ItemType, sellers: List[Seller]):
        self.item_type = item_type
        self.queue = PriorityQueue()
        for seller in sellers:
            item_quantity = seller.storage.find_item_by_item_type(self.item_type).quantity
            if item_quantity:
                self.queue.put(SellerPriority(-item_quantity, seller))
        self.is_free = True

    def push(self, new_item_quantity: int, seller: Seller):
        self.is_free = False
        self.queue.put(SellerPriority(-new_item_quantity, seller))
        self.is_free = True

    def pop(self):
        seller_priority_obj = self.queue.get()
        return -seller_priority_obj.priority, seller_priority_obj.seller
