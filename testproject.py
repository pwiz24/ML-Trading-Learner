import ManualStrategy as ms
import StrategyLearner as sl
import experiment1 as ex1
import experiment2 as ex2
import datetime as dt
import marketsimcode as msc
import matplotlib.pyplot as plt
import pandas as pd

def author():
    return 'pwang387'

def plot_manual_strategy_in(df_val, df_baseline_val, df_trades):
    plt.plot(df_val, label="Manual Strategy", color='red')
    plt.plot(df_baseline_val, label="Baseline", color='purple')
    # get vertical lines
    df_v = df_trades[(df_trades != 0) & (df_trades != 1) & (df_trades != -1)].dropna().copy()
    df_exit = df_v[df_v<0].dropna()
    df_enter = df_v[df_v>0].dropna()
    plt.vlines(df_exit.index, ymin=0.5,ymax=1.8, colors = 'black', label='Exit Point')
    plt.vlines(df_enter.index, ymin=0.5, ymax=1.8, colors = 'blue', label='Entry Point')
    plt.title("In-Sample Portfolio Val VS Baseline")
    plt.xticks(rotation=45)
    plt.ylabel("Normalized Return")
    plt.legend()
    plt.savefig("Manual Strategy In-Sample", bbox_inches="tight")
    plt.close()

def plot_manual_strategy_out(df_val, df_baseline_val, df_trades):
    plt.plot(df_val, label="Manual Strategy", color='red')
    plt.plot(df_baseline_val, label="Baseline", color='purple')
    # get vertical line
    df_v = df_trades[(df_trades != 0) & (df_trades != 1) & (df_trades != -1)].dropna().copy()
    df_exit = df_v[df_v<0].dropna()
    df_enter = df_v[df_v>0].dropna()
    plt.vlines(df_exit.index, ymin=0.5,ymax=1.8, colors = 'black', label='Exit Point')
    plt.vlines(df_enter.index, ymin=0.5, ymax=1.8, colors = 'blue', label='Entry Point')
    plt.title("Out of Sample Portfolio Val VS Baseline")
    plt.xticks(rotation=45)
    plt.ylabel("Normalized Return")
    plt.legend()
    plt.savefig("Manual Strategy Out-Of-Sample", bbox_inches="tight")
    plt.close()

def normalize(df):
    df = df/df[0]
    return df

# accepts normalized port val dfs
def get_metrics_tbl(df, sd, ed):
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values)-1
    daily_returns[0] = 0

    cum_ret = df[-1]/df[0] - 1
    avg_daily_ret = daily_returns.mean()
    std_daily_ret = daily_returns.std()

    data = [{'cum_ret':cum_ret, 'avg_daily_ret:':avg_daily_ret,'std_daily_ret':std_daily_ret}]
    df_metrics = pd.DataFrame(data)
    file_str = str(sd.date())+'_'+str(ed.date())+' metrics.csv'
    #print(df_metrics)
    # output to csv
    df_metrics.to_csv(file_str, index = False)

# create baseline trades df
# takes in df_trades and return baseline_val
def get_baseline(df_trades, syms, sv):
    df_baseline = df_trades.copy()
    df_baseline[syms] = 0
    df_baseline.ix[0] = 1000
    # creates baseline val from baseline trades
    df_baseline_val = msc.compute_portvals(df_trades=df_baseline, start_val=sv,
                                           commission=9.95, impact=0.005)
    return df_baseline_val

# runs manual in sample stuff
def run_man(df_trades, sym,commission, impact, sv, sd , ed):
    # implement marketsimcode
    df_val = msc.compute_portvals(df_trades=df_trades, start_val=sv,
                                  commission=commission, impact=impact)
    # Create baseline df
    df_baseline_val = get_baseline(df_trades, sym, sv=sv)

    # normalize both dfs before passing into the dataframe
    df_val = normalize(df_val)
    df_baseline_val = normalize(df_baseline_val)

    # get metrics
    get_metrics_tbl(df_val, sd, ed)

    return df_val, df_baseline_val

def run_test():
    sym = 'JPM'
    commission = 9.95
    impact = 0.0005
    sv = 100000

    # manual strategy in sample, two charts and a table
    in_sd = dt.datetime(2008,1,1)
    in_ed = dt.datetime(2009,12,31)
    ms_object = ms.ManualStrategy(verbose = False, impact=impact, commission=commission)
    df_trades = ms_object.testPolicy(symbol=sym, sd=in_sd, ed=in_ed, sv=sv)
    df_val_in, df_baseline_val_in = run_man(df_trades, sym, commission, impact, sv, in_sd, in_ed)
    plot_manual_strategy_in(df_val_in, df_baseline_val_in, df_trades)

    # manual strategy out of sample, two charts and a table
    out_sd = dt.datetime(2010,1,1)
    out_ed = dt.datetime(2011,12,31)
    df_trades_out = ms_object.testPolicy(symbol=sym, sd=out_sd, ed=out_ed, sv=sv)
    df_val_out, df_baseline_val_out = run_man(df_trades_out, sym, commission, impact, sv, out_sd, out_ed)
    plot_manual_strategy_out(df_val_out, df_baseline_val_out, df_trades_out)

    # learner in-sample
    learner = sl.StrategyLearner(verbose=False, impact=0.005, commission=9.95)
    learner.add_evidence(symbol=sym, sd=in_sd, ed=in_ed,sv = 100000)
    df_lt_in = learner.testPolicy(symbol=sym, sd=in_sd, ed=in_ed, sv=100000)
    # get port val and normalie
    df_lt_val_in = normalize(msc.compute_portvals(df_trades=df_lt_in, start_val=sv,
                                  commission=commission, impact=impact))

    # learner out-of-sample
    df_lt_out = learner.testPolicy(symbol=sym, sd=out_sd, ed=out_ed,sv = 100000)
    df_lt_val_out = normalize(msc.compute_portvals(df_trades=df_lt_out, start_val=sv,
                                  commission=commission, impact=impact))

    # experiment1
    ex1.plot_chart(df_lt_val_in, df_val_in, df_baseline_val_in, 'In-Sample')
    ex1.plot_chart(df_lt_val_out, df_val_out, df_baseline_val_out, 'Out-of-Sample')

    # experiment2
    ex2.get_values()

if __name__ == "__main__":
    run_test()