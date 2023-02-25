from flask import Flask, request, render_template
from dxfviewer import DXFViewer
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join("C:\\Users\\Cameron.Stewart\\Documents\\GitHub\\CADcheck\\", filename))
        viewer = DXFViewer(file)
        return render_template('viewer.html', dxf=viewer.data)
    return '''
        <form method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''
@app.route('/test2', methods=['GET'])
def test2():
    return "yay"
        

@app.route('/test', methods=['GET'])
def test():
    with open(os.path("C:\\Users\\Cameron.Stewart\\Documents\\GitHub\\CADcheck\\non_conformance_gap.dxf"), 'r') as f:
        viewer = DXFViewer(f)

    return render_template('viewer.html', dxf=viewer.data)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(os.path.join("C:\\Users\\Cameron.Stewart\\Documents\\GitHub\\CADcheck\\", filename))
    return 'file uploaded successfully'


if __name__ == '__main__':
    app.run()
