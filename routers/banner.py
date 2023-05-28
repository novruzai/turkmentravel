from fastapi import *
from sqlalchemy.orm import *
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import crud
from db import get_db


banner_router = APIRouter(tags=['Banner'])

@banner_router.post('/add-banner')
def add_banner(db: Session = Depends(get_db), file: UploadFile = File(...)):
    try:
        result = crud.create_banner(db, file)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'Create banner failed'})


@banner_router.get('/get-banner')
def get_banner(
    page: int,
    limit: int,
    db: Session = Depends(get_db)
):
    try:
        result = crud.read_banner(page, limit, db)
        result = jsonable_encoder(result)
        return JSONResponse(status_code=status.HTTP_200_OK, content=result)
    except Exception as e:
        print(e)
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'result': 'Something went wrong'})
