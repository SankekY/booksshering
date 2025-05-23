from fastapi import HTTPException, status
from fastapi.security import HTTPBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import os

class JWTManager:
    def __init__(self):
        self.jwt_secret_key = os.getenv("JWT_SECRET_KEY", "your-secret-key")
        self.jwt_algorithm = os.getenv("JWT_ALGORITHM", "HS256")
        self.jwt_access_expire = int(os.getenv("JWT_ACCESS_EXPIRE_MINUTES", "30"))

    async def create_access_token(
        self, 
        data: Dict[str, Any], 
        expires_delta: Optional[timedelta] = None
    ) -> str:
        """
        Создает JWT токен доступа
        """
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=self.jwt_access_expire))
        to_encode.update({"exp": expire})
        
        try:
            return jwt.encode(
                to_encode,
                self.jwt_secret_key,
                algorithm=self.jwt_algorithm
            )
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Token creation error"
            )

    async def verify_token(self, token: str) -> Dict[str, Any]:
        try:
            return jwt.decode(token, self.jwt_secret_key, algorithms=[self.jwt_algorithm])
        except JWTError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid token: {str(e)}",
                headers={"WWW-Authenticate": "Bearer"}
            )