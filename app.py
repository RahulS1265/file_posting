from flask import Flask,render_template,request
import requests

app = Flask(__name__)

UPLOAD_URL = 'https://0x0.st'


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    output = None
    
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error='No file part')
        
        file = request.files['file']
        
        if file.filename == '':
            return render_template('index.html', error='No selected file')
        
        response = upload_to_0x0st(file)
        output = response.text if response else 'Error uploading the file'

    return render_template('index.html', output=output)

def upload_to_0x0st(file):
    try:
        response = requests.post(UPLOAD_URL, files={'file': file})
        return response
    except requests.exceptions.RequestException:
        return None 
    

if __name__=="__main__":
     app.run(debug=True)
   