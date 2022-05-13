from pandas import DataFrame
import yfinance as yf

def ticker_info(ticker) -> dict:
    return yf.Ticker(ticker).info

def ticker_financials(ticker) -> dict:
   return yf.Ticker(ticker).financials

def ticker_analysis(ticker) -> dict:
    return yf.Ticker(ticker).analysis   
