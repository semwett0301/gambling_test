# 📊 Experiment Data Analyzer

## Overview
This project is designed to gather and analyze datasets from an experiment efficiently. It follows a structured architecture incorporating design patterns such as Observer and Strategy to ensure modularity and scalability.

## 📂 Project Structure

```
📦 analyser
├── 📂 dto        # Common data transfer objects (DTOs) and interfaces
├── 📂 listeners  # Observer pattern listeners used in services
├── 📂 services   # Main logic and publisher classes
├── 📂 utils      # Helper functions and utility classes
└── 📂 readers    # Strategy pattern-based implementations for reading screenshots from different sources
```

### 🔹 `dto/`
Contains common interfaces and data transfer objects to facilitate communication between different components of the project.

### 🔹 `listeners/`
Implements the **Observer** pattern to handle event-driven interactions. Listeners in this directory react to events triggered by services.

### 🔹 `services/`
The core of the application. This directory contains **publishers** responsible for processing data and orchestrating the overall functionality of the system.

### 🔹 `utils/`
Includes various helper functions and utility classes that provide additional functionality to support the main processing logic.

### 🔹 `readers/`
Implements the **Strategy** pattern to enable flexible reading of screenshots from multiple sources. Each strategy provides a unique way to extract and process image-based data.

---

## 🚀 Getting Started
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Required dependencies (see `requirements.txt`)

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/analyser.git
   cd gambling_test
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

### Usage
Run the main script to start the analyzer:
```sh
python main.py
```

---
## 🛠 Design Patterns
- **Observer Pattern**: Used in `listeners/` to manage event-driven workflows.
- **Strategy Pattern**: Implemented in `readers/` to support flexible input processing.

## 🛠 Technology stack
- **Computer Vision**: library `cv2` and `pytesseract`