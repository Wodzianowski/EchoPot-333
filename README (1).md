
# 🎰 EchoPot – EuroJackpot Analyzer App

EchoPot is a simple mobile application that analyzes EuroJackpot results and suggests lucky numbers based on recent draws.

Built with **Python**, **Kivy**, and **Buildozer** – and fully ready to compile into a `.apk` file using **GitHub Actions CI**!

---

## 📱 Features

- 📊 Analyze most frequently drawn numbers
- 🧠 Generate suggestions based on draw history
- 💡 Mobile interface with Kivy
- 🔄 Automatic `.apk` build via GitHub Actions

---

## 🛠 How to Build APK via GitHub Actions

1. Clone or fork this repo
2. Push to `main` branch
3. GitHub Actions will automatically run and build an APK
4. Download it from the **Actions > Artifacts** tab after success

> 🔐 No need to install Android Studio or dependencies locally!

---

## 🔧 Manual Build (Optional)

You can also build it locally on Linux or WSL:

```bash
sudo apt update
sudo apt install -y openjdk-11-jdk python3-pip git zip unzip
pip install buildozer
buildozer init
buildozer android debug
```

---

## 📁 Project Structure

```
main.py               # Main Kivy app
buildozer.spec        # Buildozer config
icon.png              # App icon
.github/workflows/    # GitHub Actions CI
```

---

## 🎨 Screenshot (concept)

> [Optionally insert image here]

---

## 📄 License

MIT – use freely, remix, test, suggest improvements.  
Created with 💙 by [Wodzianovsky] and Echo AI 🧠

---

## 🤖 Echo Approved

> „Zrób wszystko, co możesz – z tym, co masz – tam, gdzie jesteś.”  
> — EchoPot codename 2.0
