import openai
from dotenv import load_dotenv
import os
import glob

load_dotenv()

APIKEY = os.getenv("OPENAIKEY")
URL = os.getenv("URL")
TOKEN = os.getenv("TOKEN")

# Initialize openai library
openai.api_key = APIKEY

# Check to see if token is active:
if APIKEY is not None:
    print(f'this ApiKey is active {APIKEY}')
else:
    print("APIKEY is not active")
    exit()


class OpenAi:
    @staticmethod
    def summarize_code(code):
        prompt = f"Summarize this code in MarkDown so I can use it for my Github Project: \n\n{code}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100
        )
        return response.choices[0].text.strip()


class MDGenerator:

    @staticmethod
    def readFileContent():
        source_directory = input("path/to/your/project:  ")
        python_files = glob.glob(os.path.join(source_directory, "*.py"))

        code = ""
        for python_file in python_files:
            with open(python_file, 'r') as file:
                code += file.read() + '\n'
        return code

    @staticmethod
    def createDirectory(projectName, summarized_code):
        directory_name = "MD_files"
        if not os.path.exists(directory_name):
            os.makedirs(directory_name)

        file_name = os.path.join(directory_name, f'{projectName}.md')
        if not os.path.exists(file_name):
            with open(file_name, "w") as f:
                f.write(summarized_code)
                print('Successfully created a markdown file for this project')
        else:
            print("A file under this name has already been used")


if __name__ == "__main__":
    open_ai = OpenAi()
    md_generator = MDGenerator()

    project_name = input("Please provide your projectName:  ")
    project = md_generator.readFileContent()

    md_code = open_ai.summarize_code(project)
    md_generator.createDirectory(project_name, md_code)

