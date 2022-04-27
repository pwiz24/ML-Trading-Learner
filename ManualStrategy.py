import indicators as ind
import datetime as dt
import pandas as pd
import util as ut

class ManualStrategy(object):
    # Constructor
    def __init__(self, verbose=False, impact=0.0, commission=0.0):
        self.verbose = verbose
        self.impact = impact
        self.commission = commission

    def author(self):
        return 'pwang387'

    # execute the trading logic and output df trades
    def tradingLogic(self, df, sym, sv):
        df_trades = df.copy()

        # create and reset the orders col to 0
        # logic for executing trades, can add cross functions later
        df_trades[sym] = 0

        df_trades[sym][(df_trades['sma'] > 0.05) & (df_trades['mo'] > 0)
                            & (df_trades['bb'] > 1)] = -1
        df_trades[sym][ (df_trades['sma'] < 0.05) & (df_trades['mo'] < 0)
                             & (df_trades['bb'] < -1)] = 1

        # copy pandas series
        df_orders = df_trades[sym].copy()

        tracker = 0
        # buy 1000 if long, sell 1000 if short
        for i in range(df_orders.shape[0]):
            if tracker == 0:
                if df_trades.ix[i,-1] == 1:
                    df_orders.ix[i] = 1000
                    tracker = 1
                elif df_trades.ix[i,-1] == -1:
                    df_orders.ix[i] = -1000
                    tracker = -1
            elif tracker == 1:
                if df_trades.ix[i,-1] == -1:
                    df_orders.ix[i] = -2000
                    tracker = -1
            elif tracker == -1:
                if df_trades.ix[i,-1] == 1:
                    df_orders.ix[i] = 2000
                    tracker = 1

        # convert to dataframe and rename the column to JPM
        df_orders = pd.DataFrame(df_orders)

        return df_orders


    def testPolicy(self, symbol = 'JPM', sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,12,31), sv = 100000):

        # example usage of the old backward compatible util function
        syms = [symbol]
        dates = pd.date_range(sd, ed)
        prices_all = ut.get_data(syms, dates)  # automatically adds SPY
        prices = prices_all[syms]  # only portfolio symbols

        # getting pricing indicators
        df_sma = ind.sma(prices, n=10,plot=False).rename(columns={symbol:'sma'})
        df_mo = ind.momentum(prices,n=10, plot=False).rename(columns={symbol:'mo'})
        df_bb = ind.bb(prices, n=10, plot=False).rename(columns={symbol:'bb'})
        # combining into a dataframe
        df_ind = df_sma.merge(df_mo, right_index=True, left_index=True).merge(df_bb, right_index=True, left_index=True)\
            .merge(prices, right_index=True, left_index=True)

        # execute trading logic
        df_trades = self.tradingLogic(df_ind, symbol ,sv)

        if self.verbose:
            print(f"df_trades:{df_trades}")

        # only df_trades is required from this trade
        return df_trades











