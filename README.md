# Off-Road-Semantic-Segmentation-MobileNetV3Small-and-DeepLabv3Plus
Using Yamaha-CMU Off-Road Dataset for semantic segmentation using MobileNetV3Small + DeepLabV3+
\
Yamaha-CMU Off-Road Dataset을 사용하여 MobileNetV3Small + DeepLabV3+를 이용한 Semantic Segmentation 구현

# Dependency
Executed environment : conda , Windows
1.Set your virtual environment on conda first, and activate it.
\
2.Use code : conda install --file packagelist.txt / pip install -r requirements.txt (Your choice! Or just install it manually)
\
실행 환경: conda, Windows
1.먼저 conda에서 가상 환경을 설정하고 활성화하세요.
\
2.다음 코드를 사용하세요: conda install --file packagelist.txt / pip install -r requirements.txt (원하는 방법을 선택하거나 수동으로 설치할 수 있습니다.)

# Dataset Preparation 
1.Download Yamaha-OffRoad-Dataset from : https://theairlab.org/yamaha-offroad-dataset/
\
2.Unzip the file and rename the folder to 'yamaha'
\
3.File Directory should look like this
\
1.Yamaha-OffRoad-Dataset을 다음 링크에서 다운로드하세요: https://theairlab.org/yamaha-offroad-dataset/
\
2.파일의 압축을 풀고 폴더 이름을 'yamaha'로 변경하세요.
\
3.파일 디렉토리는 다음과 같이 되어야 합니다.

\

   
   ![Screenshot of File Directory](https://github.com/BaeSungHyun/Off-Road-Semantic-Segmentation-MobileNetV3Small-and-DeepLabv3Plus/blob/main/images/file_directory.png)

\
5.Run 'dataset_preprocess.py' in this repo in the same directory as the 'yamaha' folder, which will make new folder called 'annotations' and 'images' inside 'yamaha' folder
\
5.'yamaha' 폴더와 동일한 디렉토리에 있는 이 저장소의 'dataset_preprocess.py'를 실행하세요. 그러면 'yamaha' 폴더 안에 'annotations'와 'images'라는 새로운 폴더가 생성됩니다.
\
   ![Command for dataset preprocessing](https://github.com/BaeSungHyun/Off-Road-Semantic-Segmentation-MobileNetV3Small-and-DeepLabv3Plus/blob/main/images/data_preprocess.png)
6.Done!

\


# Model
1.Open jupyter notebook 'MobileNetv3Small_Deeplabv3Plus.ipynb' in this repo
\
2.Run it!
\
3.Dataset annotation inside jupyter notebook
\
1.이 저장소의 'MobileNetv3Small_Deeplabv3Plus.ipynb' 주피터 노트북을 엽니다.
\
2.실행하세요!
\
3.주피터 노트북 내에서 데이터셋 주석 작업을 진행합니다.

\


  ![Screenshot of Dataset Mask Annotations](https://github.com/BaeSungHyun/Off-Road-Semantic-Segmentation-MobileNetV3Small-and-DeepLabv3Plus/blob/main/images/dataset_mask_annotations.png)
  
4.Check your result on any form of image data on forest, mountain.
\
4.결과를 숲이나 산과 같은 이미지 데이터에서 확인하세요.
  ![Check your result](https://github.com/BaeSungHyun/Off-Road-Semantic-Segmentation-MobileNetV3Small-and-DeepLabv3Plus/blob/main/images/result_on_first_seen_data.png)


