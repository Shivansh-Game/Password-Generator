# 🔐 Password Generator

A simple yet powerful **Python Password Generator** that creates strong, secure, and customizable passwords. It also checks the password’s strength and allows you to **copy it directly to your clipboard** for easy use.

---

## 🚀 Features

* ✅ **Random password generation** with uppercase, lowercase, digits, and symbols
* 🧠 **Password strength checker** (Weak / Medium / Strong)
* 📋 **Copy password to clipboard** using `pyperclip`
* 🎨 **Colored terminal output** using ANSI escape codes
* 🔁 Option to **generate multiple passwords** without restarting the program

---

## 🛠️ Requirements

Make sure you have Python **3.10+** installed.

Install required module:

```bash
pip install pyperclip
```

---

## ▶️ How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/password-generator.git
   ```
2. Navigate into the folder:

   ```bash
   cd password-generator
   ```
3. Run the script:

   ```bash
   python password_generator.py
   ```

---

## 🧩 Usage

1. Enter the desired **password length** (minimum 4).
2. The script will:

   * Generate a password
   * Display its **strength level**
   * Ask if you want to **copy it to clipboard**
3. You can generate as many passwords as you like — type **“no”** to exit.

---

## 🧱 Example Output

```
Enter length of your password: 12

Your generated password is: vA@8g#Tn1ZpQ
Password strength: Strong

Do you want to copy password?(yes/no): yes
Password is copied to clipboard!

Do you want to generate another password?(yes/no): no
Exiting Password Generator
```

---

## 🧠 How It Works

* Ensures all character types (lowercase, uppercase, digit, symbol) are included.
* Uses `random` for secure password generation.
* Evaluates strength based on:

  * Length
  * Character variety (upper/lower, numbers, symbols)

---

## 📄 License

This project is open source and available under the **MIT License**.

---

## 💡 Future Improvements

* GUI version using **Tkinter** or **PyQt**
* Option to save passwords securely
* Add entropy-based strength estimation
