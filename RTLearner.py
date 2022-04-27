import numpy as np
from datetime import datetime
from random import randint
from scipy import stats


class RTLearner(object):
    """  		  	   		  	  			  		 			     			  	 
    This is a Random Decision Tree Learner. It is implemented correctly.
  		  	   		  	  			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  	  			  		 			     			  	 
        If verbose = False your code should not generate ANY output. When we test your code, verbose will be False.  		  	   		  	  			  		 			     			  	 
    :type verbose: bool  		  	   		  	  			  		 			     			  	 
    """

    def __init__(self, leaf_size=1, verbose=False):
        """
        Constructor method
        """
        self.leaf_size = leaf_size
        self.verbose = verbose
        pass  # move along, these aren't the drones you're looking for

    def author(self):
        """
        :return: The GT username of the student
        :rtype: str
        """
        return "pwang387"  # replace tb34 with your Georgia Tech username

    def build_tree(self, data):

        data_x = data[:, :data.shape[1] - 1]
        data_y = data[:, data.shape[1] - 1]

        if data.shape[0] == self.leaf_size and self.leaf_size == 1:
            return [-1, data_y[0], None, None]
        # implement additional leaf size logic
        if data.shape[0] <= self.leaf_size and self.leaf_size > 1:  # handles when leaf_size > 1
            return [-1, stats.mode(data_y)[0], None, None]

        if np.all(data_y == data_y[0]):  # might wanna double check this
            return [-1, data_y[0], None, None]

        else:
            # generate random
            i = randint(0, data.shape[1] - 2)

            splitVal = stats.mode(data_x[:, i], axis=0)[0]

            if splitVal == np.max(data[:, i]):  # handling the edge case and assign to median
                return [-1, stats.mode(data_y)[0], None, None]
            lefttree = np.array(self.build_tree(data[data[:, i] <= splitVal]))
            righttree = np.array(self.build_tree(data[data[:, i] > splitVal]))
            try:
                lefttree.shape[1]
                # how many rows are in the left tree? then start right tree, should be good
                root = [i, splitVal, 1, lefttree.shape[0] + 1]
            except IndexError:
                root = [i, splitVal, 1, 1 + 1]
            return np.vstack((root, lefttree, righttree))

    def add_evidence(self, data_x, data_y):
        """
        Add training data to learner

        :param data_x: A set of feature values used to train the learner
        :type data_x: numpy.ndarray
        :param data_y: The value we are attempting to predict given the X data
        :type data_y: numpy.ndarray
        """
        data = np.append(data_x, data_y[:, None], axis=1)
        self.model = self.build_tree(data)
        if self.verbose == True:
            print(self.model)
            print(f"RTLearner Runtime: {datetime.now() - start}")

    def apply_tree(self, test_x, i):
        i = int(i)

        if self.model[i][0] == -1:
            return self.model[i][1]
        # if test_x val at the tree coefficient is <= split val
        if test_x[int(self.model[i][0])] <= self.model[i][1]:

            # add the left tree pointer to i
            return self.apply_tree(test_x, i + 1)
        # if test_x val at the tree coefficient is > split val
        else:
            return self.apply_tree(test_x, i + int(self.model[i][3]))

    def query(self, test_x):
        """
        Estimate a set of test points given the model we built.

        :param points: A numpy array with each row corresponding to a specific query.
        :type points: numpy.ndarray
        :return: The predicted result of the input data according to the trained model
        :rtype: numpy.ndarray
        """
        pred_y = np.array([])
        for x in test_x:
            pred_y = np.append(pred_y, self.apply_tree(x, 0))
        return pred_y
