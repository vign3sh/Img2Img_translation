import os
from PIL import Image

# storing the list of images inside the Dayton dataset directory
path_to_orig_data = "./dayton/"
images_list_orig = os.listdir(path_to_orig_data)
print(images_list_orig[:6])
print("Total Images before merge:", len(images_list_orig))


# in this cell we will be generating aerial-street view image pair
# looping all the images
counter = 1
for index in range(0, len(images_list_orig), 2):
    # getting name of images
    over_image_name = images_list_orig[index]
    
    # check if the image name has 'overhead' in it
    if 'overhead' in over_image_name: 
        street_image_name = over_image_name.replace("overhead", "streetview")
    else:
         street_image_name = over_image_name
         over_image_name= over_image_name.replace("streetview", "overhead")   
   
    print('street view image',street_image_name)
    print('over view image',over_image_name)
    print('counter',counter)
    print('-----------------------------')

    # defining path to images
    over_image_path = path_to_orig_data + over_image_name
    street_image_path = path_to_orig_data + street_image_name

    # loading the images
    over_image = Image.open(over_image_path)
    street_image = Image.open(street_image_path)

    # resizing both the images from 354 x 354 to 256 x 256
    over_image = over_image.resize((256, 256))
    street_image = street_image.resize((256, 256))

    # creating new image object
    result_image = Image.new(mode="RGB", size=(2*256, 256))

    # pasting aerial image and then the street image
    result_image.paste(over_image, (0, 0))
    result_image.paste(street_image, (256, 0))

    result_image.save("./new_agumented/augmented_data" + str(counter) + ".jpg", "JPEG")
    counter += 1
