#!/usr/bin/env python

from argparse import ArgumentParser
import os
import cv2
import apriltag

################################################################################


def apriltag_image(input_images=['/home/neumann483/Documents/Scripts/aprilTags/tt.png'],
                   output_images=False,
                   display_images=True,
                   detection_window_name='AprilTag',
                  ):

    '''
    Detect AprilTags from static images.

    Args:   input_images [list(str)]: List of images to run detection algorithm on
            output_images [bool]: Boolean flag to save/not images annotated with detections
            display_images [bool]: Boolean flag to display/not images annotated with detections
            detection_window_name [str]: Title of displayed (output) tag detection window
    '''
    cv2.namedWindow(detection_window_name, cv2.WINDOW_NORMAL)
    parser = ArgumentParser(description='Detect AprilTags from static images.')
    apriltag.add_arguments(parser)
    options = parser.parse_args()

    '''
    Set up a reasonable search path for the apriltag DLL.
    Either install the DLL in the appropriate system-wide
    location, or specify your own search paths as needed.
    '''

    detector = apriltag.Detector(options, searchpath=apriltag._get_dll_path())

    for image in input_images:

        img = cv2.imread(image)

        print('Reading {}...\n'.format(os.path.split(image)[1]))

        result, overlay = apriltag.detect_tags(img,
                                               detector,
                                               camera_params=(616.45304578, 617.18322183, 958.38189862, 591.28276771),
                                               tag_size=0.0762,
                                               vizualization=2,
                                               verbose=3,
                                               annotation=True
                                              )

        if output_images:
            output_path = '../media/output/'+str(os.path.split(image)[1])
            output_path = output_path.replace(str(os.path.splitext(image)[1]), '.png')
            cv2.imwrite(output_path, overlay)

        if display_images:
            cv2.imshow(detection_window_name, overlay)
            while cv2.waitKey(5) < 0:   # Press any key to load subsequent image
                pass

################################################################################

if __name__ == '__main__':
    apriltag_image()
