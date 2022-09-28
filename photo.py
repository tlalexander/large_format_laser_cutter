import cv2
import sys
import numpy as np

SPACING = 50
photo_names = []
y_pos = 0
col_index = 0
while y_pos < 1301:
    photo_names.append([])
    for x_pos in range(0,1201,SPACING):
        photo_names[col_index].append("photos/pic_{:04d}_{:04d}.jpg".format(y_pos, x_pos))
    y_pos+=SPACING
    col_index+=1

def map(x, in_min, in_max, out_min, out_max):
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

def apply_brightness_contrast(input_img, brightness = 255, contrast = 127):
    brightness = map(brightness, 0, 510, -255, 255)
    contrast = map(contrast, 0, 254, -127, 127)

    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            highlight = 255
        else:
            shadow = 0
            highlight = 255 + brightness
        alpha_b = (highlight - shadow)/255
        gamma_b = shadow

        buf = cv2.addWeighted(input_img, alpha_b, input_img, 0, gamma_b)
    else:
        buf = input_img.copy()

    if contrast != 0:
        f = float(131 * (contrast + 127)) / (127 * (131 - contrast))
        alpha_c = f
        gamma_c = 127*(1-f)

        buf = cv2.addWeighted(buf, alpha_c, buf, 0, gamma_c)

    # cv2.putText(buf,'B:{},C:{}'.format(brightness,contrast),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    return buf

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

DIM = 430
orig_height, orig_width,channels = cv2.imread(photo_names[0][0]).shape
img_dtype = cv2.imread(photo_names[0][0]).dtype
crop_height = DIM
crop_width = DIM
rows = len(photo_names[0])
columns = len(photo_names)
horiz_spacing = DIM
vert_spacing = DIM
total_width = rows * horiz_spacing + crop_width
total_height = columns * vert_spacing + crop_height
# output_image = cv2.CreateMat(total_height, total_width, img_dtype)
output_image = np.zeros((total_height, total_width, channels), dtype = img_dtype)
crop_horizontal_offset = -50
crop_vertical_offset = 150
width_crop_start = int(orig_width/2 - crop_width/2 + crop_horizontal_offset)
width_crop_end = int(orig_width/2 + crop_width/2 + crop_horizontal_offset)
height_crop_start = int(orig_height/2-crop_height/2 + crop_vertical_offset)
height_crop_end = int(orig_height/2+crop_height/2 + crop_vertical_offset)

for row_num in range(rows):
    for col_num in range(columns):
        img = cv2.imread(photo_names[col_num][row_num])
        # img = rotate_image(img,-1.8)
        img = rotate_image(img,1.2)
        #img = apply_brightness_contrast(200, 40)
        img = img[height_crop_start:height_crop_end,width_crop_start:width_crop_end]
        col_off_start = (columns-col_num) * vert_spacing
        col_off_end = col_off_start + crop_height
        row_off_start = row_num * horiz_spacing
        row_off_end = row_off_start + crop_width
        output_image[col_off_start:col_off_end,row_off_start:row_off_end] = img

output_image=cv2.resize(output_image,(0,0),fx=0.5,fy=0.5)
cv2.imwrite("output24.jpg", output_image)

# output_image=cv2.resize(output_image,(0,0),fx=0.5,fy=0.5)
# cv2.imshow('final result',output_image)
#
# cv2.waitKey(0)
