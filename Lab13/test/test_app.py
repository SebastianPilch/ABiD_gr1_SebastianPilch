from myapp import app
import pytest


testdata = ([4,5,10,8,'a','b',1], [1,4,None,3,2],[2.1,3.1,1,5,4],'int_lst')

@pytest.mark.parametrize('sample', testdata)

def test_sort_swap(sample):
    if sample == 'int_list':
        got = app.sort_swap([2,6,12,9,3,7,11,4,5,10,8,1])
        want = [1,2,3,4,5,6,7,8,9,10,11,12]
        assert got == want
    assert app.sort_swap(sample) is None







