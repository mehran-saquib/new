"""

The python file to run the FastAPI.
Type "uvicorn app:app --reload" tp run this file

"""

from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from database_ import engine,SessionLocal
import models
from sqlalchemy.orm import Session

import predictor
import math

app=FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

models.Base.metadata.create_all(engine)

templates = Jinja2Templates(directory="templates")

@app.get("/")
def form_post(request:Request):
    result=""
    return templates.TemplateResponse('value_predictor.html', context={'request':request, 'result':result})

@app.post("/")
def form_post(request:Request, 
                radio:str=Form(...), 
                radio1:str=Form(...),
                radio2:str=Form(...), 
                radio3:str=Form(...), 
                radio4:str=Form(...), 
                radio5:str=Form(...), 
                radio6:str=Form(...),
                text:int=Form(...),
                text1:int=Form(...),
                text2:int=Form(...),
                text3:int=Form(...),
                db:Session=Depends(get_db)
                ):
    prediction_value=predictor.predict(radio,
                                        radio1,
                                        text,
                                        text1,
                                        radio2,
                                        radio3,
                                        radio4,
                                        radio5,
                                        radio6,
                                        text2,
                                        text3)
                            
    new_data=models.variables(
        property_type=radio,
        log_price=prediction_value,
        room_type=radio1,
        accommodates=text,
        bathrooms=text1,
        bed_type=radio2,
        cancellation_policy=radio3,
        cleaning_fee=radio4,
        city=radio5,
        instant_bookable=radio6,
        bedrooms=text2,
        beds=text3)
        
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    result_inserted="The values are inserted"
    result=round(math.exp(prediction_value),2)  
    result="$"+str(result)  
    return templates.TemplateResponse('value_predictor.html', context={'request':request, 'result':result})


#The below functions are not gonna be utilized in website for now
@app.get("/insert")
def form_insert(request:Request):
    result_inserted=""
    return templates.TemplateResponse('value_insertor.html', context={'request':request, 'result_inserted':result_inserted})


@app.post("/insert")
def form_post(request:Request, 
                radio:str=Form(...),    #Property Type
                radio1:str=Form(...),   #Room Type
                radio2:str=Form(...),   #Bed Type
                radio3:str=Form(...),   #Cancellation Policy
                radio4:str=Form(...),   #Cleaning Fee
                radio5:str=Form(...),   #City
                radio6:str=Form(...),   #Instant Bookable
                text:int=Form(...),     #Number of accomodates
                text1:int=Form(...),    #Number of Bathrooms
                text2:int=Form(...),    #Number of Bedrooms
                text3:int=Form(...),    #Enter number of beds
                text4:int=Form(...),    #Enter the predicted price
                db:Session=Depends(get_db)
                ):

    text4=math.log(text4)
    new_data=models.variables(
        property_type=radio,
        log_price=text4,
        room_type=radio1,
        accommodates=text,
        bathrooms=text1,
        bed_type=radio2,
        cancellation_policy=radio3,
        cleaning_fee=radio4,
        city=radio5,
        instant_bookable=radio6,
        bedrooms=text2,
        beds=text3)
        
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    result_inserted="The values are inserted"
    return templates.TemplateResponse('value_insertor.html', context={'request':request, 'result_inserted':result_inserted})
