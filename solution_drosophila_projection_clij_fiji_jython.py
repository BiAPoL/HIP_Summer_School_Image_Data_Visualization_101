# To make this script run in Fiji, please activate 
# the clij and clij2 update sites in your Fiji 
# installation. Read more: https://clij.github.io

# Generator version: 2.5.1.1

from ij import IJ
from ij import WindowManager
from net.haesleinhuepf.clij2 import CLIJ2

# Init GPU
clij2 = CLIJ2.getInstance()

# Load image from disc 
imp = IJ.openImage("C:/structure/data/000200.raw.tif")
# Push 000200.raw.tif to GPU memory
image_1 = clij2.push(imp);

# Copy
image_2 = clij2.create(image_1)
clij2.copy(image_1, image_2)
image_1.close()

result = clij2.pull(image_2)
result.setDisplayRange(97.96875, 106.94921875)
result.show()

# Make Isotropic
image_3 = clij2.create([266, 532, 220], clij2.Float)
original_voxel_size_x = 0.5200003
original_voxel_size_y = 0.5200003
original_voxel_size_z = 1.981982
new_voxel_size = 1.0
clij2.makeIsotropic(image_2, image_3, original_voxel_size_x, original_voxel_size_y, original_voxel_size_z, new_voxel_size)
image_2.close()

result = clij2.pull(image_3)
result.setDisplayRange(74.56982421875, 79.773681640625)
result.show()

# Cylinder Transform
image_4 = clij2.create([360, 532, 172], clij2.Float)
number_of_angles = 360
delta_angle_in_degrees = 1.0
relative_center_x = 0.5
relative_center_z = 0.5
clij2.cylinderTransform(image_3, image_4, number_of_angles, delta_angle_in_degrees, relative_center_x, relative_center_z)
image_3.close()

result = clij2.pull(image_4)
result.setDisplayRange(99.0234375, 170.93284606933594)
result.show()

# Maximum Z Projection
image_5 = clij2.create([360, 532], clij2.Float)
clij2.maximumZProjection(image_4, image_5)
image_4.close()

result = clij2.pull(image_5)
result.setDisplayRange(99.50537109375, 278.56732177734375)
result.show()
image_5.close()

