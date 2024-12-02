from fastapi import FastAPI
import uvicorn
from products.views import router as products_router
from users.views import router as users_router
from attachment.views import router as attachment_router


app = FastAPI()
app.include_router(products_router, prefix="/products")
app.include_router(users_router, prefix="/users")
app.include_router(attachment_router, prefix="/attachment")


@app.get("/")
def hello_index():
    return {
        "massage": "Hello index!",
    }


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
