import datetime as dt
import pandas as pd
import matplotlib.pyplot as plt
from util import get_data, plot_data

# author function
def author():
    return 'pwang387'

# SMA, n is n-day look back window
def sma(df_price, n = 0, plot = False):
    # returns sma dataframe
    v_sma = df_price.rolling(n).mean()
    # price/sma
    price_sma = (df_price/v_sma) - 1
    if plot:
        plt.plot(v_sma, label="SMA")
        plt.plot(df_price, label="Price")
        plt.title("SMA & Price")
        plt.xticks(rotation=45)
        plt.ylabel("Price")
        plt.legend()
        plt.savefig("SMA and Price", bbox_inches="tight")
        plt.close()
    if plot:
        plt.plot(price_sma, label="Price/SMA")
        plt.title("Price/SMA")
        plt.xticks(rotation=45)
        plt.savefig("Price_SMA", bbox_inches="tight")
        plt.close()

    return price_sma

# Momentum range: -0.5 + 0.5
def momentum(df_price, n = 0, plot = False):
    v_momentum = df_price/df_price.shift(n-1) - 1
    if plot:
        plt.plot(v_momentum, label="Momentum")
        plt.title("Momentum")
        plt.xticks(rotation=45)
        plt.savefig("Momentum", bbox_inches="tight")
        plt.close()
    if plot:
        plt.plot(df_price)
        plt.title("Price")
        plt.xticks(rotation=45)
        plt.ylabel("Dollar")
        plt.savefig("Price", bbox_inches="tight")
        plt.close()
    return v_momentum

# Bollinger Bands, returns both upper and lower band
def bb(df_price, n = 0, plot = False):
    v_sma = df_price.rolling(n).mean()
    v_std = (2 * df_price.rolling(n).std())
    upper_band = v_sma + v_std
    lower_band = v_sma - v_std
    v_bb = (df_price - v_sma)/v_std
    if plot:
        plt.plot(v_sma, label="SMA")
        plt.plot(df_price, label="Price")
        plt.plot(upper_band, label="Upper Band")
        plt.plot(lower_band, label="Lower Band")
        plt.title("Bollinger Bands")
        plt.xticks(rotation=45)
        plt.ylabel("Price")
        plt.legend()
        plt.savefig("Bolling Bands", bbox_inches="tight")
        plt.close()
    if plot:
        plt.plot(v_bb)
        plt.title("BBP")
        plt.xticks(rotation=45)
        plt.savefig("BBP", bbox_inches="tight")
        plt.close()
    return v_bb

# Percentage Price Indicator
def stochastic(df_price, plot = False):
    high_14 = df_price.rolling(14).max()
    low_14 = df_price.rolling(14).min()
    k = ((df_price - low_14)/(high_14-low_14)) * 100
    d = k.rolling(3).mean()

    if plot:
        ax = k.plot(label="%K")
        d.plot(label="%D")
        ax.set_ylabel('%')
        ax_2 = df_price.plot(label='Price',secondary_y=True)
        ax_2.set_ylabel('Price')
        plt.title("Stochastic Indicator")
        plt.xticks(rotation=45)
        ax.legend()
        ax_2.legend()
        plt.savefig("Stochastic", bbox_inches="tight")
        plt.close()
    return k

# CCI
def cci(df_price, n = 15, plot=False):
    v_md = df_price.rolling(n).apply(lambda x: pd.Series(x).mad())
    v_cci = (df_price - sma(df_price, n, False))/(0.015 * v_md)
    if plot:
        plt.plot(v_cci)
        plt.title("CCI")
        plt.xticks(rotation=45)
        plt.savefig("CCI", bbox_inches="tight")
        plt.close()
    return v_cci

def run():
    sd = dt.datetime(2008, 1, 1)
    ed = dt.datetime(2009, 12, 31)
    sym = "JPM"
    df_all_price = get_data([sym], pd.date_range(sd,ed))
    df = df_all_price[sym]

    # indicators
    v_sma = sma(df, 15, True)
    v_momentum = momentum(df,10,True)
    v_bbp = bb(df,15,True)
    v_k = stochastic(df, True)
    v_cci = cci(df,15,True)