# storage.py
import uuid
from datetime import datetime

DB = {
    "research": {},
    "documents": {}
}

def create_research(query, parent_id=None):
    research_id = str(uuid.uuid4())
    DB["research"][research_id] = {
        "id": research_id,
        "query": query,
        "parent_id": parent_id,   
        "status": "RUNNING",
        "report": None,
        "summary": None,
        "reasoning": None,
        "sources": [],
        "tokens": {},
        "cost": 0.0,
        "trace_id": None,
        "created_at": datetime.utcnow()
    }
    return research_id

def update_research(research_id, **kwargs):
    DB["research"][research_id].update(kwargs)

def get_research(research_id):
    return DB["research"].get(research_id)

def list_research():
    return list(DB["research"].values())
