import pytest

from sasin import Number, _human_readable, pln_to_sasin


TEST_CASES_POSITIVE = [
    (1, "1"),
    (20, "20"),
    (300, "300"),
    (4000, "4 k"),
    (50000, "50 k"),
    (600000, "600 k"),
    (7000000, "7 M"),
    (7123456, "7.12 M"),
    (7129999, "7.13 M"),
    (0.1, "100 m"),
    (0.02, "20 m"),
    (0.003, "3 m"),
    (0.0004, "400 μ"),
    (0.00005123, "51.23 μ"),
    (0.000005129, "5.13 μ"),
    (1000000000000000000000000000000000000000, "1000000000000000 Y"),
]


@pytest.mark.parametrize(
    ["number", "formatted"],
    TEST_CASES_POSITIVE,
)
def test_human_readable_when_positive(number: Number, formatted: str) -> None:
    assert _human_readable(number) == formatted


@pytest.mark.parametrize(["number", "formatted"], TEST_CASES_POSITIVE)
def test_human_readable_when_negative(number: Number, formatted: str) -> None:
    assert _human_readable(-1 * number) == f"-{formatted}"


@pytest.mark.parametrize(
    ["number", "formatted"], [(0, "0"), (0.0, "0"), (-0, "0"), (0.0, "0")]
)
def test_human_readable_when_zero(number: Number, formatted: str) -> None:
    assert _human_readable(number) == formatted


@pytest.mark.parametrize(
    ["pln", "sasin"],
    [
        (0, "ziobrosasin"),
        (0.0, "ziobrosasin"),
        (15000, "214.29 μsasin"),
        (1495900, "21.37 msasin"),
        (2137.1410, "30.53 μsasin"),
        (70000000, "1 sasin"),
        (-0, "ziobrosasin"),
        (-0.0, "ziobrosasin"),
        (-15000, "-214.29 μsasin"),
        (-1495900, "-21.37 msasin"),
        (-2137.1410, "-30.53 μsasin"),
        (-70000000, "-1 sasin"),
    ],
)
def test_pln_to_sasin(pln: Number, sasin: str) -> None:
    assert pln_to_sasin(pln) == sasin
