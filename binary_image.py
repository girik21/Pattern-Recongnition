import numpy as np
import matplotlib.pyplot as plt
from two_dimension import imageTable

# Convert imageTable to a NumPy array
img = np.array(imageTable)

plt.figure()
plt.imshow(img, 'gray')
plt.title('Grey-scale Map')

# Calculate histogram
bins = np.arange(256)
hist, _ = np.histogram(img, np.hstack((bins, np.array([256]))))
plt.figure(2)
plt.bar(bins, hist)
plt.title('Histogram')

# Otsu's method to find an optimal threshold
total_pixels = img.size
pixel_probabilities = hist / total_pixels
max_variance = 0          
optimal_threshold = 0

for T in range(255):
    omega_t = np.sum(pixel_probabilities[0:T+1])
    mu_t = 0
    mu2 = 0

    for i in range(T+1):
        mu_t = mu_t + i * pixel_probabilities[i]

    if omega_t != 0:
        mu_t = mu_t / omega_t

    for i in range(T+1, 256):
        mu2 = mu2 + i * pixel_probabilities[i]

    if (1 - omega_t) != 0:
        mu2 = mu2 / (1 - omega_t)

    variance_between_classes = omega_t * (1 - omega_t) * (mu_t - mu2)**2

    if max_variance < variance_between_classes:
        max_variance = variance_between_classes
        optimal_threshold = T

print("Optimum Threshold:", optimal_threshold)

# Convert to binary using the Otsu's threshold
binary_img = np.zeros_like(img, dtype=np.uint8)
binary_img[img > optimal_threshold] = 1

# Display binary image in the desired format
for row in binary_img:
    print(" ".join(map(str, row)))

# Show image
plt.figure()
plt.imshow(binary_img, 'gray')
plt.title('Binary Image')
plt.show()
