import numpy as np
from binary_image import binary_img

def groupMerge(groupCheck, label):
    if groupCheck[label] == label:
        return label
    groupCheck[label] = groupMerge(groupCheck, groupCheck[label])
    return groupCheck[label]

def total_group_merger(groupCheck):
    for i in range(len(groupCheck)):
        groupCheck[i] = groupMerge(groupCheck, i)

def connectivity_analysis(imageTable):
    rows = len(imageTable)
    cols = len(imageTable[0])
    dynamic_image = [[0 for _ in range(cols)] for _ in range(rows)]
    group_size = rows * cols
    label_size = 1
    group_check = [0] * group_size

    # Check the first row and the first column
    if imageTable[0][0] > 0:
        dynamic_image[0][0] = label_size
        group_check[label_size] = label_size
        label_size += 1

    for i in range(1, rows):
        if imageTable[i][0] > 0:
            if dynamic_image[i-1][0] > 0:
                dynamic_image[i][0] = dynamic_image[i-1][0]
            else:
                dynamic_image[i][0] = label_size
                group_check[label_size] = label_size
                label_size += 1

    for j in range(1, cols):
        if imageTable[0][j] > 0:
            if dynamic_image[0][j-1] > 0:
                dynamic_image[0][j] = dynamic_image[0][j-1]
            else:
                dynamic_image[0][j] = label_size
                group_check[label_size] = label_size
                label_size += 1

    for i in range(1, rows):
        for j in range(1, cols):
            if imageTable[i][j] > 0:
                if dynamic_image[i][j-1] > 0:
                    dynamic_image[i][j] = dynamic_image[i][j-1]
                elif dynamic_image[i-1][j] > 0:
                    dynamic_image[i][j] = dynamic_image[i-1][j]
                else:
                    dynamic_image[i][j] = label_size
                    group_check[label_size] = label_size
                    label_size += 1

    # Merge the same group
    for i in range(1, label_size):
        group_check[i] = groupMerge(group_check, i)

    # Merge the groups of the image
    for i in range(rows):
        for j in range(cols):
            if imageTable[i][j] > 0:
                imageTable[i][j] = group_check[dynamic_image[i][j]]

    total_group_merger(group_check)

    # Show groupCheck
    print("\nGROUP :   LABEL")
    for i in range(label_size):
        print(f"{i}     :      {group_check[i]}")

    return imageTable

# Convert binary_img to a NumPy array
imageTable = np.array(binary_img)

# Apply connectivity analysis
labeled_image = connectivity_analysis(imageTable)

# Display labeled image in the desired format
print('\n')
for row in labeled_image: 
    print(" ".join(map(str, row)))
