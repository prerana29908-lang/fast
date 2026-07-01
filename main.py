from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import engine, get_db
import model
from model import Student
import schemas

app = FastAPI()

model.Base.metadata.create_all(bind=engine)

@app.post("/students")
def create_student(student: schemas.StudentCreate,
                   db: Session = Depends(get_db)):

    new_student = Student(
        name=student.name,
        age=student.age,
        course=student.course,
        email=student.email
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student