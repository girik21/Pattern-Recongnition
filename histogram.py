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

if __name__ == "__main__":
    histogram = find_histogram(imageTable)
    print("Gray-Level\t#-of-pixels")
    for i, freq in enumerate(histogram):
        if freq > 0:
            print(f"{i}\t\t{freq}")
