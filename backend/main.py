
import os
import requests
from fastapi import FastAPI, Depends, HTTPException
from backend.database import engine, SessionLocal
from backend.models import Base, Transaction, Category
from dotenv import load_dotenv
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta

load_dotenv()

app = FastAPI()

# Create tables if they don't exist
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic Schemas
class CategoryCreate(BaseModel):
    name: str

class CategoryOut(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class TransactionCreate(BaseModel):
    amount: float
    description: str = ""
    timestamp: str = None
    category_id: int = None

# Simple keyword-to-category mapping
KEYWORD_CATEGORY_MAP = {
    "uber": "Transport",
    "bolt": "Transport",
    "bus": "Transport",
    "taxi": "Transport",
    "restaurant": "Food",
    "cafe": "Food",
    "groceries": "Food",
    "supermarket": "Food",
    "netflix": "Subscriptions",
    "spotify": "Subscriptions",
    "gym": "Subscriptions",
    "airtime": "Utilities",
    "electricity": "Utilities",
    "rent": "Housing",
}

def categorize_transaction(description: str, db: Session) -> int | None:
    desc_lower = description.lower()
    for keyword, cat_name in KEYWORD_CATEGORY_MAP.items():
        if keyword in desc_lower:
            # Find or create category
            category = db.query(Category).filter(Category.name == cat_name).first()
            if not category:
                category = Category(name=cat_name)
                db.add(category)
                db.commit()
                db.refresh(category)
            return category.id
    return None

class TransactionOut(BaseModel):
    id: int
    amount: float
    description: str
    timestamp: datetime
    category_id: int = None
    class Config:
        orm_mode = True

# Analytics Schemas
class AnalyticsOut(BaseModel):
    category: str
    total: float

class TrendOut(BaseModel):
    category: str
    trend: str
    change: float

class ForecastOut(BaseModel):
    estimated_balance: float
    recurring_expenses: float

# AI Insights Schemas
class InsightsRequest(BaseModel):
    analytics: list[AnalyticsOut]
    trends: list[TrendOut]
    forecast: ForecastOut

class InsightsResponse(BaseModel):
    insights: str

# Endpoints
@app.get("/")
def root():
    return {"message": "FinSense AI Backend is running"}

# Category Endpoints
@app.post("/categories", response_model=CategoryOut)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    existing = db.query(Category).filter(Category.name == category.name).first()
    if existing:
        raise HTTPException(status_code=409, detail="Category already exists")
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

@app.get("/categories", response_model=list[CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return db.query(Category).all()

# Transaction Endpoints
@app.post("/transactions", response_model=TransactionOut)
def create_transaction(tx: TransactionCreate, db: Session = Depends(get_db)):
    # If no category_id, try to categorize automatically
    category_id = tx.category_id
    if not category_id:
        category_id = categorize_transaction(tx.description, db)
    db_tx = Transaction(
        amount=tx.amount,
        description=tx.description,
        timestamp=tx.timestamp,
        category_id=category_id
    )
    db.add(db_tx)
    db.commit()
    db.refresh(db_tx)
    return db_tx

@app.get("/transactions", response_model=list[TransactionOut])
def get_transactions(category_id: int = None, db: Session = Depends(get_db)):
    query = db.query(Transaction)
    if category_id:
        query = query.filter(Transaction.category_id == category_id)
    return query.all()

# Analytics Endpoints
@app.get("/analytics", response_model=list[AnalyticsOut])
def analytics(db: Session = Depends(get_db)):
    results = db.query(Category.name, func.sum(Transaction.amount))\
        .join(Transaction, Transaction.category_id == Category.id)\
        .group_by(Category.name).all()
    return [AnalyticsOut(category=cat, total=total or 0) for cat, total in results]

@app.get("/trends", response_model=list[TrendOut])
def trends(db: Session = Depends(get_db)):
    now = datetime.utcnow()
    last_week = now - timedelta(days=7)
    prev_week = now - timedelta(days=14)
    categories = db.query(Category).all()
    output = []
    for cat in categories:
        last = db.query(func.sum(Transaction.amount)).filter(
            Transaction.category_id == cat.id,
            Transaction.timestamp >= last_week,
            Transaction.timestamp < now
        ).scalar() or 0
        prev = db.query(func.sum(Transaction.amount)).filter(
            Transaction.category_id == cat.id,
            Transaction.timestamp >= prev_week,
            Transaction.timestamp < last_week
        ).scalar() or 0
        change = last - prev
        if prev == 0:
            trend = "new" if last > 0 else "no change"
        elif change > 0:
            trend = "increase"
        elif change < 0:
            trend = "decrease"
        else:
            trend = "no change"
        output.append(TrendOut(category=cat.name, trend=trend, change=change))
    return output

@app.get("/forecast", response_model=ForecastOut)
def forecast(db: Session = Depends(get_db)):
    now = datetime.utcnow()
    start_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    days_in_month = (now.replace(month=now.month % 12 + 1, day=1) - start_month).days
    days_passed = (now - start_month).days + 1
    total_spent = db.query(func.sum(Transaction.amount)).filter(Transaction.timestamp >= start_month).scalar() or 0
    avg_daily = total_spent / days_passed if days_passed > 0 else 0
    recurring = db.query(func.sum(Transaction.amount)).filter(Transaction.description.ilike('%rent%')).scalar() or 0
    estimated_balance = avg_daily * days_in_month + recurring
    return ForecastOut(estimated_balance=estimated_balance, recurring_expenses=recurring)

# AI Insights Endpoint
@app.post("/insights", response_model=InsightsResponse)
def generate_insights(data: InsightsRequest):
    prompt = f"""
    You are a financial coach. Given the following analytics, trends, and forecast, generate clear, actionable insights for the user:
    Analytics: {data.analytics}
    Trends: {data.trends}
    Forecast: {data.forecast}
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return InsightsResponse(insights="AI insights unavailable: API key not set.")
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 300
        }
    )
    if response.status_code == 200:
        result = response.json()
        insight = result["choices"][0]["message"]["content"]
        return InsightsResponse(insights=insight)
    else:
        return InsightsResponse(insights="AI insights unavailable: API error.")
