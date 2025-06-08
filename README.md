<p align="center"><b>Software Design (2025)</b><br>Sepuluh Nopember Institute of Technology</p>

<p align="center"><img src="https://raw.githubusercontent.com/Rubinskiy/IF184202-Data-Structures/main/its.png" style="transform: scale(0.5);"></p>
  
<p align="center">Design Pattern implementation to our Final Project that was created for <a href="https://www.its.ac.id/informatika/wp-content/uploads/sites/44/2023/11/Module-Handbook-Bachelor-of-Informatics-Program-ITS.pdf">ER234301</a>.</p>
<p align="center">All solutions were created by <a href="https://github.com/Rubinskiy">Robin</a>, <a href="https://github.com/FawwazAlJawi">Jawi</a>, <a href="https://github.com/parisyaputri">Parisya</a>, and <a href="https://github.com/Argreion">Zhafir</a></p>

<hr>

# Overview

Our final project is a mobile application that allows students to create events and post them to a community of students who are interested in the event. The application is built using Flutter and Firebase.

In this project, we implemented the following design patterns:
- Proxy Pattern: Primarily in use for the event creation feature, where only verified students can create events.
- Observer Pattern: Primarily in use for the event reminder feature, where students are notified about the event.

# Proxy Pattern

## Overview

Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

## Implementation

<img src="https://refactoring.guru/images/patterns/diagrams/proxy/problem-en.png?id=b36e65189e939de5dc809636c1946a43">
Database queries can be really slow.

Solution:

<img src="https://refactoring.guru/images/patterns/diagrams/proxy/solution-en.png?id=ab36b8b03fabf92c7dd10ad87507b78c">
A proxy is a wrapper around the original object. It can perform additional actions before or after the request gets through to the original object.

# Observer Pattern

## Overview

Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

## Implementation

<img src="https://refactoring.guru/images/patterns/content/observer/observer-comic-1-en.png?id=1ec8571b22ea8fd2ed537f06cc763152">
Image on the left is a customer visiting the store every day to check if the product they want is available.
Image on the right is the store sending emails every time a new product is available.

Solution:

<img src="https://refactoring.guru/images/patterns/diagrams/observer/solution1-en.png?id=60fb9a2822649dec1c68b78733479c57">
A subscription mechanism lets individual objects subscribe to event notifications.

## References
[Proxy Pattern](https://refactoring.guru/design-patterns/proxy)
[Observer Pattern](https://refactoring.guru/design-patterns/observer)