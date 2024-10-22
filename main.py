from fastapi import Response, FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO

from schemas import ProcessItem
from utils import load_config, post_process

config = load_config('config.yml')

app = FastAPI(
    title=config['app']['name'],
    version=config['app']['version'],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO(model=config['model']['name'])


@app.get("/health-check", status_code=status.HTTP_200_OK)
async def get_root():
    # todo
    return {"status": 'ok', "message": "service is running"}


@app.post('/predict')
def process_images(response: Response, data: ProcessItem,
                   ):
    try:
        result = model(data.urls)
        result = post_process(result, config['model']['label2fa'], config['model']['label2en'])
        return {'status': 'ok', 'result': result}
    except Exception as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {'status': 'error', 'message': str(e)}
