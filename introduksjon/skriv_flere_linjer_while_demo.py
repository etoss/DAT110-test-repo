# Skriv inn flere linjer tekst, hvor brukeren avslutter med å skrive
# ei tom linje
print("Skriv inn en tekst. Avslutt med tom linje.")
linja = input("> ")
resultat = linja + "\n"
while linja != "":
    linja = input("> ")
#    resultat = resultat + linja + "\n"
    resultat += linja + "\n"
print(resultat)
