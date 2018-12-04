import sys
import os
from PIL import Image

path = "/Users/chrisluginbuhl/Dropbox/Digital Futures/Thesis/GAN Outputs/CycleGAN Nov 29/"
imgSize = 256

input_file = os.listdir(path)
input_file.remove('.DS_Store')
filenames = []
for filename in input_file:
    if filename.endswith( ('.jpeg', '.png', '.gif') ): # whatever file types you're using...
        filenames.append(filename)
filenames.sort()
numFiles = len(filenames)
if numFiles % 8 != 0:
    print("There are %s files in this folder. It should be a multiple of 8, so skipping the last %s files." % (numFiles, numFiles % 8))

#os.makedirs(path + subfolder, exist_ok=True)

# def display_results(image_path):
#     im=Image.open(image_path)
#     for x,y,w,h in faces:
#         f, e = os.path.splitext(path + subfolder + item)
#         sub_img=image[y-10:y+h+10,x-10:x+w+10]
#         cv2.rectangle(image,(x,y),(x+w,y+h),(255, 255,0),2)
#
# 	cv2.imshow("Faces Found", image)
# 	if (cv2.waitKey(0) & 0xFF == ord('q')) or (cv2.waitKey(0) & 0xFF == ord('Q')):
# 		cv2.destroyAllWindows()

for i in range(0, numFiles // 8):
    new_image = Image.new('RGB', (imgSize * 2, imgSize * 4), color = 'black')
    for j in range(0, 8):
        print("i: %s, j: %s, file: %s" % (i, j, filenames[i * 8 + j]))
        # if item == '.DS_Store':
        #     continue
        # if os.path.isfile(path + item):
        #     detect_faces(path + item)
        im=Image.open(path + filenames[i * 8 + j])
        x = imgSize * (j % 2)
        y = imgSize * (j // 2)
        new_image.paste(im, (x, y, x + imgSize, y + imgSize)) #make a grid of images 2x4
        # d = ImageDraw.Draw(img)
        # d.text((10,10), "Hello World", fill=(255,255,0))
    new_image.save(path + "new/" + "epoch_" + str(i) + ".jpg")

# for item in dirs:
#         if item == '.DS_Store':
#             continue
#         if os.path.isfile(path + item):
#             make_image()
#             display_results(path + item)
