from types import prepare_class
import openai
import requests
from dotenv import load_dotenv

#outside Libraries
import glob
from markdown import markdown

load_dotenv()


APIKEY = os.getenv("OPENAIKEY")

# check to see if token is active: 
if APIKEY is not None:
    print(f'this ApiKey is active {APIKEY}')
else:
    print("APIKEY is not active")
    exit()

URL = "NONE"


class MDGenerator:
    def __init__(self, file, projectName):
        self.file = file
        self.markdown_content = " "
        self.projectName = projectName

    def readFileContent(self):
        python_files = 'FILE PATH OR INPUT'
        glob.glob(os.path.join(self.source_directory, "*.py"))
        #LOOP THROUGH CODE
        code = ''
        for python_file in python_files:
            with open(python_files, 'r') as file:
                code += file.read() + '\n'
                return code
                

class OpenAi: 
    def summarize_code(self, code):
        prompt = f"summarize this code in MarkDown code so i can use it for my Github Project: \n\n{code}"
        response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=100
                )
        return
        response.choices[0].text.strip()

     # define source dir
source_directory = input("path/to/your/project:  ")

def createDirectory(response):






# This is a sample Python script.
