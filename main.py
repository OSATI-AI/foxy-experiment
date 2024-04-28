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

        # get tutor response
        instruction = chat.get_tutor_instruction()
        await llm_handler.tutor_response(instruction, response, message_container)
        message_container.remove(spinner)

        # get slide response
        instruction = slide_instruction(chat.dialog, response.answer, slide.content)
        await llm_handler.slide_response(instruction, slide)

    ui.add_css(r'a:link, a:visited {color: inherit !important; text-decoration: none; font-weight: 500}')
    ui.query('.nicegui-content').classes('w-full')

    # header
    with ui.row().classes('w-full h-[10%] no-wrap'):
        with ui.column().classes('w-[3%] h-full no-wrap'):
            pass

        with ui.column().classes('w-[97%] h-full no-wrap'):
            ui.image('media/foxy_header.png').classes('w-[25%]')

    # body
    with ui.row().classes('w-full h-[75%] no-wrap'):
        with ui.column().classes('w-[3%] h-full'):
            pass

        with ui.column().classes('w-[54%] h-full items-center'):

            with ui.element('div').classes('flex q-pl-lg items-center bg-white rounded-3xl h-full w-full'):
                slide.object = ui.markdown('').classes('text-h4')

        with ui.column().classes('w-[3%] h-full'):
            pass

        with ui.column().classes('w-[37%] h-full'):
            message_container = ui.scroll_area().classes('shadow-sm bg-white rounded-3xl h-full w-full').style('overflow-y: scroll')

        with ui.column().classes('w-[3%] h-full'):
            pass

    # config + input row
    with ui.row().classes('w-full h-[5%] no-wrap'):
        with ui.column().classes('w-[60%] h-full'):
            pass

        with ui.column().classes('w-[40%] h-full justify-center'):
            with ui.row().classes('w-[90%] h-[10%] no-wrap'):
                placeholder = 'message - do not share personal information!'
                text = ui.input(placeholder=placeholder).props('rounded outlined input-class=mx-3').props('color=orange-12') \
                    .classes('w-full self-center').on('keydown.enter', send)

    # footer
    with ui.row().classes('w-full h-[5%] no-wrap'):
        pass

ui.run(title='Foxy - an experimental AI tutor')
ui.run(favicon="favicon.ico")
ui.run(reload='FLY_ALLOC_ID' not in os.environ)