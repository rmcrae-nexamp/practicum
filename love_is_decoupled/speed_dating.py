import asyncio
from typing import List, Literal, Optional, Protocol

from .wellness import Wellness


class Hero(Protocol):

    def partner(self) -> Optional["Partner"]: ...
    async def get_relationship_wellness(
        self,
    ) -> Literal[Wellness.JUST_FINE, Wellness.UNHEALTHY]: ...

    def persona(self) -> "Hero": ...


class Partner(Protocol):
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


class SpeedDating:
    def __init__(self, hero: Hero):
        self.hero = hero
        self.potential_partners: List[Partner] = list()

    def mingle(self, speed_dating_partner_pool: List[Partner]):
        asyncio.run(self._chat(speed_dating_partner_pool))
        return self.potential_partners

    async def _chat(self, speed_dating_partner_pool: List[Partner]):
        interactions = list()

        for partner in speed_dating_partner_pool:
            persona = self.hero.persona()
            persona.partner = partner
            interactions.append(persona)

        results = await asyncio.gather(
            *[hero_persona.get_relationship_wellness() for hero_persona in interactions]
        )

        for hero_persona, result in zip(interactions, results):
            if result == Wellness.JUST_FINE:
                await self._match(hero_persona.partner)

    async def _match(self, potential_partner: Partner):
        self.potential_partners.append(potential_partner)
