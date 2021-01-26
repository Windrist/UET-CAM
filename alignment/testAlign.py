# from picamera.array import PiRGBArray
# from picamera import PiCamera
from matplotlib import pyplot as plt 
import cv2
import numpy as np
import pickle
import glob
import time
import serial
import serial.tools.list_ports

drawing = False 
rec = []

def draw_rec_with_fix_size(event, x, y, flags, param):
    global drawing, rec
    w = 12; h = 25
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        rec = [(x, y),(x+w, y+h)]
    elif event == cv2.EVENT_LBUTTONUP:  
        drawing = False
    
def get_mask_with_fix_size(img_path):
    newpath = "cropped/"+img_path
    global rec
    img = cv2.imread(img_path)
    img = cv2.resize(img, (960, 1280))
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rec_with_fix_size)

    while(True):
        if len(rec) == 2:
            roi = img[rec[0][1]:rec[1][1], rec[0][0]:rec[1][0]]
            cv2.rectangle(img, rec[0], rec[1], (0,255,255), 2)
            cv2.imwrite(newpath,roi)
            rec = []

        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break

def get_mask_with_all_imgs(dir, ext=['png', 'jpg']):
    all_img_paths = []
    for i in glob.glob("{}/*".format(dir)):
        if i.split(".")[-1] in ext:
            all_img_paths.append(i)

    for img_path in all_img_paths:
        get_mask_with_fix_size(img_path)

def calculate_mean_image(dir, ext=['png', 'jpg']):
    all_img_paths = []
    for i in glob.glob("{}/*".format(dir)):
        if i.split(".")[-1] in ext:
            all_img_paths.append(i)

    for img_path in all_img_paths:
        img = cv2.imread(img_path)
        size = img.shape
        mean = np.sum(img)/(size[0]*size[1])
        print(mean)

def draw_rectange(event, x, y, flags, param):
    global drawing, rec
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        rec = [(x,y)]
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        rec.append((x,y))

def get_mask(img_path):
    global rec

    img = cv2.imread(img_path)
    img = cv2.resize(img, (640,480))
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectange)

    while(True):
        if len(rec) == 2:
            cv2.rectangle(img, rec[0], rec[1], (0,255,0), 2)

        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break
    cv2.destroyAllWindows()
    roi = img[rec[0][1]:rec[1][1], rec[0][0]:rec[1][0]]
    # cv2.imshow("", roi)
    # cv2.waitKey(0)
    pickle.dump(rec, open("coords.txt", 'wb'))
    return roi

def show_image_with_fixed_coords(dir, ext=['png', 'jpg']):
    all_img_paths = []
    for i in glob.glob("{}/*".format(dir)):
        if i.split(".")[-1] in ext:
            all_img_paths.append(i)
    # print(all_img_paths)
    rec = pickle.load(open('coords.txt', 'rb'))
    for img_path in all_img_paths:
        img = cv2.imread(img_path)
        cv2.rectangle(img, rec[0], rec[1], (0,255,0), 2)
        cv2.imshow("", img)
        cv2.waitKey(0)

def calculate_histogram(img, coords="coords.txt"):
    rec = pickle.load(open(coords, 'rb'))
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    roi = img[rec[0][1]:rec[1][1], rec[0][0]:rec[1][0]]
    hist = cv2.calcHist(roi, [0], None, [256], [0, 256])
    # show the plotting graph of an image 
    plt.plot(hist) 
    plt.show()

def show_histogram_all_images(dir, coords="coords.txt", ext=['png', 'jpg']):
    all_img_paths = []
    for i in glob.glob("{}/*".format(dir)):
        if i.split(".")[-1] in ext:
            all_img_paths.append(i)

    for img_path in all_img_paths:
        img = cv2.imread(img_path)
        calculate_histogram(img, coords)

def compute_mean_value(img, coords="coords.txt"):
    rec = pickle.load(open(coords, 'rb'))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    roi = img[rec[0][1]:rec[1][1], rec[0][0]:rec[1][0]]
    size = roi.shape
    mean = np.sum(roi)/(size[0]*size[1])
    # print(mean)
    return mean

def compute_mean_all_images(dir, coords="coords.txt", ext=['png', 'jpg']):
    all_img_paths = []
    for i in glob.glob("{}/*".format(dir)):
        if i.split(".")[-1] in ext:
            all_img_paths.append(i)
    
    print(all_img_paths)
    
    for img_path in all_img_paths:
        img = cv2.imread(img_path)
        mean = compute_mean_value(img, coords)
        print(mean)
    
def get_mean_corrected(ok_dir, coords="coords.txt", ext=['png', 'jpg']):
    all_img_paths = []
    for i in glob.glob("{}/*".format(ok_dir)):
        if i.split(".")[-1] in ext:
            all_img_paths.append(i)
    # print(all_img_paths)
    average = 0
    for img_path in all_img_paths:
        img = cv2.imread(img_path)
        mean = compute_mean_value(img, coords)
        average += mean
    average /= len(all_img_paths)
    # print(average)
    pickle.dump(average, open("value.txt", 'wb'))

def get_variance(dir, coords="coords.txt", value="value.txt", ext=['png', 'jpg']):
    all_img_paths = []
    for i in glob.glob("{}/*".format(ok_dir)):
        if i.split(".")[-1] in ext:
            all_img_paths.append(i)
    
    var = 0
    expect = pickle.load(open('value.txt', 'rb'))
    for img_path in all_img_paths:
        img = cv2.imread(img_path)
        mean = compute_mean_value(img, coords)
        var += (mean - expect)^2
    
    var = sqrt(var/(len(all_img_paths)-1))
    print(var)
    pickle.dump(var, open("variance.txt", 'wb'))

def is_ok(img, coords="coords.txt", correct='value.txt'):
    value =  pickle.load(open(correct, 'rb'))
    variance = pickle.load(open("variance.txt", 'rb'))
    input_mean = compute_mean_value(img, coords)
    # Confidence interval 90%
    return abs(value-input_mean) < 1.65*variance

def test_with_images(dir, ext=['png', 'jpg'], coords="coords.txt", correct='value.txt'):
    all_img_paths = []
    for i in glob.glob("{}/*".format(dir)):
        if i.split(".")[-1] in ext:
            all_img_paths.append(i)
    
    for img_path in all_img_paths:
        img = cv2.imread(img_path)
        print(is_ok(img))
        cv2.imshow("", img)
        cv2.waitKey(0)

def get_serial_port():
    ports = serial.tools.list_ports.comports()
    for i in ports:
        port = str(i).split(' ')[0]
        # print(port)
        if port == "/dev/ttyACM0" or port == "/dev/ttyACM1" or port == "/dev/ttyUSB0":   
            return port

def receive_from_mega(ser):
    if ser.in_waiting > 0:
        cmd = ser.readline().decode('utf-8').rstrip()
        print(cmd)
        return cmd 

if __name__ == "__main__":
    ### WARNING: Get data ###
    # get_mask('images/ok/0.png')
    # get_mean_corrected('images/ok')

    # get_mask_with_fix_size('cam/ok/7.jpg')
    # get_mask_with_all_imgs('cam/ok')
    # get_mask_with_all_imgs('cam/notok')

    ### Visualize ###
    # show_image_with_fixed_coords('images/notok')
    # show_image_with_fixed_coords('images/ok')
    
    # show_histogram_all_images('images/ok')
    # show_histogram_all_images('images/notok')
    
    ### Evaluate ###
    # compute_mean_all_images('images/ok')
    # calculate_mean_image("cropped/cam/notok")
    
    ### Testing ###
    # test_with_images('images/ok')

    ### Main ###
    # # Serial configuration
    # port = get_serial_port()
    # print(port)
    # ser = serial.Serial(port, 9600, timeout=0.1)
    # ser.flush()

    # # Camera Pi configuration
    # camera = PiCamera()
    # camera.resolution = (640, 480)
    # camera.framerate = 60
    # # camera.rotation = 180
    # rawCapture = PiRGBArray(camera, size=camera.resolution)
    
    # time.sleep(0.1)
    
    # for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    #     image = frame.array
    #     cmd = receive_from_mega(ser)
    #     if cmd == "c":
    #         if is_ok(image):
    #             ser.write('1'.encode('utf-8'))
    #         else:
    #             ser.write('0'.encode('utf-8'))
    #     elif cmd == "e" or cv2.waitKey(1) & 0xFF == ord('q'): # End task
    #         break