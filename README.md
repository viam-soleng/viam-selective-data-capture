# viam-data-filter
Filter data before recording and uploading to the cloud


Source: https://github.com/viam-labs/modular-filter-examples/blob/main/pycolorfilter/run.sh
Internal example: https://docs.google.com/document/d/1TXEMsY02D8Pxg0frxP6IdxmBEuVXMG8Dc1RRjMSPSuw/edit


## Component Config

{
      "attributes": {
        "vision_service": "my_color_detector",
        "actual_cam": "actualcam"
      },
      "depends_on": [
        "actualcam",
        "my_color_detector"
      ],
      "model": "example:camera:colorfilter",
      "name": "colorfiltercam",
      "service_configs": [
        {
          "type": "data_manager",
          "attributes": {
            "capture_methods": [
              {
                "capture_frequency_hz": 1,
                "method": "ReadImage",
                "additional_params": {
                  "mime_type": "image/jpeg"
                }
              }
            ]
          }
        }
      ],
      "type": "camera"
    }



## Install Development Branch Python SDK

```
pip install git+https://github.com/viamrobotics/viam-python-sdk@rc-0.5.2
```

