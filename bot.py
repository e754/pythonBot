import discord
import google.generativeai as genai

name = 'generate-num-3397'
model = genai.GenerativeModel(model_name=f'tunedModels/{name}')

from google.generativeai.types import HarmCategory, HarmBlockThreshold

def generate_content(text):
    result = model.generate_content(
        [f'You are a narrator of a gothic horror story, rephrase this: "{text}" '],
        safety_settings={
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        },
        generation_config=genai.types.GenerationConfig(
            temperature=2,  # Increase to make it less deterministic
            top_k=50,         # Higher k for more diversity
            top_p=1.0,        # Allows for a broader selection of words
        ),
    )
    return result.text


class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.message_count = 0


        
        self.last_message = None

    async def on_ready(self):
        print("Logged in as", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        self.message_count += 1

        if self.message_count % 2 == 1:
            self.last_message = message
        else:
            if self.last_message:
                text_to_generate = self.last_message.content + " " + message.content
                generated_text = generate_content(text_to_generate)
                await message.reply(generated_text)

intents = discord.Intents.default()
intents.messages = True

# client = discord.Client(heartbeat_timeout=5)
client = Client(intents=intents)
client.run('MTI4Mjc1MDUwMjI4MjcyNzUwNg.Giv1mf.8RxWyPAR_jwYh09bpRyzFPVo4Riv2SzUW32cXM')


# import discord
# import google.generativeai as genai

# name='generate-num-3397'
# model = genai.GenerativeModel(model_name=f'tunedModels/{name}')

# from google.generativeai.types import HarmCategory, HarmBlockThreshold

# def generateContent(text):

#   result = model.generate_content(
#   [f'You are a narrator of a gothic horror story, rephrase this: "{text}" '],
#      safety_settings={
#       HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
#       HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
#       HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
#       HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT:HarmBlockThreshold.BLOCK_NONE,
#       # HarmCategory.HARM_CATEGORY_UNSPECIFIED:HarmBlockThreshold.BLOCK_NONE,
#     },
#     generation_config=genai.types.GenerationConfig(
#       temperature=0.5,
#     ),
#   )
#   return result.text

# class Client(discord.Client):
#     async def on_ready(self):
#         print("logged")

# intents=discord.Intents.default()
# intents.message_content = True

# client = Client(intents=intents)
# client.run('MTI4Mjc1MDUwMjI4MjcyNzUwNg.Giv1mf.8RxWyPAR_jwYh09bpRyzFPVo4Riv2SzUW32cXM')
