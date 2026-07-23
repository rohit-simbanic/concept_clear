# Top 20 Computer Science Fundamentals & OOP Concepts

This guide contains 20 essential, industry-standard interview questions and answers covering **Object-Oriented Programming (OOP) paradigms, Software Design Principles (SOLID), Data Structures & Algorithms, Operating Systems, and System Architecture**. Each concept includes a detailed technical explanation in English followed by a complete Bangla translation.

---

## Table of Contents
1. Object-Oriented Programming (OOP) & Its 4 Main Pillars
2. Encapsulation & Data Hiding
3. Abstraction: Abstract Classes vs Interfaces
4. Inheritance vs Composition ("Favor Composition over Inheritance")
5. Polymorphism: Compile-Time (Overloading) vs Runtime (Overriding)
6. SOLID Principles Breakdown
7. DRY, KISS, and YAGNI Software Design Principles
8. Process vs Thread and Multithreading
9. Stack Memory vs Heap Memory Allocation
10. Concurrency vs Parallelism
11. Big O Notation & Time/Space Complexity Analysis
12. Array vs Linked List (Memory Structure & Complexity)
13. Stack (LIFO) vs Queue (FIFO) Data Structures
14. Hash Tables & Hash Collision Resolution (Chaining vs Open Addressing)
15. Binary Search vs Linear Search
16. ACID Properties in Relational Databases
17. Database Indexing (B-Tree Mechanics & Performance)
18. Deadlock in Operating Systems & The 4 Coffman Conditions
19. HTTP vs HTTPS (TLS/SSL Handshake & Encryption)
20. Web Architecture: REST vs GraphQL vs WebSockets

---

### **Q1: What is Object-Oriented Programming (OOP) and what are its 4 main pillars? / Object-Oriented Programming (OOP) কী এবং এর ৪টি মূল স্তম্ভ (Pillars) কী কী?**

**Answer (English):**
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which contain data (fields/attributes) and code (methods/functions).
*   **The 4 Pillars of OOP:**
    1.  **Encapsulation:** Bundling data and methods operating on that data inside a single unit (class), while restricting direct access to internal states.
    2.  **Abstraction:** Hiding internal complex implementation details and showing only essential features to the outside world.
    3.  **Inheritance:** Allowing a child class to inherit properties and behaviors from a parent class, promoting code reusability.
    4.  **Polymorphism:** The ability of an object or method to take on multiple forms (e.g., method overriding and overloading).

**অনুবাদ (Bangla Translation):**
Object-Oriented Programming (OOP) হলো একটি প্রোগ্রামিং প্যারাডাইম যা "অবজেক্ট" ধারণার ওপর প্রতিষ্ঠিত। অবজেক্টের মধ্যে ডাটা (ফিল্ড) এবং কোড (মেথড) থাকে।
*   **OOP-এর ৪টি মূল স্তম্ভ:**
    1.  **Encapsulation (এনক্যাপসুলেশন):** ডাটা ও মেথডকে একটি ক্লাসের মধ্যে আবদ্ধ রাখা এবং সরাসরি বাইর থেকে ডাটা অ্যাক্সেস করা রুদ্ধ করা।
    2.  **Abstraction (অ্যাবস্ট্রাকশন):** ভেতরের জটিল কোড লুকিয়ে রেখে বাইরে কেবল প্রয়োজনীয় ফিচারটুকু দেখানো।
    3.  **Inheritance (ইনহেরিটেন্স):** প্যারেন্ট ক্লাসের বৈশিষ্ট্য ও মেথড চাইল্ড ক্লাসে উত্তরাধিকার সূত্রে পাওয়ার মাধ্যমে কোড রি-ইউজ করা।
    4.  **Polymorphism (পলিমরফিজম):** একই ফাংশন বা মেথডের ভিন্ন ভিন্ন রূপ বা আচরণ প্রকাশ করার ক্ষমতা।

---

### **Q2: What is Encapsulation and how do getters/setters enforce data hiding? / Encapsulation কী এবং Getters/Setters কীভাবে ডাটা হাইডিং নিশ্চিত করে?**

**Answer (English):**
Encapsulation wraps data (variables) and methods into a single class entity while making class variables `private` (Data Hiding).
*   **How it works:** Outside code cannot mutate private variables directly. Controlled access is granted exclusively through public `getter` and `setter` methods.
*   **Benefits:** Allows validation inside setters before modifying data, prevents unauthorized state corruption, and makes class implementation flexible to change without breaking external callers.

**অনুবাদ (Bangla Translation):**
Encapsulation হলো ডাটা এবং কাজকে একসাথে ক্লাসে বেঁধে রাখা এবং ক্লাস ভ্যারিয়েবলকে `private` করে বাইরে থেকে আড়াল (Data Hiding) করা।
*   **কীভাবে কাজ করে:** বাইরের কোড সরাসরি প্রাইভেট ভ্যারিয়েবল পরিবর্তন করতে পারে না। কেবল পাবলিক `getter` ও `setter` মেথডের মাধ্যমে ডাটা পড়া বা পরিবর্তন করা যায়।
*   **সুবিধা:** সেটারের ভেতর সঠিক ডাটা ভ্যালিডেশন করা যায়, দুর্ঘটনাবশত ভুল মান বসা আটকায় এবং ক্লাসের অভ্যন্তরীণ লজিক নিরাপদ রাখে।

---

### **Q3: What is Abstraction? What is the difference between an Abstract Class and an Interface? / Abstraction কী? Abstract Class এবং Interface-এর মধ্যে পার্থক্য কী?**

**Answer (English):**
Abstraction focuses on *what* an object does rather than *how* it does it.
*   **Abstract Class:** A blueprint class that cannot be instantiated directly. It can contain both abstract methods (without bodies) and concrete methods (with implementation code), as well as member variables with access modifiers. Used for tightly related classes sharing code.
*   **Interface:** A contract specifying a set of method signatures that implementing classes *must* define. It contains no state/instance variables (traditionally) and enforces what behaviors a class must have regardless of hierarchy. Used for unrelated classes sharing capabilities.

**অনুবাদ (Bangla Translation):**
Abstraction হলো ভেতরের বাস্তবায়ন না দেখিয়ে বাইরে কাজের চুক্তি প্রকাশ করা।
*   **Abstract Class:** এমন একটি ক্লাস যার অবজেক্ট তৈরি করা যায় না। এতে মেথডের বর্ণনা (Abstract Method) এবং সরাসরি কোড লেখা মেথড (Concrete Method) উভয়ই থাকতে পারে। সম্পর্কিত ক্লাসের মধ্যে সাধারণ কোড শেয়ার করতে ব্যবহৃত হয়।
*   **Interface:** একটি লিখিত চুক্তি যা বলে দেয় কোনো ক্লাসকে কী কী মেথড অবশ্যই তৈরি করতে হবে। এটি একাধিক অসংশ্লিষ্ট ক্লাসে একই ধরনের ক্ষমতা যোগ করতে ব্যবহৃত হয়।

---

### **Q4: What is Inheritance and why do software architects recommend "Composition over Inheritance"? / Inheritance কী এবং সফটওয়্যার আর্কিটেক্টরা কেন "Inheritance-এর চেয়ে Composition ব্যবহার" করার পরামর্শ দেন?**

**Answer (English):**
Inheritance enables a sub-class to acquire fields and methods of a super-class (`is-a` relationship).
*   **Why Composition over Inheritance?**
    1.  **Tight Coupling:** Deep inheritance trees create fragile code where changing a base class breaks sub-classes unexpectedly.
    2.  **Inflexible at Runtime:** Inheritance is fixed at compile time.
    3.  **Composition (`has-a` relationship):** Assembling complex objects by combining smaller, independent classes via references. It provides flexible runtime behavior replacement and loose coupling.

**অনুবাদ (Bangla Translation):**
Inheritance হলো প্যারেন্ট ক্লাস থেকে চাইল্ড ক্লাসে মেথড ও বৈশিষ্ট্য নেওয়া (`is-a` সম্পর্ক)।
*   **Inheritance-এর চেয়ে Composition কেন সেরা?**
    1.  **টাইট কাপলিং:** গভীর ইনহেরিটেন্স ট্রিতে প্যারেন্ট ক্লাসে সামান্য পরিবর্তন করলে চাইল্ড ক্লাসের কোড ভেঙে যায়।
    2.  **অনমনীয়তা:** কম্পাইল টাইমে ইনহেরিটেন্স ফিক্স হয়ে যায়।
    3.  **Composition (`has-a` সম্পর্ক):** ছোট ছোট স্বাধীন অবজেক্টকে একত্রিত করে বড় অবজেক্ট তৈরি করা। এতে রান-টাইমে সহজে আচরণ বদলানো যায় এবং কোড ফ্লেক্সিবল থাকে।

---

### **Q5: What is Polymorphism? Explain the difference between Compile-Time and Runtime Polymorphism. / Polymorphism কী? Compile-Time এবং Runtime Polymorphism-এর পার্থক্য ব্যাখ্যা করুন।**

**Answer (English):**
Polymorphism allows objects of different classes to respond differently to the same method call.
*   **Compile-Time Polymorphism (Method Overloading):** Multiple methods in the same class share the exact same name but have different parameter signatures (type or count). Resolved during compilation.
*   **Runtime Polymorphism (Method Overriding):** A child class provides a specific implementation of a method that is already defined in its parent class (`@Override`). Resolved at runtime based on the actual object instance type.

**অনুবাদ (Bangla Translation):**
Polymorphism হলো একই মেথডের অবস্থাভেদে ভিন্ন ভিন্ন আচরণ করার ক্ষমতা।
*   **Compile-Time (Method Overloading):** একই ক্লাসের ভেতর একাধিক মেথডের নাম একই কিন্তু প্যারামিটারের সংখ্যা বা টাইপ আলাদা। এটি কম্পাইল করার সময়েই নির্ধারিত হয়।
*   **Runtime (Method Overriding):** প্যারেন্ট ক্লাসের মেথডকে চাইল্ড ক্লাসে নতুন করে নিজস্ব কোড দিয়ে রি-রাইট করা। এটি রান-টাইমে অবজেক্টের ধরণ অনুযায়ী নির্ধারিত হয়।

---

### **Q6: Explain the SOLID Principles of Object-Oriented Design. / অবজেক্ট-ওরিয়েন্টেড ডিজাইনের SOLID নীতিগুলো ব্যাখ্যা করুন।**

**Answer (English):**
SOLID is an acronym for 5 design principles for maintainable software:
*   **S - Single Responsibility Principle (SRP):** A class should have one, and only one, reason to change.
*   **O - Open/Closed Principle (OCP):** Software entities should be open for extension, but closed for modification.
*   **L - Liskov Substitution Principle (LSP):** Derived classes must be completely substitutable for their base classes without breaking the app.
*   **I - Interface Segregation Principle (ISP):** Clients should not be forced to depend on interfaces they do not use (prefer small, specific interfaces).
*   **D - Dependency Inversion Principle (DIP):** High-level modules should depend on abstractions, not on concrete low-level details.

**অনুবাদ (Bangla Translation):**
SOLID হলো ভালো সফটওয়্যার ডিজাইনের ৫টি মূল নীতির সংক্ষেপ:
*   **S (Single Responsibility):** একটি ক্লাসের কেবল একটিমাত্র নির্দিষ্ট দায়িত্ব বা কাজের কারণ থাকা উচিত।
*   **O (Open/Closed):** কোড নতুন ফিচার যোগ করার জন্য উন্মুক্ত (Open) কিন্তু আগের মূল কোড পরিবর্তনের জন্য বন্ধ (Closed) থাকবে।
*   **L (Liskov Substitution):** প্যারেন্ট ক্লাসের জায়গায় চাইল্ড ক্লাস বসালেও প্রোগ্রাম না ভেঙে নিখুঁতভাবে চলতে হবে।
*   **I (Interface Segregation):** বড় ইন্টারফেসের বদলে ছোট ও সুনির্দিষ্ট ইন্টারফেস ব্যবহার করা উচিত।
*   **D (Dependency Inversion):** হাই-লেভেল কোড সরাসরি কংক্রিট ক্লাসের ওপর না ভেসে অ্যাবস্ট্রাকশন/ইন্টারফেসের ওপর নির্ভর করবে।

---

### **Q7: What are DRY, KISS, and YAGNI software design principles? / DRY, KISS, এবং YAGNI ডিজাইন প্রিন্সিপাল বলতে কী বোঝায়?**

**Answer (English):**
*   **DRY (Don't Repeat Yourself):** Every piece of knowledge or logic must have a single, unambiguous representation within a system. Extract reusable functions instead of copying code.
*   **KISS (Keep It Simple, Stupid):** Systems work best if they are kept simple rather than made complex. Avoid over-engineering.
*   **YAGNI (You Aren't Gonna Need It):** Do not add functionality until it is necessary. Avoid writing code for hypothetical future requirements.

**অনুবাদ (Bangla Translation):**
*   **DRY (Don't Repeat Yourself):** একই কোড বা লজিক বারবার না লিখে রি-ইউজেবল ফাংশন বানিয়ে একবার লেখা।
*   **KISS (Keep It Simple, Stupid):** অনর্থক কোড জটিল না করে যতটা সম্ভব সহজ-সরল রাখা।
*   **YAGNI (You Aren't Gonna Need It):** ভবিষ্যতে লাগতে পারে ভেবে আজই অহেতুক বাড়তি ফিচার বানিয়ে কোড ভারী না করা।

---

### **Q8: What is the difference between a Process and a Thread? / Process এবং Thread এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Process:** An executing instance of a program in its own isolated virtual memory space allocated by the OS. Processes do not share memory with each other directly (Inter-Process Communication required).
*   **Thread:** The smallest execution unit within a process ("lightweight process"). Multiple threads within the same process share the same heap memory space, file descriptors, and code segment, allowing fast communication but requiring synchronization (locks/mutexes) to prevent race conditions.

**অনুবাদ (Bangla Translation):**
*   **Process (প্রসেস):** অপারেটিং সিস্টেম দ্বারা বরাদ্দ করা একটি স্বতন্ত্র রানিং প্রোগ্রাম। এদের নিজস্ব মেমোরি থাকে এবং এরা সরাসরি একে অপরের মেমোরি এক্সেস করতে পারে না।
*   **Thread (থ্রেড):** প্রসেসের ভেতরের সবচেয়ে ছোট কাজ করার একক। একই প্রসেসের একাধিক থ্রেড নিজেদের মধ্যে মেমোরি ও ডাটা শেয়ার করতে পারে, তবে এতে রেস কন্ডিশন এড়াতে সিঙ্ক্রোনাইজেশন লাগে।

---

### **Q9: What is the difference between Stack Memory and Heap Memory? / Stack Memory এবং Heap Memory এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Stack Memory:** Used for static memory allocation, local variables, and function call execution frames. Follows LIFO (Last-In-First-Out) order, has extremely fast access speeds, but is limited in size. Variables are automatically deallocated when the function exits.
*   **Heap Memory:** Used for dynamic memory allocation (e.g., objects, arrays created with `new`). Managed by Garbage Collection (or manual allocation/deallocation). Slower access speed, but much larger size.

**অনুবাদ (Bangla Translation):**
*   **Stack Memory:** লোকাল ভ্যারিয়েবল এবং ফাংশন কলের হিসেব রাখার জন্য ব্যবহৃত হয়। এটি LIFO নিয়মে কাজ করে, অত্যন্ত দ্রুতগতির কিন্তু আকারে ছোট। ফাংশন শেষ হলে মেমোরি অটো মুছে যায়।
*   **Heap Memory:** ডায়নামিক অবজেক্ট ও অ্যারে জমা রাখার জন্য ব্যবহৃত হয়। গার্বেজ কালেকশন দ্বারা পরিচালিত হয়। স্ট্যাকের চেয়ে ধীরগতির কিন্তু আকারে অনেক বড়।

---

### **Q10: What is the difference between Concurrency and Parallelism? / Concurrency এবং Parallelism এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Concurrency:** About **dealing with** many things at once. Managing multiple tasks making progress by context-switching rapidly on a single CPU core.
*   **Parallelism:** About **doing** many things at once. Executing multiple tasks simultaneously at the exact same physical instant on multiple CPU cores or processors.

**অনুবাদ (Bangla Translation):**
*   **Concurrency:** একসাথে একাধিক কাজ সামলানোর (Context Switching) ক্ষমতা। একটিমাত্র সিপিইউ কোরে দ্রুত কাজ বদলে প্রোগ্রেস রাখা।
*   **Parallelism:** একই সাথে একাধিক কাজ বাস্তবে একসাথে করা। একাধিক সিপিইউ কোরে একই মুহূর্তে আলাদা আলাদা কাজ চলা।

---

### **Q11: What is Big O Notation? Explain Time and Space Complexity with examples. / Big O Notation কী? উদাহরণসহ Time এবং Space Complexity ব্যাখ্যা করুন।**

**Answer (English):**
Big O Notation measures the performance or efficiency of an algorithm as the input size ($N$) grows to infinity.
*   **Time Complexity:** Measures how runtime scales with input size.
    *   $O(1)$ Constant: Array lookup by index.
    *   $O(\log N)$ Logarithmic: Binary Search.
    *   $O(N)$ Linear: Single loop over an array.
    *   $O(N^2)$ Quadratic: Nested loops (e.g., Bubble Sort).
*   **Space Complexity:** Measures additional memory allocated by the algorithm as input grows.

**অনুবাদ (Bangla Translation):**
Big O Notation হলো ইনপুটের আকার ($N$) বাড়ার সাথে সাথে একটি অ্যালগরিদমের রান-টাইম ও মেমোরি কতটুকু বাড়ে তা মাপার গাণিতিক একক।
*   **Time Complexity (সময়কাল):** $O(1)$ (ইনডেক্স ধরে মান খোঁজা), $O(\log N)$ (Binary Search), $O(N)$ (একক লুপ), $O(N^2)$ (নেস্টেড লুপ)।
*   **Space Complexity (মেমোরি জায়গা):** অ্যালগরিদমটি চলাকালীন অতিরিক্ত কতটুকু মেমোরি জায়গা নেয় তার হিসাব।

---

### **Q12: What is the difference between an Array and a Linked List in memory? / মেমোরি গঠনের দিক থেকে Array এবং Linked List এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Array:** Stores elements in **contiguous (sequential) memory locations**. Fast index-based access ($O(1)$), but inserting/deleting elements at arbitrary positions requires shifting elements ($O(N)$). Fixed size upon allocation.
*   **Linked List:** Stores elements (nodes) in **non-contiguous memory locations**. Each node contains data and a pointer/reference to the next node. Inserting/deleting nodes is fast ($O(1)$ if pointer is known), but accessing elements requires linear traversal ($O(N)$). Dynamic size.

**অনুবাদ (Bangla Translation):**
*   **Array:** মেমোরিতে **পরপর (Contiguous) জায়গায়** ডাটা রাখে। ইনডেক্স ধরে সরাসরি এক্সেস ফাস্ট ($O(1)$), কিন্তু মাঝখানে ডাটা যোগ/বিয়োগ করা ধীরগতির ($O(N)$)।
*   **Linked List:** মেমোরির **যেকোনো জায়গায়** নোড আকারে ডাটা রাখে। প্রতিটি নোডে ডাটা ও পরের নোডের ঠিকানা (Pointer) থাকে। ডাটা যোগ/বিয়োগ করা সহজ ($O(1)$), কিন্তু ইনডেক্স দিয়ে সরাসরি খোঁজা ধীরগতির ($O(N)$)।

---

### **Q13: What is the difference between Stack and Queue data structures? / Stack এবং Queue ডাটা স্ট্রাকচারের মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Stack (LIFO - Last In, First Out):** Data added last is removed first (like a stack of plates). Operations: `push()` (insert at top) and `pop()` (remove from top). Used in browser undo/redo, call stacks, and recursion.
*   **Queue (FIFO - First In, First Out):** Data added first is removed first (like a line at a ticket counter). Operations: `enqueue()` (insert at back) and `dequeue()` (remove from front). Used in printer job queues, event loops, and message brokers.

**অনুবাদ (Bangla Translation):**
*   **Stack (LIFO - খেপের শেষটি আগে বের হবে):** সবার শেষে যা রাখবেন তা সবার আগে বের হবে (যেমন- প্লেটের তাক)। ব্যবহার: ব্রাউজারের Undo/Redo বা ফাংশন কল স্ট্যাক।
*   **Queue (FIFO - লাইনের প্রথমটি আগে বের হবে):** সবার আগে যা ঢুকবে তা সবার আগে বের হবে (যেমন- টিকিটের লাইন)। ব্যবহার: প্রিন্টার কিউ বা মেসেজ ব্রোকার।

---

### **Q14: How do Hash Tables work and how do you resolve Hash Collisions? / Hash Table কীভাবে কাজ করে এবং Hash Collision কীভাবে সমাধান করা হয়?**

**Answer (English):**
A Hash Table maps keys to values using a **Hash Function**, which computes an integer index into an array.
*   **Hash Collision:** Occurs when two distinct keys yield the exact same index from the hash function.
*   **Collision Resolution Methods:**
    1.  **Separate Chaining:** Each array bucket holds a Linked List of key-value pairs that hash to the same index.
    2.  **Open Addressing (Linear Probing):** Searches for the next available empty slot in the array sequentially when a collision happens.

**অনুবাদ (Bangla Translation):**
Hash Table একটি **Hash Function** ব্যবহার করে কী-কে (Key) অ্যারের ইনডেক্সে রূপান্তর করে ভ্যালু জমা রাখে।
*   **Hash Collision:** যখন দুটি আলাদা Key হ্যাশ ফাংশন থেকে হুবহু একই ইনডেক্স নম্বর তৈরি করে।
*   **সমাধানের উপায়:**
    1.  **Separate Chaining:** অ্যারের প্রতিটি ঘরে একটি করে Linked List রাখা যাতে একাধিক ডাটা চেইন হিসেবে জমে।
    2.  **Open Addressing:** কলিশন হলে অ্যারের পরবর্তী ফাঁকা ঘরে ডাটা বসিয়ে দেওয়া।

---

### **Q15: What is the difference between Binary Search and Linear Search? / Binary Search এবং Linear Search এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Linear Search:** Sequentially checks every element in an array from start to end until a target is found. Works on unsorted arrays. Time complexity: $O(N)$.
*   **Binary Search:** Requires a **sorted array**. Repeatedly divides the search interval in half by comparing the target with the middle element. Time complexity: $O(\log N)$.

**অনুবাদ (Bangla Translation):**
*   **Linear Search:** শুরু থেকে শেষ পর্যন্ত একে একে প্রতিটি উপাদান চেক করে খোঁজে। এলোমেলো (Unsorted) অ্যারেতে কাজ করে। সময়কাল: $O(N)$।
*   **Binary Search:** অ্যারে অবশ্যই **সাজানো (Sorted)** হতে হয়। ডাটাকে দুইভাগে ভাগ করে মাঝখানের মানের সাথে তুলনা করে খোঁজে। সময়কাল: $O(\log N)$ (অনেক ফাস্ট)।

---

### **Q16: What are the ACID properties in Relational Databases? / রিলেশনাল ডাটাবেজে ACID প্রপার্টিজ বলতে কী বোঝায়?**

**Answer (English):**
ACID ensures reliability in database transactions:
*   **A - Atomicity:** "All or Nothing". Either all statements in a transaction complete successfully, or the entire transaction is rolled back.
*   **C - Consistency:** Transactions move the database from one valid state to another, obeying all schema constraints and rules.
*   **I - Isolation:** Concurrent transactions execute independently without interfering with each other (preventing dirty reads).
*   **D - Durability:** Once a transaction commits, its changes are permanent and survive system crashes.

**অনুবাদ (Bangla Translation):**
ACID হলো ডাটাবেজ ট্রানজ্যাকশনের স্থায়িত্ব ও সঠিকতা রক্ষার ৪টি নিয়ম:
*   **Atomicity (পারমাণবিকতা):** "হলে সব হবে, না হলে কিছুই না"। সব কাজ সফল হবে নতুবা পুরো কাজ বাতিল (Rollback) হবে।
*   **Consistency (সামঞ্জস্যতা):** ডাটাবেজের সমস্ত নিয়মকানুন মেনে ডাটা আপডেট হবে।
*   **Isolation (বিচ্ছিন্নতা):** একাধিক ট্রানজ্যাকশন পাশাপাশি চললেও একটি অপরটির কাজে হস্তক্ষেপ করবে না।
*   **Durability (স্থায়িত্ব):** ট্রানজ্যাকশন সেভ হয়ে গেলে সার্ভার বন্ধ হলেও ডাটা চিরতরে স্থায়ী থাকবে।

---

### **Q17: How does Database Indexing work under the hood? / ডাটাবেজ ইনডেক্সিং (Database Indexing) কীভাবে কাজ করে?**

**Answer (English):**
Without an index, the database performs a **Full Table Scan** ($O(N)$) reading every row from disk.
*   **How Indexing Works:** An index creates a self-balancing search tree data structure (usually a **B-Tree** or **B+Tree**) on specified table columns.
*   **Performance:** Reduces lookup time from $O(N)$ to $O(\log N)$ by navigating the B-Tree pointers.
*   **Trade-off:** Speeds up `SELECT` queries, but slows down `INSERT`, `UPDATE`, and `DELETE` operations because the index tree must be updated on every write, while taking extra disk space.

**অনুবাদ (Bangla Translation):**
ইনডেক্স না থাকলে ডাটাবেজ পুরো টেবিলের প্রতিটি সারি (Full Table Scan) চেক করে ডাটা খোঁজে।
*   **কীভাবে কাজ করে:** ইনডেক্স নির্দিষ্ট কলামের ওপর একটি **B-Tree** ডাটা স্ট্রাকচার বানিয়ে রাখে।
*   **পারফরম্যান্স:** ডাটা খোঁজার গতি $O(N)$ থেকে কমিয়ে $O(\log N)$-এ নামিয়ে আনে।
*   **সুবিধা-অসুবিধা:** `SELECT` কোয়েরির গতি বাড়ায়, কিন্তু অতিরিক্ত মেমোরি নেয় এবং `INSERT`/`UPDATE`-এর সময় ইনডেক্স ট্রি আপডেট হওয়ায় লেখার কাজ সামান্য ধীরগতির হয়।

---

### **Q18: What is a Deadlock in Operating Systems and what are the 4 Coffman Conditions? / অপারেটিং সিস্টেমে Deadlock কী এবং Coffman-এর ৪টি শর্ত কী কী?**

**Answer (English):**
A Deadlock occurs when two or more processes are blocked forever, waiting for resources held by each other.
*   **4 Coffman Conditions (All 4 must hold for a deadlock to occur):**
    1.  **Mutual Exclusion:** Resources cannot be shared simultaneously.
    2.  **Hold and Wait:** Processes hold allocated resources while waiting for additional ones.
    3.  **No Preemption:** Resources cannot be forcibly confiscated from a process.
    4.  **Circular Wait:** A closed chain of processes exists where each process waits for a resource held by the next.

**অনুবাদ (Bangla Translation):**
Deadlock হলো এমন এক পরিস্থিতি যেখানে একাধিক প্রসেস একে অপরের কাছে থাকা রিসোর্সের জন্য অনন্তকাল অপেক্ষা করে আটকে থাকে।
*   **Coffman-এর ৪টি শর্ত (৪টি একসাথে ঘটলেই Deadlock হয়):**
    1.  **Mutual Exclusion:** রিসোর্স একই সাথে শেয়ার করা যায় না।
    2.  **Hold and Wait:** নিজের রিসোর্স ধরে রেখে পরেরটির জন্য অপেক্ষা করা।
    3.  **No Preemption:** জোর করে প্রসেস থেকে রিসোর্স কেড়ে নেওয়া যায় না।
    4.  **Circular Wait:** চক্রাকারে একজন আরেকজনের রিসোর্সের জন্য লাইন দিয়ে আটকে থাকা।

---

### **Q19: What is the difference between HTTP and HTTPS? Explain the TLS/SSL Handshake. / HTTP এবং HTTPS এর মধ্যে পার্থক্য কী? TLS/SSL Handshake কীভাবে কাজ করে?**

**Answer (English):**
*   **HTTP (Hypertext Transfer Protocol):** Sends data over the web in plain text. Vulnerable to interception and man-in-the-middle attacks.
*   **HTTPS (HTTP Secure):** Encrypts data using **TLS/SSL** protocols over port 443.
*   **TLS/SSL Handshake Steps:**
    1.  **Client Hello:** Client sends supported TLS versions and cipher suites.
    2.  **Server Hello & Certificate:** Server responds with its chosen cipher suite and SSL Public Certificate.
    3.  **Authentication & Key Exchange:** Client verifies certificate via Certificate Authority (CA) and generates a pre-master secret encrypted with server's Public Key.
    4.  **Symmetric Session Key Creation:** Both sides compute a shared **Symmetric Session Key** for ultra-fast encrypted data transfer during the session.

**অনুবাদ (Bangla Translation):**
*   **HTTP:** ইন্টারনেটে প্লেন টেক্সট বা খোলা তথ্য পাঠায় (হ্যাক হওয়ার ঝুঁকি থাকে)।
*   **HTTPS:** TLS/SSL এনক্রিপশন ব্যবহার করে সম্পূর্ণ নিরাপদে ডাটা আদান-প্রদান করে।
*   **TLS Handshake প্রসেস:** ক্লায়েন্ট ও সার্ভার একে অপরকে হাই পাঠায় -> সার্ভার ডিজিটাল সার্টিফিকেট পাঠায় -> ক্লায়েন্ট সিমেট্রিক সিক্রেট কি (Session Key) তৈরি করে ব্যাক পাঠায় -> দুই পক্ষই গোপন কি দিয়ে ডাটা এনক্রিপ্ট করে কথা বলে।

---

### **Q20: What is the difference between REST, GraphQL, and WebSockets in Web Architecture? / ওয়েব আর্কিটেকচারে REST, GraphQL, এবং WebSockets-এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **REST (Representational State Transfer):** Resource-based HTTP architecture using standard verbs (`GET`, `POST`, `PUT`, `DELETE`). Suffer from over-fetching or under-fetching data. Stateless.
*   **GraphQL:** Query language for APIs allowing clients to request **exact** fields needed in a single `POST` request. Prevents over-fetching.
*   **WebSockets:** Full-duplex, persistent bidirectional TCP communication channel. Best for real-time applications (chat apps, live sports, stock tickers) requiring instant updates without HTTP polling overhead.

**অনুবাদ (Bangla Translation):**
*   **REST:** ইউআরএল এবং স্ট্যান্ডার্ড HTTP মেথড (`GET`, `POST`) ভিত্তিক এপিআই। এতে প্রয়োজনের চেয়ে বেশি বা কম ডাটা চলে আসার সমস্যা থাকে।
*   **GraphQL:** ক্লায়েন্ট ঠিক যতটুকু ফিল্ড চাবে সার্ভার হুবহু ততটুকুই পাঠায় (Over-fetching দূর করে)।
*   **WebSockets:** দুইমুখী (Bidirectional) সার্বক্ষণিক খোলা সকেট লাইন। চ্যাট অ্যাপ বা লাইভ স্কোরবোর্ডের মতো রিয়েল-টাইম আপডেটের জন্য সেরা।
