import six


class NumberRangeException(Exception):
    pass


class RangeBoundsException(NumberRangeException):
    def __init__(self, lower, upper):
        self.message = 'Min value %d is bigger than max value %d.' % (
            lower,
            upper
        )


class NumberRange(object):
    def __init__(self, *args):
        if len(args) > 2:
            raise NumberRangeException(
                'NumberRange takes at most two arguments'
            )
        elif len(args) == 2:
            lower, upper = args
            if lower > upper:
                raise RangeBoundsException(lower, upper)
            self.lower = lower
            self.upper = upper
        else:
            if isinstance(args[0], six.integer_types):
                self.lower = self.upper = args[0]
            elif isinstance(args[0], six.string_types):
                self.lower, self.upper = self.parse_range(args[0])

    @classmethod
    def from_range_object(cls, value):
        lower = value.lower
        upper = value.upper
        if not value.lower_inc:
            lower += 1

        if not value.upper_inc:
            upper -= 1

        return cls(lower, upper)

    @classmethod
    def from_normalized_str(cls, value):
        """
        Returns new NumberRange object from normalized number range format.

        Example ::

            range = NumberRange.from_normalized_str('[23, 45]')
            range.lower = 23
            range.upper = 45

            range = NumberRange.from_normalized_str('(23, 45]')
            range.lower = 24
            range.upper = 45

            range = NumberRange.from_normalized_str('(23, 45)')
            range.lower = 24
            range.upper = 44
        """
        if value is not None:
            values = value[1:-1].split(',')
            try:
                lower, upper = map(
                    lambda a: int(a.strip()), values
                )
            except ValueError as e:
                raise NumberRangeException(e.message)

            if value[0] == '(':
                lower += 1

            if value[-1] == ')':
                upper -= 1

            return cls(lower, upper)

    def parse_range(self, value):
        if value is not None:
            values = value.split('-')
            if len(values) == 1:
                lower = upper = int(value.strip())
            else:
                try:
                    lower, upper = map(
                        lambda a: int(a.strip()), values
                    )
                except ValueError as e:
                    raise NumberRangeException(str(e))
            return lower, upper

    @property
    def normalized(self):
        return '[%s, %s]' % (self.lower, self.upper)

    def __eq__(self, other):
        try:
            return (
                self.lower == other.lower and
                self.upper == other.upper
            )
        except AttributeError:
            return NotImplemented

    def __repr__(self):
        return 'NumberRange(%r, %r)' % (self.lower, self.upper)

    def __str__(self):
        if self.lower != self.upper:
            return '%s - %s' % (self.lower, self.upper)
        return str(self.lower)

    def __add__(self, other):
        try:
            return NumberRange(
                self.lower + other.lower,
                self.upper + other.upper
            )
        except AttributeError:
            return NotImplemented

    def __sub__(self, other):
        try:
            return NumberRange(
                self.lower - other.lower,
                self.upper - other.upper
            )
        except AttributeError:
            return NotImplemented
