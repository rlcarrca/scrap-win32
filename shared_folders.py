import win32net
import win32netcon

COMPUTER_NAME = "" # look at this machine
INFO_LEVEL = 2

resume = 0
while 1:
  (shares, total, resume) = \
    win32net.NetShareEnum (
      COMPUTER_NAME,
      INFO_LEVEL,
      resume,
      win32netcon.MAX_PREFERRED_LENGTH
    )
  for share in shares:
    print share['netname'], "=>", share['path']
  if not resume:
    break
