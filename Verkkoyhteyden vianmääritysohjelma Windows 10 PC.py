
# Copyright Veli Heikki Vesala 2022

# Lähteet 'WLAN-verkko pätkii'-osioon: https://helpdeskgeek.com/networking/can-connect-to-wireless-router-but-not-to-the-internet/  ja https://helpdeskgeek.com/free-tools-review/what-should-you-look-for-in-a-new-modem-router/  
# Lähteet 'Ei internetyhtyettä WLAN-verkossa'-osioon: https://helpdeskgeek.com/help-desk/do-you-need-a-third-party-firewall-on-mac-and-windows/ ja https://www.online-tech-tips.com/computer-tips/unable-delete-network-adapter-windows-10/

from art import *
import time
import os
import ctypes


# Avaa terminaalin ikkuna koko näytölle

def kokoIkkunaNäyttö():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')

    SW_MAXIMIZE = 3

    hWnd = kernel32.GetConsoleWindow()  # saattaa 'handle'-toiminnon terminaaliin niin että ShowWindow() tietää mitä muokata
    user32.ShowWindow(hWnd, SW_MAXIMIZE)    # ShowWindow() kertoo ikkunalle, miltä näyttää (annetaan hWnd muuttujan arvo ja toisena parametrina 3 eli koko näyttö)


#Tyhjennä näytön ruutu kokonaan
def tyhjennäRuutu():
    tyhjää = os.system('cls')


# Otsikko jokaiselle funktiolle

def otsikko(otsikon_nimi, keskitys):
    print("")
    tprint(otsikon_nimi.center(keskitys))

def kuva_wlanYhteysPoikki():
    print(r""" 
                                                                                               Mihin WLAN-yhteys katosi?!?
                                                                                                _________________________
                                                                                               |  _____________________  |
                                                           ??                                  | |              ______ | |
                                                                   ??                          | |  Windows 10 /__/__/ | |
                                                              ??                               | |            /__/__/  | |
                                                            .    .                             | |_____________________| |
                                                            |    |                             |_________________________|
                                                           _|____|__                          / __ __ __ __ __ __ __ __  /
                                                          / |    | /|                        / __ __ __ __ __ __ __ __  /
                                                         /   R-1  / /                       / __ __ __ __ __ __ __ __  /
                                                        /________/ /                       /        ________          /
                                                        |________|/                       /__________________________/    
    

    """)


# WLAN-verkon navigointi eli 'menu'-valikko

def nav_WLAN():

    tyhjennäRuutu()
    
    otsikko("MENU:   WLAN-verkko", 100)

    kuva_wlanYhteysPoikki()

    print("\n  Miten yhteysongelma tietokoneellasi ilmenee? Vai haluatko yleistietoa verkkoprotokollista tai tietoturvasta?\n\n\
    1) Verkkoyhteyttä ei ole tai se pätkii.\n\
    2) Selain ei toimi.\n\
    3) Etsimäni verkkosivu ei löydy.\n\
    4) Muu yhteysongelma.\n\
    5) Tietoa WLAN-verkosta.\n\
    6) WLAN-verkon tietoturvauhat ja niiden ehkäiseminen.\n\
    7) Poistu ja sulje ohjelma kokonaan.\n")
    
    i = 0

    while (i < 1):

        oletuksenaNumero = None

        while (oletuksenaNumero == None):
            ongelmanValinta = input("\n  Valitse sopivin vaihtoehto vastaamalla numerolla: ")
            try:
                oletuksenaNumero = int(ongelmanValinta)
            except:
                print("\n  Ilmoita vastauksesi numerona.\n")

        ongelmanValinta = int(ongelmanValinta)

        if (ongelmanValinta == 1):
            print("\n  Verkkoyhteydessäsi on siis ongelmia. Yritetään vielä täsmentää ongelmaa.\n\n \
   1) Pätkiikö verkkoyhteytyesi?\n \
   2) Näkyykö 'Ei internet-yhteyttä'-kuvake oikeassa alakulmassa työpöytänäkymässä?\n \
   3) Katkesiko yhteys heti Windows 10 päivityksen jälkeen?\n \
   4) Palaa edelliseen valikkoon.\n")
        
            while (True):
                oletuksenaNumero = None

                while (oletuksenaNumero == None):
                    ongelmanTarkennettuVastaus = input("\n  Valitse sopivin vaihtoehto vastaamalla numerolla: ")
                    try:
                        oletuksenaNumero = int(ongelmanTarkennettuVastaus)
                    except:
                        print("\n  Ilmoita vastauksesi numerona.\n")

            
                ongelmanTarkennettuVastaus = int(ongelmanTarkennettuVastaus)

                if (ongelmanTarkennettuVastaus > 4):
                    print("\n  Anna vastaus numerona 1-4 väliltä.\n")
                elif (ongelmanTarkennettuVastaus == 1):
                    yhteysPätkii()
                    break
                elif (ongelmanTarkennettuVastaus == 2):
                    eiInternetYhteyttäKuvake()
                    break
                elif (ongelmanTarkennettuVastaus == 3):
                    päivitysOngelmaWin10("wlan")
                    break
                elif (ongelmanTarkennettuVastaus == 4):
                    nav_WLAN()
                    break

        elif (ongelmanValinta == 2):
            print("\n  Selaimesi ei siis toimi oikein. Ensin tarkentava kysymys: Näkyykö 'DNS lookup failed'-virheilmoitus selaimessa?\n\n     1) Kyllä näkyy.\n     2) Ei näy.\n     3) Palaa edelliseen valikkoon.")
            ongelmanTarkennettuVastaus = input("\n  Valitse sopivin vaihtoehto vastaamalla numerolla: ")
    
            if (ongelmanTarkennettuVastaus == "1"):
                dnsLookupFailed("wlan")
                break
            elif (ongelmanTarkennettuVastaus == "2"):
                selainEiToimi("wlan")
                break
            else:
                nav_WLAN()
                break

        elif (ongelmanValinta == 3):
            verkkosivuEiLöydy("wlan")
            break
        elif (ongelmanValinta == 4):
            print("\n  Sinulla on siis muu yhteysongelma. Valitettavasti ohjelmamme vaatii päivittämistä, jotta voisimme auttaa muissa kuin edellä esitellyissä ongelmatilanteissa.\n\n  1) Haluatko palata MENU-osioon?\n  2) Haluatko lopettaa ohjelman? Paina mitä tahansa näppäintä.")
            jatko = input("\n  Valitse sopivin vaihtoehto antamalla numero: ")

            if (jatko == "1"):
                nav_WLAN()
                break
            else:
                print("\n  Ohjelma suljetaan.\n")
                time.sleep(2)
                break

            time.sleep(4)
            break
        elif (ongelmanValinta == 5):
            tietoa_WLAN()
            break
        elif (ongelmanValinta == 6):
            tietoturva_WLAN()
            break
        elif (ongelmanValinta == 7):
            print("\n  Ohjelma suljetaan.")
            time.sleep(2)
    
        elif (ongelmanValinta > 7):
            print("\n  Valitse numerovaihtoehdoista 1-7.\n")
            continue
        i += 1


# Valinnan läpikäynti jokaisen funktion sisällä, WLAN-verkko

def valinta_wlan(määrä, ratkaisut, protokolla, ongelman_nimi):
    while (True):

        oletuksenaNumero = None

        while (oletuksenaNumero == None):
            print("\n  1) Haluatko RATKAISUEHDOTUKSIA "  + ongelman_nimi + "ongelmaasi?\n  2) Haluatko tietoa PROTOKOLLISTA, jotka usein vaikuttavat tämänkaltaisten yhteysongelmien taustalla?\n  3) Haluatko palata MENU-osioon?")
            valinta = input("\n  Valitse sopivin vaihtoehto vastaamalla numerolla: ")
            try:
                oletuksenaNumero = int(valinta)
            except:
                print("\n  Ilmoita vastaus numerona.")

        valinta = int(valinta)
        
        if (valinta == 1):
            ratkaisuEhdotukset_listaus(määrä, ratkaisut, "wlan")
            time.sleep(1)
            break           
        elif (valinta == 2 and protokolla == "Win10"):
            tietoa_protokollista_Win10("wlan")
        elif (valinta == 2 and protokolla == "selain"):
            tietoa_protokollista_selain("wlan")
        elif (valinta == 2 and protokolla == "yhteysPätkii"):
            tietoa_protokollista_yhteysongelmat("wlan")
        elif (valinta == 2 and protokolla == "dns_lookup_failed"):
            tietoa_protokollista_dnsLookUpFailed()
        elif (valinta == 3):
            nav_WLAN()
            break
        else:
            print("\n  Valitse vaihtoehto numeroista 1-3.")


# Listaa järjestyksessä kaikki ratkaisuehdotukset WLAN- ja Ethernet-verkoille

def ratkaisuEhdotukset_listaus(määrä, ratkaisut, wlanVaiEth):
    print(ratkaisut["1"])
    i = 2
    
    while (True and i <= määrä):

        if (i == määrä and wlanVaiEth == "wlan"):
            print("\n  Tässä olivat kaikki ratkaisuehdotuksemme tähän ongelmaan.\n  1) Haluatko palata MENU-osioon?\n  2) Haluatko lopettaa ohjelman? Paina mitä tahansa näppäintä.")
            jatko = input("\n  Vastaukseni: ")

            if (jatko == "1"):
                nav_WLAN()
                break
            else:
                print("\n  Ohjelma suljetaan.\n")
                time.sleep(2)
                break


        if (i == määrä and wlanVaiEth == "eth"):
            print("\n  Tässä olivat kaikki ratkaisuehdotuksemme tähän ongelmaan.\n  1) Haluatko palata MENU-osioon?\n  2) Haluatko lopettaa ohjelman? Paina mitä tahansa näppäintä.")
            jatko = input("\n  Vastaukseni: ")

            if (jatko == "1"):
                nav_Ethernet()
                break
            else:
                print("\n  Ohjelma suljetaan.\n")
                time.sleep(2)
                break

        print("  Kun olet kokeillut esitettyä ratkaisuehdotusta, kerrotko ratkesiko ongelma?\n  1) KYLLÄ, ongelma ratkesi ja ohjelman voi samantien lopettaa. \n  2) EI, ongelma ei ratkennut, tarvitsen lisää ratkaisuehdotuksia.\n  3) Palaa MENU-valikkoon.\n")
        onnistuikoRatkaisuehdotus = input("\n  Valitse sopivin vaihtoehto vastaamalla numerolla: ")

        if (onnistuikoRatkaisuehdotus == "1"):
            print("\n  Hieno homma! Suljemme nyt ohjelman, kun ongelma kerran ratkesi :)")
            time.sleep(2)
            break
        elif (i == määrä and wlanVaiEth == "wlan"):
            print("\n  Ratkaisua ei valitettavasti löydy. Päivityksen myötä voimme kenties ratkaista ongelmasi. Palataan WLAN 'menu'-valikkoon.\n")
            nav_WLAN()
            break
        elif (i == määrä and wlanVaiEth == "eth"):
            print("\n  Ratkaisua ei valitettavasti löydy. Päivityksen myötä voimme kenties ratkaista ongelmasi. Palataan Ethernet 'menu'-valikkoon.\n")
            nav_Ethernet()
            break
        elif (onnistuikoRatkaisuehdotus == "3" and wlanVaiEth == "wlan"):
            nav_WLAN()
            break
        elif (onnistuikoRatkaisuehdotus == "3" and wlanVaiEth == "eth"):
            nav_Ethernet()
            break
        elif (onnistuikoRatkaisuehdotus == "2"):
            print(ratkaisut[str(i)])
        else:
            print("\n  Anna vastaus numerona. \n")
            continue
        i+= 1


def kuva_wlanReititin():
    print(r""" 
                                                                                              ~                   ~
                                                                                          ~     ~~      ~          ~~     ~
                                                                                             ~~   ~~         ~   ~~  ~~
                                                                                        ~   ~~  >   ~~         ~~   <  ~~  
                                                                                                |                   |
                                                                                                |                   |
                                                                                           _____|___________________|____
                                                                                       __""/////|//////////\\\\\\\\\|\\\\""__                                                      
                                                                                     _//////////|//////////\\\\\\\\\|\\\\\\\\\_
                                                                                    //////////////////  _      \\\\\\\\\\\\\\\\\              
                                                                                   /_///////////////// |_| __ | \\\\\\\\\\\\\\\\\                 
                                                                                   | \__////////////// | \    | \\\\\\\\\\\\\\__/|
                                                                                   |||||""___//////////////\\\\\\\\\\\\\\___""||||   
                                                                                   ||||||||||""________________________""|||||||||     
                                                                                    \__|||||||||||||||||||||||||||||||||||||||__/
                                                                                       ""___|||||||||WLAN-Router|||||||||___""
                                                                                            ""_________________________""
                        
    
    """)


# Tietoa WLAN-verkosta

def tietoa_WLAN():
    
    tyhjennäRuutu()
    
    otsikko("Tietoa WLAN-verkosta", 100)

    kuva_wlanReititin()

    print("\nLangattomat verkot pohjautuvat IEEE:n standardeihin ja voidaan luokitella karkeasti neljään tyyppiin: WPAN, WLAN, WMAN ja WWAN. \
WLAN eli Wireless LAN:it käyttävät lähettimiä keskisuurissa verkoissa (noin 100 metrin kattavuus), kuten SOHO:issa, koti- tai kampusolosuhteissa ja ne pohjautuvat IEEE:n 802.11 standardiin käyttäen pääasiassa 2.4- tai 5-GHz radiotaajuuksia. \
WLAN-verkon tärkeimpiä langattoman verkon komponentteja ovat: Langaton verkkokortti tai langaton USB adapteri, langaton reititin, langaton tukiasema ja antennit. \
Langattoman verkon toimimiseksi tarvitaan vähintään kaksi laitetta, joilla on radiolähetin ja -vastaanotin viritettynä samalle radiotaajuudelle. \
Eli toisin sanoen päätelaitteella tulee olla langaton verkkokortti (wireless NIC) ja sen vastaparina langaton reititin tai tukiasema (AP).\n\n\
  Ohessa lyhyt yhteenveto WLAN-verkosta ja sen poikkeuksista Ethernet-verkkoon nähden:\n\n\
    - WLAN-laitteet noudattavat IEEE 802.11 standardeja.\n\
    - WLAN-laitteet käyttävät mikro- ja radioaaltoja datan lähetykseen.\n\
    - Radioaallot liikkuvat ilmassa, joten ne ovat alttiita erilaisille häiriöille.\n\
    - WLAN-yhtydet ei tarvitse radioaaltojen ansiosta fyysisiä liitäntöjä, kuten kaapeleita toimiakseen.\n\
    - Käyttää ns. half-duplex tekniikkaa, joten kommunikaatio laitteiden välillä tapahtuu 'vuorottelu'-periaatteella.\n\
    - Käyttää CSMA/CA tekniikkaa, jotta verkkoliikenne radioaalloilla olisi sujuvaa.\n\n")

    i = 0
    while (i < 1):
    
        valinta = input("Jos haluat lopettaa ohjelman, paina 'q'-näppäintä ja jos puolestaan haluat jatkaa, paina mitä tahansa muuta nappia palataksesi MENU-osioon. ")
        
        if (valinta == "q" or valinta == "Q"):
            break
        else:
            nav_WLAN()
        i+= 1


def kuva_OSI_malli():
    print(r"""
                                                                   __________________________           ___________________________
                                                                  |>                        <|         |>                         <|
                                                                  |>      - OSI-malli -     <|         |> - Protokollaesimerkki - <|
                                                                  |>________________________<|         |>_________________________<|   
                                                                  |                          |         |                           |
                                                                  |   7. Sovelluskerros      |         |    7. WWW-selain          |
                                                                  |   6. Esitystapakerros    |         |    6. HTML-sivut          |
                                                                  |   5. Istuntokerros       |         |    5. HTTP                |
                                                                  |   4. Kuljetuskerros      |         |    4. TCP 80              |
                                                                  |   3. Verkkokerros        |         |    3. IPv4                |
                                                                  |   2. Siirtokerros        |         |    2. Ethernet            |
                                                                  |   1. Fyysinen kerros     |         |    1. STP-kaapelit yms.   |
                                                                  |__________________________|         |___________________________|
    """)


# Tietoa protokollista WLAN-verkossa

def tietoa_protokollista_yhteysongelmat(wlanVaiEthernet):
    
    tyhjennäRuutu()
    
    otsikko("Protokollat", 150)

    if (wlanVaiEthernet == "wlan"):
        teksti_eth = ""
        teksti_eth2 = ""
        teksti_wlan = "DHCPv4 ja DHCPv6, DNS, IPv4 ja IPv6, NAT, TCP, UDP ja WLAN"
        teksti_wlan2 = "WLAN eli Wireless Local Area Network: Tämän IEEE 802.11-standardin mukaisen protokollan avulla määritellään langattoman lähiverkon rakenne; minkälaisia laitteita tulee käyttää, miten signalointi radioaalloilla toteutetaan jne. WLAN-lähiverkon laitteet yhdistyvät tyypillisesti langattomaan reitittimeen, joka reitittää IP-paketteja eteenpäin, huolehtien kommunikaatiosta lähiverkon ulkopuolelle. Koska WLAN-verkossa signaalit liikkuvat radioaaltoina, yhteys voi pätkiä mm. fyysisten seikkojen, kuten signaalien esteenä olevien betoniseinien, vuoksi.\n"
    if (wlanVaiEthernet == "eth"):
        teksti_wlan = ""
        teksti_wlan2 = ""
        teksti_eth = "DHCPv4 ja DHCPv6, DNS, Ethernet, IPv4 ja IPv6, NAT, TCP ja UDP"
        teksti_eth2 = "Ethernet: Tämä on nykyisin käytetyin langallinen lähiverkkoratkaisu sen tehokkuuden ansiosta. IEEE-organisaatio standardoi eri Ethernet-tekniikoita, päättäen signaloinnista ja siitä, mitä fyysisiä ratkaisuja tämän tapaisessa lähiverkossa käytetään.\n\n"


    print("\nVerkkoyhteyden taustalla vaikuttavat monet protokollat ja yhteyden pätkimisen syytä ei ole välttämättä helppoa heti osoittaa, vaan tarvitaan tarkempaa vianmääritystä. Vika voi olla:\n\n\
  - Sovellustasolla: kuormittunut verkko, jonkin päivityken jälkeen aiheutunut bugi, hidas DNS-palvelin tai ISP:n reititysongelmat.\n\
  - Konfiguraatio eli asetusten tasolla: huonosti konfiguroitu langaton WLAN-adapteri, päivittämätön reititin, päivittämätön WLAN-ohjain tai lentotila päällä.\n\
  - Laitteistotasolla: irronneet liitännät, rikkinäinen reititin tai virranhallinnan ongelmat.\n\
  - Yleisiä protokollia, jotka voivat vaikuttaa yhteysongelmien taustalla: " + teksti_eth + "" + teksti_wlan + ".\n\n\
DHCPv4 ja DHCPv6 eli Dynamic Host Configuration Protocol (versiot 4 ja 6): Nämä protokollat määrittävät automaattisesti päätelaitteelle IP-osoitetiedot, jotta tietokone voi kommunikoida muiden laitteiden kanssa internet-verkossa. Jos tietokone ei saa IP-osoitetietoja tai ne ovat vajaavaisia, verkkoyhteys ei toimi oikein. DHCPv4 antaa IP-tiedot IPv4 verkon laitteille ja DHCPv6 puolestaan IPv6 verkkoa käyttäville laitteille.\n\n\
DNS eli Domain Name System: Tämä ns. nimipalvelujärjestelmä on oleellinen koko internetin toiminnalle, sillä DNS muuntaa verkko-osoitteet IP-osoitteiksi ja toisinpäin suuren DNS-serveriverkoston avulla. Ilman tätä järjestelmää ihmisten täytyisi muistaa verkko-osoitteet binäärimuodossa, mikä olisikin huomattavasti hankalampaa kuin saada kirjoittaa verkko-osoitteet niminä. \
Mikäli DNS-servereiden toiminnassa on vikaa tai tietokoneelle on asennettu väärät DNS-asetukset, verkkoyhteys ei toimi toivotusti kun verkkosivut eivät löydy, yhteys katkeilee tai pätkii.\n\n\
" + teksti_eth2 + "\
IPv4 ja IPv6 eli Internet Protocol (versiot 4 ja 6): IP-protokollan ansiosta tietokoneen lähettämät viestit voidaan verkossa lähettää ns. IP-paketteina, joihin on merkitty bitteinä mm. lähettävän ja vastaanottavan laitteen osoitetiedot, joko IPv4- tai IPv6-osoitteina. IP-osoite on kuin tietokoneen postiosoite, johon muut verkon laitteet voivat lähettää viestejä. Mikäli IP-osoite on konfiguroitu väärin, verkkoyhteys ei varmasti toimi.\n\n\
NAT eli Network Address Translation: Tämä protokolla on kehitetty, koska IPv4-osoitteet (toisin kuin IPv6) ovat maailmanlaajuisesti lopussa ja niitä pitää verkossa säästää. IPv4-osoitteet voivat olla ns. julkisia (käytetään internetissä) tai yksityisiä (käytetään vain lähiverkossa) ja tämän osoitteenmuunnos protokollan avulla julkisesti liikennöityjä IP-osoitteita piilotetaan tai säästetään IPv4-verkossa. \
Käytännössä siis NAT:n avulla useampi tietokone jakaa yhden IP-osoitteen keskenään. NAT aiheuttaa kuitenkin monia ongelmia erilaisten kaksisuuntaisten sovellusten takia, kuten verkkoyhteyden katkeamista tai viivettä.\n\n\
TCP eli Transmission Control Protocol: Tämän protokollan avulla tietokoneet voivat luotettavasti kommunikoida keskenään ns. 'three-way-handshaken' ja eri tietoverkon hallintamekanismien ansiosta. TCP pitää huolen siitä, että IP-paketit saapuvat perille oikeassa järjestyksessä vastaanottavalle laitteelle. Monet protokollat kuljetetaankin TCP:n 'päällä' ja jos TCP ei toimi oikein tai se on vaadittuun kommunikaatioon liian hidas, verkkoyhteys todennäköisesti tulee pätkimään tai kaatumaan.\n\n\
UDP eli User Datagram Protocol: Tämä protokolla on vaihtoehto TCP:lle mahdollistaen nopeamman muttei yhtä luotettavan tiedonsiirron. UDP on kätevä mm. DNS-pyyntöjen lähetyksessä, verkkopeleissä ja muussa reaaliaikaisessa datan lähetyksessä, joka on herkkä viiveelle. Vaikka UDP on TCP:tä nopeampi, verkkoyhteys voi siltikin pätkiä, jos verkko on esimerkiksi kuormittunut.\n\n\
" + teksti_wlan2)

    input(" --- Paina 'Enter'-nappia jatkaaksesi lukemista ---  ")
    print ("\033[A                             \033[A") #poistaa edellisen input-lauseen näytöltä ja siirtää kursorin rivin alkuun

    print("Protokollien ymmärtäminen auttaa verkkoyhteyden ongelmien paikantamisessa sillä tietokoneet hahmottavat verkon niiden avulla. Protokollia on puolestaan esimerkiksi yhdessä ainoassa tietokoneen lähettämässä viestissä tyypillisesti useita ja ihmiselle onkin haastava käsittää tällaista monimutkaisuutta. Siksi on luotu erilaisia malleja valmistajien ja eri organisaatioiden toimesta, jotka auttavat protokollien hahmottamisessa ja merkityksessä tietoverkkoliikenteelle.\n\n\
Alla kuva ns. OSI-mallista, jota käytetään nykyisin yleisesti kuvaamaan verkkoliikenteen kerroksellisuutta. Yksi tietokoneen lähettämä viesti usein siis sisältää protokollia kaikista näistä OSI-mallin kerroksista, jotta yhteys olisi toiminnallinen ylipäätään. Toinen suosittu verkkoprotokollia kuvaava malli tämän rinnalla on TCP/IP-malli.")

    kuva_OSI_malli()

# Tietoa protokollista, jotka liittyvät selaimen yhteysongelmiin

def tietoa_protokollista_selain(wlanVaiEthernet):
    
    tyhjennäRuutu()

    otsikko("Protokollat", 150)

    if (wlanVaiEthernet == "wlan"):
        teksti_eth = ""
        teksti_eth2 = ""
        teksti_wlan = "HTTP ja HTTPS, DHCPv4 ja DHCPv6, DNS, ICMPv4 ja ICMPv6, IPv4 ja IPv6, NAT, TCP, UDP ja WLAN"
        teksti_wlan2 = "WLAN eli Wireless Local Area Network: Tämän IEEE 802.11-standardin mukaisen protokollan avulla määritellään langattoman lähiverkon rakenne; minkälaisia laitteita tulee käyttää, miten signalointi radioaalloilla toteutetaan jne. WLAN-lähiverkon laitteet yhdistyvät tyypillisesti langattomaan reitittimeen, joka reitittää IP-paketteja eteenpäin, huolehtien kommunikaatiosta lähiverkon ulkopuolelle. Koska WLAN-verkossa signaalit liikkuvat radioaaltoina, yhteys voi pätkiä mm. fyysisten seikkojen, kuten signaalien esteenä olevien betoniseinien, vuoksi.\n"
    if (wlanVaiEthernet == "eth"):
        teksti_wlan = ""
        teksti_wlan2 = ""
        teksti_eth = "HTTP, HTTPS, DHCPv4 ja DHCPv6, DNS, Ethernet, ICMPv4 ja ICMPv6, IPv4 ja IPv6, NAT, TCP ja UDP"
        teksti_eth2 = "Ethernet: Tämä on nykyisin käytetyin langallinen lähiverkkoratkaisu sen tehokkuuden ansiosta. IEEE-organisaatio standardoi eri Ethernet-tekniikoita, päättäen signaloinnista ja siitä, mitä fyysisiä ratkaisuja tämän tapaisessa lähiverkossa käytetään.\n\n"

    print("\nSelaimen toiminnan taustalla vaikuttavat monet protokollat ja ongelmat selaimissa ovat suhteellisen yleisiä. Vikaa voi olla esimerkiksi:\n\n\
  - Sovellustasolla: jonkin tietyn ohjelman päivitys (esim. sen myötä asetukset ovat vaihtuneet ja linkit ohjautuvat päivityksen jälkeen väärin), käyttöjärjestelmän päivitys tai päivittämätön selainversio.\n\
  - Konfiguraatio eli asetusten tasolla: väärät selaimen tai liitännäisten asetukset (jolloin Windows 10 ei esim. löydä oletusselainta), muutokset tai korruptoitunut data ns. registry keys-tiedoissa.\n\
  - Yleisiä protokollia, jotka voivat vaikuttaa web-sivujen taustalla: " + teksti_eth + "" + teksti_wlan + ".\n\n\
HTTP eli Hypertext Transfer Protocol ja HTTPS eli HTTP Secure: Tätä protokollaa käyttävät eritoten selaimet ja web-palvelimet keskinäiseen tiedonsiirtoon. Asiakasohjelma (esim. selain) pyrkii avaamaan TCP-yhteyden web-serverille ja tekee tälle palvelupyynnön esimerkiksi hakeakseen tietyn websivun. \
Webpalvelin lähettää selaimelle vastauksen, joka sisältää usein HTML-sivun ja jonka selain sitten tulkitsee sekä näyttää sisältöineen (kuvaa, ääntä tms.) käyttäjälle selainikkunassa. Mikäli HTTP-viestit eivät kulje selaimelta palvelimelle tai toisinpäin oikealla tavalla, selain ei myöskään käyttäydy oikein. \
HTTPS puolestaan on HTTP-protokollan ja TLS- ja SSL-protokollien yhdistelmä, joka toimii HTTP-protokollan periaatteella, mutta tieto on kryptattu eli salattu matkalla palvelimelta toiselle SSL:n ja TLS:n avulla.\n\n\
DHCPv4 ja DHCPv6 eli Dynamic Host Configuration Protocol (versiot 4 ja 6): Nämä protokollat määrittävät automaattisesti päätelaitteelle IP-osoitetiedot, jotta tietokone voi kommunikoida muiden laitteiden kanssa internet-verkossa. Jos tietokone ei saa IP-osoitetietoja tai ne ovat vajaavaisia, selain ei toimi oikein.\n\n\
DNS eli Domain Name System: Tämä ns. nimipalvelujärjestelmä on oleellinen koko internetin toiminnalle, sillä DNS muuntaa verkko-osoitteet IP-osoitteiksi ja toisinpäin suuren DNS-serveriverkoston avulla. Ilman tätä järjestelmää ihmisten täytyisi muistaa verkko-osoitteet binäärimuodossa, mikä olisikin huomattavasti hankalampaa kuin saada kirjoittaa verkko-osoitteet niminä. \
Mikäli DNS-servereiden toiminnassa on vikaa tai tietokoneelle on asennettu väärät DNS-asetukset, selain ei toimi toivotusti kun verkkosivut eivät löydy, yhteys katkeilee tai mahdollisesti pätkii.\n\n\
" + teksti_eth2 + "\
ICMPv4 ja ICMPv6 eli Internet Control Message Protocol (versio 4 ja 6): Tämän protokollan avulla verkkolaitteet (esim. reitittimet) lähettävät virheviestejä ja tietoa IP-osoitetietojen toimivuudesta laitteiden välillä. ICMP-protokollaa käytetäänkin verkon diagnoimisessa ja ylläpitotehtävissä. Tästä protokollasta on IPv4 ja IPv6 verkkoihin omat versionsa.\n\n\
IPv4 ja IPv6 eli Internet Protocol (versiot 4 ja 6): IP-protokollan ansiosta tietokoneen lähettämät viestit voidaan verkossa lähettää ns. IP-paketteina, joihin on merkitty bitteinä mm. lähettävän ja vastaanottavan laitteen osoitetiedot, joko IPv4- tai IPv6-osoitteina. IP-osoite on kuin tietokoneen postiosoite, johon muut verkon laitteet voivat lähettää viestejä. Mikäli IP-osoite on konfiguroitu väärin, verkkoyhteys ei varmasti toimi.\n\n\
NAT eli Network Address Translation: Tämä protokolla on kehitetty, koska IPv4-osoitteet (toisin kuin IPv6) ovat maailmanlaajuisesti lopussa ja niitä pitää verkossa säästää. IPv4-osoitteet voivat olla ns. julkisia (käytetään internetissä) tai yksityisiä (käytetään vain lähiverkossa) ja tämän osoitteenmuunnos protokollan avulla julkisesti liikennöityjä IP-osoitteita piilotetaan tai säästetään IPv4-verkossa. \
Käytännössä siis NAT:n avulla useampi tietokone jakaa yhden IP-osoitteen keskenään. NAT aiheuttaa kuitenkin monia ongelmia erilaisten kaksisuuntaisten sovellusten takia, kuten verkkoyhteyden katkeamista tai viivettä.\n\n\
TCP eli Transmission Control Protocol: Tämän protokollan avulla tietokoneet voivat luotettavasti kommunikoida keskenään ns. 'three-way-handshaken' ja eri tietoverkon hallintamekanismien ansiosta. TCP pitää huolen siitä, että IP-paketit saapuvat perille oikeassa järjestyksessä vastaanottavalle laitteelle. Monet protokollat kuljetetaankin TCP:n 'päällä' ja jos TCP ei toimi oikein tai se on vaadittuun kommunikaatioon liian hidas, verkkoyhteys todennäköisesti tulee pätkimään tai kaatumaan.\n\n\
UDP eli User Datagram Protocol: Tämä protokolla on vaihtoehto TCP:lle mahdollistaen nopeamman muttei yhtä luotettavan tiedonsiirron. UDP on kätevä mm. DNS-pyyntöjen lähetyksessä, verkkopeleissä ja muussa reaaliaikaisessa datan lähetyksessä, joka on herkkä viiveelle. Vaikka UDP on TCP:tä nopeampi, verkkoyhteys voi siltikin pätkiä, jos verkko on esimerkiksi kuormittunut.\n\n\
" + teksti_wlan2)
    
    input(" --- Paina 'Enter'-nappia jatkaaksesi lukemista ---  ")
    print ("\033[A                             \033[A") #poistaa edellisen input-lauseen näytöltä ja siirtää kursorin rivin alkuun

    print("Protokollien ymmärtäminen auttaa verkkoyhteyden ongelmien paikantamisessa sillä tietokoneet hahmottavat verkon niiden avulla. Protokollia on puolestaan esimerkiksi yhdessä ainoassa tietokoneen lähettämässä viestissä tyypillisesti useita ja ihmiselle onkin haastava käsittää tällaista monimutkaisuutta. Siksi on luotu erilaisia malleja valmistajien ja eri organisaatioiden toimesta, jotka auttavat protokollien hahmottamisessa ja merkityksessä tietoverkkoliikenteelle.\n\n\
Alla kuva ns. OSI-mallista, jota käytetään nykyisin yleisesti kuvaamaan verkkoliikenteen kerroksellisuutta. Yksi tietokoneen lähettämä viesti usein siis sisältää protokollia kaikista näistä OSI-mallin kerroksista, jotta yhteys olisi toiminnallinen ylipäätään. Toinen suosittu verkkoprotokollia kuvaava malli tämän rinnalla on TCP/IP-malli.")
    
    kuva_OSI_malli()


# Tietoa protokollista, jotka liittyvät Windows 10 päivityksen jälkeisiin ongelmiin

def tietoa_protokollista_Win10(wlanVaiEthernet):
    
    tyhjennäRuutu()

    otsikko("Protokollat", 150)

    if (wlanVaiEthernet == "wlan"):
        teksti_eth = ""
        teksti_eth2 = ""
        teksti_wlan = "ARP, Bluetooth ja WLAN"
        teksti_wlan2 = "WLAN eli Wireless Local Area Network: Tämän IEEE 802.11-standardin mukaisen protokollan avulla määritellään langattoman lähiverkon rakenne; minkälaisia laitteita tulee käyttää, miten signalointi radioaalloilla toteutetaan jne. WLAN-lähiverkon laitteet yhdistyvät tyypillisesti langattomaan reitittimeen, joka reitittää IP-paketteja eteenpäin, huolehtien kommunikaatiosta lähiverkon ulkopuolelle. Koska WLAN-verkossa signaalit liikkuvat radioaaltoina, yhteys voi pätkiä mm. fyysisten seikkojen, kuten signaalien esteenä olevien betoniseinien, vuoksi.\n"
        teksti_bluetooth = "Bluetooth: Tämän PAN-verkossa (Personal Area Network) käytetyn IEEE 802.15-standardin avulla määritellään lyhyen kantaman (n. 1-100 metriä), langaton tiedonsiirtotekniikka. Bluetoothin avulla laitteet voivat kommunikoida keskenään lähietäisyydellä ilman kaapeleita ja se koostuu kolmesta osasta: \
radio-osa (Bluetooth-radio), radiolinkin hallintaosasta (link controller) ja yhteyden hallinnasta (link manager). Bluetooth-yhteyden tietoturvaa voidaan parantaa autentikoinnilla ja tiedon salaamisella. Viallinen verkkokortti tai sen ohjaimen asetukset vaikuttavat Bluetooth-protokollan toimivuuteen ja sitä myötä myös verkkoyhteyteen.\n\n"
    if (wlanVaiEthernet == "eth"):
        teksti_wlan = ""
        teksti_wlan2 = ""
        teksti_bluetooth = ""
        teksti_eth = "ARP ja Ethernet"
        teksti_eth2 = "Ethernet: Tämä on nykyisin käytetyin langallinen lähiverkkoratkaisu sen tehokkuuden ansiosta. IEEE-organisaatio standardoi eri Ethernet-tekniikoita, päättäen signaloinnista ja siitä, mitä fyysisiä ratkaisuja tämän tapaisessa lähiverkossa käytetään.\n\n"

    print("\nWindows 10 päivitykset vaikuttavat usein tietokoneen verkkokortin (verkkosovittimen) toimintaan. Verkkokortti on siru, joka asennetaan tietokoneeseen jotta se voi kommunikoida verkossa. Kun käyttäjä esimerkiksi tekee http-pyyntöä saadakseen verkkosivun web-palvelimelta, \
tietokone lähettää luodun http-pyynnön verkkosovittimelle, joka muuttaa tiedon elektronisiksi impulsseiksi ja lähettää verkkoon web-palvelimelle saadakseen aikanaan vastauksen. Windows 10 päivityksen jälkeen verkkoviat voivatkin usein olla:\n\n\
  - Konfiguraatio eli asetusten tasolla: verkkosovittimen ohjainten asetukset.\n\
  - Laitteistotasolla: viallinen verkkokortti.\n\
  - Taustalla vaikuttavia protokollia ovat esimerkiksi: " +teksti_eth + "" + teksti_wlan + ".\n\n\
ARP eli Address Resolution Protocol: Verkossa tietokoneet kommunikoivat toistensa kanssa IP-osoitteiden avulla kaukaisistakin verkoista käsin. Jotta yksittäinen tietokone kuitenkin pystyttäisiin tunnistamaan lähiverkossa, niillä on uniikki, ns. fyysinen MAC-osoite. \
ARP pyrkii selvittämään lähiverkossa viestiä vastaanottavan laitteen MAC-osoitteen. Eli jos tietokoneella on tiedossa tietyn laitteen IP-osoite, muttei tämän MAC-osoitetta, se käyttää ARP-protokollaa MAC-osoitteen selvittämiseen. Osoitteen selvittyä lähettävä tietokone sitten lähettää viestin vastaanottavalle päätelaitteelle. \
Tietokoneet keräävät ns. ARP-tauluun tietoja IP-osoitteista ja niitä vastaavista MAC-osoitteista, jotta ne osaisivat ohjata viestejä oikealle päätelaitteelle lähiverkossaan. Viallinen verkkokortti voi mm. lähettää ARP-viestejä hallitsemattomasti tai olla vastaanottamatta niitä, jolloin verkkoyhteys ei toimi.\n\n\
" + teksti_eth2 + "\
" + teksti_bluetooth + "\
" + teksti_wlan2)

    input(" --- Paina 'Enter'-nappia jatkaaksesi lukemista ---  ")
    print ("\033[A                             \033[A") #poistaa edellisen input-lauseen näytöltä ja siirtää kursorin rivin alkuun

    print("Protokollien ymmärtäminen auttaa verkkoyhteyden ongelmien paikantamisessa sillä tietokoneet hahmottavat verkon niiden avulla. Protokollia on puolestaan esimerkiksi yhdessä ainoassa tietokoneen lähettämässä viestissä tyypillisesti useita ja ihmiselle onkin haastava käsittää tällaista monimutkaisuutta. Siksi on luotu erilaisia malleja valmistajien ja eri organisaatioiden toimesta, jotka auttavat protokollien hahmottamisessa ja merkityksessä tietoverkkoliikenteelle.\n\n\
Alla kuva ns. OSI-mallista, jota käytetään nykyisin yleisesti kuvaamaan verkkoliikenteen kerroksellisuutta. Yksi tietokoneen lähettämä viesti usein siis sisältää protokollia kaikista näistä OSI-mallin kerroksista, jotta yhteys olisi toiminnallinen ylipäätään. Toinen suosittu verkkoprotokollia kuvaava malli tämän rinnalla on TCP/IP-malli.")
    
    kuva_OSI_malli()


def kuva_dns_hierarkia():
    print(r"""
                                                                                                ____
                                                                                               /___/|           
                                                                                               | ..||                   ROOT DOMAIN (".")
                                                                                               |-__|/
                                                                                            /          \
                                                                                           /     |      \ 
                                                                                          /      |       \
                                                                                    ____         |          ____
                                                                                   /___/|       ____       /___/|
                                                                                   |...||      /___/|      |-  ||       TOP-LEVEL-DOMAINS (esim. ".com", ".mil", ".org" tai ".edu")
                                                                                   |___|/      |...||      |_..|/
                                                                                 /             |___|/             \
                                                                                /    |                      |      \
                                                                               /     |           |          |       \
                                                                         ____        |           |          |          ____
                                                                        /___/|     ____         ____       ____       /___/|        SECOND-LEVEL DOMAINS (esim. "nasa", "tryhackme" tai "google")
                                                                        |   ||    /___/|       /___/|     /___/|      |...||
                                                                        |___|/    | ..||       |...||     |. .||      |___|/
                                                                                  |___|/       |___|/     |_-_|/
    
    """)

# Tietoa DNS Lookup Failed-ilmoituksen protokollista

def tietoa_protokollista_dnsLookUpFailed():

    tyhjennäRuutu()

    otsikko("DNS-protokolla   ja   -hierarkia", 70)

    kuva_dns_hierarkia()

    print("\nDNS eli Domain Name System-protokolla määrittää verkko-osoitteelle sitä vastaavan IP-osoitteen. Eli kun kirjoitat selaimen URL-osoitekenttään verkko-osoitteeksi esim. hs.fi, DNS etsii DNS-palvelimien verkoston avulla hs.fi-nimelle sitä vastaavan IP-osoitteen. \
Tämän jälkeen selain osaa lähettää pyynnön oikealle web-serverille hakeakseen halutun sivuston. DNS onkin internetin toimivuuden kannalta yksi olennaisimpia protokollia, sillä ihmiset eivät pysty muistamaan ulkoa kaikkien vieraileviensa verkkosivujen IP-osoitteita. Mikäli siis tietokoneeseen on esimerkiksi asennettu väärä DNS-serverin osoite, joka ei ole käytössä, eivät verkkosivut lataudu.\n")

    input(" --- Paina 'Enter'-nappia jatkaaksesi lukemista ---  ")
    print ("\033[A                             \033[A") #poistaa edellisen input-lauseen näytöltä ja siirtää kursorin rivin alkuun

    print("DNS-palvelimien verkosto koostuu ns. DNS-hierarkiasta, jossa on eri tasoisia DNS-servereitä: Root Domain-serverit, Top-Level Domain-serverit (jaetaan gTLD-servereihin eli Generic Top Level ja ccTLD-servereihin eli Country Code Top Level Domain) ja Second-Level Domain-serverit (SLD). Root Domain-servereitä on maailmassa 13 kappaletta ja ne ovat koko systeemin selkäranka (näkyy URL-osoitteessa '.'-symbolina). \
TLD on oikeanpuolimmaisin osa verkko-osoitteesta (domain name) eli esim. tryhackme.com osoitteesta '.com' osa. Samaisesta osoitteesta 'tryhackme' olisi puolestaan SLD-osa. Verkko-osoitteessa on myös ns. subdomain, joka on vasemmalla puolella SLD:tä, erotettuna pisteellä tästä. Esim. verkko-osoitteessa admin.tryhackme.com subdomain-osa olisi 'admin'-osa. Useampaa subdomain-osaa voidaan käyttää verkko-osoitteessa \
jotta voidaan luoda pitempiä nimiä, tyyliin: jupiter.servers.tryhackme.com. Verkko-osoitetta rekisteröitäessä verkko-osoitteen nimen pituus saa olla 253 merkkiä tai vähemmän, mutta subdomain-osia siinä saa olla rajattomasti.\n\nDNS-hierarkia ei ole pelkkiä verkkosivuja varten, sillä sen tietokannoissa on paljon muitakin rekistereitä, yleisimpiä näistä ovat: A-, AAAA-, CNAME-, MX- ja TXT-rekisterit. A-rekisteristä selviää IPv4-osoitteet ja AAAA-rekisteristä \
IPv6-osoitteet. CNAME-rekisteristä selviää muut verkkotunnukset, esim. jos TryHackMe-yrityksen online-verkkokaupalla on subdomain-nimenä 'store.tryhackme.com', joka palauttaa CNAME-rekisteristä rekisterin ('canonical name') 'shops.shopify.com', toinen DNS-pyyntö lähetettäisiin shops.shopify.com osoitteeseen IP-osoitteen selvittämiseksi. MX-rekisteristä selviää puolestaan servereiden osoitteet, jotka käsittelevät kysellyn verkkotunnuksen \
sähköpostitietoja. Esim. MX-reksiterin vastaus 'tryhackme-com'-osoitteelle voisi olla alt1.aspmx.l.google.com. Tämä on kätevä silloin, jos sähköpostiserveri kaatuu ja pitää lähettää sähköpostia varaserverille. TXT-rekisteristä selviää tietyn verkko-osoitteen omistaja ja se listaa myös servereitä, joilla on oikeus lähettää sähköposteja tietyn verkko-osoitteen nimissä. Komentokehotteessa nslookup-työkalu on loistava DNS-tietojen selvittämiseen. \
Komentokehotteessa perus nslookup-komennon voi tehdä kaavalla: nslookup --type=<pyynnön tyyppi> <verkko-osoite>, eli esim. nslookup --type=MX www.hs.fi. Tällöin pyydetään MX-rekisteristä tietoja, jotka liittyvät hs.fi-verkkosivuun.\n")

    input(" --- Paina 'Enter'-nappia jatkaaksesi ---  ")
    print ("\033[A                             \033[A") #poistaa edellisen input-lauseen näytöltä ja siirtää kursorin rivin alkuun


def kuva_yhteysPätkii():
    print(r"""                       
    
                                                                                                                                        Miksi WLAN-yhteys pätkii?!?
                                                                                                                                           ___________________
                                      .   .                                                                                               |  _______________  |
                                    __|___|__                                                                                             | |               | |
                                   |   R-1   |  ~~ ~~ ~~ ~~ ~~ ~~ . . . ~~ ~~ . . . ~~ ~~ ~~ .. ~~ ~~ . . . ~~ ~~ ~~ ~~ ~~ . . . ~~ ~~ ~~ | |               | |
                                   |_________|                                                                                            | |_______________| |
                                                                                                                                          |___________________|   
                                                                                                                                                |        |
                                                                                                                                               /__________\


    """)

# 'Verkkoyhteys on poikki tai pätkii'-osion ratkaisuehdotukset

def yhteysPätkii():
    
    tyhjennäRuutu()
    
    otsikko("WLAN-verkkoyhteys   katkeilee", 60)

    kuva_yhteysPätkii()

    ratkaisuEhdotukset = {"1": "\nEli verkkoyhteytesi siis pätkii. Kokeillaan muutamaa keinoa tämän korjaamiseksi.\n\
\n1. Tarkista reitittimesi fyysinen sijainti ja testaa sen taajuusasetusten toiminta.\nWLAN-verkossa signaalin pitää saada kulkea esteettä, jotta yhteys ei pätki. Varmista siis, että reititin tai WLAN-tukiasema ovat tarpeeksi lähellä tietokonettasi ja ettei näiden välissä ole fyysisiä esteitä. \
Voit myös kokeilla vaihtaa reitittimesi taajuutta 2.4 GHz:stä 5 GHz:n. Tee tämä avaamalla selain ja kirjoittamalla URL-kenttään reitittimen IP-osoite (reitittimen IP-osoite löytyy esim. seuraavasti: kirjoita työpöydältä löytyvään hakukenttään 'cmd', jolloin avautuu mustaruutuinen, ns. komentokehote -> \
kirjoita 'ipconfig' ja katso reitittimen IP-osoite Wireless LAN adapter Wi-Fi-kohdasta 'Default Gateway'-sanan jälkeen) -> anna käyttäjätunnus ja salasana -> vaihda taajuus 2.4 GHz:stä 5 GHz:n asetuksista). Jos sinulla on IoT-laitteita tai muita Wi-Fi-laitteita, jotka eivät ole tarpeellisessa käytössä, katkaise niistä yhteydet.\n",
"2": "\n2. Koita reitittimesi antaa jäähtyä sammuttamalla se hetkeksi.\nJos reititin tai modeemi ei pysty ylläpitämään yhteyttä tasaisesti, tarkista onko se ylikuumentunut. \
Jos on, sammuta se ja anna jäähtyä tai kokeile 'power cycling'-metodia (eli kytke virta pois irrottamalla virtajohto noin minuutiksi ja kytke uudestaan päälle). \
Tämä auttaa luomaan uuden yhteyden internet-palveluntarjoajaan.\n ",
"3": "\n3. Käytä vianmääritysohjelmaa (Network troubleshooter).\nVianmääritysohjelma auttaa diagnosoimaan yleisimpiä verkon ongelmia. Sitä voi käyttää klikkaamalla: \
aloitus (Start) -> asetukset (Settings) -> verkko ja internet (Network & Internet) -> tila (Status) -> valitse 'verkon vianmääritys' -> noudata ohjeita ja katso, korjautuuko ongelma.\n",
"4": "\n4. Tarkista internetpalveluntarjoajasi eli ISP:n ilmoitukset lähialueesi mahdollisista yhteysongelmista.\nYhteysongelmat voivat johtua palveluntarjoajasta ja onkin hyvä tarkastaa heidän ilmoitukset mikäli yhteys pätkii ja muuta ilmeistä selitystä ei löydy esimerkiksi reitittimestäsi tai PC:stäsi.\n",
"5": "\n5. Päivitä tai asenna uusiksi WLAN adapterin eli verkkokortin ohjaimet ja tarkista sen yhteensopivuus Windows Updaten kanssa.\nKlikkaa aloita-painiketta (Start) -> laitehallinta (Device Manager) ja valitse sieltä verkkosovittimet (Network adapters) -> oikealla hiirenpainikkeella oikean verkkosovittimen kohdalta valitse päivitä ohjain (Update driver). \
Adapterin uudelleen asentamisessa valitse päivityksen sijaan 'poista' (Uninstall device) -> käynnistä tietokone ja anna Windowsin asentaa ohjaimen versio tai lataa verkosta ja asenna itse. Voit myös tarkistaa verkkokortin fyysisen kunnon avaamalla tietokoneen kotelon (tähän löytyy tarkempia ohjeita internetistä; muista käyttää ESD-mattoa ym.).\n",
"6": "\n6. Tarkista tietokoneen virranhallinnan asetukset.\nKlikkaa aloita-painiketta (Start) -> laitehallinta (Device Manager) ja valitse sieltä verkkosovittimet (Network adapters) -> tuplaklikkaa verkkosovittimesi nimeä ja valitse virranhallinta-välilehti (Power Management) sekä \
ruksaa 'salli tietokoneen säästää virtaa sammuttamalla tämä laite'-ruutu -> käynnistä tietokone uudestaan ja tarkista yhteys.\n",
"7": "\n7. Tarkista DHCP-asetukset.\nKlikkaa aloita-painiketta (Start) -> asetukset (Settings) -> verkko ja internet (Network & Internet) -> WLAN -> valitse yhteys ja tarkista, että IP-asetuksissa lukee: Automaattinen (DHCP). Jos ei, valitse muokkaa (Edit) -> valitse 'Automaattinen (DHCP)'-painike -> tarkista yhteyden toimivuus.\n",
"8": "\n8. Suorita haittaohjelmien varalta tarkistus haittaohjelmantorjuntaohjelmistollasi.\nErilaiset virukset PC:llä tai reitittimellä voivat aiheuttaa yhteysongelmia. On olemassa tiettyjä merkkejä, jotka viittaavat reitittimessä olevan viruksia tai mahdollisen hakkeroinnin kohde: \
Tietokone toimii tavallista hitaammin, internet-haut ohjautuvat omituisille sivustoille tai uusia työkalupalkkeja (toolbars) ilmestyy itsestään selaimeen.\n",
"9": "\n9. Kokeile komentokehotteessa yhteysongelmien korjausta.\nKokeile komentokehotteessa seuraavien komentojen avulla TCP/IP-pinon manuaalista nollaamista, IP-osoitteen vapauttamista ja uusimista sekä DNS-asiakasohjelman välimuistin tyhjentämistä:\n\
  a. netsh winsock reset + enter.\n  b. netsh in tip reset + enter.\n  c. ipconfig /release + enter.\n  d. ipconfig /renew + enter.\n  e. ipconfig /flushdns + enter.\n",
"10": "\n10. Resetoi eli palauta langaton reititin oletusasetuksiin.\nJos reitittimen uudelleenkäynnistys ei auta tai olet unohtanut sen salasanan (tai luulet reitittimen tietoturvan vaarantuneen ja haluat palauttaa sen asetukset estääksesi epäasialliset käyttäjät), langattoman reitittimen voi myös resetoida. Paina reitittimen pientä 'Reset'-nappulaa, \
joka on usein sen, takana noin 30 sekuntia (reitittimen valot vilkkuu tai se vain käynnistyy uudestaan) jolloin reititin palautuu oletusasetuksiin. Tämän jälkeen voit alkaa asettaa asetuksia uusiksi. Ensikerran kirjautumiseen tarvittavat oletuskäyttäjätunnus ja -salasana ovat usein printattu reitittimen taakse. Mikäli näin ei ole, näitä löytyy myös esimerkiksi seuraavista osoitteista: \
RouterPasswords.com tai PortForward.com. Toinen, 'pehmeämpi tapa' resetoida reititin on mennä selaimen kautta reitittimeen ja valita hallinta-valikko (Management-, Administration-, Advanced-, System-, Maintenance- tai muu vastaavan niminen valikko) ja etsiä sieltä oletusasetusten palautus-nappi. Tämä tekee saman kuin fyysisen 'Reset'-napin painallus, mutta vaihtoehtona on myös varmuuskopioida reitittimen konfiguraatio \
myöhempää käyttöä varten. Asetuksia uudelleen laittaessa kannattaa ehdottomasti vaihtaa oletuskäyttäjätunnukset ja -salasana sekä varmistaa perus tietoturva-asetukset (kts. ohjelman 'WLAN-verkon tietoturvauhat ja niiden ehkäiseminen'-osiosta) ovat langattoman verkkoyhteysasetusten lisäksi kunnossa.\
Vaihtoehtoisesti, jos edelliset keinot eivät auta, voi harkita uuden reitittimen tai verkkokortin hankkimista.\n"}
  
    valinta_wlan(11, ratkaisuEhdotukset, "yhteysPätkii", "WLAN-verkkosi yhteyden katkeamis")



def kuva_eiInternetYhteyttä():
    print(r"""
                                                                                                \         /
                                                                                                     |         Miksi internetyhteyttä ei ole?!?
                                                                                                 \. |     /       _________________________
                                                                           ~~         ~~          \    .         |  _____________________  |
                                                                                                   .|   /        | |              ______ | |
                                                                   ~~        ~~    ~~         ~~  \?!##!  .      | |  Windows 10 /__/__/ | |
                                                                       ~~                 ~~      / .#!\         | |            /__/__/  | |
                                                                          ~~  .    .  ~~          ./ |           | |_____________________| |
                                                                              |    |            /      . \       |_________________________|
                                                                             _|____|__               |          / __ __ __ __ __ __ __ __  /
                                                                            / |    | /|                    \   / __ __ __ __ __ __ __ __  /
                                                                           /   R-1  / /                       / __ __ __ __ __ __ __ __  /
                                                                          /________/ /                       /        ________          /
                                                                          |________|/                       /__________________________/    
    

    """)


# 'Ei internetyhteyttä'-osion ratkaisuehdotukset

def eiInternetYhteyttäKuvake():
    
    tyhjennäRuutu()

    otsikko("WLAN-verkkoyhteys   on   poikki", 60)

    kuva_eiInternetYhteyttä()

    ratkaisuEhdotukset = {"1": "\nEli sinulla ei ole internetyhteyttä jostakin syystä. Kokeillaan muutamaa keinoa.\n\
\n1. Varmista ensiksi, että WLAN on käytössä ja tarkista WLAN-kytkimen merkkivalo:\
\nValitse tehtäväpalkin oikeassa reunassa ”Ei Internet-yhteyttä”-kuvake ja varmista, että WLAN on otettu käyttöön. \
Jos näin ei ole, ota se käyttöön painamalla WLAN-kuvaketta. Varmista myös, että lentotila on poistettu käytöstä. \
Katso tämän jälkeen, että tunnistamiasi ja luottamiasi WLAN-verkkoja näkyy verkkoluettelossa. \
Jos näin on, valitse haluamasi WLAN-verkon kuvake ja yrittää muodostaa yhteys siihen. \
Jos WLAN-verkkonimen alapuolella lukee 'yhdistetty', valitse 'katkaise yhteys', odota hetki ja paina sitten uudestaan muodostaaksesi yhteyden. \
Varmista, että kannettavan tietokoneen fyysinen WLAN-kytkin on käytössä-asennossa. Sen merkkivalo palaa tavallisesti, kun WLAN on käytössä.\n",
"2": "\n2. Tarkista, onko reitittimessä yhteysongelmia tekemällä ping-testi komentokehotteessa. \nPing-testi tehdään avaamalla komentokehote (kirjoita 'cmd' hakukenttään) ja kirjoittamalla komento: ping <oletusreitittimen IP>. \
Jos ping-viesti vastaa (komentokehotteessa näkyy: 'Reply from...'), sinulla on yhteys WLAN-reitittimeen. Tällöin internet-palveluntarjoajalla voi mahdollisesti olla ongelmia yhteydessä, joten kannattaa ottaa heihin yhteyttä jos seuraavaksi esitellyt keinot eivät auta. \
Jos ping-testin tulokset osoittavat, että et saa vastausta reitittimeltä (komentokehotteessa näkyy: 'Request timed out'), yritä yhdistää tietokone suoraan modeemiin Ethernet-kaapelilla (jos sellainen löytyy). \
Jos voit muodostaa internet-yhteyden Ethernet-kaapelilla, se vahvistaa, että yhteysongelma johtuu WLAN reitittimestäsi. Varmista tällöin, että olet asentanut uusimman laiteohjelmiston (katso reitittimesi käyttöohjeet).\n",
"3": "\n3. Tarkista reitittimesi fyysinen sijainti ja testaa sen taajuusasetusten toiminta.\nWLAN-verkossa signaalin pitää saada kulkea esteettä, jotta yhteys ei pätki. Varmista siis, että reititin tai WLAN-tukiasema ovat tarpeeksi lähellä tietokonettasi ja ettei näiden välissä ole fyysisiä esteitä. \
Voit myös kokeilla vaihtaa reitittimesi taajuutta 2.4 GHz:stä 5 GHz:n. Tee tämä avaamalla selain ja kirjoittamalla URL-kenttään reitittimen IP-osoite (reitittimen IP-osoite löytyy esim. seuraavasti: kirjoita työpöydältä löytyvään hakukenttään 'cmd', jolloin avautuu mustaruutuinen, ns. komentokehote -> \
kirjoita 'ipconfig' ja katso reitittimen IP-osoite Wireless LAN adapter Wi-Fi-kohdasta 'Default Gateway'-sanan jälkeen) -> anna käyttäjätunnus ja salasana -> vaihda taajuus 2.4 GHz:stä 5 GHz:n asetuksista). Jos sinulla on IoT-laitteita tai muita Wi-Fi-laitteita, jotka eivät ole tarpeellisessa käytössä, katkaise niistä yhteydet.\n",
"4": "\n4. Koita reitittimesi antaa jäähtyä sammuttamalla se hetkeksi.\nJos reititin tai modeemi ei pysty ylläpitämään yhteyttä tasaisesti, tarkista onko se ylikuumentunut. \
Jos on, sammuta se ja anna jäähtyä tai kokeile 'power cycling'-metodia (eli kytke virta pois irrottamalla virtajohto noin minuutiksi ja kytke uudestaan päälle). \
Tämä auttaa luomaan uuden yhteyden internet-palveluntarjoajaan.\n ",
"5": "\n5. Käytä vianmääritysohjelmaa (Network troubleshooter).\nVianmääritysohjelma auttaa diagnosoimaan yleisimpiä verkon ongelmia. Sitä voi käyttää klikkaamalla: \
aloitus (Start) -> asetukset (Settings) -> verkko ja internet (Network & Internet) -> tila (Status) -> valitse 'verkon vianmääritys' -> noudata ohjeita ja katso, korjautuuko ongelma.\n",
"6": "\n6. Tarkista internetpalveluntarjoajasi eli ISP:n ilmoitukset lähialueesi mahdollisista yhteysongelmista.\nYhteysongelmat voivat johtua palveluntarjoajasta ja onkin hyvä tarkastaa heidän ilmoitukset mikäli yhteys pätkii ja muuta ilmeistä selitystä ei löydy esimerkiksi reitittimestäsi tai PC:stäsi.\n",
"7": "\n7. Yritä muodostaa yhteys toiseen laitteeseen. \nYritä muodostaa yhteys toiseen kannettavaan tietokoneeseen tai puhelimeen, joka on samassa verkossa. \
Jos niissäkin on yhteysongelmia, vika voi olla reitittimessä, modeemissa tai palveluntarjoajalla.  Jos puolestaan yhteys toimii muussa laitteessa, ongelman aiheuttaja on todennäköisesti alkuperäinen laite. \
Tarkista tällöin laitteiston tai käyttöjärjestelmän vikoja ja siirry laitteen verkon vianmääritykseen.\n",
"8": "\n8. Tarkista WLAN-profiiliasetukset.\nWLAN-profiilin avulla Windows tallentaa asetukset, joita tarvitaan yhteyden muodostamiseen WLAN-verkkoon. \
Näihin asetuksiin sisältyy verkon suojaustyyppi, avain, verkkonimi (SSID) ja niin edelleen. Jos et voi muodostaa yhteyttä WLAN-verkkoon, johon yhteyden muodostaminen onnistui aiemmin, \
verkkoasetukset ovat ehkä muuttuneet tai profiili on ehkä vioittunut. Voit korjata asian poistamalla (tai 'unohtamalla') verkkoyhteyden ja muodostamalla sitten yhteyden verkkoon uudelleen. \
Kun unohdat verkkoyhteyden, WLAN-verkkoprofiili poistetaan tietokoneesta. Verkon unohtaminen tapahtuu seuraavasti: valitse WLAN-verkkokuvake -> verkkoyhteys ja internet-asetukset (Network & Internet) -> valitse WLAN -> 'hallitse tunnettuja verkkoja'-painike -> valitse verkko, jonka haluat unohtaa -> valitse 'unohda'-kohta. \
Yritä muodostaa yhteys uudelleen haluttuun verkkoon.\n",
"9": "\n9. Päivitä tai asenna uusiksi WLAN adapterin eli verkkokortin ohjaimet ja tarkista sen yhteensopivuus Windows Updaten kanssa.\nKlikkaa aloita-painiketta (Start) -> laitehallinta (Device Manager) ja valitse sieltä verkkosovittimet (Network adapters) -> oikealla hiirenpainikkeella oikean verkkosovittimen kohdalta valitse päivitä ohjain (Update driver). \
Adapterin uudelleen asentamisessa valitse päivityksen sijaan 'poista' (Uninstall device) -> käynnistä tietokone ja anna Windowsin asentaa ohjaimen versio tai lataa verkosta ja asenna itse. Voit myös tarkistaa verkkokortin fyysisen kunnon avaamalla tietokoneen kotelon (tähän löytyy tarkempia ohjeita internetistä; muista käyttää ESD-mattoa ym.).\n",
"10": "\n10. Tarkista Windows:n järjestelmäkansiot.\nYhteysongelmat voivat johtua korruptoituneista Windows järjestelmäkansioista. Nämä voi tarkistaa system file checker-ohjelmalla (SFC). \
Tämä tehdään avaamalla CMD ja suoritetaan DISM eli Deployment Image Servicing and Management-työkalu komennolla: dism.exe /online /cleanup-image /restorehealth. DISM käyttää Windows Updatea päivittääkseen korruptoituneet kansiot uusiin. \
Tämä jälkeen voidaan skannata korruptoituneita kansioita ja vaihtaa ne uusiin komennolla: sfc /scannow. Skannerin jälkeen saadaan ilmoitus tuloksista: korruptoituneita kansioita ei löytynyt, toimintoa ei voitu suorittaa (SFC pitää suorittaa tällöin ’Safe Modessa’), \
korruptoituneita kansioita löydettiin ja ne vaihdettiin onnistuneesti tai niitä löydettiin muttei onnistuttu korjaamaan. Skannauksen tulokset voi kopioida tekstitiedostoon tarkasteltavaksi komennolla: findstr /c:'[sr]' %windir%\logs\cbs\cbs.log >%userprofile%\desktop\sfcdetails.txt'. \
Tiedostosta voi etsiä päivämäärien ja ajanperusteella korruptoituneita tiedostoja ja korvata ne manuaalisesti seuraavalla tavalla. Ota ensin korruptoitunut tiedosto hallintaan komennolla: takeown /f <korruptoituneen tiedoston sijainti>. Anna ylläpitäjälle oikeus tiedostoon komennolla: icacls <tiedoston sijainti> /grant administrators:f. \
Kopioi ja liitä toimiva tiedosto korruptoituneen tilalle komennolla: copy <toimivan tiedoston sijainti> <korruptoituneen tiedoston sijainti>. \n",
"11": "\n11. Tarkista tietoturvasovellusten konfliktit. \nTietoturva sovellukset, kuten haittaohjelmantorjuntaohjelmisto tai palomuuri voivat aiheuttaa yhteysongelmia. Tarkista näiden sovellusten asetukset ja katso, minkälainen verkkoliikenne on sallittua. Kokeile lakkauttaa näiden ohjelmistojen toiminta väliaikaisesti tai tietyiltä osin ja katso, paraneeko yhteys. \
Jos näin on, tarkista haittaohjelmantorjuntaohjelmiston toimittajalta, josko yhteyttä haittaavat asetukset ovat tärkeitä laitteen suojaamisessa. Jos eivät, jätä ne pois päältä. Voit harkita myös Windows-ympäristöön sopivia, kolmansien osapuolten suunnittelemia helppokäyttöisiä ja ilmaisia palomuureja, kuten ZoneAlarm.\n",
"12": "\n12. Kokeile komentokehotteessa yhteysongelmien korjausta.\nKokeile komentokehotteessa seuraavien komentojen avulla TCP/IP-pinon manuaalista nollaamista, IP-osoitteen vapauttamista ja uusimista sekä DNS-asiakasohjelman välimuistin tyhjentämistä:\n\
  a. netsh winsock reset + enter.\n  b. netsh in tip reset + enter.\n  c. ipconfig /release + enter.\n  d. ipconfig /renew + enter.\n  e. ipconfig /flushdns + enter.\n",
"13": "\n13. Resetoi eli palauta langaton reititin oletusasetuksiin.\nJos reitittimen uudelleenkäynnistys ei auta tai olet unohtanut sen salasanan (tai luulet reitittimen tietoturvan vaarantuneen ja haluat palauttaa sen asetukset estääksesi epäasialliset käyttäjät), langattoman reitittimen voi myös resetoida. Paina reitittimen pientä 'Reset'-nappulaa, \
joka on usein sen, takana noin 30 sekuntia (reitittimen valot vilkkuu tai se vain käynnistyy uudestaan) jolloin reititin palautuu oletusasetuksiin. Tämän jälkeen voit alkaa asettaa asetuksia uusiksi. Ensikerran kirjautumiseen tarvittavat oletuskäyttäjätunnus ja -salasana ovat usein printattu reitittimen taakse. Mikäli näin ei ole, näitä löytyy myös esimerkiksi seuraavista osoitteista: \
RouterPasswords.com tai PortForward.com. Toinen, 'pehmeämpi tapa' resetoida reititin on mennä selaimen kautta reitittimeen ja valita hallinta-valikko (Management-, Administration-, Advanced-, System-, Maintenance- tai muu vastaavan niminen valikko) ja etsiä sieltä oletusasetusten palautus-nappi. Tämä tekee saman kuin fyysisen 'Reset'-napin painallus, mutta vaihtoehtona on myös varmuuskopioida reitittimen konfiguraatio \
myöhempää käyttöä varten. Asetuksia uudelleen laittaessa kannattaa ehdottomasti vaihtaa oletuskäyttäjätunnukset ja -salasana sekä varmistaa perus tietoturva-asetukset (kts. ohjelman 'WLAN-verkon tietoturvauhat ja niiden ehkäiseminen'-osiosta) ovat langattoman verkkoyhteysasetusten lisäksi kunnossa.\
Vaihtoehtoisesti, jos edelliset keinot eivät auta, voi harkita uuden reitittimen tai verkkokortin hankkimista.\n",
"14": "\n14. Resetoi eli palauta verkko oletusasetuksiin. \nTämä on viimeinen keino, jota kannattaa kokeilla, jos muu ei toimi. Verkon resetointi voi auttaa ratkaisemaan myös muita yhteysongelmia, jotka ilmaantuvat, kun olet päivittämässä Windows 10:ä, \
tai tilanteessa, kun voit muodostaa yhteyden internetiin, mutta et voi muodostaa yhteyttä jaettuihin verkkoasemiin. Verkkoasetusten palauttaminen poistaa kaikki asentamasi verkkosovittimet ja niiden asetukset. Kun tietokone käynnistetään uudelleen, järjestelmä asentaa verkkosovittimet uudelleen käyttämällä niiden oletusasetuksia. \
Verkon resetoimiseksi voi klikata:\n  a. Aloitus (Start) -> asetukset (Settings) -> verkko ja internet (Network & Internet)-> tila (Status) -> verkon määritys uudelleen -> valitse 'määritä'-painike. \n  b. Valitse verkkoasetusten palautusnäytössä ’palauta nyt’ ja vahvista valinta valitsemalla 'kyllä'. Odota tietokoneen uudelleen käynnistystä ja tarkista, korjautuiko ongelma.\n\
  c. Kun olet palauttanut verkon oletusasetukset, saatat joutua asentamaan tai määrittämään uudelleen muita käyttämiäsi verkko-ohjelmistoja, kuten VPN-asiakasohjelmiston tai Hyper-V:n virtuaalikytkimet.\n"}

    valinta_wlan(15, ratkaisuEhdotukset, "selain", "WLAN-internetyhteys")


def kuva_Win10Logo():
    print(r"""           
                                                                                 _   _            __         _           _   _    _   ___  __
                                                                \  /\  / | |\ | | \ / \ \  /\  / /_       | | |     | | |_| | \  /_\   |  |__
                                                                 \/  \/  | | \| |_/ \_/  \/  \/  __/      | |_|     |_| |   |_/ /   \  |  |__
                                                                                          _______________   _______________
                                                                                         /              /  /              /
                                                                                        /              /  /              /
                                                                                       /              /  /              /
                                                                                      /______________/  /______________/
                                                                                     _______________   _______________
                                                                                    /              /  /              /
                                                                                   /              /  /              /
                                                                                  /              /  /              /
                                                                                 /______________/  /______________/


    """)


# 'Yhteysongelma Windows 10 päivityksen jälkeen'-osion ratkaisuehdotukset

def päivitysOngelmaWin10(wlanVaiEth):
    
    tyhjennäRuutu()

    otsikko("Windows   10:n   ongelmat", 100)

    kuva_Win10Logo()

    ratkaisuEhdotukset = {"1": "\nEli verkkoyhteys katkesi Windows 10 päivityksen jälkeen. Kokeillaan seuraavia keinoja ongelman ratkaisuun.\n\n1. Uudelleenasenna verkkokortin ohjaimet.\nEnnen verkkokortin ohjaimien uudelleenasennusta kannattaa ensin ottaa varmuuskopiot. \
Ohjaimien asennuksen voi tehdä: avaamalla laitehallinnan (Device Manager) -> laajentamalla verkkosovitin kategorian -> etsi viallinen verkkokortti (Network adapter) -> valitse 'poista laite'-asennuspainike -> \
'yritä poistaa tämän laitteen ohjainohjelmistoa'-valintaruutu -> valitse 'poista'-kohta. Käynnistetään tietokone uudestaan ja annetaan Windowsin asentaa verkkokortti ja sen ohjaimet automaattisesti. \
Jos näin ei tapahdu, asenna ohjaimen varmuuskopio.\n",
"2": "\n2. Etsi verkkokortin valmistajan päivityksiä laiteohjaimille.\nVaihtoehtoisesti verkosta voi etsiä verkkokortin valmistajan päivityksiä laiteohjaimille: avaa laitehallinta (Device Manager) -> \
laajenna verkkosovittimet ja etsi laitteesi verkkosovitin -> valitse verkkosovitin (Network adapter) -> valitse 'päivitä ohjain'-painike -> etsi päivitettyä ohjainohjelmistoa automaattisesti ja noudata ohjeita. \
Kun päivitetyt ohjaimet on asennettu, käynnistä tietokone uudelleen ja tarkasta, korjautuiko yhteysongelma. Jos Windows ei löydä uutta ohjainta verkkosovittimelle, lataa verkkosovittimen uusin ohjain tietokoneen valmistajan sivustolta. \
Sinun on tiedettävä tietokoneen valmistaja sekä mallin nimi tai numero. Tee jompikumpi seuraavista:\n\nA) Jos et pystynyt lataamaan ja asentamaan uudempaa verkkosovitinohjainta, piilota päivitys, joka aiheuttaa verkkoyhteyden katoamisen. \
Lisätietoja päivitysten piilottamisesta löytyy hakemalla tietoa 'Windows päivitykset' tai 'ohjainpäivitysten piilottaminen'.\n\nB) Jos pystyt onnistuneesti asentamaan verkkosovittimen päivitetyt ohjaimet, asenna uusimmat päivitykset uudelleen. \
Voit tehdä tämän valitsemalla: käynnistä-painike -> asetukset -> päivittäminen ja suojaus -> tarkista päivitykset.\n ",
"3": "\n3. Tarkista, verkkokortin fyysinen asento ja langattoman verkon tila.\nVerkkokortin asennon tietokoneen sisällä voi myös fyysisesti tarkistaa ja varmistaa, että se on kunnolla kiinni (käytä ESD-mattoa ja perehdy internetistä tarkemmin halutessasi tietokoneen kotelon avaamiseen). \
Lisäksi on hyvä tarkistaa verkkosovittimen langattoman verkon tila-asetus, että se vastaa yhdistettävän verkon ominaisuuksia. Tämä langattoman verkon tila -asetuksen etsiminen tehdään seuraavasti: \
laitehallinta (Device Manager) -> verkkosovittimet (Network adapters) -> klikkaa verkkosovittimen nimeä -> lisäasetukset (Advanced settings) -> langattoman verkon tila -> varmista että se on asetettu verkon käyttämään tilaan.\n", 
"4": "\n4. Tarkista, onko verkkosovitin yhteensopiva uusimman Windows Updaten kanssa.\n\
Jos verkkoyhteys katkesi heti Windows 10 päivittämisen jälkeen, verkkosovittimen nykyinen ohjain on ehkä suunniteltu aiempaan Windowsiin. Voit tarkistaa tämän yrittämällä poistaa viimeisimmän Windows-päivityksen tilapäisesti: \
käynnistä-painike eli aloitus (Start) -> asetukset (Settings) -> päivittäminen & suojaus (Update & Security) -> näytä päivityshistoria -> poista päivitykset -> valitse uusin päivitys -> valitse poista asennus. \
Jos uusimman päivityksen asennuksen poistaminen palauttaa verkkoyhteyden, tarkista, onko päivitetty ohjain saatavilla edellä olleen b-kohdan mukaisesti.\n"}

    if (wlanVaiEth == "wlan"):
        valinta_wlan(5, ratkaisuEhdotukset, "Win10", "Windows 10 päivityksen ilmenneisiin verkkoyhteys")
    elif (wlanVaiEth == "eth"):
        valinta_eth(5, ratkaisuEhdotukset, "Win10", "Windows 10 päivityksen jälkeen ilmenneisiin verkkoyhteys")


def kuva_pageNotFound():
    print(r"""   
                                                                                                                                          ______
                                                         ___   ___   ___   ___            ___  _____      ___  ___               ___      \    /
                                                        |   | |   | |   | |        |\  | |   |   |       |___ |   | |   | |\  | |   \      \  /
                                                        |___| |___| | __  |___     | \ | |   |   |       |    |   | |   | | \ | |   /       \/
                                                        |     |   | |___| |___     |  \| |___|   |       |    |___| |___| |  \| |__/        __
                                                                                                                                           |__|


    """)


# 'DNS lookup failed'-osion ratkaisuehdotukset

def dnsLookupFailed(wlanVaiEth):
    
    tyhjennäRuutu()

    otsikko("'DNS   Lookup   failed'", 120)

    kuva_pageNotFound()

    ratkaisuEhdotukset = {"1": "\nEli selaimen ikkunaan ilmestyi 'DNS Lookup failed'-ilmoitus. Se on Windows-käyttöjärjestelmäympäristössä harmittavan tavallinen virhe (Blue Screen of Death-virheen ohella) ja johtuu siitä, että DNS-serverilläsi tai sen ja päätelaitteen välisessä kommunikaatiossa on jokin pielessä. Kokeillaan ratkaista asia seuraavilla keinoin.\n\n",
"1": "\n1. Poista välimuisti ja evästeet.\nEsimerkiksi välimuisti ja evästetiedot voi poistaa Mozilla Firefoxissa seuraavasti: avaa selaimessa hampurilaisvalikko oikeasta yläkulmasta -> asetukset (Settings) -> tietosuoja ja turvallisuus (Privacy & Security) -> valitse 'evästeet ja sivustotiedot'-kohdasta (Cookies & Site Data) 'tyhjennä tiedot'-kohta (Clear Data). Tähän voi käyttää myös erilaisia ohjelmia, kuten esimerkiksi CCleaner-sovellusta. Avaa tai päivitä selain uudestaan ja katso, ratkesiko ongelma.\n",
"2": "\n2. Avaa internet-yhteyden vianmääritys.\nTee tämä kirjottamalla työpöydän hakukenttään 'vianmääritys' -> muut vianmääritykset -> internet-yhteydet -> suorita vianmääritys ja toimi sen ohjeiden mukaan.\n",
"3": "\n3. Vaihda oletuksena oleva DNS-serverisi kolmannen osapuolen, kuten Googlen DNS-serveriin tai OpenDNS-serveriin.\nTämä tehdään vaihtamalla IPv4-osoitetietoja: Kirjoita työpöydällä olevaan aloituksen hakukenttään 'ncpa.cpl' ja paina 'Enter'-painiketta -> valitse oikealla hiirenpainikkeella aktiivinen yhteys ja sen ominaisuudet \
-> valitse 'Internet Protocol version 4 (TCP/IPv4)'-kohta ja paina sen 'ominaisuus'-painiketta -> ruksi 'käytä seuraavaa DNS palvelimen osoitetta'-kohta -> laita ensisijaiseksi DNS:n IPv4-osoitteeksi 8.8.8.8 ja toiseksi IPv4-osoitteeksi 4.2.2.2 tai 8.8.4.4 ja paina sitten 'ok'-painiketta. Avaa tai päivitä selain uudestaan ja katso, ratkesiko ongelma.\n",
"4": "\n4. Poista DNS-välimuisti.\nAvaa CMD eli komentokehote (ylläpitäjänä) -> käytä komentoa: ipconfig /flushdns. Tämä poistaa DNS-välimuistin ja voi poistaa ongelman. Avaa tai päivitä selain uudestaan ja tarkista.\n",
"5": "\n5. Uudelleenkäynnistä ns. network stack.\nAvaa CMD eli komentokehote (ylläpitäjänä) -> käytä komentoa: netsh winsock reset catalog -> sulje CMD ja käynnistä tietokone uudelleen. Tarkista, toimiiko selain oikein.\n"}

    if (wlanVaiEth == "wlan"):
        valinta_wlan(6, ratkaisuEhdotukset, "dns_lookup_failed", "'DNS Lookup Failed'-")
    elif (wlanVaiEth == "eth"):
        valinta_eth(6, ratkaisuEhdotukset, "dns_lookup_failed", "'DNS Lookup Failed'-")
  

def kuva_selainEiToimi():
    print(r"""
                                                                 _______________________________________________________________           
                                                                /////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\            _________________________________________________________________
                                                               //////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\          <                                                                 >
                                                              ///////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\         <              HTTP tilakoodit eli HTTP Status Codes              >
                                                             /_____________________________________________________________________\        <                                                                 >
                                                            ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        <   HTTP Status Codes: HTTP-palvelimen lähettäessä vastauksen     >
                                                            ||||________________________________________________________________||||        <   selaimelle, vastauksen ensimmäisellä rivillä on tilakoodi,    >
                                                            ||||                                                          _ O X ||||        <   joka kertoo käyttäjän (selaimen) pyynön onnistumisesta ja     >
                                                            ||||________________________________________________________________||||        <   sen mahdollisesta jatkokäsittelystä. Yleisimmät koodit:       >
                                                            ||||                                                                ||||        <                                                                 >
                                                            ||||                                                                ||||        <   - Information Response 100-199: Kertoo selaimelle, että se    >
                                                            ||||                         404 Not Found                          ||||        <   voi lähettää loput pyynnöstä.                                 >
                                                            ||||                                                                ||||        <   - Success 200-299: Pyyntö onnistui.                           >
                                                            ||||                             ><    ><    Sorry!                 ||||        <   - Redirection 300-399: selaimen pyyntö ohjataan toiselle      >
                                                            ||||                           ___\____/_   /                       ||||        <   palvelimelle tai websivulle.                                  >
                                                            ||||                 \___     |    o o   |     ___/                 ||||        <   - Client Errors 400-499: selaimen pyynnössä oli virhe,        >
                                                            ||||                     \    |   _____  |    /                     ||||        <   tietoja tms. puuttui pyynnöstä.                               >
                                                            ||||                      \   |__________|   /                      ||||        <   - Server Errors 500-599: palvelimen päässä on jokin ongelma   >
                                                            ||||_______________________\______|___|_____/_______________________||||        <   (usein aika merkittävä sellainen, jos tämä koodi ilmestyy).   >
                                                            ||||________________________________________________________________||||        <                                                                 >
                                                            ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||        <_________________________________________________________________>
                                                            |______________________________________________________________________|
                                                                             \\\\\\\\\\\\\\\\\\\\////////////////////
                                                                              \\\\\\\\\\\\\\\\\\\///////////////////                  
                                                                               \__________________________________/
                    

    """)


# 'Selain ei toimi'-osion ratkaisuehdotukset

def selainEiToimi(wlanVaiEth):

    tyhjennäRuutu()

    otsikko("Selain   ei   toimi   oikein", 110)

    kuva_selainEiToimi()

    ratkaisuEhdotukset = {"1": "\nSelaimesi lakkasi siis toimimasta kunnolla. Kokeillaan seuraavia keinoja.\n\n1. Kokeile toista selainta.\nMikäli etsimäsi sivusto avautuu normaalisti toisella selaimella, jotakin on pielessä alkuperäisesti käyttämälläsi selaimella; vaatien välimuistin ja evästeiden poistoa, päivitystä tms. \
(tähän saa vinkkejä tämän ohjelman muista osista tai internetistä).\n", "2": "\n2. Poista ja asenna uudelleen haittaohjelmantorjuntaohjelmasi.\n",
"3": "\n3. Käytä vianetsintäohjelmaa (ns. 'app troubleshooter'-sovellusta).\nPaina 'aloitus'-painiketta (Start) -> ohjauspaneeli (Control Panel) -> valitse näkymästä suuret kuvakkeet \
-> vianmääritys (Troubleshooting) -> näytä kaikki -> valitse internet-yhteydet. Seuraa ohjeita.\n", "4": "\n4. Käytä DISM-työkalua (Deployment Image Servicing and Management command-line tool).\nPaina 'aloitus'-painiketta -> avaa komentokehote eli CMD -> \
suorita komentokehotteessa komento: DISM /Online /Cleanup-Image /ScanHealth -> suorita sitten komento: DISM /Online /Cleanup-Image /RestoreHealth. \
Kun toiminto on tehty, käynnistä tietokone uudelleen ja tarkista onko ongelma edelleen läsnä.\n",
"5": "\n5. Käytä SFC-skanneria (System File Checker-scanner).\nPaina 'aloitus'-painiketta -> avaa komentokehote eli CMD (järjestelmän ylläpitäjänä) -> suorita komento: sfc/scannow -> käynnistä tietokone uudelleen. \
SFC-skanneri tarkistaa kaikki suojatut järjestelmäkansiot ja korvaa toimimattomat uusilla.\n",
"6": "\n6. Suorita ns. clean boot.\nKirjoita työpöydän hakukenttään 'msconfig' -> valitse järjestelmä määrityksistä palvelut-välilehti (services) -> \
valitse ’piilota kaikki Microsoftin palvelut’-raksi -> valitse 'kytke pois päältä'-painike (disable all) -> valitse 'käynnistys'-välilehti (startup-tab) -> \
avaa tehtävienhallinta (task manager) -> sulje tehtävienhallinta ja paina ok -> uudelleenkäynnistä tietokone. \
Tämä toiminto vähentää konflikteja sovelluksissa, jotka toimivat taustalla Windowsia normaalisti käynnistettäessä. \
Clean boot-ympäristö avautuu edellä olevien klikkausten jälkeen, jonka suorittamisen jälkeen voit tarkastaa, toimiiko selain.\n",
"7": "\n7. Mikäli käytät Internet Exploreria, kokeile verkkodiagnostiikkatyökalua (network diagnostics tool).\nAvaa Internet Explorer -> yritä avata verkkosivu, joka antaa error-viestin -> \
paina diagnosoi yhteysongelmia painiketta, joka käynnistää diagnosointityökalun -> työkalu antaa palautetta ongelmasta, jota seurataan -> kirjoita ylös IP-osoite ja seuraa annettuja toimenpideohjeita.\n",
"8": "\n8. Tarkista tietoturvaohjelmat.\nPalomuuri ja haittaohjelmantorjuntaohjelmat voivat estää selainta toimimasta. Ei ole suositeltavaa pysyvästi lakkauttaa näitä, mutta väliaikaisesti näin voi tehdä, jotta tiedetään, \
onko selaimen ongelmat näistä johtuvia (älä klikkaa mitään vähänkään epämääräisiä linkkejä tms. näiden ollessa poissa käytöstä). Kun verkkomäärityksiä on muutettu sopivasti niin että yhteys toimii, laita haittaohjelmantorjuntaohjelma ja palomuuri takaisin päälle.\n",
"9": "\n9. Suorita järjestelmän palautus (system restore).\nPaina 'aloitus'-painiketta (Start) -> ohjauspaneeli (Control Panel) -> järjestelmä ja suojaus (System & Security) -> järjestelmä -> järjestelmänsuojaus -> järjestelmän palauttaminen (system restore) -> \
valitse toinen palautuspiste ja paina ok -> valitse seuraava -> paina palautuspiste, joka on luotu ennen ongelmien alkamista -> valitse seuraava -> valitse 'valmis'-painike. \
Tämä toiminto ei poista henkilökohtaisia kansioita, mutta poistaa sovellukset, ohjaimet ja päivitykset, jotka asennettiin palautuspisteen jälkeen.\nJotta palautuspisteeseen voi palata, toimi seuraavasti: Paina 'aloitus'-painiketta -> ohjauspaneeli -> \
kirjoita hakukenttään palautusasema (recovery) -> valitse palautusasema -> avaa järjestelmän palautus (system restore) -> valitse seuraava -> valitse palautuspiste ongelmalliseen sovellukseen, ohjaimeen tai päivitykseen liittyen -> \
valitse seuraava -> valitse 'valmis'-painike.\n", "10": "\n10. Luo uusi käyttäjäprofiili.\nPaina 'aloitus'-painiketta -> asetukset -> tilit -> perheenjäsenet ja muut käyttäjät -> 'lisää joku muu tähän tietokoneeseen'-painike -> \
täytä tarvittavat tiedot salasanoineen -> vaihda tilin tyyppiä -> ruksi ylläpitäjä painike antaaksesi ylläpitäjän oikeudet -> uudelleenkäynnistä tietokone -> kirjaudu juuri luodulla käyttäjätilillä. \
Jos internet toimii tällä käyttäjätilillä, se voi olla merkki siitä, että alkuperäinen käyttäjätili on korruptoitunut. Ongelman voi yrittää korjata alentamalla alkuperäisen tilin roolia uudelta käyttäjätililtä ja aktivoimalla sen uudestaan ylläpitäjän oikeuksiin.\n",
"11": "\n11. Suorita järjestelmän ylläpidon vianmääritys (system maintenance troubleshooter).\nPaina 'aloitus'-painiketta -> ohjauspaneeli (ryhmittely: suuret kuvakkeet) -> vianmääritys -> järjestelmä ja suojaus -> \
järjestelmän ylläpito -> valitse seuraava ja seuraa ohjeita. Tämä toiminto ratkaisee useimmat järjestelmän ongelmat.\n", "12": "\n12. Tarkista päivitykset Windows Update:sta.\nPaina 'aloitus'-painiketta -> Windows Update -> paina 'tarkista päivitykset'-painiketta ja asenna kaikki selaimeen liittyvät päivitykset.\n"}
    
    if (wlanVaiEth == "wlan"):
        valinta_wlan(13, ratkaisuEhdotukset, "selain", "selain")
    elif (wlanVaiEth == "eth"):
        valinta_eth(13, ratkaisuEhdotukset, "selain", "selain")


# 'Etsitty verkkosivu ei löydy'-osion funktiot

def verkkosivuEiLöydy(wlanVaiEth):

    tyhjennäRuutu()

    otsikko("Verkkosivu   ei   aukea", 110)

    kuva_pageNotFound()

    ratkaisuEhdotukset = {"1": "\nEtsimäsi verkkosivu ei suostu ilmeisesti avautumaan oikein. Katsotaan, jos seuraavat keinot auttaisivat.\n\n1. Tarkista, onko sivusto kaatunut vain sinun päätelaitteella vai myös muilla internetin käyttäjillä.\nMene osoitteeseen: downforeveryoneorjustme.com ja laita toimimattoman sivuston URL-osoite hakuun. \
Paina ’just me’-painiketta ja saat vastauksen. Jos saat vastaukseksi, että sivusto on kaatunut kaikilta, et voi tehdä muuta kuin odottaa. Muussa tapauksessa tiedät, että vika on päätelaitteellasi, selaimessa tms. ja on aika tutkia syvemmin ongelman syytä.\n", "2": "\n2. Kokeile avata sivusto toisella laitteella.\n\
Kokeile tietokoneesi sijaan avata sivusto esimerkiksi kännykälläsi. Jos sivusto aukeaa näillä, tiedät vian olevan tietokoneessasi eikä kyseessä ole laajemalle ulottuva yhteysongelma.\n", "3": "\n3. Kokeile avautuuko sivusto toisella selaimella.\nKokeile, onko ongelma selainkohtainen vai ei. \
Jotkin selainevästeet voivat estää pääsyn sivuille. Jos sivusto aukeaa toisella selaimella, alkuperäisellä selaimella on oletusasetuksissa jotakin pielessä. Muokkaa niitä tai poista ja uudelleen asenna selain.\n", 
"4": "\n4. Tarkista ns. 'Windows host'-tiedosto.\nAvaa 'Windows host'-tiedosto, joka on osoitteessa C:\Windows\system32\drivers\etc\ ja katso, onko siellä määriteltynä blokattujen sivujen lista tiedoston lopussa. Blokatut sivut määritellään seuraavalla kaavalla oheisen esimerkin mukaan:\n\n  IP-osoite       domain-nimi       kommentit\n  127.0.0.1       www.domain.com    # domain.com.\n\n\
Poista sivuston nimi blokattujen listasta, jos sellainen tiedostossa on ja poistu tiedostosta tallennettuasi mahdollisesti tekemäsi muutokset.\n", "5": "\n5. Tyhjennä selaimesi välimuisti ja selaushistoria.\nTämä voi auttaa, sillä tyhjennyksen jälkeen selain yrittää muodostaa yhteyden sivustolle ilman, \
että se hakee aiempia välimuistissa olevia paikallisia tiedostoja.\n", "6": "\n6. Poista kaikki selaimen evästeet.\nEvästeet voivat aiheuttaa yhteysongelmia monista syistä, esimerkiksi ne voivat olla huonosti koodattu, yhteensopimattomia jne.\n",
"7": "\n7. Skannaa PC:si haittaohjelmantorjuntaohjelmallasi ja anti-adware-ohjelmalla jos sinulla sellainen on.\n", "8": "\n8. Tarkista palomuurin asetukset.\nPalomuurin asetukset voivat estää verkkosivua avautumasta. Ei ole suositeltavaa pysyvästi lakkauttaa palomuurin toimintaa tai sen verkkoliikennemäärityksiä, mutta väliaikaisesti voi kokeilla, \
onko verkkosivun ongelmat tästä johtuvia. Kun palomuurin verkkomäärityksiä on muutettu sopivasti niin että yhteys toimii, tallenna tekemäsi muutokset.\n", "9": "\n9. Tyhjennä DNS-välimuisti.\nAvaa CMD eli komentokehote (ylläpitäjänä) -> suorita komento: ipconfig /flushdns. Tämä poistaa DNS-välimuistin ja voi poistaa ongelman. Avaa tai päivitä selain uudestaan ja tarkista toimiiko verkkosivu.\n",
"10": "\n10. Vaihda oletuksena oleva DNS-serverisi kolmannen osapuolen, kuten Googlen DNS-serveriin tai OpenDNS-serveriin.\nTämä tehdään vaihtamalla IPv4-osoitetietoja: Kirjoita työpöydällä olevaan hakukenttään 'ncpa.cpl' ja paina 'Enter'-painiketta -> valitse oikealla hiirenpainikkeella aktiivinen yhteys ja sen ominaisuudet \
-> valitse 'Internet Protocol version 4 (TCP/IPv4)'-kohta ja paina sen 'ominaisuus'-painiketta -> ruksi 'käytä seuraavaa DNS-palvelimen osoitetta'-kohta -> laita ensisijaiseksi DNS:n IPv4-osoitteeksi 8.8.8.8 ja toiseksi IPv4-osoitteeksi 4.2.2.2 tai 8.8.4.4 ja paina sitten 'ok'-painiketta. Avaa tai päivitä selain uudestaan ja katso, ratkesiko ongelma.\n",
"11": "\n11. Käytä luotettavaa VPN:ää (Virtual Private Network).\nVPN suojaa toimintaasi internetissä, kryptaten esimerkiksi lähettämäsi viestit ja sen avulla voit valita asetuksista niin, että ulkopuolisille näyttäisi kuin päätelaitteesi toimisi toiselta paikkakunnalta tai valtiosta käsin. Tämän ominaisuuden avulla verkkosivut, joille ei aiemmin ollut pääsyä, voivatkin aueta. \
Muista, että luotettavaa, ilmaista VPN-palvelua, joka asianmukaisella tavalla käsittelisi tietojasi ja suojaisi toimintaasi (usein on juuri päin vastoin), ei ole välttämättä helppoa löytää. Siksi kannattaakin mielummin hankkia maksullinen VPN-versio.\n",
"12": "\n12. Estä välityspalvelimen (proxy-server) toiminta tietokoneellasi.\nVälityspalvelimet voivat luoda ongelmia sillä niissä voi olla edistyneitä haittaohjelmia, jotka muokkaavat tietokoneesi asetuksia automaattisesti. Paina Win + I-näppäintä avataksesi Windows-asetukset -> valitse verkko ja internet (Network & Internet) -> välityspalvelin (Proxy) -> varmista, että ’automaattinen asetusten tunnistus’-asetus (automatically detect settings) on sallittu ja ’käytä asennuskomentosarjaa’-asetus (use a proxy server) ei ole sallittu.\n",
"13": "\n13. Muuta tietokoneesi aikavyöhykettä.\nTämä on erittäin mystinen ratkaisu, mutta toimii joskus. Paina Win + I-näppäintä -> valitse 'aika ja kieli'-osio (Time & language) -> etsi 'päivämäärä ja aika'-osio (Date & time) ja valitse toinen, eri aikavyöhyke.\n", 
"14": "\n14. Käynnistä uudelleen reititin tai modeemi tehdäksesi ns. soft boot.\nKirjoita 192.168.1.1 selaimesi osoitekenttään ja avaa reitittimen asetussivusto selaimessa. \
Käynnistä reititin uudelleen (soft boot) ja tämän jälkeen avaa selain uudestaan. Tämä mekanismi varmistaa, että reititin uudistaa IP-osoitteen jokaiseen laitteeseen, joka on reitittimeen kytketty ja ettei näiden välillä ole IP-osoitteeseen liittyviä konflikteja. \
Jos tämä ei toimi, tee ’hard reboot’ ja palauta reititin oletusasetuksiin (tarkempia ohjeita tähän löytyy tämän ohjelman 'Näkyykö 'Ei internet-yhteyttä'-kuvake oikeassa alakulmassa työpöytänäkymässä?'-osiosta, vinkistä nro 13 (WLAN-verkko) tai nro 8 (Ethernet-verkko).).\n"}
    
    if (wlanVaiEth == "wlan"):
        valinta_wlan(15, ratkaisuEhdotukset, "selain", "verkkosivusto-")
    elif (wlanVaiEth == "eth"):
        valinta_eth(15, ratkaisuEhdotukset, "selain", "verkkosivusto-")


def kuva_tietoturva():
    print(r"""                                                                         
                                                                                          ________________________________
                                                                                         /                                \
                                                                                        /   ____________________________   \
                                                                                       /   /||||||||||||    |      __   \   \
                                                                                      /   /////////////|    |       /|   \   \
                                                                                      \   \\\\\\\\\\\\\|    |   _-'/     /   /
                                                                                       \   \||||||||||||    |_____\_____/   /
                                                                                        \   \                    ' \   /   /
                                                                                         \   \_________      _______\_/   /
                                                                                          \   \        |    ||||||||\\   /
                                                                                           \   \       |    |//////// \ / 
                                                                                            \   \  /   |    |///////   \
                                                                                             \   \/    |    |//////   / \ 
                                                                                              \  /\    |    |/////   /   \ 
                                                                                               \/  \   |    |////   /     \
                                                                                               /\   \__|____|||/   /       \__
                                                                                              /  \                /        /\
                                                                                             /    \______________/             
                                                                                            /
                                                                                         __/
                                                                                          /\
    """)    
  
# Yleistietoa tietoturvauhista

def yleisteksti_tietoturva():
    print("  Yleistietoa tietoturvauhista\n\nHakkerit voivat päästä verkkoon ohjelmissa olevien haavoittuvuuksien, laitteistohaavoittuvuuksien tai käyttäjään liittyvien haavoittuvuuksien (yleisimmin heikkojen salasanojen) kautta. \
Hakkerit voivat käyttää erilaisia tiedustelutoiminnan keinoja ja verkkotyökaluja (esim. sähköpostikalasteluviestejä, salasanahyökkäyksä, ns. ping-sweepejä ja man-in-the-middle-hyökkäyksiä sekä porttien skannauksia) löytääkseen pääsyn lähiverkkoon. \
Hakkerin päästyä sisälle lähiverkkoon, joku neljästä seuraavasta uhkakuvasta voi hyvällä todennäköisyydellä toteutua:\n\n  - Tiedon varastaminen: Hakkeri voi varastaa tärkeitä tietoja esim. kiristystä varten.\n  - Datan tuhoaminen tai muuttaminen: Hakkeri \
voi tuhota tiedostoja esim. formatoimalla eli alustamalla kovalevyjä tai muuttamalla tiedostojen datan sisältöä.\n  - Identiteetin varastaminen: Hakkeri voi varastaa henkilötietoja hankkiakseen esim. asiakirjoja tai palveluita toisen ihmisen nimissä ja tiedoilla.\n\
  - Estää käyttäjää käyttämästä palveluita: Hakkeri voi tehdä DoS-hyökkäyksen verkkolaitteelle, liitäntöihin tai palvelimelle estääkseen käyttäjää pääsemästä internetiin tai muihin verkkopalveluihin.\n\nPahantahtoisten hakkereiden lisäksi tietoturvauhkia ovat erilaiset haittaohjelmat \
eli koodinpätkät ja ohjelmat, jotka ovat suunniteltu vahingoittamaan verkkolaitteita, vakoilemaan, varastamaan tietoa jne. Haittaohjelmilla on vaihtelevia vaikutuksia tietokoneen toimintaan, osan ollessa suhteellisen harmittomia ja toisten vieden tärkeitä tietoja käyttäjästä, kiristäen valuuttaa tms. \
Yleisimpiä haittaohjelmia ovat:\n\n  - Virukset: Haittaohjelma, joka asentaa kopion itsestään osaksi jotakin ohjelmaa leviten tietokoneelta toiselle. Ne tarvitsevat usein ihmisen apua päästäkseen leviämään (esim. epämääräisen linkin klikkaus).\n\
  - Madot: Viruksista poiketen madot eivät tarvitse leviämiseen toisia ohjelmia, vaan voivat levitä itsenäisesti hyödyntäen järjestelmien heikkouksia. Niiden haittavaikutukset ovat usein viruksen tapaisia.\n  - Troijalaiset: Haittaohjelma, joka naamioituu luotettavaksi ohjelmaksi. \
Aktivoituessaan tällä on hyvin vaihtelevia vaikutuksia luoden usein myös ’takaportteja’ muille haittaohjelmille päästä järjestelmään.\n  - Tiedusteluhyökkäykset: Hakkeri voi tutkia lähiverkkoa jäljittäen erilaisia palveluita, muita verkkolaitteita ja potenttiaalisia hyväksikäyttökohteita.\n")

# Tietoa WLAN-uhista

def wlan_uhat():
    print("\n  Mitä yleisiä uhkia WLAN-verkossa on?\n\nWLAN-verkko on avoin kaikille, jotka ovat tukiaseman ulottuvissa ja voivat kirjautua sille. WLAN uhat ovat vaarallisia, sillä hyökkääjän ei tarvitse välttämättä fyysisesti olla rakennuksessa toteuttaakseen niitä. Tyypillisiä uhkia ovat salakuuntelu (jos langaton liikenne ei ole salattu), \
WLAN:in luvaton käyttö (mikäli autentikointi ei ole kunnossa), DoS-hyökkäykset ja hyökkääjän asettamat tukiasemat.\n\nDoS-hyökkäykset ovat mahdollisia, jos laitteiden konfigurointi on pielessä, DoS-hyökkäyksellä voidaan ajaa koko langaton verkko alas niin ettei käyttäjät voi kirjautua. Toisaalta DoS:ja voi syntyä vahingossa muiden laitteiden aiheuttaessa häiriötä samalle aallonpituudelle (eritoten 2.4 GHz). \
Näitä ongelmia voi ehkäistä verkkolaitteiden ’koventamisella’, hyvillä salasanoilla, taajuuden monitoroinnilla ja varmuuskopioinnilla.\n\nHyökkääjän käyttämät tukiasemat (joita on usein halpaa hankkia) on helppo asettaa verkkoon varastamaan MAC-osoitteita, datapaketteja ja käyttämään ns. man-in-the-middle-hyökkäystä. \
Näiden tukiasemien toimintaa voi estää tunnistamalla aidot tukiasemat etukäteen ja käyttämällä monitorointityökaluja. MITM-hyökkäyksen voi toteuttaa monella tapaa ja yksi suosituimmista on ns. ’evil twin’-tukiaseman käyttö, erityisesti julkisessa kahvilassa, jossa on avoin WLAN käytössä. Tässä hyökkääjä konfiguroi tukiasemalle saman SSID:n kuin aidossa tukiasemassa. \
Tällöin käyttäjät voivat kirjautua hyökkääjän tukiasemaan, joka varastaa datan ja ohjaa liikenteen aidon tukiaseman kautta. Hyökkääjä voi näin varastaa tietoa, kuten salasanoja ja saada myös pääsyn käyttäjän laitteelle.\n")


# Ehkäisykeinoja WLAN-uhkiin

def wlan_ehkäisy():
    print("\n  Miten WLAN-verkon uhilta voi suojautua?\n\nLangaton signaali voi päästä seinien ja muiden esteiden läpi, aiheuttaen tietoturvariskin. Tukiasemissa voidaan käyttää kahta perustekniikka kräkkereitä vastaan, jotka ovat tosin helpohkoa kiertää: piilottaa SSID (tällöin tukiasema ei mainosta SSID:tä) ja asettaa MAC-osoitteiden suodatus päälle (ennalta määrätään MAC-osoitteet, jotka hyväksytään WLAN:ssa). \
Näitä keinoja tärkeämpiä ovatkin langattoman liikenteen autentikointi ja salaus. Autentikoinnissa on kaksi tapaa: open system authentication ja shared key authentication. Avoimessa autentikointi systeemissä ei ole vaadittua salasanaa, kaikki voivat kirjautua siihen, käyttäjällä on täysi vastuu (kannattaa käyttää VPN:ää) ja sitä käytetään tyypillisesti julkisissa paikoissa. \
Jaetun salausavaimen systeemissä käytetään autentikoinnissa ja salauksessa WEP-, WPA- tai WPA2-salausta käyttäjän ja tukiaseman välillä.\n\nKotireitittimen käyttäjällä on tyypillisesti kaksi vaihtoehtoa tunnistautumiseen: WPA tai WPA2. Tiloina näistä on joko personal tai enterprise. Personal tila on tarkoitettu koti- ja SOHO-ympäristöihin, jossa käyttäjä tunnistetaan PSK:lla eli pre-shared key-salasanalla ilman serveriä. \
Enterprise tilassa on autentikointiserveri (RADIUS), joka tunnistaa käyttäjät annetun käyttäjätunnuksen ja salasanan perusteella (tässä käytetään 802.1X standardia. Salauksella suojellaan dataa niin, ettei sitä voi paljaana tekstinä lukea. WPA ja WPA2 käyttävät TKIP (tarjoaa tuen legacy-WLAN:eille) ja AES-salausprotokollia (suositeltu). Enterprise-verkoissa, jotka vaativat parempaa salausta, käytetään (AAA) RADIUS-serveriä. \
Konfiguraatioon laitetaan RADIUS-serverin saavuttava IP-osoite, UDP-portti numerot (1812 ja 1813 tai 1645 ja 1646) sekä jaettu avain, jota käytetään tunnistamaan tukiasema serverille.\n\nMuita hyödyllisiä suojautumiskeinoja:\n\n  - Suojaa sinulle tärkeät tiedostot säännöllisesti otettavilla varmuuskopioilla (ohjeet tähän löytyy alla olevasta valikosta).\n  - Käytä luotettavaa antivirusohjelmistoa.\n  - Päivitä käyttöjärjestelmän ohjelmat automaattisesti Windows Updaten avulla.\n\
  - Käytä palomuuria, jossa on pakettien-, URL- ja ohjelmiensuodatusominaisuudet.\n  - Suojaudu sosiaaliselta manipulaatiolta ja ole varauksellinen sähköpostiin tulevista tuntemattomien viesteistä sekä tuntemattomien henkilökohtaisiin uteluihin.\n  - Käytä hyviä ja tarpeeksi pitkiä salasanoja (esim. salasanalauseita). Apuna voi käyttää myös ohjelmia salasanojen luontiin niin ettei niitä kaikkia tarvitse ulkoa muistaa.\n\n")


def kuva_varmuuskopiointi():
    print(r"""
                                                          _____________________                                  ________
                                                         /                    /|       __ __ __ __ __|\         /  SSD  /|      
                                                        /                    / |      |                \       /       / /
                                                       /                    / /|      |__ __ __ __ __  /      /_______/ /       _____ 
                                                      /____________________/ //|                     |/       |_______|/       (_USB_|P 
                                                     |_....__________-_-_-_|///|                                 ________     _____
                                                     |_____________________|///|       __ __ __ __ __|\         /  HDD  /|   (_USB_|P
                                                     |_...___............__|////      |                \       /       / / 
                                                     |_____________________|///       |__ __ __ __ __  /      /_______/ /        
                                                     |_...___________-_-_-_|//                       |/       |_______|/
                                                     |_____________________|/                             
                                                     
                                                    

    """)

# Ohje, kuinka tehdä varmuuskopiointi Windows 10:ssä

def varmuuskopioi_Win10(wlanVaiEth):
    tyhjennäRuutu()

    otsikko("Windows   10:   Varmuuskopiointi", 60)

    kuva_varmuuskopiointi()

    print("  Tiedostohistorian avulla voit suorittaa varmuuskopioinnin ulkoiseen asemaan tai verkkosijaintiin valitsemalla:\n\n  1) Aloitus.\n  2) Asetukset.\n  3) Päivitystyökalut.\n  4) Varmuuskopiointi.\n  5) Lisää asema.\n  6) Valitse ulkoinen asema (esim. USB-tikku) tai verkkosijainti varmuuskopiolle (esim. OneDrive).\n\n\
  Varmuuskopiot voi puolestaan palauttaa tiedostohistoria-toiminolla seuraavasti:\n\n  1) Kirjoita hakukenttään 'palauta tiedostot tiedostohistoria-toiminnon avulla' ja valittuasi sen pitäisi aueta 'Koti-Tiedostohistoria'-kansio.\n  2) Etsi tiedosto, jonka haluat palauttaa ja valitse se.\n  3) Tallenna tiedosto alkuperäiseen sijaintiin \
'palauta'-painikkeella tai tallenna toiseen sijaintiin napsauttamalla hiiren kakkospainiketta 'palauta'-kohdasta ja valitse 'palauta kohteeseen'.\n")

    if (wlanVaiEth == "wlan"):
        input("  --- Palataan MENU-osioon, kun painat mitä tahansa näppäintä ---")
        nav_WLAN()
    if (wlanVaiEth == "eth"):
        input("  --- Palataan MENU-osioon, kun painat mitä tahansa näppäintä ---")
        nav_Ethernet()


# Tietoa WLAN-verkon tietoturva uhista ja niiden ehkäisemisestä

def tietoturva_WLAN():
    tyhjennäRuutu()

    otsikko("WLAN-verkko:   Tietoturva", 80)

    kuva_tietoturva()

    yleisteksti_tietoturva()

    input(" --- Paina 'Enter'-nappia jatkaaksesi lukemista ---  ")
    print ("\033[A                                                         \033[A") #poistaa edellisen input-lauseen näytöltä ja siirtää kursorin rivin alkuun

    wlan_uhat()

    input(" --- Paina 'Enter'-nappia jatkaaksesi lukemista ---  ")
    print ("\033[A                                                         \033[A") #poistaa edellisen input-lauseen näytöltä ja siirtää kursorin rivin alkuun

    wlan_ehkäisy()

    while (True):
        oletuksenaNumero = None
    
        while (oletuksenaNumero == None):
            jatko = input("  Haluatko nyt:\n\n  1) Palata MENU-osioon? Paina '1'.\n  2) Lukea varmuuskopioinnin teosta Windows 10:ssä? Paina '2'\n  3) Lopettaa ohjelman? Paina '3'. ")
            try:
                oletuksenaNumero = int(jatko)
            except:
                print("\n  Ilmoita vastauksesi numerona.\n")
                
        jatko = int(jatko)

        if (jatko == 1):
            nav_WLAN()
            break
        elif (jatko == 2):
            varmuuskopioi_Win10("wlan")
            break
        elif (jatko == 3):
            print("\n  Ohjelma suljetaan")
            time.sleep(2)
            break
        else:
            print("\n  Valitse numerovaihtoehdoista 1-3.\n")


def kuva_ethYhteysPoikki():
    print(r""" 
                                                                                                        Mihin internetyhteys katosi?!?
                                                                                                          _________________________
                                                                                                         |  _____________________  |
                                                                         _____                           | |              ______ | |
                                                                        /_____\                          | |  Windows 10 /__/__/ | |
                                                                        |...._|________                  | |            /__/__/  | |
                                                                        | Eth |       /                  | |_____________________| |
                                                                        |  1  |         \________________|_________________________|
                                                                        |_____|                         / __ __ __ __ __ __ __ __  /
                                                                                                       / __ __ __ __ __ __ __ __  /
                                                                                                      / __ __ __ __ __ __ __ __  /
                                                                                                     /        ________          /
                                                                                                    /__________________________/    
    

    """)


# Ethernet-verkon navigointi eli 'menu'-valikko

def nav_Ethernet():

    tyhjennäRuutu()

    otsikko("MENU:   Ethernet-verkko", 100)

    kuva_ethYhteysPoikki()

    print("\n  Miten yhteysongelma tietokoneellasi ilmenee? Vai haluatko yleistietoa verkkoprotokollista tai tietoturvasta?\n\n\
    1) Verkkoyhteyttä ei ole tai se pätkii\n\
    2) Selain ei toimi.\n\
    3) Etsimäni verkkosivu ei löydy.\n\
    4) Muu yhteysongelma.\n\
    5) Tietoa Ethernet-verkosta.\n\
    6) Ethernet-verkon tietoturvauhat ja niiden ehkäiseminen.\n\
    7) Poistu ja sulje ohjelma kokonaan.\n")

    i = 0

    while (i < 1):

        oletuksenaNumero = None

        while (oletuksenaNumero == None):
            ongelmanValinta = input("  Valitse ylläolevista vaihtoehdoista sopiva kirjoittamalla numero: ")
            try:
                oletuksenaNumero = int(ongelmanValinta)
            except:
                print("\n  Ilmoita vastauksesi numerona.\n")

        ongelmanValinta = int(ongelmanValinta)

        if (ongelmanValinta == 1):
            print("\n  Verkkoyhteydessäsi on siis ongelmia. Yritetään vielä täsmentää ongelmaa. Valitse alla olevista vaihtoehdoista sopivin.\n\n \
   1) Pätkiikö verkkoyhteytyesi?\n \
   2) Näkyykö 'Ei Internet-yhteyttä'-kuvake oikeassa alakulmassa työpöytänäkymässä?\n \
   3) Katkesiko yhteys heti Windows 10 päivityksen jälkeen?\n \
   4) Palaa edelliseen valikkoon.\n")
        
            while (True):
                oletuksenaNumero = None

                while (oletuksenaNumero == None):
                    ongelmanTarkennettuVastaus = input("\n  Valitse sopivin vaihtoehto vastaamalla numerolla: ")
                    try:
                        oletuksenaNumero = int(ongelmanTarkennettuVastaus)
                    except:
                        print("\n  Ilmoita vastauksesi numerona.\n")

            
                ongelmanTarkennettuVastaus = int(ongelmanTarkennettuVastaus)

                if (ongelmanTarkennettuVastaus > 4):
                    print("\n  Anna vastaus numerona 1-4 väliltä.\n")
                elif (ongelmanTarkennettuVastaus == 1):
                    yhteysPätkii_eth()
                    break
                elif (ongelmanTarkennettuVastaus == 2):
                    eiInternetYhteyttäKuvake_eth()
                    break
                elif (ongelmanTarkennettuVastaus == 3):
                    päivitysOngelmaWin10("eth")
                    break
                elif (ongelmanTarkennettuVastaus == 4):
                    nav_Ethernet()
                    break

        elif (ongelmanValinta == 2):
            print("\n  Selaimesi ei siis toimi oikein. Ensin tarkentava kysymys: Näkyykö 'DNS lookup failed'-virheilmoitus selaimessa?\n\n     1) Kyllä näkyy.\n     2) Ei näy.\n     3) Palaa edelliseen valikkoon.")
            ongelmanTarkennettuVastaus = input("\n  Valitse sopivin vaihtoehto vastaamalla numerolla: ")

            if (ongelmanTarkennettuVastaus == "1"):
                dnsLookupFailed("eth")
                break
            elif (ongelmanTarkennettuVastaus == "2"):
                selainEiToimi("eth")
                break
            else:
                nav_Ethernet()
                break

        elif (ongelmanValinta == 3):
            verkkosivuEiLöydy("eth")
            break

        elif (ongelmanValinta == 4):
            print("\n  Sinulla on siis muu yhteysongelma. Valitettavasti ohjelmamme vaatii päivittämistä, jotta voisimme auttaa muissa kuin edellä esitellyissä ongelmatilanteissa.\n\n  1) Haluatko palata MENU-osioon?\n  2) Haluatko lopettaa ohjelman? Paina mitä tahansa näppäintä.")
            jatko = input("\n  Valitse sopivin vaihtoehto vastaamalla numerolla: ")

            if (jatko == "1"):
                nav_Ethernet()
                break
            else:
                print("\n  Ohjelma suljetaan.\n")
                time.sleep(2)
                break

        elif (ongelmanValinta == 5):
            tietoa_Ethernet()
            break

        elif (ongelmanValinta == 6):
            tietoturva_Ethernet()
            break

        elif (ongelmanValinta == 7):
            print("\n  Ohjelma suljetaan.")
            time.sleep(1)
    
        elif (ongelmanValinta > 7):
            print("\n  Valitse numerovaihtoehdoista 1-7.\n")
            continue
        i += 1


def kuva_ethernet():
    print(r"""                                                
                                                                                           /|                         /|
                                                                                          / /                        / /
                                                                            _____________/ /                        /_/__________
                                                                           / .....  _ . /_/________________________/   Eth NIC  /
                                                                          / .....  /_/ /(_________________________/  ._.._..  ./
                                                                         / /_ / /_/.. / /                        /  /_/ /_/   /
                                                                        /   Eth NIC  / /                        /  ......... /
                                                                       /____________/ /                        /____________/
                                                                                   / /                        / /
                                                                                  / /                        / /
                                                                                  |/                        (_/


    """)


# Tietoa Ethernetistä

def tietoa_Ethernet():
    
    tyhjennäRuutu()

    otsikko("Ethernet-tietoa", 120)

    kuva_ethernet()

    print("\nEthernet on WLAN:in ohella toinen lähiverkon teknologioista, joka on suosittu tänä päivänä. Se toimii OSI-mallin siirtoverkko- ja fyysisellä kerroksella tukien datansiirtoa 10 Mbps:ta aina 400 Gbps:n. \
Tiivistettynä Ethernet on protokolla, joka kertoo miten tietoa välitetään johtimissa.\n\n\
  Alla lyhyt yhteenveto siitä, miten Ethernet-verkko poikkeaa WLAN-verkosta:\n\n\
    - Se perustuu IEEE:n 802.3 standardiin.\n\
    - Laitteet käyttävät elektronisia signaaleja datan lähetykseen.\n\
    - Signaalin kuljattamista varten käytetään usein kuparisia UTP, STP tai Coax-kaapeleita, jotka kytketään laitteisiin.\n\
    - Ethernet-verkko tukee ns. full duplex mekanismia eli kommunikaatio eri päätelaitteiden välillä tapahtuu samanaikaisesti.\n\
    - Ethernet standardit määrittelevät verkkokortilta (NIC) toiselle kommunikoinnin säännöt ja OSI-mallin 1-2. kerroksen teknologisia ratkaisuja.\n\
    - WLAN-verkkoon verraten signaalinhäiriöitä ilmenee vähemmän sillä elektroniset signaalit saavat kulkea suojassa kaapelin sisällä.\n")

    i = 0
    while (i < 1):
    
        valinta = input("  Jos haluat lopettaa ohjelman, paina 'q' jos taas puolestaan haluat jatkaa, paina mitä tahansa muuta nappia palataksesi MENU-osioon. ")
        
        if (valinta == "q" or valinta == "Q"):
            break
        else:
            nav_Ethernet()
        i+= 1


# Valinnan läpikäynti jokaisen funktion sisällä, Ethernet-verkko

def valinta_eth(määrä, ratkaisut, protokolla, ongelman_nimi):
    while (True):

        oletuksenaNumero = None

        while (oletuksenaNumero == None):
            print("\n  1) Haluatko RATKAISUEHDOTUKSIA " + ongelman_nimi + "ongelmaasi?\n  2) Haluatko tietoa PROTOKOLLISTA, jotka usein vaikuttavat tämänkaltaisten yhteysongelmien taustalla?\n  3) Haluatko palata MENU-osioon?\n")
            valinta = input("\n  Valitse sopivin vaihtoehto vastaamalla numerolla: ")
            try:
                oletuksenaNumero = int(valinta)
            except:
                print("\n  Ilmoita vastauksesi numerona.")

        valinta = int(valinta)
        
        if (valinta == 1):
            ratkaisuEhdotukset_listaus(määrä, ratkaisut, "eth")
            time.sleep(1)
            break           
        elif (valinta == 2 and protokolla == "yhteysPätkii"):
            tietoa_protokollista_yhteysongelmat("eth")
        elif (valinta == 2 and protokolla == "selain"):
            tietoa_protokollista_selain("eth")
        elif (valinta == 2 and protokolla == "Win10"):
            tietoa_protokollista_Win10("eth")
        elif (valinta == 2 and protokolla == "dns_lookup_failed"):
            tietoa_protokollista_dnsLookUpFailed()
        elif (valinta == 3):
            nav_Ethernet()
            break
        else:
            print("\n  Valitse vaihtoehto numeroista 1-3.")
    

def kuva_yhteysPätkii_eth():
    print(r"""                                                                               
                                                                                                                                      Miksi yhteys pätkii?!?
                                                                                                                                       ___________________
                                                                                                                                      |  _______________  |
                                               _________                                                                              | |               | |
                                              |   R-1   |_____________01001001..101001010.....__1001..10011 101001011......___________| |               | |
                                              |_________|                                                                             | |_______________| |
                                                                                                                                      |___________________|   
                                                                                                                                           |         |
                                                                                                                                          /___________\


    """)


# 'Verkkoyhteys on poikki tai pätkii Ethernetissä'-osion ratkaisuehdotukset

def yhteysPätkii_eth():

    tyhjennäRuutu()

    otsikko("Verkkoyhteys   katkeilee", 100)

    kuva_yhteysPätkii_eth()

    ratkaisuEhdotukset = {"1": "\nEli verkkoyhteytesi pätkii. Kokeillaan muutamaa keinoa tämän korjaamiseksi.\n\
\n1. Käytä vianmääritysohjelmaa (Network troubleshooter).\nVianmääritysohjelma auttaa diagnosoimaan yleisimpiä verkon ongelmia. Sitä voi käyttää klikkaamalla: \
aloitus (Start) -> asetukset (Settings) -> verkko ja internet (Network & Internet) -> tila (Status) -> valitse 'verkon vianmääritys' -> noudata ohjeita ja katso, korjautuuko ongelma.\n",
"2": "\n2. Tarkista internetpalveluntarjoajasi eli ISP:n ilmoitukset lähialueesi mahdollisista yhteysongelmista.\nYhteysongelmat voivat johtua palveluntarjoajasta ja onkin hyvä tarkastaa heidän ilmoitukset mikäli yhteys pätkii ja muuta ilmeistä selitystä ei löydy esimerkiksi reitittimestäsi tai PC:stäsi.\n",
"3": "\n3. Päivitä tai asenna uusiksi verkkokortin (verkkosovittimen) ohjaimet ja tarkista sen yhteensopivuus Windows Updaten kanssa.\nKlikkaa aloita-painiketta (Start) -> laitehallinta (Device Manager) ja valitse sieltä verkkosovittimet (Network adapters) -> oikealla hiirenpainikkeella oikean verkkosovittimen kohdalta valitse päivitä ohjain (Update driver). \
Adapterin uudelleen asentamisessa valitse päivityksen sijaan 'poista' (Uninstall device) -> käynnistä tietokone ja anna Windowsin asentaa ohjaimen versio tai lataa verkosta ja asenna itse. Voit myös tarkistaa verkkokortin fyysisen kunnon avaamalla tietokoneen kotelon (tähän löytyy tarkempia ohjeita internetistä; muista käyttää ESD-mattoa ym.).\n",
"4": "\n4. Suorita haittaohjelmien varalta tarkistus haittaohjelmantorjuntaohjelmistollasi.\nErilaiset virukset PC:llä tai reitittimellä voivat aiheuttaa yhteysongelmia. On olemassa tiettyjä merkkejä, jotka viittaavat reitittimessä olevan viruksia tai mahdollisen hakkeroinnin kohde: \
Tietokone toimii tavallista hitaammin, internet-haut ohjautuvat omituisille sivustoille tai uusia työkalupalkkeja (toolbars) ilmestyy itsestään selaimeen.\n",
"5": "\n5. Kokeile komentokehotteessa yhteysongelmien korjausta.\nKokeile komentokehotteessa seuraavien komentojen avulla TCP/IP-pinon manuaalista nollaamista, IP-osoitteen vapauttamista ja uusimista sekä DNS-asiakasohjelman välimuistin tyhjentämistä:\n\
  a. netsh winsock reset + enter.\n  b. netsh in tip reset + enter.\n  c. ipconfig /release + enter.\n  d. ipconfig /renew + enter.\n  e. ipconfig /flushdns + enter.\n"}
    
    valinta_eth(6, ratkaisuEhdotukset, "yhteysPätkii", "Ethernet-verkon yhteys")


def kuva_eiInternetYhteyttä_eth():
    print(r"""              
                                                                                              \   |
                                                                                                       /            Mihin internetyhteys katosi? Miksi data ei kulje?
                                        ___________________________________________________     \ |          __________________________________________________________
                                                                                           }----    /  -----{
                                        01001001 01000100 10010010 10010100 00101001 010100}---- 01??  -----{                                                           
                                        ___________________________________________________}---- /  \  -----{__________________________________________________________
                                                                                                  |                 
                                                                                                /      \
                                                                                                  |
                                                           
                                                          
    """)


# 'Ei internetyhteyttä Ethernetissä'-osion ratkaisuehdotukset

def eiInternetYhteyttäKuvake_eth():

    tyhjennäRuutu()

    otsikko("Verkkoyhteys   on   poikki", 100)

    kuva_eiInternetYhteyttä_eth()

    ratkaisuEhdotukset = {"1": "\nEli sinulla ei ole internetyhteyttä jostakin syystä. Kokeillaan muutamaa keinoa.\n\
\n1. Käytä vianmääritysohjelmaa (Network troubleshooter).\nVianmääritysohjelma auttaa diagnosoimaan yleisimpiä verkon ongelmia. Sitä voi käyttää klikkaamalla: \
aloitus (Start) -> asetukset (Settings) -> verkko ja internet (Network & Internet) -> tila (Status) -> valitse 'verkon vianmääritys' -> noudata ohjeita ja katso, korjautuuko ongelma.\n",
"2": "\n2. Tarkista internetpalveluntarjoajasi eli ISP:n ilmoitukset lähialueesi mahdollisista yhteysongelmista.\nYhteysongelmat voivat johtua palveluntarjoajasta ja onkin hyvä tarkastaa heidän ilmoitukset mikäli yhteys pätkii ja muuta ilmeistä selitystä ei löydy esimerkiksi reitittimestäsi tai PC:stäsi.\n",
"3": "\n3. Yritä muodostaa yhteys toiseen laitteeseen. \nYritä muodostaa yhteys toiseen kannettavaan tietokoneeseen tai puhelimeen, joka on samassa verkossa. \
Jos niissäkin on yhteysongelmia, vika voi olla reitittimessä, modeemissa tai palveluntarjoajalla.  Jos puolestaan yhteys toimii muussa laitteessa, ongelman aiheuttaja on todennäköisesti alkuperäinen laite. \
Tarkista tällöin laitteiston tai käyttöjärjestelmän vikoja ja siirry laitteen verkon vianmääritykseen.\n",
"4": "\n4. Päivitä tai asenna uusiksi verkkokortin (verkkosovittimen) ohjaimet ja tarkista sen yhteensopivuus Windows Updaten kanssa.\nKlikkaa aloita-painiketta (Start) -> laitehallinta (Device Manager) ja valitse sieltä verkkosovittimet (Network adapters) -> oikealla hiirenpainikkeella oikean verkkosovittimen kohdalta valitse päivitä ohjain (Update driver). \
Adapterin uudelleen asentamisessa valitse päivityksen sijaan 'poista' (Uninstall device) -> käynnistä tietokone ja anna Windowsin asentaa ohjaimen versio tai lataa verkosta ja asenna itse. Voit myös tarkistaa verkkokortin fyysisen kunnon avaamalla tietokoneen kotelon (tähän löytyy tarkempia ohjeita internetistä; muista käyttää ESD-mattoa ym.).\n",
"5": "\n5. Tarkista Windows:n järjestelmäkansiot.\nYhteysongelmat voivat johtua korruptoituneista Windows järjestelmäkansioista. Nämä voi tarkistaa system file checker-ohjelmalla (SFC). \
Tämä tehdään avaamalla CMD ja suoritetaan DISM eli Deployment Image Servicing and Management-työkalu komennolla: dism.exe /online /cleanup-image /restorehealth. DISM käyttää Windows Updatea päivittääkseen korruptoituneet kansiot uusiin. \
Tämä jälkeen voidaan skannata korruptoituneita kansioita ja vaihtaa ne uusiin komennolla: sfc /scannow. Skannerin jälkeen saadaan ilmoitus tuloksista: korruptoituneita kansioita ei löytynyt, toimintoa ei voitu suorittaa (SFC pitää suorittaa tällöin ’Safe Modessa’), \
korruptoituneita kansioita löydettiin ja ne vaihdettiin onnistuneesti tai niitä löydettiin muttei onnistuttu korjaamaan. Skannauksen tulokset voi kopioida tekstitiedostoon tarkasteltavaksi komennolla: findstr /c:'[sr]' %windir%\logs\cbs\cbs.log >%userprofile%\desktop\sfcdetails.txt'. \
Tiedostosta voi etsiä päivämäärien ja ajanperusteella korruptoituneita tiedostoja ja korvata ne manuaalisesti seuraavalla tavalla. Ota ensin korruptoitunut tiedosto hallintaan komennolla: takeown /f <korruptoituneen tiedoston sijainti>. Anna ylläpitäjälle oikeus tiedostoon komennolla: icacls <tiedoston sijainti> /grant administrators:f. \
Kopioi ja liitä toimiva tiedosto korruptoituneen tilalle komennolla: copy <toimivan tiedoston sijainti> <korruptoituneen tiedoston sijainti>. \n",
"6": "\n6. Tarkista tietoturvasovellusten konfliktit. \nTietoturvasovellukset, kuten haittaohjelmantorjuntaohjelmisto tai palomuuri voivat aiheuttaa yhteysongelmia. Tarkista näiden sovellusten asetukset ja katso, minkälainen verkkoliikenne on sallittua. Voit väliaikaisesti kokeilla lakkauttaa näiden ohjelmistojen toiminnan tai tietyjen verkkoliikennemääritysten osalta ja katsoa, paraneeko yhteys. \
Jos näin on, tarkista haittaohjelmantorjuntaohjelmiston ja palomuurin toimittajalta, josko yhteyttä haittaavat asetukset ovat tärkeitä laitteiden suojaamisessa. Jos eivät, jätä ne pois päältä. Voit harkita myös Windows-ympäristöön sopivia, kolmansien osapuolten suunnittelemia helppokäyttöisiä ja ilmaisia palomuureja, kuten ZoneAlarm.\n",
"7": "\n7. Kokeile komentokehotteessa yhteysongelmien korjausta.\nKokeile komentokehotteessa seuraavien komentojen avulla TCP/IP-pinon manuaalista nollaamista, IP-osoitteen vapauttamista ja uusimista sekä DNS-asiakasohjelman välimuistin tyhjentämistä:\n\
  a. netsh winsock reset + enter.\n  b. netsh in tip reset + enter.\n  c. ipconfig /release + enter.\n  d. ipconfig /renew + enter.\n  e. ipconfig /flushdns + enter.\n",
"8": "\n8. Resetoi eli palauta verkko oletusasetuksiin. \nTämä on viimeinen keino, jota kannattaa kokeilla, jos muu ei toimi. Verkon resetointi voi auttaa ratkaisemaan myös muita yhteysongelmia, jotka ilmaantuvat, kun olet päivittämässä Windows 10:ä, \
tai tilanteessa, kun voit muodostaa yhteyden internetiin, mutta et voi muodostaa yhteyttä jaettuihin verkkoasemiin. Verkkoasetusten palauttaminen poistaa kaikki asentamasi verkkosovittimet ja niiden asetukset. Kun tietokone käynnistetään uudelleen, järjestelmä asentaa verkkosovittimet uudelleen käyttämällä niiden oletusasetuksia. \
Verkon resetoimiseksi voi klikata:\n  a. Aloitus (Start) -> asetukset (Settings) -> verkko ja internet (Network & Internet)-> tila (Status) -> verkon määritys uudelleen -> määritä. \n  b. Valitse verkkoasetusten palautusnäytössä ’palauta nyt’ ja vahvista valinta valitsemalla kyllä. Odota tietokoneen uudelleen käynnistystä ja tarkista, korjautuiko ongelma.\n\
  c. Kun olet palauttanut verkon oletusasetukset, saatat joutua asentamaan tai määrittämään uudelleen muita käyttämiäsi verkko-ohjelmistoja, kuten VPN-asiakasohjelmiston tai Hyper-V:n virtuaalikytkimet.\n"}

    valinta_eth(9, ratkaisuEhdotukset, "selain", "selain")


# Tietoa Ethernet-verkon uhista

def ethernet_uhat():
    print("\n  Mitä yleisiä uhkia Ethernet-verkossa on?\n\nAlla luetellut uhat eivät teknisesti ottaen ole Ethernet-verkon tasoisia eli OSI-mallin 1-2 kerroksen uhkia (kyseiset uhkat liittyvät enemmän kytkinten suojaamiseen ja yritysverkkoihin), mutta ovat kuitenkin hyvä pitää mielessä aina verkossa oltaessa. Raja eri verkkokerrosten välillä on sen verran abstrakti ettei ole aina selkeää missä mennään. Yleisiä verkossa vastaantulevia uhkia ovat siis:\n\n\
  - Virukset, jotka leviävät pääosin kahta kautta: USB-tikulta tai muusta siirrettävästä mediasta ja sähköpostiliitteistä.\n  - Kalasteluviestit ja muu sosiaalinen manipulointi.\n  - Hakkereiden tekemät porttiskannaukset. Haittavaikutusten ehkäistäksesi älä suorita tietokoneellasi palveluita tai ohjelmia, joista et ymmärrä mitä ne ovat.\n  - Troijalaiset, jotka leviävät verkkoasemilta \
(esim. Back Orifice ja NetBus ovat Windows-ympäristössä pahamaineisia). Paras suojautuminen trojalaisia vastaan on olla avaamatta sähköpostien liitteitä.\n")

# Tietoa

def ethernet_ehkäisy():
    print("\n  Miten Ethernet-verkossa ulkoverkon uhilta voi suojautua?\n\nHyödyllisiä suojautumiskeinoja:\n\n  - Suojaa sinulle tärkeät tiedostot säännöllisesti otettavilla varmuuskopioilla (ohjeet tähän löytyy alla olevasta valikosta).\n  - Käytä luotettavaa antivirusohjelmistoa.\n  - Päivitä käyttöjärjestelmän ohjelmat automaattisesti Windows Updaten avulla.\n\
  - Käytä palomuuria, jossa on pakettien-, URL- ja ohjelmiensuodatusominaisuudet.\n  - Suojaudu sosiaaliselta manipulaatiolta ja ole varauksellinen sähköpostiin tulevista tuntemattomien viesteistä sekä tuntemattomien henkilökohtaisiin uteluihin.\n  - Käytä hyviä ja tarpeeksi pitkiä salasanoja (esim. salasanalauseita). Apuna voi käyttää myös ohjelmia salasanojen luontiin niin ettei niitä kaikkia tarvitse ulkoa muistaa.\n\n")

# Tietoa Ethernet-verkon tietoturva uhista ja niiden ehkäisemisestä

def tietoturva_Ethernet():
    tyhjennäRuutu()

    otsikko("Ethernet-verkko:   Tietoturva", 75)

    kuva_tietoturva()

    yleisteksti_tietoturva()
    input(" --- Paina 'Enter'-nappia jatkaaksesi lukemista ---  ")
    print ("\033[A                                                         \033[A") #poistaa edellisen input-lauseen näytöltä ja siirtää kursorin rivin alkuun

    ethernet_uhat()

    input(" --- Paina 'Enter'-nappia jatkaaksesi lukemista ---  ")
    print ("\033[A                                                         \033[A") #poistaa edellisen input-lauseen näytöltä ja siirtää kursorin rivin alkuun

    ethernet_ehkäisy()

    while (True):
        oletuksenaNumero = None
    
        while (oletuksenaNumero == None):
            print("  Haluatko nyt:\n\n  1) Palata MENU-osioon?\n  2) Lukea varmuuskopioinnin teosta Windows 10:ssä?\n  3) Lopettaa ohjelman?\n")
            jatko = input("\n  Valitse sopivin vaihtoehto vastaamalla numerolla: ")
            try:
                oletuksenaNumero = int(jatko)
            except:
                print("\n  Ilmoita vastauksesi numerona.\n")
                
        jatko = int(jatko)

        if (jatko == 1):
            nav_Ethernet()
            break
        elif (jatko == 2):
            varmuuskopioi_Win10("eth")
            break
        elif (jatko == 3):
            print("\n  Ohjelma suljetaan")
            time.sleep(2)
            break
        else:
            print("\n  Valitse numerovaihtoehdoista 1-3.\n")


def kuva_aloitus():
    print(r"""                                                                                 
                                                                                                  Tämä on:
                                                                           Verkkoyhteyden vianmääritysohjelma Windows 10 PC:lle 
                                                                                      Ohjelmointi: Veli Heikki Vesala
                                                                                         _________________________
                                                                                        |  _____________________  |
                                                                                        | |              ______ | |
                                                                                        | |  Windows 10 /__/__/ | |
                                                                                        | |            /__/__/  | |
                                                                                        | |_____________________| |
                                                                                        |_________________________|
                                                                                       / __ __ __ __ __ __ __ __  /
                                                                                      / __ __ __ __ __ __ __ __  /
                                                                                     / __ __ __ __ __ __ __ __  /
                                                                                    /        ________          /
                                                                                   /__________________________/    
    

    """)

# Pääohjelma
kokoIkkunaNäyttö()

print("")
otsikko("Tervetuloa!", 150)

kuva_aloitus()

print("\nKatkesiko verkkoyhteytesi? Etkö kenties pääse YouTubesta haluamaasi videota katselemaan? Tämän verkkoyhteyden vianmääritysohjelman tarkoituksena on auttaa sinua paikantamaan ja korjaamaan tietokoneesi verkkoyhteyden vikoja ja yhdistämään sinut internetiin uudestaan.\n\n\
Aluksi, hyvä käyttäjä, on kuitenkin syytä mainita, että tämä ohjelma on vasta prototyyppi ja suunniteltu ainoastaan Windows 10 PC:n internetyhteyteen liittyviin ongelmatilanteisiin ja toimimaan vain Windows-ympäristössä. Ohjelman toimintaperiaate on seuraava: Annat ensin kuvauksen yhteysongelmastasi annettujen vaihtoehtojen perusteella ja \
ohjelma pyrkii tarjoamaan sinulle ratkaisuehdotuksia teknisesti vaivattomimmasta toimenpiteestä alkaen aina 'radikaalimpaan' ratkaisuvaihtoehtoon. Ehdotukset voivat toimia vaihtelevalla menestyksellä, sillä tietoverkkoja, käytössä olevia verkkolaitteita ja niissä esiintyviä ongelmatilanteita on hyvin monia erilaisia. \
Halutessasi voit ohjelman avulla myös laajentaa yleistietoasi ja lukea internetyhteyksien taustalla vaikuttavista protokollista, joista on pyritty kertomaan kansantajuisesti menemättä liikaa teknisiin yksityiskohtiin. Lisäksi tarjolla on tietoa WLAN- ja Ethernet-verkkojen yleisimmistä tietoturvauhista ja keinoista suojautua näiltä.\n\n\
Yritetäänpä nyt kuitenkin ratkaista käsillä oleva, akuutti yhteysongelmasi ja aivan aluksi yrittää paikantaa se. Kerrotko ensiksi:\n\n  Käytätkö WLAN eli langatonta lähiverkkoa vai Ethernet eli langallista lähiverkkoa?\n")

while (True):
    oletuksenaNumero = None
    
    while (oletuksenaNumero == None):
        print("  1) Käytän WLAN-verkkoa.\n  2) Käytän Ethernet-verkkoa.")
        vastausWLANvaiEthernet = input("\n  Valitse sopivin vaihtoehto vastaamalla numerolla: ")
        try:
            oletuksenaNumero = int(vastausWLANvaiEthernet)
        except:
            print("\n  Ilmoita vastauksesi numerona.\n")
                
    vastausWLANvaiEthernet = int(vastausWLANvaiEthernet)

    if (vastausWLANvaiEthernet == 1):
        nav_WLAN()
        break
    elif (vastausWLANvaiEthernet == 2):
        nav_Ethernet()
        break
    else:
        print("\n  Valitse numerovaihtoehdoista 1-2.\n")
           
    

    







