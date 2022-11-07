import fastapi
import uvicorn

print("hello")

api = fastapi.FastAPI()
@api.get("/")
def index():
    return {"msg" : "This is the landing page"}
@api.get("/api/endpoint")
def endpoint():
    return{"msg" : "Hello FastAPI"}

uvicorn.run(api)