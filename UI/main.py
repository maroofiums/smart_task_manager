import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(layout="wide")
st.title("Smart Task Manager Dashboard")


def fetch_tasks():
    try:
        res = requests.get(f"{API_URL}/tasks/")
        res.raise_for_status()
        return res.json()
    except Exception as e:
        st.error(f"Backend Error: {e}")
        return []


# ---------------- CREATE ----------------
st.sidebar.header("Create Task")

title = st.sidebar.text_input("Title")
description = st.sidebar.text_area("Description")
priority = st.sidebar.selectbox("Priority", [1, 2, 3])

if st.sidebar.button("Add Task"):
    payload = {
        "title": title,
        "description": description,
        "priority": priority
    }
    try:
        requests.post(f"{API_URL}/tasks/", json=payload)
        st.sidebar.success("Task Added")
        st.rerun()
    except:
        st.sidebar.error("Error creating task")


tasks = fetch_tasks()

# ---------------- SEARCH & FILTER ----------------
st.header("Search & Filters")

col1, col2, col3 = st.columns(3)

with col1:
    search = st.text_input("Search Title")

with col2:
    priority_filter = st.selectbox("Priority", ["All", 1, 2, 3])

with col3:
    status_filter = st.selectbox("Status", ["All", "Completed", "Pending"])


filtered = tasks

if search:
    filtered = [t for t in filtered if search.lower() in t["title"].lower()]

if priority_filter != "All":
    filtered = [t for t in filtered if t["priority"] == priority_filter]

if status_filter == "Completed":
    filtered = [t for t in filtered if t["completed"]]
elif status_filter == "Pending":
    filtered = [t for t in filtered if not t["completed"]]


st.header("Tasks")

for task in filtered:
    col1, col2, col3 = st.columns([4, 1, 1])

    with col1:
        st.subheader(task["title"])
        st.write(task["description"])
        st.write(f"Priority: {task['priority']}")
        st.write(f"Completed: {task['completed']}")

    with col2:
        if st.button("Toggle", key=f"toggle_{task['id']}"):
            requests.put(
                f"{API_URL}/tasks/{task['id']}",
                json={"completed": not task["completed"]}
            )
            st.rerun()

    with col3:
        if st.button("Delete", key=f"delete_{task['id']}"):
            requests.delete(f"{API_URL}/tasks/{task['id']}")
            st.rerun()
