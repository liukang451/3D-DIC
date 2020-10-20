
# importing the module 
import cv2 

import numpy as np

import dlt

clicked_coordinates = []
three_d_coordinates = []
dlt_parameters = []

# function to display the coordinates of 
# of the points clicked on the image 
def click_event(event, x, y, flags, params): 

    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 

        # displaying the coordinates 
        # on the Shell 
        print(x, ' ', y)
        color = (0, 255, 0) 
        #cv2.line(img, (147, 50), (150,50), color, 2)
        co_ordinates = (x,y)
        if len(clicked_coordinates) == 0:
            pass
        else:
            cv2.line(img, clicked_coordinates[::-1][0], co_ordinates, color, 2)
        clicked_coordinates.append(co_ordinates)      
        cv2.circle(img, co_ordinates, 2, color)
        # displaying the coordinates 
        # on the image window 
        cv2.imshow('image', img) 

    # checking for right mouse clicks     
    if event==cv2.EVENT_LBUTTONDBLCLK: 
        mask = np.zeros(img.shape, dtype=np.uint8)
        # fill the ROI so it doesn't get wiped out when the mask is applied
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,)*channel_count
        cv2.fillPoly(mask, np.int32([clicked_coordinates]), ignore_mask_color)
        # from Masterfool: use cv2.fillConvexPoly if you know it's convex
       
        # apply the mask
        masked_image = cv2.bitwise_and(img, mask)
        cv2.destroyWindow('image')
        cv2.imshow('image1', masked_image)
        # save the result
       #$ cv2.imwrite('image_masked.png', masked_image)
        print(x, ' ', y) 
        
def input_3d_coordinates():
    print("Please Enter 3D coordinates : ")
    for i in range(0, len(clicked_coordinates)):
        co_ordinates = list(map(float, input().split()))
        three_d_coordinates.append(co_ordinates)

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)

# driver function 
if __name__=="__main__": 
    #get the image 
    image = input("Enter the name of the image:  ")
    
    try:
        # reading the image 
        img = cv2.imread(image, 1) 
        img = ResizeWithAspectRatio(img, width=720)
    
        # displaying the image 
        cv2.imshow('image', img) 
    
        # setting mouse hadler for the image 
        # and calling the click_event() function 
        cv2.setMouseCallback('image', click_event) 
    
        # wait for a key to be pressed to exit 
        cv2.waitKey(0) 
    
        # close the window 
        cv2.destroyAllWindows() 
        
        #input 3d Co-ordinates
        input_3d_coordinates()
        
        #claculate DLT Parameters
        dlt.DLT(three_d_coordinates, clicked_coordinates)
    except Exception as e:
        print(e)
    
        print("Please Enter Correct Image")
    

