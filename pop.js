class Node {
    contructor(val) {
        this.val = val
        this.next = null
        this.prev = null
    }
}
class DoublyLinkedList {
    constructor() {
        this.head = null
        this.tail = null
        this.length = 0
    }
    push(val) {
        var newNode = new Node(val)
        if (!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            this.tail.next = newNode
            newNode.prev = this.tail
            this.tail = newNode
        }
        this.length++
        return this
    }
    pop() {
        if (!this.head) return undefined
        var poppedVal = this.tail
        if (this.length === 1) {
            this.head = null
            this.tail = null
        } else {
            this.tail = poppedVal.prev
            this.tail.next = null
            this.tail = null
        }
        this.length--
        return this
    }
}

list = new DoublyLinkedList()
list.push(1)
list.push(2)
list.push(3)
list.pop()