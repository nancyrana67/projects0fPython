# Personal Journal Manager

A lightweight, command-line interface (CLI) Python application that allows users to write, view, search, and manage a personal daily journal. All entries are saved locally in a plain text file, ensuring privacy and ease of access.

---

## ✨ Features

* **Add New Entries:** Save thoughts with a custom date and time timestamp.
* **View Full History:** Read through all past journal entries formatted cleanly in the console.
* **Keyword & Date Search:** Quickly find specific entries by searching for keywords or dates.
* **Secure Reset:** Delete all entries with a built-in safety confirmation prompt.
* **Robust Error Handling:** Smoothly handles missing files, empty states, and OS-level permission errors without crashing.

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.x** installed on your system. 

### Installation
1. Clone or download this repository to your local machine.
2. Ensure the main Python script (e.g., `journal.py`) is in your desired working directory.

### Running the Application
Open your terminal or command prompt, navigate to the project directory, and execute:

```bash
python journal.py

🛠️ How It Works
Upon launching, you will be greeted with an interactive main menu:

Welcome to Personal Journal Manager!
Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

1. Adding an Entry
Inputs are structured to capture both a manual timestamp and your thoughts:

Format: [YYYY-MM-DD HH:MM:SS] followed by your text body.

2. Storage
All data is persistently saved to a file named journal.txt generated automatically in the same directory as the script.

📂 Project Structure
├── journal.py         # Main application script containing the JournalManager class
└── journal.txt        # Auto-generated text file containing saved entries

📝 License
This project is open-source and free to use for personal or educational purposes.
