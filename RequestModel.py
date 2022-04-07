from pydantic import BaseModel

class PlayerProfile(BaseModel):
    username: str
    password: str

class UpdateMMR(BaseModel):
    username: str
    score: int

class GameStatus(BaseModel):
    isActive: bool
    isWin: int
    ls1: bool
    ls2: bool
    ls3: bool