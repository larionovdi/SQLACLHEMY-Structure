import fastapi
import uvicorn

from containers import Container
from users.api import router as user_router

app = fastapi.FastAPI()
app.include_router(user_router, prefix="/users")

container = Container()


if __name__== '__main__':
    uvicorn.run(app)