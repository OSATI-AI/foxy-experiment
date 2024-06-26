#!/usr/bin/env python3
from instructions import tutor_persona, slide_instruction
from utils import Chat, Response, Slide, LLM, dump_chat, DB
from ruamel.yaml import YAML
from nicegui import ui, context
from impressum import impressum
from privacy import privacy
import os

yaml = YAML()
yaml.default_flow_style = False

ui.add_head_html("""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
""")

@ui.page('/')
def main():
    chat = Chat(tutor_persona())
    slide = Slide()
    llm_handler = LLM()
    db_handler = DB()

    # Set the style for the entire page to change the background color
    ui.query('body').style(f'background-color: #f1efed')
    context.client.content.classes('supports-[height:100cqh]:h-[100cqh] supports-[height:100svh]:h-[100svh]')

    def update_settings():
        # apply changes to language and model
        language = language_select.value
        model = model_select.value
        model = ['openrouter', model]
        chat.language = language
        llm_handler.tutor_model = model

        # reset memory and set initial entry in according language
        if language == "german":
            chat.memory = "-Der Schüler braucht Hilfe vom Tutor"
        elif language == "english":
            chat.memory = "-The student needs assistance by the tutor"
        
        # reset dialog history and clear ui elements
        chat.dialog = ""
        chat.detailed_dialog = []
        text.value = ''
        slide.set_content('')
        message_container.clear()
        ui.notify('Settings saved', level='success')
        
        # close side menu 
        toggle_menu(side_menu)

    def toggle_menu(menu):
        menu.visible = not menu.visible
        language_select.value = chat.language
        model_select.value = llm_handler.tutor_model[1]
        
    def decline_save():
        ui.notify("Der Dialog wird nicht aufgezeichnet!")
        chat.save_dialog = False
        dialog.close()  # Close the popup

    async def send() -> None:
        question = text.value
        text.value = ''

        chat.add_student_response(question)

        # initialise response container
        response = Response()

        # initialise message DOM containers
        with message_container:
            with ui.row().classes('w-full').style('justify-content: right'):
                ui.chat_message(text=question, name='You', sent=True).props('bg-color=deep-purple-2')

            # think_message = ui.chat_message(name='Bot', sent=False).style('font-size: 60%').props('size=8').props('bg-color=white')
            response.container = ui.chat_message(sent=False).props('size=8').props('padding=none').props('bg-color=orange-2')
            spinner = ui.spinner(type='dots')

        message_container.scroll_to(percent=100)

        # update memory
        instruction = chat.get_memory_instruction()
        memory_updated = await llm_handler.memory_response(instruction)
        chat.update_memory(memory_updated)

        # get tutor response
        instruction = chat.get_tutor_instruction()
        await llm_handler.tutor_response(instruction, response, message_container)
        message_container.remove(spinner)

        # save tutor response in chat
        chat.add_teacher_response(response.get_answer())

        # get slide response
        instruction = slide_instruction(chat.dialog, response.answer, slide.content, chat.language)
        await llm_handler.slide_response(instruction, slide)

        # set visibility right
        warning.visible = False
        slide.object.visible = True

        # save/update dialog in DB
        if chat.save_dialog:
            db_handler.save_dialog(chat.detailed_dialog, llm_handler.tutor_model[1], chat.language)

    ui.add_css(r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}')
    ui.query('.nicegui-content').classes('w-full')
    
    # Popup Dialog for Settings
    with ui.dialog() as settings, ui.card().classes('w-[21rem] h-64'):
        ui.label("Settings").classes('text-xl font-bold')

        # Dropdown for selecting the language
        with ui.row().classes('w-full'):
            with ui.column().classes('w-[6rem]'):
                ui.label('Language:').classes('mt-5')

            with ui.column().classes('w-[12rem]'):
                language_select = ui.select(['english', 'german'], value="german").classes('w-[12rem]')

        # Dropdown for selecting Model with the label to the left
        with ui.row().classes('w-full'):
            with ui.column().classes('w-[6rem]'):
                ui.label('Model:').classes('mt-5')

            with ui.column().classes('w-[12rem]'):
                model_select = ui.select(['mistralai/mixtral-8x22b-instruct', 'meta-llama/llama-3-70b-instruct', 'openai/gpt-4o'], value='openai/gpt-4o').classes('w-[12rem]')

        # Save button
        ui.button('Save', on_click=update_settings and settings.close).props('unelevated rounded color=brown-5 text-color=white size=md')

    # header
    with ui.row().classes('w-full h-[10%] no-wrap'):
        with ui.column().classes('w-0 sm:w-[3%] -ml-6 sm:m-0 h-full no-wrap'):
            pass

        with ui.column().classes('w-[97%] h-full no-wrap'):
            with ui.row().classes('justify-between items-center w-full'):
                ui.image('media/foxy_header.png').classes('w-80')
                # settings button
                ui.button('', on_click=lambda: settings.open()).props('outline round color=brown-5 icon=settings text-color=brown-5 size=md')

    # body
    with ui.row().classes('w-full h-[77%] sm:h-[75%] flex flex-col sm:flex-row no-wrap'):
        with ui.column().classes('w-[1%] sm:w-[3%] h-[1%] sm:h-full -mb-4 sm:m-0'):
            pass

        with ui.column().classes('w-full m-0 sm:w-[54%] h-[50%] sm:h-full items-center').style('container-type: inline-size'):
            with ui.element('div').classes('flex q-pl-lg items-center bg-white rounded-3xl h-full w-full'):
                slide.object = ui.markdown('''
                    ## Hilfe bei Schwierigkeiten mit Mitose
                    - Gemeinsam herausfinden, wo die Schwierigkeiten liegen
                    - Schritt für Schritt durch das Thema gehen
                    - Alles so erklären, dass du es verstehst
                    ''').style('font-size: 2.5cqw')
                slide.object.visible = False

                warning = ui.markdown('''🚧 **Experimentelle Demoversion** 🚧<br />
                    Bitte beachten Sie, dass dies eine frühe Prototyp-Anwendung ist, die möglicherweise 
                    ungenaue Antworten liefert oder Inhalte erzeugt, die nicht für alle Zielgruppen 
                    geeignet sind. Wir raten zur Vorsicht und bitten Sie, uns eventuelle Probleme mitzuteilen.
                ''').classes('w-full text-center m-8 lg:m-32').style('font-size: 2.5cqw')

        with ui.column().classes('w-full sm:w-[3%] h-auto sm:h-full'):
            pass

        with ui.column().classes('w-full sm:w-[37%] h-[50%] sm:h-full'):
            message_container = ui.scroll_area().classes('shadow-sm bg-white rounded-3xl w-full h-full').style('overflow-y: scroll')

        with ui.column().classes('w-full sm:w-[3%] h-auto sm:h-full'):
            pass

    # config + input row
    with ui.row().classes('w-full h-[5%] flex flex-col sm:flex-row no-wrap'):
        with ui.column().classes('w-0 sm:w-[60%] h-0 sm:h-full'):
            pass

        with ui.column().classes('w-full sm:w-[40%] -mt-4 sm:mt-0 h-full justify-center'):
            with ui.row().classes('w-full sm:w-[90%] h-[10%] no-wrap'):
                placeholder = 'Nachricht - bitte gib keine persönlichen Daten ein!'
                text = ui.input(placeholder=placeholder).props('rounded outlined input-class=mx-3').props('color=orange-12') \
                    .classes('w-full self-center').style('font-size: 16px').on('keydown.enter', send)

                ui.button('', on_click=lambda: ui.download(dump_chat(yaml, chat), 'chat.yaml')).props('outline round color=brown-5 icon=download text-color=brown-5 size=md').classes('self-center')

    with ui.footer(fixed=True).classes('h-[3%] pt-1 bg-brown-2'):
        with ui.row().classes('w-full h-[3%] no-wrap'):
            #ui.label('Impressum')
            ui.link('Impressum', "impressum").classes(replace='text-xs text-white mb-3') 
            ui.link('Privacy Policy', "privacy").classes(replace='text-xs text-white mb-3')

            
    # adjust font size in markdown fields so that it scales with whiteboard width
    ui.query('h1').style('font-size: 4cqw; font-weight: bold; margin: 0cqw 0;')
    ui.query('h2').style('font-size: 3.5cqw; font-weight: bold; margin: 0cqw 0;')
    ui.query('h3').style('font-size: 3cqw; font-weight: bold; margin: 0cqw 0;')
    
    # Popup Dialog informing user that dialog is recorded and give choice to decline
    with ui.dialog() as dialog, ui.card():
        ui.label("Um unseren Tutor weiter zu verbessern, werden alle Dialogverläufe standardmäßig aufgezeichnet. Wenn Sie dies nicht möchten, klicken Sie bitte auf 'Dialog nicht aufzeichnen'.")
        with ui.row().classes('w-full'):
            ui.button('Okay', on_click=dialog.close).props('unelevated rounded color=brown-5 text-color=white size=md')
            ui.button('Dialog nicht aufzeichnen', on_click=decline_save).props('unelevated rounded color=brown-5 text-color=white size=md')

    dialog.open()

ui.run(title='Foxy - an experimental AI tutor', favicon="favicon.ico", reload='FLY_ALLOC_ID' not in os.environ)