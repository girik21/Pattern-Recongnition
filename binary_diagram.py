# binary.py

from histogram import find_histogram
from two_dimension import imageTable

def find_variance(arr):
    size = len(arr)
    mean = sum(arr) / size
    variance = sum((x - mean) ** 2 for x in arr) / size
    return variance

def find_bimodal_threshold(hist):
    max_variance_gap = 0
    threshold = 0

    for p in range(1, len(hist) - 1):
        bg_variance = find_variance(hist[:p])
        fg_variance = find_variance(hist[p:])
        variance_gap = bg_variance + fg_variance  # Calculate the total variance gap

        if variance_gap > max_variance_gap:
            max_variance_gap = variance_gap
            threshold = p

    return threshold

def convert_to_binary(imageTable, threshold):
    rows = len(imageTable)
    cols = len(imageTable[0])

    for i in range(rows):
        for j in range(cols):
            if imageTable[i][j] < threshold:
                imageTable[i][j] = 0
            else:
                imageTable[i][j] = 1

if __name__ == "__main__":
    # Calculate the histogram for the imageTable
    hist = find_histogram(imageTable)

    # Find the threshold using the Bimodal Method
    threshold_bimodal = find_bimodal_threshold(hist)
    print("Threshold using Bimodal Method:", threshold_bimodal)

    # Convert the image to binary using the threshold
    convert_to_binary(imageTable, threshold_bimodal)

    # Print the binary image
    print("\nBinary Image:")
    for row in imageTable:
        print(" ".join(str(val) for val in row))
