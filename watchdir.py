#!/usr/bin/env python3

import os, sys
import time
import argparse
import datetime
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

parser = argparse.ArgumentParser()
parser.add_argument('dir', help='The directory you want to observe.')
parser.add_argument('command', help='The command you want to run whenever something is changed in the directory you watch.')
args = parser.parse_args()

# global variable
command = args.command.replace("'", '').replace('"', '')

# class
class directoryEvent(LoggingEventHandler):
  def __init__(self):
    super(directoryEvent, self).__init__()

  def on_any_event(self, event):
    super(directoryEvent, self).on_any_event(event)
    print('\n[%s] %s is changed in directory %s' % (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), event.src_path, args.dir))
    print('        [Run command] %s' % args.command)
    os.system('%s' % command)

observer = Observer()
eventHandler = directoryEvent()
observer.schedule(eventHandler, args.dir, recursive=True)
observer.start()

try:
  while True:
    time.sleep(1)
except KeyboardInterrupt:
  observer.stop()

observer.join()

