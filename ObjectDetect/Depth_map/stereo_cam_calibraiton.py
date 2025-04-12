import cv2
import numpy as np
import glob

# Define the dimensions of the chessboard pattern (number of inner corners)
chessboard_size = (9, 6)

# Prepare object points: (0,0,0), (1,0,0), (2,0,0) ...., (chessboard_width-1, chessboard_height-1,0)
# These represent the 3D coordinates of the chessboard corners in the object space.
objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
# Create a grid of (x, y) coordinates for each corner and assign them to the first two columns of objp.
objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

# Arrays to store object points and image points from all the calibration images.
objpoints = []  # 3D points in real world space, the same for all image pairs.
imgpoints_left = []  # 2D points in the image plane of the left camera.
imgpoints_right = []  # 2D points in the image plane of the right camera.

# Load the paths of the stereo calibration images using glob.
# It assumes your left camera images are named with the prefix 'left' and end with '.jpg'.
# Similarly, right camera images start with 'right' and end with '.jpg'.
left_images = glob.glob('left*.jpg')
right_images = glob.glob('right*.jpg')

# Check if any calibration images were found. If not, exit the script.
if not left_images or not right_images:
    print("Error: No left or right calibration images found!")
    exit()

# Loop through each pair of left and right calibration images.
for i in range(len(left_images)):
    # Load the left and right images using their file paths.
    img_left = cv2.imread(left_images[i])
    img_right = cv2.imread(right_images[i])

    # Convert the color images to grayscale, as chessboard corner detection works on grayscale images.
    gray_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
    gray_right = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)

    # Find the corners of the chessboard in both the left and right grayscale images.
    # 'chessboard_size' specifies the expected pattern dimensions.
    # 'None' is for an optional output array to store the corners.
    ret_left, corners_left = cv2.findChessboardCorners(gray_left, chessboard_size, None)
    ret_right, corners_right = cv2.findChessboardCorners(gray_right, chessboard_size, None)

    # If chessboard corners were successfully found in both images of the pair:
    if ret_left and ret_right:
        # Append the pre-defined object points to the list of object points.
        objpoints.append(objp)
        # Append the detected corner coordinates from the left image to the list of left image points.
        imgpoints_left.append(corners_left)
        # Append the detected corner coordinates from the right image to the list of right image points.
        imgpoints_right.append(corners_right)

        # Perform stereo camera calibration using all the collected object points and image points.
        # This function estimates the intrinsic parameters of each camera (mtx_left, dist_left, mtx_right, dist_right)
        # and the extrinsic parameters (R - rotation matrix, T - translation vector) that describe the relative pose
        ret, mtx_left, dist_left, mtx_right, dist_right, R, T, E, F = cv2.stereoCalibrate(
            objpoints, imgpoints_left, imgpoints_right, None, None, None, None, gray_left.shape[::-1]
        )
    else:
        # If corners were not found in one or both images of the pair, print a warning message.
        print(f"Warning: Chessboard corners not found for image pair {i}")

# After processing all image pairs, check if the stereo calibration was successful.
# The 'ret' value from 'cv2.stereoCalibrate' indicates the success of the calibration.
if ret < 0.5:  # A common threshold for successful calibration (lower error is better)
    print("Error: Stereo camera calibration failed!")
else:
    print("Stereo camera calibration successful!")
    # You would typically save the calibration parameters (mtx_left, dist_left, mtx_right, dist_right, R, T) here in a .npz file for further use
    # for use in subsequent stereo vision tasks like rectification and disparity map generation.