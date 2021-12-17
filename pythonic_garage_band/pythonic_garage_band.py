class Musician:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    pass

  def __repr__(self):
      pass

  
# ----------------------

# ask how append worked, test 16 and 17

class Band:

  instances = []
  def __init__(self, name, members=None):
    self.name = name
    self.members = members
    Band.instances.append(self)

  def __str__(self):
    return f"The band {self.name}"

  def __repr__(self):
    return f"Band instance. name={self.name}, members={self.members}"

# need to go in each class instance
  @classmethod
  def to_list(cls):
    return cls.instances

  def play_solos(self):
    solos = []
    for member in self.members:
      solos.append(member.play_solo())
    return solos

# ----------------------


# ask for help with setting inherited properties/parent grandparent class
# ----------------------

class Guitarist(Musician):
  
  def __str__(self):
    return f"My name is {self.name} and I play guitar"

  def __repr__(self):
      return f"Guitarist instance. Name = {self.name}"

  @classmethod
  def to_list(cls):
    return cls.instances

  def get_instrument(self):
    return f"guitar"  

  def play_solo(self):
    return f"face melting guitar solo"
  #pass

# ----------------------

class Bassist(Musician):

  def __str__(self):
      return f"My name is {self.name} and I play bass"

  def __repr__(self):
      return f"Bassist instance. Name = {self.name}"

  @classmethod
  def to_list(cls):
    return cls.instances

  def get_instrument(self):
    return f"bass" 

  def play_solo(self):
    return f"bom bom buh bom"
  #pass


# ----------------------
class Drummer(Musician):

  def __str__(self):
      return f"My name is {self.name} and I play drums"

  def __repr__(self):
      return f"Drummer instance. Name = Sheila E."

  @classmethod
  def to_list(cls):
    return cls.instances

  def get_instrument(self):
    return f"drums" 

  def play_solo(self):
    return f"rattle boom crash"
  #pass

# initializing a class means populating values

# The __init__() function is called automatically every time the class is being used to create a new object.
# Use the pass keyword when you do not want to add any other properties or methods to the class.