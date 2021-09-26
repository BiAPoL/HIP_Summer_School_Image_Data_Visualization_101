# To make this script run in Fiji, please activate the clij, # clij2 and clij2-assistant update sites in your Fiji. 
# Read more: 
# https://clij.github.io/assistant
# 
# To make this script run in cpython, install pyclesperanto_prototype:
# pip install pyclesperanto_prototype
# Read more: 
# https://clesperanto.net
# 
# Generator (J) version: 0.6.0.1
# 
import pyclesperanto_prototype as cle

image_1 = cle.imread("C:/structure/data/000200.raw.tif")
cle.imshow(image_1)

# Copy
image_2 = cle.create_like(image_1)
cle.copy(image_1, image_2)

# show result
cle.imshow(image_2, "CLIJ2 Image of 000200.raw.tif", False, 97.34375, 214.921875)

# Make Isotropic
image_3 = cle.create([266, 532, 220], cle.Float)
original_voxel_size_x = 0.5200003
original_voxel_size_y = 0.5200003
original_voxel_size_z = 1.981982
new_voxel_size = 1.0
cle.make_isotropic(image_2, image_3, original_voxel_size_x, original_voxel_size_y, original_voxel_size_z, new_voxel_size)

# show result
cle.imshow(image_3, "Isotropic CLIJ2 Image of 000200.raw.tif", False, 97.89755249023438, 234.90142822265625)

# Cylinder Transform
image_4 = cle.create([360, 532, 172], cle.Float)
number_of_angles = 360
delta_angle_in_degrees = 1.0
relative_center_x = 0.5
relative_center_z = 0.5
cle.cylinder_transform(image_3, image_4, number_of_angles, delta_angle_in_degrees, relative_center_x, relative_center_z)

# show result
cle.imshow(image_4, "Cylinder transformed Isotropic CLIJ2 Image of 000200.raw.tif", False, 97.57662963867188, 238.6977081298828)

# Maximum Z Projection
image_5 = cle.create([360, 532], cle.Float)
cle.maximum_z_projection(image_4, image_5)

# show result
cle.imshow(image_5, "Maximum Z Projection of Cylinder transformed Isotropic CLIJ2 Image of 000200.raw.tif", False, 99.50537109375, 278.56732177734375)

