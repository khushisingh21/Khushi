import flask

app = Flask(__name__)
@app.route('/',methods=['GET'])
def home():
    return "TIU is the best university"

if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)