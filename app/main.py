from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.category_routes import router as category_router
from app.routes.expense_routes import router as expense_router

app = FastAPI()

@app.get("/health-check")
def health_check():
    return True

app.include_router(user_router)
app.include_router(category_router)
app.include_router(expense_router)