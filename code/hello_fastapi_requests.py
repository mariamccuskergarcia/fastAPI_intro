"""hello_fastapi_requests.py
"""
from fastapi import FastAPI
from pydantic import BaseModel

company_db = [
    {"ticker": "AAPL", "name": "Apple", "website": "www.apple.com"},
    {"ticker": "MSFT", "name": "Microsoft", "website": "www.microsoft.com"},
    {"ticker": "AMZN", "name": "Amazon", "website": "www.amazon.com"},
]

company_app = FastAPI()

@company_app.get("/")
def root():
    return {"app_info": "Company App v1.0"}


@company_app.get("/companies")
def get_companies():
    return company_db


@company_app.get("/companies/{ticker}")
def get_company_by_ticker(ticker: str): 
    for item in company_db:
        if item["ticker"] == ticker:
            return item

class Company(BaseModel):
    ticker: str
    name: str
    website: str

@company_app.post("/companies")
def add_company(company: Company):
    added_company = company.model_dump()
    company_db.append(added_company)
    return added_company

@company_app.put("/companies/{ticker}")
def update_company_by_ticker(ticker: str, company: Company):
    updated_company = company.model_dump()
    for n, item in enumerate(company_db):
        if item["ticker"] == ticker:
            company_db[n] = updated_company
            return updated_company

@company_app.delete("/companies/{ticker}")
def delete_company_by_ticker(ticker: str):
    for n, item in enumerate(company_db):
        if item["ticker"] == ticker:
            deleted_company = company_db.pop(n)
            return {"status":200}