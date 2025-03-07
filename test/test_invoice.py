1import unittest
from datetime import date
from src.invoice import Invoice


class TestInvoice(unittest.TestCase):
    def setUp(self):
        """This is executed before each test. Initializes data for Invoice which will be used for the tests later"""
        self.invoice = Invoice(
            invoice_id=987456,
            amount=100,
            invoice_date=date(2024, 2, 18),
            status="Pago"
        )

    def test_invoice_init(self):
        """Verify that the initial values are equal to the ones assigned for the test """
        self.assertEqual(
            self.invoice.invoice_id,
            987456,
            "The invoice ID was not initialized correctly."
        )
        self.assertEqual(
            self.invoice.amount,
            100,
            "The invoice amount was not initialized correctly."
        )
        self.assertEqual(
            self.invoice.invoice_date,
            date(2024, 2, 18),
            "The invoice date was not initialized correctly."
        )
        self.assertEqual(
            self.invoice.status,
            "Pago",
            "The invoice status was not initialized correctly."
        )


if __name__ == "__main__":
    unittest.main()
