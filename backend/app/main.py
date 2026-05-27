from fastapi import FastAPI, Depends
from typing import Annotated
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models import Tenant


app = FastAPI(title="Online Ordering System API")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.get("/tenants")
def list_tenants(db: Annotated[Session, Depends(get_db)]) -> list[dict[str, str]]:
    stmt = select(Tenant)
    tenants = db.execute(stmt).scalars().all()
    
    return [{"slug": t.slug, "name": t.name} for t in tenants]


