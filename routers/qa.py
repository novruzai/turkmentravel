from fastapi import *
from sqlalchemy.orm import *
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from models import *
import crud
from db import get_db


qa_router = APIRouter()


@qa_router.post('/add-question')
def add_question(req: questionSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_qa(req, Question, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'Something went wrong'})


@qa_router.post('/add-answer')
def add_answer(req: answerSchema, db: Session = Depends(get_db)):
    try:
        result = crud.create_qa(req, Answer, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'Something went wrong'})


@qa_router.get('/get-questions')
def get_questions(req: questionSchema, db: Session = Depends(get_db)):
    try:
        result = crud.read_questions(db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'Something went wrong'})

