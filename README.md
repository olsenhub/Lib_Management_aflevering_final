# Library Management System

## Beskrivelse
Det her projekt er et bibliotekssystem lavet i Python. Det er lavet for at vise, hvordan man kan bruge objektorienteret programmering i praksis. Programmet kan håndtere bøger og medlemmer gennem en menu i terminalen. I koden er der skrevet kommentarer på noget af koden, som under 'book.py', hvilket beskriver hvad der er hvad. Udover det, giver navne på variabler sig selv.

## Funktioner
- Tilføje bøger
- Fjerne bøger
- Opdatere bøger
- Tilføje medlemmer
- Fjerne medlemmer
- Opdatere medlemmer
- Udlåne og returnere bøger
- Søge efter bøger
- Vise information om bøger og medlemmer

## OOP i projektet
I projektet bruges flere klasser:
- `LibraryItem`
- `Book`
- `EBook`
- `Member`
- `Library`

`Book` og `EBook` arver fra `LibraryItem`, så inheritance er en del af løsningen.

Polymorphism bliver vist gennem `display_info()`, fordi metoden bruges i flere klasser men giver forskelligt output alt efter objektet.

## Struktur
- `main.py` styrer menuen
- `models/` indeholder klasserne
- `tests/` indeholder tests
