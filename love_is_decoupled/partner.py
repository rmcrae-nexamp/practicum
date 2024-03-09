"""
YOU SHALL NOT CHANGE THE INTERNALS OF THIS MODULE!!!!!!!
"""

from typing import Optional, List

import time

BITCOIN = "bitcoin"
DOPE_SHIT = "dope_shit"
MYSELF = "myself"
TOMMY = "Tom Brady"
HERO = "hero"


class Partner:
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
        self.priorities = [DOPE_SHIT, BITCOIN, MYSELF, TOMMY, MYSELF, HERO]
        return None

    def __look_at_phone(self) -> None:
        time.sleep(2)
        return None

    def __play_halo(self) -> None:
        time.sleep(2)
        return None
