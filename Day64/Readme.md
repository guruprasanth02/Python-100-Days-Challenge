# 🌟 Day 64: Exploring Object-Oriented Programming – Jobs, Subclasses, and Methods 💼

### 🎉 Today’s Highlights:

* **Object-Oriented Programming (OOP):** We explored the basics of OOP, focusing on classes, objects, methods, and inheritance.
* **Classes and Objects:** Learned how to define classes as templates and create objects (instances) from them.
* **Methods:** Explored how to define and use methods, including initialization ```(__init__)``` and custom methods.
* **Inheritance:** Understood how to create subclasses that inherit attributes and methods from a parent class while adding their own unique features.

### 🔍 Key Concepts:

1. **Classes and Objects:**

     * A class is like a blueprint (e.g., a template for jobs).
     * An object is an instance of a class (e.g., a specific job like a teacher or doctor).

2. **Methods:**

     * Subroutines defined within a class are called methods.
     * ```__init__:``` Special method to initialize object attributes when an object is created.

3. **Inheritance:**

     * Subclasses inherit attributes and methods from a parent class.
     * Subclasses can add their own attributes and override parent methods.

4. **Encapsulation:**

      * Data and methods are encapsulated within classes to create reusable and organized code.

### 👉 Day 64 Challenge: Representing Jobs

**Task Overview:**

1. **Create a generic ```Job``` class:**

      * Attributes: ```name```, ```salary```, and ```hours worked```.
      * Method: A function to print the job details.

2. **Create two subclasses:**

      * ```Doctor:``` Includes additional attributes ```speciality``` and ```years of experience```.
      * ```Teacher```: Includes additional attributes ```subject``` and ```position```.

3. **Instantiate objects for:**

      * A lawyer.
      * A computer science teacher.
      * A pediatric doctor with 7 years of experience.

4. Output the details of each job using the methods in their respective classes.

### 🛠️ Common Errors Encountered:

* **Missing ```self``` Parameter:**

     * Always include ```self``` as the first parameter in class methods to refer to the instance calling the method.

* **Incorrect Inheritance Syntax:**

     * Use ```class SubclassName(ParentClassName):``` to inherit from a parent class.

* **Overwriting Parent Attributes:**

     * When defining a subclass ```__init__``` method, call the parent class's ```__init__``` to avoid losing inherited attributes.

### 💻 Example Code:
```python
class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")

class doctor(job):
  experience = None
  speciality = None

  def __init__(self, salary, hoursWorked, experience, speciality):
    self.name = "Doctor"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.experience = experience
    self.speciality = speciality

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.experience:<10} {self.speciality:>21}")

class teacher(job):
  subject = None
  position = None

  def __init__(self, salary, hoursWorked, subject,  position):
    self.name = "Teacher"
    self.hoursWorked = hoursWorked
    self.salary = salary
    self.subject = subject
    self.position = position
  
  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.subject:<10} {self.position:>21}")

lawyer = job("Lawyer", "$100,000", "40")
lawyer.print()

doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print()

teach = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teach.print()
