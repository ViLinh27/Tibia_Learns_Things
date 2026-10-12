# O'Reilly's Real-World Software Development

## A project-driven guide to fundamentals in java

### By Raoul-GAbriel Urma and Richard Warburton

---

## 1: Starting the Journey

### Themes

- It's worth thinking about the different themes that run through the chapters, how they link up together, and why book chose them. We'll see mostly these in this book:

#### Java Features

- What to expect in this book
  - Classes and interfaces will be in Chapter 2.
  - Exceptions and packages in Chapter 3.
  - Variables and Switch expressions in chapter 5
  - Lambs expressions and method references in Chapter 7
- Java has many features that are seen in other languages since it's an OOP language

#### Software Design and Architecture

- there are patterns that exist in programming because it helps make the process more efficient and the code less brittle
- thanks to design patterns, we also know a lot of problems encountered when programming have been seen before
- More stuff to expect later in the book:
  - coupling in cohesion in ch 2
  - notification pattern in ch 3
  - how to design user freindly fluent api and the bildter pattern in ch 5
    hexagonal architecture concepts in ch 6
  - repository pattern in ch 7

#### SOLID

- software is going to change so it has to be well maintained and not brittle as hell
- if we change one feature it can't affect 90 000 other things
- SOLID explained
  - Single Responsiblity principle
    - Ch 2
  - Open/CLosed principle
    - Ch 3
  - Liskov Substitution principle
    - Ch 4
  - Interface Segregation Principle
    - Ch 5
  - Dependency Inversion Principle
    - Ch 7

#### Testing

- we're gonna learn how to AUTOMATE our software tests so we don't have to manually account for every eventuality with our software
- basics are covered in chapter 2 and 4
- Test-driven development (TDD) Chapter 5

### Chapter Summary

- outline of each chapters of this book:

#### Chapter 2: Bank Statement Analyzer

- helps learn:
  - Single Responsibilty Principle
  - Coupling
  - Cohesion

#### Chapter 3: Extending the BAnk Statements Analyzer

- add features from ch 2 program
- uses Strategy Pattern, Open/Close Principle
- how to model failures using exceptions

#### Chapter 4: Document Management System

- intros concepts :
  - inheritance in sw design
  - Liskov substitution principle
  - tradeoffs bewtgeen compoisiton and inheritance
  - write more reliable sw with automated test code

#### Chapter 5: Business Rules Engine

- making way to define business logic that is flexible and easy to maintain
- intros topics
  -test driven development
  - developing Fluent API
  - Interface Segregation Principle

#### Chapter 6: Twootr

- Builds out core of simple TWOOTR system
- learn to think outside-in
  - go from requirements through core of app
- learn how to use test doubles
  - isolate and test interactions from different components in codebase

#### Chapter 7: Extending Twootr

- Extends ch 6 implementation
- explains Dependency Inversion Principle
- Intros bigger pic architectural choices
  - event-driven/ hexagonal architectures
- extrend knowldege of automated testing by covering test doubles
  - stubs
  - mocks
- funcitonal programming techniques

#### Chapter 8: Conclusion

- revisit major themes/ concepts of book
- offer more resources to look into

### Iterating on You

- go for iterative approach in workflow
- start with high prioritiy, learn from that and see what feature is next to work on based on what you learn
- end of each chapter gives suggestions on how to improve on learning from chapter in future

---

The rest of the book is project based so those will be listed in the Projects Section Under Software Development

---
