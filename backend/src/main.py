from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from router.productrouter import routerproduct
from router.marketplacerouter import routermarketplace
from router.userrouter import routeruser
from router.pricerouter import routerprice
from database import dbconnection, schemas
import uvicorn
import time

schemas.Base.metadata.create_all(bind=dbconnection.engine)

origins = ["http://localhost",
           "http://localhost:8080",
           "http://192.168.0.106:8000"]
app = FastAPI()


@app.get('/')
async def fn():
    return {'fn': 'ok'}


app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
app.include_router(routerproduct)
app.include_router(routermarketplace)
app.include_router(routeruser)
app.include_router(routerprice)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=8000, host='192.168.0.106')
    #uvicorn.run("main:app", reload=True, port=8000, host='186.251.15.106')
