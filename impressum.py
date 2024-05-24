from nicegui import ui, context

@ui.page('/impressum')
def impressum():

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
                    # Impressum

                    ### Herausgeber
                    ELLIS Institute Tübingen gGmbH
                    Hagellocher Weg 1
                    72070 Tübingen

                    ### Handelsregister-Nr.
                    HRB 789795

                    ### Registergericht
                    Amtsgericht Stuttgart

                    ### Vertreten durch
                    Wissenschaftlicher Direktor: Prof. Dr. Bernhard Schölkopf

                    Geschäftsführer: Herr Volker Maria Geiß

                    ### Verwantwortlich für die Inhalte
                    Dr. Wieland Brendel
                    wieland.brendel (at) tue.ellis.eu

                    ### Rechtsform
                    Die ELLIS Institute Tübingen gGmbH ist eine gemeinnützige Gesellschaft mit beschränkter Haftung.

                    ### Fremdsprachige Seiten
                    Soweit Teile des Internetauftritts auch in anderen Sprachen als Deutsch angeboten werden, ist dies ausschließlich ein Service 
                    für Mitarbeiter und Gäste der ELLIS Institute Tübingen gGmbH, die der deutschen Sprache nicht mächtig sind.

                    ### Rechtliche Hinweise zur Haftung für eigene Inhalte
                    Die ELLIS Institute Tübingen gGmbH ist als Inhaltsanbieterin nach § 7 Abs. 1 Telemediengesetz für die eigenen Inhalte, die 
                    sie zur Nutzung bereithält, nach den allgemeinen Gesetzen verantwortlich. Die ELLIS Institute Tübingen gGmbH ist um Richtigkeit 
                    und Aktualität der auf dieser Internetpräsenz bereitgestellten Informationen bemüht. Trotzdem können Fehler und Unklarheiten 
                    nicht vollständig ausgeschlossen werden. Die ELLIS Institute Tübingen gGmbH übernimmt deshalb keine Gewähr für die Aktualität, 
                    Richtigkeit, Vollständigkeit oder Qualität der bereitgestellten Informationen. Für Schäden materieller oder immaterieller Art, 
                    die durch die Nutzung oder Nichtnutzung der dargebotenen Informationen bzw. durch die Nutzung fehlerhafter und unvollständiger 
                    Informationen unmittelbar oder mittelbar verursacht werden, haftet die ELLIS Institute Tübingen gGmbH nicht, sofern ihr nicht 
                    nachweislich vorsätzliches oder grob fahrlässiges Verschulden zur Last fällt. Gleiches gilt für kostenlos zum Download bereitgehaltene 
                    Software. Die ELLIS Institute Tübingen gGmbH behält es sich vor, Teile des Internetangebots oder das gesamte Angebot ohne gesonderte 
                    Ankündigung zu verändern, zu ergänzen, zu löschen oder die Veröffentlichung zeitweise oder endgültig einzustellen.

                    ### Rechtliche Hinweise zu Verknüpfungen auf externe Seiten
                    Auf dieser Internetpräsenz befinden sich Verknüpfungen zu externen Seiten. Für die Inhalte der verlinkten externen Seiten 
                    ist stets der jeweilige Anbieter verantwortlich. Die ELLIS Institute Tübingen gGmbH hat bei der erstmaligen Verknüpfung den 
                    fremden Inhalt daraufhin überprüft, ob durch ihn eine mögliche zivilrechtliche oder strafrechtliche Verantwortlichkeit 
                    ausgelöst wird. Eine permanente inhaltliche Kontrolle der verknüpften externen Seiten ist jedoch ohne konkrete Anhaltspunkte 
                    einer Rechtsverletzung nicht zumutbar. Wenn die ELLIS Institute Tübingen gGmbH feststellt oder von anderen darauf hingewiesen 
                    wird, dass ein externes Angebot, auf das sie per Link verknüpft hat, eine zivil- oder strafrechtliche Verantwortlichkeit auslöst, 
                    wird sie den Link auf dieses Angebot unverzüglich aufheben. Die ELLIS Institute Tübingen gGmbH distanziert sich ausdrücklich 
                    von derartigen Inhalten.
                    ''').style('font-size: 1cqw')

    # adjust font size in markdown fields so that it scales with whiteboard width
    ui.query('h1').style('font-size: 2cqw; font-weight: bold; margin: 0cqw 0;')
    ui.query('h2').style('font-size: 1.7cqw; font-weight: bold; margin: 0cqw 0;')
    ui.query('h3').style('font-size: 1.3cqw; font-weight: bold; margin: 0cqw 0; padding-bottom: 0; margin-bottom: 0;')