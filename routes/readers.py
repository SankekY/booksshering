from fastapi import APIRouter, HTTPException, status, Depends
from middleware.auth_middleware import JWTMiddleware

router = APIRouter(
    prefix="readers",
    tags="Readers"
)

auth = JWTMiddleware()

@router.get('', Depends(auth.verify_token()))
async def getAll():
    pass 

@router.post('')
async def create():
    pass

@router.put('/{reader_id}/')
async def update(reader_id: str):
    if not reader_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found Reader ID"
        )
    pass

@router.delete('/{reader_id}/')
async def delete(reader_id: str):
    if not reader_id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Not found Reader ID"
        )
    pass