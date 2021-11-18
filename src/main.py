import fastapi as _fastapi
import service as _service
import starlette.responses as _responses

app = _fastapi.FastAPI()


@app.get("/")
async def root():
    return _responses.RedirectResponse("/redoc")


@app.get("/gameWinner")
async def gameWinner():
    return _service.calculate_winner()
