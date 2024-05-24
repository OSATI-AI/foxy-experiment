from langchain_openai import OpenAI, ChatOpenAI
from langchain_groq import  ChatGroq
from instructions import tutor_persona, tutor_instruction, slide_instruction, memory_instruction
from fauna import fql
from fauna.client import Client
from fauna.encoding import QuerySuccess
from fauna.errors import FaunaException
import json

from nicegui import ui, context
import os
import io

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]
FAUNA_KEY = os.environ["FAUNA_KEY"]

def dump_chat(yaml, chat):
    # dump chat into YAML format
    buf = io.BytesIO()
    yaml.dump(chat.detailed_dialog, buf)
    return buf.getvalue()

class DB():
    def __init__(self):
        self.client = Client(secret=FAUNA_KEY)
        self.item_id = None

    def save_dialog(self, dialog, model, language):
        # Remove line breaks
        for e in dialog:
            k = list(e.keys())[0]
            e[k] = e[k].replace("\n", "")
        dialog = json.dumps(dialog, ensure_ascii=False)
        dialog = dialog.replace('\"', "")
        dialog = dialog.replace("\\", "")

        if self.item_id is None:
            self.create_item(dialog, model, language)
        else:
            self.update_item(dialog, model, language)

    def create_item(self, dialog, model, language):
        try:
            query = fql("Dialogs.create({dialog: \""+dialog+"\", model:\""+model+"\", language:\""+language+"\"})")
            res: QuerySuccess = self.client.query(query)
            self.item_id = res.data.id 
            print("Created DB entry with id: ", self.item_id)
        except FaunaException as e:
            print("Error while saving dialog to database")
            print(e)
            ui.notify('Data could not be saved to database', level='error')

    def update_item(self,dialog, model, language):
        try:
            query = fql("Dialogs.byId(\""+self.item_id+"\")?.update({dialog: \""+dialog+"\", model:\""+model+"\", language:\""+language+"\"})")
            res: QuerySuccess = self.client.query(query)
            self.item_id = res.data.id 
            print("Updated DB entry with id: ", self.item_id)
        except FaunaException as e:
            print("Error while saving dialog to database")
            print(e)
            ui.notify('Data could not be saved to database', level='error')

class Chat:
  def __init__(self, tutor_persona):
    self.tutor_persona = tutor_persona
    self.last_student_response = None
    self.language = "german"
    self.dialog = ''
    self.memory = '-Der Schüler braucht Hilfe vom Tutor'
    self.detailed_dialog = []
    self.save_dialog = True

  def add_student_response(self, response):
    self.dialog += f'\n S: {response}'
    self.last_student_response = response
    self.detailed_dialog.append({'S' : response})

  def add_teacher_response(self, response):
    self.dialog += f'\n T: {response}'
    self.detailed_dialog.append({'T' : response})

  def update_memory(self, memory):
      self.memory = memory
      self.detailed_dialog.append({'M' : memory})

  def get_tutor_instruction(self):
    return f'{tutor_persona(self.language)}\n {self.dialog}\n {tutor_instruction(self.last_student_response, self.memory, self.language)}'
  
  def get_memory_instruction(self):
      return memory_instruction(self.dialog, self.memory, self.language)

class Response:

    def __init__(self):
        self.response = ''
        self.thoughts = ''
        self.answer = ''

    def send_chunk(self, chunk):
        self.response += chunk

        if 'TUTOR:' in self.response:
            self.answer += chunk
        else:
            self.thoughts += chunk

    def get_answer(self):
        # remove unwanted characters
        answer = self.answer
        answer = answer.strip('TUTOR').strip(' :"')
        answer.replace("**", "")
        return answer

    def get_thoughts(self):
        return self.thoughts

class Slide:

    def __init__(self):
        self.content = ''
        self.object = None

    def get_response(self, response):
        if 'PRESENTATION:' in response:
            self.content = response.split('PRESENTATION:')[1].strip(' :"')
            self.thoughts = response.split('PRESENTATION:')[0]

    def set_content(self, content):
        self.object.set_content(content)

class LLM:

    def __init__(self):
        self.tutor_model = ['openrouter', 'openai/gpt-4o']
        self.memory_model = ['openrouter', 'openai/gpt-4o']        
        self.slide_model = ['openrouter', 'openai/gpt-4o']


    async def memory_response(self,instruction):
        if self.memory_model[0] == 'openrouter':
            llm = ChatOpenAI(model_name=self.memory_model[1], streaming=True, openai_api_key=OPENROUTER_API_KEY, openai_api_base = 'https://openrouter.ai/api/v1')
        response = ''
        
        # at the moment we are not gaining anything from making this asyny/streamed since we do not display the memory
        async for chunk in llm.astream(instruction):
            response += chunk.content
        
        return response

    async def tutor_response(self, instruction, response, message_container):
        if self.tutor_model[0] == 'groq':
            llm = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name=self.tutor_model[1])
        elif self.tutor_model[0] == 'openrouter':
            llm = ChatOpenAI(model_name=self.tutor_model[1], streaming=True, openai_api_key=OPENROUTER_API_KEY, openai_api_base = 'https://openrouter.ai/api/v1')

        # Process the stream of chunks
        async for chunk in llm.astream(instruction):
            response.send_chunk(chunk.content)

            if 'TUTOR:' in response.response:
                response.container.clear()
                with response.container:
                    ui.html(response.get_answer().replace("\"", ""))

            message_container.scroll_to(percent=100)

    async def slide_response(self, instruction, slide):
        if self.slide_model[0] == 'openrouter':
             llm = ChatOpenAI(model_name=self.slide_model[1], streaming=True, openai_api_key=OPENROUTER_API_KEY, openai_api_base = 'https://openrouter.ai/api/v1')

        response = ''

        # Process the stream of chunks
        async for chunk in llm.astream(instruction):
            response += chunk.content

        slide.get_response(response)
        slide.set_content(slide.content)