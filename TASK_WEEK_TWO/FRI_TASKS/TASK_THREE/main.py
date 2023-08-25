import time
import pyautogui
import os

# Open Visual Studio Code
def open_vscode():
    pyautogui.hotkey("win", "s")  # Open Windows search
    time.sleep(1)  # Wait for search to open
    pyautogui.write("Visual Studio Code")  # Type "Visual Studio Code"
    mypath= os.path.dirname(os.path.realpath(__file__))+"/vscode.jpg"
    isfind= None
    while isfind is None:
        isfind = pyautogui.locateOnScreen(mypath,confidence=0.7)
        
    pyautogui.press("enter")  # Press Enter
    time.sleep(5)  # Wait for VSCode to open



# pyautogui.hotkey("win", "s")  # Open Windows search
# time.sleep(1)  # Wait for search to open
# pyautogui.write("Visual Studio Code")  # Type "Visual Studio Code"
# mypath= os.path.dirname(os.path.realpath(__file__))+"/vscode.jpg"
# isfind= None
# while isfind is None:
#     isfind = pyautogui.locateOnScreen(mypath,confidence=0.7)
    
# pyautogui.press("enter")  # Press Enter
# time.sleep(5)  # Wait for VSCode to open   
# x,y= os.path.dirname(os.path.realpath(__file__))+"/extensions.PNG"
# pyautogui.moveTo(x, y, duration=0.5)
# isfind= None
# while isfind is None:
#     isfind = pyautogui.locateOnScreen(mypath,confidence=0.7)
# pyautogui.write("clangd")  # Type "clanged"
# mypath= os.path.dirname(os.path.realpath(__file__))+"/Clangd.PNG"
# isfind= None
# while isfind is None:
#     isfind = pyautogui.locateOnScreen(mypath,confidence=0.7)
# pyautogui.press('tab')
# pyautogui.press('enter')





# Install Extensions
def install_extensions():
    extensions = [
        "llvm-vs-code-extensions.vscode-clangd",  # clangd
        "matepek.vscode-catch2-test-adapter",     # C++ TestMate
        "austin.code-gnu-global",                 # C++ Helper
        "twxs.cmake",                             # CMake
        "ms-vscode.cmake-tools"                   # CMake Tools
    ]

    for extension in extensions:
        pyautogui.hotkey("ctrl", "p")  # Open Quick Open
        time.sleep(1)
        pyautogui.write(f"ext install {extension}")  # Type the extension name
        pyautogui.press("enter")
        time.sleep(5)  # Wait for extension to install

if __name__ == "__main__":
    open_vscode()  # Open VSCode
    time.sleep(10)  # Wait for VSCode to open
    install_extensions()  # Install extensions
