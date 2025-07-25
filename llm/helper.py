MISTRAL_CHANGE_PROMPT="""  
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

LLAMA3_CHANGE_PROMPT="""
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

QWEN3_CHANGE_PROMPT="""
Tvoj zadatak je da analiziraš jednu rečenicu i ispraviš je tako da ukloniš govor mržnje, uvrede, predrasude ili diskriminatorni sadržaj, ali da zadržiš osnovnu poruku ako je moguće.
Vrati samo jedan red:
Ako si ispravio rečenicu, započni sa „Preformulisana.“
Ako si zamenio rečenicu neutralnom porukom, započni sa „Neutralna poruka.“
Ne objašnjavaj, ne dodaj razloge, vrati samo rezultat.

Primeri:
Ulaz: „Ti cigani stalno kradu.“
Izlaz: Neutralna poruka. Neprihvatljivo je da generalizujemo čitav narod zbog postupaka pojedinaca.

Ulaz: „Mrzim gejeve, to nije prirodno.“
Izlaz: Preformulisana. Smatram da su različiti načini života legitimni i važno je poštovati tuđe izbore.

Ulaz: „Žene nisu za programiranje.“
Izlaz: Preformulisana. Verujem da sposobnosti u programiranju ne zavise od pola.

Ulaz: „Svi Albanci su opasni.“
Izlaz: Neutralna poruka. Nije ispravno donositi sud o ljudima na osnovu njihove nacionalnosti.

"""

PHI3_CHANGE_PROMPT="""
Tvoj zadatak je da analiziraš unetu rečenicu i ispraviš je tako da ukloniš svaki govor mržnje, uvrede, predrasude ili diskriminatorni sadržaj, ali da zadržiš osnovnu poruku ako je moguće. Rečenica treba da ostane informativna, ali da bude kulturna, neutralna i nepristrasna.

Govor mržnje uključuje:

vređanje ili omalovažavanje ljudi na osnovu rase, vere, nacionalnosti, pola, seksualne orijentacije, invaliditeta ili društvenog statusa

stereotipe, generalizacije i pozive na nasilje

Uputstvo:

Ako je moguće, preformuliši rečenicu i zadrži njenu osnovnu poruku bez uvredljivog sadržaja

Ako rečenica nema korisnu informaciju i sadrži samo govor mržnje, zameni je neutralnom porukom

Na početak odgovora uvek dodaj:

„Preformulisana.“ ako si izmenio rečenicu i zadržao smisao

„Neutralna poruka.“ ako si je zamenio neutralnom izjavom

Primeri:

Ulaz: „Ti cigani stalno kradu.“
Izlaz: Neutralna poruka. Neprihvatljivo je da generalizujemo čitav narod zbog postupaka pojedinaca.

Ulaz: „Mrzim gejeve, to nije prirodno.“
Izlaz: Preformulisana. Smatram da su različiti načini života legitimni i važno je poštovati tuđe izbore.

Ulaz: „Žene nisu za programiranje.“
Izlaz: Preformulisana. Verujem da sposobnosti u programiranju ne zavise od pola.

Ulaz: „Svi Albanci su opasni.“
Izlaz: Neutralna poruka. Nije ispravno donositi sud o ljudima na osnovu njihove nacionalnosti.

"""

change_prompt_map={"mistral":MISTRAL_CHANGE_PROMPT, "llama3": LLAMA3_CHANGE_PROMPT, "qwen3": QWEN3_CHANGE_PROMPT,"phi3":PHI3_CHANGE_PROMPT}


MISTRAL_HIGHLIGHT_PROMPT="""
U tekstu koji ce ti biti prosledjen , pronađi sve delove koji predstavljaju govor mržnje — to su uvrede, stereotipi, diskriminatorne ili nasilne izjave na osnovu rase, vere, nacionalnosti, pola, seksualne orijentacije, invaliditeta ili društvenog statusa.
Tekst koji treba da analiziraš nalazi se posle reči "Ulaz:"
Ako tekst ne sadrži govor mržnje MORAŠ da vratiš samo tekst koji je prosledjen nakon reči "Ulaz:"

Zadatak:
Označi samo te delove tako što ćeš ih staviti između <mark> i </mark>.
Nemoj menjati ostatak teksta. Nemoj dodavati objašnjenja. Vrati samo rezultat.

Primeri:

Ulaz: Ti cigani stalno kradu.
Izlaz: Ti <mark>cigani stalno kradu</mark>.

Ulaz: Mrzim gejeve, to nije prirodno.
Izlaz: <mark>Mrzim gejeve, to nije prirodno</mark>.

Ulaz: Žene su previše emotivne da bi bile lideri.
Izlaz: <mark>Žene su previše emotivne da bi bile lideri</mark>.

Ulaz: On je retardiran, ne zna ništa.
Izlaz: On je <mark>retardiran</mark>, ne zna ništa.

Ulaz: Svi Albanci su opasni.
Izlaz: <mark>Svi Albanci su opasni</mark>.

"""

LLAMA3_HIGHLIGHT_PROMPT="""
Zadatak: Obeležavanje govora mržnje u tekstu.

U tekstu koji sledi posle reči "Ulaz:", pronađi sve delove koji predstavljaju govor mržnje — to su uvrede, stereotipi, diskriminatorne ili nasilne izjave na osnovu rase, vere, nacionalnosti, pola, seksualne orijentacije, invaliditeta ili društvenog statusa.

Ako tekst NE sadrži govor mržnje, moraš da vratiš TAČNO onaj tekst koji je bio nakon reči "Ulaz:", bez ikakvih dodataka.

Zadatak:
Označi sve uvredljive ili diskriminatorne delove tako što ćeš ih staviti između <mark> i </mark>.
Ne menjaj ostatak teksta.
Ne dodaj nikakvo objašnjenje.
Vrati samo rezultat.

Primeri:

Ulaz: Ti cigani stalno kradu.
Izlaz: Ti <mark>cigani stalno kradu</mark>.

Ulaz: Mrzim gejeve, to nije prirodno.
Izlaz: <mark>Mrzim gejeve, to nije prirodno</mark>.

Ulaz: Žene su previše emotivne da bi bile lideri.
Izlaz: <mark>Žene su previše emotivne da bi bile lideri</mark>.

Ulaz: On je retardiran, ne zna ništa.
Izlaz: On je <mark>retardiran</mark>, ne zna ništa.

Ulaz: Svi Albanci su opasni.
Izlaz: <mark>Svi Albanci su opasni</mark>.

"""
QWEN3_HIGHLIGHT_PROMPT="""
Analiziraj tekst koji dolazi posle reči "Ulaz:" i označi sve delove koji sadrže govor mržnje — uvrede, stereotipe, diskriminaciju ili nasilne tvrdnje na osnovu rase, vere, nacionalnosti, pola, seksualne orijentacije, invaliditeta ili društvenog statusa.

Ako u tekstu nema govora mržnje, moraš tačno da vratiš neizmenjeni tekst koji je usledio posle "Ulaz:".

Zadatak:
- Samo delove govora mržnje obeleži tagovima <mark> i </mark>
- Ostatak teksta ne smeš da menjaš
- Ne dodaj nikakve komentare, objašnjenja ni napomene
- Vrati samo označen tekst

Primeri:

Ulaz: Ti cigani stalno kradu.
Izlaz: Ti <mark>cigani stalno kradu</mark>.

Ulaz: Mrzim gejeve, to nije prirodno.
Izlaz: <mark>Mrzim gejeve, to nije prirodno</mark>.

Ulaz: Žene su previše emotivne da bi bile lideri.
Izlaz: <mark>Žene su previše emotivne da bi bile lideri</mark>.

Ulaz: On je retardiran, ne zna ništa.
Izlaz: On je <mark>retardiran</mark>, ne zna ništa.

Ulaz: Svi Albanci su opasni.
Izlaz: <mark>Svi Albanci su opasni</mark>.

"""
PHI3_HIGHLIGHT_PROMPT="""
U tekstu koji dolazi nakon reči "Ulaz:", pronađi sve izraze koji sadrže govor mržnje — to uključuje uvrede, stereotipe, diskriminatorne ili nasilne izjave na osnovu rase, vere, nacionalnosti, pola, seksualne orijentacije, invaliditeta ili društvenog statusa.

Ako tekst ne sadrži govor mržnje, MORAŠ da vratiš taj tekst bez ikakvih promena.

Zadatak:
- Obeleži samo govor mržnje između tagova <mark> i </mark>
- Ne menjaj ostatak teksta
- Ne dodaj objašnjenja, uvode ni napomene
- Vrati samo označeni tekst

Primeri:

Ulaz: Ti cigani stalno kradu.
Izlaz: Ti <mark>cigani stalno kradu</mark>.

Ulaz: Mrzim gejeve, to nije prirodno.
Izlaz: <mark>Mrzim gejeve, to nije prirodno</mark>.

Ulaz: Žene su previše emotivne da bi bile lideri.
Izlaz: <mark>Žene su previše emotivne da bi bile lideri</mark>.

Ulaz: On je retardiran, ne zna ništa.
Izlaz: On je <mark>retardiran</mark>, ne zna ništa.

Ulaz: Svi Albanci su opasni.
Izlaz: <mark>Svi Albanci su opasni</mark>.

"""

highlight_prompt_map={"mistral":MISTRAL_HIGHLIGHT_PROMPT,"llama3":LLAMA3_HIGHLIGHT_PROMPT,"qwen3":QWEN3_HIGHLIGHT_PROMPT,"phi3":PHI3_HIGHLIGHT_PROMPT}