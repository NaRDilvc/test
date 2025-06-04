# Reminder App

This repository includes a small FastAPI example and a simple Windows-based reminder UI written with Tkinter.

## Running the API

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Reminder UI

`reminder_app.py` shows today's Microsoft Teams meetings and tasks from `todo.json` in a window that stays on top.

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Obtain a Microsoft Graph API access token and set it in the `GRAPH_TOKEN` environment variable.
3. Create `todo.json` in the repository directory with a JSON array of tasks, e.g.:
   ```json
   ["Finish report", "Review pull requests"]
   ```
4. Run the UI:
   ```bash
   python reminder_app.py
   ```

The window will remain above other applications and display your meetings and tasks.
