import xlwt
from xlwt import Workbook


class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self) -> str:
        return f"{self.name}'s number is {self.number}"

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Contact) and o.name == self.name

    def __hash__(self) -> int:
        return hash(self.name)


if __name__ == '__main__':
    number_of_files = 4
    contacts = set()
    name = ""
    number = ""
    for i in range(1, number_of_files + 1):
        with open(f"contact{i}.vcf", 'r') as f:
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
    sheet = wb.add_sheet('Contacts')

    # Specifying bold style
    style = xlwt.easyxf('font: bold 1')

    # Row, Column
    sheet.write(0, 0, 'Full Name', style)
    sheet.write(0, 1, 'Telephone Number', style)

    for idx, c in enumerate(contacts):
        sheet.write(idx + 1, 0, c.name)
        sheet.write(idx + 1, 1, c.number)

    wb.save('contact.xls')
