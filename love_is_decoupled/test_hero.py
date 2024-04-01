import asyncio

from .hero import Hero
from .partner import Partner, BITCOIN, DOPE_SHIT, HERO, MYSELF
from .wellness import Wellness


"""
Geezum creepers, I am finding it really hard to validate the expected behaviors
of our Hero.

The tests are taking forever to run. Its slowing down my feedback,
and its making it a real pain to continue to develop the Hero.

There are a couple of cases that I'd like to test, but its just so painful.

Right now there is a lot of beahvior that I'd like to test in the three public
methods (get_wellness, get_life_plan, should_find_new_partner) of the Hero class.
But I am finding it really hard to do so.

I'd also like to clean-codeify Hero, but without tests in place, that would be
irresponsible.
"""


def test_hero_get_relationship_wellness():
    """
    Given:
        - a Hero instance has a partner

    When:
        - the get_relationship_wellness method is called

    Then:
        - the method should return Wellness.JUST_FINE
    """
    # Given
    partner = Partner(priorities=[HERO])
    hero = Hero(name="Pat", interests=["doesn't matter"], patience=5)
    hero.partner = partner

    # When
    wellness = asyncio.run(hero.get_relationship_wellness())

    # Then
    assert wellness == Wellness.JUST_FINE


def test_hero_get_relationship_wellness_little_patience():
    """
    Given:
        - a Hero instance has a partner

    When:
        - the get_relationship_wellness method is called
        - the partner takes too long to communicate

    Then:
        - the method should return Wellness.UNHEALTHY
    """
    # Given
    partner = Partner(priorities=[HERO])
    hero = Hero(name="Pat", interests=["doesn't matter"], patience=1)
    hero.partner = partner

    # When
    wellness = asyncio.run(hero.get_relationship_wellness())

    # Then
    assert wellness == Wellness.UNHEALTHY


def test_hero_get_relationship_wellness_no_partner():
    """
    Given:
        - a Hero instance has no partner

    When:
        - the get_relationship_wellness method is called

    Then:
        - the method should return Wellness.UNHEALTHY
    """
    # Given
    hero = Hero(name="Pat", interests=["doesn't matter"], patience=1)

    # When
    wellness = asyncio.run(hero.get_relationship_wellness())

    # Then
    assert wellness == Wellness.UNHEALTHY


def test_hero_get_life_plan():
    """
    Given:
        - a Hero instance
        - a Partner that has no overlapping interests with the Hero

    When:
        - the get_life_plan method is called

    Then:
        - the method should return a dictionary with the interests as keys and the value as 1
    """
    # Given
    partner = Partner(priorities=[BITCOIN, DOPE_SHIT])
    hero = Hero(name="Vic", interests=["entrepreneurship", "helping others"], patience=1)
    hero.partner = partner

    # When
    life_plan = hero.get_life_plan()

    # Then
    assert life_plan == {"entrepreneurship": 1, "helping others": 1}


def test_hero_get_life_plan_with_overlapping_interests():
    """
    Given:
        - a Hero instance
        - a Partner that has overlapping interests with the Hero

    When:
        - the get_life_plan method is called

    Then:
        - the method should return a dictionary with the interests as keys and the value as 2
    """
    # Given
    partner = Partner(priorities=["helping others", "dope"])
    hero = Hero(name="Vic", interests=["entrepreneurship", "helping others"], patience=0)
    hero.partner = partner

    # When
    life_plan = hero.get_life_plan()

    # Then
    assert life_plan == {"entrepreneurship": 1, "helping others": 2}


def test_hero_get_life_plan_no_partner():
    """
    Given:
        - a Hero instance with no partner

    When:
        - the get_life_plan method is called

    Then:
        - the method should return the hero's interests as keys and the value as 1
    """
    # Given
    hero = Hero(name="Vic", interests=["entrepreneurship", "helping others"], patience=0)

    # When
    life_plan = hero.get_life_plan()

    # Then
    assert life_plan == {"entrepreneurship": 1, "helping others": 1}


def test_hero_should_find_new_partner():
    """
    Given:
        - a Hero instance
        - a Partner with HERO in its list of priorities

    When:
        - the should_find_new_partner method is called

    Then:
        - the method should return False
    """
    # Given
    partner = Partner(priorities=[HERO])
    hero = Hero(name="Tracy", interests=["vaping", "Jean-Claude Van Damme"], patience=0)
    hero.partner = partner

    # When
    should_find_new_partner = hero.should_find_new_partner()

    # Then
    assert should_find_new_partner is False


def test_hero_should_find_new_partner_no_partner():
    """
    Given:
        - a Hero instance with no partner

    When:
        - the should_find_new_partner method is called

    Then:
        - the method should return True
    """
    # Given
    hero = Hero(name="Tracy", interests=["vaping", "Jean-Claude Van Damme"], patience=0)

    # When
    should_find_new_partner = hero.should_find_new_partner()

    # Then
    assert should_find_new_partner is True
