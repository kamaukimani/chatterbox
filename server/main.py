from app import create_app
from flask_cors import CORS

app=create_app()
CORS(app)
@app.route('/')
def index():
    return "Index for Message API"

if __name__=="__main__":
    app.run(port=5555,debug=True)