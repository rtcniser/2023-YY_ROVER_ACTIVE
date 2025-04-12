import cv2
import numpy as np

# Load the calibration data
try:
    calibration_data = np.load('calibration_data.npz')
    mtx_left = calibration_data['cameraMatrixL']
    dist_left = calibration_data['distCoeffsL']
    mtx_right = calibration_data['cameraMatrixR']
    dist_right = calibration_data['distCoeffsR']
    R = calibration_data['R']
    T = calibration_data['T']
except FileNotFoundError:
    print("Error: calibration_data.npz not found. Please run stereo_calibration.py first.")
    exit()

# Load the stereo images
img_left = cv2.imread('left_image.jpg')
img_right = cv2.imread('right_image.jpg')

if img_left is None or img_right is None:
    print("Error: Could not load left_image.jpg or right_image.jpg")
    exit()

# Get image size (assuming left and right images have the same size)
height, width = img_left.shape[:2]

# Stereo rectification
rectify_scale = 1
rect_l, rect_r, proj_mat_l, proj_mat_r, Q, roi_l, roi_r = cv2.stereoRectify(
    mtx_left, dist_left, mtx_right, dist_right, (width, height), R, T, rectify_scale, (0, 0)
)

# Create the undistortion and rectification maps
left_maps = cv2.initUndistortRectifyMap(mtx_left, dist_left, rect_l, proj_mat_l, (width, height), cv2.CV_16SC2)
right_maps = cv2.initUndistortRectifyMap(mtx_right, dist_right, rect_r, proj_mat_r, (width, height), cv2.CV_16SC2)

# Rectify the images
img_rect_left = cv2.remap(img_left, left_maps[0], left_maps[1], cv2.INTER_LANCZOS4)
img_rect_right = cv2.remap(img_right, right_maps[0], right_maps[1], cv2.INTER_LANCZOS4)

# Convert to grayscale
gray_rect_left = cv2.cvtColor(img_rect_left, cv2.COLOR_BGR2GRAY)
gray_rect_right = cv2.cvtColor(img_rect_right, cv2.COLOR_BGR2GRAY)

# Create the stereo matcher (StereoSGBM example)
num_disparities = 16 * 5  # Adjust based on your scene
block_size = 11            # Adjust based on your needs
stereo = cv2.StereoSGBM_create(
    minDisparity=0,
    numDisparities=num_disparities,
    blockSize=block_size,
    P1=8 * 3 * block_size**2,
    P2=32 * 3 * block_size**2,
    disp12MaxDiff=1,
    uniquenessRatio=10,
    speckleWindowSize=100,
    speckleRange=32,
)

# Compute the disparity map
disparity = stereo.compute(gray_rect_left, gray_rect_right)

# Normalize the disparity map for visualization
normalized_disparity = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

# Display the disparity map
cv2.imshow('Rectified Left', img_rect_left)
cv2.imshow('Rectified Right', img_rect_right)
cv2.imshow('Disparity Map', normalized_disparity)
cv2.waitKey(0)
cv2.destroyAllWindows()