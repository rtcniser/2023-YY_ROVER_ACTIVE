# Object Detection
Contains the trained object detection model.

We have used YOLOv8 to train our custom dataset to detect cylinders (and Joshna). The dataset is divided into two parts and was trained on top of an existing Cylinder detection model. Best trained model (`train2`, yes great name) found in `/runs/detect/train2/weights/best.pt`

Link to the [google drive folder](https://drive.google.com/drive/folders/1QK62UmdmoQXiLw41GFYswY1ovvqW0M30?usp=drive_link) that contains the machine learning dataset we used for training. The dataset is also hosted on [Roboflow](https://universe.roboflow.com/dataset-half-part/insighting).

![](/runs/detect/train2/val_batch0_labels.jpg)

(to be updated)