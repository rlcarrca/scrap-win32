from __future__ import generators
import win32net

resume = 0
while 1:
  (_drives, total, resume) = win32net.NetUseEnum (None, 0, resume)
  for drive in _drives:
    if drive['local']:
      print drive['local'], "=>", drive['remote']
  if not resume: break