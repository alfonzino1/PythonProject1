from fastapi import FastAPI
app = FastAPI()
@app.get("/health")
def health()->dict:
    """отправляет сообщение о том что сервис жив"""
    return {
        "status": "ok",
        "version": "1.0",
    }
@app.get("/sales/summary")
def summary()->dict:
    """считает сумму, длину и round"""
    raw_sales_data = {
        "transactions": [
            {"id": 1, "manager": "Анна", "region": "Москва", "amount": 1500},
            {"id": 2, "manager": "Борис", "region": "Санкт-Петербург", "amount": 2300},
            {"id": 3, "manager": "Анна", "region": "Москва", "amount": 800},
            {"id": 4, "manager": "Вера", "region": "Казань", "amount": 3200},
            {"id": 5, "manager": "Борис", "region": "Санкт-Петербург", "amount": 1200},
            {"id": 6, "manager": "Вера", "region": "Казань", "amount": 950}
        ]
    }
    amounts = [t["amount"] for t in raw_sales_data["transactions"]]
    total_sales=sum(amounts)
    count = len(set(t["region"] for t in raw_sales_data["transactions"]))
    return {"total_sales": total_sales,
            "top_manager": "Вера",
            "regions_count": count,
            "currency": "RUB"}
