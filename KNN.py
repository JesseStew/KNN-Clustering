# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 17:22:29 2018
Jesse Stewart
CSC 535
HW2
"""

clear = "\n" * 100

from statistics import mode
import math
import csv

# Number of k-items to compare
num_k = 4

class Item(object):
    def __init__(self, contents = None, nearest_neighbors = None, weight_nn = None, classification = None):
        self.contents = contents
        self.nearest_neighbors = nearest_neighbors
        self.weight_nn = weight_nn
        self.classification = classification

# Takes list of lists and number
# returns list of Item objects
def itemize_data(data):
    item_list = []
    #create list of items
    for itr in range(1,len(data)):  #skip first tuple
        item = Item(data[itr])
        item_list.append(item)
    return item_list

# Assigns classification attribute 
# to list of Item objects
def assign_classification(itemized_data):
    for itr in itemized_data:
        itr.classification = itr.contents.pop(0)

# Find euclidean distance measure of two Item objects
# Input: two lists of numbers which are the same size.
# Returns: euclidean distance of two lists.
def euclidean_dist(train_item_data, test_item_data):
    #print("train_item_data[0]: ", train_item_data[0])
    squared_euclidean = []
    euclidean_dist = 0
    if len(train_item_data) != len(test_item_data):
        raise NameError("The len(train_item_data) != len(test_item)\nlen(train_item_data): ", len(train_item_data), "len(test_item): ", len(test_item_data))
    else:
        for num in range(0,len(train_item_data)):
            train_i = int(train_item_data[num])
            test_i = int(test_item_data[num])
            squared_euclidean.append((train_i-test_i)*(train_i-test_i))
        for num in squared_euclidean:
            euclidean_dist = euclidean_dist + num
        return math.sqrt(euclidean_dist)

# Assigns nearest neighbors to all items in test_data
# Input: list of training data items, list of test data items, and k
# No output: assign item.nearest_neighbors internally
def assign_nearest_neighbors(train_data, test_data, num_k):
    for num in range(len(test_data)):
        test_data[num].nearest_neighbors = []
        for itr in train_data:
            if len(test_data[num].nearest_neighbors) < num_k:
                test_data[num].nearest_neighbors.append(itr)
            else:
                for item in test_data[num].nearest_neighbors:
                    t = test_data[num].contents
                    d = itr.contents
                    u = item.contents
                    sim_t_u = euclidean_dist(t, u)
                    sim_t_d = euclidean_dist(t, d)
                    if sim_t_u <= sim_t_d:
                        test_data[num].nearest_neighbors.remove(item)
                        test_data[num].nearest_neighbors.append(itr)
def keywithmaxval(d):
     """ a) create a list of the dict's keys and values; 
         b) return the key with the max value"""  
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]

# ((1/d)*vote)(vote=number of objects in same class) 
# Assigns classification to all items in test_data
# Input: list of test data items
# No output: assign item.classification internally
def assign_class_by_nn(test_data):
    for item in test_data:
        #classification = []
        item.weight_nn = {}
        for itr in item.nearest_neighbors:
            euclid_dist = euclidean_dist(itr.contents, item.contents)
            #classification.append(itr.classification)
            if itr.classification in item.weight_nn.keys():
                item.weight_nn[itr.classification] = item.weight_nn[itr.classification] + (1/euclid_dist)
            else:
                item.weight_nn[itr.classification] = (1/euclid_dist)
        item.classification = keywithmaxval(item.weight_nn)
        
with open('MNIST_train.csv', newline='', encoding='utf_8') as f:
    reader = csv.reader(f)
    train_data = list(reader)
    
with open('MNIST_test.csv', newline='', encoding='utf_8') as f:
    reader = csv.reader(f)
    test_data = list(reader)

test_data = itemize_data(test_data)
assign_classification(test_data)
print("test_data[0].classification: ", test_data[0].classification)
print("test_data[1].classification: ", test_data[1].classification)
print("test_data[len(test_data)-1].classification: ", test_data[len(test_data)-1].classification)

train_data = itemize_data(train_data)
assign_classification(train_data)
print("\ntrain_data[0].classification: ", train_data[0].classification)
print("train_data[1].classification: ", train_data[1].classification)
print("train_data[len(train_data)-1].classification: ", train_data[len(train_data)-1].classification)

assign_nearest_neighbors(train_data, test_data, num_k)
assign_class_by_nn(test_data)

            