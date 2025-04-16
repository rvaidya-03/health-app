from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow React development server to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)
