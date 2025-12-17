# orm_project

A small Django project prepared for upload.

## What I added

- `.gitignore` — common Python / Django ignores
- `requirements.txt` — minimal dependencies
- `README.md` — this file

## How to push this project to GitHub (run from project root)

```powershell
cd "C:\Users\mkp94\OneDrive\Desktop\Django\orm_project"
# initialize repo if needed
git init
git add .
git commit -m "Initial commit"
# set remote (replace if you already have a remote)
git remote add origin https://github.com/Mangal9101/orm_project.git
git branch -M main
# push (you may be prompted to authenticate / use a token)
git push -u origin main
```

## Install and run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

If you want, I can initialize git and attempt to push from here; pushing may require GitHub credentials or a personal access token.