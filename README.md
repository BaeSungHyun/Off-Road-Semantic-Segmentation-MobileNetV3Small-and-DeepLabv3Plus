# Off-Road-Semantic-Segmentation-MobileNetV3Small-and-DeepLabv3Plus
Using Yamaha-CMU Off-Road Dataset for semantic segmentation using MobileNetV3Small + DeepLabV3+

# Dependency
Executed environment : conda , Windows
1. Set your virtual environment on conda first, and activate it.
2. Use code : conda install --file packagelist.txt / pip install -r requirements.txt (Your choice! Or just install it manually)

# Dataset Preparation 
1. Download Yamaha-OffRoad-Dataset from : https://theairlab.org/yamaha-offroad-dataset/
2. Unzip the file and rename the folder to 'yamaha'
3. File Directory should look like this
   ![Screenshot of File Directory](https://github.com/BaeSungHyun/Off-Road-Semantic-Segmentation-MobileNetV3Small-and-DeepLabv3Plus/images/file_directory.png)
4. Run 'dataset_preprocess.py' in this repo in the same directory as the 'yamaha' folder, which will make new folder called 'annotations' and 'images' inside 'yamaha' folder
   ![Command for dataset preprocessing](https://github.com/BaeSungHyun/Off-Road-Semantic-Segmentation-MobileNetV3Small-and-DeepLabv3Plus/images/data_preprocess.png)
5. Done!

# Model
1. Open jupyter notebook in this repo
2. Run it!
3. Dataset annotation inside jupyter notebook
  ![Screenshot of Dataset Mask Annotations](https://github.com/BaeSungHyun/Off-Road-Semantic-Segmentation-MobileNetV3Small-and-DeepLabv3Plus/images/dataset_mask_annotations.png)
4. Check your result on any form of image data on forest, mountain.
  ![Check your result](https://github.com/BaeSungHyun/Off-Road-Semantic-Segmentation-MobileNetV3Small-and-DeepLabv3Plus/images/result_on_first_seen_data.png)


