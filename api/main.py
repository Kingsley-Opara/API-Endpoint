from fastapi import FastAPI

app = FastAPI()

myself = "I'm Kingsley, a 300 level medical student in AE-FUNAI and also a Full Stack Developer"

@app.get('/')
def home():
    data = {
        'slackUsername': 'kingboy',
        'backend': True,
        'age': 20,
        'bio': myself
    }
    return data