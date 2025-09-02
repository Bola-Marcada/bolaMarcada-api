from fastapi import APIRouter, HTTPException
from schemas.sports_center_schema import CreateSportsCenterSchema
from sqlalchemy.orm import Session
from database import get_db
from fastapi import Depends

sports_center_router = APIRouter(prefix="/sports_centers", tags=["sports_centers"])


@sports_center_router.post("/create")
async def create_sports_center(
    create_sports_center_schema: CreateSportsCenterSchema,
    session: Session = Depends(get_db),
):

    try:
        # Verifica se o CNPJ já está cadastrado
        cnpj = (
            session.query(sports_centers)
            .filter_by(cnpj=create_sports_center_schema.cnpj)
            .first()
        )

        if cnpj:
            # Já existe um centro esportivo com esse CNPJ
            raise HTTPException(status_code=400, detail="CNPJ já cadastrado.")
        else:
            # Cria um novo centro esportivo
            new_sports_center = SportsCenter(
                user_id=create_sports_center_schema.user_id,
                name=create_sports_center_schema.name,
                cnpj=create_sports_center_schema.cnpj,
                latitude=create_sports_center_schema.latitude,
                longitude=create_sports_center_schema.longitude,
                photo_path=create_sports_center_schema.photo_path,
                description=create_sports_center_schema.description,
            )
            session.add(new_sports_center)
            session.commit()
            session.refresh(new_sports_center)

            return {
                "message": "Centro esportivo criado com sucesso.",
                "sports_center_id": new_sports_center.id,
            }

    # Caso dê erro ao criar o centro esportivo
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail={"message": "Erro ao criar centro esportivo.", "error": str(e)},
        )
