from fastapi import APIRouter, Depends
from app.models.user import User
from app.models.local_monitoring import LocalMonitoring
from sqlalchemy.orm import Session
from app.db.dependencies import get_db


router = APIRouter()

@router.post("/")
def create_user(
    email: str,
    name_local: str,
    db: Session= Depends(get_db)
):
    
    try:

        local_monitoring = LocalMonitoring(name_local=name_local)
        db.add(local_monitoring)
        db.commit()
        db.refresh(local_monitoring)

        user=User(
        email=email,
        local_monitoring_id = local_monitoring.id
        )

        db.add(user)
        db.commit()
        db.refresh(user)


        return {"message": "Usuário criado com sucesso", 
                "user": user.email, 
                "local_monitoring": local_monitoring.name_local}


    except:
        return { 500, "01X35 - Ocorreu um erro interno ao processar sua solicitação"}
    

@router.delete("/")
def remove_user(email: str, db:Session):
    
    try:
        db_user=  db.query(User).filter(User.email == email).first()

        if db_user:
             db.delete(db_user)
             db.commit()

             message = f"Endereço {db_user.email} removido com sucesso!"
    
        else:
             message = "Usuário não localizado"

        return {"message": message}



    except:
            return { 500, "01X35 - Ocorreu um erro interno ao processar sua solicitação"}
    




