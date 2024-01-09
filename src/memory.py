from abc import ABC, abstractmethod
from collections import defaultdict, deque
from typing import Dict, List


class MemoryInterface(ABC):

    @abstractmethod
    def append(self, user_id: int, user_content: Dict, model_content: Dict):
        pass

    @abstractmethod
    def get(self, user_id: int) -> List[Dict]:
        pass

    @abstractmethod
    def remove(self, user_id: int):
        pass


class Memory(MemoryInterface):

    def __init__(self, max_capacity: int):
        self.storage = defaultdict(deque)
        self.max_capacity = 2 * max_capacity # A unit represents a conversation


    def append(self, user_id: int, user_content: Dict, model_content: Dict):
        self.storage[user_id].append(user_content)
        self.storage[user_id].append(model_content)

        while self.storage[user_id] and len(self.storage[user_id]) > self.max_capacity:
            self.storage[user_id].popleft() # Pop an user content and a model content


    def get(self, user_id: int) -> List[Dict]:
        return list(self.storage[user_id])
    

    def remove(self, user_id: int):
        self.storage[user_id].clear()