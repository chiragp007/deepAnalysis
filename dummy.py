import mysql.connector
import sys
from PIL import Image
import base64
import io
import PIL.Image
import tensorflow as tf
import cv2
from imageio import imread
import numpy as np
physical_devices = tf.config.experimental.list_physical_devices('GPU')
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)


db = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='chirag',auth_plugin="mysql_native_password")


mycursor=db.cursor()
sql1="select * from image_data"
mycursor.execute(sql1)
data = mycursor.fetchall()
data1=base64.b64decode(data[0][0])
file_like=io.BytesIO(data1)
img=PIL.Image.open(file_like)
# img.show()
db.close()

np_data = np.fromstring(data1,np.uint8)
img1 = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
# print(img1)
# cv2.imshow("test", img1)
# cv2.waitKey(0)

# b64_bytes = data[0][0]
# b64_string = b64_bytes.decode()


# original_image = imread(file_like)
# cv2.imshow("test", original_image)
# cv2.waitKey(0)

# original_image = cv2.imread(io.BytesIO(base64.b64decode(data[0][0]))

img_array = np.fromstring(data1,np.uint8)
original_image = cv2.imdecode(img_array,cv2.COLOR_BGR2RGB)

original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)

cv2.imshow("test", original_image)
cv2.waitKey(0)