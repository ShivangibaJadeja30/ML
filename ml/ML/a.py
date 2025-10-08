import cv2
img = cv2.imread(r"D:\ML\img.jpg")  # or use double backslashes or forward slashes
img=cv2.resize(img,(1280,720))
i = cv2.imread(r"D:\ML\img.jpg",0)  # or use double backslashes or forward slashes
i=cv2.resize(i,(1280,720))
cv2.imshow("res", img)
cv2.imshow("og", i)
cv2.waitKey(0)
cv2.destroyAllWindows()