import cv2

image = cv2.imread("image.png")

cv2.imshow("orignal image", image)

position = (150,150)
font = cv2.FONT_ITALIC
fontScale = 2
color = (0,255,0)
thickness = 2

image = cv2.putText(image, "Hi Hello", position,font,fontScale,color,thickness)
cv2.imshow("image with text", image)

cv2.waitKey(0)
cv2.destroyAllWindows()