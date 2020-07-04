from flask import Flask, render_template, request
import json,logging
from SentimentClassifier import Sentiment
app = Flask(__name__)
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')
@app.route("/predict", methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            x = str(request.form['Sentence'])
            prediction=Sentiment(x).process()
            return render_template('index.html',Prediction="Sentiment: {}".format(prediction))
        else:
            return render_template('index.html')
    except:
        x=""
        prediction="Please try another sentence, I am in learning phase."
        return(prediction)
    finally:
        f=open("./ModelOutput.txt","a+",encoding="utf-8")
        f.write(str(json.dumps({"InputSentence":x,"prediction":prediction}))+"\n")
        f.close()
logging.basicConfig(filename='API.log',level=logging.DEBUG)
if __name__=="__main__":
    app.run(debug=True)

