# SMVE - Social Media Video Editor

## Folder Structure

```
SMVE/
  ├── backend/
  │   ├── app/
  │   ├── main.py
  │   └── requirements.txt
  ├── frontend/
  │   ├── app/
  │   └── requirements.txt
  ├── core/
  │   ├── video_processing/
  │   │   ├── silence_removal.py
  │   │   ├── transitions.py
  │   │   ├── effects.py
  │   │   ├── split_screen.py
  │   │   ├── b_roll.py
  │   │   ├── react.py
  │   │   ├── comparisons.py
  │   │   ├── zoom.py
  │   │   └── auto_captions.py
  ├── models/
  │   ├── __init__.py
  │   └── database_models.py
  ├── tasks/
  │   ├── __init__.py
  │   └── celery_tasks.py
  ├── tests/
  │   ├── __init__.py
  │   └── test_app.py
  └── docs/
      ├── index.md
      └── requirements.md
```

## Description

This is the core folder structure for the SMVE project, outlining the organization of backend and frontend code, video processing modules, database models, task queues, tests, and documentation.