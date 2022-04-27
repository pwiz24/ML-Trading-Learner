import matplotlib.pyplot as plt
import StrategyLearner as sl
import marketsimcode as msc
import datetime as dt
import numpy as np

def author():
    return 'pwang387'

def normalize(df):
    df = df/df[0]
    return df

def get_values():
    sym = 'JPM'
    in_sd = dt.datetime(2008,1,1)
    in_ed = dt.datetime(2009, 12, 31)
    commission = 0

    # impact = 0
    learner = sl.StrategyLearner(verbose=False, impact=0, commission=commission)
    learner.add_evidence(symbol=sym, sd=in_sd, ed=in_ed,sv = 100000)
    df_trade_0 = learner.testPolicy(symbol=sym, sd=in_sd, ed=in_ed, sv=100000)
    df_val_0 = msc.compute_portvals(df_trades=df_trade_0, start_val=100000,
                                  commission=commission, impact=0)
    df_norm_val_0 = normalize(df_val_0)

    # impact = 0.005
    learner = sl.StrategyLearner(verbose=False, impact=0.005, commission=commission)
    learner.add_evidence(symbol=sym, sd=in_sd, ed=in_ed,sv = 100000)
    df_trade_0005 = learner.testPolicy(symbol=sym, sd=in_sd, ed=in_ed, sv=100000)
    df_val_0005 = msc.compute_portvals(df_trades=df_trade_0005, start_val=100000,
                                  commission=commission, impact=0.005)
    df_norm_val_0005 = normalize(df_val_0005)

    # impact = 0.01
    learner = sl.StrategyLearner(verbose=False, impact=0.01, commission=commission)
    learner.add_evidence(symbol=sym, sd=in_sd, ed=in_ed,sv = 100000)
    df_trade_001 = learner.testPolicy(symbol=sym, sd=in_sd, ed=in_ed, sv=100000)
    df_val_001 = msc.compute_portvals(df_trades=df_trade_001, start_val=100000,
                                  commission=commission, impact=0.01)
    df_norm_val_001 = normalize(df_val_001)

    # impact = 0.05
    learner = sl.StrategyLearner(verbose=False, impact=0.05, commission=commission)
    learner.add_evidence(symbol=sym, sd=in_sd, ed=in_ed,sv = 100000)
    df_trade_005 = learner.testPolicy(symbol=sym, sd=in_sd, ed=in_ed, sv=100000)
    df_val_005 = msc.compute_portvals(df_trades=df_trade_005, start_val=100000,
                                  commission=commission, impact=0.05)
    df_norm_val_005 = normalize(df_val_005)
    # normalized return
    plot_chart(df_norm_val_0, df_norm_val_0005, df_norm_val_001, df_norm_val_005, 'Normalized Return')

    # SR
    daily_returns = df_val_0.copy()
    daily_returns[1:] = (df_val_0[1:] / df_val_0[:-1].values) - 1
    daily_returns[0] = 0
    sr_0 = (daily_returns.mean()/daily_returns.std()) * (252**0.5)

    daily_returns = df_val_0005.copy()
    daily_returns[1:] = (daily_returns[1:] / daily_returns[:-1].values) - 1
    daily_returns[0] = 0
    sr_0005 = (daily_returns.mean()/daily_returns.std()) * (252**0.5)

    daily_returns = df_val_001.copy()
    daily_returns[1:] = (daily_returns[1:] / daily_returns[:-1].values) - 1
    daily_returns[0] = 0
    sr_001 = (daily_returns.mean()/daily_returns.std()) * (252**0.5)

    daily_returns = df_val_005.copy()
    daily_returns[1:] = (daily_returns[1:] / daily_returns[:-1].values) - 1
    daily_returns[0] = 0
    sr_005 = (daily_returns.mean()/daily_returns.std()) * (252**0.5)


    plot_bar(sr_0, sr_0005, sr_001, sr_005)




# pass the value of each portfolio
def plot_chart(df_0, df_0005, df_001, df_005, ylab):
    plt.plot(df_0, label = 'impact = 0')
    plt.plot(df_0005, label='impact = 0.005')
    plt.plot(df_001, label='impact = 0.01')
    plt.plot(df_005, label='impact = 0.05')
    plt.title('In-Sample Strategy Learner')
    plt.xticks(rotation=45)
    plt.ylabel(ylab)
    plt.legend()
    plt.savefig("experiment2_line", bbox_inches="tight")
    plt.close()

def plot_bar(sr_0, sr_0005, sr_001, sr_005):
    data = {'Impact = 0': sr_0, 'Impact = 0.005':sr_0005, 'Impact = 0.01':sr_001, 'Impact = 0.05':sr_005}
    impacts = list(data.keys())
    values = list(data.values())
    plt.bar(impacts, values, width=0.4)
    plt.title("In-Sample Strategy Learner SR")
    plt.ylabel('Sharpe Ratio')
    plt.savefig("experiment2_bar", bbox_inches="tight")
    plt.close()