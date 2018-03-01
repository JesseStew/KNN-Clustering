# DM_HW2 
Implement the KNN algorithm as given in the book on page 92. The only difference is that while the book uses simple unweighted voting, you will use weighted voting in your implementation. In simple unweighted voting, once the k nearest neighbors are found, their distances from the test sample do not matter. One neighbor is one vote. In weighted voting, the vote of a neighbor is inversely proportional to its distance to the test sample. You must use Python for your implementation. 
Use the given MNIST_train.cvs as your training data set and MNIST_test.csv as the test data set. There are 10 classes, with labels 0, 1, 2, …, 9, for this data set. The first attribute/column is the class label. Also notice that the first line/row in both data sets is a headers line. Do not modify the given data sets in any way because your code will be graded using them. In your code, you can just skip over the header lines. A description of the MNIST data is available at https://www.kaggle.com/c/digit-recognizer/data 
The output from your program will display the following:
•	value of K 
•	for each test sample, print both the desired class and the computed class, where desired class, is the class label as given in the data set, and computed class, is what your code produces as the output for the sample. 
•	the accuracy rate
•	number of misclassified test samples, and 
•	total number of test samples 

Remarks:
•	Use Euclidean distance measure to compute distances.
•	You may use a random sample of the training data to decide on the value of K to use for the algorithm.
•	Make sure to use the data sets from the course web site and not any other instance of MNIST
•	You need to use basic Python for implementation. You are not allowed to use IPython  (no pandas, numpy, or scikit-learn) 
