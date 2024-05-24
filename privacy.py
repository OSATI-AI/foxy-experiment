from nicegui import ui, context

@ui.page('/privacy')
def privacy():

    # Set the style for the entire page to change the background color
    ui.query('body').style(f'background-color: #f1efed')
    # context.client.content.classes('supports-[height:100cqh]:h-[100cqh] supports-[height:100svh]:h-[100svh]')

    ui.add_css(r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}')
    ui.query('.nicegui-content').classes('w-full')

    # header
    with ui.row().classes('w-full h-[10%] no-wrap'):
        with ui.column().classes('w-0 sm:w-[3%] -ml-6 sm:m-0 h-full no-wrap'):
            pass

        with ui.column().classes('w-[97%] h-full no-wrap'):
            with ui.link('', "/"):
                ui.image('media/foxy_header.png').classes('w-80')

    with ui.row().classes('w-full h-auto no-wrap'):
            with ui.column().classes('w-0 sm:w-[3%] -ml-6 sm:m-0 h-full no-wrap'):
                pass

            with ui.column().classes('w-[97%] h-full no-wrap'):
                ui.markdown('''
                    # Datenschutzerklärung

                    ## <a name="m716"></a>Präambel

                    Mit der folgenden Datenschutzerklärung möchten wir Sie darüber aufklären, welche Arten Ihrer personenbezogenen Daten (nachfolgend auch kurz als "Daten" bezeichnet) wir zu welchen Zwecken und in welchem Umfang verarbeiten. Die Datenschutzerklärung gilt für alle von uns durchgeführten Verarbeitungen personenbezogener Daten, sowohl im Rahmen der Erbringung unserer Leistungen als auch insbesondere auf unseren Webseiten, in mobilen Applikationen sowie innerhalb externer Onlinepräsenzen, wie z. B. unserer Social-Media-Profile (nachfolgend zusammenfassend bezeichnet als "Onlineangebot").

                    Die verwendeten Begriffe sind nicht geschlechtsspezifisch.

                    Stand: 24. Mai 2024

                    ## Inhaltsübersicht

                    - [Präambel](#m716)
                    - [Verantwortlicher](#m3)
                    - [Übersicht der Verarbeitungen](#mOverview)
                    - [Maßgebliche Rechtsgrundlagen](#m2427)
                    - [Sicherheitsmaßnahmen](#m27)
                    - [Übermittlung von personenbezogenen Daten](#m25)
                    - [Internationale Datentransfers](#m24)
                    - [Allgemeine Informationen zur Datenspeicherung und Löschung](#m12)
                    - [Rechte der betroffenen Personen](#m10)
                    - [Bereitstellung des Onlineangebots und Webhosting](#m225)

                    ## <a name="m3"></a>Verantwortlicher

                    Wieland, Brendel
                    ELLIS Institut Tübingen gGmbH
                    Hagellocher Weg 1
                    72070 Tübingen, Deutschland

                    E-Mail-Adresse: [wieland.brendel@tue.ellis.eu](mailto:wieland.brendel@tue.ellis.eu)

                    ## <a name="mOverview"></a>Übersicht der Verarbeitungen

                    Die nachfolgende Übersicht fasst die Arten der verarbeiteten Daten und die Zwecke ihrer Verarbeitung zusammen und verweist auf die betroffenen Personen.

                    ### Arten der verarbeiteten Daten

                    - Nutzungsdaten.
                    - Meta-, Kommunikations- und Verfahrensdaten.
                    - Protokolldaten.

                    ### Kategorien betroffener Personen

                    - Nutzer.

                    ### Zwecke der Verarbeitung

                    - Sicherheitsmaßnahmen.
                    - Bereitstellung unseres Onlineangebotes und Nutzerfreundlichkeit.
                    - Informationstechnische Infrastruktur.

                    ## <a name="m2427"></a>Maßgebliche Rechtsgrundlagen

                    **Maßgebliche Rechtsgrundlagen nach der DSGVO:** Im Folgenden erhalten Sie eine Übersicht der Rechtsgrundlagen der DSGVO, auf deren Basis 
                    wir personenbezogene Daten verarbeiten. Bitte nehmen Sie zur Kenntnis, dass neben den Regelungen der DSGVO nationale Datenschutzvorgaben in 
                    Ihrem bzw. unserem Wohn- oder Sitzland gelten können. Sollten ferner im Einzelfall speziellere Rechtsgrundlagen maßgeblich sein, teilen wir 
                    Ihnen diese in der Datenschutzerklärung mit.

                    - **Berechtigte Interessen (Art. 6 Abs. 1 S. 1 lit. f) DSGVO)** - die Verarbeitung ist zur Wahrung der berechtigten Interessen des Verantwortlichen 
                    oder eines Dritten notwendig, vorausgesetzt, dass die Interessen, Grundrechte und Grundfreiheiten der betroffenen Person, die den Schutz 
                    personenbezogener Daten verlangen, nicht überwiegen.

                    **Nationale Datenschutzregelungen in Deutschland:** Zusätzlich zu den Datenschutzregelungen der DSGVO gelten nationale Regelungen zum 
                    Datenschutz in Deutschland. Hierzu gehört insbesondere das Gesetz zum Schutz vor Missbrauch personenbezogener Daten bei der Datenverarbeitung 
                    (Bundesdatenschutzgesetz – BDSG). Das BDSG enthält insbesondere Spezialregelungen zum Recht auf Auskunft, zum Recht auf Löschung, zum 
                    Widerspruchsrecht, zur Verarbeitung besonderer Kategorien personenbezogener Daten, zur Verarbeitung für andere Zwecke und zur Übermittlung 
                    sowie automatisierten Entscheidungsfindung im Einzelfall einschließlich Profiling. Ferner können Landesdatenschutzgesetze der einzelnen 
                    Bundesländer zur Anwendung gelangen.

                    **Hinweis auf Geltung DSGVO und Schweizer DSG:** Diese Datenschutzhinweise dienen sowohl der Informationserteilung nach dem Schweizer 
                    DSG als auch nach der Datenschutzgrundverordnung (DSGVO). Aus diesem Grund bitten wir Sie zu beachten, dass aufgrund der breiteren 
                    räumlichen Anwendung und Verständlichkeit die Begriffe der DSGVO verwendet werden. Insbesondere statt der im Schweizer DSG verwendeten 
                    Begriffe „Bearbeitung" von „Personendaten", "überwiegendes Interesse" und "besonders schützenswerte Personendaten" werden die in der 
                    DSGVO verwendeten Begriffe „Verarbeitung" von „personenbezogenen Daten" sowie "berechtigtes Interesse" und "besondere Kategorien von Daten" 
                    verwendet. Die gesetzliche Bedeutung der Begriffe wird jedoch im Rahmen der Geltung des Schweizer DSG weiterhin nach dem Schweizer DSG bestimmt.

                    ## <a name="m27"></a>Sicherheitsmaßnahmen

                    Wir treffen nach Maßgabe der gesetzlichen Vorgaben unter Berücksichtigung des Stands der Technik, der Implementierungskosten und der Art, des Umfangs, 
                    der Umstände und der Zwecke der Verarbeitung sowie der unterschiedlichen Eintrittswahrscheinlichkeiten und des Ausmaßes der Bedrohung der Rechte 
                    und Freiheiten natürlicher Personen geeignete technische und organisatorische Maßnahmen, um ein dem Risiko angemessenes Schutzniveau zu gewährleisten.

                    Zu den Maßnahmen gehören insbesondere die Sicherung der Vertraulichkeit, Integrität und Verfügbarkeit von Daten durch Kontrolle des physischen und 
                    elektronischen Zugangs zu den Daten als auch des sie betreffenden Zugriffs, der Eingabe, der Weitergabe, der Sicherung der Verfügbarkeit und ihrer 
                    Trennung. Des Weiteren haben wir Verfahren eingerichtet, die eine Wahrnehmung von Betroffenenrechten, die Löschung von Daten und Reaktionen auf die 
                    Gefährdung der Daten gewährleisten. Ferner berücksichtigen wir den Schutz personenbezogener Daten bereits bei der Entwicklung bzw. Auswahl von 
                    Hardware, Software sowie Verfahren entsprechend dem Prinzip des Datenschutzes, durch Technikgestaltung und durch datenschutzfreundliche Voreinstellungen.

                    Sicherung von Online-Verbindungen durch TLS-/SSL-Verschlüsselungstechnologie (HTTPS): Um die Daten der Nutzer, die über unsere Online-Dienste 
                    übertragen werden, vor unerlaubten Zugriffen zu schützen, setzen wir auf die TLS-/SSL-Verschlüsselungstechnologie. Secure Sockets Layer (SSL) und 
                    Transport Layer Security (TLS) sind die Eckpfeiler der sicheren Datenübertragung im Internet. Diese Technologien verschlüsseln die Informationen, 
                    die zwischen der Website oder App und dem Browser des Nutzers (oder zwischen zwei Servern) übertragen werden, wodurch die Daten vor unbefugtem 
                    Zugriff geschützt sind. TLS, als die weiterentwickelte und sicherere Version von SSL, gewährleistet, dass alle Datenübertragungen den höchsten 
                    Sicherheitsstandards entsprechen. Wenn eine Website durch ein SSL-/TLS-Zertifikat gesichert ist, wird dies durch die Anzeige von HTTPS in der URL 
                    signalisiert. Dies dient als ein Indikator für die Nutzer, dass ihre Daten sicher und verschlüsselt übertragen werden.

                    ## <a name="m25"></a>Übermittlung von personenbezogenen Daten

                    Im Rahmen unserer Verarbeitung von personenbezogenen Daten kommt es vor, dass diese an andere Stellen, Unternehmen, rechtlich selbstständige 
                    Organisationseinheiten oder Personen übermittelt beziehungsweise ihnen gegenüber offengelegt werden. Zu den Empfängern dieser Daten können 
                    z.B. mit IT-Aufgaben beauftragte Dienstleister gehören oder Anbieter von Diensten und Inhalten, die in eine Website eingebunden sind. In solchen 
                    Fällen beachten wir die gesetzlichen Vorgaben und schließen insbesondere entsprechende Verträge bzw. Vereinbarungen, die dem Schutz Ihrer Daten 
                    dienen, mit den Empfängern Ihrer Daten ab.

                    ## <a name="m24"></a>Internationale Datentransfers

                    Datenverarbeitung in Drittländern: Sofern wir Daten in einem Drittland (d. h., außerhalb der Europäischen Union (EU), des Europäischen 
                    Wirtschaftsraums (EWR)) verarbeiten oder die Verarbeitung im Rahmen der Inanspruchnahme von Diensten Dritter oder der Offenlegung bzw. 
                    Übermittlung von Daten an andere Personen, Stellen oder Unternehmen stattfindet, erfolgt dies nur im Einklang mit den gesetzlichen Vorgaben. 
                    Sofern das Datenschutzniveau in dem Drittland mittels eines Angemessenheitsbeschlusses anerkannt wurde (Art. 45 DSGVO), dient dieser als 
                    Grundlage des Datentransfers. Im Übrigen erfolgen Datentransfers nur dann, wenn das Datenschutzniveau anderweitig gesichert ist, insbesondere 
                    durch Standardvertragsklauseln (Art. 46 Abs. 2 lit. c) DSGVO), ausdrückliche Einwilligung oder im Fall vertraglicher oder gesetzlich 
                    erforderlicher Übermittlung (Art. 49 Abs. 1 DSGVO). Im Übrigen teilen wir Ihnen die Grundlagen der Drittlandübermittlung bei den einzelnen 
                    Anbietern aus dem Drittland mit, wobei die Angemessenheitsbeschlüsse als Grundlagen vorrangig gelten. Informationen zu Drittlandtransfers und 
                    vorliegenden Angemessenheitsbeschlüssen können dem Informationsangebot der EU-Kommission entnommen werden: [https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection_en?prefLang=de](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection_en?prefLang=de).

                    EU-US Trans-Atlantic Data Privacy Framework: Im Rahmen des sogenannten „Data Privacy Framework" (DPF) hat die EU-Kommission das Datenschutzniveau 
                    ebenfalls für bestimmte Unternehmen aus den USA im Rahmen der Angemessenheitsbeschlusses vom 10.07.2023 als sicher anerkannt. Die Liste der 
                    zertifizierten Unternehmen als auch weitere Informationen zu dem DPF können Sie der Website des Handelsministeriums der USA unter 
                    [https://www.dataprivacyframework.gov/](https://www.dataprivacyframework.gov/) (in Englisch) entnehmen. Wir informieren Sie im Rahmen der 
                    Datenschutzhinweise, welche von uns eingesetzten Diensteanbieter unter dem Data Privacy Framework zertifiziert sind.

                    ## <a name="m12"></a>Allgemeine Informationen zur Datenspeicherung und Löschung

                    Wir löschen personenbezogene Daten, die wir verarbeiten, gemäß den gesetzlichen Bestimmungen, sobald die zugrundeliegenden Einwilligungen 
                    widerrufen werden oder keine weiteren rechtlichen Grundlagen für die Verarbeitung bestehen. Dies betrifft Fälle, in denen der ursprüngliche 
                    Verarbeitungszweck entfällt oder die Daten nicht mehr benötigt werden. Ausnahmen von dieser Regelung bestehen, wenn gesetzliche Pflichten oder 
                    besondere Interessen eine längere Aufbewahrung oder Archivierung der Daten erfordern.

                    Insbesondere müssen Daten, die aus handels- oder steuerrechtlichen Gründen aufbewahrt werden müssen oder deren Speicherung notwendig ist zur 
                    Rechtsverfolgung oder zum Schutz der Rechte anderer natürlicher oder juristischer Personen, entsprechend archiviert werden.

                    Unsere Datenschutzhinweise enthalten zusätzliche Informationen zur Aufbewahrung und Löschung von Daten, die speziell für bestimmte Verarbeitungsprozesse gelten.

                    Bei mehreren Angaben zur Aufbewahrungsdauer oder Löschungsfristen eines Datums, ist stets die längste Frist maßgeblich.

                    Beginnt eine Frist nicht ausdrücklich zu einem bestimmten Datum und beträgt sie mindestens ein Jahr, so startet sie automatisch am Ende 
                    des Kalenderjahres, in dem das fristauslösende Ereignis eingetreten ist. Im Fall laufender Vertragsverhältnisse, in deren Rahmen Daten 
                    gespeichert werden, ist das fristauslösende Ereignis der Zeitpunkt des Wirksamwerdens der Kündigung oder sonstige Beendigung des Rechtsverhältnisses.

                    Daten, die nicht mehr für den ursprünglich vorgesehenen Zweck, sondern aufgrund gesetzlicher Vorgaben oder anderer Gründe aufbewahrt werden, 
                    verarbeiten wir ausschließlich zu den Gründen, die ihre Aufbewahrung rechtfertigen.

                    **Weitere Hinweise zu Verarbeitungsprozessen, Verfahren und Diensten:**

                    - **Aufbewahrung und Löschung von Daten:** Die folgenden allgemeinen Fristen gelten für die Aufbewahrung und Archivierung nach deutschem Recht:
                      - 10 Jahre - Aufbewahrungsfrist für Bücher und Aufzeichnungen, Jahresabschlüsse, Inventare, Lageberichte, Eröffnungsbilanz sowie die zu ihrem Verständnis erforderlichen Arbeitsanweisungen und sonstigen Organisationsunterlagen, Buchungsbelege und Rechnungen (§ 147 Abs. 3 i. V. m. Abs. 1 Nr. 1, 4 und 4a AO, § 14b Abs. 1 UStG, § 257 Abs. 1 Nr. 1 u. 4, Abs. 4 HGB).
                      - 6 Jahre - Übrige Geschäftsunterlagen: empfangene Handels- oder Geschäftsbriefe, Wiedergaben der abgesandten Handels- oder Geschäftsbriefe, sonstige Unterlagen, soweit sie für die Besteuerung von Bedeutung sind, z. B. Stundenlohnzettel, Betriebsabrechnungsbögen, Kalkulationsunterlagen, Preisauszeichnungen, aber auch Lohnabrechnungsunterlagen, soweit sie nicht bereits Buchungsbelege sind und Kassenstreifen (§ 147 Abs. 3 i. V. m. Abs. 1 Nr. 2, 3, 5 AO, § 257 Abs. 1 Nr. 2 u. 3, Abs. 4 HGB).
                      - 3 Jahre - Daten, die erforderlich sind, um potenzielle Gewährleistungs- und Schadensersatzansprüche oder ähnliche vertragliche Ansprüche und Rechte zu berücksichtigen sowie damit verbundene Anfragen zu bearbeiten, basierend auf früheren Geschäftserfahrungen und üblichen Branchenpraktiken, werden für die Dauer der regulären gesetzlichen Verjährungsfrist von drei Jahren gespeichert (§§ 195, 199 BGB).

                    ## <a name="m10"></a>Rechte der betroffenen Personen

                    Rechte der betroffenen Personen aus der DSGVO: Ihnen stehen als Betroffene nach der DSGVO verschiedene Rechte zu, die sich insbesondere aus 
                    Art. 15 bis 21 DSGVO ergeben:

                    - **Widerspruchsrecht:** Sie haben das Recht, aus Gründen, die sich aus Ihrer besonderen Situation ergeben, jederzeit gegen die Verarbeitung der Sie betreffenden personenbezogenen Daten, die aufgrund von Art. 6 Abs. 1 lit. e oder f DSGVO erfolgt, Widerspruch einzulegen; dies gilt auch für ein auf diese Bestimmungen gestütztes Profiling. Werden die Sie betreffenden personenbezogenen Daten verarbeitet, um Direktwerbung zu betreiben, haben Sie das Recht, jederzeit Widerspruch gegen die Verarbeitung der Sie betreffenden personenbezogenen Daten zum Zwecke derartiger Werbung einzulegen; dies gilt auch für das Profiling, soweit es mit solcher Direktwerbung in Verbindung steht.
                    - **Widerrufsrecht bei Einwilligungen:** Sie haben das Recht, erteilte Einwilligungen jederzeit zu widerrufen.
                    - **Auskunftsrecht:** Sie haben das Recht, eine Bestätigung darüber zu verlangen, ob betreffende Daten verarbeitet werden und auf Auskunft über diese Daten sowie auf weitere Informationen und Kopie der Daten entsprechend den gesetzlichen Vorgaben.
                    - **Recht auf Berichtigung:** Sie haben entsprechend den gesetzlichen Vorgaben das Recht, die Vervollständigung der Sie betreffenden Daten oder die Berichtigung der Sie betreffenden unrichtigen Daten zu verlangen.
                    - **Recht auf Löschung und Einschränkung der Verarbeitung:** Sie haben nach Maßgabe der gesetzlichen Vorgaben das Recht, zu verlangen, dass Sie betreffende Daten unverzüglich gelöscht werden, bzw. alternativ nach Maßgabe der gesetzlichen Vorgaben eine Einschränkung der Verarbeitung der Daten zu verlangen.
                    - **Recht auf Datenübertragbarkeit:** Sie haben das Recht, Sie betreffende Daten, die Sie uns bereitgestellt haben, nach Maßgabe der gesetzlichen Vorgaben in einem strukturierten, gängigen und maschinenlesbaren Format zu erhalten oder deren Übermittlung an einen anderen Verantwortlichen zu fordern.
                    - **Beschwerde bei Aufsichtsbehörde:** Sie haben unbeschadet eines anderweitigen verwaltungsrechtlichen oder gerichtlichen Rechtsbehelfs das Recht auf Beschwerde bei einer Aufsichtsbehörde, insbesondere in dem Mitgliedstaat ihres gewöhnlichen Aufenthaltsorts, ihres Arbeitsplatzes oder des Orts des mutmaßlichen Verstoßes, wenn Sie der Ansicht sind, dass die Verarbeitung der Sie betreffenden personenbezogenen Daten gegen die Vorgaben der DSGVO verstößt.

                    ## <a name="m225"></a>Bereitstellung des Onlineangebots und Webhosting

                    Wir verarbeiten die Daten der Nutzer, um ihnen unsere Online-Dienste zur Verfügung stellen zu können. Zu diesem Zweck verarbeiten wir die IP-Adresse des Nutzers, die notwendig ist, um die Inhalte und Funktionen unserer Online-Dienste an den Browser oder das Endgerät der Nutzer zu übermitteln.

                    - **Verarbeitete Datenarten:** Nutzungsdaten (z. B. Seitenaufrufe und Verweildauer, Klickpfade, Nutzungsintensität und -frequenz, verwendete Gerätetypen und Betriebssysteme, Interaktionen mit Inhalten und Funktionen); Meta-, Kommunikations- und Verfahrensdaten (z. B. IP-Adressen, Zeitangaben, Identifikationsnummern, beteiligte Personen). Protokolldaten (z. B. Logfiles betreffend Logins oder den Abruf von Daten oder Zugriffszeiten.).
                    - **Betroffene Personen:** Nutzer (z. B. Webseitenbesucher, Nutzer von Onlinediensten).
                    - **Zwecke der Verarbeitung:** Bereitstellung unseres Onlineangebotes und Nutzerfreundlichkeit; Informationstechnische Infrastruktur (Betrieb und Bereitstellung von Informationssystemen und technischen Geräten (Computer, Server etc.).). Sicherheitsmaßnahmen.
                    - **Aufbewahrung und Löschung:** Löschung entsprechend Angaben im Abschnitt "Allgemeine Informationen zur Datenspeicherung und Löschung".
                    - **Rechtsgrundlagen:** Berechtigte Interessen (Art. 6 Abs. 1 S. 1 lit. f) DSGVO).

                    **Weitere Hinweise zu Verarbeitungsprozessen, Verfahren und Diensten:**

                    - **Bereitstellung Onlineangebot auf gemietetem Speicherplatz:** Für die Bereitstellung unseres Onlineangebotes nutzen wir Speicherplatz, Rechenkapazität und Software, die wir von einem entsprechenden Serveranbieter (auch "Webhoster" genannt) mieten oder anderweitig beziehen; **Rechtsgrundlagen:** Berechtigte Interessen (Art. 6 Abs. 1 S. 1 lit. f) DSGVO).
                    - **Erhebung von Zugriffsdaten und Logfiles:** Der Zugriff auf unser Onlineangebot wird in Form von sogenannten "Server-Logfiles" protokolliert. Zu den Serverlogfiles können die Adresse und der Name der abgerufenen Webseiten und Dateien, Datum und Uhrzeit des Abrufs, übertragene Datenmengen, Meldung über erfolgreichen Abruf, Browsertyp nebst Version, das Betriebssystem des Nutzers, Referrer URL (die zuvor besuchte Seite) und im Regelfall IP-Adressen und der anfragende Provider gehören. Die Serverlogfiles können zum einen zu Sicherheitszwecken eingesetzt werden, z. B. um eine Überlastung der Server zu vermeiden (insbesondere im Fall von missbräuchlichen Angriffen, sogenannten DDoS-Attacken), und zum anderen, um die Auslastung der Server und ihre Stabilität sicherzustellen; **Rechtsgrundlagen:** Berechtigte Interessen (Art. 6 Abs. 1 S. 1 lit. f) DSGVO). **Löschung von Daten:** Logfile-Informationen werden für die Dauer von maximal 30 Tagen gespeichert und danach gelöscht oder anonymisiert. Daten, deren weitere Aufbewahrung zu Beweiszwecken erforderlich ist, sind bis zur endgültigen Klärung des jeweiligen Vorfalls von der Löschung ausgenommen.

                    <p class="seal"><a href="https://datenschutz-generator.de/" title="Rechtstext von Dr. Schwenke - für weitere Informationen bitte anklicken." target="_blank" rel="noopener noreferrer nofollow">Erstellt mit kostenlosem Datenschutz-Generator.de von Dr. Thomas Schwenke</a></p>

                  ''').style('font-size: 1cqw')

    # adjust font size in markdown fields so that it scales with whiteboard width
    ui.query('h1').style('font-size: 2cqw; font-weight: bold; margin: 0cqw 0;')
    ui.query('h2').style('font-size: 1.7cqw; font-weight: bold; margin: 0cqw 0;')
    ui.query('h3').style('font-size: 1.3cqw; font-weight: bold; margin: 0cqw 0; padding-bottom: 0; margin-bottom: 0;')