from fastapi import FastAPI

app= FastAPI()

@app.get("/home")
def home():
    print("succesfully run")
    print("hii")
    return {"message": "welcome Home"}

@app.get("/login")
def login():
    return {"message": "welcome to Login Page"}