
#Search and Rescue Task

#importing cv2 and numpy modules for usage
import cv2 as cv
import numpy as np


#Initialising lists to store the required data
Hb_Hg=[]
Pb_Pg=[]
priority_order=[]
image_by_ratio=[]


#initialising the BGR code for blue and red colours respectively 
b_bgr=np.array([255,0,0])
r_bgr=np.array([0,0,255])


#Storing the path to a variable 
path = "Enter the exact path of the input file"

#reading the input image file to be used for the task and processing it
img = cv.imread(cv.samples.findFile(path))

#showing the image input
cv.imshow("Input Image",img)

#using the wait Key to hold the image on the screen
print("The input image will be flashed up on the screen for your reference, press \'e\' to exit")
k = cv.waitKey(0) #0 refers to waiting infinitely
if k == ord('e'):
    cv.destroyAllWindows() #quiting from the image shown

#making a copy of the image
copy2 = img.copy()
final_img = img.copy()

#the image above is in Blue-green-red(BGR) format and now we need to convert it into Hue-Saturation-Value (HSV) format
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)

#List allocations to store the data
bur_red=[]
bur_blue=[]
un_red=[]
un_blue=[]


#Identification of houses
def triangles(img, lst, color):
    
    #Converting image to binary
    bin=cv.inRange(img, color, color)

    #Finding contours in the binary image
    contours, _= cv.findContours(bin, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    #Procedding with the loop to identify all the present houses
    for i in contours:
        accuracy=0.25*cv.arcLength(i, True)
        vertices=cv.approxPolyDP(i, accuracy, True)

        #Setting conditions for the detection of a triangle with an area greater than 500 pixels
        if len(vertices)==3 and cv.contourArea(vertices)>500:
            lst.append(vertices)



def mask_unburnt():
    #Masking the unburnt area via the same concept used above
    lower=np.array([30,30,30])
    upper=np.array([90,255,250])
    bin = cv.inRange(hsv, lower, upper)

    #Finding the contours 
    contours, _ = cv.findContours(bin, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    #Masking the unburnt area
    cv.drawContours(copy2, contours, -1, (230, 230, 50), -1)
    cv.drawContours(final_img, contours, -1, (230, 230, 50), -1)

    #identification of houses in the unmasked area
    triangles(copy2, bur_red, r_bgr)
    triangles(copy2, bur_blue, b_bgr)




def mask_burnt():
    #for masking, we need to select the color range in HSV for detection of burnt area
    lower=np.array([0,20,0])
    upper=np.array([30,255,250])

    #Converting the image into binary form
    bin = cv.inRange(hsv, lower, upper)

    #Finding contours in the binary image
    contours, _ = cv.findContours(bin, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    contour_img = np.zeros_like(bin)

    #Masking the burnt area for detection
    cv.drawContours(final_img, contours, -1, (0, 255, 255), -1)

    #identification of houses in the un masked area
    triangles(final_img, un_red, r_bgr)
    triangles(final_img, un_blue, b_bgr)

    #also masking the unburnt area
    mask_unburnt()


 #Constructing houses on the image to be given as output
def const_house():
    for i in bur_red:
        cv.drawContours(final_img, [i], 0, (0, 0 ,255), -1)
    for i in un_red:
        cv.drawContours(final_img, [i], 0, (0, 0 ,255), -1)
    for i in bur_blue:
        cv.drawContours(final_img, [i], 0, (255, 0 ,0), -1)
    for i in un_blue:
        cv.drawContours(final_img, [i], 0, (255, 0 ,0), -1)


mask_burnt()
const_house()
 

#Finalising the final output
total_houses=[len(bur_red)+len(bur_blue),len(un_red)+len(un_blue)] #these are in the order [burnt,unburnt]

priority=[len(bur_red)+2*len(bur_blue),len(un_red)+2*len(un_blue)] #these are in the order [burnt,unburnt]

ratio=total_houses[0]/total_houses[1]


#Storing the output
Hb_Hg.append(total_houses)
Pb_Pg.append(priority)
priority_order.append(ratio)
image_by_ratio.append([path,ratio])

#Printing the final image
cv.imshow("Output", final_img)
cv.waitKey(0)
k = cv.waitKey()
if k == "e":
    cv.destroyAllWindows


#Printing the final output
print("Number of houses on the burnt grass and the number of houses on the green:",Hb_Hg)
print("The total priority of houses on the burnt grass and the total priority of houses on the green grass:",Pb_Pg)
print("Rescue ratio of priority:",priority_order)

#Thanks for visiting


   












    







