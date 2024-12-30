import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

print("¡Todas las bibliotecas están instaladas y funcionando!")
import yfinance as yf

# Obtener datos de las acciones de Tesla
tesla = yf.Ticker("TSLA")

# Descargar el historial de precios
tesla_hist = tesla.history(period="max")

# Mostrar las primeras filas del historial de precios
print(tesla_hist.head())
