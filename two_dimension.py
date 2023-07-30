def read_image_to_array(file_path):
    # Initialize variables
    imageTable = []
    row = -1
    col = 0

    # Open the file to read
    with open(file_path, "r") as file:
        for line in file:
            numbers = line.strip().split()
            if row == -1:
                col = len(numbers)
            else:
                # Check if the number of columns matches for subsequent rows
                if len(numbers) != col:
                    raise ValueError("The number of columns in each row should be the same.")

            # Convert numbers to integers and add to the imageTable
            imageTable.append([int(num) for num in numbers])
            row += 1

    return imageTable, row + 1, col

file_path = "image/pattern2.txt"  
imageTable, rows, cols = read_image_to_array(file_path)


# Example: Print the 2D array and image dimensions
print("Image Array:")
for row in imageTable:
    print(row)
print("Image Dimensions (Rows x Cols):", rows, "x", cols)
