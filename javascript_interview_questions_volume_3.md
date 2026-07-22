# JavaScript Interview Questions Guide: Volume 3 (Questions 71 - 110)

This guide contains detailed answers in English alongside complete Bangla translations for questions 71 to 110 from the uploaded JavaScript Interview Questions PDF.

---

### **Q71: What is the purpose of the `new` keyword? / `new` কিওয়ার্ডের উদ্দেশ্য কী?**

**Answer (English):**
The `new` keyword is used to create an instance of a user-defined object type or a built-in object that has a constructor function.
*   **What `new` does under the hood (4 steps):**
    1.  Creates a brand new empty object `{}`.
    2.  Sets the new object's internal `[[Prototype]]` (`__proto__`) to point to the constructor's `prototype` property.
    3.  Binds `this` inside the constructor function to the newly created object.
    4.  Executes the constructor code and automatically returns the new object (unless the constructor explicitly returns its own non-primitive object).

**অনুবাদ (Bangla Translation):**
`new` কিওয়ার্ডটি কোনো কন্সট্রাক্টর ফাংশন বা অবজেক্ট টাইপ থেকে নতুন একটি কাস্টম অবজেক্ট ইন্সট্যান্স তৈরি করতে ব্যবহৃত হয়।
*   **`new` ব্যাকগ্রাউন্ডে যে ৪টি কাজ করে:**
    1.  মেমোরিতে একটি নতুন ফাঁকা অবজেক্ট `{}` তৈরি করে।
    2.  নতুন অবজেক্টের ইন্টারনাল `[[Prototype]]`-কে কন্সট্রাক্টর ফাংশনের `prototype`-এর সাথে যুক্ত করে।
    3.  কন্সট্রাক্টর ফাংশনের ভেতরের `this`-কে এই নতুন অবজেক্টের সাথে বাইন্ড করে।
    4.  কন্সট্রাক্টরের কোড রান করায় এবং নতুন অবজেক্টটি অটোমেটিকালি রিটার্ন করে।

---

### **Q72: How do you create a constructor function? / কীভাবে একটি কন্সট্রাক্টর ফাংশন তৈরি করবেন?**

**Answer (English):**
A constructor function is defined like a regular function, but by naming convention, its name starts with a Capital letter. Inside, properties and methods are attached to `this`.
*   **Example:**
    ```javascript
    function Person(name, age) {
      this.name = name;
      this.age = age;
      this.sayHello = function() {
        return `Hi, I am ${this.name}`;
      };
    }
    const user1 = new Person('Rohit', 25);
    ```

**অনুবাদ (Bangla Translation):**
কন্সট্রাক্টর ফাংশন সাধারণ ফাংশনের মতোই লেখা হয়, তবে কনভেনশন অনুযায়ী এর নামের প্রথম অক্ষর বড় হাতের (Capital Letter) দেওয়া হয়। এর ভেতরে প্রপার্টি ও মেথডগুলোকে `this`-এর সাথে যুক্ত করা হয়।
*   **উদাহরণ:**
    ```javascript
    function Person(name, age) {
      this.name = name;
      this.age = age;
      this.sayHello = function() {
        return `Hi, I am ${this.name}`;
      };
    }
    const user1 = new Person('Rohit', 25);
    ```

---

### **Q73: What are the differences between JavaScript ES2015 classes and ES5 function constructors? / ES2015 ক্লাস এবং ES5 কন্সট্রাক্টর ফাংশনের মধ্যে পার্থক্য কী কী?**

**Answer (English):**
1.  **Syntax:** ES2015 uses `class` and `constructor()` syntax, which is cleaner than ES5 function prototypes.
2.  **Hoisting:** ES5 function declarations are hoisted, whereas ES2015 classes are **not hoisted** (stay in Temporal Dead Zone).
3.  **Strict Mode:** ES2015 class bodies automatically run in strict mode (`"use strict"`).
4.  **Inheritance:** ES2015 uses declarative `extends` and `super()`, replacing verbose ES5 `Object.create(Parent.prototype)` and manual constructor binding.
5.  **Execution without `new`:** Calling an ES5 constructor without `new` mutates `window` (global), while calling an ES2015 class without `new` throws a `TypeError`.

**অনুবাদ (Bangla Translation):**
1.  **সিনট্যাক্স:** ES2015-এ `class` এবং `constructor()` সিনট্যাক্স ব্যবহার করা হয় যা ES5 প্রোটোটাইপের চেয়ে পঠনযোগ্য।
2.  **হোইস্টিং:** ES5 কন্সট্রাক্টর ফাংশন হোইস্ট হয়, কিন্তু ES2015 ক্লাস **হোইস্ট হয় না** (TDZ-এ থাকে)।
3.  **Strict Mode:** ES2015 ক্লাসের বডি স্বয়ংক্রিয়ভাবে strict mode-এ রান করে।
4.  **ইনহেরিটেন্স:** ES2015-এ সহজ `extends` ও `super()` দিয়ে ইনহেরিট করা যায়, যা ES5-এর জটিল `Object.create()` এর ব্যবহার দূর করে।
5.  **`new` ছাড়া কল:** ES5 কন্সট্রাক্টরকে `new` ছাড়া কল করলে গ্লোবাল অবজেক্ট নষ্ট হতে পারে, কিন্তু ES2015 ক্লাসকে `new` ছাড়া কল করলে সরাসরি `TypeError` এরর দেয়।

---

### **Q74: What advantage is there for using the JavaScript arrow syntax for a method in a constructor? / কন্সট্রাক্টরের ভেতরের মেথডে অ্যারো (arrow) সিনট্যাক্স ব্যবহারের সুবিধা কী?**

**Answer (English):**
The primary advantage is that arrow functions automatically bind `this` lexically to the newly created instance at creation time.
*   **Benefit:** If the method is passed around as a callback (e.g., in event listeners or `setTimeout`), a regular function method will lose its `this` context (becoming `undefined` or `window`). An arrow function method permanently retains its original `this` instance reference.

**অনুবাদ (Bangla Translation):**
প্রধান সুবিধা হলো অ্যারো ফাংশন তৈরির মুহূর্তেই তার লেক্সিকাল `this`-কে কন্সট্রাক্টরের নতুন অবজেক্টের সাথে চিরতরে বাইন্ড করে ফেলে।
*   **লাভ:** এই মেথডটিকে কোনো কলব্যাক হিসেবে (যেমন- ইভেন্ট লিসেনার বা `setTimeout`-এ) পাস করলেও এর `this` কখনো পরিবর্তন বা নষ্ট হয়ে `undefined` হয় না; এটি স্থায়ীভাবে মূল অবজেক্টকেই নির্দেশ করে।

---

### **Q75: Why might you want to create static class members in JavaScript? / JavaScript-এ কেন স্ট্যাটিক ক্লাস মেম্বার (static class members) তৈরি করতে চাইবেন?**

**Answer (English):**
Static properties and methods are defined with the `static` keyword inside a class. They belong to the class itself, rather than to instances created from the class.
*   **Use Cases:**
    1.  **Utility/Helper Functions:** Methods that don't need instance data (e.g., `Math.max()`, `Array.from()`).
    2.  **Namespace Configuration:** Storing app-wide constants related to a domain (e.g., `Config.API_URL`).
    3.  **Factory Methods:** Creating custom instances dynamically (e.g., `User.createGuestUser()`).

**অনুবাদ (Bangla Translation):**
স্ট্যাটিক প্রপার্টি ও মেথড তৈরি করতে `static` কিওয়ার্ড ব্যবহার করা হয়। এগুলো কোনো নির্দিষ্ট অবজেক্ট ইন্সট্যান্সের অন্তর্গত নয়, বরং সরাসরি ক্লাসের নিজস্ব মেম্বার হিসেবে কাজ করে।
*   **ব্যবহারের কারণ:**
    1.  **ইউটিলিটি বা হেল্পার ফাংশন:** যেসব কাজের জন্য ইন্সট্যান্স ডেটার প্রয়োজন নেই (যেমন- `Math.max()`)।
    2.  **কনফিগারেশন ও কনস্ট্যান্ট:** পুরো অ্যাপ্লিকেশনের জন্য ক্লাসের নিজস্ব কনস্ট্যান্ট রাখা।
    3.  **ফ্যাক্টরি মেথড:** ক্লাস থেকেই কাস্টম ইন্সট্যান্স রিটার্ন করা (যেমন- `User.createGuestUser()`)।

---

### **Q76: What is a closure in JavaScript, and how/why would you use one? / JavaScript-এ ক্লোজার (Closure) কী এবং কেন/কীভাবে এটি ব্যবহার করবেন?**

**Answer (English):**
A closure is the combination of a function bundled together with references to its surrounding lexical state. In JavaScript, a inner function always has access to the variables of its outer function, even **after** the outer function has finished executing and returned.
*   **Why use closures:**
    1.  **Data Privacy / Encapsulation:** Creating private variables that cannot be modified directly from the outside.
    2.  **State Preservation:** Retaining state across asynchronous function calls or event handlers.
    3.  **Currying & Partial Application:** Pre-filling arguments in functional programming.

**অনুবাদ (Bangla Translation):**
ক্লোজার (Closure) হলো এমন একটি মেকানিজম যেখানে একটি ইনার বা ভিতরের ফাংশন তার আউটার বা বাইরের ফাংশনের স্কোপের ভ্যারিয়েবলগুলোকে মনে রাখে এবং অ্যাক্সেস করতে পারে, এমনকি বাইরের ফাংশনটির এক্সিকিউশন শেষ হয়ে রিটার্ন হয়ে যাওয়ার **পরও**।
*   **কেন ব্যবহার করবেন:**
    1.  **ডাটা প্রাইভেসি বা এনক্যাপসুলেশন:** বাইরে থেকে সরাসরি অ্যাক্সেস বা পরিবর্তন করা যায় না এমন প্রাইভেট ভ্যারিয়েবল তৈরি করতে।
    2.  **স্টেট বজায় রাখা:** অ্যাসিনক্রোনাস কাজ বা ইভেন্ট হ্যান্ডলারের মাঝে স্টেট মনে রাখা।
    3.  **কারিইং (Currying):** ফাংশনাল প্রোগ্রামিংয়ে আর্গুমেন্ট আংশিক পাস করার জন্য।

---

### **Q77: Explain the concept of lexical scoping. / Lexical scoping ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
Lexical scoping (also known as static scoping) means that the accessibility of variables is determined strictly by the physical location of code inside the source files at compile time.
*   **Behavior:** Inner nested functions can access variables declared in their outer enclosing parent scopes, but outer parent scopes cannot access variables declared inside inner child scopes.

**অনুবাদ (Bangla Translation):**
লেক্সিকাল স্কোপিং (Lexical Scoping) বলতে বোঝায় যে ভ্যারিয়েবলের অ্যাক্সেস বা সীমানা কোড ফাইলের ফিজিক্যাল অবস্থানের ওপর ভিত্তি করে ডিক্লেয়ারেশনের সময় নির্ধারিত হয়।
*   **নিয়ম:** ভেতরের নেস্টেড ফাংশন তার বাইরের প্যারেন্ট ফাংশনের সব ভ্যারিয়েবল দেখতে পায়, কিন্তু বাইরের ফাংশন ভেতরের চাইল্ড ফাংশনের ভ্যারিয়েবল অ্যাক্সেস করতে পারে না।

---

### **Q78: Explain the concept of scope in JavaScript. / JavaScript-এ স্কোপ (Scope) ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
Scope determines the accessibility and visibility of variables, functions, and objects in specific parts of your code.
*   **Main Types of Scope:**
    1.  **Global Scope:** Accessible from anywhere in the application.
    2.  **Function Scope:** Variables declared with `var`, `let`, or `const` inside a function are accessible only within that function.
    3.  **Block Scope:** Variables declared with `let` or `const` inside curly braces `{}` (like `if`, `for`, `while`) are accessible only inside that block.

**অনুবাদ (Bangla Translation):**
স্কোপ (Scope) হলো কোডের একটি সীমানা যা নির্ধারণ করে যে কোডের কোন অংশ থেকে কোন ভ্যারিয়েবল বা ফাংশন অ্যাক্সেস করা যাবে।
*   **প্রধান ৩টি স্কোপ:**
    1.  **গ্লোবাল স্কোপ (Global Scope):** অ্যাপ্লিকেশনের যেকোনো জায়গা থেকে অ্যাক্সেসযোগ্য।
    2.  **ফাংশন স্কোপ (Function Scope):** কোনো ফাংশনের ভেতরে ডিক্লেয়ার করা ভ্যারিয়েবল কেবল সেই ফাংশনের ভেতরেই কাজ করে।
    3.  **ব্লক স্কোপ (Block Scope):** কার্লি ব্র্যাকেটের `{}` ভেতরে `let` বা `const` দিয়ে ডিক্লেয়ার করা ভ্যারিয়েবল কেবল ওই ব্লকের ভেতরেই কাজ করে।

---

### **Q79: How can closures be used to create private variables? / কীভাবে ক্লোজার ব্যবহার করে প্রাইভেট ভ্যারিয়েবল তৈরি করা যায়?**

**Answer (English):**
By wrapping a variable inside an outer function and exposing only specific inner methods (getters/setters) to the outside world.
*   **Example:**
    ```javascript
    function createCounter() {
      let count = 0; // Private variable
      return {
        increment() { count++; return count; },
        getCount() { return count; }
      };
    }
    const counter = createCounter();
    counter.increment(); // 1
    console.log(counter.count); // undefined (cannot access directly)
    ```

**অনুবাদ (Bangla Translation):**
একটি আউটার ফাংশনের ভেতরে ভ্যারিয়েবল লুকিয়ে রেখে কেবল কিছু নির্দিষ্ট ইনার মেথড (যেমন getter/setter) বাইরে রিটার্ন করার মাধ্যমে প্রাইভেট ভ্যারিয়েবল তৈরি করা হয়।
*   **উদাহরণ:**
    ```javascript
    function createCounter() {
      let count = 0; // প্রাইভেট ভ্যারিয়েবল
      return {
        increment() { count++; return count; },
        getCount() { return count; }
      };
    }
    const counter = createCounter();
    counter.increment(); // ১
    console.log(counter.count); // undefined (সরাসরি অ্যাক্সেস সম্ভব নয়)
    ```

---

### **Q80: What are the potential pitfalls of using closures? / ক্লোজার ব্যবহারের সম্ভাব্য ক্ষতিকর দিক বা সমস্যাগুলো কী কী?**

**Answer (English):**
1.  **Memory Leaks:** If closed-over variables are no longer needed but inner functions are kept referenced in memory, garbage collection is prevented, consuming memory.
2.  **Over-consumption of CPU/Memory:** Creating functions inside functions repeatedly recreates closures.
3.  **Debugging Complexity:** Deep scope chains can make inspecting variable values during debugging more difficult.

**অনুবাদ (Bangla Translation):**
1.  **মেমোরি লিক (Memory Leaks):** ক্লোজারের ভেতরের অপ্রয়োজনীয় ভ্যারিয়েবলের রেফারেন্স মেমোরিতে থেকে গেলে গার্বেজ কালেকশন হতে পারে না, ফলে ব্রাউজারের মেমোরি নষ্ট হয়।
2.  **পারফরম্যান্স ইস্যু:** অহেতুক বেশি ক্লোজার ব্যবহার করলে মেমোরি ও সিপিইউ প্রসেসিং এর ওপর চাপ পড়ে।
3.  **ডিবাগিংয়ের জটিলতা:** স্কোপ চেইন অনেক গভীর হলে ডিবাগ করার সময় ভ্যারিয়েবলের মান ট্র্যাক করা কঠিন হয়ে পড়ে।

---

### **Q81: Explain the difference between global scope, function scope, and block scope. / গ্লোবাল স্কোপ, ফাংশন স্কোপ এবং ব্লক স্কোপের মধ্যে পার্থক্য ব্যাখ্যা করুন।**

**Answer (English):**
*   **Global Scope:** Defined outside any function/block. Accessible everywhere in the application.
*   **Function Scope:** Created by function boundaries. `var`, `let`, and `const` inside a function cannot be accessed outside it.
*   **Block Scope:** Created by `{}` braces (e.g., `if`, `for`). Only `let` and `const` respect block scope (`var` leaks out of blocks to the surrounding function/global scope).

**অনুবাদ (Bangla Translation):**
*   **গ্লোবাল স্কোপ:** যেকোনো ফাংশন বা ব্লকের বাইরে অবস্থিত। সম্পূর্ণ প্রজেক্ট থেকে পাওয়া যায়।
*   **ফাংশন স্কোপ:** ফাংশনের সীমানা দ্বারা তৈরি। ফাংশনের ভেতরের `var`, `let`, `const` বাইরে পাওয়া যায় না।
*   **ব্লক স্কোপ:** কার্লি ব্র্যাকেট `{}` (যেমন `if` বা `for`) দ্বারা তৈরি। কেবল `let` ও `const` ব্লক স্কোপ মেনে চলে (`var` ব্লক ভেঙে বাইরে চুইয়ে পড়ে)।

---

### **Q82: Explain how `this` works in JavaScript. / JavaScript-এ `this` কীভাবে কাজ করে ব্যাখ্যা করুন।**

**Answer (English):**
The `this` keyword is a dynamic reference to the execution context of the function. Its value depends on **how** a function is invoked:
1.  **Method Call (`obj.method()`):** `this` points to `obj`.
2.  **Regular Function Call (`foo()`):** `this` points to `window` (or `undefined` in strict mode).
3.  **Constructor Call (`new Foo()`):** `this` points to the newly created instance.
4.  **Explicit Binding (`call/apply/bind`):** `this` points to the explicitly passed object.
5.  **Arrow Functions:** `this` is lexically inherited from the surrounding scope at definition time.

**অনুবাদ (Bangla Translation):**
`this` হলো ফাংশনের এক্সিকিউশন কনটেক্সটের একটি ডাইনামিক রেফারেন্স। এটি কীভাবে ফাংশনটিকে **কল করা হচ্ছে** তার ওপর নির্ভর করে:
1.  **মেথড কল (`obj.method()`):** `this` নির্দেশ করে `obj`-কে।
2.  **সাধারণ ফাংশন কল (`foo()`):** `this` নির্দেশ করে `window`-কে (strict mode-এ `undefined`)।
3.  **কন্সট্রাক্টর কল (`new Foo()`):** `this` নির্দেশ করে নতুন অবজেক্টকে।
4.  **Explicit Binding (`call/apply/bind`):** `this` নির্দেশ করে পাস করা অবজেক্টকে।
5.  **অ্যারো ফাংশন:** `this` তৈরি হওয়ার সময়ের চারপাশের লেক্সিকাল স্কোপের `this` গ্রহণ করে।

---

### **Q83: Explain `Function.prototype.bind` in JavaScript. / JavaScript-এ `Function.prototype.bind` ব্যাখ্যা করুন।**

**Answer (English):**
`Function.prototype.bind()` creates and returns a **new function** with its `this` keyword permanently bound to the provided object, regardless of how it is later called.
*   **Features:**
    1.  Permanently sets `this`.
    2.  Supports **Partial Application**: You can pre-set initial arguments before the bound function is invoked later.

**অনুবাদ (Bangla Translation):**
`Function.prototype.bind()` একটি **নতুন ফাংশন** তৈরি করে ফেরত দেয়, যার ভেতরের `this` নির্দেশকটি চিরতরে পাস করা অবজেক্টের সাথে যুক্ত (bound) হয়ে যায়।
*   **ফিচারসমূহ:**
    1.  স্থায়ীভাবে `this` সেট করে।
    2.  **পার্শিয়াল অ্যাপ্লিকেশন (Partial Application):** ফাংশন রান করার আগেই কিছু ডিফল্ট আর্গুমেন্ট ফিক্সড করে রাখার সুবিধা দেয়।

---

### **Q84: Explain the different ways the `this` keyword can be bound. / `this` কিওয়ার্ড বাইন্ড হওয়ার বিভিন্ন পদ্ধতিগুলো কী কী?**

**Answer (English):**
1.  **Default Binding:** In standalone function invocation, `this` binds to global `window` (or `undefined` in strict mode).
2.  **Implicit Binding:** When called via object property (`obj.fn()`), `this` binds to `obj`.
3.  **Explicit Binding:** Using `.call()`, `.apply()`, or `.bind()` to manually specify `this`.
4.  **New Binding:** Using `new` keyword binds `this` to the newly instantiated object.
5.  **Lexical Binding:** Arrow functions inherit `this` from surrounding scope.

**অনুবাদ (Bangla Translation):**
1.  **Default Binding:** সাধারণ ফাংশন কলের ক্ষেত্রে `this` গ্লোবাল `window` অবজেক্টের সাথে যুক্ত হয় (strict mode-এ `undefined`)।
2.  **Implicit Binding:** অবজেক্টের মেথড হিসেবে কল করলে (`obj.fn()`) `this` সেই অবজেক্টের সাথে যুক্ত হয়।
3.  **Explicit Binding:** `.call()`, `.apply()`, বা `.bind()` ব্যবহার করে ম্যানুয়ালি `this` সেট করা।
4.  **New Binding:** `new` কিওয়ার্ড দিয়ে নতুন অবজেক্ট তৈরির সময় `this` সেই অবজেক্টের সাথে যুক্ত হয়।
5.  **Lexical Binding:** অ্যারো ফাংশন তার চারপাশের স্কোপ থেকে `this` গ্রহণ করে।

---

### **Q85: What are the common pitfalls of using the `this` keyword? / `this` কিওয়ার্ড ব্যবহারের সাধারণ ভুল বা বিপজ্জনক দিকগুলো কী কী?**

**Answer (English):**
1.  **Losing `this` in Callbacks:** Passing a method as a callback (e.g., `setTimeout(obj.method, 1000)`) causes `this` to break and default to `window`/`undefined`.
2.  **Nested Functions:** A regular function declared inside a method resets `this` to global instead of keeping the parent object context.
3.  **Arrow Functions in Objects:** Defining object methods using arrow functions causes `this` to point to global scope instead of the object.

**অনুবাদ (Bangla Translation):**
1.  **কলব্যাকে `this` হারিয়ে যাওয়া:** মেথডকে কলব্যাক হিসেবে পাঠালে (যেমন- `setTimeout(obj.method, 1000)`) `this`-এর লিংক কেটে গিয়ে `window` হয়ে যায়।
2.  **নেস্টেড ফাংশন:** মেথডের ভেতরে নতুন সাধারণ ফাংশন লিখলে তা প্যারেন্ট অবজেক্টকে ভুলে গিয়ে গ্লোবাল `this` পায়।
3.  **অবজেক্টের ভেতর অ্যারো ফাংশন:** অবজেক্টের সরাসরি মেথড হিসেবে অ্যারো ফাংশন লিখলে তার `this` অবজেক্টকে না বুঝিয়ে গ্লোবাল স্কোপকে বোঝায়।

---

### **Q86: Explain the concept of `this` binding in event handlers. / Event handlers-এ `this` বাইন্ডিংয়ের ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
When an HTML element triggers a DOM event, traditional event listener callbacks bind `this` to the **DOM element** that received the event (`event.currentTarget`).
*   **Exception with Arrow Functions:** If an arrow function is used as the event listener callback, `this` is not the DOM element, but rather the outer scope `this` (usually `window`).

**অনুবাদ (Bangla Translation):**
যখন কোনো HTML এলিমেন্ট ডম ইভেন্ট ফায়ার করে, তখন প্রথাগত ইভেন্ট লিসেনার কলব্যাকের ভেতরের `this` সরাসরি সেই **DOM এলিমেন্টকে** নির্দেশ করে (`event.currentTarget`)।
*   **অ্যারো ফাংশনের ক্ষেত্রে ব্যতিক্রম:** ইভেন্ট লিসেনারে অ্যারো ফাংশন ব্যবহার করলে `this` সেই ডম এলিমেন্টকে না বুঝিয়ে বাইরের স্কোপের `this` (যেমন `window`)-কে নির্দেশ করে।

---

### **Q87: What is the DOM and how is it structured? / DOM কী এবং এটি কীভাবে গঠিত?**

**Answer (English):**
The **Document Object Model (DOM)** is a programming interface for HTML documents. It represents the web page as an inverted **Tree Structure** of objects, where each node represents a part of the document (elements, attributes, text nodes).
*   Allows JavaScript to dynamically read, modify, add, or delete HTML elements and CSS styles.

**অনুবাদ (Bangla Translation):**
**ডকুমেন্ট অবজেক্ট মডেল (DOM)** হলো ওয়েব পেজের একটি প্রোগ্রামিং ইন্টারফেস। এটি পুরো HTML পেজকে গাছের মতো উল্টানো **ট্রি স্ট্রাকচার (Tree Structure)** আকারে রিপ্রেজেন্ট করে, যেখানে প্রতিটি নোড (Node) হলো এলিমেন্ট, অ্যাট্রিবিউট বা টেক্সট।
*   এর মাধ্যমে জাভাস্ক্রিপ্ট দিয়ে ডাইনামিকালি পেজের উপাদান ও সিএসএস স্টাইল পরিবর্তন বা ডিলিট করা যায়।

---

### **Q88: What’s the difference between an “attribute” and a “property” in the DOM? / DOM-এ “attribute” এবং “property” এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Attribute:** Defined in the HTML source code markup (`<input value="hello">`). Its type is always a string and it reflects the *initial/default* state.
*   **Property:** A live variable inside the DOM object created by the browser (`inputElement.value`). Its type can be any JavaScript data type and it represents the *current dynamic* state as the user interacts with the page.

**অনুবাদ (Bangla Translation):**
*   **Attribute (অ্যাট্রিবিউট):** এটি সরাসরি HTML মার্কআপে লেখা থাকে (যেমন- `<input value="hello">`)। এটি কেবল স্ট্রিং টাইপ হয় এবং এটি প্রাথমিক বা ডিফল্ট মান নির্দেশ করে।
*   **Property (প্রপার্টি):** এটি ব্রাউজারের ডম অবজেক্টের ভেতরের লাইভ ভ্যারিয়েবল (`inputElement.value`)। এটি যেকোনো ডাটা টাইপের হতে পারে এবং ইউজার টাইপ করার সাথে সাথে এটি বর্তমান রিয়েল-টাইম মান নির্দেশ করে।

---

### **Q89: Explain the difference between `document.querySelector()` and `document.getElementById()`. / `document.querySelector()` এবং `document.getElementById()` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`getElementById('myId')`:** Accepts only an ID string (without `#`). Highly optimized and faster for retrieving a single element by its ID.
*   **`querySelector('.myClass #myId')`:** Accepts any valid CSS selector string (classes, IDs, attributes, pseudo-selectors). Returns the **first** matching element. More flexible but slightly slower.

**অনুবাদ (Bangla Translation):**
*   **`getElementById('myId')`:** এটি কেবল আইডি নেম নেয় (হ্যাশ `#` ছাড়া)। আইডি দিয়ে একটিমাত্র এলিমেন্ট দ্রুত খুঁজে বের করার জন্য এটি সবচেয়ে ফাস্ট।
*   **`querySelector('.myClass #myId')`:** এটি যেকোনো বৈধ সিএসএস সিলেক্টর সাপোর্ট করে। প্রথম ম্যাচিং এলিমেন্টটি ফেরত দেয়। এটি অত্যন্ত ফ্লেক্সিবল।

---

### **Q90: How do you add, remove, and modify HTML elements using JavaScript? / কীভাবে জাভাস্ক্রিপ্ট ব্যবহার করে HTML এলিমেন্ট যোগ, রিমুভ এবং মডিফাই করবেন?**

**Answer (English):**
*   **Add:** `const el = document.createElement('div'); parent.appendChild(el);`
*   **Remove:** `element.remove();` or `parent.removeChild(child);`
*   **Modify Content:** `el.textContent = 'Hello';` or `el.innerHTML = '<b>Hello</b>';`
*   **Modify Attributes:** `el.setAttribute('id', 'newId');` or `el.classList.add('active');`

**অনুবাদ (Bangla Translation):**
*   **যোগ করা (Add):** `const el = document.createElement('div'); parent.appendChild(el);`
*   **রিমুভ করা (Remove):** `element.remove();` অথবা `parent.removeChild(child);`
*   **কন্টেন্ট মডিফাই:** `el.textContent = 'Hello';` অথবা `el.innerHTML = '<b>Hello</b>';`
*   **অ্যাট্রিবিউট মডিফাই:** `el.setAttribute('id', 'newId');` অথবা `el.classList.add('active');`

---

### **Q91: What are event listeners and how are they used? / Event listeners কী এবং কীভাবে এগুলো ব্যবহার করা হয়?**

**Answer (English):**
Event listeners are functions attached to DOM nodes that wait for specific user interactions (e.g., click, keydown, submit, scroll) and execute a callback function in response.
*   **Syntax:** `element.addEventListener('click', callbackFunction);`
*   **Removal:** `element.removeEventListener('click', callbackFunction);`

**অনুবাদ (Bangla Translation):**
ইভেন্ট লিসেনার হলো ডম এলিমেন্টের সাথে যুক্ত থাকা বিশেষ ফাংশন যা ব্যবহারকারীর নির্দিষ্ট কাজের (যেমন- মাউস ক্লিক, কিবোর্ড প্রেস, পেজ স্ক্রল) জন্য অপেক্ষা করে এবং ঘটনা ঘটা মাত্র নির্দিষ্ট কলব্যাক ফাংশন রান করায়।
*   **সিনট্যাক্স:** `element.addEventListener('click', callbackFunction);`
*   **রিমুভ করা:** `element.removeEventListener('click', callbackFunction);`

---

### **Q92: Explain the event phases in a browser. / ব্রাউজারে ইভেন্ট ফেজ (Event Phases) বা ধাপসমূহ ব্যাখ্যা করুন।**

**Answer (English):**
When an event occurs in the DOM, it travels through 3 distinct phases:
1.  **Capturing Phase (Trickling):** The event travels down from the top `Window` root through parent nodes down to the target element.
2.  **Target Phase:** The event reaches the actual target element where the interaction occurred.
3.  **Bubbling Phase:** The event bubbles back up from the target element through ancestors back to the `Window` root.

**অনুবাদ (Bangla Translation):**
ডমে কোনো ঘটনা ঘটলে ইভেন্টটি ৩টি প্রধান ধাপে ভ্রমণ করে:
1.  **Capturing Phase (ক্যাপচারিং ফেজ):** ইভেন্টটি একদম ওপরের `Window` ও রুট থেকে নিচে নামতে নামতে টার্গেট এলিমেন্টের দিকে যায়।
2.  **Target Phase (টার্গেট ফেজ):** ইভেন্টটি মূল টার্গেট এলিমেন্টে পৌঁছায়।
3.  **Bubbling Phase (বাবলিং ফেজ):** ইভেন্টটি টার্গেট এলিমেন্ট থেকে উল্টো দিকে ওপরের প্যারেন্ট এলিমেন্টগুলোর মধ্য দিয়ে আবার রুটে ফিরে যায়।

---

### **Q93: Describe event bubbling in JavaScript and browsers. / JavaScript এবং ব্রাউজারে ইভেন্ট বাবলিং (Event Bubbling) বর্ণনা করুন।**

**Answer (English):**
Event Bubbling is the default DOM propagation direction where an event triggered on a child element travels up the DOM hierarchy, firing event listeners on all ancestor parent elements one by one until it reaches `window`. It enables Event Delegation.

**অনুবাদ (Bangla Translation):**
ইভেন্ট বাবলিং (Event Bubbling) হলো ডমের ডিফল্ট আচরণের ধরণ, যেখানে কোনো চাইল্ড এলিমেন্টে ক্লিক বা ইভেন্ট ঘটলে সেই ইভেন্টটি বুদবুদের মতো ওপরের সমস্ত প্যারেন্ট এলিমেন্টগুলোর মধ্য দিয়ে ধাপে ধাপে ভেসে উঠে `window` পর্যন্ত চলে যায়।

---

### **Q94: Describe event capturing in JavaScript and browsers. / JavaScript এবং ব্রাউজারে ইভেন্ট ক্যাপচারিং (Event Capturing) বর্ণনা করুন।**

**Answer (English):**
Event Capturing (also called Trickling) is the opposite of bubbling. The event is intercepted first by the outermost ancestor (`window`) and trickles down to the target element.
*   **Enabling Capturing:** Pass `{ capture: true }` or `true` as the 3rd argument in `addEventListener()`.

**অনুবাদ (Bangla Translation):**
ইভেন্ট ক্যাপচারিং (Event Capturing) হলো বাবলিংয়ের ঠিক উল্টো নিয়ম। এতে ইভেন্টটি ওপরের প্যারেন্ট বা `window` থেকে শুরু হয়ে নিচে নামতে নামতে মূল চাইল্ড এলিমেন্টে পৌঁছায়।
*   **চালু করার উপায়:** `addEventListener()` এর ৩য় প্যারামিটারে `{ capture: true }` সেট করতে হয়।

---

### **Q95: Explain event delegation in JavaScript. / JavaScript-এ ইভেন্ট ডেলিগেশন (Event Delegation) ব্যাখ্যা করুন।**

**Answer (English):**
Event Delegation is a pattern where a single event listener is attached to a **common parent element** instead of attaching multiple listeners to individual child elements.
*   **How it works:** Uses Event Bubbling. When a child is clicked, the event bubbles to the parent, where `event.target` identifies which specific child was clicked.
*   **Benefits:** Saves memory, improves performance, and automatically handles dynamically added child elements.

**অনুবাদ (Bangla Translation):**
ইভেন্ট ডেলিগেশন (Event Delegation) হলো এমন একটি টেকনিক যেখানে ১০০টি আলাদা চাইল্ড এলিমেন্টে আলাদা ইভেন্ট লিসেনার না বসিয়ে কেবল তাদের **প্যারেন্ট কন্টেইনারে** একটিমাত্র ইভেন্ট লিসেনার বসানো হয়।
*   **মেকানিজম:** ইভেন্ট বাবলিংয়ের সহায়তায় চাইল্ডে ক্লিক করলে প্যারেন্ট সেই ইভেন্ট রিসিভ করে এবং `event.target` দিয়ে বোঝা যায় কোন চাইল্ডে ক্লিক হয়েছিল।
*   **সুবিধা:** প্রচুর মেমোরি বাঁচায় এবং নতুন ডাইনামিক চাইল্ড যোগ হলেও কোড স্বয়ংক্রিয়ভাবে কাজ করে।

---

### **Q96: How do you prevent the default behavior of an event? / কোনো ইভেন্টের ডিফল্ট আচরণ কীভাবে বন্ধ করবেন?**

**Answer (English):**
Call `event.preventDefault()` inside the event handler callback.
*   **Example:** Prevents a form from refreshing the page on submit, or prevents an `<a>` tag from navigating to a link URL.

**অনুবাদ (Bangla Translation):**
ইভেন্ট কলব্যাক ফাংশনের ভেতরে `event.preventDefault()` পদ্ধতি ব্যবহার করে।
*   **উদাহরণ:** ফর্মে সাবমিট বাটনে চাপ দিলে পেজ রিফ্রেশ হওয়া অথবা `<a>` লিংকে চাপ দিলে পেজ রিডাইরেক্ট হওয়া বন্ধ করতে।

---

### **Q97: What is the difference between `event.preventDefault()` and `event.stopPropagation()`? / `event.preventDefault()` এবং `event.stopPropagation()` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`event.preventDefault()`:** Stops the browser's default native action for the event (e.g., submitting a form, checking a checkbox), but **does not stop** the event from bubbling up the DOM tree.
*   **`event.stopPropagation()`:** Stops the event from bubbling up (or capturing down) the DOM tree to parent elements, but **does not stop** the browser's default action.

**অনুবাদ (Bangla Translation):**
*   **`event.preventDefault()`:** ব্রাউজারের নিজস্ব ডিফল্ট কাজ বন্ধ করে (যেমন ফর্ম রিফ্রেশ হওয়া বা চেকবাক্স সিলেক্ট হওয়া), কিন্তু ডম ট্রির ওপরের দিকে ইভেন্ট বাবলিং হওয়া বন্ধ করে না।
*   **`event.stopPropagation()`:** ডম ট্রিতে ইভেন্টটি ওপরের প্যারেন্টে বাবলিং হওয়া বন্ধ করে, কিন্তু ব্রাউজারের নিজস্ব ডিফল্ট কাজ বন্ধ করে না।

---

### **Q98: What is the difference between `mouseenter` and `mouseover` event in JavaScript and browsers? / `mouseenter` এবং `mouseover` ইভেন্টের মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`mouseover`:** **Bubbles up.** Fires when mouse enters the element OR any of its child elements.
*   **`mouseenter`:** **Does NOT bubble.** Fires only when the mouse enters the bound element itself, ignoring movement across internal child elements.

**অনুবাদ (Bangla Translation):**
*   **`mouseover`:** **এটি বাবলিং করে।** মাউস কার্সার মূল এলিমেন্ট বা তার ভেতরের যেকোনো চাইল্ড এলিমেন্টে ঢুকলে এটি ফায়ার হয়।
*   **`mouseenter`:** **এটি বাবলিং করে না।** মাউস কার্সার কেবল মূল এলিমেন্টের বর্ডারে ঢুকলেই ফায়ার হয়, ভেতরের চাইল্ডে গেলে নতুন করে ফায়ার হয় না।

---

### **Q99: What is the difference between `innerHTML` and `textContent`? / `innerHTML` এবং `textContent` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`innerHTML`:** Parses and returns or updates the complete HTML markup (including tags). Can pose **XSS security risks** if injecting unsanitized user strings.
*   **`textContent`:** Returns or sets purely raw text content, stripping all HTML tags. Safer, faster, and respects `<style>` and `<script>` text visibility.

**অনুবাদ (Bangla Translation):**
*   **`innerHTML`:** এটি HTML ট্যাগ সহ সম্পূর্ণ কন্টেন্ট রিড ও রেন্ডার করতে পারে। অনিরাপদ ইনপুট দিলে এটি **XSS সিকিউরিটি ঝুঁকি** তৈরি করে।
*   **`textContent`:** এটি সমস্ত HTML ট্যাগ বাদ দিয়ে কেবল প্লেইন টেক্সট দেখায় বা সেট করে। এটি দ্রুত এবং নিরাপদ।

---

### **Q100: How do you manipulate CSS styles using JavaScript? / কীভাবে জাভাস্ক্রিপ্ট দিয়ে CSS স্টাইল পরিবর্তন করবেন?**

**Answer (English):**
1.  **Inline Style:** `element.style.backgroundColor = 'blue';`
2.  **Class List Manipulation (Best practice):**
    *   `element.classList.add('active');`
    *   `element.classList.remove('active');`
    *   `element.classList.toggle('active');`
3.  **CSS Text:** `element.style.cssText = 'color: red; margin: 10px;';`

**অনুবাদ (Bangla Translation):**
1.  **ইনলাইন স্টাইল পরিবর্তন:** `element.style.backgroundColor = 'blue';`
2.  **ক্লাস যোগ/বিয়োগ (সেরা উপায়):**
    *   `element.classList.add('active');`
    *   `element.classList.remove('active');`
    *   `element.classList.toggle('active');`
3.  **সরাসরি সিএসএস টেক্সট দিয়ে:** `element.style.cssText = 'color: red; margin: 10px;';`

---

### **Q101: Describe the difference between `<script>`, `<script async>` and `<script defer>`. / `<script>`, `<script async>` এবং `<script defer>` এর মধ্যে পার্থক্য বর্ণনা করুন।**

**Answer (English):**
*   **`<script>` (Default):** HTML parsing pauses while the script is downloaded and executed. Blocks page rendering.
*   **`<script async>`:** Downloads script asynchronously in parallel with HTML parsing. Executes **immediately** when downloaded, pausing HTML parsing briefly. Order of execution is not preserved.
*   **`<script defer>`:** Downloads script asynchronously in parallel with HTML parsing. Executes **only after** HTML parsing is complete, preserving exact script declaration order.

**অনুবাদ (Bangla Translation):**
*   **`<script>` (ডিফল্ট):** স্ক্রিপ্ট ফাইল ডাউনলোড ও রান হওয়ার সময় HTML পার্সিং বন্ধ থাকে। পেজ লোড ব্লক হয়।
*   **`<script async>`:** HTML পার্সিং চলাকালীন ব্যাকগ্রাউন্ডে ডাউনলোড হয় এবং ডাউনলোড শেষ হওয়া মাত্রই সাথে সাথে রান হয়ে যায় (পার্সিং বন্ধ করে)। ফাইলের ক্রম বজায় থাকে না।
*   **`<script defer>`:** HTML পার্সিং চলাকালীন ব্যাকগ্রাউন্ডে ডাউনলোড হয়, কিন্তু সম্পূর্ণ HTML রিড শেষ হওয়ার পর সিরিয়াল বজায় রেখে রান করে।

---

### **Q102: What is the difference between the Window object and the Document object? / Window অবজেক্ট এবং Document অবজেক্টের মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`Window` Object:** The top-level global browser object representing the browser tab window. It holds global variables, BOM features (history, location, navigator, setTimeout).
*   **`Document` Object:** A property of the `Window` object (`window.document`) that represents the loaded HTML document/DOM loaded inside the window frame.

**অনুবাদ (Bangla Translation):**
*   **`Window` অবজেক্ট:** এটি ব্রাউজারের মূল গ্লোবাল অবজেক্ট যা ব্রাউজার উইন্ডো বা ট্যাবকে রিপ্রেজেন্ট করে। এতে গ্লোবাল ভ্যারিয়েবল ও বিওএম (BOM) ফিচার (যেমন history, location, setTimeout) থাকে।
*   **`Document` অবজেক্ট:** এটি `Window` অবজেক্টের একটি প্রপার্টি (`window.document`), যা ওই উইন্ডোর ভেতরে লোড হওয়া নির্দিষ্ট HTML ওয়েব পেজ বা ডম-কে নির্দেশ করে।

---

### **Q103: Describe the difference between a cookie, `sessionStorage` and `localStorage` in browsers. / ব্রাউজারে cookie, `sessionStorage` এবং `localStorage` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Cookie:** Small storage (~4KB). Sent to server automatically on every HTTP request. Used for server auth sessions.
*   **`localStorage`:** Larger storage (~5-10MB). Never expires unless manually cleared. Client-side only.
*   **`sessionStorage`:** Storage (~5MB). Cleared automatically when the browser tab is closed. Client-side only.

**অনুবাদ (Bangla Translation):**
*   **Cookie:** ছোট স্টোরেজ (মাত্র ৪KB)। প্রতিটি HTTP রিকোয়েস্টে সার্ভারে ট্রাভেল করে। সেশন ও অথেন্টিকেশনে ব্যবহৃত হয়।
*   **`localStorage`:** বড় স্টোরেজ (৫-১০MB)। ম্যানুয়ালি মুছে না ফেলা পর্যন্ত ব্রাউজারে স্থায়ীভাবে থেকে যায়।
*   **`sessionStorage`:** স্টোরেজ (৫MB)। ব্রাউজার ট্যাব বন্ধ করলেই মেমোরি থেকে সাথে সাথে মুছে যায়।

---

### **Q104: How do you make an HTTP request using the Fetch API? / Fetch API ব্যবহার করে কীভাবে HTTP রিকোয়েস্ট পাঠাবেন?**

**Answer (English):**
Using the native `fetch()` function which returns a Promise:
```javascript
// GET Request
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));

// POST Request
fetch('https://api.example.com/data', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John' })
});
```

**অনুবাদ (Bangla Translation):**
নেটিভ `fetch()` ফাংশন ব্যবহার করে যা প্রমিজ রিটার্ন করে:
```javascript
// GET রিকোয়েস্ট
fetch('https://api.example.com/data')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));

// POST রিকোয়েস্ট
fetch('https://api.example.com/data', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'John' })
});
```

---

### **Q105: What are the different ways to make an API call in JavaScript? / JavaScript-এ এপিআই কল করার বিভিন্ন উপায় কী কী?**

**Answer (English):**
1.  **Fetch API:** Native promise-based modern standard.
2.  **`XMLHttpRequest` (XHR):** Legacy event-based object.
3.  **`Axios` / `TanStack Query`:** Popular third-party HTTP client libraries.
4.  **`async/await` syntax:** Paired with `fetch` or `axios`.

**অনুবাদ (Bangla Translation):**
1.  **Fetch API:** আধুনিক প্রমিজ-বেসড নেটিভ স্ট্যান্ডার্ড।
2.  **`XMLHttpRequest` (XHR):** পুরাতন ইভেন্ট-বেসড মেথড।
3.  **`Axios`:** জনপ্রিয় থার্ড-পার্টি এইচটিটিপি ক্লায়েন্ট লাইব্রেরি।
4.  **`async/await`:** ফেচ বা এক্সিওসের সাথে ব্যবহার করা সংক্ষেপ মেথড।

---

### **Q106: Explain AJAX in as much detail as possible. / AJAX সম্পর্কে যতদূর সম্ভব বিস্তারিত ব্যাখ্যা করুন।**

**Answer (English):**
AJAX stands for **Asynchronous JavaScript and XML**. It is not a technology itself, but a technique for building fast dynamic web pages.
*   **Core Concept:** Allows web pages to send and receive data asynchronously from a web server in the background **without reloading the entire web page**.
*   Uses `fetch()` or `XMLHttpRequest` behind the scenes to update parts of a DOM page dynamically.

**অনুবাদ (Bangla Translation):**
AJAX-এর পূর্ণরূপ হলো **Asynchronous JavaScript and XML**। এটি কোনো একক প্রযুক্তি নয়, বরং ডায়নামিক ওয়েব পেজ বানানোর একটি বিশেষ টেকনিক।
*   **মূল ধারণা:** পুরো ওয়েব পেজ রিফ্রেশ বা লোড না করে ব্যাকগ্রাউন্ডে সার্ভারের সাথে অ্যাসিনক্রোনাসলি ডেটা আদান-প্রদান করতে সাহায্য করে।
*   এটি নেপথ্যে `fetch()` বা `XMLHttpRequest` ব্যবহার করে পেজের নির্দিষ্ট অংশ ডায়নামিকালি আপডেট করে।

---

### **Q107: What are the advantages and disadvantages of using AJAX? / AJAX ব্যবহারের সুবিধা ও অসুবিধাগুলো কী কী?**

**Answer (English):**
*   **Advantages:**
    1.  Better User Experience (smooth page updates without refreshing).
    2.  Reduces Server Load & Bandwidth (only requested data is transferred).
    3.  Fast and interactive applications.
*   **Disadvantages:**
    1.  SEO Challenges (search engines may miss dynamic data if not SSR).
    2.  Browser Back/Forward Button Issues (URL doesn't change by default).
    3.  Relies on JavaScript enabled in client browser.

**অনুবাদ (Bangla Translation):**
*   **সুবিধাসমূহ:**
    1.  উন্নত ইউজার এক্সপেরিয়েন্স (পেজ রিফ্রেশ না করেই দ্রুত ডাটা আপডেট)।
    2.  সার্ভার লোড ও ব্যান্ডউইথ সাশ্রয় (কেবল প্রয়োজনীয় ডাটা আদান-প্রদান হয়)।
*   **অসুবিধাসমূহ:**
    1.  এসইও (SEO) চ্যালেঞ্জ (সার্ভার সাইড রেন্ডারিং না থাকলে গুগল বট ডাইনামিক ডেটা পড়তে পারে না)।
    2.  ব্রাউজার ব্যাক বাটন সমস্যা (ইউআরএল পরিবর্তিত হয় না)।

---

### **Q108: What are the differences between `XMLHttpRequest` and `fetch()` in JavaScript and browsers? / `XMLHttpRequest` এবং `fetch()` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`XMLHttpRequest`:** Older callback/event-based API. Tracks download/upload progress natively (`xhr.onprogress`). Requires more code.
*   **`fetch()`:** Modern Promise-based API. Cleaner syntax, supports `async/await`. Does not reject on HTTP error status codes like 404 or 500 (requires checking `response.ok`).

**অনুবাদ (Bangla Translation):**
*   **`XMLHttpRequest`:** পুরাতন ইভেন্ট-বেসড মেথড। ফাইল আপলোড/ডাউনলোড প্রোগ্রেস নেটিভালি ট্র্যাক করা যায় (`onprogress`)। কোড বড় হয়।
*   **`fetch()`:** আধুনিক প্রমিজ-বেসড মেথড। কোড অনেক পরিষ্কার। তবে ৪-৪ বা ৫০০ এইচটিটিপি এররে সরাসরি রিজেক্ট হয় না (`response.ok` দিয়ে চেক করতে হয়)।

---

### **Q109: How do you abort a web request using `AbortController` in JavaScript? / JavaScript-এ `AbortController` ব্যবহার করে কীভাবে ওয়েব রিকোয়েস্ট বাতিল করবেন?**

**Answer (English):**
Create an instance of `AbortController`, pass its `signal` to `fetch()`, and call `controller.abort()` when cancellation is needed.
*   **Example:**
    ```javascript
    const controller = new AbortController();
    fetch(url, { signal: controller.signal })
      .catch(err => { if (err.name === 'AbortError') console.log('Aborted!'); });
    
    // Abort request
    controller.abort();
    ```

**অনুবাদ (Bangla Translation):**
`AbortController`-এর একটি ইন্সট্যান্স তৈরি করে তার `signal` প্রপার্টিটি `fetch()`-এ পাস করতে হয়, এবং রিকোয়েস্ট বাতিল করতে `controller.abort()` কল করতে হয়।
*   **উদাহরণ:**
    ```javascript
    const controller = new AbortController();
    fetch(url, { signal: controller.signal })
      .catch(err => { if (err.name === 'AbortError') console.log('Aborted!'); });
    
    // রিকোয়েস্ট বাতিল করা
    controller.abort();
    ```

---

### **Q110: Explain how JSONP works (and how it’s not really Ajax). / JSONP কীভাবে কাজ করে এবং কেন এটি প্রকৃতপক্ষে AJAX নয় তা ব্যাখ্যা করুন।**

**Answer (English):**
JSONP (JSON with Padding) was a legacy technique to bypass browser **Same-Origin Policy** cross-domain restrictions before CORS existed.
*   **How it works:** Dynamically creates a `<script src="http://example.com/data?callback=myFunc">` tag because `<script>` tags are not restricted by Same-Origin Policy. The server wraps JSON inside a JS callback call: `myFunc({ data })`.
*   **Why not real AJAX:** It does not use `XMLHttpRequest` or `fetch()`, and is limited strictly to `GET` requests.

**অনুবাদ (Bangla Translation):**
JSONP (JSON with Padding) হলো CORS আসার পূর্বে ব্রাউজারের **Same-Origin Policy** বাইপাস করে অন্য ডোমেন থেকে ডাটা আনার একটি সনাতন টেকনিক।
*   **কাজের নিয়ম:** ব্রাউজারে ডাইনামিকালি একটি `<script src="...&callback=myFunc">` ট্যাগ যোগ করা হয় (যেহেতু স্ক্রিপ্ট ট্যাগে অরিজিন ব্লক থাকে না)। সার্ভার তখন JSON ডাটাটিকে একটি ফাংশন কলের ভেতর পুরে পাঠায়।
*   **কেন এটি রিয়েল AJAX নয়:** এটি কোনো `XMLHttpRequest` বা `fetch()` ব্যবহার করে না এবং কেবল `GET` রিকোয়েস্টই পাঠাতে পারে।
