from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from intelxapi import intelx
import json, os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")

INTELX_API_KEY = os.getenv('INTELX_API_KEY')
ix = intelx(INTELX_API_KEY)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "results": None})

@app.post("/", response_class=HTMLResponse)
async def search(request: Request, query: str = Form(...), maxresults=100, buckets=[], timeout=5, datefrom="", dateto="", sort=4, media=0, terminate=[]):
    results = ix.search(query, maxresults, buckets, timeout, datefrom, dateto, sort, media, terminate)
    
    return templates.TemplateResponse("index.html", {"request": request, "results": results["records"]})

@app.get("/view/{storageid}-{bucket}-{medi}", response_class=JSONResponse)
async def view(storageid: str, bucket=[], medi=24):
    try:
        # Ở đây, bạn sẽ cần sử dụng phương thức thích hợp từ intelxapi để lấy thông tin chi tiết
        # Ví dụ (giả sử có phương thức get_details):
        details = ix.FILE_VIEW(0, 23, storageid, bucket)
        if len(details) > 0:
            return JSONResponse(content=details)
        else:
            return JSONResponse(content="No data")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Item not found: {str(e)}")