import unitypack
import os
from cv2 import cv2
import numpy
from PIL import Image
import json

while True:
    card_id = input("id: ")
    card = open(f"./static/{card_id}/ui_class_{card_id}.unity3d", "rb")
    bundle = unitypack.load(card)
    for asset in bundle.assets:
        for id, object in asset.objects.items():
            data = object.read()
            if object.type == "Texture2D":
                if "A" in data.name:
                    # data.image.show()
                    alpha = cv2.flip(
                        cv2.cvtColor(numpy.asarray(data.image), cv2.COLOR_RGB2GRAY), 0
                    )
                    cv2.imwrite(f"./static/{card_id}/class_{card_id}_A.png", alpha)
                else:
                    # data.image.show()
                    image = cv2.flip(
                        cv2.cvtColor(
                            numpy.asarray(data.image.convert("RGBA")),
                            cv2.COLOR_RGBA2BGRA,
                        ),
                        0,
                    )
                    cv2.imwrite(f"./static/{card_id}/class_{card_id}_O.png", image)
            if object.type == "TextAsset":
                if "atlas" in data.name:
                    with open(
                        f"./static/{card_id}/class_{card_id}.atlas", "w+"
                    ) as atlas:
                        atlas.write(data.script.replace("\r\n", "\n"))
                elif data.name == f"class_{card_id}":
                    with open(
                        f"./static/{card_id}/class_{card_id}.json", "w+"
                    ) as jfile:
                        jfile.write(data.script)
    card.close()
    b, g, r, a = cv2.split(image)
    outImage = cv2.merge((b, g, r, alpha))
    cv2.imwrite(f"./static/{card_id}/class_{card_id}.png", outImage)
