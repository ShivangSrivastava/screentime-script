# 📅 ScreenTime Script 📅

Welcome to the **ScreenTime Script**! This handy tool helps you keep track of your screen time on your Linux computer. Follow the instructions below to get started and integrate it into your workflow.

## 🛠️ Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ShivangSrivastava/screentime-script.git
   cd screentime-script
   ```

2. **Rename files i.e. remove .sh**

   ```bash
   # Keep .sh file
   cp startscreentime.sh startscreentime
   cp screentime.sh screentime
   # Rename original file
   mv startscreentime.sh startscreentime
   mv screentime.sh screentime
   ```

3. **Move Scripts to `/usr/local/bin`:**

   This makes the scripts available system-wide.

   ```bash
   sudo cp startscreentime /usr/local/bin/
   sudo cp screentime /usr/local/bin/
   ```

4. **Make Scripts Executable:**

   Ensure the scripts have execute permissions.

   ```bash
   sudo chmod +x /usr/local/bin/startscreentime
   sudo chmod +x /usr/local/bin/screentime
   ```

5. **Add `startscreentime` Command to Your Shell Configuration:**

   Add the following line to your `.bashrc` or `.zshrc` file to ensure the script runs every time you open a terminal.

   ```bash
   echo 'startscreentime' >> ~/.bashrc# For Bash users
   echo 'startscreentime' >> ~/.zshrc# For Zsh users
   ```

   After updating your `.bashrc` or `.zshrc`, reload the file:

   ```bash
   source ~/.bashrc# For Bash users
   source ~/.zshrc# For Zsh users
   ```

## 🖥️ Usage

- **Default Usage:** To calculate the screen time for the current date, simply run:

  ```bash
  screentime
  ```

- **Show Screen Time for All Dates:** To display screen time for all recorded dates, use:

  ```bash
  screentime -a
  ```

## 📜 Script Overview

### `startscreentime`

- **Purpose:** Logs your active screen time to `/tmp/screen_time_log.txt`.
- **Behavior:** Runs when you open a new terminal and logs the timestamp if the system is active.

### `screentime`

- **Purpose:** Calculates the total screen time based on the log entries.
- **Options:**
- **Default:** Shows screen time for the current date.
- **`-a`:** Shows screen time for all recorded dates.

## 🔄 Updates & Maintenance

Feel free to contribute or suggest improvements! If you encounter any issues, open an issue on the repository or submit a pull request.

---

Thank you for using the **ScreenTime Script**! Stay productive and keep track of your screen time efficiently! 🚀
