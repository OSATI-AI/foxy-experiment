#!/usr/bin/env python3
from log_callback_handler import NiceGuiLogElementCallbackHandler
import asyncio
from instructions import tutor_persona, slide_instruction
from utils import Chat, Response, Slide, LLM

from nicegui import ui, context
import os

@ui.page('/')
def main():
    chat = Chat(tutor_persona())
    slide = Slide()
    llm_handler = LLM()

    # Set the style for the entire page to change the background color
    ui.query('body').style(f'background-color: #f1efed')
    context.client.content.classes('h-[100vh]')

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

        #print("\n\n MEMORY = ", memory_updated)

        # get tutor response
        instruction = chat.get_tutor_instruction()
        await llm_handler.tutor_response(instruction, response, message_container)
        message_container.remove(spinner)

        # get slide response
        instruction = slide_instruction(chat.dialog, response.answer, slide.content)
        await llm_handler.slide_response(instruction, slide)

        # set visibility right
        warning.visible = False
        slide.object.visible = True

    ui.add_css(r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}')
    ui.query('.nicegui-content').classes('w-full')

    # header
    with ui.row().classes('w-full h-[10%] no-wrap'):
        with ui.column().classes('w-0 sm:w-[3%] -ml-6 sm:m-0 h-full no-wrap'):
            pass

        with ui.column().classes('w-[97%] h-full no-wrap'):
            ui.image('media/foxy_header.png').classes('w-80')

    # body
    with ui.row().classes('w-full h-[75%] flex flex-col sm:flex-row no-wrap'):
        with ui.column().classes('w-[1%] sm:w-[3%] h-[1%] sm:h-full -mb-4 sm:m-0'):
            pass

        with ui.column().classes('w-full m-0 sm:w-[54%] h-[50%] sm:h-full items-center'):
            with ui.element('div').classes('flex q-pl-lg items-center bg-white rounded-3xl h-full w-full'):
                slide.object = ui.markdown('''
                    ## Hilfe bei Schwierigkeiten mit Mitose
                    - Gemeinsam herausfinden, wo die Schwierigkeiten liegen
                    - Schritt für Schritt durch das Thema gehen
                    - Alles so erklären, dass du es verstehst
                    ''').classes('text-base sm:text-4xl')
                slide.object.visible = False

                warning = ui.markdown('''🚧 **Experimentelle Demoversion** 🚧<br />
                    Bitte beachten Sie, dass dies eine frühe Prototyp-Anwendung ist, die möglicherweise 
                    ungenaue Antworten liefert oder Inhalte erzeugt, die nicht für alle Zielgruppen 
                    geeignet sind. Wir raten zur Vorsicht und raten Ihnen uns alle Probleme, die Sie 
                    feststellen, mitzuteilen.
                ''').classes('w-full text-center m-8 lg:m-32')

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

        with ui.column().classes('w-full sm:w-[40%] -mt-8 sm:mt-0 h-full justify-center'):
            with ui.row().classes('w-full sm:w-[90%] h-[10%] no-wrap'):
                placeholder = 'message - do not share personal information!'
                text = ui.input(placeholder=placeholder).props('rounded outlined input-class=mx-3').props('color=orange-12') \
                    .classes('w-full self-center').on('keydown.enter', send)

    # footer
    with ui.row().classes('w-full h-[5%] no-wrap'):
        pass

ui.run(title='Foxy - an experimental AI tutor', favicon="favicon.ico", reload='FLY_ALLOC_ID' not in os.environ)