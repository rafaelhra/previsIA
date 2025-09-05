# plotter.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import config

def plot_results(original_data, train_predict, next_day_prediction):
    """Plota os resultados: histórico, previsões de treino e previsão futura."""
    
    # Criar um array para plotar as previsões de treino alinhadas com as datas corretas
    train_predict_plot = np.empty_like(original_data['Close'].values.reshape(-1, 1))
    train_predict_plot[:, :] = np.nan
    train_predict_plot[config.TIME_STEPS:len(train_predict) + config.TIME_STEPS, :] = train_predict

    # Plotando
    plt.figure(figsize=(16, 8))
    plt.title(f'Previsão de Preços para {config.TICKER}')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento (R$)')
    
    plt.plot(original_data.index, original_data['Close'], label='Histórico de Preços')
    plt.plot(original_data.index, train_predict_plot, label='Previsões de Treino', alpha=0.7)
    
    # Adicionando a previsão do dia seguinte
    last_date = original_data.index[-1]
    next_date = last_date + pd.DateOffset(days=1)
    plt.scatter(next_date, next_day_prediction, color='r', s=100, label=f'Previsão (D+1): R${next_day_prediction[0][0]:.2f}')

    plt.legend()
    plt.grid(True)
    plt.show()