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

#Extract all addresses in ‘USA’.
$ grep 'USA' contacts.csv | awk '{print $3, $4, $5, $6, $7}'
123 Main St, Anytown, USA,
456 Oak St, Sometown, USA,
789 Pine Rd, Othertown, USA,
321 Maple Dr, Newcity, USA,
654 Cedar St, Oldtown, USA,
987 Elm St, Smalltown, USA,
246 Birch St, Uptown, USA,
135 Walnut St, Middletown, USA,
864 Chestnut St, Metropolis, USA,
975 Cypress Ave, Bigcity, USA,

#Extract the last names of all people.
$ awk '{print $2}' contacts.csv
Doe,
Smith,
Johnson,
Harris,
Brown,
White,
Green,
Black,
Blue,
Silver,

#Extract all email domains (part after the @ sign).
$ grep -o '@[^ ]*' contacts.csv
@example.com,
@gmail.com,
@yahoo.com,
@hotmail.com,
@company.com,
@domain.org,
@domain.net,
@webmail.com,
@provider.com,
@university.edu,

#Extract all instances of the first name ‘David’ along with their full address (street and city).
$ grep 'David' contacts.csv | awk '{print $1, $2, $3, $4, $5, $6, $7}'
David Green, 246 Birch St, Uptown, USA,

#Find all entries where the phone number ends with ‘7’.
$ grep '7$' contacts.csv | awk '{print $9, $10}'
(555) 123-4567
(555) 246-1357

#Extract all instances of first names that end with the letter 'e'.
$ grep "^\b[A-Za-z]*e\b" contacts.csv | awk '{print $1}'
Jane
Mike
Alice

