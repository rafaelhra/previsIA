import numpy as np
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler
import config

def download_data():
    """Baixa os dados do ativo usando as configurações do config.py"""
    print(f"Baixando dados para {config.TICKER}...")
    data = yf.download(config.TICKER, start=config.START_DATE, end=config.END_DATE)
    return data

def preprocess_data(data):
    """Realiza o pré-processamento dos dados para o modelo LSTM."""
    close_prices = data['Close'].values.reshape(-1, 1)

    # Normalização
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_prices = scaler.fit_transform(close_prices)

    # Criação das sequências
    X = []
    y = []
    for i in range(config.TIME_STEPS, len(scaled_prices)):
        X.append(scaled_prices[i-config.TIME_STEPS:i, 0])
        y.append(scaled_prices[i, 0])

    X, y = np.array(X), np.array(y)
    
    # Reshape para o formato da LSTM
    X = np.reshape(X, (X.shape[0], X.shape[1], 1))

    return X, y, scaler, close_prices, scaled_prices