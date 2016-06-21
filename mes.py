import sys

if sys.version_info < (3,0):
        import Tkinter as tkinter
        import tkMessageBox as mbox
else:
        import tkinter
        import tkinter.messagebox as mbox

window = tkinter.Tk()
window.wm_withdraw()
mbox.showinfo('my app','my message')
