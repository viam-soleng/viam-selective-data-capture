import asyncio

from viam.components.camera import Camera
from viam.module.module import Module
from viam.resource.registry import Registry, ResourceCreatorRegistration

from color_filter.color_filter import ColorFilterCam

async def main():
    """This function creates and starts a new module, after adding all desired resource models.
    Resource creators must be registered to the resource registry before the module adds the resource model. 
    """
    Registry.register_resource_creator(Camera.SUBTYPE, ColorFilterCam.MODEL, ResourceCreatorRegistration(ColorFilterCam.new_cam))
    module = Module.from_args()

    module.add_model_from_registry(Camera.SUBTYPE, ColorFilterCam.MODEL)
    await module.start()

if __name__ == "__main__":
    asyncio.run(main())