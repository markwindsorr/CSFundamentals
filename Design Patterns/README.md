<h1 align="center">
	:white_flower: Design Patterns
</h1>

<h3 align="center">
	A Learning Repository
</h3>

___

## Creational

### Singleton

The singleton design pattern ensures that there is only one instance of that class and that you can access it globally.

## Structural

### Model View Controller (MVC)

Commonly used for user interfaces and divides the program logic into three interconnected elements.

* Models: where your data resides. Things like persistence, model objects, parsers, managers, and networking code live here
* Views: what the user sees. These classes are often reusable as they contain domain-specific logic. UILabel is a view in iOS that presents text on the screen. Its extensible and reusable
* Controllers: Where you write most of your code. Mediates between the view and the model. In iOS they usually interact via the delegation pattern. A common example is when we have a view controller and a table view inside the view controller. The table view is the delegating object and the view controller is the delegate. The table view has protocols called UITableViewDelegate and UITableViewDatasource. Each protocol has a list of methods that will be implemented by the delegate which is the view controller. The delegating object (table view) keeps a reference of the delegate (view controller) and notifies it of an event that the delegating object (view controller) is about to handle or has just handled, such as the didSelectRowAtIndexPath method. 

### Delegation

### Model-View-ViewModel (MVVM)


Separates the development of the interface from the development of the business logic. The view model provides data from the model in a form that the view can easily use. Its a structural design pattern that separates objects into three distinct groups:

* Models: holds the applications data. They're usually structs or simple classes.
* Views: displays visual elements and controls on the screen
* View Models: transform model information into values that can be displayed on a view. They're usually classes, so they can be passed around as references.

## Behavioral

### Singleton



