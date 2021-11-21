#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org, https://github.com/cloudedbats
# Copyright (c) 2021-present Arnold Andreasson
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

import os
import uvicorn
import rpi_cam

if __name__ == "__main__":

    # CloudedBats camera manager.
    picam_manager = rpi_cam.PicamManager()
    
    # # Launch REST API.
    rpi_cam.api_app.rpicam_manager = picam_manager
    uvicorn.run(
        "rpi_cam.api_app:app",
        loop="asyncio",
        host= os.getenv("PICAM_HOST", "0.0.0.0"),
        port=int(os.getenv("PICAM_PORT", "8082")),
        log_level=os.getenv("PICAM_LOG_LEVEL", "info"),
    )
