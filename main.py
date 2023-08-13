from _typeshed import OpenBinaryModeReading
import openai
from dotenv import load_dotenv
import os

#outside Libraries
import glob
from markdown import markdown

load_dotenv()


APIKEY = os.getenv("OPENAIKEY")
URL = os,getenv("URL")
TOKEN = os.getenv("TOKEN")


# check to see if token is active: 
if APIKEY is not None:
    print(f'this ApiKey is active {APIKEY}')
else:
    print("APIKEY is not active")
    exit()



class OpenAi: 
    def summarize_code(self, code):
        prompt = f"summarize this code in MarkDown code so i can use it for my Github Project,                                                                          please dont say aything just return me the summ                                                                                                      block thats need to use: \n\n{code}"
        response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=100
                )
        return

class MDGenerator:
  

    def readFileContent(self):    
        source_directory = input("path/to/your/project:  ")
        python_files = 'FILE PATH OR INPUT'
        glob.glob(os.path.join(source_directory, "*.py"))
        #LOOP THROUGH CODE
        code = ''
        for python_file in python_files:
            with open(python_file, 'r') as file:
                code += file.read() + '\n'
                return code

    
    def createDirectory(self, projectName):
         Directory_Name = "MD_files"
         file_name = os.path.join(Directory_Name, f'{projectName}.md')
    
        if not os.path.exists(Directory_Name):
            with open(file_name, "wb") as f:
                f.write(code)

                print('sucessfully created a md for this project')

        else: 
            print("a file under this name as allready been used")

                

 
             

     # define source dir
    OpenAi = OpenAi()
    MDGenerator = MDGenerator()

    projectName = input("please provide with your projectName:  ")
    project = MDGenerator.readFileContent()
    
    md_code = OpenAi.summarize_code(project)
    MDGenerator.createDirectory(md_code)
    # This is a ample Python sript.
