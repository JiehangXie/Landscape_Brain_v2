from paddlelite.lite import *
import numpy as np
from PIL import Image
from color import get_pseudo_color_map


def normalize(input_img):
    '''数据归一化
        input_img: 图像数据--numpy.ndarray
    '''
    # 对RGB通道进行均值-方差的归一化
    #https://aistudio.baidu.com/aistudio/projectdetail/2283361?channelType=0&channel=0
    img_means = [0.5,0.5,0.5]
    img_stds = [0.5,0.5,0.5]
    input_img[0, 0] = (input_img[0, 0] / 255. - img_means[0]) / img_stds[0]
    input_img[0, 1] = (input_img[0, 1] / 255. - img_means[1]) / img_stds[1]
    input_img[0, 2] = (input_img[0, 2] / 255. - img_means[2]) / img_stds[2]
    
    return input_img

def seg(img_path):
    config = MobileConfig()
    config.set_model_from_file("./bisenetv2_opt.nb")
    predictor = create_paddle_predictor(config)
    
    image = Image.open(img_path)
    origin_size = image.size
    resized_image = image.resize((1024, 1024), Image.BILINEAR)
    input_data = np.array(resized_image).transpose(2, 0, 1).reshape([1, 3, 1024, 1024]).astype('float32')
    resized_image = normalize(input_data)
    
    input_tensor = predictor.get_input(0)
    input_tensor.from_numpy(input_data)
    predictor.run()
    output_tensor = predictor.get_output(0)
    #print(output_tensor.shape())
    
    sc_img = output_tensor.numpy()[0] #单通道label图
    result_img = get_pseudo_color_map(sc_img) #渲染结果图
    result_img = result_img.resize(origin_size)
    #result_img.save('111.png')
    return sc_img,result_img