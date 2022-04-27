""""""  		  	   		  	  			  		 			     			  	 
"""  		  	   		  	  			  		 			     			  	 
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Copyright 2018, Georgia Institute of Technology (Georgia Tech)  		  	   		  	  			  		 			     			  	 
Atlanta, Georgia 30332  		  	   		  	  			  		 			     			  	 
All Rights Reserved  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Template code for CS 4646/7646  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Georgia Tech asserts copyright ownership of this template and all derivative  		  	   		  	  			  		 			     			  	 
works, including solutions to the projects assigned in this course. Students  		  	   		  	  			  		 			     			  	 
and other users of this template code are advised not to share it with others  		  	   		  	  			  		 			     			  	 
or to make it available on publicly viewable websites including repositories  		  	   		  	  			  		 			     			  	 
such as github and gitlab.  This copyright statement should not be removed  		  	   		  	  			  		 			     			  	 
or edited.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
We do grant permission to share solutions privately with non-students such  		  	   		  	  			  		 			     			  	 
as potential employers. However, sharing with other current or future  		  	   		  	  			  		 			     			  	 
students of CS 7646 is prohibited and subject to being investigated as a  		  	   		  	  			  		 			     			  	 
GT honor code violation.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
-----do not edit anything above this line---  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
Student Name: Tucker Balch (replace with your name)  		  	   		  	  			  		 			     			  	 
GT User ID: tb34 (replace with your User ID)  		  	   		  	  			  		 			     			  	 
GT ID: 900897987 (replace with your GT ID)  		  	   		  	  			  		 			     			  	 
"""  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
import datetime as dt
import BagLearner as bl
import RTLearner as rt
import indicators as ind
import pandas as pd
import util as ut  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
class StrategyLearner(object):  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    A strategy learner that can learn a trading policy using the same indicators used in ManualStrategy.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
    :param verbose: If “verbose” is True, your code can print out information for debugging.  		  	   		  	  			  		 			     			  	 
        If verbose = False your code should not generate ANY output.  		  	   		  	  			  		 			     			  	 
    :type verbose: bool  		  	   		  	  			  		 			     			  	 
    :param impact: The market impact of each transaction, defaults to 0.0  		  	   		  	  			  		 			     			  	 
    :type impact: float  		  	   		  	  			  		 			     			  	 
    :param commission: The commission amount charged, defaults to 0.0  		  	   		  	  			  		 			     			  	 
    :type commission: float  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    # constructor  		  	   		  	  			  		 			     			  	 
    def __init__(self, verbose=False, impact=0.0, commission=0.0):  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        Constructor method  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        self.verbose = verbose  		  	   		  	  			  		 			     			  	 
        self.impact = impact  		  	   		  	  			  		 			     			  	 
        self.commission = commission
        self.learner = None
        self.n = 10

    def author(self):
        return 'pwang387'
  		  	   		  	  			  		 			     			  	 
    # this method should create a RTLearner, and train it for trading
    def add_evidence(  		  	   		  	  			  		 			     			  	 
        self,  		  	   		  	  			  		 			     			  	 
        symbol="IBM",  		  	   		  	  			  		 			     			  	 
        sd=dt.datetime(2008, 1, 1),  		  	   		  	  			  		 			     			  	 
        ed=dt.datetime(2009, 1, 1),  		  	   		  	  			  		 			     			  	 
        sv=10000,  		  	   		  	  			  		 			     			  	 
    ):  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        Trains your strategy learner over a given time frame.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
        :param symbol: The stock symbol to train on  		  	   		  	  			  		 			     			  	 
        :type symbol: str  		  	   		  	  			  		 			     			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  	  			  		 			     			  	 
        :type sd: datetime  		  	   		  	  			  		 			     			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  	  			  		 			     			  	 
        :type ed: datetime  		  	   		  	  			  		 			     			  	 
        :param sv: The starting value of the portfolio  		  	   		  	  			  		 			     			  	 
        :type sv: int  		  	   		  	  			  		 			     			  	 
        """
  		  	   		  	  			  		 			     			  	 
        # get price
        syms = [symbol]  		  	   		  	  			  		 			     			  	 
        dates = pd.date_range(sd, ed)  		  	   		  	  			  		 			     			  	 
        prices_all = ut.get_data(syms, dates)  # automatically adds SPY  		  	   		  	  			  		 			     			  	 
        prices = prices_all[syms]  # only portfolio symbols
        if self.verbose:  		  	   		  	  			  		 			     			  	 
            print(prices)

        train_x, train_y = self.create_df(prices, symbol)
        self.learner = bl.BagLearner(learner=rt.RTLearner, bags=10, kwargs={"leaf_size":3},
                                     boost=False, verbose = False)
        self.learner.add_evidence(train_x, train_y)


  		  	   		  	  			  		 			     			  	 

  		  	   		  	  			  		 			     			  	 

    # assign y to train_x or test_x; the original price is based on
    # n is the lookback window.
    def assign_y(self, prices, symbol):
        # Long if the future price in 5 days is greater than the current price;

        df_y = pd.DataFrame(data=0, index=prices.index, columns=prices.columns)

        for i in range(prices.shape[0]-5):
            price_ratio = (prices.ix[i+5,symbol]-prices.ix[i,symbol])/prices.ix[i,symbol]
            if price_ratio > (0.02 + self.impact):
                df_y.ix[i,symbol] = 1
            elif price_ratio < (-0.02 - self.impact):
                df_y.ix[i,symbol] = -1

        return df_y

    # creates df for learner, returns training and test df
    def create_df(self, prices, symbol):
        # figure out where to ini n
        # split the data into train and test

        train_x = pd.DataFrame(data=0, index=prices.index, columns=['sma','mm','bb'])

        # create train df
        train_x['sma'] = ind.sma(prices, self.n)
        train_x['mm'] = ind.momentum(prices, self.n)
        train_x['bb'] = ind.bb(prices, self.n)
        train_y = self.assign_y(prices, symbol)

        return train_x, train_y



    # this method should use the existing policy and test it against new data
    def testPolicy(
        self,  		  	   		  	  			  		 			     			  	 
        symbol="IBM",  		  	   		  	  			  		 			     			  	 
        sd=dt.datetime(2009, 1, 1),  		  	   		  	  			  		 			     			  	 
        ed=dt.datetime(2010, 1, 1),  		  	   		  	  			  		 			     			  	 
        sv=10000,  		  	   		  	  			  		 			     			  	 
    ):  		  	   		  	  			  		 			     			  	 
        """  		  	   		  	  			  		 			     			  	 
        Tests your learner using data outside of the training data  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
        :param symbol: The stock symbol that you trained on on  		  	   		  	  			  		 			     			  	 
        :type symbol: str  		  	   		  	  			  		 			     			  	 
        :param sd: A datetime object that represents the start date, defaults to 1/1/2008  		  	   		  	  			  		 			     			  	 
        :type sd: datetime  		  	   		  	  			  		 			     			  	 
        :param ed: A datetime object that represents the end date, defaults to 1/1/2009  		  	   		  	  			  		 			     			  	 
        :type ed: datetime  		  	   		  	  			  		 			     			  	 
        :param sv: The starting value of the portfolio  		  	   		  	  			  		 			     			  	 
        :type sv: int  		  	   		  	  			  		 			     			  	 
        :return: A DataFrame with values representing trades for each day. Legal values are +1000.0 indicating  		  	   		  	  			  		 			     			  	 
            a BUY of 1000 shares, -1000.0 indicating a SELL of 1000 shares, and 0.0 indicating NOTHING.  		  	   		  	  			  		 			     			  	 
            Values of +2000 and -2000 for trades are also legal when switching from long to short or short to  		  	   		  	  			  		 			     			  	 
            long so long as net holdings are constrained to -1000, 0, and 1000.  		  	   		  	  			  		 			     			  	 
        :rtype: pandas.DataFrame  		  	   		  	  			  		 			     			  	 
        """
  		  	   		  	  			  		 			     			  	 
        # here we build a fake set of trades  		  	   		  	  			  		 			     			  	 
        # your code should return the same sort of data  		  	   		  	  			  		 			     			  	 
        dates = pd.date_range(sd, ed)  		  	   		  	  			  		 			     			  	 
        prices_all = ut.get_data([symbol], dates)  # automatically adds SPY  		  	   		  	  			  		 			     			  	 
        prices = prices_all[[symbol,]]  # only portfolio symbols
        trades_SPY = prices_all["SPY"]  # only SPY, for comparison later


        test_x = pd.DataFrame(data=0, index=prices.index, columns=['sma','mm','bb'])
        # create train df
        test_x['sma'] = ind.sma(prices, self.n)
        test_x['mm'] = ind.momentum(prices, self.n)
        test_x['bb'] = ind.bb(prices, self.n)
        test_y = self.learner.query(test_x.values)

        # the column name needs to be sym so marketsim can execute
        df_trades = pd.DataFrame(data=0, index=prices.index, columns=[symbol])

        tracker = 0
        # buy 1000 if long, sell 1000 if short
        for i in range(df_trades.shape[0]):
            if tracker == 0:
                if test_y[0][i] == 1:
                    df_trades.ix[i] = 1000
                    tracker = 1
                elif test_y[0][i] == -1:
                    df_trades.ix[i] = -1000
                    tracker = -1
            elif tracker == 1:
                if test_y[0][i] == -1:
                    df_trades.ix[i] = -2000
                    tracker = -1
            elif tracker == -1:
                if test_y[0][i] == 1:
                    df_trades.ix[i] = 2000
                    tracker = 1
        # holdings check
        # print(df_trades.sum())
        return df_trades


if __name__ == "__main__":
    print("One does not simply think up a strategy")  		  	   		  	  			  		 			     			  	 
