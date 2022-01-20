import pasword_screen
import sys

def window():
    app = pasword_screen.QApplication(sys.argv)
    win = pasword_screen.MyWindow()  
    win.show()
    sys.exit(app.exec_())
    
window()