from pydantic import BaseModel



class questionSchema(BaseModel):
    username: str
    email: str
    text: str


class answerSchema(BaseModel):
    text: str
    question_id: int 