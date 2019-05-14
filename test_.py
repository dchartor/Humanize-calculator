import pytest
from calc import up_to_3_chars, num2word, converter


@pytest.mark.parametrize('num, output', [('5', 'five '), ('56', 'fifty six '), ('567', 'five hundred sixty seven '), 
                                         ('3456', 'three thousand four hundred fifty six '), ('75496', 'seventy five thousand four hundred ninety six '), 
                                         ('857391', 'eight hundred fifty seven thousand three hundred ninety one ')])
def test_num_up_to_6_chars(num, output):
    assert num2word(num) == output


def test_neg_num():
    assert converter('- 74') == 'minus seventy four '


def test_converted_number():
    assert up_to_3_chars(123) == 'one hundred twenty three '


def test_invalid_input():
    assert converter('5 % 5') == 'Invalid input'
    assert converter('') == 'Invalid input'


