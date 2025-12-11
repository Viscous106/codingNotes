## 1. DOM Selectors

### `getElementById`

The `document.getElementById()` method returns an `Element` object representing the element whose `id` property matches the specified string. Since `id`s are unique, it's a fast way to get a direct reference to an element.

-   **Syntax**: `document.getElementById(id)`
-   **`id`**: A case-sensitive string representing the ID of the element to locate.
-   **Return Value**: An `Element` object, or `null` if no element with the specified ID is found.

### `getElementsByClassName`, `getElementsByTagName`

These methods return a live `HTMLCollection` of elements, meaning that the collection is automatically updated when changes are made to the document.

-   **`document.getElementsByClassName(names)`**: Returns all child elements which have all of the given class names.
    -   **Syntax**: `document.getElementsByClassName(classNames)`
    -   **`classNames`**: A string containing one or more class names to match, separated by spaces.
    -   **Return Value**: A live `HTMLCollection`.

-   **`document.getElementsByTagName(name)`**: Returns a live `HTMLCollection` of elements with the given tag name.
    -   **Syntax**: `document.getElementsByTagName(tagName)`
    -   **`tagName`**: A string representing the name of the tag to match. The special string `'*'` represents all elements.
    -   **Return Value**: A live `HTMLCollection`.

### `querySelector`

The `document.querySelector()` method returns the first `Element` within the document that matches the specified selector or group of selectors.

-   **Syntax**: `document.querySelector(selectors)`
-   **`selectors`**: A string containing one or more CSS selectors separated by commas.
-   **Return Value**: The first matching `Element`, or `null` if no matches are found.

### `querySelectorAll`

The `document.querySelectorAll()` method returns a static `NodeList` representing a list of the document's elements that match the specified group of selectors.

-   **Syntax**: `document.querySelectorAll(selectors)`
-   **`selectors`**: A string containing one or more CSS selectors separated by commas.
-   **Return Value**: A static `NodeList`.

### `NodeList` Basics

A `NodeList` is a collection of nodes (e.g., elements) extracted from a document.

-   **Static vs. Live**:
    -   `querySelectorAll` returns a *static* `NodeList`: changes to the DOM do not affect the contents of the `NodeList`.
    -   `getElementsByClassName` and `getElementsByTagName` return *live* `HTMLCollection`s: changes to the DOM are reflected in the collection.
-   **Iteration**: `NodeList`s can be iterated using `forEach` or by converting them to an array (`Array.from(nodeList)`).
-   **Access**: Elements can be accessed by index (e.g., `nodeList[0]`).

## 2. Creating & Modifying Elements

### `createElement`

The `document.createElement()` method is used to create a new HTML element with the specified tag name.

-   **Syntax**: `document.createElement(tagName, options)`
-   **`tagName`**: A string specifying the type of element to be created (e.g., `'div'`, `'span'`).
-   **`options` (optional)**: An object that can contain a single property named `is` for custom elements.
-   **Return Value**: The new `Element` object.

### `append`, `prepend`, `appendChild`, `insertBefore`

These methods are used to add nodes to an element.

-   **`Node.appendChild()`**: Adds a single `Node` to the end of the list of children of a specified parent node. If the node already exists, it moves it.
    -   **Syntax**: `parentNode.appendChild(childNode)`
    -   **Return Value**: The appended `childNode`.
    -   **Note**: Only accepts `Node` objects.

-   **`Node.insertBefore()`**: Inserts a single `Node` before a reference node as a child of a specified parent node.
    -   **Syntax**: `parentNode.insertBefore(newNode, referenceNode)`
    -   **`referenceNode`**: The node before which `newNode` is inserted. If `null`, `newNode` is inserted at the end.
    -   **Return Value**: The inserted `newNode`.

-   **`Element.append()`**: Inserts a set of `Node` objects or strings after the last child of the `Element`. It can append multiple arguments and handles strings by converting them to `Text` nodes.
    -   **Syntax**: `parentElement.append(nodeOrString1, nodeOrString2, ...)`
    -   **Return Value**: `undefined`.

-   **`Element.prepend()`**: Inserts a set of `Node` objects or strings before the first child of the `Element`. It can prepend multiple arguments and handles strings by converting them to `Text` nodes.
    -   **Syntax**: `parentElement.prepend(nodeOrString1, nodeOrString2, ...)`
    -   **Return Value**: `undefined`.

### Removing Elements

There are several ways to remove elements from the DOM:

-   **`Element.remove()`**: Removes the element from its parent node directly.
    -   **Syntax**: `element.remove()`
-   **`Node.removeChild()`**: Removes a specified child node from the DOM. Requires a reference to both the parent and child.
    -   **Syntax**: `parentNode.removeChild(childNode)`
-   **`innerHTML = ''` or `textContent = ''`**: Setting these properties to an empty string effectively removes all child elements. `textContent` is generally faster for this purpose.
-   **`replaceChildren()`**: `container.replaceChildren();` will remove all existing children.

### Working with `classList` (`add`, `remove`, `toggle`)

The `Element.classList` property provides a `DOMTokenList` object for convenient manipulation of an element's class attributes.

-   **`add(String [, String, ...])`**: Adds one or more specified class values.
    -   **Example**: `element.classList.add("new-class", "another-class");`
-   **`remove(String [, String, ...])`**: Removes one or more specified class values.
    -   **Example**: `element.classList.remove("old-class");`
-   **`toggle(String [, force])`**: Toggles the presence of a class value.
    -   If `force` is omitted: adds the class if not present (returns `true`), removes it if present (returns `false`).
    -   If `force` is `true`: adds the class.
    -   If `force` is `false`: removes the class.
    -   **Example**: `element.classList.toggle("visible");`

### `setAttribute`, `getAttribute`

These methods are used to manage attributes on HTML elements.

-   **`setAttribute(name, value)`**: Sets the value of an attribute on a specified element. If the attribute exists, its value is updated; otherwise, a new attribute is added.
    -   **Syntax**: `element.setAttribute(name, value)`
    -   `name`: The attribute name (e.g., `'class'`, `'id'`, `'src'`).
    -   `value`: The value to assign.
-   **`getAttribute(attributeName)`**: Returns the value of a specified attribute on the element.
    -   **Syntax**: `element.getAttribute(attributeName)`
    -   **Return Value**: A string of the attribute's value, or `null` if the attribute does not exist.

### `dataset` Usage

The `HTMLElement.dataset` property provides access to custom data attributes (`data-*`) on an element. It returns a `DOMStringMap` object.

-   **HTML**: `<div data-id="123" data-user-name="John Doe"></div>`
-   **JavaScript Access**:
    -   Reading: `element.dataset.id`, `element.dataset.userName` (camelCase conversion).
    -   Setting: `element.dataset.newAttribute = 'some value';`
    -   Removing: `delete element.dataset.newAttribute;`
-   **Use Case**: Storing small pieces of custom data directly on HTML elements.

## 3. Events

### `addEventListener`

The `EventTarget.addEventListener()` method attaches an event handler to the specified element.

-   **Syntax**: `element.addEventListener(type, listener, options)`
-   **`type`**: A case-sensitive string representing the event type to listen for (e.g., `'click'`, `'input'`).
-   **`listener`**: The function to be called when the event occurs.
-   **`options` (optional)**: An object specifying characteristics about the event listener (e.g., `once`, `passive`, `capture`).

### Event Types (click, input, keyup, etc.)

Common event types include:
-   **Mouse Events**: `click`, `dblclick`, `mousedown`, `mouseup`, `mousemove`, `mouseover`, `mouseout`, `mouseenter`, `mouseleave`.
-   **Keyboard Events**: `keydown`, `keypress`, `keyup`.
-   **Form Events**: `submit`, `input`, `change`, `focus`, `blur`.
-   **Document/Window Events**: `load`, `unload`, `resize`, `scroll`, `DOMContentLoaded`.

### Event Object (`event.target`, `event.currentTarget`)

When an event occurs, an `Event` object is passed to the event listener function.
-   **`event.target`**: The actual element on which the event *originally occurred*. This can be a descendant of the element the listener is attached to.
-   **`event.currentTarget`**: The element to which the event listener was *attached*. This is the element on which `addEventListener` was called.

### `preventDefault`, `stopPropagation`

These methods control the default behavior and propagation of events.

-   **`Event.preventDefault()`**: Prevents the browser's default action for a given event.
    -   **Example**: Preventing a form from submitting when a button is clicked, or preventing a link from navigating.
-   **`Event.stopPropagation()`**: Prevents further propagation of the current event in the capturing and bubbling phases.
    -   **Example**: If a button inside a `div` is clicked, and both have click listeners, `stopPropagation()` on the button's click will prevent the `div`'s click listener from firing.



## 6. Local Storage



Local Storage allows web applications to store data persistently in the browser, with no expiration date. The data is stored as key/value pairs.



### `setItem`, `getItem`, `removeItem`, `clear`



-   **`localStorage.setItem(key, value)`**: Stores a key-value pair. Both `key` and `value` must be strings.

    -   **Example**: `localStorage.setItem('username', 'JohnDoe');`

-   **`localStorage.getItem(key)`**: Retrieves the value associated with the given key.

    -   **Example**: `let username = localStorage.getItem('username');` (returns `'JohnDoe'` or `null` if not found).

-   **`localStorage.removeItem(key)`**: Removes the key-value pair with the specified key.

    -   **Example**: `localStorage.removeItem('username');`

-   **`localStorage.clear()`**: Removes all key-value pairs from local storage for the current domain.

    -   **Example**: `localStorage.clear();`



### Storing Objects using JSON



Local Storage only stores strings. To store JavaScript objects, you need to convert them to JSON strings before storing and parse them back when retrieving.



-   **Storing an object**:

    ```javascript

    const userSettings = { theme: 'dark', notifications: true };

    localStorage.setItem('userSettings', JSON.stringify(userSettings));

    ```

-   **Retrieving an object**:

    ```javascript

    const storedSettings = localStorage.getItem('userSettings');

    const userSettings = storedSettings ? JSON.parse(storedSettings) : null;

    console.log(userSettings.theme); // 'dark'

    ```



## Method only guide

-   `getElementById`
-   `getElementsByClassName`
-   `getElementsByTagName`
-   `querySelector`
-   `querySelectorAll`
-   `createElement`
-   `append`
-   `prepend`
-   `appendChild`
-   `insertBefore`
-   `remove`
-   `removeChild`
-   `classList.add`
-   `classList.remove`
-   `classList.toggle`
-   `setAttribute`
-   `getAttribute`
-   `dataset`
-   `addEventListener`
-   `preventDefault`
-   `stopPropagation`
-   `localStorage.setItem`
-   `localStorage.getItem`
-   `localStorage.removeItem`
-   `localStorage.clear`
-   `JSON.stringify`
-   `JSON.parse`
