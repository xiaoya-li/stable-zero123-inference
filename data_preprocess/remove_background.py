#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# file: data_preprocess/remove_background.py

import os
import logging
import requests
from dataclasses import dataclass
from utils.get_logger import get_info_logger


@dataclass
class RemoveBackGroundConfig:
    clipdrop_url: str = "https://clipdrop-api.co/remove-background/v1"
    clipdrop_api_key: str = "0670f28a91123e0edda01a56cdf45c5cd3e3bc56568c33236d335163b332504a02397fc45520a3c4706e83e8ada1d8ba"
    max_retry: int = 5
    save_output_dir : str = "../outputs"
    input_dir : str = ""


class RemoveBackGround:
    """
    https://clipdrop.co/apis/docs/remove-background
    """
    def __init__(self, config: RemoveBackGroundConfig, logger: logging.basicConfig = None):
        self.config = config
        self.logger = logger if logger is not None else get_info_logger(save_log_file=os.path.join(self.config.save_output_dir, "clipdrop_log"))

    def remove_background_via_clipdrop_api(self, image_w_bk_path: str, save_image_wo_bk_dir: str):
        filetype = image_w_bk_path.split('.')[-1]
        filename = image_w_bk_path.split("/")[-1]
        assert filetype in ["png", "webp", "jpg"]
        response = requests.post(self.config.clipdrop_url,
                          files={
                              'image_file': (
                                  image_w_bk_path, open(image_w_bk_path, 'rb'), f'image/{filetype}'
                              )
                          },
                          headers={'x-api-key': self.config.clipdrop_api_key}
                          )
        if response.ok:
            # {image.replace(filetype, "png")}
            with open(f'{save_image_wo_bk_dir}/{filename}', 'wb') as f:
                f.write(response.content)
            self.logger.info(f">>> [Success] - {image_w_bk_path}")
        else:
            response.raise_for_status()
            self.logger.info(f">>> [Fail] - {image_w_bk_path}")


