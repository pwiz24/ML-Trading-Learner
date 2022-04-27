import numpy as np
import RTLearner as rt
from random import choices
from scipy import stats

class BagLearner(object):

    def __init__(self, learner=rt.RTLearner, kwargs={}, bags=10, boost = False, verbose=False):
        """
        Constructor method
        """
        self.learner = learner
        self.bags = bags
        self.boost = False
        self.verbose = verbose
        self.kwargs = kwargs
        self.learner_list = []
        pass

    def author(self):
        """
        :return: The GT username of the student
        :rtype: str
        """
        return "pwang387"  # replace tb34 with your Georgia Tech username


    def add_evidence(self, data_x, data_y):
        """
        Add training data to learner

        :param data_x: A set of feature values used to train the learner
        :type data_x: numpy.ndarray
        :param data_y: The value we are attempting to predict given the X data
        :type data_y: numpy.ndarray
        """
        # both data_x and y have = rows
        rows = data_x.shape[0]
        data = np.append(data_x, data_y, axis=1)

        for i in range(self.bags):
            # shuffle test data, sub_x, sub_y are dataframes with size n and repeat elements
            sub_data = np.array(choices(data, k=rows))
            sub_x = sub_data[:,:-1]
            sub_y = sub_data[:,-1]
            learner = self.learner(**self.kwargs)
            learner.add_evidence(sub_x, sub_y)
            self.learner_list.append(learner)

        if self.verbose == True:
             print(self.learner_list)

    def query(self, test_x):
        """
        Estimate a set of test points given the model we built.

        :param points: A numpy array with each row corresponding to a specific query.
        :type points: numpy.ndarray
        :return: The predicted result of the input data according to the trained model
        :rtype: numpy.ndarray
        """

        results = []
        for i, c in enumerate(self.learner_list):
            results.append(c.query(test_x))
        results = np.array(results)
        return stats.mode(results, axis = 0)[0]
