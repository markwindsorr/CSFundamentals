import UIKit

/*
Linked Lists

Here we will implement a linked list (insert, delete)
*/

class Node {
    
    let value : String
    var nextNode : Node?
    
    init(value : String, nextNode : Node?) {
        self.nextNode = nextNode
        self.value = value
    }
}


class LinkedList {
    
    var head : Node?
    
    func displayLinkedList (){
        
        if head == nil {
            print("empty list!")
            return
        }
        
        print("Here is your linked list: ")
        
        var currentNode = head
        while currentNode != nil {
            print(currentNode?.value ?? "")
            currentNode = currentNode?.nextNode
        }
        
    }
    
    func insert(value : String){
        
        // Empty list case
        if head == nil {
            head = Node(value: value, nextNode: nil)
            return
        }
        
        // Here we start at the head and traverse until we reach nil aka the end of the list
        // our current node at this point will be the end of the list
        var currentNode = head
        while currentNode?.nextNode != nil {
            currentNode = currentNode?.nextNode
        }
        // We can now assign the nextNode property of our ending node to the node we want to create
        currentNode?.nextNode = Node(value: value, nextNode: nil)
    }
    
    func delete(value : String){
        
        if head?.value == value {
            head = head?.nextNode
        }
        
        var previousNode : Node?
        var currentNode = head
        while currentNode != nil && currentNode?.value != value {
            previousNode = currentNode
            currentNode = currentNode?.nextNode
        }
 
        previousNode?.nextNode = currentNode?.nextNode
    }
    
}


var linkedList = LinkedList()

linkedList.insert(value: "one")
linkedList.insert(value: "two")
linkedList.insert(value: "three")


// One -> Two -> Three -> nil

linkedList.displayLinkedList()

linkedList.delete(value: "two")

linkedList.displayLinkedList()

if let headValue = linkedList.head?.value {
    print("Linked list head is : \(headValue)")
}





