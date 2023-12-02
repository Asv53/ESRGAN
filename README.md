# ESRGAN
We used ESRGAN (Enhances Super Resolution Generative Adversarial Networks) to increase the resolution of the Image.
This project aims to know the impact of number of Residual in Residual Dense Blocks (RRDB) and number of Growth Channels on the image upscalinng (x4).
This project is based on "basicsr" repository.
In this project which we trained 4 models 
1. 21 blocks with 32 growth channels
2. 21 blocks with 36 growth channels
3. 23 blocks with 32 growth channels
4. 25 blocks with 32 growth channels
These models were trained on SET 14 dataset with random flips and rotation and validated on SET 5 dataset.
These models are trained upto 10000 iterations (epochs ~= 50)
These models were evaluated on a custom dataset consisting of images from various datasts that include URBAN100, OST300 and BSD100.
These models are evaluated for every 500 iterations and the results were plotted.
