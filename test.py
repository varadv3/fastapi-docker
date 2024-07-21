from subprocess import run

def execute():
    input = open("IO/input.txt", "r")
    output = open("IO/output.txt", "w")
    error = open("IO/error.txt", "w")

    result = run(["python3", "./IO/script.py"], stdin=input, stdout=output, stderr=error)

    print(result)

    input.close()
    output.close()
    error.close()

    return result.returncode