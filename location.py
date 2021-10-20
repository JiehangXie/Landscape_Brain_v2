import exifread 
import re

def ex_info(loc):
    result = re.compile(r'\[(.*?), (.*?), (.*?)\]').findall(loc)
    result = eval(result[0][0]) + eval(result[0][1])/60 + eval(result[0][2])/3600
    return result

def exifread_infos(photo):
    lat,lon = 0,0
    f = open(photo,'rb')
    contents = exifread.process_file(f)
    if contents=={}:
        return False
    else:
        for key in contents:
            if key == "GPS GPSLongitude":
                #print("经度 =", contents[key],contents['GPS GPSLatitudeRef'])
                lon = str(contents[key])
                lon = ex_info(lon)

            elif key =="GPS GPSLatitude":
                #print("纬度 =",contents[key],contents['GPS GPSLongitudeRef'])
                lat = str(contents[key])
                lat = ex_info(lat)
        return [lat,lon]