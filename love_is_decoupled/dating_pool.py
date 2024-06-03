import time
from typing import List, Optional

from .partner import BITCOIN, DOPE_SHIT, HERO, MYSELF, TOMMY


class LongTermPartner:
    def __init__(self, priorities: Optional[List[str]] = None):
        self.priorities = priorities

    def __str__(self):
        return "I'll call you back later."

    def communicate(self):
        self.__look_at_phone()
        self.__play_halo()
        return "Hey, what's up?"

    def list_priorities(self):
        if not self.priorities:
            self._set_priorities()
        return self.priorities

    def _set_priorities(self):
        self.__look_at_phone()
        self.__play_halo()
        self.priorities = [MYSELF, HERO, DOPE_SHIT, BITCOIN]
        return None

    def __look_at_phone(self) -> None:
        time.sleep(2)
        return None

    def __play_halo(self) -> None:
        time.sleep(2)
        return None


class ShortTermPartner:
    def __init__(self, priorities: Optional[List[str]] = None):
        self.priorities = priorities

    def __str__(self):
        return "I'm busy right now. I'll call you back later."

    def communicate(self):
        self.__look_at_phone()
        self.__play_halo()
        return "Hey, what's up?"

    def list_priorities(self):
        if not self.priorities:
            self._set_priorities()
        return self.priorities

    def _set_priorities(self):
        self.__look_at_phone()
        self.__play_halo()
        self.priorities = [TOMMY, MYSELF, BITCOIN, DOPE_SHIT, MYSELF, TOMMY, HERO]
        return None

    def __look_at_phone(self) -> None:
        time.sleep(2)
        return None

    def __play_halo(self) -> None:
        time.sleep(2)
        return None
