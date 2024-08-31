import xlwt
from xlwt import Workbook
import xlrd


class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}'s number is {self.number}"

    def __eq__(self, o: object) -> bool:
        return (
            isinstance(o, Contact) and o.name == self.name and o.number == self.number
        )

    def __hash__(self) -> int:
        return hash(self.name)


if __name__ == "__main__":
    contacts = set()
    spreadsheet = "contacts.xls"
    workbook = xlrd.open_workbook(spreadsheet)
    sheet = workbook.sheet_by_index(0)
    for row_index in range(1, sheet.nrows):  # Skip header row
        name = sheet.cell_value(row_index, 0)
        number = sheet.cell_value(row_index, 1)
        contacts.add(Contact(name, number))

    number_of_files = 1
    for i in range(1, number_of_files + 1):
        with open(f"contacts{i}.vcf", "r") as f:
            for x in f:
                if x.startswith("FN"):
                    name = x.split(":", 1)[1].strip()  # Or x[x.index(":")+1:]
                elif name and x.startswith("TEL"):
                    number = x.split(":", 1)[1].strip()

                if name and number:
                    contacts.add(Contact(name, number))
                    name = ""
                    number = ""

    contacts = sorted(contacts, key=lambda x: x.name)

    for contact in contacts:
        print(contact)

    # Create workbook
    wb = Workbook()

    # Create sheet
    sheet = wb.add_sheet("Contacts")

    # Specifying bold style
    style = xlwt.easyxf("font: bold 1")

    # Row, Column
    sheet.write(0, 0, "Full Name", style)
    sheet.write(0, 1, "Telephone Number", style)

    for idx, c in enumerate(contacts):
        sheet.write(idx + 1, 0, c.name)
        sheet.write(idx + 1, 1, c.number)

    wb.save(spreadsheet)
