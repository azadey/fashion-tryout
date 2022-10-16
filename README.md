# Fashion Tryout
This was a research project to implement a virtual try-on system.
When a user provides a image them selve a virtual image of user wearing different clothes is synthesized using deep learning models.
This was inspired by first order motion model by AliaksandrSiarohin [first-order-motion-model](https://github.com/AliaksandrSiarohin/first-order-model)
The deep learning training was done on google colab environment. The training data used was from open sourced Large-scale Fashion (DeepFashion) Database [dataset](https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html)

### Steps to Run the code.
- It is important that the runtime setting is set as GPU. The we install the packages.
- The fashion dataset provided consists of two text files (fashion_train.txt and fashion_test.txt);
these two files are downloaded for data preparation.
- The following code is executed to train the data.
`!CUDA_VISIBLE_DEVICES=0,1,2,3 python run.py --config config/fashion-256.yml --device_ids 0,1,2,3`
- The driving videos used for this implementation can be downloaded from the following link:
https://drive.google.com/drive/folders/1JM8ZjI7YO8WXGpUi5XAzqrvrWN9Z2KSo?usp=s
haring.
- The source files used for the implementation can be downloaded from the following link:
https://drive.google.com/drive/folders/1Wu-
3q8XvAb8QD4yqeCUmTDXf1HQ3lUvB?usp=sharing
- Trained checkpoint data (fashion.pth.tar) can be downloaded from the following link:
https://drive.google.com/file/d/1W7qunHxacXC8tdkHjMyLF43nTbIf8HwX/view?usp=shari
ng.


### Results 1

https://user-images.githubusercontent.com/1397092/196004516-5748ae90-8f80-40ef-8b3a-76462822cd1b.mp4

### Results 2

https://user-images.githubusercontent.com/1397092/196004544-d6826392-d49d-4fc9-83f0-3c926181a3cf.mp4

### Results 3

https://user-images.githubusercontent.com/1397092/196004555-f847d1d6-8a67-4417-acb8-80ae17a103e5.mp4

### Results 4

https://user-images.githubusercontent.com/1397092/196004559-d018b975-ce36-451c-a057-2720d5c6c1cc.mp4

### Results 5

https://user-images.githubusercontent.com/1397092/196004568-1da81f78-553e-462a-bb8d-73a2522536d9.mp4

