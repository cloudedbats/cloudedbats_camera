#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Project: http://cloudedbats.org, https://github.com/cloudedbats
# Copyright (c) 2021-present Arnold Andreasson
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

import time
import datetime
import asyncio
import fastapi
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional
import websockets.exceptions

# CloudedBats.
import rpi_cam

app = fastapi.FastAPI(
    title="CloudedBats Camera",
    description="CloudedBats Camera - a part of CloudedBats.org.",
    version=rpi_cam.__version__,
)

app.mount("/static", StaticFiles(directory="rpi_cam/static"), name="static")
templates = Jinja2Templates(directory="rpi_cam/templates")

# CloudedBats.
picam_manager = None

@app.on_event("startup")
async def startup_event():
    """ """
    # try:
    #     global picam_manager
    #     await picam_manager.startup()
    #     # Logging debug.
    #     picam_manager.picam_logging.debug(message="API called: startup.")
    # except Exception as e:
    #     # Logging error.
    #     message = "Called: startup: " + str(e)
    #     picam_manager.picam_logging.error(message, short_message=message)


@app.on_event("shutdown")
async def shutdown_event():
    """ """
    # try:
    #     global picam_manager
    #     # Logging debug.
    #     picam_manager.picam_logging.debug(message="API called: startup.")
    #     await picam_manager.shutdown()
    # except Exception as e:
    #     # Logging error.
    #     message = "Called: shutdown: " + str(e)
    #     picam_manager.picam_logging.error(message, short_message=message)


@app.get("/")
async def webpage(request: fastapi.Request):
    try:
        global picam_manager
        # # Logging debug.
        # picam_manager.picam_logging.debug(message="API called: webpage.")
        # status_dict = await picam_manager.get_status_dict()
        # location_status = picam_manager.picam_settings.get_location_status()
        return templates.TemplateResponse(
            "picam_web.html",
            {
                "request": request,
                # "rec_status": status_dict.get("rec_status", ""),
                # "location_status": location_status,
                # "device_name": status_dict.get("device_name", ""),
                # "detector_time": time.strftime("%Y-%m-%d %H:%M:%S"),
                "picam_version": rpi_cam.__version__,
            },
        )
    except Exception as e:
        # Logging error.
        message = "Called: webpage: " + str(e)
        # rpi_cam.picam_logging.error(message, short_message=message)


@app.get("/start-live-view/")
async def start_live_view():
    try:
        global picam_manager
        # Logging debug.
        # picam_manager.picam_logging.debug(message="API called: start-live-view.")
        await picam_manager.start_live_view()
    except Exception as e:
        # Logging error.
        message = "Called: start_rec: " + str(e)
        # picam_manager.picam_logging.error(message, short_message=message)


@app.get("/stop-live-view/")
async def stop_live_view():
    try:
        global picam_manager
        # Logging debug.
        # picam_manager.picam_logging.debug(message="API called: stop-live-view.")
        await picam_manager.stop_live_view()
    except Exception as e:
        # Logging error.
        message = "Called: start_rec: " + str(e)
        # picam_manager.picam_logging.error(message, short_message=message)

