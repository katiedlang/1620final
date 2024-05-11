from PyQt5.QtWidgets import QMainWindow, QLabel, QRadioButton, QPushButton, QVBoxLayout, QWidget, QLineEdit

class VotingApp(QMainWindow):
   def __init__(self):
       super().__init__()

       # Create widgets
       self.central_widget = QWidget()
       self.setCentralWidget(self.central_widget)

       # Voting Application Interface
       self.label_id = QLabel("Voter ID:")
       self.input_id = QLineEdit()
       self.radio_jane = QRadioButton("Jane")
       self.radio_john = QRadioButton("John")
       self.btn_submit = QPushButton("Submit Vote")

       # Layout for Voting Application Interface
       layout_voting = QVBoxLayout()
       layout_voting.addWidget(self.label_id)
       layout_voting.addWidget(self.input_id)
       layout_voting.addWidget(self.radio_jane)
       layout_voting.addWidget(self.radio_john)
       layout_voting.addWidget(self.btn_submit)

       # Main layout
       main_layout = QVBoxLayout()
       main_layout.addLayout(layout_voting)
       self.central_widget.setLayout(main_layout)
