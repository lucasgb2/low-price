from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.productrouter import routerproduct
from router.marketplacerouter import routermarketplace
from router.userrouter import routeruser
from router.pricerouter import routerprice
import uvicorn
import os

if os.environ.get('ENV') and os.environ['ENV'] == 'PROD':
    print('Run App PROD')
else:
    from dotenv import load_dotenv
    load_dotenv()

app = FastAPI()

@app.get('/api/v1/lowprice')
async def fn():
    return {'api': 'lowprice'}

origins = ["*"]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"])
app.include_router(routerproduct)
app.include_router(routermarketplace)
app.include_router(routeruser)
app.include_router(routerprice)

PORTAPI = int(os.environ['PORTAPI'])

if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', reload=True, port=PORTAPI)
