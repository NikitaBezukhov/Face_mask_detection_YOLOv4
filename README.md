# __Face mask detection with DarkNet YOLOv4!__ 
## The dataset is __[Face Mask Detection from Kaggle](https://www.kaggle.com/andrewmvd/face-mask-detection)__.
## DarkNet is from __[AlexeyAB repo on GitHub](https://github.com/AlexeyAB/darknet)__.
## Was built in __[Google Colab](https://colab.research.google.com/)__ environment, so make any adjustments needed for it to work on your machine.
## You can find code and detailed project analysis in __[YOLOv4_face_mask.ipynb](https://github.com/NikitaBezukhov/Face_mask_detection_YOLOv4/blob/main/YOLOv4_face_mask.ipynb)__ notebook.
## The results of the training will be presented below.
### Dataset consists of 853 unique images of different sizes and aspect ratios of people with/without face mask and with mask worn incorrectly. (3 classes in total)
### Model trained for 10 hours on 1 Tesla P100 GPU.
### Resulting metrics are:
![chart (1)](https://user-images.githubusercontent.com/74721678/128638544-c200bf06-7fd4-4068-971d-c1594a85645a.png)
![Screenshot_1](https://user-images.githubusercontent.com/74721678/128638562-7471a0a3-deeb-4782-86ef-bc5e86424067.png)
![Screenshot_2](https://user-images.githubusercontent.com/74721678/128638566-fc1bcc8e-b5d9-4311-b1d1-16227ceadbd4.png)
![Screenshot_3](https://user-images.githubusercontent.com/74721678/128638750-3489cc36-6b11-4744-a71e-f07d353c10c6.png)
## In the end we were able to achieve 86.75 mAP50 which I consider a pretty good result since we only had 725 training images. The lowest AP was on "incorrect mask wearing" class - 77.53%, which is expected, since upon inspection its representation in the dataset was pretty low. With mask and without mask APs were 93.65% and 89.07% respectively which I think is really good for this small of a dataset. And for confidence thresholds of 0.25 and 0.50 average IoU was around 76-78%, which also is a good result.
## You can look at relusts of model's performance on video __[on YouTube.](https://www.youtube.com/watch?v=Iqq_cIUtZUU)__ 
![Screenshot_4](https://user-images.githubusercontent.com/74721678/128639008-4571b982-1eee-4749-b963-88b1c499b8bd.png)
