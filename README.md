# 🎚️ Studio Time Calc
**A Precision Delay & Reverb Timing Utility for Modern Producers**

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![CustomTkinter](https://img.shields.io/badge/GUI-CustomTkinter-blue?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)

---

### 📥 [Download the Windows .exe](YOUR_GOOGLE_DRIVE_LINK_HERE)

---

## ⚡ The Problem
In music production, setting your delay times and reverb decays manually can be a buzzkill. If your timings aren't mathematically synced to the BPM, your mix sounds "muddy." 

**Studio Time Calc** fixes this by giving you sample-accurate millisecond values instantly.



---

## ✨ Key Features
* **Instant Sync:** Type your BPM and hit `Enter` — no extra clicks needed.
* **One-Tap Copy:** Click "COPY" and the button turns green to confirm. Values are saved to your clipboard for instant pasting into your DAW.
* **Pro Layout:** Dark Mode interface designed to look like a hardware rack unit.
* **Precision Math:** Calculates down to 2 decimal places for 1/4, 1/8, 1/16, 1/32, and Reverb Bar lengths.

---

## 🛠️ Technical Breakdown
Built as part of my **BCA curriculum**, this project focuses on:
1.  **Event Binding:** Handling keyboard interrupts (`<Return>`).
2.  **Threaded UI:** Smooth transitions using the `after()` method for button feedback.
3.  **Encapsulation:** Clean, Object-Oriented Python code.

🚀 How to Run
Download: Grab the .exe from the link above.

Run: Open Delay Calculator.exe.

Calculate: Type your BPM (e.g., 128) and hit Enter.

Paste: Click COPY and paste the value into your VST/Plugin.

📸 Preview
Tip: Take a screenshot of your app, upload it to GitHub, and replace this text with the image link!

👨‍💻 Author
Created with ❤️ by  chinmaya

GitHub: @chinmaya_353

Portfolio: https://chinmaya353.netlify.app/

Developed for the music community. If this helped your workflow, give it a ⭐!
```python
# The Core Logic
ms_per_quarter = 60000 / bpm
