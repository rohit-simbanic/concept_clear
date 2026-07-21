# JavaScript Interview Questions Guide: Volume 1 (Questions 1 - 35)

This guide contains detailed answers in English alongside complete Bangla translations for questions 1 to 35 from the uploaded JavaScript Interview Questions PDF.

---

### **Q1: What are the various data types in JavaScript? / JavaScript-এ বিভিন্ন ডাটা টাইপসমূহ কী কী?**

**Answer (English):**
In JavaScript, data types are divided into two main categories:
1.  **Primitive Data Types:** Store a single value directly in Stack memory. They are immutable.
    *   `Number`: Represents integers and floating-point numbers.
    *   `String`: Represents sequences of characters.
    *   `Boolean`: Represents `true` or `false`.
    *   `Undefined`: A variable that has been declared but not assigned a value.
    *   `Null`: Represents the intentional absence of any object value.
    *   `Symbol`: Unique and immutable identifier (ES6).
    *   `BigInt`: Represents integers with arbitrary precision for very large numbers.
2.  **Non-primitive (Reference) Data Types:** Store collections of data or complex entities in Heap memory. They are mutable.
    *   `Object`, `Array`, `Function`, `Date`, `RegExp`, `Map`, `Set`.

**অনুবাদ (Bangla Translation):**
JavaScript-এ ডাটা টাইপগুলোকে প্রধানত দুটি ভাগে ভাগ করা হয়:
1.  **Primitive (মৌলিক) ডাটা টাইপ:** এগুলো সরাসরি স্ট্যাক মেমোরিতে একটি সিঙ্গেল মান জমা রাখে এবং এগুলো অপরিবর্তনযোগ্য (Immutable)।
    *   `Number`: পূর্ণসংখ্যা এবং দশমিক সংখ্যা নির্দেশ করে।
    *   `String`: অক্ষর বা লেখার সমষ্টি নির্দেশ করে।
    *   `Boolean`: সত্য (`true`) অথবা মিথ্যা (`false`) নির্দেশ করে।
    *   `Undefined`: ভ্যারিয়েবল ডিক্লেয়ার করা হয়েছে কিন্তু কোনো মান দেওয়া হয়নি।
    *   `Null`: অবজেক্টের মানের শূন্যতা বা অনুপস্থিতি নির্দেশ করে।
    *   `Symbol`: ইউনিক ও অপরিবর্তনশীল আইডেন্টিফায়ার (ES6)।
    *   `BigInt`: সাধারণ লিমিটের চেয়ে বড় সংখ্যার নির্ভুল হিসাবের জন্য ব্যবহৃত হয়।
2.  **Non-primitive / Reference (যৌগিক) ডাটা টাইপ:** এগুলো হিপ মেমোরিতে জটিল ডেটা স্ট্রাকচার বা অবজেক্টের কালেকশন স্টোর করে এবং এগুলো পরিবর্তনযোগ্য (Mutable)।
    *   `Object`, `Array`, `Function`, `Date`, `RegExp`, `Map`, `Set` ইত্যাদি।

---

### **Q2: How do you check the data type of a variable? / কীভাবে কোনো ভ্যারিয়েবলের ডাটা টাইপ চেক করবেন?**

**Answer (English):**
You can use the `typeof` operator to check the data type of a variable. It returns a string representing the type.
*   **Examples:**
    ```javascript
    typeof "Hello"   // "string"
    typeof 42        // "number"
    typeof true      // "boolean"
    typeof undefined // "undefined"
    typeof Symbol()  // "symbol"
    typeof {}        // "object"
    typeof function(){} // "function"
    ```
*   **Edge Cases:**
    *   For arrays: `typeof []` returns `"object"`. Use `Array.isArray(variableName)` to reliably check for arrays.
    *   For null: `typeof null` returns `"object"`. Use `variableName === null` to check for null.

**অনুবাদ (Bangla Translation):**
কোনো ভ্যারিয়েবলের ডাটা টাইপ জানার জন্য জাভাস্ক্রিপ্টে `typeof` অপারেটর ব্যবহার করা হয়। এটি মানের টাইপ অনুযায়ী একটি স্ট্রিং রিটার্ন করে।
*   **উদাহরণ:**
    ```javascript
    typeof "Hello"   // "string"
    typeof 42        // "number"
    typeof {}        // "object"
    ```
*   **ব্যতিক্রমসমূহ:**
    *   অ্যারের ক্ষেত্রে: `typeof []` এর মান `"object"` দেখায়। তাই অ্যারে নিশ্চিত করতে `Array.isArray(variableName)` ব্যবহার করতে হবে।
    *   Null এর ক্ষেত্রে: `typeof null` এর মান `"object"` দেখায়। তাই সঠিক চেক করার জন্য `variableName === null` ব্যবহার করতে হয়।

---

### **Q3: What’s the difference between a JavaScript variable that is: null, undefined or undeclared? / null, undefined এবং undeclared ভ্যারিয়েবলের মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`null`:** Explicitly assigned by the developer to represent the intentional absence of any value. Its type is `'object'`. It is equal to undefined under loose comparison (`==`) but not strict comparison (`===`).
*   **`undefined`:** Indicates that a variable has been declared in the code but has not been assigned a value yet. Its type is `'undefined'`.
*   **Undeclared:** A variable that has not been declared at all using `var`, `let`, or `const`. Accessing it throws a `ReferenceError`.

**অনুবাদ (Bangla Translation):**
*   **`null`:** এটি ডেভেলপার নিজে থেকে ভ্যারিয়েবলের মান খালি বা অনুপস্থিত বোঝাতে অ্যাসাইন করেন। এর টাইপ হলো `'object'`।
*   **`undefined`:** এটি নির্দেশ করে যে ভ্যারিয়েবলটি কোডে ডিক্লেয়ার করা হয়েছে কিন্তু এখনো কোনো মান সেট করা হয়নি। এর টাইপ হলো `'undefined'`।
*   **Undeclared (ডিক্লেয়ার না করা):** এই ভ্যারিয়েবলটি কোডের কোথাও `var`, `let` বা `const` দিয়ে তৈরিই করা হয়নি। এটি অ্যাক্সেস করতে গেলে ব্রাউজার `ReferenceError` ছুড়ে দেয়।

---

### **Q4: What are the differences between JavaScript variables created using let, var or const? / let, var এবং const দিয়ে তৈরি করা ভ্যারিয়েবলগুলোর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`var`:** Function-scoped or globally-scoped. Can be redeclared and reassigned. It is hoisted to the top of its scope and initialized with `undefined`.
*   **`let`:** Block-scoped. Cannot be redeclared within the same scope, but can be reassigned. Hoisted to the top of the block but not initialized (stays in the Temporal Dead Zone, throwing a `ReferenceError` if accessed early).
*   **`const`:** Block-scoped. Cannot be redeclared or reassigned. Requires an immediate initialization upon declaration. Hoisted to the Temporal Dead Zone just like `let`.

**অনুবাদ (Bangla Translation):**
*   **`var`:** এটি ফাংশন স্কোপড বা গ্লোবাল স্কোপড। একই ভ্যারিয়েবল পুনরায় ডিক্লেয়ার এবং রি-অ্যাসাইন করা যায়। এটি হোইস্ট হয়ে শুরুতে `undefined` মান নিয়ে মেমোরিতে থাকে।
*   **`let`:** এটি ব্লক স্কোপড (কার্লি ব্র্যাকেটের ভেতরের অংশ)। এটি একই ব্লকে রি-ডিক্লেয়ার করা যায় না, তবে রি-অ্যাসাইন করা যায়। এটি হোইস্ট হলেও ইনিশিয়ালাইজ হয় না (Temporal Dead Zone এ থাকে বিধায় ডিক্লেয়ারেশনের আগে কল করলে `ReferenceError` দেয়)।
*   **`const`:** এটিও ব্লক স্কোপড। এটি রি-ডিক্লেয়ার বা রি-অ্যাসাইন করা যায় না এবং তৈরির সময়ই মান দেওয়া বাধ্যতামূলক। এটিও হোইস্ট হওয়ার পর ডিক্লেয়ারেশনের আগে ব্যবহার করতে গেলে এরর দেখায়।

---

### **Q5: Why is it, in general, a good idea to leave the global JavaScript scope of a website as-is and never touch it? / সাধারণত ওয়েবসাইটের গ্লোবাল স্কোপ যেমন আছে তেমন রাখা এবং তা পরিবর্তন না করা কেন ভালো অভ্যাস?**

**Answer (English):**
Polluting the global scope (the `window` object in browsers) is considered a bad practice due to:
1.  **Naming Conflicts:** Different scripts might define the same global variable name, overwriting each other and causing silent bugs.
2.  **Cluttered Namespace:** Makes the codebase hard to manage, debug, and maintain.
3.  **Scope Leaks & Memory Leaks:** Global variables are not garbage collected as long as the page is open, leading to memory overhead.
4.  **Modularity & Encapsulation:** Good code design isolates functions and variables in their respective module/block scopes.
5.  **Security Concerns:** Malicious scripts running on the page can easily read or modify global data.

**অনুবাদ (Bangla Translation):**
গ্লোবাল স্কোপ (ব্রাউজারে `window` অবজেক্ট) নোংরা বা দূষিত না করা একটি ভালো কোডিং অভ্যাস কারণ:
1.  **নামের সংঘর্ষ (Naming Conflicts):** একাধিক স্ক্রিপ্ট একই নামে গ্লোবাল ভ্যারিয়েবল ডিক্লেয়ার করলে একটির মান অন্যটিকে ওভাররাইট করে কোডে অপ্রত্যাশিত বাগ তৈরি করে।
2.  **জটিল কোডবেস:** কোড বড় হলে ডিবাগিং এবং মেইনটেইন করা অত্যন্ত কঠিন হয়ে পড়ে।
3.  **মেমোরি লিক (Memory Leaks):** পেজ চালু থাকা পর্যন্ত গ্লোবাল ভ্যারিয়েবল মেমোরি থেকে মুছে যায় না, যা ব্রাউজারের মেমোরি নষ্ট করে।
4.  **মডুলারিটি ও এনক্যাপসুলেশন:** আদর্শ কোড ডিজাইন ভ্যারিয়েবল ও ফাংশনকে তাদের নিজস্ব মডিউল বা লোকাল স্কোপে লক রাখে।
5.  **নিরাপত্তা ঝুঁকি:** গ্লোবাল ডাটা খুব সহজেই যেকোনো হ্যাকিং বা ক্ষতিকারক স্ক্রিপ্ট দিয়ে রিড ও এডিট করা যায়।

---

### **Q6: How do you convert a string to a number in JavaScript? / JavaScript-এ কীভাবে একটি স্ট্রিং-কে নাম্বারে রূপান্তর করবেন?**

**Answer (English):**
You can convert a string to a number using several built-in methods:
1.  **`Number(str)`:** Converts the entire string to a number. Returns `NaN` if it contains invalid characters (e.g., `Number("123")` -> `123`).
2.  **`parseInt(str, radix)`:** Parses the string from left to right and returns an integer (e.g., `parseInt("123.45")` -> `123`).
3.  **`parseFloat(str)`:** Parses the string and returns a floating-point decimal (e.g., `parseFloat("123.45")` -> `123.45`).
4.  **Unary Plus operator (`+`):** The fastest shorthand method (e.g., `+"123"` -> `123`).

**অনুবাদ (Bangla Translation):**
জাভাস্ক্রিপ্টে স্ট্রিং থেকে নাম্বারে রূপান্তরের কয়েকটি জনপ্রিয় পদ্ধতি রয়েছে:
1.  **`Number(str)`:** পুরো স্ট্রিংটিকে নাম্বারে রূপান্তর করে। অবৈধ ক্যারেক্টার থাকলে `NaN` রিটার্ন করে (যেমন- `Number("123")` -> `123`)।
2.  **`parseInt(str)`:** স্ট্রিংয়ের বাম থেকে পড়ে শুধুমাত্র পূর্ণসংখ্যা অংশটি রিটার্ন করে (যেমন- `parseInt("123.45")` -> `123`)।
3.  **`parseFloat(str)`:** স্ট্রিংটি প্রসেস করে দশমিক সহ মান রিটার্ন করে (যেমন- `parseFloat("123.45")` -> `123.45`)।
4.  **ইউনারি প্লাস (`+`):** এটি নাম্বারে রূপান্তর করার সবচেয়ে দ্রুততম সংক্ষিপ্ত উপায় (যেমন- `+"123"` -> `123`)।

---

### **Q7: What are template literals and how are they used? / Template literals কী এবং কীভাবে এগুলো ব্যবহার করা হয়?**

**Answer (English):**
Template literals are string literals enclosed by backticks (`` ` ``) instead of single or double quotes.
*   **Usage Features:**
    1.  **String Interpolation:** Allows embedding expressions or variables directly inside the string using the `${expression}` syntax.
    2.  **Multi-line Strings:** Preserves newlines and spaces directly in the code without needing `\n`.
*   **Example:**
    ```javascript
    const myName = 'John';
    const greeting = `Hello, ${myName}!
    Welcome to JavaScript.`;
    ```

**অনুবাদ (Bangla Translation):**
টেমপ্লেট লিটারেলস হলো ব্যাকটিক (`` ` ``) চিহ্নের ভেতরে লেখা বিশেষ স্ট্রিং ফরম্যাট।
*   **ব্যবহারের সুবিধাসমূহ:**
    1.  **স্ট্রিং ইন্টারপোলেশন:** স্ট্রিংয়ের ভেতরে সরাসরি `${expression}` লিখে যেকোনো ভ্যারিয়েবল বা এক্সপ্রেশনের ডাইনামিক মান বসানো যায়।
    2.  **মাল্টি-লাইন স্ট্রিং:** কোনো `\n` ব্যবহার ছাড়াই সরাসরি কোডের ভেতরের নতুন লাইন বা এন্টার কি-এর স্পেসিং ধরে রাখে।
*   **উদাহরণ:**
    ```javascript
    const myName = 'John';
    const greeting = `Hello, ${myName}!
    Welcome to JavaScript.`;
    ```

---

### **Q8: Explain the concept of tagged templates. / Tagged templates ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
Tagged templates allow you to parse template literals with a custom function. The tag function receives the literal string segments as an array for its first argument, and the evaluated expressions as subsequent arguments (or collected via rest parameter).
*   **Example:**
    ```javascript
    function tag(strings, ...values) {
      return strings[0] + values[0] + strings[1] + values[1] + strings[2];
    }
    const result = tag`Hello ${'world'}! How are ${'you'}?`;
    // result = "Hello world! How are you?"
    ```
*   **Use Cases:** Used in libraries like `styled-components` for CSS-in-JS, sanitizing HTML inputs, or localization translation.

**অনুবাদ (Bangla Translation):**
ট্যাগড টেমপ্লেট হলো এমন একটি পদ্ধতি যার মাধ্যমে কোনো টেমপ্লেট লিটারেলকে একটি ফাংশনের সাহায্যে পার্স বা রান করা যায়। ট্যাগ ফাংশনটি প্রথম আর্গুমেন্ট হিসেবে সাধারণ স্ট্রিং অংশগুলোর একটি অ্যারে পায় এবং পরবর্তী আর্গুমেন্টগুলোতে ডাইনামিক ভ্যালুগুলো পায়।
*   **উদাহরণ:**
    ```javascript
    function tag(strings, ...values) {
      return strings[0] + values[0] + strings[1] + values[1] + strings[2];
    }
    const result = tag`Hello ${'world'}! How are ${'you'}?`;
    ```
*   **ব্যবহার:** এটি সিএসএস-ইন-জেএস লাইব্রেরি (যেমন `styled-components`), এইচটিএমএল ইনপুট পিউরিফাই করা বা ভাষা রূপান্তরের কাজে ব্যবহৃত হয়।

---

### **Q9: What is the spread operator and how is it used? / Spread operator কী এবং কীভাবে এটি ব্যবহার করা হয়?**

**Answer (English):**
The spread operator, represented by three dots (`...`), is used to expand or spread iterable objects (like arrays or strings) into individual elements, or copy/merge key-value pairs of objects.
*   **Common Uses:**
    1.  **Cloning Arrays/Objects:** `const copy = [...originalArray];`
    2.  **Merging Arrays:** `const merged = [...arr1, ...arr2];`
    3.  **Merging Objects:** `const newObj = { ...obj1, ...obj2 };`
    4.  **Passing arguments to functions:** `Math.max(...numbers);`

**অনুবাদ (Bangla Translation):**
স্প্রেড অপারেটরকে তিনটি ডট (`...`) দিয়ে প্রকাশ করা হয়। এটি কোনো ইটারেবল অবজেক্টকে (যেমন অ্যারে বা স্ট্রিং) ভেঙে তার ভেতরের উপাদানগুলোকে আলাদা করতে অথবা অবজেক্টের প্রপার্টিগুলোকে ছড়িয়ে দিয়ে নতুন অবজেক্ট বানাতে ব্যবহৃত হয়।
*   **প্রধান ব্যবহারসমূহ:**
    1.  **অ্যারে বা অবজেক্ট কপি করা:** `const copy = [...originalArray];`
    2.  **একাধিক অ্যারে একত্র করা:** `const merged = [...arr1, ...arr2];`
    3.  **একাধিক অবজেক্ট মার্জ করা:** `const newObj = { ...obj1, ...obj2 };`
    4.  **ফাংশনে আর্গুমেন্ট পাস করা:** `Math.max(...numbers);`

---

### **Q10: What are Symbols used for in JavaScript? / JavaScript-এ Symbols কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
Symbols are a primitive data type introduced in ES6. Every Symbol value returned from the `Symbol()` function is completely unique and immutable.
*   **Key Uses:**
    1.  **Unique Object Property Keys:** Prevents naming collisions when adding properties to an object, especially when combining different libraries or modules.
    2.  **Creating Private/Hidden Properties:** Symbol properties are not enumerable, meaning they do not show up in `for...in` loops or `Object.keys()`. They can only be accessed using `Object.getOwnPropertySymbols()`.

**অনুবাদ (Bangla Translation):**
সিম্বল (Symbol) হলো ES6-এ আসা একটি প্রিমিটিভ ডাটা টাইপ। `Symbol()` ফাংশন দিয়ে তৈরি করা প্রতিটি মান ব্রাউজারে সম্পূর্ণ অনন্য (Unique) এবং অপরিবর্তনশীল হয়।
*   **মূল ব্যবহারসমূহ:**
    1.  **অনন্য অবজেক্ট প্রপার্টি কি (Key):** অবজেক্টের ভেতরে ইউনিক প্রপার্টি তৈরি করতে এটি ব্যবহৃত হয়, যাতে অন্য কোনো থার্ড-পার্টি কোডের সাথে নামের কনফ্লিক্ট বা সংঘর্ষ না হয়।
    2.  **লুকানো প্রপার্টি তৈরি:** সিম্বল দিয়ে ডিফাইন করা প্রপার্টিগুলো `for...in` লুপ বা `Object.keys()` এ ধরা পড়ে না, ফলে ডেটা হাইডিং বা অবজেক্টের ইন্টারনাল স্টেট সুরক্ষিত রাখা যায়।

---

### **Q11: What are proxies in JavaScript used for? / JavaScript-এ proxies কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
A `Proxy` object wraps another target object and allows you to intercept and customize its fundamental operations (such as property lookup, assignment, enumeration, and function invocation).
*   **Use Cases:**
    1.  **Property Assignment Validation:** Validating type/range of data before writing to an object.
    2.  **Logging and Debugging:** Creating wrappers to log every read/write operation.
    3.  **Reactivity Systems:** Triggering UI updates dynamically when object properties change (this is how Vue.js 3 reactivity works).
*   **Example Syntax:**
    ```javascript
    const proxy = new Proxy(targetObject, {
      get(target, prop) {
        console.log(`Accessing ${prop}`);
        return target[prop];
      }
    });
    ```

**অনুবাদ (Bangla Translation):**
জাভাস্ক্রিপ্টে `Proxy` হলো এমন একটি অবজেক্ট যা অন্য একটি টার্গেট অবজেক্টকে র্যাপ বা কভার করে তার সাধারণ কার্যকলাপসমূহ (যেমন- প্রপার্টি রিড, রাইট, ফাংশন কল) ইন্টারসেপ্ট করে তার আচরণ কাস্টমাইজ করতে সাহায্য করে।
*   **ব্যবহারের ক্ষেত্রসমূহ:**
    1.  **ডাটা ভ্যালিডেশন:** অবজেক্টে কোনো মান সেভ করার আগে তা ঠিক আছে কি না তা যাচাই করা।
    2.  **লগিং ও ডিবাগিং:** প্রতিবার অবজেক্টের ভ্যালু অ্যাক্সেস করার সময় ট্র্যাক বা লগ রাখা।
    3.  **রিঅ্যাক্টিভ সিস্টেম:** অবজেক্টের মান বদলানোর সাথে সাথে ডাইনামিকালি ইউজার ইন্টারফেস আপডেট করা (Vue.js 3 এ এটি ব্যবহৃত হয়)।

---

### **Q12: Explain the concept of "hoisting" in JavaScript. / JavaScript-এ "hoisting" ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
Hoisting is JavaScript's default behavior of moving variable and function declarations to the top of their containing scope during the compile phase before code execution.
*   **Hoisting Rules:**
    *   `var` variables are hoisted and initialized with `undefined`.
    *   `let` and `const` variables are hoisted but remain uninitialized in the Temporal Dead Zone (TDZ).
    *   Function declarations are fully hoisted (both declaration and body), meaning they can be called before being defined physically in the code.
    *   Function expressions are not hoisted as functions, only their variable declaration is hoisted.

**অনুবাদ (Bangla Translation):**
হোইস্টিং (Hoisting) হলো জাভাস্ক্রিপ্টের এমন একটি আচরণ যার কারণে কোড রান করার আগেই মেমোরি ফেজে ভ্যারিয়েবল ও ফাংশন ডিক্লেয়ারেশনগুলো তাদের স্কোপের সবার ওপরে চলে যায় বলে মনে হয়।
*   **হোইস্টিংয়ের নিয়মাবলী:**
    *   `var` দিয়ে ডিক্লেয়ার করা ভ্যারিয়েবল হোইস্ট হয়ে `undefined` দিয়ে মেমোরি পায়।
    *   `let` ও `const` হোইস্ট হলেও ইনিশিয়ালাইজ হয় না এবং ব্যবহারের আগ পর্যন্ত TDZ জোন-এ লক থাকে।
    *   সাধারণ ফাংশন ডিক্লেয়ারেশন সম্পূর্ণ হোইস্ট হয় (বডি সহ), ফলে ডিক্লেয়ার করার আগেই ফাংশন কল করা সম্ভব হয়।
    *   ফাংশন এক্সপ্রেশন (যেমন- অ্যারো ফাংশন) সম্পূর্ণ হোইস্ট হয় না, কেবল তার ভ্যারিয়েবল অংশটি হোইস্ট হয়।

---

### **Q13: Explain the difference in hoisting between var, let, and const. / var, let এবং const এর হোইস্টিং আচরণের মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`var`:** Hoisted to the top of its scope and initialized with `undefined`. If accessed before declaration, it returns `undefined` instead of throwing an error.
*   **`let` & `const`:** Hoisted to the top of their scope but not initialized. They enter the **Temporal Dead Zone (TDZ)**. If accessed before their declaration line is executed, the JavaScript engine throws a `ReferenceError: Cannot access variable before initialization`.
*   Additionally, `const` requires an initial assignment at compile time, whereas `let` can be declared empty.

**অনুবাদ (Bangla Translation):**
*   **`var`:** এটি হোইস্ট হয়ে মেমোরিতে সরাসরি `undefined` ভ্যালু সেট করে। তাই ডিক্লেয়ার করার আগে এটি প্রিন্ট করতে গেলে কোনো এরর না দিয়ে `undefined` দেখায়।
*   **`let` এবং `const`:** এরাও হোইস্ট হয় কিন্তু মেমোরিতে কোনো ইনিশিয়াল ভ্যালু পায় না এবং **Temporal Dead Zone (TDZ)**-এ অবস্থান করে। ডিক্লেয়ার করার আগে এদের অ্যাক্সেস করতে গেলে ব্রাউজার `ReferenceError` দেখাবে।
*   অতিরিক্ত পার্থক্য হলো, `const`-এর ডিক্লেয়ারেশনের সময়েই ভ্যালু অ্যাসাইন করতে হয়, যা `let` এর ক্ষেত্রে ফাঁকা রাখা সম্ভব।

---

### **Q14: How does hoisting affect function declarations and expressions? / হোইস্টিং কীভাবে ফাংশন ডিক্লেয়ারেশন ও ফাংশন এক্সপ্রেশনকে প্রভাবিত করে?**

**Answer (English):**
*   **Function Declarations:** The entire function body is hoisted. You can call the function *before* its line of definition in the code without any errors.
    ```javascript
    foo(); // Prints "Hello"
    function foo() { console.log("Hello"); }
    ```
*   **Function Expressions:** Only the variable holding the function is hoisted (following its declaration keyword rule). The function body assignment is executed only at runtime. Calling it early throws an error:
    ```javascript
    bar(); // Throws TypeError: bar is not a function (if var bar = ...)
    var bar = function() { console.log("Hi"); };
    ```

**অনুবাদ (Bangla Translation):**
*   **ফাংশন ডিক্লেয়ারেশন:** এর সম্পূর্ণ ফাংশন বডি মেমোরিতে হোইস্ট হয়। তাই কোডে ফাংশন লেখার পূর্বেই একে কল করলে এটি সফলভাবে রান করে।
    ```javascript
    foo(); // আউটপুট: "Hello"
    function foo() { console.log("Hello"); }
    ```
*   **ফাংশন এক্সপ্রেশন:** এখানে কেবল ফাংশন ধারণকারী ভ্যারিয়েবলটি হোইস্ট হয়, অ্যাসাইনমেন্টটি রান টাইমে ঘটে। ডিক্লেয়ার করার আগে কল করলে এরর দেখাবে:
    ```javascript
    bar(); // TypeError: bar is not a function
    var bar = function() { console.log("Hi"); };
    ```

---

### **Q15: What are the potential issues caused by hoisting? / হোইস্টিংয়ের কারণে কী কী সম্ভাব্য সমস্যা তৈরি হতে পারে?**

**Answer (English):**
1.  **Unexpected `undefined` Values:** Accessing a `var` variable early returns `undefined` silently instead of crashing, which can lead to unexpected logic outcomes.
2.  **Accidental Global Variables:** If strict mode is not enabled, assigning a value to an undeclared variable implicitly creates a global variable.
3.  **Function Execution Errors:** Calling a function expression before its definition crashes the application with a `TypeError`.
4.  **Debugging Complexity:** The code behavior might look confusing since the runtime flow doesn't match the physical file ordering.

**অনুবাদ (Bangla Translation):**
1.  **অপ্রত্যাশিত `undefined` মান:** `var` ভ্যারিয়েবল ডিক্লেয়ার করার আগে কল করলে এরর না দিয়ে `undefined` রিটার্ন করে, যা লজিক্যাল বাগ তৈরি করতে পারে।
2.  **অনাকাঙ্ক্ষিত গ্লোবাল ভ্যারিয়েবল:** strict mode না থাকলে ডিক্লেয়ার না করা ভ্যারিয়েবলে ভ্যালু সেট করলে তা গ্লোবাল উইন্ডো প্রপার্টি হয়ে যায়।
3.  **ফাংশন এক্সিকিউশন এরর:** ফাংশন এক্সপ্রেশনকে আগে কল করলে `TypeError` দিয়ে অ্যাপ ক্র্যাশ করে।
4.  **ডিবাগিংয়ের জটিলতা:** কোড ফিজিক্যালি যেভাবে সাজানো রানটাইমে তার হোইস্টিং আচরণ আলাদা হওয়ায় ডেভেলপার ডিবাগ করতে গিয়ে বিভ্রান্ত হতে পারেন।

---

### **Q16: How can you avoid problems related to hoisting? / হোইস্টিং সংক্রান্ত সমস্যাগুলো কীভাবে এড়িয়ে চলবেন?**

**Answer (English):**
1.  **Use `let` and `const`:** Always declare your variables using `let` or `const` instead of `var`. This ensures block scoping and triggers errors immediately if accessed early.
2.  **Declare Variables at the Top:** Make it a habit to declare all variables at the beginning of their respective function or block scopes.
3.  **Define Functions Before Calling:** Always write your function definitions before the lines where they are invoked.
4.  **Enable Strict Mode:** Add `"use strict";` at the top of your scripts to prevent accidental global variable creation.

**অনুবাদ (Bangla Translation):**
1.  **`let` ও `const` ব্যবহার করা:** ভ্যারিয়েবল তৈরির জন্য `var` পরিহার করে সবসময় `let` বা `const` ব্যবহার করতে হবে, যা হোইস্টিং বাগ আগেই এরর আকারে আটকে দেবে।
2.  **শুরুতে ডিক্লেয়ার করা:** সব ভ্যারিয়েবল তাদের নিজ নিজ স্কোপ বা ব্লকের একদম শুরুতে ডিক্লেয়ার করার অভ্যাস গড়ে তোলা।
3.  **কল করার আগে ডিফাইন করা:** যেকোনো ফাংশন ডিক্লেয়ার বা ডিফাইন করার পরেই কেবল তা কল করার সিকোয়েন্স বজায় রাখা।
4.  **Strict Mode অন করা:** ফাইলের ওপরে `"use strict";` ব্যবহার করা যাতে কোনো ডিক্লেয়ার না করা ভ্যারিয়েবল অটো-গ্লোবাল হতে না পারে।

---

### **Q17: What is the difference between == and === in JavaScript? / JavaScript-এ == এবং === এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`==` (Loose/Abstract Equality):** Compares two values for equality after performing **Type Coercion** (automatic conversion of data types). E.g., `5 == "5"` returns `true` because the string "5" is converted to a number.
*   **`===` (Strict Equality):** Compares both the **value** and the **data type** without performing type coercion. If the types are different, it immediately returns `false`. E.g., `5 === "5"` returns `false`.

**অনুবাদ (Bangla Translation):**
*   **`==` (Loose Equality):** এটি দুটি মানের ডাটা টাইপ চেক করার আগে টাইপ কোয়ার্সন (Type Coercion বা টাইপ কনভার্সন) করে মান সমান কি না চেক করে। যেমন- `5 == "5"` এর মান `true` হবে (কারণ এটি স্ট্রিংকে নাম্বারে কনভার্ট করে নিয়েছে)।
*   **`===` (Strict Equality):** এটি কোনো টাইপ কনভার্সন ছাড়াই একযোগে ভ্যালু বা মান এবং ডাটা টাইপ—উভয়টি তুলনা করে। টাইপ মিল না থাকলে সরাসরি `false` রিটার্ন করে। যেমন- `5 === "5"` এর মান `false` হবে।

---

### **Q18: What language constructs do you use for iterating over object properties and array items in JavaScript? / JavaScript-এ অবজেক্ট প্রপার্টি এবং অ্যারে আইটেম ইটারেট (লুপ) করার জন্য কোন কোন ল্যাঙ্গুয়েজ কনস্ট্রাক্ট ব্যবহার করবেন?**

**Answer (English):**
*   **For Objects:**
    1.  `for...in` loop: Iterates over all enumerable string properties of an object (always guard with `Object.hasOwn(obj, key)` to filter inherited properties).
    2.  `Object.keys(obj)` or `Object.values(obj)` paired with `forEach` loop.
*   **For Arrays:**
    1.  `for...of` loop: The modern and cleanest way to iterate over iterable array values directly.
    2.  `Array.prototype.forEach()`: Executes a callback function for each item with item index details.
    3.  Traditional `for` loop: `for(let i=0; i < arr.length; i++)`.
    4.  Functional methods: `map()`, `filter()`, `reduce()`.

**অনুবাদ (Bangla Translation):**
*   **অবজেক্টের ক্ষেত্রে:**
    1.  `for...in` লুপ: অবজেক্টের সব চাবি বা প্রপার্টির ওপর লুপ চালায় (উত্তরাধিকার সূত্রে পাওয়া চাবি এড়াতে `Object.hasOwn()` দিয়ে ফিল্টার করা ভালো)।
    2.  `Object.keys(obj)` বা `Object.values(obj)` বের করে তার ওপর `forEach` লুপ চালানো।
*   **অ্যারেল ক্ষেত্রে:**
    1.  `for...of` লুপ: অ্যারের প্রতিটি মানের ওপর সরাসরি লুপ চালানোর সবচেয়ে আধুনিক ও পঠনযোগ্য উপায়।
    2.  `forEach()` মেথড: প্রতিটি আইটেমের ইনডেক্স সহ কলব্যাক ফাংশন এক্সিকিউট করে।
    3.  সাধারণ `for` লুপ: ইনডেক্স কন্ট্রোল করে লুপ চালানো।
    4.  ফাংশনাল মেথডসমূহ: `map()`, `filter()`, `reduce()`।

---

### **Q19: What is the purpose of the break and continue statements? / break এবং continue স্টেটমেন্টের উদ্দেশ্য কী?**

**Answer (English):**
*   **`break` Statement:** Used to immediately terminate and exit the enclosing loop or `switch` statement. The control flow moves to the line immediately following the loop.
*   **`continue` Statement:** Used to skip the rest of the current loop iteration and immediately proceed to the evaluation of the next cycle of the loop.

**অনুবাদ (Bangla Translation):**
*   **`break` স্টেটমেন্ট:** চলমান লুপ বা `switch` ব্লক থেকে তাত্ক্ষণিকভাবে বের হয়ে লুপের কার্যক্রম বন্ধ করতে ব্যবহৃত হয়।
*   **`continue` স্টেটমেন্ট:** চলমান লুপের বর্তমান ইটারেশনের কাজ মাঝপথে স্কিপ বা এড়িয়ে গিয়ে সরাসরি পরবর্তী ইটারেশন বা লুপের পরবর্তী চক্করে চলে যায়।

---

### **Q20: What is the purpose of the ternary operator and how is it used? / Ternary operator এর উদ্দেশ্য কী এবং এটি কীভাবে ব্যবহার করা হয়?**

**Answer (English):**
The ternary operator is a shorthand way of writing simple `if-else` conditional expressions in JavaScript. It is the only operator in JS that takes three operands: a condition, expression to execute if true, and expression to execute if false.
*   **Syntax:** `condition ? exprIfTrue : exprIfFalse`
*   **Example:**
    ```javascript
    const result = (age >= 18) ? "Adult" : "Minor";
    ```

**অনুবাদ (Bangla Translation):**
টার্নারি অপারেটর হলো জাভাস্ক্রিপ্টে ছোটখাটো `if-else` কন্ডিশনকে এক লাইনে সংক্ষেপে লেখার মেথড। এটি জাভাস্ক্রিপ্টের একমাত্র অপারেটর যা তিনটি অংশ নিয়ে কাজ করে: কন্ডিশন, সত্য হলে রিটার্ন ভ্যালু এবং মিথ্যা হলে রিটার্ন ভ্যালু।
*   **সিনট্যাক্স:** `condition ? exprIfTrue : exprIfFalse`
*   **উদাহরণ:**
    ```javascript
    const result = (age >= 18) ? "Adult" : "Minor";
    ```

---

### **Q21: How do you access the index of an element in an array during iteration? / অ্যারে ইটারেশন বা লুপের সময় কীভাবে কোনো এলিমেন্টের ইনডেক্স অ্যাক্সেস করবেন?**

**Answer (English):**
You can access the index in several ways:
1.  **`Array.prototype.forEach`:** The index is passed as the second parameter in the callback.
    ```javascript
    array.forEach((element, index) => { console.log(index, element); });
    ```
2.  **`for...of` with `entries()`:** Use array destructuring on `.entries()`.
    ```javascript
    for (const [index, element] of array.entries()) { console.log(index, element); }
    ```
3.  **Traditional `for` loop:** Access the loop counter directly (`array[i]`).

**অনুবাদ (Bangla Translation):**
অ্যারে লুপ চলার সময় ইনডেক্স অ্যাক্সেস করার কয়েকটি পদ্ধতি নিচে দেওয়া হলো:
1.  **`forEach` ব্যবহার করে:** এর কলব্যাক ফাংশনে দ্বিতীয় প্যারামিটার হিসেবে ইনডেক্স পাওয়া যায়।
    ```javascript
    array.forEach((element, index) => { console.log(index, element); });
    ```
2.  **`entries()` সহ `for...of` লুপ:** অ্যারের `.entries()` থেকে ইনডেক্স ও আইটেম ডিস্ট্রাকচার করে নেওয়া যায়।
    ```javascript
    for (const [index, element] of array.entries()) { console.log(index, element); }
    ```
3.  **সাধারণ `for` লুপ:** সরাসরি লুপ কাউন্টার ভ্যারিয়েবলটি ব্যবহার করে।

---

### **Q22: What is the purpose of the switch statement? / switch স্টেটমেন্টের উদ্দেশ্য কী?**

**Answer (English):**
The `switch` statement evaluates an expression and matches its value against multiple `case` labels. When a match is found, the block of code associated with that case is executed. It is used as a clean alternative to write long, messy `if...else if...else` chains. 
*Note:* A `break` statement is required at the end of each case block to prevent the execution from falling through to the next case automatically.

**অনুবাদ (Bangla Translation):**
`switch` স্টেটমেন্ট কোনো একটি এক্সপ্রেশনের মানের ওপর ভিত্তি করে একাধিক `case` লেবেলের সাথে তুলনা করে ম্যাচিং ব্লকের কোড রান করতে ব্যবহৃত হয়। এটি অনেক লম্বা ও নোংরা `if...else if...else` ব্লকের সুন্দর বিকল্প হিসেবে কাজ করে।
*বিশেষ দ্রষ্টব্য:* প্রতিটি কেস ব্লকের শেষে `break` দেওয়া জরুরি, নতুবা কোড পরবর্তী কেসগুলোতেও স্বয়ংক্রিয়ভাবে ঢুকে যাবে (একে fall-through বলে)।

---

### **Q23: What are rest parameters and how are they used? / Rest parameters কী এবং কীভাবে এগুলো ব্যবহার করা হয়?**

**Answer (English):**
Rest parameters allow a function to accept an indefinite number of arguments as a single array. They are denoted by three dots (`...`) followed by the array name at the end of the function arguments list.
*   **Example:**
    ```javascript
    function sum(...numbers) {
      return numbers.reduce((acc, curr) => acc + curr, 0);
    }
    console.log(sum(1, 2, 3)); // 6
    ```
*   **Constraint:** The rest parameter must always be the very last parameter in the function definition.

**অনুবাদ (Bangla Translation):**
রেস্ট প্যারামিটার (Rest Parameter) হলো এমন একটি ফিচার যার মাধ্যমে একটি ফাংশন সীমাহীন আর্গুমেন্ট গ্রহণ করে একটি সিঙ্গেল অ্যারেতে রূপান্তর করতে পারে। এটি প্যারামিটার লিস্টের শেষে তিনটি ডট (`...`) এবং অ্যারের নাম দিয়ে লিখতে হয়।
*   **উদাহরণ:**
    ```javascript
    function sum(...numbers) {
      return numbers.reduce((acc, curr) => acc + curr, 0);
    }
    console.log(sum(1, 2, 3)); // ৬
    ```
*   **সীমাবদ্ধতা:** রেস্ট প্যারামিটার অবশ্যই প্যারামিটার লিস্টের সবার শেষে থাকতে হবে।

---

### **Q24: Explain the concept of the spread operator and its uses. / Spread operator এর ধারণা ও এর ব্যবহারসমূহ ব্যাখ্যা করুন।**

**Answer (English):**
(This is a duplicate of Q9 from the PDF index. Below is a summary).
The spread operator (`...`) spreads elements of an iterable (like an array or string) into individual parts. It is commonly used for:
*   Cloning arrays/objects: `const copy = [...arr];`
*   Concatenating arrays: `const merged = [...arr1, ...arr2];`
*   Spreading array items as function arguments: `myFunction(...arrayArg);`

**অনুবাদ (Bangla Translation):**
(এটি ইমেজের সূচী অনুযায়ী প্রশ্ন নং ৯ এর অনুরূপ। নিচে এর সারসংক্ষেপ দেওয়া হলো)।
স্প্রেড অপারেটর (`...`) কোনো অ্যারে বা কালেকশন ভেঙে তার আইটেমগুলোকে ছড়িয়ে দেয়। এর সাধারণ ব্যবহারসমূহ:
*   অ্যারে বা অবজেক্ট কপি করতে: `const copy = [...arr];`
*   একাধিক অ্যারে একত্র করতে: `const merged = [...arr1, ...arr2];`
*   ফাংশনে আর্গুমেন্ট পাস করতে: `myFunction(...arrayArg);`

---

### **Q25: What are the benefits of using spread syntax in JavaScript and how is it different from rest syntax? / JavaScript-এ spread সিনট্যাক্সের সুবিধা কী এবং এটি rest সিনট্যাক্স থেকে কীভাবে আলাদা?**

**Answer (English):**
*   **Benefits of Spread:** It provides a clean, modern, and readable declarative syntax for shallow-copying and merging arrays or objects, replacing legacy verbose methods like `arr.slice()`, `arr.concat()`, and `Object.assign()`.
*   **Differences:**
    *   **Spread (`...`)** **expands** an array or object into individual elements. It is used in *expressions* or *function calls* (e.g., `const newArr = [...oldArr]`).
    *   **Rest (`...`)** **collects/condenses** multiple loose arguments into a single array. It is used in *function parameter definitions* (e.g., `function foo(...args) {}`).

**অনুবাদ (Bangla Translation):**
*   **স্প্রেড সিনট্যাক্সের সুবিধা:** এটি কোনো অ্যারে বা অবজেক্ট কপি এবং একত্র করার জন্য খুবই পঠনযোগ্য ডিক্ল্যারেটিভ সিনট্যাক্স দেয়, যা আগের জটিল কোড যেমন `arr.concat()` বা `Object.assign()` এর ব্যবহার প্রতিস্থাপন করে।
*   **পার্থক্য:**
    *   **Spread:** এটি অ্যারেকে ভেঙে এর ভেতরের উপাদানগুলোকে *বাইরে ছড়িয়ে দেয়*। এটি এক্সপ্রেশন বা ফাংশন কল করার সময় ব্যবহৃত হয়।
    *   **Rest:** এটি একাধিক ছড়ানো মানকে *একত্র করে একটি অ্যারে বানায়*। এটি ফাংশন ডিক্লেয়ার করার সময় প্যারামিটারে ব্যবহৃত হয়।

---

### **Q26: What are iterators and generators in JavaScript and what are they used for? / JavaScript-এ iterators এবং generators কী এবং এগুলো কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
*   **Iterators:** Objects that implement a standard iterator protocol by having a `next()` method. This method returns an object containing `{ value: any, done: boolean }` where `done` indicates if iteration has ended.
*   **Generators:** Special functions written using `function*` syntax that can pause their execution and resume later. They use the `yield` keyword to output values. Calling a generator returns a generator-iterator object.
*   **Use Cases:** Useful for lazy evaluation (processing massive datasets only when needed to save memory), implementing custom loops, and handling data streams.

**অনুবাদ (Bangla Translation):**
*   **Iterators (ইটারেটর):** এটি এমন অবজেক্ট যা স্ট্যান্ডার্ড ইটারেশন প্রোটোকল মেনে চলে এবং যার একটি `next()` মেথড থাকে। এই মেথডটি প্রতি কলে `{ value, done }` অবজেক্ট রিটার্ন করে।
*   **Generators (জেনারেটর):** এটি `function*` এবং `yield` কিওয়ার্ড দিয়ে তৈরি বিশেষ ফাংশন যা রান করার মাঝে নিজেকে পজ (সাময়িক স্থগিত) করতে পারে এবং পরবর্তীতে পজ হওয়া স্থান থেকে পুনরায় চলা শুরু করতে পারে।
*   **ব্যবহার:** মেমোরি বাঁচাতে অলস মূল্যায়ন (Lazy Evaluation - যখন ডেটা দরকার তখনই লোড করা) এবং বড় বড় ডেটা স্ট্রিম প্রসেস করতে এটি ব্যবহৃত হয়।

---

### **Q27: Explain the differences on the usage of foo between function foo() {} and var foo = function() {} in JavaScript. / JavaScript-এ function foo() {} এবং var foo = function() {} ব্যবহারের মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`function foo() {}` (Function Declaration):** The function is fully hoisted (both name and body). It can be called anywhere in the scope, even before its physical line of declaration.
*   **`var foo = function() {}` (Function Expression):** The variable `foo` is hoisted as `undefined`, but the function assignment stays in its place. Calling `foo()` before the assignment line will result in a `TypeError: foo is not a function`.

**অনুবাদ (Bangla Translation):**
*   **`function foo() {}` (ফাংশন ডিক্লেয়ারেশন):** এই ফাংশনটি সম্পূর্ণ হোইস্ট হয়। ফলে ফাইলে লেখার আগেই একে কল করলে এটি সফলভাবে রান করে।
*   **`var foo = function() {}` (ফাংশন এক্সপ্রেশন):** এখানে কেবল `foo` ভ্যারিয়েবলটি হোইস্ট হয়ে `undefined` হয়, কিন্তু মূল ফাংশনটি স্বস্থানেই থাকে। তাই ডিক্লেয়ার করার আগে কল করলে `TypeError` এরর দেখায়।

---

### **Q28: What is the difference between a parameter and an argument? / Parameter এবং Argument এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Parameter:** A placeholder variable defined in the function's declaration/signature (e.g., `a` and `b` in `function add(a, b) {}`).
*   **Argument:** The actual, concrete value passed to the function when it is executed (e.g., `2` and `3` in `add(2, 3)`).

**অনুবাদ (Bangla Translation):**
*   **Parameter (প্যারামিটার):** এটি ফাংশন ডিক্লেয়ার করার সময় ব্র্যাকেটের ভেতর লেখা কন্টেইনার বা ভ্যারিয়েবলগুলোর নাম (যেমন: `function add(a, b)` এ `a` ও `b` হলো প্যারামিটার)।
*   **Argument (আর্গুমেন্ট):** এটি ফাংশন রান করার সময় প্যারামিটারে পাঠানো বাস্তব বা নির্দিষ্ট মান (যেমন: `add(2, 3)` এ `2` ও `3` হলো আর্গুমেন্ট)।

---

### **Q29: Explain the concept of hoisting with regards to functions. / ফাংশনের ক্ষেত্রে hoisting এর ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
Function hoisting allows function declarations to be lifted to the top of their enclosing scope. Because the engine hoists the entire function body, you can call the function safely before its definition in the code. However, this does not apply to function expressions or arrow functions (which follow variable hoisting constraints).

**অনুবাদ (Bangla Translation):**
ফাংশন হোইস্টিংয়ের কারণে ব্রাউজার ইঞ্জিন সম্পূর্ণ ফাংশন বডিকে স্কোপের সবার ওপরে নিয়ে যায়। এর ফলে কোডে ফাংশন লেখার আগেই নিরাপদে একে রান করা যায়। তবে এটি ফাংশন এক্সপ্রেশন বা অ্যারো ফাংশনের ক্ষেত্রে খাটে না (কারণ তারা ভ্যারিয়েবল হোইস্টিং রুলস মেনে চলে)।

---

### **Q30: What’s the difference between .call and .apply in JavaScript? / JavaScript-এ .call এবং .apply এর মধ্যে পার্থক্য কী?**

**Answer (English):**
Both methods are used to invoke a function with a custom, explicitly bound `this` context. The only difference is how they accept parameters:
*   **`.call(thisArg, arg1, arg2, ...)`:** Accepts arguments individually as a comma-separated list.
*   **`.apply(thisArg, [argsArray])`:** Accepts arguments as a single array or array-like object.

**অনুবাদ (Bangla Translation):**
উভয় মেথডই কোনো ফাংশনকে কাস্টম বা নির্দিষ্ট `this` কনটেক্সটের সাপেক্ষে রান করতে ব্যবহৃত হয়। এদের মধ্যে মূল পার্থক্য হলো প্যারামিটার আদান-প্রদানের স্টাইলে:
*   **`.call(thisArg, arg1, arg2...)`:** এটি প্যারামিটারগুলো কমা দিয়ে একটি একটি করে আলাদাভাবে নেয়।
*   **`.apply(thisArg, [argsArray])`:** এটি প্যারামিটারগুলো একটিমাত্র অ্যারে বা অ্যারেলিস্ট আকারে গ্রহণ করে।

---

### **Q31: Can you offer a use case for the new arrow => function syntax? / নতুন arrow => ফাংশন সিনট্যাক্সের একটি বাস্তব ব্যবহার ক্ষেত্র দেখান।**

**Answer (English):**
The primary use case for arrow functions is when you need to maintain the lexical context of the `this` keyword inside callbacks. Unlike regular functions, arrow functions do not define their own `this`. They inherit it from their enclosing lexical parent scope, making them ideal for event listeners, `setTimeout` callbacks, and array mapping methods.
*   **Example:**
    ```javascript
    const numbers = [1, 2, 3];
    const doubled = numbers.map(n => n * 2);
    ```

**অনুবাদ (Bangla Translation):**
অ্যারো ফাংশনের প্রধান ব্যবহার ক্ষেত্র হলো যখন কোনো কলব্যাক ফাংশনের ভেতরে লেক্সিকাল `this` এর মান অবিকৃত রাখা প্রয়োজন হয়। অ্যারো ফাংশনের নিজস্ব কোনো `this` নেই, এটি তার চারপাশের প্যারেন্ট স্কোপ থেকে `this` এর মান গ্রহণ করে, যা ইভেন্ট হ্যান্ডলার বা `setTimeout` এর ভেতর কোডকে সচল রাখতে সাহায্য করে।
*   **উদাহরণ:**
    ```javascript
    const numbers = [1, 2, 3];
    const doubled = numbers.map(n => n * 2);
    ```

---

### **Q32: Difference between: function Person(){}, const person = Person(), and const person = new Person() in JavaScript? / function Person(){}, const person = Person(), এবং const person = new Person() এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`function Person() {}`:** A standard function declaration. It can be used either as a normal helper function or as a constructor function.
*   **`const person = Person()`:** Invokes the function as a regular function call. It does not create a new object instance. In non-strict mode, `this` refers to `window` (global), and the return value is `undefined` (unless explicitly returned).
*   **`const person = new Person()`:** Invokes the function as a constructor. The `new` keyword automatically creates a new empty object instance, binds `this` to it, sets the prototype to `Person.prototype`, and returns the newly created object.

**অনুবাদ (Bangla Translation):**
*   **`function Person() {}`:** এটি একটি সাধারণ ফাংশন ডিক্লেয়ারেশন। এটি সাধারণ ফাংশন অথবা কন্সট্রাক্টর ফাংশন—উভয় হিসেবেই কাজ করতে পারে।
*   **`const person = Person()`:** এটি একটি সাধারণ ফাংশন কল। এটি কোনো নতুন অবজেক্ট তৈরি করে না। নন-স্ট্রিক্ট মোডে এর ভেতরের `this` নির্দেশ করে `window` অবজেক্টকে এবং এর রিটার্ন ভ্যালু হয় `undefined`।
*   **`const person = new Person()`:** এটি একটি কন্সট্রাক্টর কল। `new` কিওয়ার্ড দেওয়ার কারণে এটি মেমোরিতে একটি নতুন অবজেক্ট ইন্সট্যান্স তৈরি করে, তার সাথে `this` বাইন্ড করে এবং প্রোটোটাইপ চেইন সেটআপ করে সেই নতুন অবজেক্টটি রিটার্ন করে।

---

### **Q33: What is the definition of a higher-order function in JavaScript? / JavaScript-এ higher-order function এর সংজ্ঞা কী?**

**Answer (English):**
A Higher-Order Function (HOF) is a function that takes one or more functions as arguments, and/or returns a function as its result.
*   **Examples:**
    *   `Array.prototype.map()`: Takes a mapping callback function as an argument.
    *   `Array.prototype.filter()`, `Array.prototype.reduce()`.
    *   `Function.prototype.bind()`: Returns a new function with bound context.

**অনুবাদ (Bangla Translation):**
হায়ার-অর্ডার ফাংশন (Higher-Order Function) হলো এমন ফাংশন যা অন্য এক বা একাধিক ফাংশনকে আর্গুমেন্ট হিসেবে গ্রহণ করে, অথবা রিটার্ন ভ্যালু হিসেবে একটি নতুন ফাংশন আউটপুট দেয়।
*   **উদাহরণ:**
    *   `Array.prototype.map()`: এটি ম্যাপিং করার জন্য প্যারামিটারে একটি কলব্যাক ফাংশন গ্রহণ করে।
    *   `filter()`, `reduce()` এবং `Function.prototype.bind()` (যা একটি নতুন ফাংশন রিটার্ন করে)।

---

### **Q34: What are callback functions and how are they used? / Callback functions কী এবং কীভাবে এগুলো ব্যবহার করা হয়?**

**Answer (English):**
A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete a routine or respond to an event. They are widely used to manage asynchronous operations, such as network requests, reading files, timer delays (`setTimeout`), or DOM event handling.

**অনুবাদ (Bangla Translation):**
কলব্যাক ফাংশন হলো এমন একটি ফাংশন যা অন্য কোনো ফাংশনের ভেতরে প্যারামিটার বা আর্গুমেন্ট হিসেবে পাঠানো হয়, এবং পরবর্তীতে মূল ফাংশনের ভেতর থেকে উপযুক্ত সময়ে তাকে কল বা ফায়ার করা হয়। এটি অ্যাসিনক্রোনাস কাজ যেমন এপিআই ডেটা লোড, ফাইল রিড বা ডম ইভেন্ট হ্যান্ডল করতে ব্যবহৃত হয়।

---

### **Q35: What’s a typical use case for anonymous functions in JavaScript? / JavaScript-এ anonymous (বেনামী) ফাংশনের একটি সাধারণ ব্যবহার ক্ষেত্র কী?**

**Answer (English):**
Anonymous functions are functions declared without a name. Common use cases include:
1.  **Immediate Invocation (IIFE):** `(function() { ... })();` to create a local scope and prevent global variable pollution.
2.  **Short-lived Callback Arguments:** Passing them directly into higher-order functions like `map`, `filter`, or `setTimeout` (e.g., `setTimeout(function() { ... }, 1000)`).
3.  **Function Expressions:** Assigning a function to a variable (`const foo = function() {}`).

**অনুবাদ (Bangla Translation):**
অ্যানোনিমাস বা বেনামী ফাংশন হলো এমন ফাংশন যার কোনো নাম থাকে না। এর সাধারণ ব্যবহার ক্ষেত্রসমূহ:
1.  **IIFE ( Immediately Invoked Function Expression):** লোকাল স্কোপ তৈরি ও গ্লোবাল স্কোপ দূষণ এড়াতে সরাসরি রান করা `(function(){ ... })();`।
2.  **অস্থায়ী কলব্যাক আর্গুমেন্ট:** কোনো হায়ার-অর্ডার ফাংশন যেমন `map` বা `setTimeout` এর ভেতর সরাসরি প্যারামিটার হিসেবে পাস করা (যেমন: `setTimeout(function() { ... }, 1000)`)।
3.  **ফাংশন এক্সপ্রেশন:** ভ্যারিয়েবলের ভেতরে ফাংশন অ্যাসাইন করে রাখা।
