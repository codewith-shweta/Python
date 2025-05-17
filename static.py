class Goal:
    def __init__(self,name,position):
        self.name = name
        self.position = position

    def name(self):
        return f"{self.name} = {self.position}"

@staticmethod
def valid(position):
    valids = ["Chef","Monitor","Cookie", "Cook"]
    return position in valids

employee1 = Goal("Engagement","Prank")
employee1.info("Prank")

#nthi thatu

