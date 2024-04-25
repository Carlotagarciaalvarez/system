import pandas as pd
import matplotlib.pyplot as plt

import ta

def plot_graphic():
    # Load DataFrame from CSV file
    df = pd.read_csv('ADA.csv')

    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Calculate Relative Strength Index (RSI)
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()

    # Plotting RSI
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['rsi'], label='RSI', color='blue')
    plt.axhline(70, linestyle='--', color='red', label='Overbought (70)')
    plt.axhline(30, linestyle='--', color='green', label='Oversold (30)')
    plt.title('Relative Strength Index (RSI) for Buy Signals')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.show()



