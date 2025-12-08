import xmltodict
import os
import pathlib

def get_parent_folder(path):
    return pathlib.Path(path).parent

def abs(x):
    if x < 0 :
        return -x
    return x

class_id = {'person': 0, 'fall': 1, 'falling': 2, '10+': 3, 'dog': 4}

def xmltotxt(label_folder):
    label_list = os.listdir(label_folder)
    for label_name in label_list:
        os.makedirs(os.path.join(get_parent_folder(label_folder), 'labels'), exist_ok=True)
        new_path = (os.path.join(get_parent_folder(label_folder), 'labels'))
        label_path = os.path.join(label_folder, label_name)
        with open(label_path, 'r', encoding='utf-8') as f:
            label_file = open(os.path.join(new_path, label_name.split('.')[0] + '.txt'), 'a', encoding='utf-8')
            file = f.read()
            f_dict = xmltodict.parse(file)
            print(f_dict)
            objects = f_dict['annotation']['object']
            size = f_dict['annotation']['size']
            print(size)
            img_width, img_height, img_channel = map(float, [size['width'], size['height'], size['depth']])
            if type(objects) == dict:
                objects = [objects]
            print(objects)
            for object in objects:
                print(object)
                obj_name = object['name']
                img_xmin = float(object['bndbox']['xmin'])
                img_xmax = float(object['bndbox']['xmax'])
                img_ymin = float(object['bndbox']['ymin'])
                img_ymax = float(object['bndbox']['ymax'])
                center_x = abs(img_xmax + img_xmin) / (2 * img_width)
                center_y = abs(img_ymax + img_ymin) / (2 * img_height)
                weight = abs(img_xmax - img_xmin) / img_width
                height = abs(img_ymax - img_ymin)/ img_height
                tar = [class_id[obj_name], center_x, center_y, weight, height]
                print(tar)
                label_file.write(' '.join(map(str, tar)))
                label_file.write('\n')


            #return
