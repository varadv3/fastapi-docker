from fastapi import FastAPI, HTTPException, status
from schemas import Code
from test import execute

app = FastAPI()

@app.post("/compile")
def compile(code: Code):

    # Write source Code
    with open("IO/script.py", "w") as source_code:
        source_code.write(code.source_code)

    # Write input file
    with open("IO/input.txt", "w") as input:
        input.write(code.input)

    returncode = execute()
    
    try:
        if(returncode == 0):
            with open("IO/output.txt", "r") as output:
                result = output.read()
        else:
            with open("IO/error.txt", "r") as error:
                result = error.read()
    except Exception as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return {"returncode": returncode, "desc": result}