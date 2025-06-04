# Reminder App

This repository includes a small FastAPI example and a stylish Windows-based reminder UI built with ttkbootstrap.

## Running the API

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

## Reminder UI

`reminder_app.py` shows today's Microsoft Teams meetings and tasks from `todo.json` in a window that stays on top. It uses the [ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap) theme library for a more modern look.

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
   You can change the theme by editing `reminder_app.py` and passing a different
   `themename` to `ttk.Window`.

The window will remain above other applications and display your meetings and tasks.
