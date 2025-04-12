# Object Detection
Contains the trained object detection model. Good start for an introduction to [Machine Learning](https://mrce.in/ebooks/Machine%20Learning%20for%20Absolute%20Beginners.pdf).

We have used YOLOv11 to train our custom dataset to detect cylinders (and Joshna). The dataset is divided into three parts (train, valid, test) and was trained on top of an existing Cylinder detection model. Best trained model (`train2`, yes great name) found in `/runs/detect/train2/weights/best.pt`. 

Link to the [google drive folder](https://drive.google.com/drive/folders/1QK62UmdmoQXiLw41GFYswY1ovvqW0M30?usp=drive_link) that contains the machine learning dataset we used for training. The dataset is also hosted on [Roboflow](https://universe.roboflow.com/dataset-half-part/insighting).

![](runs/detect/train2/val_batch0_labels.jpg)
## Instructions for prepping the dataset using roboflow 

- Normalise images (crop to 640x640 using bulk cropper).
- Upload the images on Roboflow to get them segregated into train, test and validate.
- Annotate (mark and label cylinders) the images
- Upload the images to the dataset.
- Downloaded the dataset in the YOLOv8 format

More intstructions can be found [here](https://blog.roboflow.com/getting-started-with-roboflow/).

## Instructions for training the model 

`cylinder.py` contains real-time object detection on webcam footage. Run the file after installing the `ultralytics` library. More instructions can be found [here](https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993) and the YOLOv8 documentation.

## What next?

- While the model can detect real cylinders with relative ease, it also detects quite a lot of false positives.
- More dataset can be included with different lighting conditions to improve the dataset.
- Object detection needs to be integrated with Jetson to create a depth map and eventually calculate the distance to the cylinder.
