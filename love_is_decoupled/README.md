# Love is Decoupled

This project is designed for a practicum. It is inspired by software that I seen in the wild, and I have modeled the issues encountered within it to have similar impact and affects.


## The Goods

The Hero of our story is in a bad spot. They are defined as a class in the `hero.py` module. There is some obvious behavior in the Hero that is not validated under test. It seems like the Hero could be generally improved, but while its not under test, that is risky.

Our poor Hero seems to be in an unhealthy relationship, but I don't see how they could move on.

As you work through making improvements, treat the `partner.py` module as if it were a third party service that you have no control over. Add tests in the `test_hero.py` module, use whatever tools or techniques you'd like, and fix some shiz!

## Getting Set Up

```sh
% python3 -m venv venv
% source venv/bin/activate
% pip install -r requirements.txt
```

## Running the Tests

Note, THE TESTS ARE VERY SLOW. This is part of the problem to solve.

To run the tests:

```sh
% python -m pytest .
```