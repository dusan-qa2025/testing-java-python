import math
import pytest

class TestApp():

    @pytest.mark.test_group1
    def test_fabs(self):
        assert math.fabs(-6) == 6

    @pytest.mark.parametrize('num', [56, 44, -6])
    def test_isfinite(self, num):
        assert math.isfinite(num) == True

    def test_floor(self):
        assert math.floor(6.6) == 6
