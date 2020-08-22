#!/usr/bin/env python

# Script that creates the layout for a poster to be sent to a fabric designer like my fabric design for printing.
# Right now works only for resolution of 2500 x 4000. Examples found in moviemania.io
# Released under Public Domain by Miguel Martorell

# Version 1.0

# Installation : put the automate_poster_creation.py file in your $HOME/.gimp-2.n/plug-ins.
# On Linux and Mac OSX the file must be executable.
# Documentation : http://www.gimp.org/docs/python/index.html

from gimpfu import *
import os

def automate_poster_creation_from_folder(source_folder_path, destination_folder_path):
  fileSourceDir = source_folder_path # "C:\\Users\hellbinder\\Pictures\\Moviemania to process\\"
  fileDestinationDir = destination_folder_path # "C:\\Users\\hellbinder\\Pictures\\Moviemania Posters\\"
  for file in os.listdir(fileSourceDir):
    if file.endswith(".jpg"):
        source_file_path = os.path.join(fileSourceDir, file)
        destination_file_path = os.path.join(fileDestinationDir, file)
        loadedImage = pdb.gimp_file_load(source_file_path, source_file_path)
        mainLayer = loadedImage.layers[0]
        mainLayerImage = mainLayer.image
        pdb.gimp_layer_scale(mainLayer, 7200, 11520, 0)  # to scale by layer
        backgroundLayer = pdb.gimp_layer_new(
            mainLayerImage, 9900, 14400, 0, "Background", 100, 0)
        pdb.gimp_drawable_fill(backgroundLayer, 0)
        pdb.gimp_image_add_layer(mainLayerImage, backgroundLayer, 1)
        pdb.gimp_image_resize_to_layers(mainLayerImage)
        y = (backgroundLayer.height - mainLayer.height) / 2
        x = (backgroundLayer.width - mainLayer.width) / 2
        mainLayer.set_offsets(x, y)
        pdb.gimp_image_flatten(mainLayerImage)
        pdb.gimp_image_rotate(mainLayerImage, 0)  # -90 degrees
        drawable = pdb.gimp_image_active_drawable(
            mainLayerImage)  # get drawable object
        pdb.file_jpeg_save(mainLayerImage,
                        drawable,
                        destination_file_path,  # "C:\\Users\\hellbinder\\Pictures\\test.jpg",
                        destination_file_path,  # "C:\\Users\\hellbinder\\Pictures\\test.jpg",
                        1, 0, 0, 0, "", 2, 0, 0, 0)
        pdb.gimp_image_delete(loadedImage)
    
register(
    "automate_poster_creation_from_folder",
    "Fabric Designer layout creator for GIMP in folders",
    "Created the fabric designer layout needed from all images in a folder to be able to tranfer into a canvas.",
    "Miguel Martorell",
    "GPL License",
    "2019",
    "<Toolbox>/Tools/Posterize/Posterize Folder",
    "",
    [
        (PF_DIRNAME, "source_folder_path", "Source File Directory", ""),
        (PF_DIRNAME, "destination_folder_path", "Destination File Directory", "")
    ],
    [],
    automate_poster_creation_from_folder)

main()
