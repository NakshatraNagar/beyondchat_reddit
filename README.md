# Reddit User Persona Generator 

Hi! 👋  

This project takes a Reddit user profile link, collects their recent posts and comments, and creates a simple user persona based on their activity.

---

## 📂 What's Inside This Repo?

| File Name | Purpose |
|-----------|---------|
| `project.py` | Python script to collect Reddit data |
| `kojied_data.txt` | Raw posts/comments from user `kojied` |
| `kojied_persona_output.txt` | GPT-style user persona for `kojied` |
| `Hungry-Move-6603_data.txt` | Raw data from user `Hungry-Move-6603` |
| `Hungry-Move-6603_persona_output.txt` | GPT-style user persona for `Hungry-Move-6603` |

---

## 🛠️ How to Run This Project

> Follow these simple steps 👇

### 1. Install Required Library
You need to install `praw`, a Python Reddit API wrapper.

```bash
pip install praw
```

---

### 2. Run the Python Script

```bash
python project.py
```

It will ask you to enter a Reddit profile link, like:

```
https://www.reddit.com/user/kojied/
```

---

### 3. What Will Happen?

- The script will collect the user's recent Reddit posts and comments.
- It will save the data in a `.txt` file like this:
  ```
  kojied_data.txt
  ```
- A user persona is then created manually (with help from GPT) and saved in:
  ```
  kojied_persona_output.txt
  ```

---

## 💡 Note About GPT

Due to OpenAI API credit limits, the GPT part is **not automated in the script**.  
Instead, I generated the persona using GPT separately and included it as a `.txt` file.
If I had sufficient amount of credits then i should have done it.

---

## ✅ Assignment Covered Points

- ✅ Reddit scraping with Python  
- ✅ Persona building using GPT  
- ✅ Clear citations included  
- ✅ Clean, simple, beginner-friendly code  
- ✅ README with easy instructions  
