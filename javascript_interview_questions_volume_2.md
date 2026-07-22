# JavaScript Interview Questions Guide: Volume 2 (Questions 36 - 70)

This guide contains detailed answers in English alongside complete Bangla translations for questions 36 to 70 from the uploaded JavaScript Interview Questions PDF.

---

### **Q36: What is recursion and how is it used in JavaScript? / JavaScript-এ রিকার্শন (Recursion) কী এবং কীভাবে ব্যবহৃত হয়?**

**Answer (English):**
Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem by breaking it down into smaller, self-similar sub-problems.
*   **Key Components:**
    1.  **Base Case:** A condition that stops the recursion and returns a result without making further recursive calls (prevents stack overflow).
    2.  **Recursive Step:** The code block where the function calls itself with modified arguments moving towards the base case.
*   **Example (Factorial):**
    ```javascript
    function factorial(n) {
      if (n === 0 || n === 1) return 1; // Base case
      return n * factorial(n - 1);       // Recursive step
    }
    console.log(factorial(4)); // 24
    ```

**অনুবাদ (Bangla Translation):**
রিকার্শন (Recursion) হলো এমন একটি প্রোগ্রামিং পদ্ধতি যেখানে একটি ফাংশন কোনো সমস্যার সমাধানের জন্য নিজেকেই বারবার কল করে এবং সমস্যাটিকে ছোট ছোট উপ-সমস্যায় বিভক্ত করে সমাধান করে।
*   **প্রধান উপাদানসমূহ:**
    1.  **বেস কেস (Base Case):** এটি রিকার্শন বন্ধ করার কন্ডিশন। বেস কেস না থাকলে ফাংশনটি অসীম লুপে চলে গিয়ে `Maximum call stack size exceeded` এরর দেবে।
    2.  **রিকার্সিভ স্টেপ (Recursive Step):** যে অংশে ফাংশনটি নতুন আর্গুমেন্ট সহ নিজেকে পুনরায় কল করে বেস কেসের দিকে ধাবিত হয়।
*   **উদাহরণ (ফ্যাক্টোরিয়াল):**
    ```javascript
    function factorial(n) {
      if (n === 0 || n === 1) return 1; // বেস কেস
      return n * factorial(n - 1);       // রিকার্সিভ স্টেপ
    }
    console.log(factorial(4)); // ২৪
    ```

---

### **Q37: What are default parameters and how are they used? / Default parameters কী এবং এগুলো কীভাবে ব্যবহার করা হয়?**

**Answer (English):**
Default parameters allow function parameters to be initialized with default values if no argument or an `undefined` value is passed when the function is invoked.
*   **Benefits:** Prevents `undefined` parameter values and eliminates manual ternary or logical OR checks inside the function body.
*   **Example:**
    ```javascript
    function greet(name = 'Guest', role = 'User') {
      return `Hello ${name}, your role is ${role}`;
    }
    console.log(greet()); // "Hello Guest, your role is User"
    console.log(greet('Rohit')); // "Hello Rohit, your role is User"
    ```

**অনুবাদ (Bangla Translation):**
ডিফল্ট প্যারামিটার (Default Parameters) হলো ফাংশন ডিক্লেয়ারেশনের সময় প্যারামিটারে আগে থেকেই একটি মান সেট করে রাখা, যাতে ফাংশন রান করার সময় যদি কোনো আর্গুমেন্ট না দেওয়া হয় বা `undefined` পাস করা হয়, তবে যেন ওই ডিফল্ট মানটি ব্যবহৃত হয়।
*   **সুবিধা:** ফাংশনের ভেতরে ম্যানুয়ালি `if (!name)` বা `name || 'Guest'` দিয়ে ভ্যালিডেশন চেক করার ঝামেলা দূর করে।
*   **উদাহরণ:**
    ```javascript
    function greet(name = 'Guest', role = 'User') {
      return `Hello ${name}, your role is ${role}`;
    }
    console.log(greet()); // "Hello Guest, your role is User"
    console.log(greet('Rohit')); // "Hello Rohit, your role is User"
    ```

---

### **Q38: Explain why the following doesn’t work as an IIFE: `function foo(){}();`. What needs to be changed to properly make it an IIFE? / `function foo(){}();` কোডটি কেন IIFE হিসেবে কাজ করে না? একে সঠিক IIFE করতে কী পরিবর্তন করতে হবে?**

**Answer (English):**
*   **Why it fails:** The JavaScript parser encounters the keyword `function` at the beginning of a line and interprets `function foo(){}` as a standard **Function Declaration**, not an expression. Parentheses `()` following a function declaration are treated as a separate, invalid grouping operator syntax error, rather than an invocation.
*   **Fix:** To convert a function declaration into a **Function Expression** (which can be invoked immediately), you must wrap the function inside grouping parentheses:
    ```javascript
    (function foo() {
      console.log("IIFE Executed!");
    })();
    ```

**অনুবাদ (Bangla Translation):**
*   **কেন ব্যর্থ হয়:** জাভাস্ক্রিপ্ট ইন্টারপ্রেটার লাইনের শুরুতে `function` শব্দ দেখলে পুরো `function foo(){}`-কে একটি সাধারণ **ফাংশন ডিক্লেয়ারেশন** হিসেবে ধরে নেয় (ফাংশন এক্সপ্রেশন নয়)। ফাংশন ডিক্লেয়ারেশনের পর ব্র্যাকেট `()` বসালে জাভাস্ক্রিপ্ট একে সিনট্যাক্স এরর মনে করে।
*   **সমাধান:** ফাংশন ডিক্লেয়ারেশনকে **ফাংশন এক্সপ্রেশনে** রূপান্তর করতে পুরো ফাংশনটিকে ফার্স্ট ব্র্যাকেটের `()` ভেতরে ঘিরে দিতে হয়:
    ```javascript
    (function foo() {
      console.log("IIFE Executed!");
    })();
    ```

---

### **Q39: What are the various ways to create objects in JavaScript? / JavaScript-এ অবজেক্ট তৈরি করার বিভিন্ন পদ্ধতিগুলো কী কী?**

**Answer (English):**
JavaScript provides multiple ways to create objects:
1.  **Object Literals (Most Common):** `const obj = { name: 'John', age: 30 };`
2.  **`Object()` Constructor:** `const obj = new Object(); obj.name = 'John';`
3.  **`Object.create()`:** `const obj = Object.create(prototypeObj);` (Inherits from a specified prototype object).
4.  **Constructor Functions:** Using `new` keyword with an ES5 function: `function Person(name) { this.name = name; }`
5.  **ES6 Classes:** `class Person { constructor(name) { this.name = name; } }`
6.  **Factory Functions:** Functions that return a new object literal.

**অনুবাদ (Bangla Translation):**
জাভাস্ক্রিপ্টে অবজেক্ট তৈরি করার প্রধান উপায়গুলো হলো:
1.  **অবজেক্ট লিটারেল (সবচেয়ে সহজ ও জনপ্রিয়):** `const obj = { name: 'John', age: 30 };`
2.  **`Object()` কন্সট্রাক্টর:** `const obj = new Object(); obj.name = 'John';`
3.  **`Object.create()`:** কোনো একটি নির্দিষ্ট প্রোটোটাইপ অবজেক্টকে হুবহু ভিত্তি করে নতুন অবজেক্ট বানানো।
4.  **কন্সট্রাক্টর ফাংশন:** `new` কিওয়ার্ড সহ সাধারণ ফাংশন দিয়ে অবজেক্ট তৈরি।
5.  **ES6 ক্লাস (ES6 Classes):** `class Person { constructor(name) { this.name = name; } }`
6.  **ফ্যাক্টরি ফাংশন (Factory Functions):** সাধারণ ফাংশন যা রান হলে নতুন অবজেক্ট লিটারেল রিটার্ন করে।

---

### **Q40: Explain the difference between dot notation and bracket notation for accessing object properties. / অবজেক্ট প্রপার্টি অ্যাক্সেস করার জন্য ডট নোটেশন (.) এবং ব্র্যাকেট নোটেশনের ([] ) মধ্যে পার্থক্য ব্যাখ্যা করুন।**

**Answer (English):**
*   **Dot Notation (`obj.prop`):** Concise and readable. However, it can only be used with valid JavaScript identifiers (cannot contain spaces, hyphens, numbers at the start, or dynamic variables).
*   **Bracket Notation (`obj['prop']`):** More versatile. It allows:
    1.  Accessing properties containing special characters or spaces: `obj['favorite color']`.
    2.  Accessing properties dynamically via variable values: `const key = 'name'; obj[key];`.
    3.  Accessing properties with numeric keys: `obj[123]`.

**অনুবাদ (Bangla Translation):**
*   **ডট নোটেশন (`obj.prop`):** সংক্ষিপ্ত ও সহজে পড়া যায়। তবে এটি কেবল ভ্যালিড জাভাস্ক্রিপ্ট আইডেন্টিফায়ারের ক্ষেত্রেই কাজ করে (স্পেস, হাইফেন বা ডাইনামিক ভ্যারিয়েবল সাপোর্ট করে না)।
*   **ব্র্যাকেট নোটেশন (`obj['prop']`):** এটি অত্যন্ত শক্তিশালী এবং নিম্নোক্ত সুবিধা দেয়:
    1.  স্পেস বা স্পেশাল ক্যারেক্টার যুক্ত প্রপার্টি রিড করা: `obj['favorite color']`
    2.  ডাইনামিক ভ্যারিয়েবলের মান দিয়ে প্রপার্টি পড়া: `const key = 'name'; obj[key];`
    3.  সংখ্যাত্মক কি অ্যাক্সেস করা: `obj[123]`

---

### **Q41: What are the different methods for iterating over an array? / অ্যারে ইটারেট (লুপ) করার বিভিন্ন মেথডগুলো কী কী?**

**Answer (English):**
Standard array iteration techniques in JavaScript include:
1.  **`for` loop:** Traditional indexed iteration (`for(let i=0; i<arr.length; i++)`).
2.  **`for...of` loop:** Clean syntax to iterate directly over elements.
3.  **`Array.prototype.forEach()`:** Executes a callback for every element (cannot be broken with `break`).
4.  **`Array.prototype.map()`:** Transforms each element and returns a new array.
5.  **`Array.prototype.filter()`:** Returns a filtered new array matching a condition.
6.  **`Array.prototype.reduce()`:** Accumulates values into a single result.
7.  **`Array.prototype.some()` / `every()`:** Checks boolean conditions across elements.

**অনুবাদ (Bangla Translation):**
অ্যারের উপাদানগুলোর ওপর লুপ চালানোর বিভিন্ন পদ্ধতি:
1.  **`for` লুপ:** ইনডেক্স ভিত্তিক প্রথাগত লুপ।
2.  **`for...of` লুপ:** সরাসরি উপাদানগুলোর ওপর সহজে লুপ চালানোর আধুনিক নিয়ম।
3.  **`forEach()`:** প্রতিটি উপাদানের জন্য কলব্যাক ফায়ার করে (তবে এটি মাঝপথে `break` করা যায় না)।
4.  **`map()`:** প্রতিটি উপাদানকে মডিফাই করে একটি নতুন অ্যারে তৈরি করে।
5.  **`filter()`:** শর্ত পূরণ করা উপাদানগুলো বেছে নতুন অ্যারে দেয়।
6.  **`reduce()`:** অ্যারের উপাদানগুলোকে প্রসেস করে একটিমাত্র মানে রূপান্তর করে।
7.  **`some()` / `every()`:** বুলিয়ান শর্ত চেক করে সত্য/মিথ্যা আউটপুট দেয়।

---

### **Q42: How do you add, remove, and update elements in an array? / কীভাবে একটি অ্যারেতে এলিমেন্ট যুক্ত করবেন, রিমুভ করবেন এবং আপডেট করবেন?**

**Answer (English):**
*   **Adding Elements:**
    *   `push(val)`: Adds element to the end.
    *   `unshift(val)`: Adds element to the beginning.
    *   `splice(index, 0, val)`: Inserts element at a specific index.
*   **Removing Elements:**
    *   `pop()`: Removes element from the end.
    *   `shift()`: Removes element from the beginning.
    *   `splice(index, deleteCount)`: Removes elements from a specific index.
*   **Updating Elements:**
    *   Direct assignment: `arr[index] = newValue;`
    *   `splice(index, 1, newValue)`: Replaces an element.

**অনুবাদ (Bangla Translation):**
*   **এলিমেন্ট যুক্ত করা (Adding):**
    *   `push(val)`: অ্যারের শেষে এলিমেন্ট যোগ করে।
    *   `unshift(val)`: অ্যারের শুরুতে এলিমেন্ট যোগ করে।
    *   `splice(index, 0, val)`: নির্দিষ্ট ইনডেক্সে নতুন এলিমেন্ট বসায়।
*   **এলিমেন্ট রিমুভ করা (Removing):**
    *   `pop()`: শেষের এলিমেন্টটি মুছে ফেলে।
    *   `shift()`: শুরুর এলিমেন্টটি মুছে ফেলে।
    *   `splice(index, deleteCount)`: নির্দিষ্ট ইনডেক্স থেকে শুরু করে এলিমেন্ট ডিলিট করে।
*   **এলিমেন্ট আপডেট করা (Updating):**
    *   সরাসরি ইনডেক্স দিয়ে মান সেট করা: `arr[index] = newValue;`
    *   `splice(index, 1, newValue)`: নির্দিষ্ট ইনডেক্সের মান বদলে নতুন মান বসানো।

---

### **Q43: What are the different ways to copy an object or an array? / অবজেক্ট বা অ্যারে কপি করার বিভিন্ন পদ্ধতি কী কী?**

**Answer (English):**
*   **Shallow Copy:**
    1.  Spread operator: `const arrCopy = [...arr];` / `const objCopy = { ...obj };`
    2.  `Object.assign({}, obj)` or `arr.slice()`
*   **Deep Copy:**
    1.  `structuredClone(obj)`: The built-in modern JavaScript native method.
    2.  `JSON.parse(JSON.stringify(obj))`: Works for basic objects without functions, undefined, or circular references.
    3.  Lodash library: `_.cloneDeep(obj)`.

**অনুবাদ (Bangla Translation):**
*   **শ্যালো কপি (Shallow Copy):**
    1.  স্প্রেড অপারেটর: `const arrCopy = [...arr];` / `const objCopy = { ...obj };`
    2.  `Object.assign({}, obj)` অথবা `arr.slice()`
*   **ডিপ কপি (Deep Copy):**
    1.  `structuredClone(obj)`: আধুনিক ব্রাউজারের নেটিভ ও সেরা মেথড।
    2.  `JSON.parse(JSON.stringify(obj))`: ফাংশন বা `undefined` না থাকা সাধারণ অবজেক্টের জন্য।
    3.  Lodash লাইব্রেরির `_.cloneDeep(obj)`।

---

### **Q44: Explain the difference between shallow copy and deep copy. / Shallow copy এবং Deep copy এর মধ্যে পার্থক্য ব্যাখ্যা করুন।**

**Answer (English):**
*   **Shallow Copy:** Copies only the top-level properties of an object/array. If the object contains nested objects or arrays, their **memory references** are shared. Modifying a nested object in the copy will also alter the original object.
*   **Deep Copy:** Duplicates every level of an object recursively, creating entirely independent memory instances for all nested objects and arrays. Modifying the copy never affects the original.

**অনুবাদ (Bangla Translation):**
*   **Shallow Copy (শ্যালো কপি):** এটি অবজেক্টের প্রথম লেভেলের মানগুলোকে কপি করে। তবে ভেতরে নেস্টেড বা ইনার অবজেক্ট থাকলে তাদের **মেমোরি রেফারেন্স** একই থাকে। ফলে কপিকৃত অবজেক্টের নেস্টেড মান পরিবর্তন করলে মূল অবজেক্টের মানও বদলে যায়।
*   **Deep Copy (ডিপ কপি):** এটি রিকার্সিভলি অবজেক্টের ভেতরের সমস্ত লেভেলের নেস্টেড অবজেক্ট ও অ্যারের সম্পূর্ণ স্বাধীন নতুন মেমোরি কপি তৈরি করে। ফলে কপিকৃত অবজেক্টে কোনো পরিবর্তন আনলে মূল অবজেক্ট সম্পূর্ণ অপরিবর্তিত থাকে।

---

### **Q45: What are the advantages of using the spread operator with arrays and objects? / অ্যারে এবং অবজেক্টে স্প্রেড অপারেটর ব্যবহারের সুবিধাগুলো কী কী?**

**Answer (English):**
1.  **Immutability:** Easily creates copies or updated versions of arrays/objects without mutating the original state (crucial for React state updates).
2.  **Concise Syntax:** Simplifies merging multiple arrays (`[...a, ...b]`) or combining object properties (`{ ...obj1, ...obj2 }`).
3.  **Function Arguments:** Expands arrays into separate parameters (`Math.max(...arr)`).
4.  **Readability:** Modern, declarative syntax that replaces complex methods like `concat()`, `slice()`, or `Object.assign()`.

**অনুবাদ (Bangla Translation):**
1.  **ইমিউটেবিলিটি (Immutability):** মূল অবজেক্ট বা অ্যারে নষ্ট না করে সহজে কপি বা আপডেট করা যায় (যা React স্টেট ম্যানেজমেন্টের জন্য অপরিহার্য)।
2.  **সহজ ও সংক্ষিপ্ত সিনট্যাক্স:** একাধিক অ্যারে একত্র করা (`[...a, ...b]`) বা অবজেক্ট প্রপার্টি মার্জ করা সহজ করে।
3.  **আর্গুমেন্ট পাস করা:** অ্যারেকে আলাদা আলাদা ফাংশন আর্গুমেন্টে রূপান্তর করা (`Math.max(...arr)`)।
4.  **পঠনযোগ্যতা:** সিএসএস/জেএস কোডকে পরিচ্ছন্ন করে `concat()` বা `Object.assign()` এর জটিলতা দূর করে।

---

### **Q46: How do you check if an object has a specific property? / কোনো অবজেক্টে নির্দিষ্ট প্রপার্টি আছে কিনা তা কীভাবে চেক করবেন?**

**Answer (English):**
1.  **`Object.hasOwn(obj, 'prop')` (Recommended modern way):** Checks if the object has the property as its own (non-inherited) property.
2.  **`obj.hasOwnProperty('prop')`:** Older instance method to check own properties.
3.  **`'prop' in obj`:** Checks if the property exists on the object **or** anywhere along its prototype chain.
4.  **Direct comparison:** `obj.prop !== undefined` (can give false negatives if the property exists and is set to `undefined`).

**অনুবাদ (Bangla Translation):**
1.  **`Object.hasOwn(obj, 'prop')` (আধুনিক ও সেরা উপায়):** অবজেক্টটির নিজের মধ্যে (প্রোটোটাইপ বাদে) প্রপার্টিটি আছে কিনা চেক করে।
2.  **`obj.hasOwnProperty('prop')`:** অবজেক্টের নিজস্ব প্রপার্টি চেক করার সনাতন মেথড।
3.  **`'prop' in obj`:** প্রপার্টিটি অবজেক্টে **অথবা** তার প্রোটোটাইপ চেইনের কোথাও আছে কিনা চেক করে।
4.  **সরাসরি চেক:** `obj.prop !== undefined` (তবে প্রপার্টির মান নিজে `undefined` হলে এটি ভুল রেজাল্ট দেয়)।

---

### **Q47: Explain the difference between mutable and immutable objects in JavaScript. / JavaScript-এ Mutable এবং Immutable অবজেক্টের মধ্যে পার্থক্য ব্যাখ্যা করুন।**

**Answer (English):**
*   **Mutable Objects:** Objects whose internal properties and values can be modified after creation. In JavaScript, all default objects, arrays, maps, and sets are mutable (e.g., `obj.name = 'NewName'` modifies the existing object in memory).
*   **Immutable Objects:** Objects whose values cannot be modified, added, or deleted once created. Primitive values are immutable by nature. Objects can be made immutable using `Object.freeze()`.

**অনুবাদ (Bangla Translation):**
*   **Mutable Objects (পরিবর্তনযোগ্য অবজেক্ট):** যেসব অবজেক্ট তৈরির পরও তাদের ভেতরের মান বা প্রপার্টি সরাসরি পরিবর্তন বা ডিলিট করা যায়। জাভাস্ক্রিপ্টে সব সাধারণ অবজেক্ট, অ্যারে ইত্যাদি ডিফল্টভাবে মিউটেবল (যেমন- `obj.name = 'NewName'` মেমোরির মূল অবজেক্টকে বদলে দেয়)।
*   **Immutable Objects (অপরিবর্তনযোগ্য অবজেক্ট):** যেসব অবজেক্ট তৈরির পর তাদের মেমোরির মান সরাসরি বদলানো বা ডিলিট করা সম্ভব নয়। প্রিমিটিভ টাইপসমূহ জন্মগতভাবেই ইমিউটেবল। কোনো সাধারণ অবজেক্টকে ইমিউটেবল করতে `Object.freeze()` ব্যবহার করা হয়।

---

### **Q48: Explain the concept of destructuring assignment for objects and arrays. / অবজেক্ট এবং অ্যারের জন্য Destructuring assignment এর ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
Destructuring assignment is an ES6 syntax feature that allows unpacking values from arrays or properties from objects directly into distinct variables.
*   **Array Destructuring:** Uses position-based syntax with square brackets `[]`.
    ```javascript
    const [a, b, ...rest] = [10, 20, 30, 40];
    ```
*   **Object Destructuring:** Uses key-name matching syntax with curly braces `{}`.
    ```javascript
    const user = { name: 'John', age: 25 };
    const { name, age } = user;
    ```

**অনুবাদ (Bangla Translation):**
ডিফেক্টরিং অ্যাসাইনমেন্ট (Destructuring Assignment) হলো ES6-এর একটি পাওয়ারফুল ফিচার যার মাধ্যমে অ্যারে বা অবজেক্টের ভেতরের মানগুলোকে ভেঙে সরাসরি নতুন আলাদা ভ্যারিয়েবলে স্টোর করা যায়।
*   **অ্যারে ডিস্ট্রাকচারিং:** পজিশন বা ইনডেক্স অনুযায়ী ফার্স্ট ব্র্যাকেট `[]` ব্যবহার করে করা হয়:
    ```javascript
    const [a, b, ...rest] = [10, 20, 30, 40];
    ```
*   **অবজেক্ট ডিস্ট্রাকচারিং:** প্রপার্টি বা কি (Key) এর নাম মিলিয়ে সেকেন্ড ব্র্যাকেট `{}` ব্যবহার করে করা হয়:
    ```javascript
    const user = { name: 'John', age: 25 };
    const { name, age } = user;
    ```

---

### **Q49: What is `Object.freeze()` for? / `Object.freeze()` এর কাজ কী?**

**Answer (English):**
`Object.freeze()` freezes an object, making it completely **immutable**.
*   **Behavior of Frozen Object:**
    1.  New properties cannot be added.
    2.  Existing properties cannot be removed or deleted.
    3.  Values of existing properties cannot be changed.
    4.  Property descriptors (writable, configurable, enumerable) cannot be reconfigured.
*   *Note:* It provides a **shallow freeze**. Nested objects inside the frozen object can still be mutated unless recursively frozen.

**অনুবাদ (Bangla Translation):**
`Object.freeze()` কোনো একটি অবজেক্টকে ফ্রিজ বা লক করে সম্পূর্ণ **ইমিউটেবল (অপরিবর্তনযোগ্য)** বানিয়ে দেয়।
*   **ফ্রিজ করা অবজেক্টের বৈশিষ্ট্য:**
    1.  নতুন কোনো প্রপার্টি যোগ করা যায় না।
    2.  বিদ্যমান কোনো প্রপার্টি ডিলিট বা রিমুভ করা যায় না।
    3.  বিদ্যমান প্রপার্টির মান পরিবর্তন করা যায় না।
    4.  strict mode অন থাকলে পরিবর্তন করতে গেলে এরর মারবে।
*   *বিশেষ দ্রষ্টব্য:* এটি একটি **শ্যালো ফ্রিজ** দেয়। অর্থাৎ এর ভেতরে থাকা নেস্টেড অবজেক্ট কিন্তু মিউটেবলই থেকে যায়।

---

### **Q50: What is `Object.seal()` for? / `Object.seal()` এর কাজ কী?**

**Answer (English):**
`Object.seal()` seals an object.
*   **Behavior of Sealed Object:**
    1.  Prevents adding new properties to the object.
    2.  Prevents deleting existing properties (marks them as non-configurable).
    3.  **Allows modifying the values of existing writable properties.**
*   **Difference from `Object.freeze()`:** `Object.freeze()` prevents modifying property values, whereas `Object.seal()` allows changing values of existing properties.

**অনুবাদ (Bangla Translation):**
`Object.seal()` কোনো অবজেক্টকে সিলড বা সীলমোহর করে দেয়।
*   **সিলড অবজেক্টের বৈশিষ্ট্য:**
    1.  নতুন কোনো প্রপার্টি যোগ করা বন্ধ করে।
    2.  বিদ্যমান প্রপার্টি মুছে ফেলা বা ডিলিট করা বন্ধ করে।
    3.  **বিদ্যমান প্রপার্টিগুলোর মান কিন্তু পরিবর্তন (Update) করা যায়।**
*   **`Object.freeze()` এর সাথে তফাৎ:** `freeze()` মান পরিবর্তন করতেও বাধা দেয়, কিন্তু `seal()` বিদ্যমান প্রপার্টির নতুন মান বসানোর সুযোগ দেয়।

---

### **Q51: What is `Object.preventExtensions()` for? / `Object.preventExtensions()` এর কাজ কী?**

**Answer (English):**
`Object.preventExtensions()` prevents new properties from ever being added to an object.
*   **Behavior:**
    *   You **cannot add** new properties.
    *   You **can delete** existing properties.
    *   You **can modify** values of existing properties.
*   **Comparison:** It is the least restrictive among `preventExtensions()`, `seal()`, and `freeze()`.

**অনুবাদ (Bangla Translation):**
`Object.preventExtensions()` কোনো অবজেক্টে নতুন করে কোনো প্রপার্টি যুক্ত করা বন্ধ করে দেয়।
*   **বৈশিষ্ট্য:**
    *   নতুন প্রপার্টি **যোগ করা যাবে না**।
    *   বিদ্যমান প্রপার্টি **ডিলিট করা যাবে**।
    *   বিদ্যমান প্রপার্টির মান **পরিবর্তন বা আপডেট করা যাবে**।
*   **তুলনা:** `preventExtensions()`, `seal()`, এবং `freeze()` এর মধ্যে এটি সবচেয়ে কম সীমাবদ্ধতামূলক মেথড।

---

### **Q52: What are JavaScript object getters and setters for? / JavaScript অবজেক্ট গেটার্স (getters) এবং সেটার্স (setters) কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
Getters and setters are pseudo-properties that execute custom functions when a property is read (accessed) or written to (assigned). They are defined using `get` and `set` keywords.
*   **Purposes:**
    1.  **Encapsulation:** Hiding internal state/private variables (e.g., `_name`).
    2.  **Validation:** Validating data before assigning it in a setter.
    3.  **Computed Properties:** Dynamically computing a value on the fly (e.g., combining `firstName` + `lastName` to return `fullName`).
*   **Example:**
    ```javascript
    const user = {
      _age: 20,
      get age() { return this._age; },
      set age(val) { if (val > 0) this._age = val; }
    };
    ```

**অনুবাদ (Bangla Translation):**
গেটার্স (`get`) এবং সেটার্স (`set`) হলো অবজেক্টের বিশেষ সিউডো-প্রপার্টি যা কোনো মান রিড করার সময় বা রাইট/অ্যাসাইন করার সময় ব্যাকগ্রাউন্ডে নির্দিষ্ট কাস্টম লজিক রান করায়।
*   **ব্যবহারের উদ্দেশ্য:**
    1.  **এনক্যাপসুলেশন:** প্রাইভেট প্রপার্টি বা ইন্টারনাল স্টেট লুকিয়ে রাখা।
    2.  **ডাটা ভ্যালিডেশন:** সেটারে মান সেট করার সময় ভ্যালিডেশন দেওয়া (যেমন- বয়স ০ এর কম হতে পারবে না)।
    3.  **কম্পিউটেড প্রপার্টি:** রানটাইমে ডাইনামিক ভ্যালু হিসাব করে প্রদান করা (যেমন- `firstName` ও `lastName` মিলিয়ে `fullName` রিটার্ন করা)।

---

### **Q53: What are JavaScript object property flags and descriptors? / JavaScript অবজেক্ট প্রপার্টি ফ্লাগস (flags) এবং ডেসক্রিপ্টরস (descriptors) কী?**

**Answer (English):**
Object properties have more than just a value; they carry hidden attributes called **Property Flags**:
1.  **`writable`:** If `true`, the value can be changed; otherwise, it's read-only.
2.  **`enumerable`:** If `true`, the property shows up in `for...in` loops and `Object.keys()`.
3.  **`configurable`:** If `true`, the property can be deleted and its flags modified.
*   **Property Descriptors:** Objects that package these flags along with the `value`.
    *   Get descriptor: `Object.getOwnPropertyDescriptor(obj, 'prop')`
    *   Set descriptor: `Object.defineProperty(obj, 'prop', { writable: false })`

**অনুবাদ (Bangla Translation):**
অবজেক্ট প্রপার্টির কেবল মানই থাকে না, তার ব্যাকগ্রাউন্ডে ৩টি হিডেন অ্যাট্রিবিউট বা **Property Flags** থাকে:
1.  **`writable`:** `true` হলে মান বদলানো যায়, `false` হলে রিড-অনলি থাকে।
2.  **`enumerable`:** `true` হলে `for...in` লুপ বা `Object.keys()` এ প্রপার্টিটি দেখা যায়।
3.  **`configurable`:** `true` হলে প্রপার্টিটি ডিলিট করা বা তার ফ্লাগ পরিবর্তন করা যায়।
*   **ডেসক্রিপ্টর:** `Object.defineProperty()` মেথড দিয়ে এই ফ্লাগগুলো ম্যানুয়ালি সেট বা পরিবর্তন করা যায়।

---

### **Q54: How do you reliably determine whether an object is empty? / কোনো অবজেক্ট খালি (empty) কিনা তা কীভাবে নিশ্চিতভাবে পরীক্ষা করবেন?**

**Answer (English):**
To reliably check if an object `{}` has no enumerable properties:
1.  **Standard Modern Way:**
    ```javascript
    const isEmpty = obj => Object.keys(obj).length === 0 && obj.constructor === Object;
    ```
2.  **Handling Symbols/Non-enumerables:**
    ```javascript
    const isTotallyEmpty = obj => Object.getOwnPropertyNames(obj).length === 0 && Object.getOwnPropertySymbols(obj).length === 0;
    ```

**অনুবাদ (Bangla Translation):**
কোনো অবজেক্ট `{}` পুরোপুরি খালি কিনা তা চেক করার সেরা আধুনিক নিয়ম:
1.  **সাধারণ ও জনপ্রিয় উপায়:**
    ```javascript
    const isEmpty = obj => Object.keys(obj).length === 0 && obj.constructor === Object;
    ```
2.  **সিম্বল বা হিডেন প্রপার্টি সহ শতভাগ নিশ্চিত চেক:**
    ```javascript
    const isTotallyEmpty = obj => Object.getOwnPropertyNames(obj).length === 0 && Object.getOwnPropertySymbols(obj).length === 0;
    ```

---

### **Q55: What is the event loop in JavaScript runtimes? / JavaScript রানটাইমে ইভেন্ট লুপ (Event Loop) কী?**

**Answer (English):**
The Event Loop is a constantly running background mechanism in JavaScript runtimes (browsers / Node.js) that coordinates code execution, event handling, and callback processing.
*   **How it works:**
    1.  Synchronous code executes on the single-threaded **Call Stack**.
    2.  Asynchronous tasks (APIs, timers, promises) are offloaded to Web APIs.
    3.  Completed async callbacks enter either the **Microtask Queue** (Promises, process.nextTick) or **Macrotask Queue** (setTimeout, setInterval).
    4.  The **Event Loop** constantly monitors the Call Stack. Once the Call Stack is completely empty, it pushes all tasks from the Microtask Queue first, followed by Macrotask Queue items onto the stack for execution.

**অনুবাদ (Bangla Translation):**
ইভেন্ট লুপ (Event Loop) হলো জাভাস্ক্রিপ্ট রানটাইমের (ব্রাউজার বা Node.js) একটি ব্যাকগ্রাউন্ড মেকানিজম যা সিঙ্গেল-থ্রেডেড হওয়া সত্ত্বেও অ্যাসিনক্রোনাস কাজগুলো নির্বিঘ্নে পরিচালনা করে।
*   **কাজের ধাপসমূহ:**
    1.  সিনক্রোনাস কোডগুলো প্রধান **Call Stack**-এ ধাপে ধাপে এক্সিকিউট হয়।
    2.  অ্যাসিনক্রোনাস কাজ (যেমন- টাইমার, এপিআই রিকোয়েস্ট) ব্রাউজারের Web API-তে ব্যাকগ্রাউন্ডে চলে যায়।
    3.  কাজ শেষ হলে তাদের কলব্যাকগুলো **Microtask Queue** (প্রমিজ) অথবা **Macrotask Queue** (setTimeout)-এ সিরিয়ালে জমা হয়।
    4.  ইভেন্ট লুপ সার্বক্ষণিক কল স্ট্যাককে পর্যবেক্ষণ করে। কল স্ট্যাক খালি হওয়ামাত্রই এটি প্রথমে মাইক্রোটাস্ক কিউ-এর কাজ এবং পরে ম্যাক্রোটাস্ক কিউ-এর কাজ কল স্ট্যাকে পাঠিয়ে রান করায়।

---

### **Q56: Explain the difference between synchronous and asynchronous functions in JavaScript. / JavaScript-এ Synchronous এবং Asynchronous ফাংশনের মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Synchronous Functions:** Blocking in nature. Each statement executes line-by-line in sequential order. The execution of subsequent code is paused until the current operation finishes (can freeze the UI during heavy operations).
*   **Asynchronous Functions:** Non-blocking in nature. They trigger an operation and allow the program execution to move to the next lines immediately without waiting. The callback or promise resolves in the background when ready, keeping the UI responsive.

**অনুবাদ (Bangla Translation):**
*   **Synchronous (সিনক্রোনাস) ফাংশন:** এটি ব্লকিং টাইপ। কোড ওপর থেকে নিচে এক লাইন এক লাইন করে সিরিয়ালি রান করে। একটি লাইনের কাজ শেষ না হওয়া পর্যন্ত পরবর্তী লাইনের কাজ স্থগিত থাকে (বড় কাজ হলে স্ক্রিন হ্যাং হয়ে যায়)।
*   **Asynchronous (অ্যাসিনক্রোনাস) ফাংশন:** এটি নন-ব্লকিং টাইপ। এটি দীর্ঘ সময় সাপেক্ষ কাজ শুরু করে দিয়ে ব্রাউজারকে আটকায় না, বরং পরবর্তী লাইনের কোড রান হতে দেয়। ব্যাকগ্রাউন্ডে কাজ শেষ হলে কলব্যাক বা প্রমিজের মাধ্যমে রেজাল্ট প্রসেস করে।

---

### **Q57: Explain the concept of a callback function in asynchronous operations. / অ্যাসিনক্রোনাস অপারেশনে কলব্যাক ফাংশনের ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
In asynchronous operations (like `setTimeout`, `fetch`, or event handling), a callback function is a function passed as an argument that is scheduled to run *only after* the long-running task completes. Because async tasks don't return values immediately, the callback acts as a handler receiving the final data or response once the operation finishes.

**অনুবাদ (Bangla Translation):**
অ্যাসিনক্রোনাস অপারেশনে (যেমন ফাইল রিড, টাইমার বা এপিআই কল) কোনো কাজ তাৎক্ষণিকভাবে রেজাল্ট দিতে পারে না। তাই সেই দীর্ঘমেয়াদী কাজ শেষ হওয়ার পর ফলাফল প্রসেস করার জন্য প্যারামিটার হিসেবে যে ফাংশনটি পাঠিয়ে দেওয়া হয়, কাজ শেষে ব্রাউজার স্বয়ংক্রিয়ভাবে সেই ফাংশনটি ফায়ার করে—এটাই অ্যাসিনক্রোনাস কলব্যাক।

---

### **Q58: What are Promises and how do they work? / Promises কী এবং এগুলো কীভাবে কাজ করে?**

**Answer (English):**
A `Promise` is a JavaScript object representing the eventual completion (or failure) of an asynchronous operation and its resulting value. It eliminates "callback hell" through chaining.
*   **How it works:** You attach `.then()` handlers to process resolved values and `.catch()` handlers to handle errors once the asynchronous action finishes.
*   **Example Syntax:**
    ```javascript
    const myPromise = new Promise((resolve, reject) => {
      if (success) resolve("Data received");
      else reject("Error occurred");
    });
    myPromise.then(res => console.log(res)).catch(err => console.error(err));
    ```

**অনুবাদ (Bangla Translation):**
প্রমিজ (Promise) হলো জাভাস্ক্রিপ্টের একটি অবজেক্ট যা কোনো অ্যাসিনক্রোনাস অপারেশনের ভবিষ্যৎ ফলাফল (সফলতা বা ব্যর্থতা) নির্দেশ করে। এটি কলব্যাক হেল (Callback Hell) দূর করে পরিষ্কার কোড লিখতে সাহায্য করে।
*   **কাজের নিয়ম:** প্রমিজ সফল হলে এর রেজাল্ট প্রসেস করতে `.then()` এবং ব্যর্থ হলে এরর হ্যান্ডেল করতে `.catch()` ব্যবহার করা হয়।
*   **সিনট্যাক্স উদাহরণ:**
    ```javascript
    const myPromise = new Promise((resolve, reject) => {
      if (success) resolve("Data received");
      else reject("Error occurred");
    });
    myPromise.then(res => console.log(res)).catch(err => console.error(err));
    ```

---

### **Q59: Explain the different states of a Promise. / একটি Promise এর বিভিন্ন স্টেট বা অবস্থাগুলো ব্যাখ্যা করুন।**

**Answer (English):**
A Promise exists in one of three mutually exclusive states:
1.  **Pending:** Initial default state. The asynchronous operation is still ongoing and has neither resolved nor rejected.
2.  **Fulfilled (Resolved):** The operation completed successfully, and `resolve(value)` was called.
3.  **Rejected:** The operation failed, and `reject(error)` was called.
*   *Settled:* A promise is considered "settled" once it is either fulfilled or rejected (it can never change state after settling).

**অনুবাদ (Bangla Translation):**
একটি প্রমিজ মূলত তিনটি অবস্থার (State) মধ্য দিয়ে যায়:
1.  **Pending (পেন্ডিং):** এটি প্রাথমিক অবস্থা। অ্যাসিনক্রোনাস কাজ এখনো চলছে, সফল বা ব্যর্থ কোনটিই নিশ্চিত হয়নি।
2.  **Fulfilled / Resolved (সফল):** কাজ সফলভাবে সম্পন্ন হয়েছে এবং `resolve()` কল করা হয়েছে।
3.  **Rejected (ব্যর্থ):** কাজ ব্যর্থ হয়েছে এবং `reject()` কল করা হয়েছে।
*   *Settled:* প্রমিজ যখন Fulfilled বা Rejected যেকোনো একটিতে পৌঁছায়, তাকে Settled বলা হয় (একবার Settled হলে মান আর পাল্টানো যায় না)।

---

### **Q60: What are the pros and cons of using Promises instead of callbacks in JavaScript? / JavaScript-এ কলব্যাকের বদলে Promises ব্যবহারের সুবিধা ও অসুবিধাগুলো কী কী?**

**Answer (English):**
*   **Pros:**
    1.  **Avoids Callback Hell:** Prevents deeply nested pyramid-of-doom code with readable `.then()` chaining.
    2.  **Better Error Handling:** Centralized error catching via `.catch()`.
    3.  **Parallel Operations:** Easy handling of multiple async actions using `Promise.all()`.
*   **Cons:**
    1.  Slight overhead compared to raw callbacks.
    2.  Uncaught promise rejections can fail silently if `.catch()` is omitted.
    3.  Cannot be cancelled natively (without `AbortController`).

**অনুবাদ (Bangla Translation):**
*   **সুবিধাসমূহ (Pros):**
    1.  **কলব্যাক হেল এড়ানো:** পিরামিডের মতো জটিল নেস্টেড কোড দূর করে সুন্দর `.then()` চেইনিং সুবিধা দেয়।
    2.  **উন্নত এরর হ্যান্ডলিং:** একটিমাত্র `.catch()` দিয়ে পুরো প্রমিজ চেইনের এরর ধরা যায়।
    3.  **প্যারালাল এক্সিকিউশন:** `Promise.all()` দিয়ে একাধিক কাজ একযোগে হ্যান্ডেল করা যায়।
*   **অসুবিধাসমূহ (Cons):**
    1.  র কোড কলব্যাকের চেয়ে সামান্য বেশি মেমোরি নেয়।
    2.  `.catch()` না লিখলে এরর মাঝপথে সাইলেন্টলি হারিয়ে যেতে পারে।
    3.  সরাসরি প্রমিজ ক্যানসেল বা থামানো যায় না।

---

### **Q61: What is the use of `Promise.all()`? / `Promise.all()` এর কাজ কী?**

**Answer (English):**
`Promise.all()` accepts an array (or iterable) of promises and returns a single Promise.
*   **Behavior:**
    *   It fulfills when **all** input promises fulfill, returning an array of resolved values in the exact input order.
    *   It **fails fast**: If any single promise rejects, the entire `Promise.all()` immediately rejects with that error, ignoring all other pending or resolved promises.

**অনুবাদ (Bangla Translation):**
`Promise.all()` একাধিক প্রমিজের একটি অ্যারে গ্রহণ করে এবং একটিমাত্র কম্বাইন্ড প্রমিজ রিটার্ন করে।
*   **আচরণ:**
    *   অ্যারের **সবগুলো** প্রমিজ সফল হলে এটি সবার রেজাল্ট নিয়ে একটি অ্যারে আউটপুট দেয়।
    *   **Fail-Fast মেকানিজম:** অ্যারের যেকোনো *একটি* প্রমিজ রিজেক্ট বা ফেল করলেই পুরো `Promise.all()` সাথে সাথে রিজেক্ট হয়ে যায়।

---

### **Q62: How is `Promise.all()` different from `Promise.allSettled()`? / `Promise.all()` এবং `Promise.allSettled()` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`Promise.all()`:** Fails fast. If one promise fails, it rejects immediately without waiting for other promises to finish.
*   **`Promise.allSettled()`:** Waits for **every** promise in the array to settle (either fulfill or reject). It never rejects overall; instead, it returns an array of objects describing the outcome of each promise (containing `{ status: 'fulfilled', value }` or `{ status: 'rejected', reason }`).

**অনুবাদ (Bangla Translation):**
*   **`Promise.all()`:** এটি ফেইল-ফাস্ট। যেকোনো একটি প্রমিজ ব্যর্থ হলেই এটি পুরো অ্যারে রিজেক্ট করে দেয়।
*   **`Promise.allSettled()`:** এটি কখনো ওভারঅল ফেল করে না। এটি অ্যারের **প্রতিটি** প্রমিজ শেষ (Fulfilled বা Rejected) হওয়া পর্যন্ত অপেক্ষা করে এবং প্রতিটি প্রমিজের স্ট্যাটাস ও ভ্যালু সহ অবজেক্টের অ্যারে রিটার্ন করে।

---

### **Q63: What is async/await and how does it simplify asynchronous code? / async/await কী এবং এটি কীভাবে অ্যাসিনক্রোনাস কোডকে সহজ করে?**

**Answer (English):**
`async/await` is syntactic sugar built on top of Promises introduced in ES2017.
*   The `async` keyword placed before a function makes it return a promise implicitly.
*   The `await` keyword pauses function execution inside an `async` function until the promise settles.
*   **Simplification:** It allows writing asynchronous code that looks and reads sequentially like synchronous code, making debugging easier and enabling standard `try...catch` blocks for error handling.

**অনুবাদ (Bangla Translation):**
`async/await` হলো ES2017-এ আনা প্রমিজের ওপর তৈরি করা সহজ সিনট্যাক্স (Syntactic Sugar)।
*   ফাংশনের সামনে `async` দিলে ফাংশনটি স্বয়ংক্রিয়ভাবে একটি প্রমিজ রিটার্ন করে।
*   ফাংশনের ভেতরে প্রমিজের সামনে `await` দিলে প্রমিজটি সমাধান হওয়া পর্যন্ত কেবল সেই ফাংশনের এক্সিকিউশন পজ থাকে।
*   **সহজ করার উপায়:** এটি অ্যাসিনক্রোনাস কোডকে সাধারণ সিনক্রোনাস কোডের মতো সোজা ও পঠনযোগ্য করে তোলে এবং সাধারণ `try...catch` ব্লক দিয়ে এরর ধরার সুবিধা দেয়।

---

### **Q64: How do you handle errors in asynchronous operations? / অ্যাসিনক্রোনাস অপারেশনে এরর কীভাবে হ্যান্ডেল করবেন?**

**Answer (English):**
1.  **With `async/await`:** Wrap the `await` statement inside a standard `try...catch` block.
    ```javascript
    try {
      const res = await fetch(url);
      const data = await res.json();
    } catch (error) {
      console.error("Fetch failed:", error);
    }
    ```
2.  **With Promises:** Attach a `.catch()` method to the promise chain.
    ```javascript
    fetch(url).then(res => res.json()).catch(err => console.error(err));
    ```
3.  **Global Handlers:** `window.addEventListener('unhandledrejection')` in browsers.

**অনুবাদ (Bangla Translation):**
1.  **`async/await` এর সাথে:** কোডকে `try...catch` ব্লকে রাখা।
    ```javascript
    try {
      const res = await fetch(url);
      const data = await res.json();
    } catch (error) {
      console.error("Fetch failed:", error);
    }
    ```
2.  **Promises এর সাথে:** চেইনের শেষে `.catch()` মেথড যুক্ত করা।
    ```javascript
    fetch(url).then(res => res.json()).catch(err => console.error(err));
    ```
3.  **গ্লোবাল এরর ক্যাচার:** ব্রাউজারে `unhandledrejection` ইভেন্ট লিসেনার ব্যবহার করে।

---

### **Q65: Explain the concept of a microtask queue. / মাইক্রোটাস্ক কিউ (Microtask Queue) ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
The Microtask Queue is a high-priority queue in the JavaScript Event Loop specifically reserved for short asynchronous tasks that must execute immediately after the current script finishes, before the browser yields control back to rendering or processing macrotasks.
*   **Contains:** Promise callbacks (`.then`, `.catch`, `.finally`), `queueMicrotask()`, `MutationObserver`.
*   **Priority:** The Event Loop drains the **entire** Microtask Queue completely before picking even a single task from the Macrotask Queue (timers/events).

**অনুবাদ (Bangla Translation):**
মাইক্রোটাস্ক কিউ (Microtask Queue) হলো ইভент লুপের একটি উচ্চ-অগ্রাধিকারের কিউ (Queue)।
*   **যেসকল কাজ থাকে:** প্রমিজ কলব্যাকসমূহ (`.then`, `.catch`), `queueMicrotask()`, এবং `MutationObserver` এর কাজ।
*   **অগ্রাধিকার:** সাধারণ টাইমার বা ম্যাক্রোটাস্কের (Macrotask) কাজ শুরু করার আগেই ইভেন্ট লুপ মাইক্রোটাস্ক কিউ-এর সমস্ত কাজ শতভাগ ক্লিয়ার করে নেয়।

---

### **Q66: What is the difference between `setTimeout()`, `setImmediate()`, and `process.nextTick()`? / `setTimeout()`, `setImmediate()`, এবং `process.nextTick()` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
In Node.js runtime environment:
1.  **`process.nextTick()`:** Executes immediately after the current operation completes, before the Event Loop continues to any queue phases. Highest execution priority.
2.  **`setTimeout(fn, 0)`:** Schedules a callback in the Macrotask (Timers phase) after a minimum threshold of ~1ms delay.
3.  **`setImmediate(fn)`:** Schedules a callback in the Check phase of the Event Loop (executes right after I/O polling phase).

**অনুবাদ (Bangla Translation):**
Node.js রানটাইম এনভায়রনমেন্টে:
1.  **`process.nextTick()`:** বর্তমান অপারেশন শেষ হওয়া মাত্রই ইভেন্ট লুপের যেকোনো ফেজের আগে রান করে। এর অগ্রাধিকার সবচেয়ে বেশি।
2.  **`setTimeout(fn, 0)`:** ইভেন্ট লুপের টাইমার ফেজে মেমোরি মিনিমাম ডিলে পার করে ফায়ার হয়।
3.  **`setImmediate(fn)`:** ইভেন্ট লুপের Check ফেজে আই/ও (I/O) পোলিং পর্ব শেষ হওয়ার সাথে সাথেই রান করে।

---

### **Q67: Explain how prototypal inheritance works in JavaScript. / JavaScript-এ প্রোটো টাইপাল ইনহেরিটেন্স (Prototypal Inheritance) কীভাবে কাজ করে ব্যাখ্যা করুন।**

**Answer (English):**
Prototypal inheritance is JavaScript's mechanism where objects inherit properties and methods directly from other objects via an internal link called `[[Prototype]]` (accessed via `__proto__` or `Object.getPrototypeOf()`).
*   When a property is accessed on an object, JS first checks the object itself. If not found, it traverses up the internal prototype link to its prototype object, continuing up until it finds the property or reaches `null`.

**অনুবাদ (Bangla Translation):**
প্রোটোটাইপাল ইনহেরিটেন্স হলো জাভাস্ক্রিপ্টের এমন একটি মেকানিজম যার মাধ্যমে একটি অবজেক্ট অন্য একটি অবজেক্টের মান ও মেথড সরাসরি প্রোটোটাইপ লিন্কের (`[[Prototype]]` বা `__proto__`) মাধ্যমে ব্যবহার করতে পারে। কোনো প্রপার্টি অবজেক্টে না থাকলে ব্রাউজার প্রোটোটাইপ ধরে ওপরে উঠতে থাকে এবং মান খুঁজে বের করে।

---

### **Q68: What is the prototype chain and how does it work? / Prototype chain কী এবং এটি কীভাবে কাজ করে?**

**Answer (English):**
The prototype chain is a linked series of object references. Every object points to a prototype object, which in turn points to its own prototype object, ending at `Object.prototype`, whose prototype is `null`. Property lookups travel up this chain sequentially until reaching `null`.

**অনুবাদ (Bangla Translation):**
প্রোটোটাইপ চেইন হলো অবজেক্টসমূহের একটি পারস্পরিক শৃঙ্খল বা লিঙ্কড লিস্ট। প্রতিটি অবজেক্ট তার প্রোটোটাইপ অবজেক্টকে নির্দেশ করে, যা আবার তার নিজস্ব প্রোটোটাইপকে নির্দেশ করতে করতে শেষে `Object.prototype`-এ পৌঁছায় (যার শেষ মান `null`)।

---

### **Q69: Explain the difference between classical inheritance and prototypal inheritance. / Classical inheritance এবং Prototypal inheritance এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Classical Inheritance (Java, C++):** Class-based model. Classes serve as rigid blueprints, and instances are created by copying class structures. Classes inherit from other classes.
*   **Prototypal Inheritance (JavaScript):** Object-based model. Objects inherit directly from other objects without rigid class blueprints. Objects are dynamically linked at runtime via prototype delegation.

**অনুবাদ (Bangla Translation):**
*   **Classical Inheritance (ক্লাসিক্যাল ইনহেরিটেন্স):** এটি ক্লাস-বেসড মডেল (যেমন Java বা C++)। এতে ক্লাস তৈরি করে অবজেক্টের স্ট্রাকচার ব্লুপ্রিন্ট বানান হয় এবং ক্লাস অন্য ক্লাসকে ইনহেরিট করে।
*   **Prototypal Inheritance (প্রোটোটাইপাল ইনহেরিটেন্স):** এটি অবজেক্ট-বেসড মডেল (JavaScript)। এতে কোনো ব্লুপ্রিন্ট ছাড়াই সরাসরি একটি অবজেক্ট অন্য অবজেক্টকে লিংক করে মান শেয়ার করে।

---

### **Q70: Explain the concept of inheritance in ES2015 classes. / ES2015 ক্লাসে ইনহেরিটেন্স (Inheritance) ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
ES2015 introduced modern class syntax using `extends` and `super` keywords as syntactic sugar over prototypal inheritance.
*   **`extends`:** Allows a subclass to inherit methods and static properties from a parent class.
*   **`super()`:** Must be called inside the child class constructor to execute the parent class constructor and correctly initialize `this`.
*   **Example:**
    ```javascript
    class Animal {
      constructor(name) { this.name = name; }
    }
    class Dog extends Animal {
      constructor(name, breed) {
        super(name); // Call parent constructor
        this.breed = breed;
      }
    }
    ```

**অনুবাদ (Bangla Translation):**
ES2015-এ প্রোটোটাইপাল ইনহেরিটেন্স সহজ করার জন্য `extends` এবং `super` কিওয়ার্ড নিয়ে আসা হয়।
*   **`extends`:** এর মাধ্যমে চাইল্ড ক্লাস প্যারেন্ট ক্লাসের বৈশিষ্ট্যগুলো গ্রহণ করে।
*   **`super()`:** চাইল্ড ক্লাসের কন্সট্রাক্টরের ভেতর `super()` কল করে প্যারেন্ট ক্লাসের কন্সট্রাক্টর ও `this` ইনিশিয়ালাইজ করতে হয়।
*   **উদাহরণ:**
    ```javascript
    class Animal {
      constructor(name) { this.name = name; }
    }
    class Dog extends Animal {
      constructor(name, breed) {
        super(name); // প্যারেন্ট কন্সট্রাক্টর কল
        this.breed = breed;
      }
    }
    ```
