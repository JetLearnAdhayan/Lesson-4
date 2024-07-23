import cv2

image = cv2.imread("image.png")

cv2.imshow("orignal image", image)

start_point = (5,5)

end_point = (220,255)

color = (0,255,0)
thickness = -2

image = cv2.rectangle(image, start_point,end_point,color,thickness)

cv2.imshow("image with rectangle", image)






cv2.waitKey(0)
cv2.destroyAllWindows()