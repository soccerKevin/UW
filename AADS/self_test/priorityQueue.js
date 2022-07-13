class Elem {
  constructor(elem, priority) {
    this.elem = elem
    this.priority = priority
  }
}

class PriorityQueue {
  constructor() {
    this.queue = new Array()
  }

  add(elem, priority) {
    let contains = false

    for (const i in this.queue) {
      const currentElem = this.queue[i]
      if (currentElem.priority > priority) {
        // Insert just before this element
        this.queue.splice(i, 0, new Elem(elem, priority))
        contains = true
        break;
      }
    }

    if (!contains) this.queue.push(new Elem(elem, priority))
  }

  pop() {
    return this.queue.shift().elem
  }
}

module.exports = PriorityQueue

