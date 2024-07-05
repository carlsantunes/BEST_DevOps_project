from digit_classification import normalize
import numpy as np

def test_add():
    input = np.array([255, 0])
    output = normalize(input)
    assert output[0] == 1
    assert output[1] == 0



