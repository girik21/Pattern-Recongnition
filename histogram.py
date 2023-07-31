import numpy as np
from two_dimension import imageTable

def find_histogram(imageTable):
    RANGE = 256
    hist = [0] * RANGE

    range_val = imageTable[0][0]
    for i in range(RANGE):
        hist[i] = 0

    rows = len(imageTable)
    cols = len(imageTable[0])
    for i in range(rows):
        for j in range(cols):
            value = imageTable[i][j]
            hist[value] += 1
            if value > range_val:
                range_val = value

    range_val += 1

    return hist

def otsu(image):
    hist = find_histogram(image)
    nhist = np.array(hist) / np.sum(hist)
    vmax = 0
    tmax = 1

    for t in range(1, len(nhist)):
        q1 = np.sum(nhist[0: t])
        q2 = 1 - q1

        j = 0
        u1 = 0
        for j in range(t - 1):
            u1 = u1 + j * nhist[j]
        if q1 > 0:
            u1 = u1 / q1

        j = t + 1
        u2 = 0
        for j in range(t, 255):
            u2 = u2 + j * nhist[j]
        if q2 > 0:
            u2 = u2 / q2

        vb = q1 * q2 * (u1 - u2) ** 2

        if vb > vmax:
            vmax = vb
            tmax = t

    return tmax

if __name__ == "__main__":
    histogram = find_histogram(imageTable)
    print("Gray-Level\t#-of-pixels")
    for i, freq in enumerate(histogram):
        if freq > 0:
            print(f"{i}\t\t{freq}")

    threshold = otsu(imageTable)
    print("Threshold using Otsu's Method:", threshold)
