import rvm_classification
import numpy as np

test_data = np.loadtxt("datasets/banana_test_data_1.asc")
test_taraget = np.loadtxt("datasets/banana_test_labels_1.asc")

train_data = np.loadtxt("datasets/banana_train_data_1.asc")
train_taraget = np.loadtxt("datasets/banana_train_labels_1.asc")


classification = rvm_classification.train(train_data, train_taraget)
