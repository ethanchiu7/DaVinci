# 2/(1+np.exp(-0.03305665294705416*50)) -1
# author zhaoxin
import numpy as np

def get_delta(x, y):
    return np.log((2/(1+y)) - 1) / x

def normalizationBySigmoid(delta, x):
    return 2/(1+np.exp(delta * x)) -1

delta = get_delta(5, 0.8)
print(delta)

y = normalizationBySigmoid(delta, 1)
print(y)