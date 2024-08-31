# Contact Parser

**Problem Statement**: I have too many contacts on my phone. Many of whom I have lost touch with. But, occasionally I get a text message from a rando and I'm like "who dis be?". Every 6 months or so I would back up my contacts. What can I do with them?

**Approach**: Python script to parse the contacts into an organized spreadsheet for easy lookup.

**Note**: For obvious reason I am excluding my .vcf (Virtual Contact File) files but there is a sample.vcf file on this repo. VCF files can be exported from your phone.

**Example of a Contact**

- BEGIN:VCARD
- VERSION:2.1
- N:Wong;Becca
- FN:Becca Wong
- TEL;CELL:+12061234567
- END:VCARD

**How to Run**

1. Name your VCF files `contact{1..n}`.vcf
1. Set up venv `py -m venv venv`
1. Activate virtual environment `source ./venv/Scripts/activate`
1. Install dependency `pip install xlwt xlrd`
1. Run `py main.py`