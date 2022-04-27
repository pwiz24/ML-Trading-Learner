""""""  		  	   		  	  			  		 			     			  	 
"""MC2-P1: Market simulator.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
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
import os  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
import numpy as np  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
import pandas as pd  		  	   		  	  			  		 			     			  	 
from util import get_data, plot_data  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
def author():
    return 'pwang387'


def compute_portvals(
    df_trades,
    start_val=1000000,  		  	   		  	  			  		 			     			  	 
    commission=9.95,
    impact=0.005,
):  		  	   		  	  			  		 			     			  	 
    """  		  	   		  	  			  		 			     			  	 
    Computes the portfolio values.  		  	   		  	  			  		 			     			  	 
  		  	   		  	  			  		 			     			  	 
    :param orders_file: Path of the order file or the file object  		  	   		  	  			  		 			     			  	 
    :type orders_file: str or file object  		  	   		  	  			  		 			     			  	 
    :param start_val: The starting value of the portfolio  		  	   		  	  			  		 			     			  	 
    :type start_val: int  		  	   		  	  			  		 			     			  	 
    :param commission: The fixed amount in dollars charged for each transaction (both entry and exit)  		  	   		  	  			  		 			     			  	 
    :type commission: float  		  	   		  	  			  		 			     			  	 
    :param impact: The amount the price moves against the trader compared to the historical data at each transaction  		  	   		  	  			  		 			     			  	 
    :type impact: float  		  	   		  	  			  		 			     			  	 
    :return: the result (portvals) as a single-column dataframe, containing the value of the portfolio for each trading day in the first column from start_date to end_date, inclusive.  		  	   		  	  			  		 			     			  	 
    :rtype: pandas.DataFrame  		  	   		  	  			  		 			     			  	 
    """

    # step 1, prices df
    start_date = min(df_trades.index)
    end_date = max(df_trades.index)
    syms = df_trades.columns[0]
    df_prices = get_data([syms], pd.date_range(start_date, end_date))
    df_prices = df_prices[syms]  # remove SPY
    df_prices['Cash'] = 1.00

    # Create cash column for df_trades to calculate holdings
    df_trades = df_trades.copy()
    df_trades['Cash'] = 0

    # step 2, trades df
    # Calculate impact n commission
    for day in df_trades.index:
        if df_trades.ix[day][0] > 0:
            df_trades.ix[day, 'Cash'] += -(df_prices.ix[day] * impact * df_trades.ix[day][0])
            df_trades.ix[day, 'Cash'] += -commission
        elif df_trades.ix[day][0] < 0:
            df_trades.ix[day, 'Cash'] += (df_prices.ix[day] * impact * df_trades.ix[day][0])
            df_trades.ix[day, 'Cash'] += -commission

    # add price and
    # impact/commission together
    df_trades['Cash'] = df_trades['Cash'] + (df_prices*-df_trades[syms])

    # step 3, holdings
    df_holdings = df_trades.copy()
    df_holdings.iloc[0, -1] += start_val
    df_holdings = df_holdings.cumsum()

    # step 4, calculate port values
    df_holdings[syms] = df_prices * df_holdings[syms]
    df_portvals = df_holdings.sum(axis = 1)

    return df_portvals
  		  	   		  	  			  		 			     			  	 

