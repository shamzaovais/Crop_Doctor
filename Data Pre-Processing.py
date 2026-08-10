import cv2
import matplotlib.pyplot as plt
import numpy as np


def crimmins(data):
    new_image = data.copy()
    nrow = len(data)
    ncol = len(data[0])

    # Dark pixel adjustment

    # First Step
    # N-S
    for i in range(1, nrow):
        for j in range(ncol):
            if data[i - 1, j] >= (data[i, j] + 2):
                new_image[i, j] += 1
    data = new_image
    # E-W
    for i in range(nrow):
        for j in range(ncol - 1):
            if data[i, j + 1] >= (data[i, j] + 2):
                new_image[i, j] += 1
    data = new_image
    # NW-SE
    for i in range(1, nrow):
        for j in range(1, ncol):
            if data[i - 1, j - 1] >= (data[i, j] + 2):
                new_image[i, j] += 1
    data = new_image
    # NE-SW
    for i in range(1, nrow):
        for j in range(ncol - 1):
            if data[i - 1, j + 1] >= (data[i, j] + 2):
                new_image[i, j] += 1
    data = new_image
    # Second Step
    # N-S
    for i in range(1, nrow - 1):
        for j in range(ncol):
            if (data[i - 1, j] > data[i, j]) and (data[i, j] <= data[i + 1, j]):
                new_image[i, j] += 1
    data = new_image
    # E-W
    for i in range(nrow):
        for j in range(1, ncol - 1):
            if (data[i, j + 1] > data[i, j]) and (data[i, j] <= data[i, j - 1]):
                new_image[i, j] += 1
    data = new_image
    # NW-SE
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            if (data[i - 1, j - 1] > data[i, j]) and (data[i, j] <= data[i + 1, j + 1]):
                new_image[i, j] += 1
    data = new_image
    # NE-SW
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            if (data[i - 1, j + 1] > data[i, j]) and (data[i, j] <= data[i + 1, j - 1]):
                new_image[i, j] += 1
    data = new_image
    # Third Step
    # N-S
    for i in range(1, nrow - 1):
        for j in range(ncol):
            if (data[i + 1, j] > data[i, j]) and (data[i, j] <= data[i - 1, j]):
                new_image[i, j] += 1
    data = new_image
    # E-W
    for i in range(nrow):
        for j in range(1, ncol - 1):
            if (data[i, j - 1] > data[i, j]) and (data[i, j] <= data[i, j + 1]):
                new_image[i, j] += 1
    data = new_image
    # NW-SE
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            if (data[i + 1, j + 1] > data[i, j]) and (data[i, j] <= data[i - 1, j - 1]):
                new_image[i, j] += 1
    data = new_image
    # NE-SW
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            if (data[i + 1, j - 1] > data[i, j]) and (data[i, j] <= data[i - 1, j + 1]):
                new_image[i, j] += 1
    data = new_image
    # Fourth Step
    # N-S
    for i in range(nrow - 1):
        for j in range(ncol):
            if (data[i + 1, j] >= (data[i, j] + 2)):
                new_image[i, j] += 1
    data = new_image
    # E-W
    for i in range(nrow):
        for j in range(1, ncol):
            if (data[i, j - 1] >= (data[i, j] + 2)):
                new_image[i, j] += 1
    data = new_image
    # NW-SE
    for i in range(nrow - 1):
        for j in range(ncol - 1):
            if (data[i + 1, j + 1] >= (data[i, j] + 2)):
                new_image[i, j] += 1
    data = new_image
    # NE-SW
    for i in range(nrow - 1):
        for j in range(1, ncol):
            if (data[i + 1, j - 1] >= (data[i, j] + 2)):
                new_image[i, j] += 1
    data = new_image

    # Light pixel adjustment

    # First Step
    # N-S
    for i in range(1, nrow):
        for j in range(ncol):
            if (data[i - 1, j] <= (data[i, j] - 2)):
                new_image[i, j] -= 1
    data = new_image
    # E-W
    for i in range(nrow):
        for j in range(ncol - 1):
            if (data[i, j + 1] <= (data[i, j] - 2)):
                new_image[i, j] -= 1
    data = new_image
    # NW-SE
    for i in range(1, nrow):
        for j in range(1, ncol):
            if (data[i - 1, j - 1] <= (data[i, j] - 2)):
                new_image[i, j] -= 1
    data = new_image
    # NE-SW
    for i in range(1, nrow):
        for j in range(ncol - 1):
            if (data[i - 1, j + 1] <= (data[i, j] - 2)):
                new_image[i, j] -= 1
    data = new_image
    # Second Step
    # N-S
    for i in range(1, nrow - 1):
        for j in range(ncol):
            if (data[i - 1, j] < data[i, j]) and (data[i, j] >= data[i + 1, j]):
                new_image[i, j] -= 1
    data = new_image
    # E-W
    for i in range(nrow):
        for j in range(1, ncol - 1):
            if (data[i, j + 1] < data[i, j]) and (data[i, j] >= data[i, j - 1]):
                new_image[i, j] -= 1
    data = new_image
    # NW-SE
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            if (data[i - 1, j - 1] < data[i, j]) and (data[i, j] >= data[i + 1, j + 1]):
                new_image[i, j] -= 1
    data = new_image
    # NE-SW
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            if (data[i - 1, j + 1] < data[i, j]) and (data[i, j] >= data[i + 1, j - 1]):
                new_image[i, j] -= 1
    data = new_image
    # Third Step
    # N-S
    for i in range(1, nrow - 1):
        for j in range(ncol):
            if (data[i + 1, j] < data[i, j]) and (data[i, j] >= data[i - 1, j]):
                new_image[i, j] -= 1
    data = new_image
    # E-W
    for i in range(nrow):
        for j in range(1, ncol - 1):
            if (data[i, j - 1] < data[i, j]) and (data[i, j] >= data[i, j + 1]):
                new_image[i, j] -= 1
    data = new_image
    # NW-SE
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            if (data[i + 1, j + 1] < data[i, j]) and (data[i, j] >= data[i - 1, j - 1]):
                new_image[i, j] -= 1
    data = new_image
    # NE-SW
    for i in range(1, nrow - 1):
        for j in range(1, ncol - 1):
            if (data[i + 1, j - 1] < data[i, j]) and (data[i, j] >= data[i - 1, j + 1]):
                new_image[i, j] -= 1
    data = new_image
    # Fourth Step
    # N-S
    for i in range(nrow - 1):
        for j in range(ncol):
            if (data[i + 1, j] <= (data[i, j] - 2)):
                new_image[i, j] -= 1
    data = new_image
    # E-W
    for i in range(nrow):
        for j in range(1, ncol):
            if (data[i, j - 1] <= (data[i, j] - 2)):
                new_image[i, j] -= 1
    data = new_image
    # NW-SE
    for i in range(nrow - 1):
        for j in range(ncol - 1):
            if (data[i + 1, j + 1] <= (data[i, j] - 2)):
                new_image[i, j] -= 1
    data = new_image
    # NE-SW
    for i in range(nrow - 1):
        for j in range(1, ncol):
            if (data[i + 1, j - 1] <= (data[i, j] - 2)):
                new_image[i, j] -= 1
    data = new_image
    return new_image.copy()





# Laplacian Filter
image2 = cv2.imread('/home/ahmedhasan/PycharmProjects/Research/Global Wheat Detection/global-wheat-detection/train/0a9f24bdc.jpg',0)
new_image = cv2.Laplacian(image2,cv2.CV_8U)
image3 =image2 + new_image

# Frequency Filter
dft = cv2.dft(np.float32(image3),flags = cv2.DFT_COMPLEX_OUTPUT)
# shift the zero-frequncy component to the center of the spectrum
dft_shift = np.fft.fftshift(dft)

rows, cols = image3.shape
crow,ccol = rows//2 , cols//2
# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1
# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
# plot both images
# plt.figure(figsize=(11,6))
# plt.subplot(121),plt.imshow(image3, cmap = 'gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(img_back)
# plt.title('Low Pass Filter'), plt.xticks([]), plt.yticks([])
# plt.show()
# Contrast adjusting with gamma correction y = 1.2

gray_correct = np.array(255 * (img_back / 255) ** 1.2 , dtype='uint8')
thresh = cv2.adaptiveThreshold(gray_correct, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 255, 19)
thresh = cv2.bitwise_not(thresh)
# Dilatation et erosion
kernel = np.ones((15,15), np.uint8)
img_dilation = cv2.dilate(thresh, kernel, iterations=1)
img_erode = cv2.erode(img_dilation,kernel, iterations=1)
# clean all noise after dilatation and erosion
# img_erode = cv2.medianBlur(img_erode, 7)

plt.figure(figsize=(11,6))
plt.subplot(121),plt.imshow(thresh)
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_dilation)
plt.title('Low Pass Filter'), plt.xticks([]), plt.yticks([])
plt.show()


# new_image = crimmins(image2)
#
# plt.figure(figsize=(11,6))
# plt.subplot(121), plt.imshow(image2, cmap='gray'),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(new_image, cmap='gray'),plt.title('Crimmins Smoothing')
# plt.xticks([]), plt.yticks([])
# plt.show()



