# Importing libraries
from neuralintents import GenericAssistant
import matplotlib.pyplot as plt
from numpy.lib.npyio import save
import pandas as pd
import pandas_datareader as web
import mplfinance as mpf

import pickle
import sys
import datetime as dt

with open('portfolio.pkl', 'rb') as f:
    portfolio = pickle.load(f)

def save_portfolio():
    with open('portfolio.pkl', 'wb') as f:
        pickle.dump(portfolio, f) 

def add_portfolio():
    ticker = input("Qual ação você deseja adicionar: ")
    amount = input("Quanto da ação você deseja adicionar: ")

    if ticker in portfolio.keys():
        portfolio[ticker] += int(amount)
    else:
        portfolio[ticker] = int(amount)

    save_portfolio()

def remove_portfolio():
    ticker = input("Qual ação você deseja vender: ")
    amount = input("Quanto da ação você deseja vender: ")

    if ticker in portfolio.keys():
        if amount <= portfolio[ticker]:
            portfolio[ticker] -= int(amount)
            save_portfolio()
        else:
            print("Você não tem nenhuma ação!")
    else:
        print(f"Você não possui nenhuma parte da {ticker}")

def show_portfolio():
    print("Seu portfólio:")
    for ticker in portfolio.keys():
        print(f"Você possui {portfolio[ticker]} partes da {ticker}")

def portfolio_worth():
    sum = 0
    for ticker in portfolio.keys():
        data = web.DataReader(ticker, 'yahoo')
        price = data['Close'].iloc[-1]
        sum += price
    print(f"Seu portfólio está valendo {sum} USD")

def portfolio_gains():
    starting_data = input("Insira a data para comparação (YYYY-MM-DD): ")

    sum_now = 0
    sum_then = 0

    try:
        for ticker in portfolio.keys():
            data = web.DataReader(ticker, 'yahoo')
            price_now = data['Close'].iloc[-1]
            price_then = data.loc[data.index == starting_data]['Close'].values[0]
            sum_now += price_now
            sum_then += price_then
        
        print(f"Ganhos relativos: {(sum_now-sum_then)/(sum_then) * 100}%")
        print(f"Ganhos absolutos: {sum_now-sum_then} USD")
    except IndexError:
        print("Não há negociação neste dia!")

def plot_chart():
    ticker = input("Escolha um símbolo da ação: ")
    starting_string = input("Escolha a data de início (DD-MM-YYYY): ")

    plt.style.use('dark_background')

    start = dt.datetime.strptime(starting_string, "%d/%m/%Y")
    end = dt.datetime.now()

    data = web.DataReader(ticker, 'yahoo', start, end)

    colors = mpf.make_marketcolors(up='#00ff00', down='#ff0000', wick='inherit', edge='inherit', volume='in')
    mpf_style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)
    mpf.plot(data, type='candle', style=mpf_style, volume=True)

def bye():
    print("Goodbye")
    sys.exit(0)

mappings = {
    'plot_chart': plot_chart,
    'add_portfolio': add_portfolio,
    'remove_portfolio': remove_portfolio,
    'show_portfolio': show_portfolio,
    'portfolio_worth': portfolio_worth,
    'portfolio_gains': portfolio_gains,
    'bye': bye
}

assistant = GenericAssistant('intents.json', mappings, "financial_assistant_model")

assistant.load_model()

while True:
    message = input()
    assistant.request(message)