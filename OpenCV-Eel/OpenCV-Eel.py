#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import base64

import eel
import cv2

cap = cv2.VideoCapture(2)

eel.init('web')
eel.start('index.html',mode='chrome',cmdline_args=['--start-fullscreen'],block=False)

while True:
    start_time = time.time()

    eel.sleep(0.01)

    ret, frame = cap.read()
    if not ret:
        continue

    _, imencode_image = cv2.imencode('.jpg', frame)
    base64_image = base64.b64encode(imencode_image)
    eel.set_base64image("data:image/jpg;base64," + base64_image.decode("ascii"))

    cv2.waitKey(1)

    elapsed_time = round((time.time() - start_time), 3)
    eel.set_elapsedtime(elapsed_time)