# pylint: disable=missing-docstring
"""
The test module for Prime Factors
"""
import pytest

from prime import generate_prime_factors

def test_incorrect_dat_type():
    with pytest.raises(ValueError):
        generate_prime_factors("str")
        generate_prime_factors(6.6)
