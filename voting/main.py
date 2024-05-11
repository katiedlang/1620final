
import sys
import json
from PyQt5.QtWidgets import QApplication, QMessageBox
from voting_gui import VotingApp

class VotingAppMain(VotingApp):
   def __init__(self):
       super().__init__()

       # Connect signals
       self.btn_submit.clicked.connect(self.handle_vote_submission)

       # Initialize voter list
       self.voters = self.load_voters()

   def handle_vote_submission(self):
       voter_id = self.input_id.text()
       candidate = "Jane" if self.radio_jane.isChecked() else "John"

       try:
           # Validate voter ID (example: must be numeric)
           if not voter_id.isdigit():
               raise ValueError("Invalid voter ID. Please enter a numeric value.")

           # Check if voter has already voted
           if self.has_already_voted(voter_id):
               raise Exception("You have already voted. Duplicate votes are not allowed.")

           # Handle the vote (store it, update UI, etc.)
           self.process_vote(voter_id, candidate)
           QMessageBox.information(self, 'Vote Submitted', f"Voter {voter_id} voted for {candidate}")
       except Exception as e:
           QMessageBox.warning(self, 'Error', f"Error: {e}")

   def has_already_voted(self, voter_id):
       return voter_id in self.voters

   def process_vote(self, voter_id, candidate):
       self.voters.append(voter_id)
       self.save_voters()
       # You can add code here to store the vote (e.g., in a file or database)

   def load_voters(self):
       try:
           with open('voters.json', 'r') as f:
               return json.load(f)
       except FileNotFoundError:
           return []

   def save_voters(self):
       with open('voters.json', 'w') as f:
           json.dump(self.voters, f)

if __name__ == "__main__":
   app = QApplication(sys.argv)
   window = VotingAppMain()
   window.show()
   sys.exit(app.exec_())
