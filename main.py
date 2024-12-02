from contextlib import asynccontextmanager

from fastapi import FastAPI
import uvicorn
from products.views import router as products_router
from users.views import router as users_router
from attachment.views import router as attachment_router
from core.models import Base, db_helper

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with db_helper.engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#         yield


app = FastAPI()
app.include_router(products_router, prefix='/products')
app.include_router(users_router, prefix='/users')
app.include_router(attachment_router, prefix='/attachment')

@app.get('/')
def hello_index():
    return {
        "massage":"Hello index!",
    }

if __name__ == '__main__':
    uvicorn.run('main:app', reload = True)