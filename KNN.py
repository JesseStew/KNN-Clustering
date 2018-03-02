# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 17:22:29 2018
Jesse Stewart
CSC 535
HW2
"""

import csv

with open('MNIST_train.csv', newline='', encoding='utf_8') as f:
    reader = csv.reader(f)
    train_data = list(reader)
    
with open('MNIST_test.csv', newline='', encoding='utf_8') as f:
    reader = csv.reader(f)
    test_data = list(reader)

