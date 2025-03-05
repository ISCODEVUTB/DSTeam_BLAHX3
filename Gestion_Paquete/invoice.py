from datetime import date

class Invoice:
    def __init__(self, invoice_id: int, amount: float, date: str, status: str):
        self.__invoice_id = invoice_id
        self.__amount = amount
        self.__date = date
        self.__status = status

    @property
    def invoice_id(self) -> int:
        return self.__invoice_id

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def date(self) -> date:
        return self.__date

    @property
    def status(self) -> str:
        return self.__status

    def __str__(self):
        return f"Invoice(ID: {self.invoice_id}, Amount: ${self.amount:.2f}, Date: {self.date}, Status: {self.status})"

#Prueba de la clase
def main():
    try_invoice = Invoice(14873, 254, date(2023, 4, 5), "Entregado")
    print(try_invoice)

if __name__ == '__main__':
    main()
