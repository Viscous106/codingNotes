# JavaScript Asynchronous Programming: A Comprehensive Guide

## 1. The Foundation: Synchronous vs. Asynchronous

JavaScript is single-threaded (it has one call stack). It can only do one thing at a time.

- **Synchronous**: Code executes line-by-line. If one line takes a long time (blocking), everything else waits.
- **Asynchronous**: Code initiates a task (like a timer or API call) and moves on immediately. The task runs in the background (handled by the browser/Node runtime) and notifies the main thread when finished.

### The Event Loop (How it actually works)

This is the missing "why" behind async code.

- **Call Stack**: Where code executes.
- **Web APIs**: Where async tasks (DOM, setTimeOut, Fetch) wait.
- **Queue**:
    - **Microtask Queue**: High priority (Promises, queueMicrotask).
    - **Callback (Task) Queue**: Low priority (setTimeout, setInterval).
- **Rule**: The Event Loop checks: "Is the Stack empty? If yes, run Microtasks first. If Microtasks are empty, run the Callback Queue."

## 2. Callbacks (The Old Way)

Passing a function into another function to be called later.

### The Problem: Inversion of Control & Callback Hell

- **Callback Hell**: excessive nesting (Pyramid of Doom).
- **Inversion of Control**: You hand your code execution over to a third-party function (like `setTimeout` or an external library), trusting them to call it correctly (not too early, not twice).

```javascript
// The "Pyramid of Doom"
getData(1, (data1) => {
    getData(2, (data2) => {
        getData(3, (data3) => {
            console.log("All done");
        });
    });
});
```

## 3. Promises (The Solution)

A Promise is an object representing the eventual completion (or failure) of an asynchronous operation.

### The 3 States:

- **Pending**: Initial state, neither fulfilled nor rejected.
- **Fulfilled (Resolved)**: Operation completed successfully.
- **Rejected**: Operation failed.

### Correction on your `getData` function

Your original code mixed callbacks (`getNextData`) with Promises. This is an anti-pattern. Promises are designed to return values, not accept next-step callbacks.

#### Better Pattern:
```javascript
function getData(dataID) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            // Simulate 80% success rate
            const success = Math.random() > 0.2; 
            if (success) {
                console.log(`Fetched Data: ${dataID}`);
                resolve("Success");
            } else {
                reject(new Error(`Failed to fetch ${dataID}`));
            }
        }, 2000);
    });
}
```

### Promise Chaining (Solving Callback Hell)

We return a new Promise from the `.then()` handler to keep the chain flat.
```javascript
getData(1)
    .then((res) => {
        return getData(2); // Return the next promise
    })
    .then((res) => {
        return getData(3);
    })
    .then((res) => {
        console.log("All 3 fetched sequentially");
    })
    .catch((err) => {
        // Catches errors from ANY step in the chain
        console.error("Something went wrong:", err);
    })
    .finally(() => {
        console.log("Cleanup (runs regardless of success/failure)");
    });
```

## 4. Promise Combinators (Parallel Execution)

Missing from your notes. Sometimes you don't need Data 1 before Data 2. You want them both now.

| Method                    | Behavior                                             | Use Case                       |
|---------------------------|------------------------------------------------------|--------------------------------|
| `Promise.all([p1, p2])`   | Runs all in parallel. Fails if any fail.             | You need all data to proceed.  |
| `Promise.allSettled([p1, p2])` | Runs all. Returns results for all, even if some fail. | You want to see what worked and what didn't. |
| `Promise.race([p1, p2])`  | Returns result of the first one to settle.           | Timeouts (Api vs 5s Timer).    |

### Example: Parallel Fetching
```javascript
const p1 = getData(1);
const p2 = getData(2);
const p3 = getData(3);

// This takes ~2 seconds total (concurrent), not 6 seconds (sequential)
Promise.all([p1, p2, p3])
    .then((results) => {
        console.log("All data received:", results);
    })
    .catch((err) => {
        console.error("One failed, so all failed:", err);
    });
```

## 5. Async / Await (Modern Syntax)

Syntactic sugar over Promises. It makes async code look and behave like synchronous code.

- `async`: Wraps the function return in a Promise.
- `await`: Pauses the execution of that specific function (not the whole browser) until the Promise resolves.

### Professional Fetch Example:
```javascript
const getFacts = async () => {
    // ALWAYS use try-catch with async/await
    try {
        console.log("Fetching...");
        
        // The execution pauses here at line 6 until fetch is done
        let response = await fetch("https://cat-fact.herokuapp.com/facts");
        
        // Check if API returned a 404 or 500 error (fetch doesn't reject on 404)
        if (!response.ok) {
            throw new Error(`HTTP Error! status: ${response.status}`);
        }

        let data = await response.json(); // Wait for parsing
        console.log(data);
        
    } catch (error) {
        // Handles network errors OR the error we threw above
        console.error("Error handling data:", error.message);
    }
};
```

## 6. Important Interview Concept: Execution Order

Combine your knowledge of the Event Loop (Microtasks) to predict this output.
```javascript
console.log("1: Script Start");

setTimeout(() => {
    console.log("2: SetTimeout");
}, 0);

Promise.resolve().then(() => {
    console.log("3: Promise 1");
}).then(() => {
    console.log("4: Promise 2");
});

console.log("5: Script End");

// OUTPUT ORDER:
// 1: Script Start
// 5: Script End      (Synchronous code finishes first)
// 3: Promise 1       (Microtasks run before Macrotasks)
// 4: Promise 2       (Still processing Microtask queue)
// 2: SetTimeout      (Callback queue runs last)
```
