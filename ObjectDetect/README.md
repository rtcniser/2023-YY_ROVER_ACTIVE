# Object Detection
Contains the trained object detection model.

We have used YOLOv8 to train our custom dataset to detect cylinders (and Joshna). The dataset is divided into two parts and was trained on top of an existing Cylinder detection model. Best trained model (`train2`, yes great name) found in `/runs/detect/train2/weights/best.pt`. 

Link to the [google drive folder](https://drive.google.com/drive/folders/1QK62UmdmoQXiLw41GFYswY1ovvqW0M30?usp=drive_link) that contains the machine learning dataset we used for training. The dataset is also hosted on [Roboflow](https://universe.roboflow.com/dataset-half-part/insighting).

![](runs/detect/train2/val_batch0_labels.jpg)

## Instructions for use

`cylinder.py` contains real-time object detection on webcam footage. Run the file after installing the `ultralytics` library. More instructions can be found [here](https://dipankarmedh1.medium.com/real-time-object-detection-with-yolo-and-webcam-enhancing-your-computer-vision-skills-861b97c78993) and the YOLOv8 documentation.

## What next?

- While the model can detect real cylinders with relative ease, it also detects quite a lot of false positives.
- More dataset can be included with different lighting conditions to improve the dataset.
- Object detection needs to be integrated with Jetson to create a depth map and eventually calculate the distance to the cylinder.