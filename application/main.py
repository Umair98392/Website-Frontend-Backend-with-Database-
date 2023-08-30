from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from . import crud, models, schemas
from .database import SessionLocal, engine

#The statement below is used to create the tables in database.
#This step initializes the tables based on the models defined in the models module.
models.Base.metadata.create_all(bind=engine)

#Create a FastAPI app instance
app = FastAPI()


# Configure CORS settings
origins = [
    
    
    "http://127.0.0.1:8085"
       # Adjust this to match your frontend's URL
    # Add more allowed origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
#This function returns a session from the SessionLocal
#We need to have an independent database session/connection (SessionLocal) per request,
#use the same session through all the request and then close it after the request is finished.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#Define API endpoints:
#The application defines several API endpoints for user and item management 
#using FastAPI's decorators (@app.post, @app.get).
# and create FastAPI path operations code (example: def create_user())

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@app.get("/")
def root():
    html_content = """
            <!DOCTYPE html>
            <html>
                <body>
                    <h1>API Documentation</h1>
                    <p>Welcome to our API! Below are the available endpoints:</p>
                    <ul>
                        <li><a href="/docs">API Documentation (Swagger UI)</a></li>
                        <li><a href="/users">GET /users - Get a list of users</a></li>
                        <li><a href="/items">GET /items - Get a list of items</a></li>
                        <!-- Add more links for other endpoints -->
                    </ul>
                </body>
            </html>
        """
    return HTMLResponse(content=html_content)

    
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users



@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user





@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
