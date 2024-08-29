# 📅 ScreenTime Script 📅

Welcome to the ScreenTime Script! 🎉 This tool helps you track your screen time on a Linux computer. Follow the steps below to set it up and integrate it into your daily workflow. 🌟

## 🚀 Quick Start Guide

### 1. Clone the Repository

First, clone this repository to your local machine:
```bash
git clone https://github.com/ShivangSrivastava/screentime-script.git
cd screentime-script
```

### 2. Rename and Move Files

Move the provided files to `/usr/local/bin` for system-wide accessibility. You can rename them as needed.

```bash
# Rename files
mv startscreentime.sh startscreentime
mv screentime.sh screentime
# Move files
sudo mv startscreentime /usr/local/bin/
sudo mv screentime /usr/local/bin/
sudo mv screentime.py /usr/local/bin/
```

### 3. Make Scripts Executable

Ensure the scripts have execute permissions:
```bash
sudo chmod +x /usr/local/bin/startscreentime
sudo chmod +x /usr/local/bin/screentime
```

### 4. Add `startscreentime` Command to Your Shell Configuration

To make the `startscreentime` command available in your terminal, add the following line to your `.bashrc` or `.zshrc` file:

```bash
echo startscreentime > ~/.bashrc
# or
echo startscreentime > ~/.zshrc
```

After updating your `.bashrc` or `.zshrc`, reload the file:

```bash
source ~/.bashrc
# or
source ~/.zshrc
```

## 🛠️ Usage

### Start Tracking Screen Time

> Open terminal to initiate screen time tracking

### Display Screen Time

You can display today's screen time or view all screen time records:

- To view today's screen time:
  ```bash
  screentime
  ```

- To view all screen time records:
  ```bash
  screentime -a
  ```

- To view today's raw screen time (without additional string):
  ```bash
  screentime -r
  ```

## 🤝 Contributing

Feel free to open issues or submit pull requests if you have any suggestions or improvements!

---
Happy tracking! 🕒✨
