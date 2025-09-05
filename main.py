import numpy as np
import config
import data_scraping
import model_builder
import plotter

def main():
    """Função principal que orquestra a execução do projeto."""
    raw_data = data_scraping.download_data()
    X_train, y_train, scaler, close_prices, scaled_prices = data_scraping.preprocess_data(raw_data)

    model = model_builder.build_lstm_model(input_shape=(X_train.shape[1], 1))

    print("Treinando o modelo...")
    model.fit(X_train, y_train, epochs=25, batch_size=32, verbose=1)

    last_sequence = scaled_prices[-config.TIME_STEPS:]
    X_pred = np.reshape(last_sequence, (1, config.TIME_STEPS, 1))
    
    predicted_price_scaled = model.predict(X_pred)
    predicted_price = scaler.inverse_transform(predicted_price_scaled)
    
    print(f"Previsão do preço de fechamento para o próximo dia: {predicted_price[0][0]:.2f}")

    train_predictions_scaled = model.predict(X_train)
    train_predictions = scaler.inverse_transform(train_predictions_scaled)

    plotter.plot_results(raw_data, train_predictions, predicted_price)

if __name__ == "__main__":
    main()