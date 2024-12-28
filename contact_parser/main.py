import xlwt
from xlwt import Workbook
import xlrd
import os
import vobject

class Contact:
    """Represents a contact with a name and a phone number."""

    def __init__(self, name: str, number: str):
        """Initialize a Contact object."""
        self.name = name
        self.number = number

    def __str__(self) -> str:
        """Return a string representation of the contact."""
        return f"{self.name}'s number is {self.number}"

    def __eq__(self, o: object) -> bool:
        """Check if two contacts are equal."""
        return (
            isinstance(o, Contact) and o.name == self.name and o.number == self.number
        )

    def __hash__(self) -> int:
        """Return a hash of the contact."""
        return hash(self.name)


def read_contacts_from_spreadsheet(spreadsheet: str) -> set:
    """Read contacts from a spreadsheet."""
    contacts = set()
    if os.path.exists(spreadsheet):
        workbook = xlrd.open_workbook(spreadsheet)
        sheet = workbook.sheet_by_index(0)
        for row_index in range(1, sheet.nrows):  # Skip header row
            name = sheet.cell_value(row_index, 0)
            number = sheet.cell_value(row_index, 1)
            contacts.add(Contact(name, number))
    return contacts


def read_contacts_from_vcard(vcard_file: str) -> set:
    """Read contacts from a vCard file."""
    contacts = set()
    with open(vcard_file, 'r') as file:
        vcf_data = file.read()

    vcard_list = vobject.readComponents(vcf_data)

    for vcard in vcard_list:
        name = vcard.fn.value if hasattr(vcard, 'fn') else 'N/A'
        tel = vcard.tel.value if hasattr(vcard, 'tel') else 'N/A'
        tel = tel.replace("-", "").replace("+", "")
        contacts.add(Contact(name, tel))

    return contacts


def write_contacts_to_spreadsheet(spreadsheet: str, contacts: set) -> None:
    """Write contacts to a spreadsheet."""
    # Create workbook
    wb = Workbook()

    # Create sheet
    sheet = wb.add_sheet("Contacts")

    # Specifying bold style
    style = xlwt.easyxf("font: bold 1")

    # Row, Column
    sheet.write(0, 0, "Full Name", style)
    sheet.write(0, 1, "Telephone Number", style)

    for idx, c in enumerate(sorted(contacts, key=lambda x: x.name)):
        sheet.write(idx + 1, 0, c.name)
        sheet.write(idx + 1, 1, c.number)

    wb.save(spreadsheet)


if __name__ == "__main__":
    contacts = read_contacts_from_spreadsheet("output.xls")
    contacts.update(read_contacts_from_vcard("contacts.vcf"))
    write_contacts_to_spreadsheet("output.xls", contacts)