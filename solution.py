import pandas as pd
import numpy as np


chat_id = 682673597 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    t=71
    for i in range(len(x)):
        x[i]*=(2/(t**2))
    return x.mean() # Ваш ответ
