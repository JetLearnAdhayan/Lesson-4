import cv2

image = cv2.imread("image.png")

cv2.imshow("orignal image", image)

# Center coordinates
center_coordinates = (50,50)
#Radius of circle
radius = 20

#blue color in bgr
color = (0,255,0)

#Line thickness of 2 px
thickness = 2

image = cv2.circle(image,center_coordinates, radius, color, thickness)
cv2.imshow("image with circle", image)










cv2.waitKey(0)
cv2.destroyAllWindows()