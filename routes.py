from fastapi import APIRouter, Depends, HTTPException
from database import get_db, engine
from schemas import RoupaRegister, RoupaUpdate, RoupaResponse
from models import Roupa, Base
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/roupas")

@router.get("/", response_model=list[RoupaResponse])
def allRoupas(db: Session = Depends(get_db)):
    return db.query(Roupa).all()

@router.get("/{roupa_id}", response_model=RoupaResponse)
def get_Roupa(roupa_id: int, db: Session = Depends(get_db)):
    roupa = db.query(Roupa).filter(Roupa.id == roupa_id).first()

    if not roupa:
        raise HTTPException(404, "Roupa não encontrada!")

    return roupa

@router.post("/", response_model=RoupaResponse)
def create_roupa(roupa: RoupaRegister ,db: Session = Depends(get_db)):
    rr = Roupa(**roupa.model_dump())
    db.add(rr)
    db.commit()
    db.refresh(rr)
    return rr

@router.delete("/{roupa_id}")
def delete_roupa(roupa_id: int, db: Session = Depends(get_db)):
    rr = db.query(Roupa).filter(Roupa.id == roupa_id).first()

    if not rr:
        raise HTTPException(404, "Roupa não encontrada!")

    db.delete(rr)
    db.commit()

    return {"message": "Roupa deletada com sucesso!"}

@router.patch("/{roupa_id}", response_model=RoupaResponse)
def update_roupa(roupa_id: int, up: RoupaUpdate ,db: Session = Depends(get_db)):
    rr = db.query(Roupa).filter(Roupa.id == roupa_id).first()

    if not rr:
        raise HTTPException(404, "Roupa não encontrada!")

    upd = up.model_dump(exclude_unset=True)

    for key, value in upd.items():
         setattr(rr, key, value)

    db.commit()
    db.refresh(rr)

    return rr


@router.get("/latest", response_model=RoupaResponse)
def get_latest_roupa(db: Session = Depends(get_db)):
    rr = db.query(Roupa).order_by(Roupa.id.desc()).first()

    if not rr:
        raise HTTPException(404, "Roupa não encontrada!")

    return rr

