from datetime import datetime
from typing import Annotated
from pydantic import UUID4, BaseModel, Field



class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid' #não deixa campos extras q não foram definidos no modelo.
        from_attributes = True #Isso permite que o FastAPI preencha automaticamente os campos da classe de esquema com base nos atributos que correspondem aos campos da solicitação HTTP. Isso é útil ao lidar com dados de solicitação e evita a necessidade de atribuir manualmente cada campo.

class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data de criação')]
