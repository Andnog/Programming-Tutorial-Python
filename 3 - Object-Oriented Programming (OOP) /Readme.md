# 💻 Object-Oriented Programming (OOP) Overview

This section provides an overview of Object-Oriented Programming (OOP) concepts, covering both the presentation content and detailed topics from the provided notebooks. It is aimed at those who wish to understand the core principles of OOP, including classes, objects, and SOLID principles.

## 📚 Table of Contents

### 📊 Presentation Content

The presentation provides an introduction to the main concepts of Object-Oriented Programming:

1. **🏛️ Classes and 🎯 Objects**: An overview of how classes serve as blueprints for objects, and the relationship between classes and instances.
2. **⚙️ Methods and 📦 Attributes**: Explanation of attributes (both class and instance) and methods that define object behavior.
3. **👨‍👩‍👧‍👦 Inheritance**: A detailed explanation of how inheritance allows classes to derive properties and behaviors from other classes.
4. **🔄 Polymorphism**: Concepts of polymorphism, enabling different classes to be treated as instances of a common superclass, and allowing method overriding.
5. **🔒 Encapsulation**: The process of bundling data and methods into a single unit, ensuring data integrity through access control.
6. **🌀 Abstraction**: Introduction to abstract classes and methods, emphasizing hiding implementation details and focusing on essential functionalities.

### 📓 Notebook Content

#### 1. 🏛️ Classes and 🎯 Objects

- **🏛️ Class**
  - **Definition**: A class is a blueprint for creating objects, encapsulating data (attributes) and behaviors (methods).
  - **Implementation**: How to create a class in Python using the `class` keyword.
  - **Class 📦 Attributes and Instance 📦 Attributes**: Class attributes are shared among all instances, whereas instance attributes are specific to each object.
  - **⚙️ Methods in a 🏛️ Class**: Methods define the behavior of objects; they include a reference to the object (`self`).

- **🎯 Objects**
  - **Definition**: An object is an instance of a class, representing a specific entity in memory.
  - **Instance**: How to create an object using a class constructor.
  - **Accessing Class 📦 Attributes and ⚙️ Methods**: Using dot notation to interact with an object's attributes and methods.

#### 2. Four Pillars of OOP

- **👨‍👩‍👧‍👦 Inheritance**
  - **Inheritance Relationships**: Parent-child relationships between classes, enabling code reuse.
  - **Subclasses and Superclasses**: Subclasses inherit from superclasses and can add or modify functionality.
  - **Inheritance Hierarchy**: Organizing classes in a hierarchical manner for specialization and reuse.

- **🔄 Polymorphism**
  - **Concept**: Allows different classes to be treated as instances of a common superclass.
  - **Importance**: Promotes flexibility, code reuse, and simplified interface design.
  - **Method Overriding and Dynamic Method Dispatch**: Redefining methods in a subclass and determining which method to call at runtime.

- **🔒 Encapsulation**
  - **Data Hiding**: Restricting direct access to object attributes to protect data integrity.
  - **Access Modifiers**: Public, private, and protected modifiers control the visibility of class attributes and methods.
  - **📥 Attribute Getters/Setters**: Using getters and setters to provide controlled access to attributes.

- **🌀 Abstraction**
  - **Abstract Classes**: Classes that cannot be instantiated and serve as blueprints for subclasses.
  - **Abstract Methods and Implementations**: Methods that must be implemented by subclasses, providing a template for required functionality.

- **💻 Code Example**: Example of using OOP concepts to model a library system, demonstrating classes, inheritance, and methods.

#### 3. 🛠️ SOLID Principles

- **SOLID Principles Explanation**: A set of design principles aimed at improving software design and maintainability.
  - **Single Responsibility Principle**: A class should have one and only one reason to change.
  - **Open-Closed Principle**: Classes should be open for extension but closed for modification.
  - **Liskov Substitution Principle**: Subtypes must be substitutable for their base types without altering the correctness of the program.
  - **Interface Segregation Principle**: Clients should not be forced to depend on interfaces they do not use.
  - **Dependency Inversion Principle**: High-level modules should not depend on low-level modules; both should depend on abstractions.