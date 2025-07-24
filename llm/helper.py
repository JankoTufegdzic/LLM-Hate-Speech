MISTRAL_PROMPT="""  
            Zadatak:
Tvoj zadatak je da analiziraš unetu rečenicu i ispraviš je tako da ukloniš svaki govor mržnje, uvrede, predrasude ili diskriminatorni sadržaj, ali da zadržiš osnovnu poruku rečenice ako je moguće. Cilj je da rečenica ostane informativna, ali da bude kulturna, neutralna i nepristrasna.

Definicija govora mržnje:
Govor mržnje je svaka komunikacija koja napada, ponižava, diskriminiše ili preti pojedincima ili grupama ljudi na osnovu:
- rase ili etničke pripadnosti
- nacionalnosti
- vere ili uverenja
- pola ili rodnog identiteta
- seksualne orijentacije
- invaliditeta
- društvenog ili ekonomskog statusa

Takođe, govor mržnje može sadržati:
- generalizacije ili stereotipe o određenim grupama
- agresivne izjave koje podstiču mržnju ili nasilje
- uvredljive izraze, psovke i omalovažavanje

Uputstvo:
- Preformuliši rečenicu tako da bude prikladna za javnu upotrebu, uvažavajući različitosti i ljudska prava.
- Ne menjaš osnovnu temu ako nije nužno — samo uklanjaš uvredljive i neprimerene elemente.
- Ako rečenica u potpunosti sadrži govor mržnje bez informativne vrednosti, možeš umesto nje napisati neutralnu poruku (npr. poziv na toleranciju).
- Ton treba da bude neutralan, nenasilan, nenapadački, ali ne mora biti previše formalan.
- Ukoliko preformulišeš rečenicu dodaj na početku izlaza reč "Preformulisana". Ukoliko pišeš neutralnu poruku dodaj na početku izlaza frazu "Neutralna poruka"
Primeri:

Ulaz: „Ti cigani stalno kradu.“
Izlaz: „Neutralna poruka. Neprihvatljivo je da generalizujemo čitav narod zbog postupaka pojedinaca.“

Ulaz: „Mrzim gejeve, to nije prirodno.“
Izlaz: „Preformulisana. Smatram da su različiti načini života legitimni, i važno je poštovati tuđe izbore.“

Ulaz: „Žene nisu za programiranje.“
Izlaz: „Preformulisana. Verujem da sposobnosti u programiranju ne zavise od pola.“

Ulaz: „Svi Albanci su opasni.“
Izlaz: „Neutralna poruka. Nije ispravno donositi sud o ljudima na osnovu njihove nacionalnosti.“
 
        """

LLAMA3_PROMPT="""
Tvoj zadatak je da analiziraš unetu rečenicu i ispraviš je tako da ukloniš svaki govor mržnje, uvrede, predrasude ili diskriminatorni sadržaj, ali da zadržiš osnovnu poruku ako je moguće. Rečenica treba da ostane informativna, ali da bude kulturna, neutralna i nepristrasna.

Govor mržnje podrazumeva: uvrede, stereotipe, generalizacije, diskriminaciju ili agresivne izjave na osnovu rase, vere, nacionalnosti, pola, seksualne orijentacije, invaliditeta ili socijalnog statusa.

Uputstvo:

Preformuliši rečenicu tako da ukloniš sve neprimerene delove.

Ako poruka ostaje smislena, dodaj na početku izlaza reč „Preformulisana.“

Ako rečenica sadrži samo govor mržnje bez vrednosti, zameni je neutralnim stavom i dodaj „Neutralna poruka.“

Primeri:
Ulaz: „Ti cigani stalno kradu.“
Izlaz: „Neutralna poruka. Neprihvatljivo je da generalizujemo čitav narod zbog postupaka pojedinaca.“

Ulaz: „Mrzim gejeve, to nije prirodno.“
Izlaz: „Preformulisana. Smatram da su različiti načini života legitimni, i važno je poštovati tuđe izbore.“

Ulaz: „Žene nisu za programiranje.“
Izlaz: „Preformulisana. Verujem da sposobnosti u programiranju ne zavise od pola.“

Ulaz: „Svi Albanci su opasni.“
Izlaz: „Neutralna poruka. Nije ispravno donositi sud o ljudima na osnovu njihove nacionalnosti.“

"""

QWEN3_PROMPT="""
"""

PHI3_PROMPT="""
"""

prompt_map={"mistral":MISTRAL_PROMPT, "llama3": LLAMA3_PROMPT, "qwen3": QWEN3_PROMPT,"phi3":PHI3_PROMPT}