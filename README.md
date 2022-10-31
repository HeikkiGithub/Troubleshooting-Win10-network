## Verkkoyhteyden vianmääritysohjelma Windows 10 PC:lle


Tämän vianmääritysohjelman tarkoituksena on auttaa käyttäjää paikantamaan ja korjaamaan Windows 10-käyttöjärjestelmällä toimivan tietokoneen verkkoyhteyden vikoja ja yhdistämään käyttäjä verkkoon uudestaan.


### Ohjelman kuvaus

Ohjelma on suunniteltu ainoastaan Windows 10 PC:n verkkoyhteyteen liittyviin ongelmatilanteisiin ja toimimaan vain Windows-ympäristössä. Se tarjoaa lyhyen ongelmanrajauksen jälkeen ratkaisuehdotuksia, joita käyttäjä voi kokeilla saadaakseen verkkoyhteyden palaamaan. Ratkaisuehdotukset voivat toimia vaihtelevalla menestyksellä, sillä tietoverkkoja, käytössä olevia verkkolaitteita ja niissä esiintyviä ongelmatilanteita on hyvin monia erilaisia. Halutessaan ohjelman avulla voi myös lukea verkkoyhteyksien taustalla vaikuttavista protokollista, joista on pyritty kertomaan kansantajuisesti menemättä liikaa teknisiin yksityiskohtiin. Lisäksi tarjolla on tietoa WLAN- ja Ethernet-verkkojen yleisimmistä tietoturvauhista ja keinoista suojautua niiltä.

Alla esimerkkikuva ohjelmasta ja sen ulkoasusta. Ohjelma toimii komentoriviltä ja siinä on käytetty yksinkertaista ASCII-taidetta. 

![Ohjelman aloituskuva](https://github.com/HeikkiGithub/Troubleshooting-Win10-network/blob/main/kuvat/ohjelma_tervetuloa.png)


### Ohjelman saattaminen toimintakuntoon

Ohjelma on kirjoitettu python ohjelmointikieltä käyttäen ja tallennettuna python-tiedostoon (merkitään .py päätteellä). Tällaisten tiedostojen suorittaminen on varsin helppoa, sillä siihen tarvitaan vain Python-ohjelma. Alla pikaiset ohjeet pythonin asennuksesta ja vianmääritysohjelman käynnistämisestä:

1. Jos sinulla ei ole Python-ohjelmistoa asennettuna tietokoneellesi, käy lataamassa siitä käyttöjärjestelmällesi sopiva versio osoitteesta: https://www.python.org/downloads/.
2. Lataa GitHub-repossani oleva python-tiedosto Verkkoyhteyden vianmääritysohjelma Windows 10 PC.py esimerkiksi firefox-selaimessa seuraavasti: valitse 'Raw'-painike -> Ctrl + A tai 'Valitse kaikki'-painikke -> liitä sisältö tekstinkäsittelyohjelmaan (muistioon tms.) ja anna sille nimi .py päätteellä -> suorita ohjelma kaksioisklikkaamalla tai kakkospainike -> Avaa sovelluksessa -> Python.


### Ohjelman käyttöohjeet

Ohjelman käyttö ei vaadi käyttäjältä muuta, kuin Enter- ja numeronäppäimien, käyttöä.

Ohjelma toimii seuraavasti: 
  1. Aluksi käyttäjä kertoo ohjelmalle, onko hänellä käytössä langaton WLAN- vai langallinen Ethernet-verkko.
  2. Menu-valikossa käyttäjä voi etsiä ratkaisua verkkoyhtyeysongelmaansa tai hakea halutessaan tietoa tietoturvasta ja verkkoprotokollista.
  3. Mikäli käyttäjä etsii sillä hetkellä verkkoyhteysongelmaan ratkaisua, ohjelma pyrkii rajaamaan yhteysongelman syytä antamalla käyttäjälle muutaman vaihtoehdon, joista tämä valitsee sopivimmalta vaikuttavan numerolla.
  4. Kun ongelman rajaus on tehty käyttäjä voi valita: ottaako vastaan yhteysongelmaan ratkaisuehdotuksia, tietoa käsillä olevan ongelman taustalla tyypillisesti vaikuttavista verkkoprotokollista tai palata menu-osioon.
  5. Mikäli käyttäjä pyytää ratkaisuehdotuksia, ohjelma tarjoaa niitä yksi kerrallaan, jolloin ideana on, että käyttäjä kokeilee ratkaisun toimivuutta ja jos ongelma ei ratkea, käyttäjä voi pyytää lisäehdotuksia kokeiltavaksi kunnes ongelma ratkeaa tai ehdotukset loppuvat kesken. Ratkaisuehdotukset on pyritty esittämään toteutukseltaan teknisesti vaivattomimmasta 'radikaalimpaan' ratkaisuvaihtoehtoon.
  6. Ohjelma lopettaa toimintansa jos ratkaisu löytyy tai mikäli käyttäjä niin haluaa (useimmissa valikoissa on lopetus-vaihtoehto).

Alla kuva vianmääritysohjelman menu-valikosta.

![Kuva ohjelman menu-valikosta](https://github.com/HeikkiGithub/Troubleshooting-Win10-network/blob/main/kuvat/ohjelma_menu.png)


### Mihin ongelmaan ohjelma pyrkii etsimään ratkaisua?

On paljon ihmisiä, joilla ei ole taustalla mitään teknistä koulutusta tai käsitystä siitä, mitä kannattaisi kotioloissa kokeilla, jos esimerkiksi verkkoyhteys langattomasta reitittimestä pettää. Ohjelma yrittää auttaa vaihe vaiheelta selkeillä ohjeilla kokematontakin käyttäjää kokeilemaan eri keinoja verkkoyhtyden palauttamiseen.


### Miksi tein ohjelman ja mikä motivoi sen tekoon?

Ohjelma on tehty puhtaasti oppimismielessä ja se syntyi osittain vahingossa suuremman vianmääritysohjelma-projektin sivutuotteena. Sen pääasiallisena tarkoituksena on jäsentää itselleni tavallisimpien verkkoprotokollien toimintaa, antoi mahdollisuuden opiskella python-ohjelmointia, kehittää ongelmanratkaisutaitojani ja luovuutta sekä opettaa ohjelmointiprosessin perusteita. Koulutyön ohella tällaisten itseä motivoivien, kokeellisten projektien tekeminen on paitsi hauskaa, myös opettavaista. 


### Mitä opin projektista?

Projektin myötä opin, että suunnitelmallisuus on erittäin tärkeä osa ohjelmointiprosessia. Vaikka suunnitelmien tekoon voi kulua paljonkin aikaa, oikein tehtynä ja hyvällä suunnitelmalla itse ohjelmoinnissa säästyy lopulta aikaa, kun tietää mitä ohjelmalla haluaa saada aikaan eikä summittaisesti vain koodaa hetken huumassa. Tärkeä osa oppimista oli yrittää keksiä loogisesti toimiva, vähäeleinen ohjelma, joka olisi selkeä käyttäjälle. Tämän onnistumisesta voi olla montaa mieltä, sillä ohjelman toimintalogiikan olisi voinut toteuttaa hyvinkin eri tavalla ja pelkän tekstin lukeminen näytöltä ilman muita silmiin pistäviä elementtejä on hieman puuduttavaa. Projektin aikana oli viihdyttävää myös pikaisesti kokeilla ASCII-taiteen tekoa.


### Projektin mahdollinen tulevaisuus?

Ohjelmassa on valtavasti kehittämisen kohteita. Ensinnäkin ohjelmaa pitäisi testata todellisissa tilanteissa ja kehittää sen pohjalta lisää. Tämä versio ei ole silmälle kaikkein ystävällisin, vaikka ohjelma rakenteeltaan onkin suhteellisen selkeä. Sen asetteluita voisi tulevaisuudessa päivittää (mm. laajalla ruudulla teksti ei ole keskitetty ja minkänlaisia marginaaleja ei ole). Yksi ratkaisu tähän olisi toteuttaa ihan oma graafinen käyttäjärajapinta, jolloin ASCII-taiteenkin voisi korvata jollakin näyttävämmällä. Myös pikkuhiljaa yleistymässä olevan Windows 11-käyttöjärjestelmän vuoksi ohjelman voisi päivittää koskettamaan sitä Windows 10:n sijaan. 


### Ohjelman tekijä

@HeikkiGithub
