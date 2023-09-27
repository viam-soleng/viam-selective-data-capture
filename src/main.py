import asyncio

from viam.components.camera import Camera
from viam.module.module import Module
from viam.resource.registry import Registry, ResourceCreatorRegistration

from image_filter.image_filter import ImageFilterCam

async def main():
    """This function creates and starts a new module, after adding all desired resource models.
    Resource creators must be registered to the resource registry before the module adds the resource model. 
    """
    Registry.register_resource_creator(Camera.SUBTYPE, ImageFilterCam.MODEL, ResourceCreatorRegistration(ImageFilterCam.new_cam))
    module = Module.from_args()

    module.add_model_from_registry(Camera.SUBTYPE, ImageFilterCam.MODEL)
    await module.start()

if __name__ == "__main__":
    asyncio.run(main())