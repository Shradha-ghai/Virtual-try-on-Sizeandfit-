# Virtual-try-on-Sizeandfit(In Progress)
Our project consists of four major parts:

<br />1-Uploading image on webpage.(completed)
<br />Javascript and css code was implemented on Visual Studio and a webpage was created for uploading a photo from the user-end on the webpage to be further tested for virtual try on.

<br />2-Pose identification(completed)
<br />Deep Learning based Human Pose Estimation using OpenCV is now implemented on the photo uploaded by the user. This project uses a pre-trained Caffe model where two datasets have been trained named MPII and COCO which outputs:
<br />-> Confidence and Affinity maps for the keypoint-Left Shoulder.
<br />-> Affinity maps for Neck-Left shoulder pair
<br />After training the dataset the final results were predicted accordingly.


<br />3-Human Parsing(Working on improving the model)
<br />Initially  all the necessary packages needed for the project were imported which were run and verified.
<br />All the required python files are run on Spyder.
<br />The model file and the dataset including training validation and test data was then imported.
<br />After training the dataset the final results were predicted accordingly.

<br />4-Implementation of virtual try on using PyTorch
<br />Pytorch deep learning model for cloth warping is yet to be implemented which includes training of the human body clothes like pants,shorts, shirts etc.
