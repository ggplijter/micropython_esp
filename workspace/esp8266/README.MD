

## esp8266:

### from download 
1) go to: `https://micropython.org/download/ESP8266_GENERIC/`
2) download a version with 1M, ie: `ESP8266_GENERIC-FLASH_1M-20241129-v1.24.1.bin`
3) run:
   - `.\..\.venv\Scripts\esptool.exe --baud 115200 read_flash 0x00000 0x100000 firmware_backup.bin`
   - `.\..\.venv\Scripts\esptool.exe erase_flash`
   - `.\..\.venv\Scripts\esptool.exe --baud 460800 write_flash --flash_size=detect -fm dout 0 .\fw\ESP8266_GENERIC-FLASH_1M-20241129-v1.24.1.bin`


### building from source 

see also:
- https://docs.micropython.org/en/latest/develop/gettingstarted.html
- build_from_source/micropython/ports/esp8266/README.md


#### ON WINDOWS:

Start WSL (Ubuntu for example)

1) cd ~
2) sudo apt-get update && sudo apt-get upgrade
3) sudo apt-get install build-essential libffi-dev git pkg-config esptool
4) mkdir projects/build_micropython_from_src
5) cd projects/build_micropython_from_src
6) wget https://github.com/jepler/esp-open-sdk/releases/download/2018-06-10/xtensa-lx106-elf-standalone.tar.gz
7) tar zxvf xtensa-lx106-elf-standalone.tar.gz
8) rm xtensa-lx106-elf/bin/esptool.py
9) export PATH=$(pwd)/xtensa-lx106-elf/bin/:$PATH
10) git clone --recursive https://github.com/micropython/micropython.git
10) cd micropython/ports/esp8266/
11) make BOARD=ESP8266_GENERIC BOARD_VARIANT=FLASH_1M

 cd ~
  191  ls
  192  mkdir projects
  193  cd projects/
  194  mkdir build_micropython_from_src
  195  cd build_micropython_from_src/
  196  wget https://github.com/jepler/esp-open-sdk/releases/download/2018-06-10/xtensa-lx106-elf-standalone.tar.gz
  197  tar zxvf xtensa-lx106-elf-standalone.tar.gz
  198  export PATH=$(pwd)/xtensa-lx106-elf/bin/:$PATH
  199  git clone --recursive https://github.com/micropython/micropython.git
  200  cd micropython/ports/esp8266/
  201  ls
  202  echo $PATH
  203  make BOARD=ESP8266_GENERIC BOARD_VARIANT=FLASH_1M
  204  cp build-ESP8266_GENERIC-FLASH_1M/firmware.bin ~/projects/build_micropython_from_src/

`git submodule update --init --recursive`

##### from folder inside repo with WSL

2) sudo apt-get update && sudo apt-get upgrade
3) sudo apt-get install build-essential libffi-dev git pkg-config esptool
4) tar zxvf xtensa-lx106-elf-standalone.tar.gz
5) rm xtensa-lx106-elf/bin/esptool.py
6) export PATH=$(pwd)/xtensa-lx106-elf/bin/:$PATH                                                               

##### build esp8266 port
2) cd micropython/ports/esp8266
3) make BOARD=ESP8266_GENERIC BOARD_VARIANT=FLASH_1M



#### ON LINUX:
##### download toolchain espressif
1) `mkdir ~/projects/espressif`
2) `cd ~/projects/espressif`
3) `wget https://github.com/jepler/esp-open-sdk/releases/download/2018-06-10/xtensa-lx106-elf-standalone.tar.gz` (download espressif toolchain)
4) tar zxvf xtensa-lx106-elf-standalone.tar.gz
5) `rm xtensa-lx106-elf/bin/esptool.py`
6) `export PATH=$HOME/projects/espressif/xtensa-lx106-elf/bin/:$PATH`

##### build esp8266 port
1) `cd projects` 
2) `git clone --recursive https://github.com/micropython/micropython.git`
3) `cd micropython/ports/esp8266`
4) `make BOARD=ESP8266_GENERIC BOARD_VARIANT=FLASH_1M` 
5) if succeeded something like this should appear:

```
Successfully created esp8266 image.
flash     33488
 .text    31264 at 0x40100000
 .data    1060 at 0x3ffe8000
 .rodata  1124 at 0x3ffe8430
padding   3376
irom0text 563288
total     600152
md5       ec732483b7c8209438978424ac4bc825
```

`.\.venv\Scripts\mpremote.exe connect COM13`
