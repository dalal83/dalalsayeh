import yfinance as yf

# Mensaje para confirmar que las bibliotecas están instaladas
print("¡Todas las bibliotecas están instaladas y funcionando!")

# Obtener los datos de las acciones de Tesla
tesla = yf.Ticker("TSLA")  # El símbolo de Tesla es "TSLA"

# Descargar el historial de precios
tesla_hist = tesla.history(period="max")  # period="max" obtiene todo el historial de precios

# Mostrar las primeras filas del historial de precios
print(tesla_hist.head())
# Obtener los datos de GameStop
gamestop = yf.Ticker("GME")  # El símbolo de GameStop es "GME"

# Descargar el historial de precios
gamestop_hist = gamestop.history(period="max")  # period="max" obtiene todos los datos históricos

# Mostrar las primeras filas del historial
print(gamestop_hist.head())
import requests  # Asegúrate de importar esta biblioteca
from bs4 import BeautifulSoup  # También necesaria para el web scraping

# URL de ejemplo para obtener datos de ingresos (ajusta esta URL según lo que necesites)
url = "https://example.com/tesla-income-data"

# Hacer una solicitud HTTP a la página
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    print("Solicitud exitosa!")
    soup = BeautifulSoup(response.content, 'html.parser')
    # Aquí puedes extraer los datos específicos que necesitas
    print(soup.prettify())  # Muestra el contenido HTML para inspeccionar
else:
    print(f"Error en la solicitud: {response.status_code}")
import matplotlib.pyplot as plt

# Leer datos de Tesla
tesla_stock = pd.read_csv("tesla_stock_data.csv")
tesla_revenue = pd.read_csv("tesla_revenue_data.csv")

# Graficar
plt.figure(figsize=(14, 7))

# Gráfico de acciones
plt.subplot(2, 1, 1)
plt.plot(tesla_stock['Date'], tesla_stock['Close'], label='Tesla Stock Price', color='blue')
plt.title('Tesla Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Gráfico de ingresos
plt.subplot(2, 1, 2)
plt.plot(tesla_revenue['Date'], tesla_revenue['Revenue'], label='Tesla Revenue', color='green')
plt.title('Tesla Revenue')
plt.xlabel('Date')
plt.ylabel('Revenue (USD)')
plt.legend()

plt.tight_layout()
plt.savefig("tesla_dashboard.png")
plt.show()
# Leer datos de GameStop
gamestop_stock = pd.read_csv("gamestop_stock_data.csv")
gamestop_revenue = pd.read_csv("gamestop_revenue_data.csv")

# Graficar
plt.figure(figsize=(14, 7))

# Gráfico de acciones
plt.subplot(2, 1, 1)
plt.plot(gamestop_stock['Date'], gamestop_stock['Close'], label='GameStop Stock Price', color='orange')
plt.title('GameStop Stock Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Gráfico de ingresos
plt.subplot(2, 1, 2)
plt.plot(gamestop_revenue['Date'], gamestop_revenue['Revenue'], label='GameStop Revenue', color='red')
plt.title('GameStop Revenue')
plt.xlabel('Date')
plt.ylabel('Revenue (USD)')
plt.legend()

plt.tight_layout()
plt.savefig("gamestop_dashboard.png")
plt.show()
