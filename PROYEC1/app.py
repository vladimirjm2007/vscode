import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QComboBox, QMessageBox
)
from PyQt5.QtCore import Qt

class VentanaVentas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Ventas de Ventiladores")
        self.setGeometry(100, 100, 400, 300)

        # Variables para almacenar los datos de venta
        self.precio_ventilador = {
            "Pequeño": 50,
            "Mediano": 80,
            "Grande": 120
        }
        self.total_venta = 0

        # Crear la interfaz
        self.init_ui()

    def init_ui(self):
        # Widget principal
        widget_central = QWidget()
        self.setCentralWidget(widget_central)

        # Layout vertical
        layout = QVBoxLayout()

        # Etiqueta de título
        titulo = QLabel("Bienvenido al Sistema de Ventas")
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titulo)

        # Selector de tipo de ventilador
        layout.addWidget(QLabel("Seleccione el tipo de ventilador:"))
        self.combo_tipo = QComboBox()
        self.combo_tipo.addItems(["Pequeño", "Mediano", "Grande"])
        layout.addWidget(self.combo_tipo)

        # Campo para la cantidad
        layout.addWidget(QLabel("Ingrese la cantidad:"))
        self.input_cantidad = QLineEdit()
        self.input_cantidad.setPlaceholderText("Ejemplo: 2")
        layout.addWidget(self.input_cantidad)

        # Botón para agregar al carrito
        btn_agregar = QPushButton("Agregar al Carrito")
        btn_agregar.clicked.connect(self.agregar_carrito)
        layout.addWidget(btn_agregar)

        # Mostrar total de la venta
        self.label_total = QLabel("Total de la venta: $0")
        self.label_total.setAlignment(Qt.AlignCenter)
        self.label_total.setStyleSheet("font-size: 16px; color: green;")
        layout.addWidget(self.label_total)

        # Botón para finalizar la venta
        btn_finalizar = QPushButton("Finalizar Venta")
        btn_finalizar.clicked.connect(self.finalizar_venta)
        layout.addWidget(btn_finalizar)

        # Asignar el layout al widget central
        widget_central.setLayout(layout)

    def agregar_carrito(self):
        try:
            # Obtener el tipo de ventilador seleccionado
            tipo = self.combo_tipo.currentText()

            # Obtener la cantidad ingresada
            cantidad = int(self.input_cantidad.text())

            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor a cero.")

            # Calcular el subtotal
            precio_unitario = self.precio_ventilador[tipo]
            subtotal = cantidad * precio_unitario

            # Actualizar el total de la venta
            self.total_venta += subtotal

            # Mostrar mensaje de confirmación
            QMessageBox.information(self, "Producto Agregado", f"Se agregaron {cantidad} ventiladores {tipo} al carrito.\nSubtotal: ${subtotal}")

            # Actualizar el label del total
            self.label_total.setText(f"Total de la venta: ${self.total_venta}")

        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))

    def finalizar_venta(self):
        if self.total_venta > 0:
            QMessageBox.information(self, "Venta Finalizada", f"¡Venta finalizada!\nTotal pagado: ${self.total_venta}")
            self.total_venta = 0
            self.label_total.setText("Total de la venta: $0")
        else:
            QMessageBox.warning(self, "Error", "No hay productos en el carrito.")

# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaVentas()
    ventana.show()
    sys.exit(app.exec_())