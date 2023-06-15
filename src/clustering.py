import numpy as np


def get_centroids(data, ks):
    dct = {}
    for i in range(len(data)):
        if ks[i] not in dct.keys():
            dct[ks[i]] = [data[i]]
            continue
        dct[ks[i]].append(data[i])

    for k in dct:
        dct[k] = np.mean(dct[k], axis=0)
    return dct


def assign_k(data, k):
    n = len(data)
    rv = np.ndarray(n)

    for i in range(n):
        rv[i] = np.random.randint(k)

    return rv