from digit_classification import normalize
import numpy as np

def test_add():
    input = np.array([255, 0])
    output = normalize(input)
    assert output[1] == 1
    assert output[2] == 0



