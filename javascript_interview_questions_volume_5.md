# JavaScript Interview Questions Guide: Volume 5 (Questions 151 - 193)

This guide contains detailed answers in English alongside complete Bangla translations for questions 151 to 193 from the uploaded JavaScript Interview Questions PDF.

---

### **Q151: What are Web Workers and how can they be used to improve performance? / Web Workers কী এবং পারফরম্যান্স বাড়াতে এগুলো কীভাবে ব্যবহার করা যায়?**

**Answer (English):**
Web Workers are background scripts that run in a separate thread parallel to the main UI thread.
*   **Performance Improvement:** Offloads heavy CPU tasks (like complex calculations, parsing large files, image processing) away from the main thread, keeping the user interface completely responsive without freezing or lagging.

**অনুবাদ (Bangla Translation):**
Web Workers হলো ব্যাকগ্রাউন্ড স্ক্রিপ্ট যা ব্রাউজারের মেইন ইউআই (UI) থ্রেড থেকে আলাদা একটি থ্রেডে চলে।
*   **পারফরম্যান্স বৃদ্ধি:** এটি মেমোরি-সংবেদনশীল বা ভারী গাণিতিক হিসাবগুলো মেইন থ্রেড থেকে সরিয়ে ব্যাকগ্রাউন্ডে সম্পন্ন করায়, যার ফলে ইউজার ইন্টারফেস স্ক্রিন ফ্রিজ বা ল্যাগ না করে স্মুথ থাকে।

---

### **Q152: Explain the concept of caching and how it can be used to improve performance. / ক্যাশিং (Caching) ধারণাটি ব্যাখ্যা করুন এবং এটি পারফরম্যান্স বাড়াতে কীভাবে কাজ করে?**

**Answer (English):**
Caching is the technique of storing copies of files or HTTP API responses in a temporary high-speed storage location (browser cache, memory cache, Service Worker cache, or CDN).
*   **Benefits:** Reduces latency and server bandwidth by avoiding repeated network round-trips for static assets (images, CSS, JS bundles).

**অনুবাদ (Bangla Translation):**
ক্যাশিং হলো কোনো ফাইল বা এপিআই রেসপন্সের একটি অনুলিপি অস্থায়ী মেমোরিতে (যেমন ব্রাউজার ক্যাশ বা সার্ভিস ওয়ার্কার) সেভ রাখার পদ্ধতি।
*   **সুবিধা:** একই ডাটা বারবার সার্ভার থেকে ডাউনলোড করা লাগে না, ফলে নেটওয়ার্ক ল্যাটেন্সি কমে এবং পেজ মুহূর্তের মধ্যে লোড হয়।

---

### **Q153: What are some tools that can be used to measure and analyze JavaScript performance? / JavaScript পারফরম্যান্স মাপার ও অ্যানালাইসিস করার কিছু টুলস কী কী?**

**Answer (English):**
1.  **Chrome DevTools:** Performance Panel (CPU profiling, flame charts) and Memory Panel (heap snapshots for memory leaks).
2.  **Lighthouse:** Automated auditing tool for Core Web Vitals, TTI, and bundle performance.
3.  **WebPageTest:** Real-device network performance analysis.
4.  **`console.time()` / `performance.now()`:** Code-level execution benchmarks.

**অনুবাদ (Bangla Translation):**
1.  **Chrome DevTools:** Performance ও Memory প্যানেল (সিপিইউ প্রোফাইলিং এবং মেমোরি লিক ট্র্যাকিং)।
2.  **Lighthouse:** পেজ স্পিড ও ওয়েব ভাইটালসের জন্য স্বয়ংক্রিয় অডিট টুল।
3.  **WebPageTest:** রিয়েল ডিভাইসে নেটওয়ার্ক পারফরম্যান্স মাপার টুল।
4.  **`performance.now()`:** কোডের নির্দিষ্ট অংশের রান হওয়ার সময় সুনির্দিষ্টভাবে বের করার জন্য।

---

### **Q154: How can you optimize network requests for better performance? / উন্নত পারফরম্যান্সের জন্য নেটওয়ার্ক রিকোয়েস্ট কীভাবে অপ্টিমাইজ করবেন?**

**Answer (English):**
1.  **Minimize HTTP Requests:** Bundle CSS/JS files and use SVGs or image spriting.
2.  **Use HTTP/2 or HTTP/3:** Enables multiplexing over a single TCP connection.
3.  **Compression:** Enable Gzip or Brotli compression on the server.
4.  **Cache-Control & CDNs:** Serve assets close to the user using Edge CDNs and cache headers.
5.  **Data Pagination & Debouncing:** Avoid fetching unnecessary data.

**অনুবাদ (Bangla Translation):**
1.  **রিকোয়েস্ট সংখ্যা কমানো:** কোড বান্ডেল করা এবং স্প্রাইট ইমেজ ব্যবহার করা।
2.  **HTTP/2 ব্যবহার:** একটি কানেকশনে একসাথে অনেক ফাইল আদান-প্রদান করা।
3.  **ডাটা কম্প্রেশন:** সার্ভারে Gzip বা Brotli কম্প্রেশন অন রাখা।
4.  **ক্যাশিং ও সিডিএন:** কন্টেন্ট ডেলিভারি নেটওয়ার্ক (CDN) ও ক্যাশ হেডার ব্যবহার।

---

### **Q155: What are the different types of testing in software development? / সফটওয়্যার ডেভেলপমেন্টে বিভিন্ন ধরনের টেস্টিং কী কী?**

**Answer (English):**
1.  **Unit Testing:** Testing individual functions or components in complete isolation.
2.  **Integration Testing:** Testing how multiple modules work together.
3.  **End-to-End (E2E) Testing:** Testing the complete user flow from UI to database using automated real-browser interaction.
4.  **Regression / Acceptance Testing:** Ensuring new changes don't break existing functionality and meet business requirements.

**অনুবাদ (Bangla Translation):**
1.  **Unit Testing:** একটি নির্দিষ্ট ফাংশন বা কম্পোনেন্টকে একদম আলাদা করে টেস্ট করা।
2.  **Integration Testing:** একাধিক মডিউল একসাথে ঠিকমতো কাজ করছে কিনা তা পরীক্ষা করা।
3.  **End-to-End (E2E) Testing:** পুরো সিস্টেম বা ব্রাউজার ফ্লো শুরু থেকে শেষ পর্যন্ত ইউজারের দৃষ্টিকোণ থেকে অটোমেটেড টেস্ট করা।
4.  **Regression Testing:** নতুন কোড দেওয়ার পর আগের ফিচারগুলো ভেঙে গেছে কিনা তা পরীক্ষা করা।

---

### **Q156: Explain the difference between unit testing, integration testing, and end-to-end testing. / Unit testing, Integration testing, এবং End-to-end testing এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Unit Testing:** Fast, cheap, isolated. Tests single units (e.g., a math helper function). External dependencies are mocked.
*   **Integration Testing:** Medium speed and cost. Tests interaction between interconnected modules (e.g., component + API state store).
*   **E2E Testing:** Slower, expensive, high confidence. Tests actual app running in real browsers end-to-end (e.g., user login to checkout payment flow).

**অনুবাদ (Bangla Translation):**
*   **Unit Testing:** অত্যন্ত দ্রুত ও সহজ। বিচ্ছিন্ন একক ফাংশন পরীক্ষা করা হয় (বাইরের সব কিছু মক করা থাকে)।
*   **Integration Testing:** মাঝারি গতির। একাধিক মডিউলের মধ্যবর্তী মেলবন্ধন টেস্ট করা হয়।
*   **E2E Testing:** ধীরগতির কিন্তু সর্বাধিক নির্ভরযোগ্য। আসল ব্রাউজারে সম্পূর্ণ ইউজার জার্নি (যেমন লগইন থেকে শুরু করে পেমেন্ট) পরীক্ষা করা হয়।

---

### **Q157: What are some popular JavaScript testing frameworks? / জনপ্রিয় কিছু JavaScript টেস্টিং ফ্রেমওয়ার্ক কী কী?**

**Answer (English):**
*   **Unit/Integration:** Jest, Vitest, Mocha, Jasmine.
*   **E2E Testing:** Cypress, Playwright, Selenium.
*   **Testing Utilities:** React Testing Library (RTL).

**অনুবাদ (Bangla Translation):**
*   **ইউনিট ও ইন্টিগ্রেশন:** Jest, Vitest, Mocha, Jasmine।
*   **ই-টু-ই (E2E):** Cypress, Playwright, Selenium।
*   **ইউটিলিটি:** React Testing Library (RTL)।

---

### **Q158: How do you write unit tests for JavaScript code? / JavaScript কোডের জন্য কীভাবে ইউনিট টেস্ট লিখবেন?**

**Answer (English):**
Using a test framework like Jest or Vitest with the standard `describe`, `it`/`test`, and `expect` assertion pattern:
```javascript
// sum.js
export const sum = (a, b) => a + b;

// sum.test.js
import { sum } from './sum';

describe('Sum function', () => {
  it('should correctly add two numbers', () => {
    expect(sum(2, 3)).toBe(5);
  });
});
```

**অনুবাদ (Bangla Translation):**
Jest বা Vitest এর মতো ফ্রেমওয়ার্ক দিয়ে `describe`, `it`, এবং `expect` ব্যবহার করে টেস্ট কোড লিখতে হয়:
```javascript
// sum.js
export const sum = (a, b) => a + b;

// sum.test.js
import { sum } from './sum';

describe('Sum function', () => {
  it('should correctly add two numbers', () => {
    expect(sum(2, 3)).toBe(5);
  });
});
```

---

### **Q159: Explain the concept of test-driven development (TDD). / Test-Driven Development (TDD) ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
TDD is a software development methodology where developers write tests **before** writing the actual feature code following the **Red-Green-Refactor** cycle:
1.  **Red:** Write a failing test for a non-existent feature.
2.  **Green:** Write minimal production code just enough to pass the test.
3.  **Refactor:** Clean up and optimize the code while ensuring tests remain green.

**অনুবাদ (Bangla Translation):**
TDD হলো এমন একটি ডেভেলপমেন্ট পদ্ধতি যেখানে মূল কোড লেখার **আগেই** টেস্ট কোড লেখা হয়। এটি **Red-Green-Refactor** চক্র মেনে চলে:
1.  **Red:** নতুন ফিচারের জন্য ফেইলিং টেস্ট লেখা।
2.  **Green:** কেবল টেস্টটি পাস করার উপযোগী ন্যূনতম কোড লেখা।
3.  **Refactor:** টেস্ট সবুজ রেখে মূল কোডটিকে সুন্দর ও অপ্টিমাইজ করা।

---

### **Q160: What are mocks and stubs and how are they used in testing? / টেস্টিংয়ে Mocks এবং Stubs কী এবং কীভাবে এগুলো ব্যবহার করা হয়?**

**Answer (English):**
*   **Stubs:** Provide hardcoded dummy responses to function calls to isolate the unit being tested from external data services (e.g., stubbing an API to return fake JSON).
*   **Mocks:** More advanced objects that verify **behavior**—tracking how many times a function was called, with what specific arguments, and in what order.

**অনুবাদ (Bangla Translation):**
*   **Stubs:** এগুলো ডামি বা ফিক্সড রেসপন্স প্রদান করে যাতে আসল সার্ভারে কানেক্ট না করেই টেস্ট চালানো যায়।
*   **Mocks:** এগুলো কোডের **আচরণ** ট্র্যাক করে (যেমন- কোনো ফাংশন কতবার কল হয়েছে বা কোন আর্গুমেন্টে কল করা হয়েছে তা টেস্ট করা)।

---

### **Q161: How can you test asynchronous code in JavaScript? / JavaScript-এ অ্যাসিনক্রোনাস কোড কীভাবে টেস্ট করবেন?**

**Answer (English):**
1.  **`async/await` in test blocks:**
    ```javascript
    test('fetches user data', async () => {
      const data = await fetchUser();
      expect(data.name).toBe('John');
    });
    ```
2.  **Returning Promises:** Return the promise directly from the test function.
3.  **Done Callback:** Call `done()` when async task completes.

**অনুবাদ (Bangla Translation):**
1.  **টেস্ট ব্লকে `async/await` ব্যবহার করা:**
    ```javascript
    test('fetches user data', async () => {
      const data = await fetchUser();
      expect(data.name).toBe('John');
    });
    ```
2.  **প্রমিজ রিটার্ন করা:** টেস্ট ফাংশন থেকে সরাসরি প্রমিজ রিটার্ন করা।

---

### **Q162: What are some best practices for writing maintainable and effective tests in JavaScript? / মেইনটেইনযোগ্য এবং কার্যকর টেস্ট লেখার সেরা অনুশীলনগুলো কী কী?**

**Answer (English):**
1.  **Test Behavior, Not Implementation Details:** Focus on inputs and UI outputs rather than private internal state variables.
2.  **FIRST Principles:** Fast, Isolated/Independent, Repeatable, Self-validating, Timely.
3.  **Clear Test Descriptions:** Use descriptive names for `it()` blocks.
4.  **Avoid Shared Mutable Test State:** Reset state before each test (`beforeEach`).

**অনুবাদ (Bangla Translation):**
1.  **আচরণ টেস্ট করা:** ইনার কোড টেস্ট না করে ইনপুট ও আউটপুট ভ্যালু টেস্ট করা।
2.  **FIRST নিয়ম মানা:** টেস্ট দ্রুত, স্বাধীন এবং রিপিটযোগ্য হতে হবে।
3.  **পরিষ্কার নাম দেওয়া:** `it()` ব্লকে স্পষ্ট ডেসক্রিপশন দেওয়া।
4.  **স্টেট রিসেট করা:** প্রতিটি টেস্টের আগে `beforeEach` দিয়ে ডামি ডেটা ফ্রেশ রাখা।

---

### **Q163: Explain the concept of code coverage and how it can be used to assess test quality. / Code Coverage ধারণাটি ব্যাখ্যা করুন এবং এটি কীভাবে টেস্টের গুণগত মান বিচারে সাহায্য করে?**

**Answer (English):**
Code coverage is a quantitative metric measuring the percentage of source code executed while running the automated test suite.
*   **Metrics:** Statement coverage, Branch coverage (`if/else`), Function coverage, Line coverage.
*   *Note:* High coverage (e.g., 90%) indicates thorough execution but does not guarantee the test assertions themselves are well-written or bug-free.

**অনুবাদ (Bangla Translation):**
কোড কাভারেজ (Code Coverage) হলো একটি পরিমাপক শতাংশ যা দেখায় টেস্ট চালানোর সময় সোর্স কোডের কত শতাংশ অংশ ফায়ার বা এক্সিকিউট হয়েছে।
*   **পরিমাপের দিক:** Statement, Branch (`if/else`), Function, Line কাভারেজ।
*   *নোট:* ৯০% কাভারেজ থাকা মানেই অ্যাপে বাগ নেই তা শতভাগ নিশ্চিত নয়, তবে এটি ভালো টেস্ট কোডের নির্দেশক।

---

### **Q164: What are some tools that can be used for JavaScript testing? / JavaScript টেস্টিংয়ের জন্য কিছু টুলস কী কী?**

**Answer (English):**
Jest, Vitest, Cypress, Playwright, Istanbul (for coverage reports), MSW (Mock Service Worker for API mocking).

**অনুবাদ (Bangla Translation):**
Jest, Vitest, Cypress, Playwright, Istanbul (কোড কাভারেজের জন্য), MSW (এপিআই মকিংয়ের জন্য)।

---

### **Q165: What are design patterns and why are they useful? / Design Patterns কী এবং এগুলো কেন দরকারী?**

**Answer (English):**
Design patterns are reusable, battle-tested solutions to common software architecture problems.
*   **Benefits:** Accelerates development, provides a common vocabulary among developers, improves code readability, maintainability, and architectural scalability.

**অনুবাদ (Bangla Translation):**
ডিজাইন প্যাটার্নস (Design Patterns) হলো সফটওয়্যার আর্কিটেকচারের সুপরিচিত সমস্যাগুলোর পরীক্ষিত এবং পুনরায় ব্যবহারযোগ্য সমাধান কাঠামো।
*   **সুবিধা:** কোড স্ট্রাকচার সুন্দর করে, ডেভেলপারদের বোঝার সুবিধার জন্য স্ট্যান্ডার্ড আর্কিটেকচার দেয় এবং কোড স্কেল করা সহজ করে।

---

### **Q166: Explain the concept of the Singleton pattern. / Singleton pattern ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
The Singleton pattern restricts the instantiation of a class to **one single instance** across the entire application, providing a global point of access to it.
*   **Use Cases:** Database connection pools, global state stores (Redux store), logger singletons.

**অনুবাদ (Bangla Translation):**
সিংগেলটন প্যাটার্ন (Singleton Pattern) নিশ্চিত করে যে পুরো অ্যাপ্লিকেশনে একটি ক্লাসের **কেবলমাত্র একটিই মাত্র অবজেক্ট ইন্সট্যান্স** থাকবে।
*   **ব্যবহার:** ডেটাবেজ কানেকশন পুল, গ্লোবাল রেডাক্স (Redux) স্টোর বা লগিং অবজেক্ট।

---

### **Q167: What is the Factory pattern and how is it used? / Factory pattern কী এবং এটি কীভাবে ব্যবহার করা হয়?**

**Answer (English):**
The Factory pattern is a creational design pattern that uses factory functions/classes to create objects without specifying the exact concrete class or creation logic to the client caller.
*   **Use Case:** Creating different types of UI buttons or notification elements dynamically based on user input.

**অনুবাদ (Bangla Translation):**
ফ্যাক্টরি প্যাটার্ন (Factory Pattern) হলো সরাসরি `new` কিওয়ার্ড না লিখে কোনো ফাংশন বা মেথড ব্যবহারের মাধ্যমে রানটাইমে ডাইনামিকালি বিভিন্ন অবজেক্ট তৈরি করার পদ্ধতি।

---

### **Q168: Explain the Observer pattern and its use cases. / Observer pattern এবং এর ব্যবহার ক্ষেত্রসমূহ ব্যাখ্যা করুন।**

**Answer (English):**
The Observer pattern establishes a one-to-many dependency where a subject object maintains a list of observer dependents and automatically notifies them of state changes.
*   **Use Cases:** Event Listeners in DOM, RxJS observables, pub/sub event emitters, state updates in frontend frameworks.

**অনুবাদ (Bangla Translation):**
অবজারভার প্যাটার্ন (Observer Pattern) হলো এমন একটি প্যাটার্ন যেখানে একটি সাবজেক্ট অবজেক্ট তার একাধিক অবজারভারের সাথে যুক্ত থাকে এবং সাবজেক্টের কোনো ডাটা চেঞ্জ হলে সাথে সাথে সব অবজারভার স্বয়ংক্রিয়ভাবে আপডেট নোটিফিকেশন পেয়ে যায় (যেমন- DOM Event Listeners বা RxJS)।

---

### **Q169: What is the Module pattern and how does it help with encapsulation? / Module pattern কী এবং এটি এনক্যাপসুলেশনে কীভাবে সাহায্য করে?**

**Answer (English):**
The Module pattern uses IIFEs and closures to encapsulate private variables and functions, exposing only a public API object.
*   **Encapsulation:** Protects internal code state from being mutated globally.

**অনুবাদ (Bangla Translation):**
মডিউল প্যাটার্ন IIFE এবং ক্লোজার ব্যবহার করে কোডের প্রাইভেট অংশ লুকিয়ে রেখে কেবল কিছু পাবলিক ফাংশন বাইরে রিটার্ন করে এনক্যাপসুলেশন নিশ্চিত করে।

---

### **Q170: Explain the concept of the Prototype pattern. / Prototype pattern ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
The Prototype pattern creates new objects by cloning an existing prototype object using `Object.create()`, avoiding expensive initialization.

**অনুবাদ (Bangla Translation):**
প্রোটোটাইপ প্যাটার্ন হলো নতুন অবজেক্ট তৈরির সময় শূন্য থেকে শুরু না করে বিদ্যমান কোনো অবজেক্টকে ক্লোন বা কপি (`Object.create`) করে নতুন অবজেক্ট বানানোর পদ্ধতি।

---

### **Q171: What is the Decorator pattern and how is it used? / Decorator pattern কী এবং এটি কীভাবে ব্যবহার করা হয়?**

**Answer (English):**
The Decorator pattern dynamically wraps an existing object to add new responsibilities or behaviors without modifying the underlying class code.

**অনুবাদ (Bangla Translation):**
ডেকোরেটর প্যাটার্ন মূল অবজেক্ট বা ক্লাসের কোড পরিবর্তন না করে তার ওপর নতুন একটি র্যাপার মেথড বসিয়ে বাড়তি ফিচার যোগ করার কাজে ব্যবহৃত হয়।

---

### **Q172: Explain the concept of the Strategy pattern. / Strategy pattern ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
The Strategy pattern defines a family of interchangeable algorithms, encapsulating each one, and selecting the appropriate strategy dynamically at runtime (e.g., choosing payment strategies: Paypal vs CreditCard).

**অনুবাদ (Bangla Translation):**
স্ট্র্যাটেজি প্যাটার্ন একাধিক অ্যালগরিদমকে আলাদা ক্লাসে রেখে রানটাইমে প্রয়োজন অনুযায়ী নির্বাচন করে রান করতে সাহায্য করে (যেমন পেমেন্ট মেথড সিলেক্ট করা: বিকাশ বনাম কার্ড)।

---

### **Q173: What is the Command pattern and how is it used? / Command pattern কী এবং এটি কীভাবে ব্যবহার করা হয়?**

**Answer (English):**
The Command pattern encapsulates a request as a standalone object containing `execute()` and `undo()` methods. Useful for implementing multi-level **Undo/Redo** logic or action queues.

**অনুবাদ (Bangla Translation):**
কমান্ড প্যাটার্ন কোনো একটি রিকোয়েস্টকে `execute()` ও `undo()` পদ্ধতি সহ স্বাধীন অবজেক্ট বানায়, যা সফটওয়্যারে **Undo/Redo** (পূর্বাবস্থায় ফিরে যাওয়া) ফিচার বানাতে ব্যবহৃত হয়।

---

### **Q174: Why is extending built-in JavaScript objects not a good idea? / JavaScript-এর বিল্ট-ইন অবজেক্ট প্রসারিত করা (extending built-in prototypes) কেন ভালো ধারণা নয়?**

**Answer (English):**
Adding properties to native prototypes (like `Array.prototype.customMethod = ...`) is dangerous because:
1.  **Name Collisions:** Future native JS updates or third-party libraries might introduce a method with the same name, breaking code.
2.  **Global Pollution:** Unintended side effects across all arrays/objects in the codebase.

**অনুবাদ (Bangla Translation):**
জাভাস্ক্রিপ্টের নেটিভ প্রোটোটাইপ (যেমন `Array.prototype`)-এ নিজস্ব ফাংশন যোগ করা ঝুঁকিপূর্ণ কারণ অন্য কোনো থার্ড-পার্টি লাইব্রেরি বা জাভাস্ক্রিপ্টের নতুন সংস্করণে একই নামে অফিশিয়াল ফিচার আসলে সম্পূর্ণ প্রজেক্টের কোড ক্র্যাশ করবে।

---

### **Q175: What is Cross-Site Scripting (XSS) and how can you prevent it? / Cross-Site Scripting (XSS) কী এবং কীভাবে এটি প্রতিরোধ করবেন?**

**Answer (English):**
XSS is a vulnerability where attackers inject malicious scripts into web pages viewed by other users.
*   **Prevention:**
    1.  Sanitize and escape all user input before rendering.
    2.  Use `textContent` instead of `innerHTML`.
    3.  Implement Content Security Policy (CSP) headers.
    4.  Use `HttpOnly` cookies for sensitive tokens.

**অনুবাদ (Bangla Translation):**
XSS হলো হ্যাকিংয়ের এমন একটি ফাঁদ যেখানে হ্যাকার অন্য ইউজারের দেখা ওয়েব পেজে ক্ষতিকারক জাভাস্ক্রিপ্ট কোড পুশ করে দেয়।
*   **প্রতিরোধ:** ইনপুট ফিল্টার করা, `innerHTML`-এর বদলে `textContent` ব্যবহার করা এবং CSP হেডার ব্যবহার করা।

---

### **Q176: Explain the concept of Cross-Site Request Forgery (CSRF) and its mitigation techniques. / Cross-Site Request Forgery (CSRF) ধারণাটি এবং এটি প্রতিরোধের উপায় ব্যাখ্যা করুন।**

**Answer (English):**
CSRF tricks an authenticated user's browser into executing unintended, unauthorized requests to a target web server using saved cookies.
*   **Mitigation:** Anti-CSRF Tokens (synchronizer token pattern), `SameSite=Strict` or `SameSite=Lax` cookie flags, and checking CORS origin headers.

**অনুবাদ (Bangla Translation):**
CSRF হলো হ্যাকারের তৈরি ক্ষতিকারক সাইট থেকে ইউজারের অজান্তে তার ব্রাউজারে থাকা কুকি ব্যবহার করে অন্য সার্ভারে অবৈধ রিকোয়েস্ট পাঠানো।
*   **প্রতিরোধ:** Anti-CSRF টোকেন ব্যবহার করা এবং কুকিতে `SameSite=Strict` সেট করা।

---

### **Q177: How can you prevent SQL injection vulnerabilities in JavaScript applications? / JavaScript অ্যাপ্লিকেশনে SQL Injection কীভাবে প্রতিরোধ করবেন?**

**Answer (English):**
Always use **Parameterized Queries** (Prepared Statements) or an ORM/Query Builder (like Prisma, Knex) instead of raw string concatenation when writing SQL queries.

**অনুবাদ (Bangla Translation):**
সরাসরি স্ট্রিং যোগ করে SQL কোড না লিখে **Parameterized Queries** বা প্রিসমা (Prisma)-র মতো আধুনিক ORM ব্যবহার করা।

---

### **Q178: What are some best practices for handling sensitive data in JavaScript? / JavaScript-এ সংবেদনশীল ডেটা (Sensitive Data) হ্যান্ডেল করার সেরা উপায়গুলো কী কী?**

**Answer (English):**
Never store passwords or private API keys in client-side code. Store JWTs in `HttpOnly`, `Secure` cookies (not `localStorage`). Transmit data via HTTPS only.

**অনুবাদ (Bangla Translation):**
লগইন টোকেন বা সিক্রেট কি কখনো `localStorage`-এ না রেখে `HttpOnly`, `Secure` কুকিতে রাখা এবং সবসময় HTTPS ব্যবহার করা।

---

### **Q179: Explain Content Security Policy (CSP) and how it enhances security. / Content Security Policy (CSP) কী এবং এটি কীভাবে নিরাপত্তা বাড়ায়?**

**Answer (English):**
CSP is an HTTP response header (`Content-Security-Policy`) that allows developers to define an approved whitelist of trusted domain sources from which scripts, styles, images, and fonts can load. Prevents XSS and clickjacking.

**অনুবাদ (Bangla Translation):**
CSP হলো এইচটিটিপি হেডার যা ব্রাউজারকে বলে দেয় পেজে কেবল কোন কোন নিরাপদ ডোমেন থেকে স্ক্রিপ্ট বা ফাইল লোড করা যাবে। এটি XSS আক্রমণ ঠেকায়।

---

### **Q180: What are some common security headers and their purpose? / সাধারণ কিছু সিকিউরিটি হেডার এবং তাদের কাজ কী?**

**Answer (English):**
*   `Content-Security-Policy`: Restricts allowed content sources.
*   `X-Frame-Options`: Prevents Clickjacking by disallowing framing (`DENY`).
*   `Strict-Transport-Security` (HSTS): Forces HTTPS connections.
*   `X-Content-Type-Options: nosniff`: Prevents MIME type sniffing.

**অনুবাদ (Bangla Translation):**
*   `Content-Security-Policy`: অনুমোদিত ফাইলের সোর্স ফিল্টার করা।
*   `X-Frame-Options`: ক্লিকজ্যাকিং প্রতিরোধে iframe বন্ধ করা।
*   `Strict-Transport-Security`: জোরপূর্বক HTTPS কানেকশন চালু রাখা।

---

### **Q181: How can you prevent clickjacking attacks? / Clickjacking আক্রমণ কীভাবে প্রতিরোধ করবেন?**

**Answer (English):**
Set the `X-Frame-Options: DENY` or `SAMEORIGIN` HTTP header, or use CSP `frame-ancestors 'self'` to stop malicious sites from embedding your webpage inside an invisible `<iframe>`.

**অনুবাদ (Bangla Translation):**
`X-Frame-Options: DENY` হেডার দিয়ে যেকোনো থার্ড-পার্টি ওয়েবসাইটে আপনার সাইটকে অদৃশ্য `<iframe>` হিসেবে এম্বেড হওয়া ব্লক করে দেওয়া।

---

### **Q182: Explain the concept of input validation and its importance in security. / ইনপুট ভ্যালিডেশন ধারণাটি এবং নিরাপত্তার ক্ষেত্রে এর গুরুত্ব ব্যাখ্যা করুন।**

**Answer (English):**
Input validation ensures user-submitted data conforms to expected formats, types, and lengths before processing. It is the first line of defense against XSS, SQL Injection, and command injection attacks.

**অনুবাদ (Bangla Translation):**
ইউজারের পাঠানো ডেটা সিস্টেমে ঢোকার আগেই তা সঠিক ফরম্যাটের কিনা তা চেক করা। এটি XSS ও SQL ইনজেকশন ঠেকানোর প্রথম ডিফেন্স।

---

### **Q183: What are some tools and techniques for identifying security vulnerabilities in JavaScript code? / JavaScript কোডের সিকিউরিটি দুর্বলতা খোঁজার কিছু টুলস ও পদ্ধতি কী কী?**

**Answer (English):**
Use `npm audit` for dependency vulnerabilities, static code analyzers like `ESLint` with security plugins, OWASP ZAP, and Snyk.

**অনুবাদ (Bangla Translation):**
ডিপেনডেন্সি চেক করতে `npm audit`, কোড স্ক্যান করতে `ESLint` সিকিউরিটি প্লাগ-ইন এবং Snyk ব্যবহার করা।

---

### **Q184: How can you implement secure authentication and authorization in JavaScript applications? / JavaScript অ্যাপ্লিকেশনে নিরাপদ অথেন্টিকেশন ও অথরাইজেশন কীভাবে ইমপ্লিমেন্ট করবেন?**

**Answer (English):**
Use HTTPS, issue short-lived JWTs stored in `HttpOnly` cookies, validate tokens on the server for every protected route, and implement Role-Based Access Control (RBAC).

**অনুবাদ (Bangla Translation):**
HTTPS ব্যবহার করা, `HttpOnly` কুকিতে সংক্ষিপ্ত মেয়াদের JWT টোকেন রাখা এবং সার্ভার সাইডে Role-Based Access Control (RBAC) দিয়ে পারমিশন ভ্যালিডেট করা।

---

### **Q185: Explain the same-origin policy with regards to JavaScript. / JavaScript-এর ক্ষেত্রে Same-Origin Policy ব্যাখ্যা করুন।**

**Answer (English):**
The Same-Origin Policy is a fundamental browser security mechanism that restricts scripts on one origin from reading data from another origin. An origin is defined by **Protocol + Domain + Port**. E.g., `http://site.com` cannot read `https://site.com`.

**অনুবাদ (Bangla Translation):**
Same-Origin Policy হলো ব্রাউজারের সিকিউরিটি নিয়ম যা এক ডোমেনের জাভাস্ক্রিপ্টকে অন্য ডোমেনের ডেটা পড়তে বাধা দেয়। **প্রোটোকল + ডোমেন + পোর্ট** তিনটিই হুবহু মিলতে হয়।

---

### **Q186: What is `'use strict';` in JavaScript for? / JavaScript-এ `'use strict';` কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
Enables **Strict Mode** in JavaScript.
*   **Advantages:** Catches silent coding errors by throwing explicit exceptions (e.g., prevents undeclared global variables, duplicate parameter names, or writing to read-only properties).

**অনুবাদ (Bangla Translation):**
এটি জাভাস্ক্রিপ্টের কড়া বা নিরেট মোড (Strict Mode) চালু করে। ডিক্লেয়ার না করা গ্লোবাল ভ্যারিয়েবল বা ভুল কোড লিখলে তা সাইলেন্টলি পার না হয়ে সরাসরি এরর থ্রো করে।

---

### **Q187: What tools and techniques do you use for debugging JavaScript code? / JavaScript কোড ডিবাগ করার জন্য আপনি কোন কোন টুলস ও পদ্ধতি ব্যবহার করেন?**

**Answer (English):**
1.  **Chrome DevTools:** Breakpoints, conditional breakpoints, Scope inspection, and Call Stack viewer.
2.  `debugger;` statements.
3.  `console` methods (`console.log`, `table`, `error`, `group`).
4.  React/Redux DevTools for framework state.

**অনুবাদ (Bangla Translation):**
1.  **Chrome DevTools:** ব্রাউজারে ব্রেকপয়েন্ট বসানো, কল স্ট্যাক ও স্কোপ চেক করা।
2.  কোডের ভেতরে `debugger;` স্টেটমেন্ট বসানো।
3.  `console.table()`, `console.error()` ব্যবহার করা।

---

### **Q188: How does JavaScript garbage collection work? / JavaScript-এ গার্বেজ কালেকশন (Garbage Collection) কীভাবে কাজ করে?**

**Answer (English):**
Garbage collection is an automatic memory management process in JS engines.
*   **Primary Algorithm (Mark-and-Sweep):** Starts from root objects (`window`), traverses all reachable references, marks them as "in use", and sweeps away (deallocates) all unmarked unreachable objects from memory.

**অনুবাদ (Bangla Translation):**
গার্বেজ কালেকশন মেমোরি খালি করার মেকানিজম। এটি **Mark-and-Sweep** অ্যালগরিদম দিয়ে গ্লোবাল রুট থেকে শুরু করে যেসব অবজেক্টের আর কোনো কানেকশন কোডে নেই, তাদের মেমোরি থেকে অটোমেটিক মুছে ফেলে।

---

### **Q189: Explain what a single page app is and how to make one SEO-friendly. / Single Page App (SPA) কী এবং একে কীভাবে SEO-friendly করা যায়?**

**Answer (English):**
An SPA loads a single HTML file and dynamically updates page views via JS without full browser reloads.
*   **SEO Optimization:** Use **Server-Side Rendering (SSR)** or **Static Site Generation (SSG)** via frameworks like Next.js or Nuxt.js so search engine crawlers receive pre-rendered HTML.

**অনুবাদ (Bangla Translation):**
SPA হলো এমন অ্যাপ যা একবার মাত্র HTML লোড করে এবং পরবর্তীতে পেজ রিফ্রেশ ছাড়া ডাইনামিকালি ইউআই আপডেট করে।
*   **SEO ফ্রেন্ডলি করা:** Next.js দিয়ে Server-Side Rendering (SSR) বা SSG করা যাতে গুগল বট সরাসরি সম্পূর্ণ HTML পড়তে পারে।

---

### **Q190: How can you share code between JavaScript files? / JavaScript ফাইলগুলোর মধ্যে কীভাবে কোড শেয়ার করবেন?**

**Answer (English):**
Using ES6 Module `export` in the source file and `import` in the target file. In Node.js CommonJS, use `module.exports` and `require()`.

**অনুবাদ (Bangla Translation):**
ES6 মডিউলের `export` এবং `import` ব্যবহার করে (অথবা Node.js-এ `module.exports` ও `require()`)।

---

### **Q191: How do you organize your code? / আপনি কীভাবে আপনার কোড সাজান বা সংগঠিত করেন?**

**Answer (English):**
I follow a modular architecture by feature/domain folder structures, separating concerns into presentation components, state logic, API services, and utility helpers, following clean code principles and ESLint formatting.

**অনুবাদ (Bangla Translation):**
আমি মডুলার আর্কিটেকচার অনুসরন করি; যেখানে ইউআই কম্পোনেন্ট, এপিআই সার্ভিস, স্টেট ও ইউটিলিটি ফাইলগুলোকে আলাদা ফোল্ডারে ভাগ করে সাজানো হয়।

---

### **Q192: What are some of the advantages/disadvantages of writing JavaScript code in a language that compiles to JavaScript? / JavaScript-এ কম্পাইল হওয়া অন্য ভাষায় (যেমন TypeScript) কোড লেখার সুবিধা ও অসুবিধা কী কী?**

**Answer (English):**
*   **Advantages (e.g., TypeScript):** Static type safety, compile-time error detection, superior IDE autocomplete and refactoring support.
*   **Disadvantages:** Additional build step, learning curve, and extra setup configuration overhead.

**অনুবাদ (Bangla Translation):**
*   **সুবিধা (যেমন TypeScript):** স্ট্যাটিক টাইপ সেফটি, কোড রান করার আগেই এরর ধরা পড়া এবং চমৎকার অটো-কমপ্লিশন।
*   **অসুবিধা:** নতুন করে কম্পাইল/বিল্ড স্টেপ যুক্ত হওয়া এবং শেখার বাড়তি চাপ।

---

### **Q193: When would you use `document.write()`? / কখন আপনি `document.write()` ব্যবহার করবেন?**

**Answer (English):**
`document.write()` is heavily **deprecated** and should almost **never** be used in modern web development. Calling it after a page has finished loading will completely overwrite the entire HTML document. It is only seen in legacy third-party analytics scripts or simple educational code sandboxes.

**অনুবাদ (Bangla Translation):**
`document.write()` বর্তমানে পরিত্যক্ত (Deprecated) এবং আধুনিক ওয়েব ডেভেলপমেন্টে এটি **কখনোই ব্যবহার করা উচিত নয়**। পেজ লোড শেষ হওয়ার পর এটি কল করলে সম্পূর্ণ পেজ মুছে যায়। এটি কেবল পুরাতন এনালিমেন্টাল টেস্ট ছাড়া আর কোথাও ব্যবহৃত হয় না।
