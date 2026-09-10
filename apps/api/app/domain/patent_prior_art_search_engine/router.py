from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.patent_prior_art_search_engine.schemas import AgenticPatentPriorArtSearchEngineSessionCreate, AgenticPatentPriorArtSearchEngineSessionResponse
from app.domain.patent_prior_art_search_engine.service import AgenticPatentPriorArtSearchEngineService

router = APIRouter(prefix="/api/v1/patent_prior_art_search_engine", tags=["Agentic Patent Prior Art Search Engine Domain"])

@router.post("/sessions", response_model=AgenticPatentPriorArtSearchEngineSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticPatentPriorArtSearchEngineSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Patent Prior Art Search Engine.
    """
    return AgenticPatentPriorArtSearchEngineService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticPatentPriorArtSearchEngineSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticPatentPriorArtSearchEngineService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
