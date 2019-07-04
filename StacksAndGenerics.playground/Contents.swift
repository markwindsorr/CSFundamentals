import UIKit

/*
 
Here we analyze how to implement a Stack using a simple LinkedList Node Data structure.
We are going to implement the push and pop functions of a Stack. Finally, let's support
Genergice by modifying our Stack class to be of parameter T. This will allow us to push
and pop values out of our Stack very easily based on what we need to support.
 
 
*/

class Node<T> {
    
    let value : T
    var next : Node?
    
    init(_ value: T){
        self.value = value
    }
}

class Stack<T> {
    
    var top : Node<T>?
    
    func push(_ value: T) {
        let oldTop = top   // get the previous top
        top = Node(value)  // assign new top
        top?.next = oldTop // assign next node to be the previous top
    }
    
    func pop() -> T? {
        let currentTop = top     // get current top
        top = top?.next          // assign top to be the next node in stack
        return currentTop?.value // return the current tops value
    }
    
    func peek() -> T? {
        return top?.value // just return the current tops value
    }
    
}

struct User {
    let name: String
    let username: String
}


//Here we will create a Stack of Ints

let intStack = Stack<Int>()

intStack.push(1)
intStack.push(2)
intStack.push(3)

intStack.peek()
intStack.pop()

//Here we will create a stack of users

let userStack = Stack<User>()

let me = User(name: "Mark", username: "markwindsorr")
let you = User(name: "Brian", username: "brianIsGun")

userStack.push(me)
userStack.push(you)

userStack.peek()




