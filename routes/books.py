from fastapi import APIRouter, HTTPException, Depends

router = APIRouter(
    prefix="books",
    tags=['Books'],
    
)

@router.get('')
async def get_all():
    pass

@router.post('')
async def add():
    pass

@router.put('/{book_id}/')
async def update():
    pass 

@router.delete('/{book_id}/')
async def delete():
    pass