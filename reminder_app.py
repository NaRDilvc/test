import os
import json
import requests
import tkinter as tk
from datetime import datetime, timezone


class ReminderApp:
    def __init__(self, root):
        self.root = root
        root.title("Today's Meetings and Tasks")
        root.attributes('-topmost', True)
        root.geometry('400x400')

        self.meeting_label = tk.Label(root, text="Today's Teams Meetings", font=('Arial', 14, 'bold'))
        self.meeting_label.pack(pady=5)

        self.meeting_list = tk.Listbox(root, width=50)
        self.meeting_list.pack(pady=5)

        self.todo_label = tk.Label(root, text='To Do List', font=('Arial', 14, 'bold'))
        self.todo_label.pack(pady=5)

        self.todo_list = tk.Listbox(root, width=50)
        self.todo_list.pack(pady=5)

        self.refresh_button = tk.Button(root, text='Refresh', command=self.refresh)
        self.refresh_button.pack(pady=10)

        self.refresh()

    def refresh(self):
        self.load_meetings()
        self.load_todos()

    def load_meetings(self):
        self.meeting_list.delete(0, tk.END)
        meetings = fetch_todays_meetings()
        if not meetings:
            self.meeting_list.insert(tk.END, 'No meetings found.')
        for meeting in meetings:
            start = meeting.get('start')
            subject = meeting.get('subject')
            self.meeting_list.insert(tk.END, f"{start} - {subject}")

    def load_todos(self):
        self.todo_list.delete(0, tk.END)
        todos = load_todos()
        if not todos:
            self.todo_list.insert(tk.END, 'No tasks.')
        for todo in todos:
            self.todo_list.insert(tk.END, f"- {todo}")


def fetch_todays_meetings():
    token = os.getenv('GRAPH_TOKEN')
    if not token:
        return []
    headers = {'Authorization': f'Bearer {token}'}
    today = datetime.now(timezone.utc).astimezone().date().isoformat()
    url = (
        'https://graph.microsoft.com/v1.0/me/calendarview'
        f'?startDateTime={today}T00:00:00&endDateTime={today}T23:59:59'
    )
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return []
    data = resp.json().get('value', [])
    meetings = []
    for item in data:
        meetings.append({
            'start': item['start']['dateTime'][11:16],
            'subject': item['subject']
        })
    return meetings


def load_todos():
    path = 'todo.json'
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        try:
            tasks = json.load(f)
        except json.JSONDecodeError:
            return []
    return tasks


if __name__ == '__main__':
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()
