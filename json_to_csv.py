import os
import glob
import pandas as pd
import json
from pprint import pprint

def json_to_csv(path):
    print('in the function')
    print('path is ', path)
    json_list = []
    for json_file in glob.glob(path + '/*.json'):
        specs = json.load(open(json_file))
        for member in specs['objects']:
            value = (specs['filename'],
            int(specs['image_w_h'][0]),
            int(specs['image_w_h'][1]),
            member['label'],
            int(member['x_y_w_h'][0]),
            int(member['x_y_w_h'][1]),
            int(member['x_y_w_h'][2]),
            int(member['x_y_w_h'][3])
            )
            json_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    json_df = pd.DataFrame(json_list, columns=column_name)
    return json_df

def main():
    image_path = os.path.join('~/data/bike/tagged/training/', 'annotations')
    print(image_path)
    json_df = json_to_csv(image_path)
    json_df.to_csv('oncoming_labels.csv', index=None)
    print('Successfully converted json to csv.')


main()
