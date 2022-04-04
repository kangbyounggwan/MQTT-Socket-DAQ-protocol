import pandas as pd
import numpy as np
import joblib
import os

basedir = os.path.abspath(os.path.dirname(__file__))
MODEL_FILE_PATH = basedir + '/ModelFiles/'


def rrcf(t_sum_raw):
    path = MODEL_FILE_PATH + 'rrcf147.model'

    with open(path, "rb") as file:
        model = joblib.load(file)

    data = pd.DataFrame(t_sum_raw)
    rrcf_result = model.predict(data)
    rrcf_score = - model.score_samples(data)
    print(rrcf_score)
    print(rrcf_result)
    return rrcf_result, rrcf_score


def lof(t_sum_raw):
    data = np.array(t_sum_raw, dtype='complex_').astype(float)
    path = MODEL_FILE_PATH + 'lof2.model'
    print(data)
    with open(path, "rb") as file:
        model = joblib.load(file)


    lof_result = model.predict(data)
    lof_score = - model.score_samples(data)

    print(lof_result)
    print(lof_score)
    return lof_result, lof_score
