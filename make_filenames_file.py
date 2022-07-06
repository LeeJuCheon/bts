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

upper_directory_image = 'CAM_FRONT/'
upper_directory_depth = 'LIDAR_TOP/'
image_file_path = 'C:/Users/dogu/BTS/workspace/dataset/nuscene_depth_tcl/CAM_FRONT/'
depth_file_path = 'C:/Users/dogu/BTS/workspace/dataset/nuscene_depth_tcl/LIDAR_TOP/'
output_txt = './bts/train_test_inputs/nuscenes_train_files_with_gt.txt'

focal = 1252.8131


#image_file_list = os.walk(image_file_path)   # file path에 있는 파일들 list 불러오기
image_file_list = []
for (path, dir, files) in os.walk(image_file_path):
    for filename in files:
        path=path.replace('\\','/')
        path=path.split(upper_directory_image)[-1]
        image_file_list.append(path+filename)
    
#image_file_list.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

#depth_file_list = os.walk(depth_file_path)   # file path에 있는 파일들 list 불러오기
depth_file_list= []
for (path, dir, files) in os.walk(depth_file_path):
    for filename in files:
        path=path.replace('\\','/')
        path=path.split(upper_directory_depth)[-1]
        depth_file_list.append(path+filename)

#depth_file_list.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

print('Start!')

with open(output_txt, 'w') as f:
    for num in range(len(image_file_list)):
        f.write(image_file_list[num])
        f.write(' ')
        f.write(depth_file_list[num])
        f.write(' ')
        f.write(str(focal))
        f.write('\n')

print('Finished!')