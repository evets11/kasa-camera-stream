import os
import sys
import json
import Wrapper
import asyncio
import requests
import HealthChecker
from concurrent.futures import ThreadPoolExecutor

class Controller:
    def loadConfiguration(self, path):
        print("[Controller] Loading configuration.")
        with open(path) as configFile:
            parsedConfig = json.load(configFile)
            return parsedConfig
        print("[Controller] Configuration loaded.")

    def run(self):
        print("[Controller] Controller is starting.")

        # Set variables
        self.config = self.loadConfiguration("/data/options.json")

        # Create Ffmpeg wrapper
        self.ffmpegWrapper = Wrapper.FfmpegWrapper(self, 10)
        self.ffmpegWrapper.startProcess()

        # Start tasks
        loop = asyncio.get_event_loop()

        print("[Controller] Controller is running.")
        loop.run_forever()
        print("[Controller] Exiting.")

def main():
   controller = Controller()
   controller.run()

if __name__ == '__main__':
    main()