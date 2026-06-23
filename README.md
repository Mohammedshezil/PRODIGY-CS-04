# KeyMon 🚀
### Interactive Keylogger with Console Interface • Python

![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![pynput](https://img.shields.io/badge/Library-pynput-green.svg)
![License-MIT](https://img.shields.io/badge/License-MIT-orange.svg)
![Status-Academic](https://img.shields.io/badge/Status-Internship_Project-cyan.svg)

---

## 🔍 Overview
### About the Project
**KeyMon** is an interactive, console-based keylogger designed for cybersecurity education and system monitoring. Built with Python and the `pynput` library, it features a bold, professional terminal interface that allows users to configure logging paths and control the monitoring process in real-time. This project demonstrates low-level input hooking and file I/O operations while emphasizing ethical usage.

---

## 🛠️ What It Does
* **Real-time Keystroke Monitoring:** Captures both alphanumeric and special keys.
* **Custom Storage Path:** Interactive menu to select where to save logs.
* **Bold Console UI:** High-contrast ASCII art and color-coded status updates.
* **Manual Control:** Dedicated start/stop functionality via the control panel.
* **Modular Design:** Built with clean, reusable Python classes.

---

## ⚙️ How It Works

| Step | Action | Description |
| :--- | :--- | :--- |
| **01** | **Hook** | Background Listener hooks into system input via `pynput`. |
| **02** | **Event** | Handlers differentiate between chars and special keys. |
| **03** | **Log** | Logging Module appends data with high-precision timestamps. |
| **04** | **Pathing** | Dynamic Pathing verifies directory existence before writing. |
| **05** | **UI** | ANSI Escape Codes provide the bold, colorful terminal UI. |
| **06** | **Shutdown** | Safe Termination allows for graceful listener shutdown. |

---

## 🚦 Status Levels

* 🟢 **Idle:** Program is running but the listener is not active.
* 🟡 **Configure:** User is modifying the log storage directory.
* 🔴 **Logging Active:** Keystrokes are being captured and saved to file.

---

## 📋 Features Implemented
* [x] **Interactive Menu:** Selection-based navigation system.
* [x] **ASCII Branding:** Large block-style header for "KeyMon".
* [x] **Error Handling:** Validates directory paths before initialization.
* [x] **Session Logging:** Appends data across multiple sessions.
* [x] **Cross-Platform Support:** Compatible with both Linux and Windows.

---

## 👨‍💻 Developer Credits
**Developer:** [Mohammed Shezil](https://github.com/Mohammedshezil)  
**Organization:** Prodigy Infotech  
**Task:** Task 04 - Simple Keylogger  
*Developed as part of the Cybersecurity Internship program.*

---

## ⚠️ Ethical Disclaimer
*This tool is intended for educational purposes only. Unauthorized use of this software to monitor keystrokes on machines you do not have explicit permission to access is illegal and unethical. Use responsibly.*

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.8+**
* **pip** (Python package installer)

### Installation

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/Mohammedshezil/PRODIGY-CS-04.git](https://github.com/Mohammedshezil/PRODIGY-CS-04.git)
   cd PRODIGY-CS-04
   ```

2. **Install Dependencies**
   The project requires the `pynput` library to monitor hardware input.
   ```bash
   pip install pynput
   ```

3. **Run the Application**
   ```bash
   python keymon.py
   ```
