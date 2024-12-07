# **API-Key-Harvester**  

![image](https://github.com/user-attachments/assets/2dbb660b-c7d1-40ef-9f7c-b6bf19f9660a)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/github/license/BuildaCyberLab/domain-dominator)
![Repo Stars](https://img.shields.io/github/stars/BuildaCyberLab/domain-dominator?style=social)

**Scans file directories, repositories, or configurations for hardcoded API keys, secrets, or sensitive credentials.**  

## **Features**  
- Detects common API key patterns (e.g., AWS, Google, Stripe, etc.).  
- Scans through directories recursively to find sensitive credentials.  
- Lightweight and simple to use.  

---

## **Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/YourUsername/API-Key-Harvester.git
cd API-Key-Harvester
```

### **2. Set Up Python Environment**  
Ensure Python 3.x is installed on your machine. Install the required libraries:  
```bash
pip install -r requirements.txt
```  
(Note: If there’s no `requirements.txt`, this project only needs Python’s built-in libraries, so no extra installation is required.)

---

## **Usage**  

### **Basic Command**  
Run the tool to scan a specific directory:  
```bash
python api_key_harvester.py /path/to/scan
```  

- Replace `/path/to/scan` with the absolute or relative path to the directory you want to scan.  
- If no path is provided, it will default to the current directory.  

### **Example Output**  
```text
[!] Found API Key in config.json: ['AIzaSyD1234567890-ExampleKey123456']
[!] Found API Key in app.py: ['sk_live_abcdefghijklmnopqrstuvwxyz12']
```  

### **Common Patterns Detected**  
- **AWS Access Keys**: `AKIA[0-9A-Z]{16}`  
- **Google API Keys**: `AIza[0-9A-Za-z-_]{35}`  
- **Stripe Live Keys**: `sk_live_[0-9a-zA-Z]{24}`  

### **Custom Pattern Matching**  
You can add custom patterns by modifying the `patterns` list in the script:  
```python
patterns = [
    r"AKIA[0-9A-Z]{16}",  # AWS Access Key
    r"AIza[0-9A-Za-z-_]{35}",  # Google API Key
    r"sk_live_[0-9a-zA-Z]{24}",  # Stripe Live Key
    r"your-custom-pattern-here",  # Add your own pattern
]
```

---

## **Examples**  

### **Scan a Specific Folder**  
```bash
python api_key_harvester.py /home/user/projects
```

### **Save Results to a File**  
Modify the script to write results to a log file, or redirect output:  
```bash
python api_key_harvester.py /path/to/scan > results.txt
```

---

## **Contributing**  
1. Fork this repository.  
2. Create a new branch: `git checkout -b feature-branch-name`.  
3. Commit your changes: `git commit -m "Add a new feature"`.  
4. Push to the branch: `git push origin feature-branch-name`.  
5. Submit a pull request.  

---

## **License**  
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  
