from pytest import raises
from primitives import NumberRange, NumberRangeException


class TestNumberRangeInit(object):
    def test_init_supports_multiple_args(args):
        num_range = NumberRange(1, 3)
        assert num_range.lower == 1
        assert num_range.upper == 3

    def test_init_supports_strings(args):
        num_range = NumberRange('1-3')
        assert num_range.lower == 1
        assert num_range.upper == 3

    def test_init_supports_strings_with_spaces(args):
        num_range = NumberRange('1 - 3')
        assert num_range.lower == 1
        assert num_range.upper == 3

    def test_init_supports_exact_ranges_as_strings(args):
        num_range = NumberRange('3')
        assert num_range.lower == 3
        assert num_range.upper == 3

    def test_init_supports_integers(args):
        num_range = NumberRange(3)
        assert num_range.lower == 3
        assert num_range.upper == 3


def test_equality_operator():
    assert NumberRange(1, 3) == NumberRange(1, 3)


def test_str_representation():
    assert str(NumberRange(1, 3)) == '1 - 3'
    assert str(NumberRange(1, 1)) == '1'


def test_raises_exception_for_badly_constructed_range():
    with raises(NumberRangeException):
        NumberRange(3, 2)


def test_from_str_exception_handling():
    with raises(NumberRangeException):
        NumberRange('1 - ')


def test_from_normalized_str():
    assert str(NumberRange.from_normalized_str('[1,2]')) == '1 - 2'
    assert str(NumberRange.from_normalized_str('[1,3)')) == '1 - 2'
    assert str(NumberRange.from_normalized_str('(1,3)')) == '2'


class TestArithmeticOperators(object):
    def test_add_operator(self):
        assert NumberRange(1, 2) + NumberRange(1, 2) == NumberRange(2, 4)

    def test_sub_operator(self):
        assert NumberRange(1, 3) - NumberRange(1, 2) == NumberRange(0, 1)

    def test_isub_operator(self):
        range_ = NumberRange(1, 3)
        range_ -= NumberRange(1, 2)
        assert range_ == NumberRange(0, 1)

    def test_iadd_operator(self):
        range_ = NumberRange(1, 2)
        range_ += NumberRange(1, 2)
        assert range_ == NumberRange(2, 4)
