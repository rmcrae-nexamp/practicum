from .partner import Partner
from .wellness import Wellness


class Hero:

    _partner: Partner | None = None

    def __init__(self, name: str, interests: list[str]):
        self.name = name
        self.interests = interests

    @property
    def partner(self):
        if not self._partner:
            self._partner = Partner()
        return self._partner

    def get_wellness(self):
        communincation = self._check_partner()
        if communincation is None:
            return Wellness.UNHEALTHY
        return Wellness.FAIR
    
    def get_life_plan(self) -> dict[str, int]:
        partner_priorities = self.partner.list_priorities()
        life_plan = {
            interest: self._value_interest_for_life_plan(interest, partner_priorities)
            for interest in self.interests
        }
        return life_plan

    def _check_partner(self):
        return self.partner.communicate()
    
    def _value_interest_for_life_plan(self, interest: str, partner_priorities: list[str]):
        return 2 if interest in partner_priorities else 1
    

