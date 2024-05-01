import numpy as np
import cv2

def rgb_to_luv(image):
    # Convert image from RGB to LUV color space
    luv_image = np.zeros_like(image, dtype=np.float32)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Normalize RGB values to range [0, 1]
            r = image[i, j, 0] / 255.0
            g = image[i, j, 1] / 255.0
            b = image[i, j, 2] / 255.0
            
            # Convert RGB to XYZ
            # Using D65 illuminant and sRGB standard
            X = 0.412453 * r + 0.357580 * g + 0.180423 * b
            Y = 0.212671 * r + 0.715160 * g + 0.072169 * b
            Z = 0.019334 * r + 0.119193 * g + 0.950227 * b
            
            # Add epsilon to avoid division by zero
            epsilon = 0.000001
            X += epsilon
            Y += epsilon
            Z += epsilon
            
            # Convert XYZ to LUV
            ref_X = 0.950456
            ref_Y = 1.0
            ref_Z = 1.088754
            
            var_U = (4 * X) / (X + 15 * Y + 3 * Z)
            var_V = (9 * Y) / (X + 15 * Y + 3 * Z)
            
            ref_U = (4 * ref_X) / (ref_X + 15 * ref_Y + 3 * ref_Z)
            ref_V = (9 * ref_Y) / (ref_X + 15 * ref_Y + 3 * ref_Z)
            
            L = 116 * (Y / ref_Y) ** (1/3) - 16
            U = 13 * L * (var_U - ref_U)
            V = 13 * L * (var_V - ref_V)
            
            luv_image[i, j, 0] = L
            luv_image[i, j, 1] = U
            luv_image[i, j, 2] = V
            
    return luv_image.astype(np.uint8)

rgb_image = cv2.imread('D:/2.jpeg')  

luv_image = rgb_to_luv(rgb_image)


cv2.imshow('LUV Image', luv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
