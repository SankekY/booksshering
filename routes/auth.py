from utils.jwtmanadger import JWTManager
from fastapi.security import HTTPAuthorizationCredentials
from fastapi import Depends, security, APIRouter, HTTPException
from typing import Dict, Any
from models.LibrarianModel import LibrarianS
from models.TokenModel import TokenData

jwt_manager = JWTManager()

router = APIRouter(prefix='/login/')

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> Dict[str, Any]:
    return await jwt_manager.verify_token(credentials.credentials)



@router.post("register")
async def register(user: LibrarianS) -> TokenData:
    access_token = await jwt_manager.create_access_token(
        data={"sub": user.email, "role": "admin"}
    )
    return {
        "status": True,
        "access_token": access_token, "token_type": "bearer"
    }

@router.post("login")
async def login(user: LibrarianS) -> TokenData:

    access_token = await jwt_manager.create_access_token(
        data={"sub": user.email, "role": "admin"}
    )
    return {"access_token": access_token, "token_type": "bearer"}
