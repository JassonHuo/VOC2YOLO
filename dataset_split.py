import os
from voc2yolo import get_parent_folder
from random import shuffle
import shutil
def split_data(img_folder, label_folder, train_rate=0.7):
    #创建文件格式
    new_data_folder = os.path.join(get_parent_folder(get_parent_folder(label_folder)), 'dataset')
    os.makedirs(new_data_folder, exist_ok=True)
    os.makedirs(os.path.join(new_data_folder, 'train'), exist_ok=True)
    train_imgs = os.path.join(new_data_folder, 'train', 'images')
    os.makedirs(train_imgs, exist_ok=True)
    train_labels = os.path.join(new_data_folder, 'train', 'labels')
    os.makedirs(train_labels, exist_ok=True)
    os.makedirs(os.path.join(new_data_folder, 'val'), exist_ok=True)
    val_imgs = os.path.join(new_data_folder, 'val', 'images')
    os.makedirs(val_imgs, exist_ok=True)
    val_labels = os.path.join(new_data_folder, 'val', 'labels')
    os.makedirs(val_labels, exist_ok=True)

    name_list = os.listdir(label_folder)
    print(name_list)
    train_size = int(len(name_list) * train_rate)
    test_size = len(name_list) - train_size
    shuffle(name_list)
    train_name_list = name_list[:train_size]
    test_name_list = name_list[test_size:]
    for label in train_name_list:
        label_path = os.path.join(label_folder, label)
        img_name = label.split('.')[0] + '.jpg'
        img_path = os.path.join(img_folder, img_name)
        shutil.copy(label_path, os.path.join(train_labels, label))
        shutil.copy(img_path, os.path.join(train_imgs, img_name))
    for label in test_name_list:
        label_path = os.path.join(label_folder, label)
        img_name = label.split('.')[0] + '.jpg'
        img_path = os.path.join(img_folder, img_name)
        shutil.copy(label_path, os.path.join(val_labels, label))
        shutil.copy(img_path, os.path.join(val_imgs, img_name))


split_data(r'D:\Python_study\fall_detection\mixed_fall\JPEGImages', r'D:\Python_study\fall_detection\mixed_fall\labels')
