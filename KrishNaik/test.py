// XOR Doubly Linked List Node
struct xdll_node {
    int elem;
    struct xdll_node* nxp;  // XOR of next and previous node
};

// Function to iterate over XOR Doubly Linked List
void iter(struct xdll_node* head, void (*iter_fn)(struct xdll_node*)) {
    struct xdll_node *prev = NULL, *current = head, *next;

    while (current != NULL) {
        // Call the function
        iter_fn(current);

        // Get the next node
        next = (struct xdll_node*)((uintptr_t)(prev) ^ (uintptr_t)(current->nxp));

        // Update previous and current
        prev = current;
        current = next;
    }
}

// Function to rotate XOR Doubly Linked List
struct xdll_node* rotate(struct xdll_node* head) {
    struct xdll_node *prev = NULL, *current = head, *next;

    // Traverse to the end of the list
    while (current->nxp != prev) {
        next = (struct xdll_node*)((uintptr_t)(prev) ^ (uintptr_t)(current->nxp));
        prev = current;
        current = next;
    }

    // Now current is at the end of the list
    // And prev is the second last node

    // Disconnect the last node from the second last node
    prev->nxp = (struct xdll_node*)((uintptr_t)(prev->nxp) ^ (uintptr_t)(current));
    current->nxp = prev;

    return current;
}
