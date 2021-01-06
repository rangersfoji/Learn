from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel
import sys

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.title = 'label with click '
		self.left = 100
		self.top =100
		self.width = 500
		self.height = 300

		self.ini_window()

	def ini_window(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)

		self.set_Componants()

		self.show()

	def set_Componants(self):
		self.label = QLabel('',self)
		self.label.move(50,20)
		self.btn = QPushButton('click me',self)
		self.btn.move(50,50)

		self.btn.clicked.connect(self.on_click)

	def on_click(self):
		print('button clicked')
		self.label.setText('button clicked')
		self.update() # if text more than label size than it will adjust size

	def update(self):
		self.label.adjustSize()




if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	sys.exit(app.exec())