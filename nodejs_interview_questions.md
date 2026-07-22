# Top 20 Node.js Interview Questions & Answers (with Bangla Translation)

This guide contains 20 comprehensive, industry-standard interview questions on Node.js, covering core architecture, libuv, event loop, streams, concurrency, Express middleware, security, and performance scaling. Each question has a detailed answer in English followed by a complete Bangla translation.

---

## Table of Contents
1. What is Node.js and how does it work?
2. What is the Event Loop in Node.js and what are its phases?
3. Difference between `process.nextTick()`, `setImmediate()`, and `setTimeout()`
4. Synchronous (Blocking) vs Asynchronous (Non-Blocking) I/O
5. How Node.js handles concurrency despite being single-threaded
6. What is `libuv` and its role in Node.js?
7. What are Streams in Node.js and their types?
8. Difference between Buffer and Stream
9. What are Express.js Middleware functions and how do they work?
10. How to handle Uncaught Exceptions and Unhandled Promise Rejections
11. `cluster` module vs `worker_threads`
12. What is `EventEmitter` and how does it work?
13. How Garbage Collection and Memory Management work in V8
14. Common causes of Memory Leaks in Node.js and how to debug them
15. Managing Environment Variables and Secret Configuration
16. Authentication vs Authorization and implementing JWT
17. Purpose of `package-lock.json` and semantic versioning
18. Managing Database Connection Pooling
19. What is CORS and how do you configure it in Express?
20. How to scale a Node.js application for production traffic

---

### **Q1: What is Node.js and how does it work? / Node.js কী এবং এটি কীভাবে কাজ করে?**

**Answer (English):**
Node.js is an open-source, cross-platform JavaScript runtime environment built on Google Chrome's V8 JavaScript engine. It allows developers to run JavaScript code on the server side outside of a web browser.
*   **How it works:** Node.js uses a **single-threaded, event-driven, non-blocking I/O architecture**. Instead of spawning a new thread for every client request (like traditional servers like Apache), Node.js registers requests with the event loop and delegates heavy I/O operations (file reading, network calls, database queries) to C++ worker threads via `libuv`. Once the task is complete, the callback is returned to the main thread to send the response.

**অনুবাদ (Bangla Translation):**
Node.js হলো গুগল ক্রোম-এর V8 জাভাস্ক্রিপ্ট ইঞ্জিনের ওপর তৈরি একটি ওপেন-সোর্স, ক্রস-প্ল্যাটফর্ম জাভাস্ক্রিপ্ট রানটাইম এনভায়রনমেন্ট। এটি ব্রাউজারের বাইরে সার্ভার-সাইডে জাভাস্ক্রিপ্ট কোড চালানোর সুবিধা দেয়।
*   **কীভাবে কাজ করে:** Node.js একটি **সিঙ্গেল-থ্রেডেড, ইভেন্ট-ড্রিভেন এবং নন-ব্লকিং I/O আর্কিটেকচার** অনুসরণ করে। প্রথাগত সার্ভারের মতো প্রতি রিকোয়েস্টে নতুন থ্রেড তৈরি না করে, Node.js সমস্ত রিকোয়েস্ট ইভেন্ট লুপে জমা করে এবং ভারী কাজের (যেমন ফাইল রিড, নেটওয়ার্ক কাল, ডাটাবেজ কোয়েরি) ভার `libuv`-এর ব্যাকগ্রাউন্ড থ্রেড পুলে পাঠিয়ে দেয়। কাজ শেষ হলে কলব্যাকের মাধ্যমে রেসপন্স ফেরত পাঠায়।

---

### **Q2: What is the Event Loop in Node.js and what are its phases? / Node.js-এ Event Loop কী এবং এর ধাপসমূহ কী কী?**

**Answer (English):**
The Event Loop is the core mechanism that allows Node.js to perform non-blocking I/O operations despite JavaScript being single-threaded. It constantly checks the call stack and executes queued callbacks from different queues.
*   **6 Phases of the Node.js Event Loop (executed in order):**
    1.  **Timers:** Executes callbacks scheduled by `setTimeout()` and `setInterval()`.
    2.  **Pending Callbacks:** Executes I/O callbacks deferred to the next loop iteration (e.g., TCP errors).
    3.  **Idle, Prepare:** Used internally by Node.js.
    4.  **Poll:** Retrieves new I/O events and executes I/O-related callbacks (e.g., file reads, network connections).
    5.  **Check:** Executes callbacks scheduled by `setImmediate()`.
    6.  **Close Callbacks:** Executes socket/handle close callbacks (e.g., `socket.on('close')`).

**অনুবাদ (Bangla Translation):**
ইভেন্ট লুপ (Event Loop) হলো Node.js-এর মূল মেকানিজম যা সিঙ্গেল-থ্রেডেড হওয়া সত্ত্বেও নন-ব্লকিং I/O কাজ পরিচালনা করতে সাহায্য করে। এটি অনবরত কল স্ট্যাক পর্যবেক্ষণ করে এবং বিভিন্ন কিউ (Queue) থেকে কলব্যাক নিয়ে রান করায়।
*   **Event Loop-এর ৬টি ধাপ (পর্যায়ক্রমে চলে):**
    1.  **Timers Phase:** `setTimeout()` এবং `setInterval()`-এর কলব্যাক রান করায়।
    2.  **Pending Callbacks Phase:** বিলম্বিত হওয়া সিস্টেম I/O এরর বা কলব্যাক চালায়।
    3.  **Idle, Prepare Phase:** Node.js ইন্টারনাল ব্যবহারের জন্য রাখে।
    4.  **Poll Phase:** নতুন I/O ইভেন্ট গ্রহণ করে এবং ফাইল রিড বা নেটওয়ার্ক কানেকশনের কলব্যাক প্রসেস করে।
    5.  **Check Phase:** `setImmediate()` দিয়ে শিডিউল করা কলব্যাক চালায়।
    6.  **Close Callbacks Phase:** কানেকশন ক্লোজ ইভেন্ট (যেমন `socket.on('close')`) হ্যান্ডেল করে।

---

### **Q3: What is the difference between `process.nextTick()`, `setImmediate()`, and `setTimeout()`? / `process.nextTick()`, `setImmediate()`, এবং `setTimeout()` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`process.nextTick()`:** Executes immediately after the currently running script operation completes, **before** the event loop continues to any phase. It has the highest priority (Microtask-like behavior).
*   **`setImmediate()`:** Executes in the **Check phase** of the event loop right after the Poll phase completes.
*   **`setTimeout(fn, delay)`:** Executes in the **Timers phase** after the specified minimum delay (ms) threshold has passed.

| Method | Phase / Execution Timing | Priority |
| :--- | :--- | :--- |
| `process.nextTick()` | Immediately after current operation (Before Event Loop continues) | Highest |
| `setImmediate()` | Check Phase (After Poll phase) | Medium |
| `setTimeout()` | Timers Phase (After delay threshold) | Normal |

**অনুবাদ (Bangla Translation):**
*   **`process.nextTick()`:** বর্তমান কোডের কাজ শেষ হওয়া মাত্রই এবং ইভেন্ট লুপের যেকোনো ফেজে যাওয়ার **আগেই** রান করে। এর অগ্রাধিকার সবচেয়ে বেশি।
*   **`setImmediate()`:** ইভেন্ট লুপের **Check ফেজে** (Poll ফেজ শেষ হওয়ার পর) কলব্যাক পরিচালনা করে।
*   **`setTimeout(fn, delay)`:** ইভেন্ট লুপের **Timers ফেজে** নির্দিষ্ট সময় (ms) পার হওয়ার পর রান করে।

---

### **Q4: What is the difference between synchronous (blocking) and asynchronous (non-blocking) functions in Node.js? / Node.js-এ Synchronous (Blocking) এবং Asynchronous (Non-Blocking) ফাংশনের পার্থক্য কী?**

**Answer (English):**
*   **Synchronous (Blocking):** Execution of additional JavaScript in the Node.js process is paused until a non-JavaScript operation completes. E.g., `fs.readFileSync()`. It blocks the main thread, making the app unresponsive to other clients.
*   **Asynchronous (Non-Blocking):** The operation is initiated, and control returns immediately to the event loop. Node.js continues executing subsequent lines of code while the task finishes in the background. E.g., `fs.readFile()` or `fs.promises.readFile()`.

**অনুবাদ (Bangla Translation):**
*   **Synchronous (Blocking):** এই মেথড চলাকালীন বর্তমান কাজ শেষ না হওয়া পর্যন্ত পরবর্তী কোড রান হওয়া সম্পূর্ণ বন্ধ (Block) থাকে। যেমন- `fs.readFileSync()`। এটি মেইন থ্রেড থামিয়ে দেওয়ায় অন্য ইউজাররা ল্যাগ অনুভব করেন।
*   **Asynchronous (Non-Blocking):** এটি ব্যাকগ্রাউন্ডে কাজ শুরু করে দিয়ে সাথে সাথে ইভেন্ট লুপে কন্ট্রোল ফিরিয়ে দেয়, ফলে পরবর্তী লাইনের কোড রুক্সে ছাড়া চলতে থাকে। কাজ শেষ হলে কলব্যাক বা প্রমিজ রেজাল্ট দেয়। যেমন- `fs.readFile()`।

---

### **Q5: How does Node.js handle concurrency if it is single-threaded? / সিঙ্গেল-থ্রেডেড হওয়া সত্ত্বেও Node.js কীভাবে Concurrency (একসাথে অনেক কাজ) হ্যান্ডেল করে?**

**Answer (English):**
Node.js handles concurrency through **Delegation** using the Event Loop and `libuv` Worker Thread Pool.
*   The main JavaScript execution thread never blocks on I/O.
*   When an asynchronous task (like a database call, file read, or HTTP fetch) is triggered, Node.js offloads the task to the underlying operating system kernel (which supports OS-level async threads) or to the 4 default C++ worker threads managed by `libuv`.
*   When the operation completes, the background thread notifies the Event Loop, placing the callback into the queue for execution on the main thread.

**অনুবাদ (Bangla Translation):**
Node.js ইভেন্ট লুপ এবং `libuv` ওয়্যার্কার থ্রেড পুলের মাধ্যমে **কাজ ভাগ করে (Delegation)** একযোগে অসংখ্য ক্লায়েন্টের কাজ হ্যান্ডেল করে।
*   মেইন জাভাস্ক্রিপ্ট থ্রেড কোনো I/O কাজের জন্য অপেক্ষা করে না।
*   যেকোনো ভারী ফাইল বা ডাটাবেজ কাজ আসলে Node.js তা অপারেটিং সিস্টেমের নেটিভ কার্নেল বা `libuv`-এর ৪টি C++ ব্যাকগ্রাউন্ড থ্রেডে পাঠিয়ে দেয়।
*   ব্যাকগ্রাউন্ডে কাজ শেষ হলে থ্রেড ইভেন্ট লুপকে অ্যালার্ট করে এবং ইভেন্ট লুপের মাধ্যমে মেইন থ্রেড কলব্যাকটি প্রসেস করে রেসপন্স ডিশপ্যাচ করে।

---

### **Q6: What is `libuv` and what role does it play in Node.js? / `libuv` কী এবং Node.js-এ এর ভূমিকা কী?**

**Answer (English):**
`libuv` is a multi-platform C library designed specifically for Node.js to handle asynchronous I/O operations.
*   **Role of `libuv`:**
    1.  Implements the Node.js **Event Loop**.
    2.  Manages the **Worker Thread Pool** (default 4 threads, configurable via `UV_THREADPOOL_SIZE`).
    3.  Provides cross-platform support for file system operations, DNS lookups, child processes, timers, and network sockets across Linux, macOS, and Windows.

**অনুবাদ (Bangla Translation):**
`libuv` হলো একটি মাল্টি-প্ল্যাটফর্ম C লাইব্রেরি যা মূলত Node.js-কে অ্যাসিনক্রোনাস I/O সাপোর্ট দেওয়ার জন্য তৈরি করা হয়েছিল।
*   **`libuv`-এর ভূমিকা:**
    1.  Node.js-এর **Event Loop** পরিচালনা করে।
    2.  **Worker Thread Pool** ম্যানেজ করে (ডিফল্ট ৪টি থ্রেড থাকে, যা `UV_THREADPOOL_SIZE` দিয়ে বাড়ানো যায়)।
    3.  Linux, macOS এবং Windows-এর ফাইল সিস্টেম, নেটওয়ার্ক সকেট ও ডিএনএস লুকআপের কাজের ইউনিভার্সাল নেটিভ সাপোর্ট নিশ্চিত করে।

---

### **Q7: What are Streams in Node.js and what are the different types of streams? / Node.js-এ Streams কী এবং এদের প্রকারভেদসমূহ কী কী?**

**Answer (English):**
Streams are objects that let you read data from a source or write data to a destination continuously in chunks, without loading the entire dataset into memory all at once.
*   **4 Main Types of Streams:**
    1.  **Readable:** Stream from which data can be read (e.g., `fs.createReadStream()`, HTTP request).
    2.  **Writable:** Stream to which data can be written (e.g., `fs.createWriteStream()`, HTTP response).
    3.  **Duplex:** Stream that is both Readable and Writable (e.g., TCP net socket).
    4.  **Transform:** Duplex stream where the output is computed based on the input data (e.g., `zlib.createGzip()` for file compression).

**অনুবাদ (Bangla Translation):**
স্ট্রিম (Streams) হলো এমন অবজেক্ট যা মেমোরিতে একবারে পুরো ডাটা লোড না করে ছোট ছোট চাঙ্ক (Chunk) বা টুকরো আকারে অনবরত ডাটা রিড বা রাইট করতে সাহায্য করে।
*   **স্ট্রিমের ৪টি প্রধান প্রকারভেদ:**
    1.  **Readable:** যেখান থেকে ডাটা পড়া যায় (যেমন- `fs.createReadStream()`, HTTP রিকোয়েস্ট)।
    2.  **Writable:** যেখানে ডাটা লেখা হয় (যেমন- `fs.createWriteStream()`, HTTP রেসপন্স)।
    3.  **Duplex:** যা একই সাথে পড়তে ও লিখতে পারে (যেমন- TCP সকেট)।
    4.  **Transform:** ডুপ্লেক্স স্ট্রিম যা ইনপুট ডাটাকে মডিফাই করে আউটপুট দেয় (যেমন- ফাইল জিপ বা কমপ্রেস করার `zlib.createGzip()`)।

---

### **Q8: What is the difference between Buffer and Stream in Node.js? / Node.js-এ Buffer এবং Stream এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Buffer:** A temporary fixed-size chunk of memory allocated outside the V8 heap used to hold raw binary data. Data must be loaded completely into the buffer before processing.
*   **Stream:** A continuous sequence of data chunks moving over time. It processes data piece by piece as it arrives, consuming significantly less RAM for large files.

| Feature | Buffer | Stream |
| :--- | :--- | :--- |
| **Data Handling** | Loads whole data into memory before processing. | Processes data piece-by-piece in chunks. |
| **Memory Usage** | High RAM consumption for large files. | Very low and constant RAM consumption. |
| **Limit** | Limited by maximum buffer size (~4GB). | Handles files of arbitrary size. |

**অনুবাদ (Bangla Translation):**
*   **Buffer:** এটি V8 মেমোরির বাইরে একটি নির্দিষ্ট ফিক্সড সাইজের বাইনারি ডাটা হোল্ডার। কোনো প্রসেসিং করার আগে পুরো ফাইলকে বাফারে লোড করতে হয়।
*   **Stream:** এটি ধারাবাহিক ডাটা ফ্লো। এটি পুরো ফাইল না নামিয়ে ছোট ছোট অংশে প্রসেস করে, যা র‍্যামের (RAM) খরচ অনেক কমায়।

| বৈশিষ্ট্য | Buffer | Stream |
| :--- | :--- | :--- |
| **ডাটা প্রসেসিং** | পুরো ডাটা মেমোরিতে আসার পর কাজ শুরু করে। | ডাটা আসা মাত্রই টুকরো টুকরো করে কাজ শুরু করে। |
| **মেমোরি খরচ** | বড় ফাইলের জন্য মেমোরি খরচ অনেক বেশি। | মেমোরি খরচ খুব কম ও স্থিতিশীল। |

---

### **Q9: What are Middleware functions in Express.js and how do they work? / Express.js-এ Middleware ফাংশন কী এবং এগুলো কীভাবে কাজ করে?**

**Answer (English):**
Middleware functions are functions that have access to the Request object (`req`), Response object (`res`), and the `next` middleware function in the application’s request-response cycle.
*   **Tasks performed by middleware:**
    1.  Execute custom code (logging, CORS check).
    2.  Make changes to request and response objects (parsing JSON body, attaching user session).
    3.  End the request-response cycle (`res.send()`).
    4.  Call `next()` to pass control to the subsequent middleware function.

```javascript
app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);
  next(); // Pass to next middleware
});
```

**অনুবাদ (Bangla Translation):**
মিডলওয়্যার (Middleware) হলো এমন ফাংশন যার কাছে রিকোয়েস্ট অবজেক্ট (`req`), রেসপন্স অবজেক্ট (`res`) এবং পরবর্তী মিডলওয়্যারে যাওয়ার নির্দেশক `next` ফাংশনের অ্যাক্সেস থাকে।
*   **মিডলওয়্যারের কাজসমূহ:**
    1.  কাস্টম কোড রান করা (যেমন- অ্যাক্টিভিটি লগ রাখা, সিকিউরিটি চেক)।
    2.  `req` এবং `res` অবজেক্ট পরিবর্তন করা (যেমন- JSON বডি পার্স করা, অথেন্টিকেশন চেক করা)।
    3.  রিকোয়েস্ট শেষ করা (`res.json()`)।
    4.  পরবর্তী মিডলওয়্যারে যাওয়ার জন্য `next()` কল করা।

---

### **Q10: How do you handle Uncaught Exceptions and Unhandled Promise Rejections in Node.js? / Node.js-এ Uncaught Exceptions এবং Unhandled Promise Rejections কীভাবে হ্যান্ডেল করবেন?**

**Answer (English):**
Uncaught exceptions or unhandled promise rejections can crash a Node.js process if not managed properly.
*   **Handling Uncaught Exceptions:**
    ```javascript
    process.on('uncaughtException', (err) => {
      console.error('Uncaught Exception thrown:', err);
      // Perform graceful shutdown / cleanup database connections
      process.exit(1);
    });
    ```
*   **Handling Unhandled Rejections:**
    ```javascript
    process.on('unhandledRejection', (reason, promise) => {
      console.error('Unhandled Rejection at:', promise, 'reason:', reason);
    });
    ```
*   *Best Practice:* Use process management tools like **PM2** to auto-restart the application if a process exits after cleanup.

**অনুবাদ (Bangla Translation):**
হ্যান্ডেল না করা এরর বা প্রমিজ রিজেকশন হ্যান্ডেল না করলে পুরো Node.js প্রসেস বন্ধ বা ক্র্যাশ হয়ে যায়।
*   **Uncaught Exception হ্যান্ডলিং:**
    ```javascript
    process.on('uncaughtException', (err) => {
      console.error('গুরুতর এরর ঘটেছে:', err);
      // ডেটাবেজ কানেকশন ক্লোজ করে নিরাপদ এক্সিট করা
      process.exit(1);
    });
    ```
*   **Unhandled Rejection হ্যান্ডলিং:**
    ```javascript
    process.on('unhandledRejection', (reason, promise) => {
      console.error('হ্যান্ডেল না করা প্রমিজ এরর:', reason);
    });
    ```
*   *আদর্শ নিয়ম:* প্রোডাকশনে **PM2** প্রসেস ম্যানেজার ব্যবহার করা যা ক্র্যাশ হলে অটোমেটিক অ্যাপ রিস্টার্ট করায়।

---

### **Q11: What is the difference between `cluster` module and `worker_threads` in Node.js? / Node.js-এ `cluster` মডিউল এবং `worker_threads` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`cluster` Module:** Spawns multiple **separate Node.js processes** (OS-level processes) running on different CPU cores, sharing the same server port via a master process. Each process has its own V8 instance, memory, and event loop. Best for scaling web servers across CPU cores.
*   **`worker_threads` Module:** Spawns multiple **threads within a single process**. Threads share the same process memory space (via `ArrayBuffer`) and V8 instance. Best for offloading CPU-heavy tasks (like cryptography, image resizing) without starting full new processes.

**অনুবাদ (Bangla Translation):**
*   **`cluster` মডিউল:** এটি একই পোর্টে লিসেন করে প্রতিটি সিপিইউ কোরের (CPU Core) জন্য আলাদা **Node.js প্রসেস** চালু করে। প্রতিটি প্রসেসের নিজস্ব V8 মেমোরি ও ইভেন্ট লুপ থাকে। এটি ওয়েব সার্ভার স্কেল করতে সেরা।
*   **`worker_threads` মডিউল:** এটি একটিমাত্র প্রসেসের ভেতরে একাধিক **থ্রেড** তৈরি করে, যারা নিজেদের মধ্যে মেমোরি শেয়ার করতে পারে। এটি সিপಿಯು-ভারী কাজ (যেমন- ক্রিপ্টোগ্রাফি বা ফাইল প্রসেসিং) থ্রেডে পাঠিয়ে করার জন্য বেস্ট।

---

### **Q12: What is `EventEmitter` and how does it work? / Node.js-এ `EventEmitter` কী এবং এটি কীভাবে কাজ করে?**

**Answer (English):**
`EventEmitter` is a core Node.js module that facilitates event-driven programming. It allows objects to emit named events that trigger registered listener functions.
*   **Example Syntax:**
    ```javascript
    const EventEmitter = require('events');
    const myEmitter = new EventEmitter();

    // Register listener
    myEmitter.on('userLoggedIn', (user) => {
      console.log(`Welcome ${user.name}`);
    });

    // Emit event
    myEmitter.emit('userLoggedIn', { name: 'Rohit' });
    ```

**অনুবাদ (Bangla Translation):**
`EventEmitter` হলো Node.js-এর একটি বিল্ট-ইন মডিউল যা ইভেন্ট-ড্রিভেন কোড লিখতে সাহায্য করে। এর মাধ্যমে নির্দিষ্ট নামে ইভেন্ট ফায়ার (emit) করা যায় এবং ওই ইভেন্টের সাথে লিসেনার ফাংশন জুড়ে দেওয়া যায়।
*   **সিনট্যাক্স উদাহরণ:**
    ```javascript
    const EventEmitter = require('events');
    const myEmitter = new EventEmitter();

    // লিসেনার রেজিস্টার করা
    myEmitter.on('userLoggedIn', (user) => {
      console.log(`স্বাগতম ${user.name}`);
    });

    // ইভেন্ট ফায়ার করা
    myEmitter.emit('userLoggedIn', { name: 'Rohit' });
    ```

---

### **Q13: How does Garbage Collection and Memory Management work in the V8 engine? / V8 ইঞ্জিনে Garbage Collection এবং মেমোরি ম্যানেজমেন্ট কীভাবে কাজ করে?**

**Answer (English):**
V8 divides heap memory into two main generations:
1.  **Nursery / Young Generation:** Holds newly allocated short-lived objects. Uses a fast algorithm called **Scavenger (Cheney's Algorithm)** to clear dead objects. Surviving objects are promoted to the Old Generation.
2.  **Old Generation:** Holds long-lived objects. Managed by the **Mark-Sweep-Compact** algorithm:
    *   **Marking:** Identifies all reachable objects from global roots.
    *   **Sweeping:** Deallocates memory of unreachable objects.
    *   **Compacting:** Defragments memory to avoid fragmentation.

**অনুবাদ (Bangla Translation):**
V8 ইঞ্জিন হিপ মেমোরিকে প্রধানত দুটি যুগে ভাগ করে মেমোরি ম্যানেজ করে:
1.  **Young Generation (তরুণ প্রজন্ম):** নতুন তৈরি হওয়া সংক্ষিপ্ত মেয়াদের অবজেক্টগুলোকে রাখা হয়। এটি **Scavenger** অ্যালগরিদম দিয়ে খুব দ্রুত অব্যবহৃত অবজেক্ট মুছে ফেলে। টিকে যাওয়া অবজেক্টগুলোকে Old Generation-এ পাঠিয়ে দেওয়া হয়।
2.  **Old Generation (পুরাতন প্রজন্ম):** দীর্ঘমেয়াদী অবজেক্ট ধারণ করে। এটি **Mark-Sweep-Compact** অ্যালগরিদম ব্যবহার করে গ্লোবাল রুট থেকে অকেজো অবজেক্টগুলো চিহ্নিত (Mark) করে মেমোরি থেকে ঝেড়ে (Sweep) ফেলে এবং ফ্র্যাগমেন্টেশন রোধে কমপ্যাক্ট করে।

---

### **Q14: What are common causes of Memory Leaks in Node.js and how do you debug them? / Node.js-এ মেমোরি লিকের প্রধান কারণসমূহ কী কী এবং কীভাবে এগুলো ডিবাগ করবেন?**

**Answer (English):**
*   **Common Causes:**
    1.  Global variables (`accidentalGlobal = data`).
    2.  Uncleared event listeners or subscriptions (`emitter.on()` without removal).
    3.  Closures retaining references to outer scope objects.
    4.  Uncleared `setInterval()` timers.
*   **Debugging Techniques:**
    1.  Take Heap Snapshots using **Chrome DevTools** (`node --inspect index.js`).
    2.  Compare heap memory usage before and after load tests.
    3.  Use tools like **Clinic.js** or `process.memoryUsage()`.

**অনুবাদ (Bangla Translation):**
*   **মেমোরি লিকের প্রধান কারণসমূহ:**
    1.  ভুলবশত গ্লোবাল ভ্যারিয়েবল ডিক্লেয়ার করা।
    2.  ইভেন্ট লিসেনার রিমুভ না করে খোলা রাখা (`emitter.on()`)।
    3.  ক্লোজারের মাধ্যমে বাইরের মেমোরি ধরে রাখা।
    4.  `setInterval()` বন্ধ বা ক্লিয়ার না করা।
*   **ডিবাগ করার উপায়:**
    1.  `node --inspect` দিয়ে **Chrome DevTools**-এ Heap Snapshot তুলনা করা।
    2.  **Clinic.js** বা `process.memoryUsage()` দিয়ে মেমোরি গ্রাফ পর্যবেক্ষণ করা।

---

### **Q15: How do you manage Environment Variables and Secret Configuration in Node.js? / Node.js-এ Environment Variables এবং গোপন কনফিগারেশন কীভাবে ম্যানেজ করবেন?**

**Answer (English):**
1.  Use `.env` files locally paired with the `dotenv` package (`require('dotenv').config()`) or Node.js native `--env-file=.env` flag (Node v20.6+).
2.  Access configuration parameters via `process.env.VARIABLE_NAME`.
3.  **Security Rule:** Never commit `.env` files to Git (add to `.gitignore`). In production environments (AWS, Docker, Kubernetes), inject secrets via container environment configurations or Secret Managers (AWS Secrets Manager, HashiCorp Vault).

**অনুবাদ (Bangla Translation):**
1.  লোকালি `.env` ফাইল এবং `dotenv` প্যাকেজ (`require('dotenv').config()`) অথবা Node v20.6+ এর নেটিভ `--env-file` ফ্লাগ ব্যবহার করে।
2.  কোডে `process.env.VARIABLE_NAME` দিয়ে মান রিড করা।
3.  **নিরাপত্তা নিয়ম:** `.env` ফাইল কখনো Git-এ পুশ না করা (`.gitignore`-এ রাখা)। প্রোডাকশনে Docker/K8s বা AWS Secrets Manager দিয়ে মেমোরিতে সিক্রেট পুশ করা।

---

### **Q16: What is the difference between Authentication and Authorization? How do you implement JWT authentication in Node.js? / Authentication এবং Authorization-এর পার্থক্য কী? Node.js-এ কীভাবে JWT দিয়ে অথেন্টিকেশন ইমপ্লিমেন্ট করবেন?**

**Answer (English):**
*   **Authentication (Who are you?):** Verifying user identity (e.g., login with email/password).
*   **Authorization (What can you do?):** Checking user permissions to access a specific resource (e.g., Admin vs User roles).
*   **JWT Implementation Flow:**
    1.  User logs in -> Server verifies credentials -> Server signs a JSON Web Token using `jsonwebtoken.sign(payload, secretKey, { expiresIn: '1h' })`.
    2.  Client receives token and attaches it to request headers: `Authorization: Bearer <token>`.
    3.  Express middleware intercepts requests and verifies the token using `jsonwebtoken.verify(token, secretKey)`.

**অনুবাদ (Bangla Translation):**
*   **Authentication (ইউজার কে?):** ইউজারের পরিচয় সুনিশ্চিত করা (যেমন- ইমেইল ও পাসওয়ার্ড দিয়ে লগইন)।
*   **Authorization (ইউজারের ক্ষমতা কতটুকু?):** ইউজারের রোল বা পারমিশন চেক করা (যেমন- এডমিন নাকি সাধারণ ইউজার)।
*   **JWT দিয়ে বাস্তবায়ন:**
    1.  ইউজার লগইন করলে সার্ভার `jsonwebtoken.sign()` দিয়ে একটি টোকেন জেনারেট করে ক্লায়েন্টে পাঠায়।
    2.  ক্লায়েন্ট পরবর্তীতে প্রতি রিকোয়েস্টের হেডারে টোকেন পাঠায়: `Authorization: Bearer <token>`।
    3.  Express মিডলওয়্যার `jsonwebtoken.verify()` দিয়ে টোকেনের সত্যতা যাচাই করে রাউট এক্সেস দেয়।

---

### **Q17: What are REPL and npm package scripts in Node.js, and what is `package-lock.json` for? / Node.js-এ REPL এবং npm স্ক্রিপ্ট কী, এবং `package-lock.json`-এর কাজ কী?**

**Answer (English):**
*   **REPL (Read-Eval-Print Loop):** An interactive shell triggered by typing `node` in the terminal to execute quick JS code blocks on the fly.
*   **`package-lock.json`:** Automatically generated file that records the **exact dependency tree** and exact version hashes installed in `node_modules`. It guarantees that every developer and production deployment installs the exact same dependency versions, preventing "works on my machine" bugs.

**অনুবাদ (Bangla Translation):**
*   **REPL:** টার্মিনালে `node` লিখে ইন্টারঅ্যাক্টিভ শ্যেল চালু করা, যেখানে সরাসরি জাভাস্ক্রিপ্ট কোড টেস্ট করা যায়।
*   **`package-lock.json`:** এটি প্রজেক্টে ইনস্টল হওয়া প্রতিটি প্যাকেজের **হুবহু সুনির্দিষ্ট ভার্সন হ্যাশ (Exact Version Tree)** রেকর্ড করে রাখে। এটি নিশ্চিত করে যে প্রতিটি ডেভেলপার ও প্রোডাকশন সার্ভারে একই ভার্সনের ডিপেনডেন্সি ইনস্টল হবে।

---

### **Q18: How do you handle database connections and prevent connection exhaustion in Node.js? / Node.js-এ কীভাবে ডেটাবেজ কানেকশন ম্যানেজ করবেন এবং Connection Exhaustion প্রতিরোধ করবেন?**

**Answer (English):**
Use **Database Connection Pooling** (supported natively by PostgreSQL `pg.Pool`, MySQL `mysql2`, Mongoose/MongoDB).
*   **Why Connection Pooling?** Opening a new TCP connection for every incoming HTTP request is expensive and quickly exhausts database connection limits. A Connection Pool maintains a reusable pool of open connections (e.g., max 20), sharing them dynamically across HTTP requests and returning them to the pool once the query finishes.

**অনুবাদ (Bangla Translation):**
**Database Connection Pooling (কানেকশন পুলিং)** ব্যবহার করে।
*   **কেন কানেকশন পুলিং?** প্রতি HTTP রিকোয়েস্টে নতুন ডেটাবেজ কানেকশন খোলা অত্যন্ত ব্যয়বহুল এবং এতে ডেটাবেজের কানেকশন লিমিট শেষ হয়ে যায়। কানেকশন পুল আগে থেকেই কিছু কানেকশন (যেমন সর্বোচ্চ ২০টি) খোলা রাখে। রিকোয়েস্ট আসলে পুল থেকে কানেকশন ধার দেয় এবং কোয়েরি শেষে আবার পুলে কানেকশন ফিরিয়ে নেয়।

---

### **Q19: What is CORS (Cross-Origin Resource Sharing) and how do you configure it in Express? / CORS কী এবং Express-এ কীভাবে এটি কনফিগার করবেন?**

**Answer (English):**
CORS is a browser security mechanism that blocks web pages from making HTTP requests to a different domain/origin than the one that served the web page.
*   **Configuration in Express:** Use the `cors` middleware package to allow specific origins and HTTP methods.
```javascript
const cors = require('cors');
app.use(cors({
  origin: 'https://myfrontend.com',
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  credentials: true
}));
```

**অনুবাদ (Bangla Translation):**
CORS হলো ব্রাউজারের একটি নিরাপত্তা মেকানিজম যা কোনো ফ্রন্টএন্ড ওয়েবসাইটকে তার নিজের ডোমেন ছাড়া অন্য কোনো আলাদা অরিজিন/ডোমেনে এপিআই রিকোয়েস্ট পাঠাতে বাধা দেয়।
*   **Express-এ কনফিগারেশন:** `cors` প্যাকেজ ব্যবহার করে নির্দিষ্ট ডোমেন এলাউ করা হয়:
```javascript
const cors = require('cors');
app.use(cors({
  origin: 'https://myfrontend.com',
  methods: ['GET', 'POST', 'PUT', 'DELETE'],
  credentials: true
}));
```

---

### **Q20: How do you scale a Node.js application for high traffic and production load? / উচ্চ ট্রাফিক ও প্রোডাকশন লোডের জন্য একটি Node.js অ্যাপ্লিকেশন কীভাবে স্কেল করবেন?**

**Answer (English):**
1.  **Vertical Scaling (Clustering):** Use PM2 or the `cluster` module to spawn multiple instances of the Node.js app matching the number of server CPU cores.
2.  **Horizontal Scaling (Load Balancing):** Run multiple server nodes behind a reverse proxy/load balancer like **NGINX**, AWS ALB, or Kubernetes.
3.  **Caching Layer:** Implement **Redis** or Memcached to cache database queries and session states.
4.  **Stateless Architecture:** Keep the server completely stateless so any load balancer can route requests to any server node seamlessly.
5.  **Asynchronous Message Queues:** Use RabbitMQ or BullMQ/Redis for offloading background tasks (sending emails, processing PDFs).

**অনুবাদ (Bangla Translation):**
1.  **Vertical Scaling (ভার্টিকাল স্কেলিং):** PM2 বা `cluster` মডিউল ব্যবহার করে সার্ভারের প্রতিটি সিপিইউ কোরের (CPU Core) জন্য আলাদা Node.js ইন্সট্যান্স চালু করা।
2.  **Horizontal Scaling (হরিজন্টাল স্কেলিং):** NGINX বা AWS Load Balancer-এর পেছনে একাধিক সার্ভার নোড চালিয়ে রিকোয়েস্ট ভাগ করে দেওয়া।
3.  **ক্যাশিং লেয়ার (Redis):** বারবার লাগা ডেটাবেজ কোয়েরি সেভ রাখতে **Redis** ক্যাশ ব্যবহার করা।
4.  **স্টেটলেস আর্কিটেকচার:** সার্ভারকে সম্পূর্ণ স্টেটলেস রাখা যাতে যেকোনো সার্ভার রিকোয়েস্ট হ্যান্ডেল করতে পারে।
5.  **মেসেজ কিউ:** ব্যাকগ্রাউন্ড কাজ (ইমেইল পাঠানো বা পিডিএফ তৈরি) সামলাতে RabbitMQ বা BullMQ ব্যবহার করা।
