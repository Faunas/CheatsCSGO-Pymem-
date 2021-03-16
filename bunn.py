import time

import keyboard
import pymem
import requests

#csgo.hpp
#  ---------- Получение оффсетов для чита  ----------
_process = pymem.Pymem("csgo.exe")
_client = pymem.process.module_from_name(_process.process_handle, "client.dll").lpBaseOfDll

dwForceJump = (0x524CEB4)
dwLocalPlayer = (0xD8B2BC)
m_fFlags = (0x104)

def BHOP():
    while True:
        try:
            if keyboard.is_pressed("space"):
                player = _process.read_int(_client + dwLocalPlayer)
                jump = _client + dwForceJump
                player_state = _process.read_int(player + m_fFlags)

                if player_state == 257 or player_state == 263:  # 257 и 263
                    _process.write_int(jump, 5)
                    time.sleep(0.1)  #
                    _process.write_int(jump, 4)
        except pymem.exception.MemoryReadError:
            pass

BHOP()

a=1