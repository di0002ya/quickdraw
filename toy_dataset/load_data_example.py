"""
Author: Liu Chang

An example of using the data generated by generate_data.py
"""

import os.path as path
import pickle

data_path='/raid5/liuchang/quick_draw_output'

with open(path.join(data_path, 'train_X'), 'rb') as f:
    train_X = pickle.load(f)

with open(path.join(data_path, 'train_Y'), 'rb') as f:
    train_Y = pickle.load(f)

with open(path.join(data_path, 'test_X'), 'rb') as f:
    test_X = pickle.load(f)
with open(path.join(data_path, 'test_Y'), 'rb') as f:
    test_Y = pickle.load(f)

print(len(train_X))
