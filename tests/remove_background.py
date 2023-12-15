#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# file: tests/remove_background.py

import os
import requests

CLIPDROP_API_KEY="0670f28a91123e0edda01a56cdf45c5cd3e3bc56568c33236d335163b332504a02397fc45520a3c4706e83e8ada1d8ba"

def test_request(dir_list):
    path = os.getcwd()
    for image in dir_list:
        print('.', image)
        if os.path.isfile(f'{path}\output\{image}'):
            print(f'ERROR: {image} File already exists.')
        else:
            filetype = image.split('.')[-1]

            r = requests.post('https://clipdrop-api.co/remove-background/v1',
                              files={
                                  'image_file': (
                                      image, open(image, 'rb'), f'image/{filetype}'
                                  )
                              },
                              headers={'x-api-key': CLIPDROP_API_KEY}
                              )
            if r.ok:
                # {image.replace(filetype, "png")}
                with open(f'{path}/demo.png', 'wb') as f:
                    f.write(r.content)
                print('+', image)
            else:
                r.raise_for_status()
                print('ERROR:', image)



if __name__ == "__main__":
    image_file_object = ["/root/autodl-tmp/stable-zero123-inference/load/images_w_background/pm.png"]
    test_request(image_file_object)
