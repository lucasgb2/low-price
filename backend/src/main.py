from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.productrouter import routerproduct
from router.marketplacerouter import routermarketplace
from router.userrouter import routeruser
from router.pricerouter import routerprice
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

origins = ["http://localhost",
           "http://localhost:8080",
           "http://192.168.0.106:8000"]
app = FastAPI()


@app.get('/api/v1/lowprice')
async def fn():
    return {'api': 'lowprice'}


app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
app.include_router(routerproduct)
app.include_router(routermarketplace)
app.include_router(routeruser)
app.include_router(routerprice)

PORT = int(os.environ['PORTAPI'])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, port=PORT)
