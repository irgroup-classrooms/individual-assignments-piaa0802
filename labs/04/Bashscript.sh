#!/bin/bash

#Extract all email addresses from the text.
$ grep -o '[^ ]*@[^ ]*' contacts.csv
john.doe@example.com,
jane.smith@gmail.com,
mjohnson@yahoo.com,
lharris@hotmail.com,
rbrown@company.com,
alice.white@domain.org,
dgreen@domain.net,
eblack@webmail.com,
cblue@provider.com,
ssilver@university.edu,

#Extract all phone numbers from the text.
$ grep -o '(555) [^ ]*' contacts.csv
(555) 123-4567
(555) 987-6543
(555) 555-5555
(555) 321-6789
(555) 876-5432
(555) 432-5678
(555) 246-1357
(555) 531-2468
(555) 864-9753
(555) 975-8642

#Extract all names that start with the letter ‘J’.
$ grep -o 'J[^ ]*' contacts.csv
John
Jane
Johnson,

#Extract all street names that contain the word 'St'.
$ grep -o '[^ ]* [^ ]* [^ ]*St' contacts.csv
123 Main St
456 Oak St
654 Cedar St
987 Elm St
246 Birch St
135 Walnut St
864 Chestnut St
