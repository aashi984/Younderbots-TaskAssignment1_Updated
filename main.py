from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.status import HTTP_303_SEE_OTHER
from database import engine, Base, get_db, Vaccination

Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    vaccinations = db.query(Vaccination).all()
    return templates.TemplateResponse("index.html", {"request": request, "vaccinations": vaccinations})

@app.post("/add", response_class=HTMLResponse)
def add(
    name: str = Form(...), age: int = Form(...), gender: str = Form(...),
    vaccine_name: str = Form(...), dose_number: int = Form(...),
    vaccination_date: str = Form(...), email: str = Form(...), contact_number: str = Form(...),
    db: Session = Depends(get_db)
):
    db.add(Vaccination(
        name=name, age=age, gender=gender, vaccine_name=vaccine_name,
        dose_number=dose_number, vaccination_date=vaccination_date,
        email=email, contact_number=contact_number
    ))
    db.commit()
    return RedirectResponse("/", status_code=HTTP_303_SEE_OTHER)

@app.get("/edit/{vaccination_id}", response_class=HTMLResponse)
def edit(request: Request, vaccination_id: int, db: Session = Depends(get_db)):
    vaccination = db.query(Vaccination).filter(Vaccination.id == vaccination_id).first()
    return templates.TemplateResponse("edit.html", {"request": request, "vaccination": vaccination})

@app.post("/update/{vaccination_id}", response_class=HTMLResponse)
def update(
    vaccination_id: int, name: str = Form(...), age: int = Form(...), gender: str = Form(...),
    vaccine_name: str = Form(...), dose_number: int = Form(...),
    vaccination_date: str = Form(...), email: str = Form(...), contact_number: str = Form(...),
    db: Session = Depends(get_db)
):
    v = db.query(Vaccination).filter(Vaccination.id == vaccination_id).first()
    v.name, v.age, v.gender, v.vaccine_name = name, age, gender, vaccine_name
    v.dose_number, v.vaccination_date, v.email, v.contact_number = dose_number, vaccination_date, email, contact_number
    db.commit()
    return RedirectResponse("/", status_code=HTTP_303_SEE_OTHER)

@app.get("/delete/{vaccination_id}")
def delete(vaccination_id: int, db: Session = Depends(get_db)):
    db.delete(db.query(Vaccination).filter(Vaccination.id == vaccination_id).first())
    db.commit()
    return RedirectResponse("/", status_code=HTTP_303_SEE_OTHER)
