#неправильный вид кода
#from enum import Enum
#from abc import ABCMeta, abstractmethod

#class Teams(Enum):
  #BLUE_TEAM = 1
  #RED_TEAM = 2
  #GREEN_TEAM = 3

#class Student:
  #def __init__(self, name):
    #self.name = name

#class TeamMemberships():
  #def __init__(self):
    #self.team_memberships = []

 # def add_team_memberships(self, student, team):
    #self.team_memberships.append((student, team))

#class Analysis():
  #def __init__(self, team_student_memberships):
   # memberships = team_student_memberships.team_memberships
    #for members in memberships:
      #if members[1] == Teams.RED_TEAM:
        #print(f'{members[0].name} is in RED team')

#student1 = Student('Ravi')
#student2 = Student('Archie')
#student3 = Student('James')

#team_memberships = TeamMemberships()
#team_memberships.add_team_memberships(student1, Teams.BLUE_TEAM)
#team_memberships.add_team_memberships(student2, Teams.RED_TEAM)
#team_memberships.add_team_memberships(student3, Teams.GREEN_TEAM)

#Analysis(team_memberships)



from enum import Enum
from abc import ABCMeta, abstractmethod

class Teams(Enum):
  BLUE_TEAM = 1
  RED_TEAM = 2
  GREEN_TEAM = 3

class TeamMembershipLookup():
  @abstractmethod
  def find_all_students_of_team(self, team):
    pass

class Student:
  def __init__(self, name):
    self.name = name

class TeamMemberships(TeamMembershipLookup):
  def __init__(self):
    self.team_memberships = []

  def add_team_memberships(self, student, team):
    self.team_memberships.append((student, team))

  def find_all_students_of_team(self, team):
    for members in self.team_memberships:
      if members[1] == team:
        yield members[0].name

class Analysis():
  def __init__(self, team_membership_lookup):
    for student in team_membership_lookup.find_all_students_of_team(Teams.RED_TEAM):
      print(f'{student} is in RED team.')

student1 = Student('Ravi')
student2 = Student('Archie')
student3 = Student('James')

team_memberships = TeamMemberships()
team_memberships.add_team_memberships(student1, Teams.BLUE_TEAM)
team_memberships.add_team_memberships(student2, Teams.RED_TEAM)
team_memberships.add_team_memberships(student3, Teams.GREEN_TEAM)

Analysis(team_memberships)
