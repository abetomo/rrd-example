import numpy as np
import rerun as rr

from PIL import Image, ImageDraw

rr.init("example")
rr.save("example.rrd")

# delta_time(0.1) * 200 = 20 sec
delta_time = 0.1
for i in range(200):
    t = i * delta_time
    rr.set_time("timestamp", duration=t)

    # The values are quite arbitrary since this is just an example.
    # Velocity is the derivative of position.
    rr.log("motor/position", rr.Scalars(np.sin(t)))
    rr.log("motor/velocity", rr.Scalars(np.cos(t)))

    torque = 5.0 + np.random.normal(0, 0.3)
    rr.log("motor/torque", rr.Scalars(torque))

    if i % 10 == 0:
        image = Image.new("RGB", (320, 320), color=(0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.text((160, 160), f"{t:.1f}s", fill=(255, 255, 255), anchor="mm")
        rr.log("camera/image", rr.Image(np.array(image)))
