import os

import discord
from dotenv import load_dotenv
from discord.utils import get

import random
from unidecode import unidecode

# import mého webscaperu
#from zakony import ustanoveniZakona

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

obecne = 0

@client.event
async def on_ready():
    global obecne
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    obecne = await client.fetch_channel(905841944507322428) # kanál na procvičování češtiny
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
    #await obecne.send("Vítejte na kanále pro učení. Budu se vám snažit pomoci při učení. Jako první jsem se naučil zkoušet z češtiny. Pokud chcete zapnout učení, napište `uč češtinu` a já začnu vám náhodně psát autora nebo jejich dílo. Vaši odpověď vyhodnotím a hned zadám další otázku. Pokud byste chtěli učení předčasně ukončit, zadejte příkaz `uč rst` a já vyhodnotím vaše znalosti a učení ukončím. Pro psaní názvů děl a jmen autorů mám pravidlo, že není nutné psát velká písmena ani diakritiku, jen u jmen spisovatelů pište pro správné vyhodnocení jen jejich příjmení, v případě bratří Čapků jejich iniciálu a příjmení, např. `j. Čapek` nebo `steinbeck`.")

# proměnná pro učení
studySet = []
dotazovani = 0
odpoved = ""
odpovedplna = ""
polozky = 0
spravne = 0
vyber = []

@client.event
async def on_message(message):
    global studySet, dotazovani, odpoved, odpovedplna, obecne, polozky, spravne, vyber
    if message.author == client.user:
        return
    print(message.author, message.author.id)

    if message.content == 'MO':
        response = "```l) osoby s poruchou intelektu, s poruchou autistického spektra, a kognitivní poruchou nebo se závažnou alterací duševního stavu, jejichž mentální schopnosti či aktuální duševní stav neumožňují dodržování tohoto zákazu```"#random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if message.content.find("§") == 0 or message.content.find("Čl.") == 0:
        try:
            ustanoveni = message.content.split()
            for i in ustanoveni[1:]:
                icislo = False
                for j in i:
                    if j.isdigit():
                        icislo = True
                        break
                if not icislo:
                    ustanoveni.remove(i)    
                print(ustanoveni)
            if len(ustanoveni[2]) >= 6:
                cislozakona = ustanoveni[2].split("/")
            else:
                cislozakona = ustanoveni[3].split("/")   
            if len(ustanoveni[2]) < 6:
                odstavec = int(ustanoveni[2])
            else:
                try:
                    odstavec = int(ustanoveni[3])
                except:    
                    odstavec = 0    
            
            response = ustanoveniZakona(f"{ustanoveni[0]} {ustanoveni[1]}", f"{cislozakona[1]}-{cislozakona[0]}", odstavec)
            odst = f" odst. {odstavec}" if odstavec != 0 else ""
            response = f"{ustanoveni[0]} {ustanoveni[1]}{odst} zákona {cislozakona[0]}/{cislozakona[1]} Sb. zní:```{response}```"
            
            if len(response) > 2000:
                response =  "Chlape, upřesni svůj požadavek, zpráva je příliš dlouhá."
            # Dělení zprávy na kratší kusy pod 2000 znaků, nebo rozdělení na více zpráv - UNDER CONSTRUCTION ;)
            #     delka = 0
            #     posl = response.find("\n")
            #     while posl < 2000:
            #         try:
            #             delka = posl
            #             posl = response[posl+2:].find("\n")
            #             #print(response[posl+2:])
            #         except:
            #             break
            # response = response[:posl]        
        except:
            odpovedi = [f"Heeej, ještě jednou mě budeš takhle otravovat, tak budeš předhozen {client.get_emoji(766190415673425920)} a budeš si muset psát do sešitu výživné věty typu `Naučím se odhadovat.`", f"Co to má znamenat? Pamatuj, že `vnitřní sebekázeň je důležitá při studiu na VŠ,` jak pravila {client.get_emoji(766190415673425920)}.", "Jestli tady budeš psát `§` a přitom nebudeš chtít znát znění nějakého zákona, TAK DOSTANEŠ FLÁKANEC!"]
            response = random.choice(odpovedi) #Chlape, zahlédl jsem na začátku tvé zprávy `§` nebo `Čl.`, ale někde jsi udělal chybu. Pokud chceš znát ustanovení nějakého zákona, piš ho ve tvaru `ustanovení z. číslo_zákona`, např. `§ 5 z. 89/2012` nebo `Čl. 7 z. 2/1993`."         
        if response == "``````":
            response = "Vypadá to, že článek nebo paragraf, který hledáš, neexistuje."
        await message.channel.send(response)

    if message.content == "Bobe strč si ten paragraf do prdele":
        odpovedi = ["Nech Boba na pokoji <@788873442664906752>, starej se o sebe, určitě je ten paragraf důležitý.", "Zase ty, <@788873442664906752>, že se nestydíš tahkle tady otravovat.", "<@788873442664906752>, radši si hlídej svůj řád a na paragrafy zapomeň.", "<@788873442664906752>, za takovou nestoudnost bys měl být zbaven všech řádů a degradován na žížalu."]
        response = random.choice(odpovedi)
        await message.channel.send(response)
    if message.content == "<@!815666757623611413> release":
        response = "```Aktuální verze: 11 \n NOVINKY ve verzi: \n - nově lze zobrazit i jen odstavec ze zákona \n - při zadávání požadavku o výpis ustanovení zákona není podstatné pořadí a úprava textu (jen samozřejmě pro vyvolání této operace je nutné začít text buď symbolem §, nebo textem 'Čl.') \n - všechny zápisy požadavku, kde bude § nebo Čl. a příslušné číslo, číslo zákona a popř. číslo odstavce, budou vyhodnoceny správně \n - doplněna chybová hláška při přesažení maximální délky zprávy 2000 znaků \n - zobrazení tohoto release logu```"
        await message.channel.send(response)

    # učení pojmů - autor-dílo apod.
    print(message.channel, message.guild)
    #if message.channel == "obecné" and message.guild == "bkulvejt's server":

    if message.channel.id == 905841944507322428 and message.author.id != 700657766527664168:
        if message.content == "uč rst" or message.content == "uč konec":
            await obecne.send(f"Vyhodnocení: Z celkových {polozky} otázek jsi správně odpověděl na {spravne} z nich. \n  Úspěšnost {round(spravne / polozky, 3) * 100} %.")
            await obecne.send("Učení zastaveno.")
            dotazovani = 0
            odpoved = ""
            odpovedplna = ""
            studySet = []
            polozky = 0
            spravne = 0
            vyber = []
        elif message.content == "uč help":
            await obecne.send("""- - - - - UČ HELP - - - - -
začátek učení: `uč češtinu` | konec učení: `uč rst` nebo `uč konec`
Pro správné vyhodnocení pište pouze příjmení spisovatelů, pouze u bratří Čapků připište iniciálu.
Kontrola odpovědí není case-sensitive ani není citlivá na diakritiku.
Po zodpovězení všech otázek je vyhodnocen výsledek. Vyhodnocení se taktéž zobrazí při předčasném ukončení pomocí příkazu.""")
        elif message.content[:2] == "uč":
            dotazovani = 0
            odpoved = ""
            odpovedplna = ""
            studySet = []
            polozky = 0
            spravne = 0
            vyber = []
            if message.content[3:] == "češtinu":
                f = open("cestina-zadani.txt","r",encoding="utf8")
                f = f.read()
                fpripr = f.split("\n")
                #print(f.read())
                """for _ in f:
                    fpripr.append(f.readline())
                print(fpripr)"""
                for prip in range(len(fpripr)):
                    studySet.append([])
                for n, vypis in enumerate(fpripr):
                    vypis = vypis.split("; ")
                    for j in vypis:
                        studySet[n].append(j)
                print(studySet)
                #studySet = [["s1", "d11", "d12"], ["s2", "d21"], ["s3", "d31", "d32"]]
                await obecne.send("Zadání zaznamenáno")
            else:
                await obecne.send("Takové zadání neexistuje.")
                return

        def zjednodus(text):
            return unidecode(text.lower())

        def zadej():
            global studySet, obecne, dotazovani, odpoved, odpovedplna, vyber
            vyber = random.choice(studySet)
            # print(vyber)
            studySet.remove(vyber)
            # print(studySet)

            verze = random.choice(vyber)
            print("Zadání:", verze)

            # await obecne.send(verze)

            if verze == vyber[0]:
                odpovedplna = vyber[1:]
                vyberbez = []
                for i in range(1,len(vyber)):
                    vyberbez.append(zjednodus(vyber[i]))
                odpoved = vyberbez
            else:
                odpovedplna = vyber[0]
                odpoved = zjednodus(vyber[0])
            print("Odpověď:", odpoved)
            dotazovani = 1
            return verze

        def vyhodnot():
            global odpoved, odpovedplna, dotazovani, polozky, spravne, vyber, studySet
            if (zjednodus(message.content) in odpoved and type(odpoved) == list) or (zjednodus(message.content) == odpoved):
                polozky += 1
                spravne += 1
                return "✅"
            polozky += 1
            studySet.append(vyber)
            return "❌"


        if len(studySet) > 0 and dotazovani == 0:
            await obecne.send(zadej())
        elif len(studySet) > 0 and dotazovani == 1:
            await message.add_reaction(vyhodnot())
            docodp = ""
            if type(odpovedplna) == list:
                for vypis in odpovedplna:
                    docodp += f"{vypis}, "
                docodp = docodp[:-2]
                await obecne.send(f"Správně je {docodp}")
            else:
                await obecne.send(f"Správně je {odpovedplna}")
            #print("Odpověď:",odpoved)
            await obecne.send(zadej())
        elif dotazovani == 1:
            await message.add_reaction(vyhodnot())
            docodp = ""
            if type(odpovedplna) == list:
                for vypis in odpovedplna:
                    docodp += f"{vypis}, "
                docodp = docodp[:-2]
                await obecne.send(f"Správně je {docodp}")
            else:
                await obecne.send(f"Správně je {odpovedplna}")
            await obecne.send(f"Vyhodnocení: Z celkových {polozky} otázek jsi správně odpověděl na {spravne} z nich. \n  Úspěšnost {round(spravne/polozky*100,1)} %.")
            dotazovani = 0







# @client.event
# @commands.has_permissions(manage_roles=True) 
# async def on_message(message):
#     print("ano")
#     if message.content == 'ahoj bobobote':
#         membobo = message.author
#         var = discord.utils.get(message.guild.roles, name = "New Budha")
#         print(var)
#         print(discord.Permissions.manage_roles == False)
#         await Member.add_roles(membobo, var)

client.run(TOKEN)
