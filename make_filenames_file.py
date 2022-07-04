import os

"""
##### Input #######
upper_directory - Folder with collection of images and groundtruth depth images
image_file_path - Folder with sequence of images
depth_file_path - Folder with sequence of groundtruth depth images
output_txt - name of the txt file
카메라 focal length - 721.5377
##### Output ######
The txt file
It should be placed in /bts/train_test_inputs/
"""

upper_directory_image = ''
upper_directory_depth = ''
image_file_path = 'C:/Users/dogu/BTS/workspace/dataset/kitti_dataset_mini/data_depth_annotated/val/rgb/'
depth_file_path = 'C:/Users/dogu/BTS/workspace/dataset/kitti_dataset_mini/data_depth_annotated/val/depth/'
output_txt = 'eigen_test_files_mini_with_gt.txt'

focal = 721.5377


#image_file_list = os.walk(image_file_path)   # file path에 있는 파일들 list 불러오기
image_file_list = []
for (path, dir, files) in os.walk(image_file_path):
    for filename in files:
        path=path.replace('\\','/')
        path=path.split('data_depth_annotated/')[-1]
        image_file_list.append(path+'/'+filename)
    
#image_file_list.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

#depth_file_list = os.walk(depth_file_path)   # file path에 있는 파일들 list 불러오기
depth_file_list= []
for (path, dir, files) in os.walk(depth_file_path):
    for filename in files:
        path=path.replace('\\','/')
        path=path.split('data_depth_annotated/')[-1]
        depth_file_list.append(path+'/'+filename)

#depth_file_list.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

print('Start!')

with open(output_txt, 'w') as f:
    for num in range(len(image_file_list)):
        f.write(upper_directory_image+image_file_list[num])
        f.write(' ')
        f.write(upper_directory_depth+depth_file_list[num])
        f.write(' ')
        f.write(str(focal))
        f.write('\n')

print('Finished!')