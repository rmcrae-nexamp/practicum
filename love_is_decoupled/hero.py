# Removed the import statement for the Partner class and HERO variable to decouple the two modules.
import concurrent.futures
import copy
from typing import Dict, List, Literal, Optional, Protocol, Set

from .wellness import Wellness


class Partner(Protocol):
    """Created an interface for the partner."""

    def communicate(self) -> Optional[bool]:
        """Check if the partner is communicating with the Hero. If the
        partner is communicating, return True. If the partner is not
        communicating, return False.

        Returns:
            Optional[bool]: If the partner is communicating
        """

    def list_priorities(self) -> List[str]:
        """List the partner's priorities. The partner will return a list
        of their priorities.

        Returns:
            List[str]: The partner's priorities
        """


class Hero:

    _partner: Optional[Partner] = None
    _wellness: Literal[Wellness.JUST_FINE, Wellness.UNHEALTHY] = Wellness.JUST_FINE

    def __init__(self, name: str, interests: List[str], patience: int):
        self.name = name
        self.interests = interests
        self.patience = patience

    @property
    def partner(self) -> Optional[Partner]:
        # Rather than the Hero creating a Partner instance, the Partner instance
        # is passed in as a dependency.
        return self._partner

    @partner.setter
    def partner(self, partner: Partner) -> None:
        if not self.wellness == Wellness.JUST_FINE:
            raise ValueError("The Hero is not well. They cannot have a partner.")

        if not self._check_partner(patience=self.patience):
            raise ValueError(
                "The potential partner is not communicating. The Hero doesn't want them."
            )

        self._partner = partner

    async def get_relationship_wellness(
        self,
    ) -> Literal[Wellness.JUST_FINE, Wellness.UNHEALTHY]:
        """See how well the Hero is doing in their relationship. The Hero will first check in
        with their partner to see if they are communicating. If they aren't
        talking, the Hero will return that they are not doing well. If they
        are communicating, the Hero will return that they are doing just
        fine.

        Returns:
            Literal[Wellness.JUST_FINE, Wellness.UNHEALTHY]: How the hero is doing
        """
        communication = await self._check_partner(patience=self.patience)
        if communication is False:
            return Wellness.UNHEALTHY
        return Wellness.JUST_FINE

    @property
    def wellness(self) -> Wellness:
        # Separating the wellness of the Hero from the relationship status.
        return self._wellness

    @wellness.setter
    def wellness(self, wellness: Wellness) -> None:
        self._wellness = wellness

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
        if not self.partner:
            return True

        # Might time out if the partner takes too long to list priorities.
        partner_priorities = self.partner.list_priorities()
        return type(self).__name__.lower() not in partner_priorities

    def persona(self) -> "Hero":
        return copy.deepcopy(self)

    async def _check_partner(self, patience: int) -> bool:
        if not self.partner:
            return False

        # TICK TICK! The Hero doesn't have all day.
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(self.partner.communicate)
            try:
                return future.result(timeout=patience)
            except concurrent.futures.TimeoutError:
                return False

    def _get_partner_priorities(self) -> Set[str]:
        if not self.partner:
            return set()

        partner_priorities = self.partner.list_priorities()
        if not partner_priorities:
            return set()
        return set(self.partner.list_priorities())

    def _construct_life_plan(
        self, partner_priorities: Set[str] = None
    ) -> Dict[str, int]:
        # The Hero should be able to construct a life plan with or without a partner.
        if not partner_priorities:
            partner_priorities = set()

        return {
            interest: self._value_interest_for_life_plan(interest, partner_priorities)
            for interest in self.interests
        }

    @staticmethod
    def _value_interest_for_life_plan(interest: str, partner_priorities: Set[str]):
        return 2 if interest in partner_priorities else 1
