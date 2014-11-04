__author__ = 'enstulen'


fornavn = ["johan", "eli", "mats", "lene", "simon", "inger", "henrik", "kari", "per"]
etternavn = ["Hag", "Hag", "Basmestad", "Grimlavaag", "Kleivesund", "Fintenes", "Svalesand", "Molteby", "Hegesen"]


#a)
for n in range(len(fornavn)):
    første_bokstav_upper = fornavn[n][0:1].upper()
    første_bokstav = fornavn[n][0:1]
    fullt_navn = fornavn[n].replace(fornavn[n][0], første_bokstav_upper) + " " + etternavn[n]
    print(fullt_navn)
print("----------------")

#b)
etternavn.reverse()
for n in range(len(fornavn)):
    første_bokstav_upper = fornavn[n][0:1].upper()
    første_bokstav = fornavn[n][0:1]
    fullt_navn_baklengs = fornavn[n].replace(fornavn[n][0], første_bokstav_upper) + " " + etternavn[n]
    print(fullt_navn_baklengs)
#Simon Kleivesund - midterste


