from fastapi import APIRouter, Body, Request, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from .models import groupModel, authenticationCodeModel, UpdateTaskModel

router = APIRouter()

# get all authentication codes


@router.get("/", response_description="check the code is wether enable")
async def check_code(request: Request):
    codes = []
    for doc in await request.app.mongodb["authentication_code"].find().to_list(length=100):
        codes.append(doc)
    return codes


@router.post("/", response_description="Add new group")
async def create_group(request: Request, group: groupModel = Body(...)):
    group = jsonable_encoder(group)
    new_group = await request.app.mongodb["group_id"].insert_one(group)
    created_task = await request.app.mongodb["group_id"].find_one(
        {"_id": new_group.inserted_id}
    )

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_task)


@router.get("/", response_description="List all groups")
async def list_tasks(request: Request):
    tasks = []
    for doc in await request.app.mongodb["group_id"].find().to_list(length=100):
        tasks.append(doc)
    return tasks


@router.get("/{id}", response_description="Get a specific group info")
async def show_task(id: str, request: Request):
    if (task := await request.app.mongodb["group_id"].find_one({"_id": id})) is not None:
        return task

    raise HTTPException(status_code=404, detail=f"Task {id} not found")


@router.put("/{id}", response_description="Update the specific group info")
async def update_task(id: str, request: Request, group: UpdateTaskModel = Body(...)):
    group = {k: v for k, v in group.dict().items() if v is not None}
    print(group)

    if len(group) >= 1:
        update_result = await request.app.mongodb["group_id"].update_one(
            {"_id": id}, {"$set": group}
        )

        if update_result.modified_count == 1:
            if (
                updated_group := await request.app.mongodb["group_id"].find_one({"_id": id})
            ) is not None:
                return updated_group

    if (
        existing_group := await request.app.mongodb["group_id"].find_one({"_id": id})
    ) is not None:
        return existing_group

    raise HTTPException(status_code=404, detail=f"Task {id} not found")


@router.delete("/{id}", response_description="Delete group")
async def delete_task(id: str, request: Request):
    delete_result = await request.app.mongodb["group_id"].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Group {id} not found")
