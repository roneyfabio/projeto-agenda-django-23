Skip to content
luizomf
projeto-agenda-django-23
Repository navigation
Code
Issues
Pull requests
Agents
Actions
Projects
Security and quality
Insights
Files
Go to file
t
T
.vscode
base_static
base_templates
comandos
README.md
contact
project
.gitignore
manage.py
projeto-agenda-django-23
/comandos/
luizomf
luizomf
Criando e editando a senha de um super usuário Django
d52e8d7
 · 
3 years ago
projeto-agenda-django-23
/comandos/
Name	Last commit message	Last commit date
..
README.md
Criando e editando a senha de um super usuário Django
3 years ago
README.md
Iniciar o projeto Django

python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact
Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
Migrando a base de dados do Django

python manage.py makemigrations
python manage.py migrate
Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py changepassword USERNAME
