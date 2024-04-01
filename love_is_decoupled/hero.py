# Removed the import statement for the Partner class and HERO variable to decouple the two modules.
from typing import Dict, List, Literal, Optional, Protocol, Set

from .wellness import Wellness


class Hero:

    _partner: Optional[Partner] = None

    def __init__(self, name: str, interests: List[str]):
        self.name = name
        self.interests = interests

    @property
    def partner(self):
        if not self._partner:
            self._partner = Partner()
        return self._partner

    def get_wellness(self) -> Literal[Wellness.JUST_FINE, Wellness.UNHEALTHY]:
        """See how well the Hero is doing. The Hero will first check in
        with their partner to see if they are communicating. If they aren't
        talking, the Hero will return that they are not doing well. If they
        are communicating, the Hero will return that they are doing just
        fine.

        Returns:
            Literal[Wellness.JUST_FINE, Wellness.UNHEALTHY]: How the hero is doing
        """
        communincation = self._check_partner()
        if communincation is None:
            return Wellness.UNHEALTHY
        return Wellness.JUST_FINE

    def get_life_plan(self) -> Dict[str, int]:
        """Construct a life plan for the Hero. The Hero will first check
        in with their partner to see what their priorities are. The Hero
        will then construct a life plan based on their own interests and
        their partner's priorities.

        Returns:
            Dict[str, int]: Interests and their values for the life plan
        """
        partner_priorities = self._get_partner_priorities()
        life_plan = self._construct_life_plan(partner_priorities)
        return life_plan

    def should_find_new_partner(self) -> bool:
        """Check if the Hero should find a new partner. The Hero will
        check if they are in their partner's list of priorities. If they
        are not, the Hero will return True. If they are, the Hero will
        return False.

        Returns:
            bool: If the Hero should find a new partner
        """
        partner_priorities = self.partner.list_priorities()
        return HERO not in partner_priorities

    def _check_partner(self):
        return self.partner.communicate()

    def _get_partner_priorities(self) -> Set[str]:
        partner_priorities = self.partner.list_priorities()
        if not partner_priorities:
            return set()
        return set(self.partner.list_priorities())

    def _construct_life_plan(self, partner_priorities: Set[str]) -> Dict[str, int]:
        return {
            interest: self._value_interest_for_life_plan(interest, partner_priorities)
            for interest in self.interests
        }

    def _value_interest_for_life_plan(self, interest: str, partner_priorities: Set[str]):
        return 2 if interest in partner_priorities else 1
