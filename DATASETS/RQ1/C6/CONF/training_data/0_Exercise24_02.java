public class MyLinkedList<E> extends MyAbstractList<E> {

  private Node<E> head, tail;

  
  public MyLinkedList() {
  }

  
  public MyLinkedList(E[] objects) {
    super(objects);
  }

  
  public E getLast() {
    if (size == 0) {
      return null;
    } else {
      return tail.element;
    }
  }

  
  public boolean contains(E e) {
    Node<E> current = head;
    while (current != null) {
      if (e.equals(current.element)) {
        return true;
      }
      current = current.next;
    }
    return false;
  }

  
  public E get(int index) {
    checkIndex(index);
    Node<E> current = head;
    for (int i = 0; i < index; i++) {
      current = current.next;
    }
    return current.element;
  }

  
  public int indexOf(E e) {
    Node<E> current = head;
    for (int i = 0; i < size; i++) {
      if (e.equals(current.element)) {
        return i;
      }
      current = current.next;
    }
    return -1;
  }

  
  public int lastIndexOf(E e) {
    Node<E> current = tail;
    for (int i = size - 1; i >= 0; i--) {
      if (e.equals(current.element)) {
        return i;
      }
      current = current.previous;
    }
    return -1;
  }

  
  public E set(int index, E e) {
    checkIndex(index);
    Node<E> current = head;
    for (int i = 0; i < index; i++) {
      current = current.next;
    }
    E oldElement = current.element;
    current.element = e;
    return oldElement;
  }

  
  private static class Node<E> {
    E element;
    Node<E> next;
    Node<E> previous;

    public Node(E element) {
      this.element = element;
    }
  }

}