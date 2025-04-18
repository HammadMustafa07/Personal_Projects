
---

# Quiz Application

A basic quiz tool created using Python, UV, and Streamlit.

## Getting Started

### 1️⃣ Set Up UV

To begin, install **UV** (skip if already installed):

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

For users on Windows:

```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Check if UV installed correctly:

```sh
uv --version
```

---

### 2️⃣ Initialize the Project Folder

Start a new project with the following commands:

```sh
uv init quiz-app
cd quiz-app
```

---

### 3️⃣ Add Streamlit as a Package

Install **Streamlit** as a required package:

```sh
uv add streamlit
```

---

### 4️⃣ Activate the Virtual Environment (Windows)

Use this command to activate:

```sh
.venv\Scripts\activate
```

For macOS/Linux systems:

```sh
source .venv/bin/activate
```

---

### 5️⃣ Launch the Quiz App

To run the application:

```sh
streamlit run main.py
```

🎉 And you're done! Your quiz application is now up and running 🚀

---
