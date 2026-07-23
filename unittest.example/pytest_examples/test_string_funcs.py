import pytest

class TestStringFuncs():

    @pytest.mark.test_group1
    def test_upper(self):
        assert 'foo'.upper() == 'FOO'

    def test_isupper(self):
        assert 'FOO'.isupper() == True

    