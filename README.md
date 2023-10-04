# VIAM - Selective Image Capture

This repo contains a simple camera component which filters before storing and uploading them into the Viam cloud.
It takes a camera component and vision service running a detection model as input. The camera image is handed over to the vision service and if the vision service returns # detections > 0 it skips the storing/uploading procedure.


## Component Configuration

To be able to use the image filter component, you have to add a camera component (called "camera" in the sample config below) and a vision service which will apply the selection criteria (called "colordetector" in the sample config below). Additionally you store the data and upload it into the cloud, the data management service is required.

The actual image filter component can then be created analogous to the following sample configuration:

```
    {
      "model": "viam-soleng:camera:imagefilter",
      "type": "camera",
      "namespace": "rdk",
      "attributes": {
        "vision_service": "colordetector",
        "actual_cam": "camera"
      },
      "depends_on": [
        "camera",
        "colordetector"
      ],
      "service_configs": [
        {
          "type": "data_manager",
          "attributes": {
            "capture_methods": [
              {
                "disabled": false,
                "method": "ReadImage",
                "additional_params": {
                  "mime_type": "image/jpeg"
                },
                "capture_frequency_hz": 1
              }
            ]
          }
        }
      ],
      "name": "imagefilter"
    }
```


