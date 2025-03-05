from datetime import date


class Invoice:
    def __init__(self, invoice_id: int, amount: float, invoice_date: date, status: str):
        self._invoice_id = invoice_id
        self._amount = amount
        self._invoice_date = invoice_date
        self._status = status

    @property
    def invoice_id(self) -> int:
        return self._invoice_id

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def invoice_date(self) -> date:
        return self._invoice_date

    @property
    def status(self) -> str:
        return self._status

    def __str__(self):
        return (f"Invoice(ID: {self.invoice_id}, Amount: ${self.amount:.2f}, "
                f"Date: {self.invoice_date.strftime('%Y-%m-%d')}, Status: {self.status})")


# Prueba de la clase
def main():
    invoice_example = Invoice(14873, 254, invoice_date = date(2023, 4, 5), status = "Entregado")
    print(invoice_example)


if __name__ == "__main__":
    main()
