# pylint: disable=line-too-long
"""
Escriba el código que ejecute la acción solicitada.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def crear_grafico_bar(datos, columna, titulo, color, archivo_salida, xlabel):
    plt.figure()
    datos[columna].value_counts().plot(kind="bar", color=color, title=titulo)
    plt.xlabel(xlabel)
    plt.ylabel("Cantidad")
    plt.tight_layout()
    plt.savefig(archivo_salida)
    plt.close()


def crear_grafico_hist(datos, columna, titulo, color, archivo_salida, xlabel, bins=10):
    plt.figure()
    datos[columna].plot(kind="hist", bins=bins, color=color, title=titulo)
    plt.xlabel(xlabel)
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(archivo_salida)
    plt.close()


def agregar_tarjeta_html(imagen, titulo, descripcion):
    return f"""
        <div class="card">
            <img src="{imagen}" alt="{titulo}">
            <div class="card-title">{titulo}</div>
            <div class="card-description">{descripcion}</div>
        </div>"""


def pregunta_01():
    """
    Crea un dashboard HTML con visualizaciones basadas en el archivo
    'files/input/shipping-data.csv'. Las gráficas generadas deben
    guardarse en la carpeta 'docs' y visualizarse desde un archivo HTML
    similar al mostrado en el ejemplo proporcionado.
    """
    ruta_datos = "files/input/shipping-data.csv"
    ruta_salida = "docs"
    os.makedirs(ruta_salida, exist_ok=True)

    df = pd.read_csv(ruta_datos)
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Shipping Dashboard</title>
        <style>
            body { font-family: Arial; background-color: #f4f4f9; margin: 0; }
            h1 { text-align: center; margin-top: 40px; color: #2c3e50; }
            .container { display: flex; flex-direction: column; align-items: center; padding: 20px; }
            .dashboard-cards { display: flex; flex-wrap: wrap; justify-content: center; }
            .card {
                background: white; margin: 15px; padding: 20px; width: 300px;
                border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                text-align: center;
            }
            .card img { max-width: 100%; border-radius: 8px; }
            .card-title { font-weight: bold; margin-top: 15px; color: #2c3e50; }
            .card-description { font-size: 0.9em; color: #7f8c8d; }
            .footer {
                text-align: center; padding: 20px;
                background-color: #34495e; color: white; margin-top: 40px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Shipping Dashboard</h1>
            <div class="dashboard-cards">
    """

    # Gráfico 1: Envíos por bodega
    archivo1 = os.path.join(ruta_salida, "shipping_per_warehouse.png")
    crear_grafico_bar(df, "Warehouse_block", "Shipping per Warehouse", "lightblue", archivo1, "Warehouse Block")
    html += agregar_tarjeta_html("shipping_per_warehouse.png", "Shipping per Warehouse", "Distribución de envíos por bodega.")

    # Gráfico 2: Modo de envío
    archivo2 = os.path.join(ruta_salida, "mode_of_shipment.png")
    crear_grafico_bar(df, "Mode_of_Shipment", "Mode of Shipment", "lightgreen", archivo2, "Mode of Shipment")
    html += agregar_tarjeta_html("mode_of_shipment.png", "Mode of Shipment", "Conteo de envíos por modo de transporte.")

    # Gráfico 3: Calificación del cliente
    archivo3 = os.path.join(ruta_salida, "average_customer_rating.png")
    crear_grafico_hist(df, "Customer_rating", "Average Customer Rating Distribution", "salmon", archivo3, "Customer Rating")
    html += agregar_tarjeta_html("average_customer_rating.png", "Average Customer Rating", "Distribución de calificaciones de clientes.")

    # Gráfico 4: Peso del producto
    archivo4 = os.path.join(ruta_salida, "weight_distribution.png")
    crear_grafico_hist(df, "Weight_in_gms", "Weight Distribution", "lightcoral", archivo4, "Weight (gms)", bins=20)
    html += agregar_tarjeta_html("weight_distribution.png", "Weight Distribution", "Distribución de pesos de productos.")

    # Cierre del HTML
    html += """
            </div>
        </div>
        <div class="footer">
            <p>&copy; 2024 Shipping Dashboard. Todos los derechos reservados.</p>
        </div>
    </body>
    </html>
    """

    # Guardar archivo HTML
    with open(os.path.join(ruta_salida, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
