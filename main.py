



from typing import List, Optional
from fastapi import FastAPI, Query
from fastapi.encoders import jsonable_encoder  #to encode our responses
from model.dbHandler import match_exact, match_like


app = FastAPI()

@app.get("/")
def index():
    """
    usage of the API
    1. Provide usage instructions formatted as json
    """
    response = {"usage":"/dict?word=<word>"}
    return jsonable_encoder(response)
    

  

@app.get("/dict")  # the dictionary method handles the GET requests
def dictionary(word:str): #we add 'word' as a parameter.
    """
    DEFAULT ROUTE. This method will
    1. accept a word from the request
    2. try to find an exact match and return it if found
    3. if not found, find all approx matches and return 
    """
    if not word:  # if no word is provided at all!
        response = {
            "status":"error",
            "word":word,
            "data":"you initiated an empty search!"
            }
        return jsonable_encoder(response)

    definitions = match_exact(word)
    if definitions:
        response = {"status":"success","word":word, "data":definitions}
        return jsonable_encoder(response)
    
#    # approximate match
#    definitions = match_like(word)
#    if definitions:
#        response = {"status":"partianl", "word":word, "data":definitions}
#        return 
#    else:
#        response = {"status":"error", "word":word, "data": "word not found"}
#    return jsonable_encoder(response)