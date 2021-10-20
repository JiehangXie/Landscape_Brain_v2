import numpy as np
from collections import Counter

def evaluate_img(img_np):
    img_np_flatten = img_np.flatten()
    Pixel_all = len(img_np_flatten) #像素总数量
    Pixel_Count = dict(Counter(img_np_flatten))
    Elements = {"building":0,"green":0,"sky":0}
    for p in range(0,18):
        try:
            if p==2 or p==3:Elements["building"] += round(Pixel_Count[p]/Pixel_all,3)
            if p==8 or p==9:Elements["green"] += round(Pixel_Count[p]/Pixel_all,3)
            if p==10:Elements["sky"] += round(Pixel_Count[p]/Pixel_all,3)
        except:
            pass
    
    #计算得分
    score = round(Elements["building"]*(-2.5) + Elements["green"]*5.69 + Elements["sky"]*3.42,2)
    #建议评价
    advice = 0 #正常
    advice_list = []
    if Elements["green"] <= 0.2: advice_list.append(1) 
    if Elements["sky"] <= 0.15: advice_list.append(2) 
    if Elements["building"] >= 0.6:advice_list.append(3)

    if 1 in advice_list:advice = 1 #植物不够
    if 2 in advice_list:advice = 2 #采光不足
    if 3 in advice_list:advice = 3 #建筑密度过高
    if 1 in advice_list and 2 in advice_list:advice = 4 #植物不足采光不足
    if 1 in advice_list and 3 in advice_list:advice = 5 #植物不足建筑密度过高
    if 2 in advice_list and 3 in advice_list:advice = 6 #采光不足建筑密度过高
    if 1 in advice_list and 2 in advice_list and 3 in advice_list:advice = 6 #植物不足采光不足建筑密度过高

    return Elements,score,advice