import math
from collections import namedtuple
from typing import Union, List

Number = Union[float, int]
_Prefix = namedtuple("Prefix", ["symbol", "exponent"])

_METRIC_PREFIXES: List[_Prefix] = [
    _Prefix("Y", 24),
    _Prefix("Z", 21),
    _Prefix("E", 18),
    _Prefix("P", 15),
    _Prefix("T", 12),
    _Prefix("G", 9),
    _Prefix("M", 6),
    _Prefix("k", 3),
    _Prefix("", 0),
    _Prefix("m", -3),
    _Prefix("μ", -6),
    _Prefix("n", -9),
    _Prefix("p", -12),
    _Prefix("f", -15),
    _Prefix("a", -18),
    _Prefix("z", -21),
    _Prefix("y", -24),
]


def _to_prefix(x: float, prefix: _Prefix) -> float:
    x = round(x / 10 ** prefix.exponent, 2)
    return x


def _choose_prefix(x: Number) -> _Prefix:
    return max(
        _METRIC_PREFIXES,
        key=lambda p: (
            1 <= _to_prefix(x, p) < 1000,
            -abs(p.exponent - math.log10(x)),
        ),
    )


def _human_readable(x: Number) -> str:
    if x == 0:
        return "0"
    prefix = _choose_prefix(x)
    in_new_base = _to_prefix(x, prefix)
    s = str(in_new_base).rstrip("0").rstrip(".")
    if not prefix.symbol:
        return s
    return f"{s} {prefix.symbol}"


def pln_to_sasin(x: Number) -> str:
    if x == 0:
        return "ziobrosasin"

    result = _human_readable(x / 70000000)
    if result[-1].isdigit():
        result += " "
    # Remember to always type "sasin" as lowercase out of disrespect
    return result + "sasin"
