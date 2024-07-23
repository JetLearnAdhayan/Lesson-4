import cv2

image = cv2.imread("image.png")

cv2.imshow("orignal image", image)

start_point = (0,0)



end_point = (300,250)


thickness = 2

color = (0,255,0)

image1 = cv2.line(image,start_point,end_point,color,thickness)
cv2.imshow("image with line", image1)









cv2.waitKey(0)
cv2.destroyAllWindows()