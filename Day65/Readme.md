# 🌟 Day 65: OOP Game Characters 🕹️✨

### 🎊 Today’s Highlights:

* **Object-Oriented Programming (OOP):** We used OOP principles to design and manage game characters with attributes and behaviors.
* **Inheritance in Action:** Leveraged inheritance to create a base class ```Character``` and extend it with subclasses ```Player``` and ```Enemy```, adding unique properties and methods.
* **Encapsulation and Polymorphism:** Demonstrated encapsulation by grouping character-related data and functionality and polymorphism by overriding methods in subclasses.

### 🔍 Key Concepts:

1. **Base Class - ```Character```:**

    * Contains shared attributes (```name```, ```health```, ```magic_points```) and a method to display them.
    * Initializes these values during object creation.

2. **Sub-Class - ```Player```:**

    * Inherits from ```Character``` and adds a ```lives``` attribute.
    * Includes an ```am_i_alive()``` method to check if the player is alive (```health > 0```).

3. **Sub-Class - ```Enemy```:**

    * Inherits from ```Character``` and introduces ```type``` and ```strength``` attributes.
    * Further subclassed into:
      
         * ```Orc```: Adds a ```speed``` attribute.
         * ```Vampire```: Adds a ```day_night``` tracker to indicate activity time.

4. **Instantiating Objects:**

    * Created one player, two vampires, and three orcs with unique attributes.
    * Used methods to display their details.

### 👉 Day 65 Challenge: Game Character Management Overview:

1. **Create a Base Class (```Character```):**

      * Attributes: ```name```, ```health```, ```magic_points```.
      * Method: ```display_info()``` to output character details.

2. **Create Subclasses:**

      * Player: Add ```lives``` and ```am_i_alive()``` method.
      * ```Enemy```: Add type and strength.
        
           * ```Orc```: Add ```speed```.
           * ```Vampire```: Add ```day_night```.

3. **Instantiate Objects and Display Values:**

      * Player: Name, health, magic points, lives.
      * Vampires: Name, health, magic points, type, strength, day/night status.
      * Orcs: Name, health, magic points, type, strength, speed.

### 🛠️ Common Errors Encountered:

1. **Initialization Errors:**

      * Forgetting to call the base class initializer in subclasses.
      * Fix: Use ```super().__init__()``` to ensure the base class attributes are initialized.

2. **Attribute Errors:**

      * Accessing non-existent attributes or forgetting to define them.
      * Fix: Define all required attributes in ```__init__()``` and use meaningful default values.

3. **Method Overriding Issues:**

      * Forgetting to properly override or extend methods in subclasses.
      * Fix: Use ```super().method()``` to retain base class functionality if needed.

4. **Object Instantiation Mistakes:**

      * Forgetting required parameters when creating objects.
      * Fix: Provide all necessary arguments as per the class definition.


### 📜 My Code:
```python
class character:
  name = None
  health = 100
  mp = 100

  def __init__(self, name):
    self.name = name

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}")

  def setStats(self, health, mp):
    self.health = health
    self.mp = mp

class player(character):
  nickname = None
  lives = 3

  def __init__(self, nickname):
    self.name = "Player"
    self.nickname = nickname

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tNickname: {self.nickname}\tLives: {self.lives}")

  def isAlive(self):
    if self.lives > 0:
      print(f"{self.nickname} lives on!")
      return True
    else:
      print(f"{self.nickname} has expired!")
      return False

IronMan = player("IronMan the mighty")
IronMan.print()
print(IronMan.isAlive())

class enemy(character):
  type = None
  strength = None

  def __init__(self, name, type, strength):
    self.name = name
    self.type = type
    self.strength = strength

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}")

class orc(enemy):
  speed = None

  def __init__(self, speed):
    self.name = "Orc"
    self.type = "Orc"
    self.strength = 200
    self.speed = speed

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tSpeed: {self.speed}")

Thanos = orc(250)
Vision = orc(205)

Thanos.print()
Vision.print()

class vampire(enemy):
  day = True

  def __init__(self, day):
    self.name = "Vampire"
    self.type = "Vampire"
    self.strength = 150
    self.day = day

  def print(self):
    print(f"{self.name}\tHP: {self.health}\t MP: {self.mp}\tType: {self.type}\tStrength: {self.strength}\tDay: {self.day}")

Vanhil = vampire(False)
Vanhil.print()
