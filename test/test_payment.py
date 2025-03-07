import unittest
from datetime import date
from src.payment import Payment
from src.payment import PaymentMethod


class TestPayment(unittest.TestCase):
    def setUp(self):
        """This is executed before each test. Initializes data for Payment which will be used for the tests later"""
        self.payment = Payment(
            payment_id=36987,
            amount=99.99,
            method=PaymentMethod.CREDIT,
            date=date(2024, 2, 18)
        )

    def test_payment_init(self):
        """Verify that the initial values are equal to the ones assigned for the test """
        self.assertEqual(
            self.payment.payment_id,
            36987,
            "The payment number was not initialized correctly."
        )
        self.assertEqual(
            self.payment.amount,
            99.99,
            "The amount to pay was not initialized correctly."
        )
        self.assertEqual(
            self.payment.method,
            PaymentMethod.CREDIT,
            "The invoice status was not initialized correctly."
        )
        self.assertEqual(
            self.payment.date,
            date(2024, 2, 18),
            "The invoice date was not initialized correctly."
        )

    def test_invalid_payment_method(self):
        """Verify that an invalid payment method raises an error"""
        with self.assertRaises(ValueError, msg="Invalid payment method"):
            Payment(12346, 250.00, "Cash", date(2024, 8, 19))


if __name__ == "__main__":
    unittest.main()
