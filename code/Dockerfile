# ubuntu_python_fastapi.dockerfile
# Step 1. Download the ubuntu image
FROM ubuntu:latest

# Step 2. Update apt 
RUN apt update

# Step 3. Install python3 and python3-pip using apt
RUN apt install -y python3 python3-pip

# Step 4. Install fastapi and uvicorn with pip
RUN python3 -m pip install fastapi uvicorn

COPY ./hello_fastapi_requests.py / 

CMD ["uvicorn", "--host=0.0.0.0", "--port=8080", "hello_fastapi_requests:company_app"]