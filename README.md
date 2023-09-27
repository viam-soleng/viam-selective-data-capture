# VIAM - Selective Image Capture

This repo contains a simple camera component which filters before storing and uploading them into the Viam cloud.
It takes a camera component and vision service running a detection model as input. The camera image is handed over to the vision service and if the vision service returns # detections > 0 it skips the storing/uploading procedure.


