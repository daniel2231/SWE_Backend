import os, re

def run_readability_check():

    output = os.popen(f"pylama ./app/result/userCode.py  -l \"mypy\"").read()
    error = len(output.split("\n")) - 1
    result = 20 - error

    mypy = {"score": result if result >= 0 else 0, "error": output}

    output = os.popen(f"pylama ./app/result/userCode.py  -l \"pylint\"").read()
    error = len(output.split("\n")) - 1
    result = int(20 - error)

    pylint = {"score": result if result >= 0 else 0, "error": output}

    output = os.popen(f"pylama ./app/result/userCode.py  -l \"eradicate\"").read()
    error = len(output.split("\n")) - 1
    result = 20 - error

    eradicate = {"score": result if result >= 0 else 0, "error": output}

    output = os.popen(f"pylama ./app/result/userCode.py  -l \"radon\"").read()
    error = len(output.split("\n")) - 1
    result = 20 - error

    radon = {"score": result if result >= 0 else 0, "error": output}

    output = os.popen(f"pylama ./app/result/userCode.py  -l \"pycodestyle\"").read()
    error = len(output.split("\n")) - 1
    result = 20 - error

    pycodestyle = {"score": result if result >= 0 else 0, "error": output}

    return {"mypy": mypy, "pylint": pylint, "eradicate": eradicate, "radon": radon, "pycodestyle": pycodestyle}