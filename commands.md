

- python -m venv fastapi_env

- source fastapi_env/Scripts/activate

- python -m pip install fastapi uvicorn requests psycopg2

- uvicorn hello_fastapi_requests:company_app

- uvicorn fastapi_inventory_app:app
