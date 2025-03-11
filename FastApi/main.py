from fastapi import FastAPI
#to activate the virtual enviroment: source .venv/bin/activate
#to deactivate the virtual enviroment: deactivate

app = FastAPI()
#to raise the server: #fastapi dev main.py# !!Works as well as the command under here, better use this one, the documentation uses it as well.
#to raise the server: univorn main:app --reload.
#unicorn:{name of the server plug in}, main:{name of the file.py where we are working}, app:{name of the application that we create on our file.py}, --reload:{reload the page in real time as we are working on the file, like a debugger}


#url local http://127.0.0.1:8000/
@app.get("/")
async def root():
    return "Hola Mundo"

#url local http://127.0.0.1:8000/url
@app.get("/url")
async def root():
    return { "urls_curso":"http://aymama.nya" }

#To access the documentation you can use 'http://127.0.0.1:8000/docs' or 'http://127.0.0.1:8000/redoc' 