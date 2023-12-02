##ESRGAN (Enhances Super Resolution Generative Adversarial Networks)
This project aims to know the impact of number of Residual in Residual Dense Blocks (RRDB) and number of Growth Channels on the image upscalinng (x4). This project is based on "basicsr" repository.

#OUR WORK In this project which we trained 4 models:

21 blocks with 32 growth channels.
21 blocks with 36 growth channels.
23 blocks with 32 growth channels.
25 blocks with 32 growth channels.
#DATASETS These models were trained on SET 14 dataset with random flips and rotation and validated on SET 5 dataset. These models are trained upto 10000 iterations (epochs ~= 50) These models were evaluated on a custom dataset consisting of images from various datasts that include URBAN100, OST300 and BSD100. These models are evaluated for every 500 iterations and the results were plotted. Datasets used are available in "datasets" folder. Models are aalialble in "experiments" folder.

RESULTS
All the results for each iteration are located in the "results" folder.

#MISCELLANEOUS All the training and testing codes are available in "docs" folder README.md
