class VotingSystem:
    def __init__(self):
        self.__candidates = {}

    def vote(self, candidate):
        if candidate in self.__candidates:
            self.__candidates[candidate] += 1
        else:
            raise ValueError("Candidate does not exist.")

    def add_candidate(self, candidate):
        if candidate not in self.__candidates:
            self.__candidates[candidate] = 0
        else:
            raise ValueError("Candidate already exists.")

    def get_results(self):
        return self.__candidates

