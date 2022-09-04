import sys

KEYS_low = {
  1  : "ESC",
  2  : "1",
  3  : "2",
  4  : "3",
  5  : "4",
  6  : "5",
  7  : "6",
  8  : "7",
  9  : "8",
  10 : "9",
  11 : "0",
  16 : "q",
  17 : "w",
  18 : "e",
  19 : "r",
  20 : "t",
  21 : "y",
  22 : "u",
  23 : "i",
  24 : "o",
  25 : "p",
  30 : "a",
  31 : "S",
  32 : "d",
  33 : "f",
  34 : "g",
  35 : "h",
  36 : "j",
  37 : "k",
  38 : "l",
  44 : "z",
  45 : "x",
  46 : "c",
  47 : "v",
  48 : "b",
  49 : "n",
  50 : "m",
  29: "LEFTCTRL",
  15: "\t",
  28: "\n",
  108: "DOWN",
  14: "\\",
  42: "SHIFT",
  27: "{",
  43: "_",
  105: "LEFT",
  89: "KEY_RO",
  79: "KEY_KP1",
  57: " ",
  52: "."
}
KEYS_high = {
  1  : "ESC",
  2  : "1",
  3  : "2",
  4  : "3",
  5  : "4",
  6  : "5",
  7  : "6",
  8  : "7",
  9  : "8",
  10 : "9",
  11 : "0",
  16 : "Q",
  17 : "W",
  18 : "E",
  19 : "R",
  20 : "T",
  21 : "Y",
  22 : "U",
  23 : "I",
  24 : "O",
  25 : "P",
  30 : "A",
  31 : "S",
  32 : "D",
  33 : "F",
  34 : "G",
  35 : "H",
  36 : "J",
  37 : "K",
  38 : "L",
  44 : "Z",
  45 : "X",
  46 : "C",
  47 : "V",
  48 : "B",
  49 : "N",
  50 : "M",
  29: "LEFTCTRL",
  15: "TAB",
  28: "ENTER",
  108: "DOWN",
  14: "BACKSPACE",
  42: "SHIFT",
  27: "4",
  43: "8",
  105: "LEFT",
  89: "KEY_RO",
  79: "KEY_KP1",
  57: "SPACE",
  52: "DOT"
}

def read_data(f):
    return f.read(3)

def main(f):
    the_data = b''
    doner = False
    try:
        while True:
            new_data = read_data(f)
            the_data += new_data

            key_num = new_data[0]
            if new_data[2] == 0:
                print("release ",end="")
            if new_data[2] == 1:
                print("press ",end="")
            if new_data[2] == 2:
                print("held ",end="")

            print(KEYS[key_num])
    except Exception as e:
        print(e)


if __name__=="__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <data file>")
        exit(0)
    
    f = open(sys.argv[1],'rb')

    main(f)