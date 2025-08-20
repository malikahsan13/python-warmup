from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/submit-form/")
def submit_form(username: str = Form(...), password: str = Form(...)):
    print("username", username)
    print("password", password)
    
    return {"msg":"Form submitted successfully", "username": username}