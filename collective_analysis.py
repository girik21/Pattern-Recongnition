import numpy as np
from binary_image import binary_img
from scipy import ndimage

def connectivity_analysis(imageTable):
    # Convert the array to binary with only background and foreground (Step 4)
    binary_image = np.where(imageTable > 0, 1, 0)

    # Label the objects in the image (Step 5)
    labeled_image, num_objects = ndimage.label(binary_image, structure=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    # Show labeled image after group merge
    print('\n')
    print("After Group Merge:")
    for row in labeled_image:
        print(" ".join(map(str, row)))

    # Extract unique labels from the labeled image
    unique_labels = np.unique(labeled_image)
    
    # Create a dictionary to map group numbers to their labels
    group_labels = {}
    for group_num, label in enumerate(unique_labels):
        group_labels[group_num] = label

    # Show the mapping of group numbers to labels
    print("\nGROUP :   LABEL")
    for group_num, label in group_labels.items():
        print(f"{group_num}     :      {label}")

    return labeled_image

# Convert binary_img to a NumPy array
imageTable = np.array(binary_img)

# Show the original image
print('\n')
print("Before Group Merge:")
for row in imageTable:
    print(" ".join(map(str, row)))

# Apply connectivity analysis
labeled_image = connectivity_analysis(imageTable)