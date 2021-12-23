# Loppuraportti 

### Jäsenet: 

Roni Tammisalo (Github: rtammisalo) 

Markus Meriläinen (Github: Makakoodi) 

Juho Herranen (Github: J-Uhero) 

Zhishang Chen (Github: Chester-CH) 

 

## Kohdatut ongelmat (prosessi, projektityöskentely, tekniset): 

### Sprint 1 

Ryhmämme aloitustilaisuus ja katselmoinnit tapahtuivat kampuksella, joten tapasimme ryhmänä livenä kerran viikkossa. Alun tapaamisessa ehdimme määritellä product backlogin storyineen, mutta jouduimme jäämään vielä sen jälkeen kokoustamaan kampukselle taskien ja alustavan arkkitehtuurin määrittelyä varten, joka osoittautui aikaa vieväksi, joten saimme tehtyä vain osan alkutoimista ja esimerkiksi ja työmääräarvioiden tekeminen jäi myöhemmin etänä tehtäväksi. Sovimme alkutapaamisessa käyttävämme Telegramia pääasiallisena kommunikointikanavana ja sovellusarkkitehtuurin pohjautuvan Ohtesta tuttuun repository-/kerrosarkkitehtuuriin, vaikka lopulta sovelluksessamme erillisen sovelluslogiikan merkitys jäi vähäiseksi käyttöliittymän, lukuvinkki-olioiden ja tietokantarajapinnan käytön rinnalla.  

Robotti-testien toiminta/asentaminen aiheutti hieman päänvaivaa alussa. Projektityöskentely kärsi huomattavasti kommunikaation puutteesta ja ryhmästä jopa lähti juuri ennen sprintin loppua pois yksi jäsen asiasta ilmoittamatta. Scrumiin liittyvän läheisen ryhmätyöskentely ei onnistunut muutamaa yksilöllistä Zoom-kokoontumista lukuunottamatta ja silloinkin aika meni pitkälti Pythonista keskusteluun. Ryhmä ei ollut toisaalta sopinut erikseen pitävänsä live-keskustelu/zoom-tapaamisia. Telegram-kanavalla keskustelun aktiivisuus oli vaihtelevaa. Product backlogin ja sprint backlogin päivittäminen excelissä oli ongelmallista. Aloitus- ja konfiguraatioasiat  saatiin tehtyä loppuun projektin aloitusviikolla, mutta muuten ensimmäistä user storya koskeva työ kasaantui pääasiassa seuraavan viikon alkuun maanantaille ennen katselmointia. Työtaakka jakautui epätasaisesti. Katselmoinnissa ja sen jälkeen käydyssä retrospektiivissä sprintin ongelmat nousivat selkeästi esille. 

Ohjelmistoarkkitehtuuri oli joillekin ryhmässä vieras ja siihen totuttelu vei aikaa. 

Vastuunjaossa projektissa luotettiin siihen, että osalliset itse valitsevat itselleen tehtäväksi mieluisia taskeja ja merkkaavat taskien kohdalle sprint backlogiin “checked out”, kun aloittavat niitä tekemään. Kohdallamme ongelmaksi tässä nousi, että jos joku valitsee taskin itselleen, mutta sen aloitus/tekeminen viivästyy, niin storyn tekeminen voi jäädä jumiin. Lisäksi jotkin taskit, kuten robot-testaus jäi yleensä viimeiseksi tehtäväksi, joten myöhimpään työskentelynsä alottaneilla ei välttämättä ollut enää valinnan varaa taskien suhteen ja tehtäväksi jäi taski, jonka asia ei ollut entuudestaan tuttua, eikä aikaa ollut enää juuri asiaan perehtymiseen.
 

### Sprint 2

Sprintin retrossa läpikäytyjä ongelmia ei kaikkia kyetty poistamaan. Excel-ongelmat jatkuivat.

 Työn nähtiin myös sujuneen paremmin kuin ensimmäisessä sprintissä.

Tasainen työjako, sprint 3:ssä oli huomattavasti työläämpiä storyjä kuin muissa sprintissa, ja ehkä ei ole hyvä idea antaa liian isoja user storyjä viimeiselle viikolle.

### Sprint 3 

Aikaisemmin tehtyjen robotti-testien rikkoutuminen ja jatkuva korjailu vei aikaa. Ryhmätyöskentely oli heikkoa, sillä suurin osa ryhmän jäsenistä osallistui sprinttiin vasta viimeisinä päivinä. Kommunikaatiossa olisi ollut myös parannettavaa sen osalta, että ryhmän kesken olisi selkeämmin ilmoitettu, mitä asioita ja muutoksia tehdään ja ilmoituksia olisi seurattu, minkä vuoksi aikaa meni myös merge-konfiktien korjaamiseen ja tehtyä työtä hukkaan. Excelin kanssa oli osalla edelleen ongelmia. 

## Mikä projektissa sujui hyvin/parannusehdotuksia ensikertaa varten 

Parannusehdotuksina voisi mainita esim. daily scrumin käyttöönoton jossain muodossa, vaikkapa kerran viikossa keskellä sprinttiä. Jonkin sortin tiedonjakoalusta(Discord?) olisi ollut hyvä, missä voice chattiin liittyminen ja ruudunjako on matalan kynnyksen takana. Tämä kannustaisi kaikkia jäseniä jollain tavalla asennoitumaan jatkuvampaan kehittämiseen niin, ettei kaikki työ jäisi viimeiselle päivälle. Puhumalla on myös ehkä helpompi kysyä apua ja neuvoa, jos jää jumiin tai ei edes tiedä miten edetään. Projektissa ei myöskään ollut scrum masterin roolissa olevaa henkilöä, joka voisi kysellä avuntarpeesta ja projektin tilasta, mikä varmaankin myös kannustaisi aktiivisempaan työotteeseen. 

Product backlogin ja sprint backlogien hallinnassa kannattaa käyttää jotain softaa, jonka toiminnasta jo ainakin joku ryhmän jäsenistä tuntee. Ryhmän käytössä ollut Excel-spreadsheet ei roolissaan kovin hyvin onnistunut ja sen toiminnan opettelu aiheutti huomattavaa taakkaa työmäärässä. Kuusi tuntia viikossa on liian lyhyt aika, varsinkin jos siitä pelkkä prosessinhallintasoftan kanssa säätäminen vie vielä tunnin tai kaksi. 

Ryhmän olisi myös kannattanut perehtyä paremmin toistensa osaamistasoihin ja jakaa työtehtävät enemmän sen pohjalta. Kaikkien olisi kuitenkin pitänyt osallistua product backlogin ja sprint backlogien ylläpitoon, eikä jättää sitä vain yhden tai kahden tehtäväksi. Projektissahan kuitenkin oli tarkotus opetella koko Scrum-frameworkin käyttöä.

## Mitä halusimme oppia, mitä opimme ja mikä oli turhaa 

Excelin käyttöä ainakin osalla ryhmästä tuli pakosta harjoiteltua, mikä aiheutti päänvaivaa, mutta toi myös kokemusta ja varmaan hieman osaamistakin sen käyttöön. Kurssimateriaalissa muutaman tehtävän verran harjoiteltua Robot Frameworkin käyttöä tuli opeteltua uutena asiana hieman lisää käytännössä. Ryhmän vähemmän osaavat oppivat myös paljon pythonista ja ohjelman arkkitehtuurista kokeneemmilta jäseniltä. Ryhmätyöskentelyssä antoisinta oli nähdä harjaantuneempien ryhmäläisten ratkaisuja esimerkiksi UI:n ja olioiden toteutuksesta, joten projektissa näki erilaisia toteutus- ja lähestymistapoja sovelluksen eri osa-alueisiin, joita tuskin ei olisi itse tajunnut toteuttaa vastaavalla tavalla. Näin ollen projekti antoi myös perspektiiviä yleisestikin sovelluksien toteuttamiseen. 
