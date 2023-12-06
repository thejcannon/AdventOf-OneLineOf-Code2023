# Advent Of (One line of) Code 2023

This repo hosts my solutions to 2023's Advent of Code.

However, there's a twist.

All of the solutions are implemented as Python "one-liners" (more specifically, one-statementers).

I've also done my best attempt at code that is moderately performant (considering the constraints).
That means trying to return-early when possible, not parsing strings if unnecessary, etc....

No AI or cheating (such as writing the code and then using a tool to transform it) of any nature was used to make these.

For most of these, I just wrote the one-liner as-is, without debugging or tests.

I do this because I find the constraints very fun and challenging.

# Tricks

This wouldn't be possible without tricks. I'l try and document them here as I go along.

## The Basics

The basic toolbox for one-liners is crafted almost exclusively from functional programming:

- lambdas: `lambda x, y ...`. Note that a lambda is a callable whose return is the value of the sole expression evaluated
- comprehensions: `x for y in z`.
- `map`: `map(callable, iterable)` lazily yields the result of calling `callable` for each element in `iterable`
- `sum`: `sum(iterable)` just adds all the elements of the iterable
- A bunch of stuff in `itertools`:
  - `starmap` and `takewhile` are very useful
- `functools.reduce`
- Functions from the `operator` module
- Stuff in the `collections` module

## The Tricks

The tricks are as follows:

- Imports: Just use `__import__("<modname>")`
- Getting the first thing out of an iterable: `next(iterable)`
- Consuming an entire iterable just for its side-effects: `collections.deque(iterable, maxlen=0)`
- Variables: Declare a lambda and immediately call it. The variable is the parameter,
  and all inner lambdas (which become closures) will be able to reference it. This looks like:
  `(lambda x, y: <expr>)(<expr>, <expr>)`
  - On problem 1, I hadn't figured this out yet, and instead used `next(starmap(lambda x, y, (<pair>)))`
- Statements for assignment: Use the corresponding dunder method. E.g. `__setitem__` for `x[i] = y`.
- Evaluating Multiple expressions: lambdas can only contain one expression. _However_,
  that expression could be a list, and that list could have multiple elements, and those elements
  can be expressions which **must** be evaluated in order to compute their corresponding values
  in the list. :wink:
  - Or perhaps you know expressions will return a `False`-y value. `(<expr> or <expr>)` is an easy way
    to have both be evaluated with the result being the result of the second expression, given you know
    the first expression will always be `False`-y
    Same goes if you know they will return `True`-thy values using `(<expr> and <expr>)`.
