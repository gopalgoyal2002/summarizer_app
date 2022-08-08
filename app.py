import logging

import uvicorn
from fastapi import FastAPI

logger = logging.getLogger(__name__)
logger.info("Open http://127.0.0.1:8000/docs to API Documentation.")
from apis.router import router

def get_application() -> FastAPI:
    app = FastAPI(title="summarizer-api", debug=True, version="1.0")

    
    app.include_router(router)

    return app


app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)