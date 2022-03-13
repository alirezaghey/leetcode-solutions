// Definition for Node.
class LinkedListNode {
    val: number
    next: LinkedListNode | null
    random: LinkedListNode | null
    constructor(val?: number, next?: LinkedListNode, random?: LinkedListNode) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
        this.random = (random===undefined ? null : random)
    }
}


// Time complexity: O(n) where n is the length of the linked list
// Space complexity: O(n)
function copyRandomList(head: LinkedListNode | null): LinkedListNode | null {
    
    const dummyHead: LinkedListNode = new LinkedListNode()
    let curr: LinkedListNode = dummyHead
    let currOld: LinkedListNode = head
    const map = new Map<LinkedListNode, LinkedListNode>()
    
    while (currOld != null) {
        curr.next = new LinkedListNode(currOld.val)
        map.set(currOld, curr.next)
        curr = curr.next
        currOld = currOld.next
    }
    
    currOld = head
    while (currOld != null) {
        if (currOld.random != null) {
            map.get(currOld).random = map.get(currOld.random)
        }
        currOld = currOld.next
    }
    
    return dummyHead.next
};