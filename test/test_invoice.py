import unittest
from datetime import date

from paqueges.Gestion_Paquete.invoice import Invoice

class TestInvoice(unittest.TestCase):
    def setUp(self):
        """Se ejecuta antes de cada prueba. Inicializar datos para Invoice con los cuales se van a hacer las pruebas posteriormente"""
        self.invoice = Invoice(
            invoice_id = 987456,
            amount = 100,
            date = date(2024, 2, 18),
            status = "Entregado"
        )

    def test_invoice_init(self):
        """Verificar que los valores iniciales sean iguales a los asignados para la prueba"""
        self.assertEqual(
            self.invoice.invoice_id,
            987456,
            "El ID de la factura no se inicializó correctamente."
        )
        self.assertEqual(
            self.invoice.amount,
            100,
            "El monto de la factura no se inicializó correctamente."
        )
        self.assertEqual(
            self.invoice.date,
            date(2024, 2, 18),
            "La fecha de creación de la factura no se inicializó correctamente."
        )
        self.assertEqual(
            self.invoice.status,
            "Entregado",
            "El estado de la factura no se inicializó correctamente."
        )

if __name__ == "__main__":
    unittest.main()
