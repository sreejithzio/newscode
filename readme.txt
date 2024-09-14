step 1 
Create a virtual env
python -m venv env
env/Scripts/activate


step2 
install all requirements
pip install -r requirements.txt


step3
- http://127.0.0.1:8000/get
call the above api  for fetching data from news api and store it into our DB

- http://127.0.0.1:8000/
List all news from our DB

- http://127.0.0.1:8000/get_by_title/
call the above api as post requiets
