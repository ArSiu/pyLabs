# Run

[1]copy repository
```
$ git clone https://github.com/ArSiu/pyLabs/tree/lab3
```
[1.1]go to directory pyLabs
```
$ cd pyLabs
```
[2]change branch to lab1
```
$ git checkout lab3
```
[3]type in console
```
$ python3 main.py
```
# Wanna Use Code In Your Own
### Edit main.py find fields where we put data and change it.
```
tech_manager = TechniqueManager([
            InkjetPrinter("INKJ2000", "3202", Companies.Panasonic, 2019, 299.9, 220, 60, 100, 100, 10),
            LaserPrinter("LP-2040", "4550", Companies.Panasonic, 2020, 200.0, 220, 160, 150, 150),
            CuttingPlotter("CT25", "3542", Companies.Bosh, 2009, 50, 50, 100, "STL 090"),
            Shredder("RoyTom", "model-Y", Companies.Philips, 2007, 30, 220, 200, 12, 24)
        ])
```
# Some info
### This is the code of lab work for learning Python here is the task.
### Write code from lab2(UML)When writing a program, you need to use the python code convention.Classes need to be properly divided into packages.
### Working with the console or console menu should be minimal.
### Only those classes that are on the class diagram should be present in the code.
### The attributes of the classes and their visibility must match those indicated in the class diagram. The same goes for class methods.
### Use the built-in sorting methods available in Python to sort
### Sorting should be implemented in a separate method
### The code does not contain static methods / attributes. Code must use enum type
### The code should be filled in a separate repository, having previously created a pull request
### (ie the code should be written in a separate branch on its basis to make a pull request)
### To test the operation of your code, you need to create a separate class in which the main method will be located
