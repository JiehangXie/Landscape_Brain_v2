from flask import Flask,request,jsonify,render_template,make_response
from gevent import pywsgi
from flask_cors import *
import database
from PIL import Image
import os
import time
from seg_api import seg
from evaluate import evaluate_img
from location import exifread_infos

app = Flask(__name__,template_folder="./dist",
            static_folder="./dist/assets")
CORS(app, supports_credentials=True)

DOMAIN = "http://lhs.gis.show:5000"
ORIGINAL_IMAGE_SAVE_PATH = './dist/assets/file/Original_Image'
COLOR_IMAGE_SAVE_PATH = './dist/assets/file/Color_Image'

@app.route('/', defaults = {'path': ''}, methods=['GET'])
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

@app.route('/api/v1/',methods=['GET'])
def api_v1():
    data = database.get_data()
    data = make_response(data)  # 设置响应体
    data.status = '200'  # 设置状态码
    data.headers['Access-Control-Allow-Origin'] = "*"  # 设置允许跨域
    data.headers['Access-Control-Allow-Methods'] = 'GET'
    return data

@app.route('/api/upload/v1/',methods=['POST'])
def upload_image():

    Timestamp = int(time.time()*1000) #13位时间戳
    Original_Image_Path = os.path.join(ORIGINAL_IMAGE_SAVE_PATH,'%s.jpg'%(Timestamp))
    Color_Image_Path = os.path.join(COLOR_IMAGE_SAVE_PATH,'%s.png'%(Timestamp))

    Original_Image = request.files.get('file')
    Original_Image = Original_Image.read()
    with open(Original_Image_Path,'wb') as f:
        f.write(Original_Image)

    Pix_result ,Color_Image = seg(Original_Image_Path)
    Color_Image.save(Color_Image_Path)
    Elements,score,advice = evaluate_img(Pix_result)
    building,green,sky = Elements["building"],Elements["green"],Elements["sky"]

    #获取坐标
    location = exifread_infos(Original_Image_Path)
    if location!=False:
        lat,lng = location[0],location[1]
    else:
        lat,lng = 0,0
    
    
    HTTP_Original_Image_Path = Original_Image_Path.replace('./dist/assets/file','%s/assets/file'%DOMAIN)
    HTTP_Color_Image_Path = Color_Image_Path.replace('./dist/assets/file','%s/assets/file'%DOMAIN)

    Save_info = [Timestamp,HTTP_Original_Image_Path,HTTP_Color_Image_Path,lat,lng,Timestamp,building,green,sky,score,advice]
    Save_image = database.write_data(Save_info)
    if Save_image==True:
        print("数据保存成功。")
    else:
        print("数据保存失败。")

    #print(request.files)
    return jsonify(status="Success")


if __name__ == '__main__':
    #server = pywsgi.WSGIServer(('0.0.0.0', 5000), app) #ipv4
    server = pywsgi.WSGIServer(('::', 5000), app) #ipv6
    print('Service Runing……')
    server.serve_forever()