# PrevisIA 📈

## Descrição

PrevisIA é um sistema de previsão de curto prazo para o preço de ações, utilizando um modelo de redes neurais recorrentes (LSTM) para analisar o histórico de preços e prever o valor de fechamento do dia seguinte. Este projeto foi desenvolvido para demonstrar a aplicação de técnicas de Deep Learning em séries temporais financeiras.

## Exemplo de Saída

![alt text](img\graph-image.png)

## Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Análise de Dados:** Pandas, NumPy
- **Coleta de Dados:** `yfinance`
- **Inteligência Artificial:** `TensorFlow` com `Keras`
- **Pré-processamento:** `Scikit-learn`
- **Visualização:** `Matplotlib`

## Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/PrevisIA.git](https://github.com/SEU_USUARIO/PrevisIA.git)
    cd PrevisIA
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute o script principal:**
    ```bash
    python main.py
    ```
    O script irá baixar os dados, treinar o modelo e exibir um gráfico com a previsão.

## Extensões Futuras

- [ ] Adicionar novas variáveis ao modelo, como volume de negociação.
- [ ] Implementar indicadores técnicos (Médias Móveis, RSI) como features.
- [ ] Criar uma interface web simples com Streamlit ou Flask para exibir a previsão.
