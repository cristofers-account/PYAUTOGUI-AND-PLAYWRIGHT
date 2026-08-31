# PYAUTOGUI-AND-PLAYWRIGHT
# 🖥️ PyAutoGUI Automation Project

A Python-based GUI automation project created as part of my **Generative AI and Automation learning journey**.

## 📌 About the Project

This assignment demonstrates the use of **PyAutoGUI**, a Python library that allows programs to control the mouse and keyboard and interact with graphical user interfaces.

The project covers basic automation tasks such as mouse movement, mouse clicks, keyboard input, hotkeys, and timed actions.

## 🎯 Objectives

* Understand the fundamentals of **PyAutoGUI**
* Automate mouse and keyboard operations using Python
* Learn how Python can interact with desktop applications
* Build a foundation for future **AI automation and RPA projects**
* Practice creating, testing, and managing Python projects using Git and GitHub

## 🛠️ Technologies Used

| Technology            | Purpose                 |
| --------------------- | ----------------------- |
| 🐍 Python             | Programming language    |
| 🖱️ PyAutoGUI         | GUI automation          |
| 💻 VS Code / Terminal | Development environment |
| 🔀 Git                | Version control         |
| 🐙 GitHub             | Project repository      |

## 📂 Repository Structure

```text
PyAutoGUI-Assignment/
│
├── basic_pyautogui.py
├── README.md
└── requirements.txt
```

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-repository-url>
```

Navigate to the project folder:

```bash
cd PyAutoGUI-Assignment
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install the required package:

```bash
pip install pyautogui
```

## ▶️ Run the Project

Run the Python script:

```bash
python basic_pyautogui.py
```

The script will execute the programmed mouse and keyboard automation tasks.

## 🧩 PyAutoGUI Functions Used

The assignment demonstrates functions such as:

```python
pyautogui.moveTo()
pyautogui.click()
pyautogui.write()
pyautogui.press()
pyautogui.hotkey()
pyautogui.sleep()
```

## ⚠️ Important Note

PyAutoGUI directly controls the computer's mouse and keyboard.

Before running the program:

* Save any important work
* Make sure the correct application is open
* Check the coordinates used in the script
* Test the automation carefully

PyAutoGUI's failsafe can be enabled with:

```python
pyautogui.FAILSAFE = True
```

Moving the mouse to the **top-left corner of the screen** can then trigger the failsafe.

## 📈 Learning Outcome

This assignment helped me understand how Python can be used to automate repetitive desktop tasks.

It provides a foundation for progressing toward:

* 🤖 AI Automation
* ⚙️ Workflow Automation
* 🖥️ Desktop Automation
* 🔄 Robotic Process Automation (RPA)
* 🧠 AI-powered business automation

## 🚀 Future Improvements

Possible future enhancements include:

* Automating real-world workflows
* Adding image recognition
* Integrating AI tools
* Automating browser-based tasks
* Building end-to-end AI automation workflows

## 👨‍💻 Author

**Christopher Fredrick**

### 🎓 Generative AI & Automation Learning Project

---

⭐ If you find this project useful, feel free to explore the code and learn from it.

# Cricbuzz Match Screenshot Automation

An automated script built with **Playwright** that launches Google Chrome, navigates to Cricbuzz, locates the latest live match, and captures a full-page screenshot as a PNG file.

## 📋 Features

* **Official Chrome Launch:** Automatically launches the official Google Chrome browser instead of the default Chromium binary.
* **Smart Elements Tracking:** Dynamically waits for live score elements to render completely before taking actions.
* **Full-Page Capture:** Captures the entire vertical length of the match center, including the detailed scorecard and recent commentary.
* **Graceful Fallbacks:** Captures a fallback homepage screenshot if a specific live match link cannot be parsed.

## ⚙️ How It Works (Workflow Description)

1. **Launch Browser:** Initializes Playwright to launch a dedicated instance of the official **Google Chrome** browser with a standardized desktop viewport (1280x800).
2. **Navigate to Cricbuzz:** Navigates directly to `https://cricbuzz.com` and pauses until network activity settles (`networkidle`) to guarantee all real-time live scores are fully loaded.
3. **Identify Latest Match:** Automatically scans the homepage's live ticker or match center grid, targets the primary link for the **latest live match**, and simulates a user click.
4. **Capture & Save PNG:** Waits for the match details page to render, captures a vertical **full-page screenshot** (ensuring the full scorecard and commentary are included), and saves the file locally as a high-quality **`.png` image**.

## 🚀 Setup & Execution

### Prerequisites
Make sure you have Python installed, then install the required dependencies:

```bash
pip install playwright
playwright install chrome
```

### Running the Script
Execute the automation script using the following command:

```bash
python main.py
```

## 📂 Output
Upon successful execution, the script will generate a file named **`latest_match_score.png`** in your project's root directory.

