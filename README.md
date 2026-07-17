# 🩸 Mystic Falls Diaries (Django Chronicles)

[![Django Version](https://img.shields.io/badge/django-5.0+-092e20?style=for-the-badge&logo=django)](https://vampirediaries.net)
[![Faction](https://img.shields.io/badge/Factions-Vampire%20%7C%20Witch%20%7C%20Werewolf%20%7C%20Hybrid-purple?style=for-the-badge)](#)
[![Security](https://img.shields.io/badge/Protection-Vervain%20Enforced-red?style=for-the-badge)](#)

> *"Dear Diary, today a vampire asked me my name. I said Elena. Then he forced me to forget. Good thing I have this database..."*

Welcome to **Mystic Falls Diaries**, a secure, lore-friendly Django web application where supernatural beings and vulnerable humans can record their daily struggles, dark secrets, and hunger cravings without the fear of Original Vampires compelling their minds.

---

## 🏛️ Features & Supernatural Mechanics

*   **Supernatural Council Signup:** Register your profile and choose your faction carefully. Power always comes with a price.
    *   *Available Factions:* Human, Vampire, Witch, Werewolf, Doppelgänger, and Hybrid.
*   **Cloaked Authentication:** "Break the Seal" to unlock your diary or initiate your story through tailored, safe cryptographic portals.
*   **Vervain Mind Protection:** A toggleable security feature. If enabled, your secrets are completely shielded from Damon or Klaus's compulsion. If unprotected, your mind remains vulnerable.
*   **Threat Level Assessment:** Rate your day from `1` (Human Calm) to `5` (Ripper on the Loose) to track the chaos level in town.

---

## ⚙️ Tech Stack & Architecture

*   **Backend:** Python 3.x & Django Web Framework
*   **Database:** SQLite / PostgreSQL (Stores your secrets away from supernatural eyes)
*   **Frontend:** Semantic HTML5, CSS3 (Custom gothic-themed UI utilizing `Cinzel` and `IM Fell English` typography)
*   **Security:** Django Built-in Password Hashing & CSRF Protection tokens (The ultimate anti-magic barrier)

---

## 📂 Project Structure Overview

The project is split into two core grimoires (apps):
*   `supernatural_users`: Manages the Extended `UserProfile` (Factions, Locations, Bios) and the customized sign-up mechanism.
*   `entries`: Handles the creation, encryption simulation (`Vervain`), and retrieval of daily diary logs.

---

## 🚀 Installation & Local Setup

To lift the cloaking spell and run this project on your local machine, follow these steps:

### 1. Clone the Grimoire
```bash
git clone [https://github.com/your-username/mystic-falls-diaries.git](https://github.com/your-username/mystic-falls-diaries.git)
cd mystic-falls-diaries
```

### 2. Set Up the Safe Environment
Create and activate a virtual environment:
``` python
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
Ensure Django is installed:
``` python
pip install django
```

### 4. Apply the Migrations
Generate and execute database migrations to prepare the journal indices:
``` python
python manage.py makemigrations
python manage.py migrate
```

### 5. Cross the Threshold (Run Server)
Fire up the local development server:
``` python
python manage.py runserver
```

Now open your browser and navigate to http://127.0.0.1:8000/diary/.


















