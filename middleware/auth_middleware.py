from fastapi import FastAPI, Request, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Dict, Any
from utils.jwtmanadger import JWTManager

app = FastAPI()
security = HTTPBearer()
jwt_manager = JWTManager()

# Middleware для проверки JWT
@app.middleware("http")
async def jwt_auth_middleware(request: Request, call_next):

    if request.url.path in ["/docs", "/openapi.json", "/login", "/register"]:
        return await call_next(request)

    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    token = auth_header.split()[1]
    try:
        payload = await jwt_manager.verify_token(token)
        request.state.user = payload
    except HTTPException:
        raise

    return await call_next(request)


