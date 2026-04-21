from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List, Dict, Any
import shutil
import os

app = FastAPI()

# In-memory store for processing tasks and presets (for demonstration)
tasks: Dict[str, str] = {}
presets: List[str] = ["preset1", "preset2", "preset3"]  # Replace with actual presets

@app.post("/upload")
async def upload_video(video: UploadFile = File(...)):
    video_path = f"uploads/{{video.filename}}"
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
    task_id = f"task_{{len(tasks) + 1}}"  # Simulated task ID
    tasks[task_id] = "Uploaded"  # Update status
    return {"task_id": task_id, "message": "Video uploaded successfully."}

@app.post("/edit")
async def edit_video(task_id: str, preset: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    if preset not in presets:
        raise HTTPException(status_code=400, detail="Invalid preset")
    tasks[task_id] = f"Editing with {{preset}}"  # Simulate editing
    return {"task_id": task_id, "status": "Editing started."}

@app.get("/status/{task_id}")
async def get_status(task_id: str):
    status = tasks.get(task_id, "Task not found")
    return {"task_id": task_id, "status": status}

@app.get("/download/{file_id}")
async def download_file(file_id: str):
    # Simulate file download
    file_path = f"processed/{{file_id}}.mp4"  # Simulated file path
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return {"file_id": file_id, "download_url": f"/files/{{file_id}}.mp4"}

@app.get("/presets")
async def list_presets():
    return {"presets": presets}