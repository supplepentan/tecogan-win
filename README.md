# TecoGAN for windows

## Introduction
This is Windows model of TecoGAN.   
original : https://github.com/thunil/TecoGAN

## Requirements
python 3.6.8  
CUDA 10.0 (for tensorflow-gpu) and 10.1 (for pytorch-gpu)

## Running the TecoGAN-win Model
```bash
# Install related modules.
python initial_setup.py

# Download our TecoGAN model, the _Vid4_ and _TOS_ scenes shown in our paper and video.
python runGan.py 0

# Run the inference mode on the calendar scene.
# You can take a look of the parameter explanations in the runGan.py, feel free to try other scenes!
python runGan.py 1 

# Evaluate the results with 4 metrics, PSNR, LPIPS[1], and our temporal metrics tOF and tLP with pytorch.
# Take a look at the paper for more details! 
python runGan.py 2
```

## Learning (Now Adjusting)
```bash
# Collecting date for learning
python dataPrepare.py --start_id 2000 --duration 120 --REMOVE --disk_path TrainingDataPath

# Train the TecoGAN model, based on our FRVSR model
# Please check and update the following parameters: 
# - VGGPath, it uses ./model/ by default. The VGG model is ca. 500MB
# - TrainingDataPath (see above)
# - in main.py you can also adjust the output directory of the  testWhileTrain() function if you like (it will write into a train/ sub directory by default)
python3 runGan.py 3
```

## Acknowledgements
This code is built on TecoGAN (https://github.com/thunil/TecoGAN),  thank for the authors for sharing their codes.