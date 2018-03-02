# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 17:22:29 2018
Jesse Stewart
CSC 535
HW2
"""

import csv

# Number of k-items to compare
num_k = 3

class Item(object):
    def __init__(self, contents = None, k = None, nearest_neighbors = None, classification = None):
        self.contents = contents
        self.k = k
        self.nearest_neighbors = nearest_neighbors
        self.classification = classification

# Takes list of lists and number assigned to k
# returns list of Item objects
def itemize_data(data, num_k):
    item_list = []
    #create list of items
    for itr in range(1,len(data)):  #skip first tuple
        item = Item(data[itr], num_k)
        item_list.append(item)
    return item_list

# Assigns classification attribute 
# to list of Item objects
def assign_classification(itemized_data):
    for itr in itemized_data:
        itr.classification = itr.contents[0]

with open('MNIST_train.csv', newline='', encoding='utf_8') as f:
    reader = csv.reader(f)
    train_data = list(reader)
    
with open('MNIST_test.csv', newline='', encoding='utf_8') as f:
    reader = csv.reader(f)
    test_data = list(reader)

test_data = itemize_data(test_data, num_k)
assign_classification(test_data)
print("test_data[0].classification: ", test_data[0].classification)
print("test_data[1].classification: ", test_data[1].classification)
print("test_data[len(test_data)-1].classification: ", test_data[len(test_data)-1].classification)
print("test_data[len(test_data)-1].k: ", test_data[len(test_data)-1].k)