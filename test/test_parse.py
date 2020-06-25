from scripta import parse
from unittest import TestCase


class ParseTest(TestCase):
    def test_parse(self):
        actual = vars(parse.parse(['foo']))
        expected = {
            'columns': None,
            'errors': None,
            'keys': None,
            'output': None,
            'prompt': None,
            'rows': None,
            'scripts': ['foo'],
            'svg': '',
            'theme': None,
            'times': None,
            'upload': False,
            'verbose': False,
        }
        assert actual == expected
