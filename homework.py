import cv2

image = cv2.imread("image.png")

cv2.imshow("orignal Image", image)

start_point = (100,100)

end_point = (200,200)

color = (0,255,0)
thickness = 2

image1 = cv2.rectangle(image, start_point,end_point,color,thickness)

# Center coordinates
center_coordinates = (150,80)
#Radius of circle
radius = 50

#blue color in bgr
color = (0,255,0)

#Line thickness of 2 px
thickness = -2

image1 = cv2.circle(image,center_coordinates, radius, color, thickness)
cv2.imshow("image with circle", image1)

cv2.waitKey(0)
cv2.destroyAllWindows