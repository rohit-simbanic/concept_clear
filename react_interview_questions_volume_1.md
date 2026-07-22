# React Interview Questions Guide: Volume 1 (Questions 1 - 40)

This guide contains detailed answers in English alongside complete Bangla translations for questions 1 to 40 from the uploaded React Interview Questions PDF.

---

### **Q1: What is React? Describe the benefits of React. / React কী? React-এর সুবিধাসমূহ বর্ণনা করুন।**

**Answer (English):**
React is an open-source, component-based JavaScript library developed by Meta (Facebook) for building fast, interactive user interfaces, especially Single-Page Applications (SPAs).
*   **Key Benefits:**
    1.  **Component-Based Architecture:** Encourages modular, reusable, and testable UI blocks.
    2.  **Virtual DOM & High Performance:** Minimizes expensive real DOM manipulations by using a lightweight virtual representation and efficient diffing.
    3.  **Declarative UI:** Developers describe *what* the UI should look like for a given state, and React handles rendering.
    4.  **One-Way Data Binding:** Unidirectional data flow makes application state predictable and easy to debug.
    5.  **Rich Ecosystem & Community:** Huge ecosystem of libraries, hooks, and active community support.

**অনুবাদ (Bangla Translation):**
React হলো মেটা (Facebook) দ্বারা তৈরি একটি ওপেন-সোর্স, কম্পোনেন্ট-ভিত্তিক জাভাস্ক্রিপ্ট লাইব্রেরি, যা দ্রুত ও ইন্টারঅ্যাক্টিভ ইউজার ইন্টারফেস (বিশেষ করে সিঙ্গেল পেইজ অ্যাপ্লিকেশন বা SPA) তৈরির জন্য ব্যবহৃত হয়।
*   **প্রধান সুবিধাসমূহ:**
    1.  **কম্পোনেন্ট-ভিত্তিক স্ট্রাকচার:** ইউআই-কে ছোট ছোট পুনর্ব্যবহারযোগ্য (Reusable) ব্লকে ভাগ করে কোড লেখা সহজ করে।
    2.  **ভার্চুয়াল ডম (Virtual DOM) ও গতিশীলতা:** প্রকৃত ডম সরাসরি পরিবর্তন করার খরচ কমিয়ে মেমোরিতে ভার্চুয়াল রেন্ডারিং ও ডিফিংয়ের মাধ্যমে অ্যাপের পারফরম্যান্স বৃদ্ধি করে।
    3.  **ডিক্লেয়ারেটিভ UI:** স্টেট অনুযায়ী স্ক্রিন কেমন দেখাবে তা ডিক্লেয়ার করে দিলেই রিয়্যাক্ট স্বয়ংক্রিয়ভাবে রেন্ডারিং হ্যান্ডেল করে।
    4.  **একমুখী ডেটা প্রবাহ (One-way Data Flow):** ডেটা উপর থেকে নিচে প্রবাহিত হওয়ায় অ্যাপের স্টেট ম্যানেজমেন্ট সহজ ও অনুমানযোগ্য হয়।
    5.  **সমৃদ্ধ ইকোসিস্টেম:** বিশাল কমিউনিটি সাপোর্ট ও অসংখ্য রেডিমেড লাইব্রেরির সুবিধা।

---

### **Q2: What is the difference between React Node, React Element, and a React Component? / React Node, React Element এবং React Component এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **React Element:** An immutable, plain JavaScript object describing a DOM node or component structure (e.g., created via `JSX` or `React.createElement()`).
*   **React Component:** A function or class that accepts props as input and returns a React Element tree. It encapsulates UI logic and state.
*   **React Node:** A broad union type representing anything that React can render. It includes React Elements, strings, numbers, React Fragments, arrays of nodes, booleans, `null`, or `undefined`.

**অনুবাদ (Bangla Translation):**
*   **React Element:** এটি একটি লাইটওয়েট ও অপরিবর্তনশীল (Immutable) প্লেন জাভাস্ক্রিপ্ট অবজেক্ট, যা স্ক্রিনে কী রেন্ডার হবে তার বিবরণ ধারণ করে (যেমন `JSX` বা `React.createElement()` দিয়ে তৈরি অবজেক্ট)।
*   **React Component:** এটি একটি ফাংশন বা ক্লাস যা ইনপুট হিসেবে Props গ্রহণ করে এবং একটি React Element রিটার্ন করে। এটি ইউআই লজিক ও স্টেট ধারণ করে।
*   **React Node:** এটি একটি বিস্তৃত টাইপ যা রিয়্যাক্ট ব্রাউজারে রেন্ডার করতে পারে এমন যেকোনো কিছু নির্দেশ করে (যেমন- React Element, স্ট্রিং, নাম্বার, অ্যারে, ফ্র্যাগমেন্ট, `null` বা `undefined`)।

---

### **Q3: What is JSX and how does it work? / JSX কী এবং এটি কীভাবে কাজ করে?**

**Answer (English):**
JSX stands for **JavaScript XML**. It is a syntax extension for JavaScript that allows writing HTML-like code directly inside JS files.
*   **How it works:** Browsers cannot parse JSX directly. Build tools like Babel or SWC transpile JSX into standard `React.createElement()` or `_jsx()` function calls before execution.
*   **Example:**
    ```jsx
    const element = <h1 className="title">Hello World</h1>;
    // Transpiles into:
    const element = React.createElement('h1', { className: 'title' }, 'Hello World');
    ```

**অনুবাদ (Bangla Translation):**
JSX-এর পূর্ণরূপ হলো **JavaScript XML**। এটি জাভাস্ক্রিপ্টের একটি সিনট্যাক্স এক্সটেনশন যা জাভাস্ক্রিপ্ট কোডের ভেতরে সরাসরি HTML-এর মতো দেখতে কোড লেখার সুবিধা দেয়।
*   **কীভাবে কাজ করে:** ব্রাউজার সরাসরি JSX বুঝতে পারে না। Babel বা SWC-এর মতো ট্রান্সপাইলার টুলস JSX-কে রূপান্তর করে সাধারণ `React.createElement()` ফাংশন কলে বদলে দেয়।
*   **উদাহরণ:**
    ```jsx
    const element = <h1 className="title">Hello World</h1>;
    // রূপান্তরিত হয়ে হয়:
    const element = React.createElement('h1', { className: 'title' }, 'Hello World');
    ```

---

### **Q4: What is the difference between state and props in React? / React-এ State এবং Props এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **State:** Internal, mutable data managed **within** the component itself using hooks like `useState`. Changes to state trigger a re-render of the component.
*   **Props (Properties):** External, immutable (read-only) data passed down from a **parent** component to a child component. A child cannot modify its received props directly.

**অনুবাদ (Bangla Translation):**
*   **State:** এটি কম্পোনেন্টের **নিজস্ব অভ্যন্তরীণ** পরিবর্তনযোগ্য (Mutable) ডেটা, যা `useState` বা `useReducer` দিয়ে ম্যানেজ করা হয়। স্টেট বদলালে কম্পোনেন্ট পুন রেন্ডার (Re-render) হয়।
*   **Props (Properties):** এটি **প্যারেন্ট কম্পোনেন্ট থেকে চাইল্ড কম্পোনেন্টে** পাঠানো বাহ্যিক ডেটা। চাইল্ড কম্পোনেন্টের ভেতরে প্রপস রিড-অনলি (অপরিবর্তনযোগ্য) থাকে।

---

### **Q5: What is the purpose of the `key` prop in React? / React-এ `key` প্রপসের উদ্দেশ্য কী?**

**Answer (English):**
The `key` prop is a unique string attribute used by React when rendering dynamic lists of components.
*   **Purpose:** It helps React's **Reconciliation (Diffing)** algorithm uniquely identify which items in a list have been changed, added, or removed. This optimizes DOM updates and prevents components from losing local state during list mutation.

**অনুবাদ (Bangla Translation):**
ডাইনামিক অ্যারে বা লিস্ট রেন্ডার করার সময় প্রতিটি এলিমেন্টকে আলাদাভাবে চেনার জন্য `key` প্রপস ব্যবহার করা হয়।
*   **উদ্দেশ্য:** এটি রিয়্যাক্টের **Reconciliation (Diffing)** অ্যালগরিদমকে লিস্টের কোন আইটেমটি নতুন যোগ হয়েছে, মুছে গেছে বা পরিবর্তিত হয়েছে তা নিখুঁতভাবে চিহ্নিত করতে সাহায্য করে। এতে অপ্রয়োজনীয় ডম আপডেট বন্ধ হয়।

---

### **Q6: What is the consequence of using array indices as the value for `key` in React? / React-এ `key` হিসেবে অ্যারে ইনডেক্স ব্যবহার করার পরিণতি কী?**

**Answer (English):**
Using array indices as keys can cause unexpected UI bugs and poor rendering performance if the list order changes (e.g., sorting, filtering, prepending items).
*   **Consequences:**
    1.  React uses keys to associate state with DOM nodes. If items are reordered, the index associated with an item changes, causing React to reuse DOM nodes with stale component state.
    2.  Leads to incorrect form input values, broken animations, or unnecessary re-renders.
*   *Best Practice:* Always use a unique, persistent ID (like a database primary key or UUID).

**অনুবাদ (Bangla Translation):**
লিস্টের ক্রম পরিবর্তিত হলে (যেমন- সর্টিং, ফিল্টারিং বা শুরুতে নতুন উপাদান যোগ করা) `key` হিসেবে অ্যারের ইনডেক্স ব্যবহার করলে মারাত্মক ভিজ্যুয়াল বাগ ও পারফরম্যান্স সমস্যা তৈরি হয়।
*   **পরিণতি:**
    1.  রিঅ্যাক্ট ইনডেক্স ধরে ডম নোডের স্টেট মেলায়। সিকোয়েন্স পাল্টালে ইনডেক্স বদলে যায়, ফলে পুরোনো উপাদান নতুন উপাদানের ভুল স্টেট ধরে রাখে।
    2.  ফর্ম ফিল্ডের মান ওলটপালট হওয়া, ভুল অ্যানিমেশন এবং অহেতুক রি-রেন্ডারিং ঘটে।
*   *আদর্শ নিয়ম:* সবসময় ইউনিক ও স্থায়ী আইডি (যেমন ডাটাবেজ ID বা UUID) কি হিসেবে ব্যবহার করা উচিত।

---

### **Q7: What is the difference between controlled and uncontrolled React Components? / Controlled এবং Uncontrolled রিয়্যাক্ট কম্পোনেন্টের মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Controlled Components:** Form input elements whose values are controlled directly by **React State**. Changes are handled via `onChange` handlers, making state the "single source of truth".
*   **Uncontrolled Components:** Form input elements that manage their own internal state within the **DOM**. Values are fetched on-demand using React `refs` (`useRef`).

**অনুবাদ (Bangla Translation):**
*   **Controlled Components:** ফর্মে ইনপুটের মান সরাসরি **React State** দিয়ে নিয়ন্ত্রিত হয়। ইনপুট পরিবর্তনের জন্য `onChange` মেথড ব্যবহার করা হয়। স্টেটই হলো একমাত্র অথেনটিক সোর্স।
*   **Uncontrolled Components:** ফর্মে ইনপুটের মান সরাসরি **DOM**-এর ভেতরেই থাকে। প্রয়োজনে রিয়্যাক্ট `ref` (`useRef`) দিয়ে মান রিড করা হয়।

---

### **Q8: What are some pitfalls about using context in React? / React Context ব্যবহারে কী কী সম্ভাব্য অসুবিধা বা ঝুঁকি (pitfalls) রয়েছে?**

**Answer (English):**
1.  **Unnecessary Re-renders:** Every time a Context provider's value changes, **all** consuming child components re-render automatically, even if they only use a subset of the context.
2.  **Overuse for Local State:** Using Context for component-specific local state causes unnecessary complexity and performance degradation.
3.  **Coupling & Reduced Reusability:** Components that depend heavily on Context are harder to reuse outside of their Provider tree.
*   *Mitigation:* Split contexts into smaller slices, memoize provider values with `useMemo`, or use external state managers (Zustand/Redux) for complex state.

**অনুবাদ (Bangla Translation):**
1.  **অপ্রয়োজনীয় Re-render:** কনটেক্সট প্রোভাইডারের মান সামান্য বদলালেই এর সাথে যুক্ত **সমস্ত চাইল্ড কম্পোনেন্ট** রি-রেন্ডার হয়ে যায়, এমনকি যে কম্পোনেন্ট ওই ডেটা ব্যবহারও করছে না সেটিও।
2.  **অতিরিক্ত ব্যবহার:** সাধারণ লোকাল স্টেটের কাজে কনটেক্সট ব্যবহার করলে কোড জটিল হয়ে যায় এবং পারফরম্যান্স কমে।
3.  **কমে যাওয়া পুনর্ব্যবহারযোগ্যতা:** কনটেক্সটের ওপর নির্ভরশীল কম্পোনেন্ট প্রোভাইডার ব্লকের বাইরে স্বাধীনভাবে রি-ইউজ করা যায় না।
*   *সমাধান:* ছোট ছোট কনটেক্সটে ভাগ করা, `useMemo` দিয়ে প্রোভাইডার ভ্যালু সেভ করা অথবা জ্যুস্ট্যান্ড (Zustand) বা Redux ব্যবহার করা।

---

### **Q9: What are the benefits of using hooks in React? / React-এ Hooks ব্যবহারের সুবিধাগুলো কী কী?**

**Answer (English):**
1.  **No Class Components Needed:** Enables functional components to manage state and lifecycle side-effects without writing complex class boilerplate or binding `this`.
2.  **Reusable Stateful Logic:** Custom hooks allow extracting logic into clean, testable functions shared across multiple components.
3.  **Better Code Organization:** Logic related to a single feature (e.g., data fetching + subscription) can be grouped together in a single `useEffect` instead of splitting it across `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`.

**অনুবাদ (Bangla Translation):**
1.  **ক্লাস কম্পোনেন্টের জটিলতা দূর:** জটিল ক্লাস বা `this` বাইন্ডিং ছাড়া সাধারণ ফাংশনাল কম্পোনেন্টেই স্টেট ও লাইফসাইকেল হ্যান্ডেল করা যায়।
2.  **পুনর্ব্যবহারযোগ্য লজিক:** কাস্টম হুকস বানিয়ে স্টেট ফুল লজিকগুলোকে আলাদা ফাংশন হিসেবে প্রজেক্টের যেকোনো জায়গায় রি-ইউজ করা যায়।
3.  **উন্নত কোড বিন্যাস:** একই ফিচারের লজিকগুলো একটিমাত্র `useEffect`-এ সাজিয়ে রাখা যায়, যা ক্লাসের মতো আলাদা আলাদা লাইফসাইকেল মেথডে ছড়িয়ে থাকে না।

---

### **Q10: What are the rules of React hooks? / React Hooks-এর নিয়মাবলী কী কী?**

**Answer (English):**
1.  **Only Call Hooks at the Top Level:** Never call hooks inside loops, conditions, nested functions, or try/catch blocks. This guarantees that hooks execute in the exact same order on every render.
2.  **Only Call Hooks from React Functions:** Only call hooks inside React functional components or custom hooks, not regular JS functions.
3.  **Custom Hook Naming Convention:** Custom hooks must always start with the prefix `use` (e.g., `useFetch`).

**অনুবাদ (Bangla Translation):**
1.  **সর্বদা টপ-লেভেলে হুক কল করা:** কখনোই কোনো লুপ, কন্ডিশন (`if`), নেস্টেড ফাংশন বা `try/catch`-এর ভেতরে হুক কল করা যাবে না। এতে প্রতি রেন্ডারে হুক কলের নির্দিষ্ট ক্রম বজায় থাকে।
2.  **কেবলমাত্র React ফাংশন থেকে কল করা:** হুক কেবল রিয়্যাক্ট ফাংশনাল কম্পোনেন্ট অথবা কাস্টম হুকের ভেতর থেকেই কল করা যাবে।
3.  **কাস্টম হুকের নামকরণ:** কাস্টম হুকের নাম অবশ্যই `use` দিয়ে শুরু হতে হবে (যেমন- `useFetch`)।

---

### **Q11: What is the difference between `useEffect` and `useLayoutEffect` in React? / React-এ `useEffect` এবং `useLayoutEffect` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`useEffect` (Asynchronous):** Runs **after** the browser has painted the DOM updates onto the screen. It does not block page rendering (ideal for data fetching, subscriptions, timers).
*   **`useLayoutEffect` (Synchronous):** Runs **synchronously after** DOM mutations but **before** the browser paints the pixels on screen. It blocks visual paint until execution completes (ideal for measuring element layouts or adjusting scroll positions to prevent visual flickering).

**অনুবাদ (Bangla Translation):**
*   **`useEffect` (অ্যাসিনক্রোনাস):** ব্রাউজার ডম পরিবর্তন করে স্ক্রিনে পিক্সেল আঁকার (Paint) **পরে** রান করে। এটি পেজ রেন্ডার হতে বাধা দেয় না (এপিআই কল বা টাইমারের জন্য সেরা)।
*   **`useLayoutEffect` (সিনক্রোনাস):** ডম পরিবর্তনের পরপরই কিন্তু ব্রাউজার স্ক্রিনে ছবি আঁকার **পূর্বে** রান করে। এটি স্ক্রিনে পিক্সেল ফুটিয়ে তোলার কাজ থামিয়ে রাখে (ডম এলিমেন্টের সাইজ মাপা বা স্ক্রলিং পজিশন ঠিক করে ফ্লিকারিং বা কাপুনি এড়াতে ব্যবহৃত হয়)।

---

### **Q12: What is the purpose of callback function argument format of `setState()` in React and when should it be used? / React-এ `setState()` এর কলব্যাক ফাংশন আর্গুমেন্ট ফরম্যাটের উদ্দেশ্য কী এবং এটি কখন ব্যবহার করা উচিত?**

**Answer (English):**
React batches state updates asynchronously for performance optimizations.
*   **Purpose:** Passing a updater function `setCount(prevCount => prevCount + 1)` ensures that the update is calculated based on the **most recent pending state**, rather than a stale closure snapshot.
*   **When to use:** Whenever the new state value relies directly on the previous state value, or when multiple state updates occur rapidly within the same handler event loop.

**অনুবাদ (Bangla Translation):**
পারফরম্যান্স অপ্টিমাইজেশনের জন্য রিয়্যাক্ট অ্যাসিনক্রোনাসলি স্টেট আপডেট ব্যাচ করে।
*   **উদ্দেশ্য:** `setCount(prevCount => prevCount + 1)` কলব্যাক ফরম্যাট ব্যবহার করলে নিশ্চিত হওয়া যায় যে নতুন মানটি আগের **একদম সর্বশেষ আপডেটেড মান** থেকেই হিসাব হচ্ছে।
*   **কখন ব্যবহার করবেন:** যখন নতুন স্টেটের মান সরাসরি আগের স্টেটের মানের ওপর নির্ভর করে, অথবা একটি ইভেন্টে পরপর একাধিকবার স্টেট আপডেট করার প্রয়োজন হয়।

---

### **Q13: What does the dependency array of `useEffect` affect? / `useEffect`-এর ডিপেনডেন্সি অ্যারে কী কী বিষয়কে প্রভাবিত করে?**

**Answer (English):**
The dependency array controls the **execution lifecycle** of the effect callback:
1.  **`[]` (Empty Array):** Effect executes **once** after the initial component mount.
2.  **`[a, b]` (With Values):** Effect executes after initial mount AND re-executes whenever any dependency value (`a` or `b`) changes between renders.
3.  **Omitted (No Array):** Effect executes after **every single render** of the component, which can lead to infinite loops if state is updated inside.

**অনুবাদ (Bangla Translation):**
ডিপেনডেন্সি অ্যারে `useEffect`-এর **রান হওয়ার সময়কাল** নির্ধারণ করে:
1.  **`[]` (ফাঁকা অ্যারে):** পেজ প্রথমবার মাউন্ট (Mount) হওয়ার পর কেবল **একবারই** ফাংশনটি রান করবে।
2.  **`[a, b]` (ভ্যালু সহ):** প্রথমবার মাউন্টের পর যখনই অ্যারের ভেতরের কোনো ভ্যালুর চেঞ্জ হবে, তখনই ইফেক্টটি আবার রান করবে।
3.  **অ্যারে না দিলে (Omitted):** কম্পোনেন্ট প্রতিবার রেন্ডার হওয়ার পর **অনবরত** রান করতে থাকবে (যা মেমোরি লিক ও ইনফিনিট লুপ বানাতে পারে)।

---

### **Q14: What is the `useRef` hook in React and when should it be used? / React-এ `useRef` হুক কী এবং এটি কখন ব্যবহার করা উচিত?**

**Answer (English):**
`useRef` returns a mutable ref object `{ current: initialValue }` that persists across component re-renders.
*   **Key Behavior:** Mutating the `.current` property does **NOT** trigger a component re-render.
*   **When to use:**
    1.  Directly accessing or manipulating DOM elements (focusing inputs, measuring size, scrolling).
    2.  Storing mutable values that don't affect UI rendering (timer IDs, WebSocket instances, previous state snapshots).

**অনুবাদ (Bangla Translation):**
`useRef` একটি অপরিবর্তনশীল রেফারেন্স অবজেক্ট `{ current: initialValue }` দেয় যা রেন্ডারের মাঝেও মান ধরে রাখে।
*   **মূল বৈশিষ্ট্য:** `.current` প্রপার্টি পরিবর্তন করলেও কম্পোনেন্ট **রি-রেন্ডার হয় না**।
*   **কখন ব্যবহার করবেন:**
    1.  সরাসরি DOM এলিমেন্ট অ্যাক্সেস করতে (ইনপুট ফোকাস, স্ক্রলিং, সাইজ মাপা)।
    2.  এমন কোনো মান সেভ রাখতে যা পাল্টালেও স্ক্রিনের ইউআই রেন্ডারে প্রভাব ফেলে না (যেমন টাইমার ID, সকেট কানেকশন)।

---

### **Q15: What is the `useCallback` hook in React and when should it be used? / React-এ `useCallback` হুক কী এবং এটি কখন ব্যবহার করা উচিত?**

**Answer (English):**
`useCallback` is a performance optimization hook that memoizes a **function instance** across re-renders until its dependencies change.
*   **Why it's needed:** In JS, functions are recreated on every render. If passed as a prop to a memoized child component (`React.memo`), it triggers unnecessary child re-renders. `useCallback` keeps the function reference stable.
*   **When to use:** When passing callbacks to optimized child components or when a function is inside a `useEffect` dependency array.

**অনুবাদ (Bangla Translation):**
`useCallback` হলো একটি পারফরম্যান্স অপ্টিমাইজেশন হুক যা ডিপেনডেন্সি পরিবর্তন না হওয়া পর্যন্ত একটি **ফাংশন রেফারেন্সকে মেমোরাইজ** (ক্যাশে) করে রাখে।
*   **কেন প্রয়োজন:** প্রতি রেন্ডারে নতুন ফাংশন তৈরি হয়। প্রপস হিসেবে চাইল্ড কম্পোনেন্টে পাঠালে `React.memo` থাকা সত্ত্বেও চাইল্ড রি-রেন্ডার হয়। `useCallback` রেফারেন্স স্থির রাখে।
*   **কখন ব্যবহার করবেন:** মেমোরাইজড চাইল্ড কম্পোনেন্টে কলব্যাক পাঠানোর সময় অথবা ফাংশনটি কোনো `useEffect`-এর ডিপেনডেন্সি হলে।

---

### **Q16: What is the `useMemo` hook in React and when should it be used? / React-এ `useMemo` হুক কী এবং এটি কখন ব্যবহার করা উচিত?**

**Answer (English):**
`useMemo` is a performance optimization hook that memoizes the **result of a calculation** between re-renders.
*   **How it works:** It executes the calculation function only when one of its dependencies changes; otherwise, it returns the cached result.
*   **When to use:**
    1.  Avoiding expensive, computationally heavy calculations (e.g., sorting massive arrays, complex data filtering).
    2.  Stabilizing object/array reference values passed as props to memoized child components.

**অনুবাদ (Bangla Translation):**
`useMemo` হলো একটি পারফরম্যান্স অপ্টিমাইজেশন হুক যা কোনো **জটিল হিসাবের ফলাফলকে মেমোরাইজ (ক্যাশে)** করে রাখে।
*   **কীভাবে কাজ করে:** ডিপেনডেন্সি পরিবর্তিত হলেই কেবল এটি হিসাবটি পুনরায় করে, নতুবা আগের ক্যাশ করা ফলাফল সরাসরি ফেরত দেয়।
*   **কখন ব্যবহার করবেন:**
    1.  ভারী বা জটিল গাণিতিক হিসাব (যেমন- হাজার হাজার ডেটা ফিল্টারিং বা সর্টিং) এড়াতে।
    2.  চাইল্ড কম্পোনেন্টে পাঠানো অবজেক্ট বা অ্যারে প্রপসের রেফারেন্স স্থির রাখতে।

---

### **Q17: What is the `useReducer` hook in React and when should it be used? / React-এ `useReducer` হুক কী এবং এটি কখন ব্যবহার করা উচিত?**

**Answer (English):**
`useReducer` is an alternative to `useState` for managing complex state logic using a **reducer function** `(state, action) => newState`.
*   **When to use:**
    1.  When state logic involves multiple sub-values or complex conditional branches.
    2.  When the next state depends heavily on the previous state.
    3.  When managing complex form states or state transitions across sibling components paired with Context.

**অনুবাদ (Bangla Translation):**
`useReducer` হলো জটিল স্টেট লজিক সমাধানের জন্য `useState`-এর বিকল্প হুক, যা একটি **রিডিউসার ফাংশন** `(state, action) => newState` এর মাধ্যমে কাজ করে।
*   **কখন ব্যবহার করবেন:**
    1.  যখন স্টেট অবজেক্টের ভেতর একাধিক শাখা বা জটিল কন্ডিশনাল লজিক থাকে।
    2.  যখন পরবর্তী স্টেট আগের স্টেটের ওপর গভীরভাবে নির্ভরশীল হয়।
    3.  জটিল ফর্ম স্টেট বা বড় অ্যাপ্লিকেশনের স্টেট ডাইনামিকালি পরিচালনা করতে।

---

### **Q18: What is the `useId` hook in React and when should it be used? / React-এ `useId` হুক কী এবং এটি কখন ব্যবহার করা উচিত?**

**Answer (English):**
`useId` is a hook introduced in React 18 for generating unique, stable IDs that are consistent across both Server-Side Rendering (SSR) and client hydration.
*   **When to use:** Generating HTML element IDs for form accessibility attributes (e.g., linking `<label htmlFor={id}>` with `<input id={id}>`) to avoid hydration mismatch errors.
*   *Note:* Do NOT use `useId` to generate keys in list mapping.

**অনুবাদ (Bangla Translation):**
`useId` হলো React 18-এ আসা একটি হুক যা সার্ভার-সাইড রেন্ডারিং (SSR) এবং ক্লায়েন্ট ক্লায়েন্ট সাইড হাইড্রেশনের মাঝে ইউনিক ও স্থায়ী (Stable) আইডি তৈরি করে।
*   **কখন ব্যবহার করবেন:** অ্যাক্সেসিবিলিটির জন্য ফর্মের ইনপুট ও লেবেল কানেক্ট করতে (`<label htmlFor={id}>` ও `<input id={id}>`), যাতে সার্ভার ও ব্রাউজারের আইডিতে কোনো অমিল না হয়।
*   *নোট:* লিস্টের `key` প্রপস তৈরির জন্য `useId` ব্যবহার করা উচিত নয়।

---

### **Q19: What does re-rendering mean in React? / React-এ Re-rendering বলতে কী বোঝায়?**

**Answer (English):**
Re-rendering is the process where React executes a component function again to compute a new Virtual DOM tree based on updated state, props, or context.
*   **The Re-render Flow:**
    1.  State/Props/Context changes.
    2.  Component function executes -> returns new JSX / Virtual DOM.
    3.  React diffs the new Virtual DOM with the old one (Reconciliation).
    4.  React commits only the specific changed nodes to the real browser DOM.

**অনুবাদ (Bangla Translation):**
Re-rendering হলো এমন এক প্রসেস যেখানে স্টেট, প্রপস বা কনটেক্সট পরিবর্তনের পর রিয়্যাক্ট নতুন ভার্চুয়াল ডম হিসাব করার জন্য কম্পোনেন্ট ফাংশনটিকে পুনরায় রান করায়।
*   **প্রসেসের ধাপ:**
    1.  স্টেট/প্রপস পরিবর্তন ঘটে।
    2.  ফাংশন রি-রান করে নতুন JSX ডম পাঠায়।
    3.  রিঅ্যাক্ট আগের ভার্চুয়াল ডমের সাথে নতুনটির তুলনা (Diffing) করে।
    4.  কেবলমাত্র পরিবর্তন হওয়া অংশটুকু মূল ব্রাউজার ডমে আপডেট করে।

---

### **Q20: What are React Fragments used for? / React Fragments কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
React Fragments (`<React.Fragment>` or shorthand `<>...</>`) allow grouping multiple JSX elements without adding extra wrapper nodes (like unnecessary `<div>`s) to the real DOM.
*   **Benefits:** Keeps the HTML DOM tree clean, avoids breaking CSS flexbox/grid layouts, and improves performance slightly by creating fewer DOM elements.

**অনুবাদ (Bangla Translation):**
React Fragments (`<React.Fragment>` বা সংক্ষেপে `<>...</>`) মূল ব্রাউজার ডমে অহেতুক বাড়তি কোনো ডিভ (`<div>`) নোড যোগ করা ছাড়াই একাধিক JSX এলিমেন্টকে একসাথে গ্রুপ করে রিটার্ন করতে সাহায্য করে।
*   **সুবিধা:** ডম ফ্রি পরিষ্কার রাখে, সিএসএস ফ্লেক্সবক্স বা গ্রিড লেআউট ভাঙতে দেয় না এবং অতিরিক্ত ডম এলিমেন্ট তৈরি না করে পারফরম্যান্স ঠিক রাখে।

---

### **Q21: What is `forwardRef()` in React used for? / React-এ `forwardRef()` কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
`forwardRef()` is an API that allows a component to pass (forward) a received `ref` down to one of its child DOM elements or child components.
*   **Use Case:** When a parent component needs direct access to a DOM node inside a custom child component (e.g., focusing a custom input field `<MyInput ref={inputRef} />`).

**অনুবাদ (Bangla Translation):**
`forwardRef()` হলো রিয়্যাক্টের একটি এপিআই যা কোনো কম্পোনেন্টকে তার কাছে আসা `ref`-কে নিচের কোনো চাইল্ড ডম এলিমেন্টের কাছে পাস (Forward) করার সুবিধা দেয়।
*   **ব্যবহার:** যখন কোনো প্যারেন্ট কম্পোনেন্টকে সরাসরি চাইল্ডের ভেতরের কাস্টম ডম নোড স্পর্শ করতে হয় (যেমন- কাস্টম ইনপুট কম্পোনেন্ট ফোকাস করা)।

---

### **Q22: How do you reset a component’s state in React? / React-এ কীভাবে কোনো কম্পোনেন্টের স্টেট রিসেট (Reset) করবেন?**

**Answer (English):**
1.  **Manual Reset:** Calling the state setter function with the initial values (`setForm(initialState)`).
2.  **Key-based Reset (Idiomatic Way):** Pass a different `key` prop to the component (`<MyComponent key={resetId} />`). When the `key` changes, React completely unmounts the old component instance and mounts a fresh one with initial state.

**অনুবাদ (Bangla Translation):**
1.  **ম্যানুয়াল রিসেট:** সেটার ফাংশন দিয়ে পুনরায় প্রাথমিক মান বসানো (`setForm(initialState)`)।
2.  **Key পরিবর্তন করে রিসেট (সেরা উপায়):** কম্পোনেন্টে একটি আলাদা `key` প্রপস দেওয়া (`<MyComponent key={resetId} />`)। `key` পরিবর্তন করা মাত্রই রিয়্যাক্ট আগের কম্পোনেন্ট আনমাউন্ট করে একদম নতুন ইনিশিয়াল স্টেট সহ কম্পোনেন্ট বসায়।

---

### **Q23: Why does React recommend against mutating state? / React কেন সরাসরি State Mutate (পরিবর্তন) না করার পরামর্শ দেয়?**

**Answer (English):**
React relies on **shallow reference equality checks** (`Object.is`) to determine if state has changed.
*   **Why Mutation Fails:** If you mutate an object/array directly (e.g., `state.user.name = 'New'`), the memory reference remains unchanged. React assumes no state change occurred and skips re-rendering, causing UI stale bugs and unpredictable state behavior.
*   *Solution:* Always create a new object/array copy when updating state (e.g., `{ ...state, name: 'New' }`).

**অনুবাদ (Bangla Translation):**
স্টেট পরিবর্তিত হয়েছে কিনা তা বুঝতে রিয়্যাক্ট অবজেক্টের **মেমোরি রেফারেন্স (Shallow Comparison)** চেক করে।
*   **সরাসরি পরিবর্তন করলে কী হয়:** অবজেক্ট বা অ্যারে সরাসরি মিউটেট করলে (যেমন- `state.push(1)`) মেমোরির এড্রেস একই থেকে যায়। ফলে রিয়্যাক্ট মনে করে কোনো পরিবর্তন হয়নি এবং রেন্ডারিং স্কিপ করে বাগ তৈরি করে।
*   *সমাধান:* সবসময় নতুন কপি বানিয়ে অবজেক্ট বা অ্যারে আপডেট করা উচিত।

---

### **Q24: What are error boundaries in React for? / React-এ Error Boundaries কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
Error Boundaries are class components that catch JavaScript runtime errors anywhere in their child component tree during rendering, lifecycle methods, and constructors.
*   **Behavior:** Instead of crashing the entire React app with a blank white screen, they log the error and display a fallback UI gracefully.
*   *Note:* They do NOT catch errors inside event handlers, async code (`setTimeout`), or Server-Side Rendering.

**অনুবাদ (Bangla Translation):**
Error Boundaries হলো বিশেষ ক্লাস কম্পোনেন্ট যা তাদের নিচের চাইল্ড কম্পোনেন্ট ট্রির যেকোনো জায়গার রেন্ডারিং এরর ধরে ফেলে এবং পুরো ওয়েবসাইট ক্র্যাশ করা থেকে রক্ষা করে।
*   **আচরণ:** এরর হলে সাদা ফাঁকা স্ক্রিন দেখানোর বদলে এটি ইউজারকে একটি সুন্দর ব্যাকআপ বা ফলব্যাক ইউআই দেখায়।
*   *নোট:* ইভেন্ট হ্যান্ডলার বা অ্যাসিনক্রোনাস কোডের এরর এরা ধরতে পারে না।

---

### **Q25: How do you test React applications? / React অ্যাপ্লিকেশন কীভাবে টেস্ট করবেন?**

**Answer (English):**
React apps are tested using a combination of test runners and testing libraries:
1.  **Unit & Integration Testing:** Using **Jest** (test runner/assertion) and **React Testing Library (RTL)** to simulate user interactions and verify rendered DOM output from the user's perspective.
2.  **End-to-End (E2E) Testing:** Using **Cypress** or **Playwright** to test complete user workflows in real browsers.

**অনুবাদ (Bangla Translation):**
রিঅ্যাক্ট অ্যাপ মূলত ২ ধরনের টুল দিয়ে টেস্ট করা হয়:
1.  **Unit & Integration Testing:** **Jest** (টেস্ট রানার) এবং **React Testing Library (RTL)** ব্যবহার করে ইউজারের দৃষ্টিকোণ থেকে বাটন ক্লিক বা ইনপুট সিমুলেট করে টেস্ট করা হয়।
2.  **End-to-End (E2E) Testing:** **Cypress** বা **Playwright** দিয়ে বাস্তব ব্রাউজারে সম্পূর্ণ ইউজার ফ্লো টেস্ট করা হয়।

---

### **Q26: Explain what React hydration is. / React Hydration কী তা ব্যাখ্যা করুন।**

**Answer (English):**
Hydration is the process in Server-Side Rendering (SSR) where React attaches event listeners and state management to the static HTML markup sent by the server, turning it into a fully interactive client-side application.
*   **Flow:** Server sends static HTML -> Browser paints HTML quickly -> React bundle loads -> React "hydrates" the static HTML by wiring up event handlers.

**অনুবাদ (Bangla Translation):**
হাইড্রেশন (Hydration) হলো সার্ভার-সাইড রেন্ডারিং (SSR)-এর একটি প্রক্রিয়া, যেখানে সার্ভার থেকে আসা স্ট্যাটিক HTML কোডের ওপর জাভাস্ক্রিপ্ট ইভেন্ট লিসেনার ও স্টেট যুক্ত করে তাকে সম্পূর্ণ ডাইনামিক ও ইন্টারঅ্যাক্টিভ করা হয়।
*   **ধাপ:** সার্ভার HTML পাঠায় -> ব্রাউজার টেক্সট দেখায় -> রিয়্যাক্ট ফাইল লোড হয় -> রিয়্যাক্ট স্ট্যাটিক HTML-এর ওপর ইভেন্ট বসিয়ে পেজকে সচল (Hydrate) করে।

---

### **Q27: What are React Portals used for? / React Portals কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
React Portals (`ReactDOM.createPortal(child, container)`) allow rendering a component's JSX into a DOM node that exists **outside** the parent component's DOM hierarchy.
*   **Use Cases:** UI overlays like Modals, Tooltips, Dropdowns, or Dialogs that need to break out of parent container styles (`overflow: hidden` or `z-index` stacking context).

**অনুবাদ (Bangla Translation):**
React Portals (`ReactDOM.createPortal(child, container)`) কোনো কম্পোনেন্টকে তার প্যারেন্ট ডম কাঠামোর **বাইরে** অন্য যেকোনো ডম নোডে রেন্ডার করার সুবিধা দেয়।
*   **ব্যবহার:** মডাল (Modal), টুলটিপ (Tooltip) বা ড্রপডাউন তৈরি করতে, যা প্যারেন্টের সিএসএস বা `overflow: hidden` সীমানা ভেঙে স্ক্রিনের ওপর ভেসে ওঠে।

---

### **Q28: How do you debug React applications? / React অ্যাপ্লিকেশন কীভাবে ডিবাগ করবেন?**

**Answer (English):**
1.  **React Developer Tools:** Browser extension to inspect component hierarchy, view/edit state and props in real-time, and trace re-renders.
2.  **Console Logging & `debugger`:** `console.log()` or browser breakpoints.
3.  **Strict Mode:** Highlights side effects and deprecated APIs during development.
4.  **Error Boundaries:** Catches runtime UI errors with detailed stack traces.

**অনুবাদ (Bangla Translation):**
1.  **React Developer Tools:** ব্রাউজার এক্সটেনশন দিয়ে কম্পোনেন্ট ট্রি, স্টেট ও প্রপস রিয়েল-টাইমে অডিট করা।
2.  **কনসোল লগ ও ব্রেকপয়েন্ট:** `console.log()` বা ব্রাউজার `debugger` ব্রেকপয়েন্ট ব্যবহার করা।
3.  **Strict Mode:** ডেভেলপমেন্টে এরর ও সাইড এফেক্ট শনাক্ত করা।

---

### **Q29: What is React Strict Mode and what are its benefits? / React Strict Mode কী এবং এর সুবিধাসমূহ কী কী?**

**Answer (English):**
`<React.StrictMode>` is a development-only helper tool that wraps components to highlight potential problems in an application without rendering visible UI.
*   **Benefits:**
    1.  Detects unsafe lifecycle methods and deprecated APIs.
    2.  Intentional **double-invokes** component renders and effects in development to catch unexpected side-effects and impure code.

**অনুবাদ (Bangla Translation):**
`<React.StrictMode>` হলো একটি ডেভেলপমেন্ট-অনলি টুল যা কোনো ভিজ্যুয়াল ইউআই না বানিয়ে কোডের সম্ভাব্য ভুলত্রুটি খুঁজে বের করে।
*   **সুবিধাসমূহ:**
    1.  পুরাতন বা ক্ষতিকর এপিআই এবং আনসেফ লাইফসাইকেল ধরিয়ে দেয়।
    2.  সাইড-এফেক্ট বা ক্ষতিকর কোড শনাক্ত করতে ডেভেলপমেন্ট মোডে কম্পোনেন্টকে **দুইবার করে রেন্ডার ও রান** করায়।

---

### **Q30: How do you localize React applications? / React অ্যাপ্লিকেশন কীভাবে লোকালাইজ (Localization / i18n) করবেন?**

**Answer (English):**
Localization (i18n) adapts an app for different languages and formats.
*   **Implementation:** Using popular libraries like `react-i18next` or `react-intl`. Translation strings are stored in JSON files per language. A provider wraps the app, and the `useTranslation()` hook injects localized text dynamically based on the current user locale.

**অনুবাদ (Bangla Translation):**
লোকালাইজেশন (i18n) হলো অ্যাপকে বিভিন্ন দেশের ভাষা ও ফরম্যাটে ব্যবহারযোগ্য করা।
*   **বাস্তবায়ন:** `react-i18next` লাইব্রেরি ব্যবহার করে। ভাষার ডেটা JSON ফাইলে থাকে। `useTranslation()` হুকের মাধ্যমে ইউজারের ভাষা অনুযায়ী স্ক্রিনের লেখা স্বয়ংক্রিয়ভাবে বদলে যায়।

---

### **Q31: What is code splitting in a React application? / React অ্যাপ্লিকেশনে Code Splitting কী?**

**Answer (English):**
Code splitting is a performance optimization technique that breaks down a large JavaScript bundle into smaller chunks loaded on-demand.
*   **Implementation:** Using `React.lazy()` for dynamic imports and wrapping components with `<React.Suspense fallback={<Loader />}>`. Route-based code splitting ensures users only download code for the current page.

**অনুবাদ (Bangla Translation):**
কোড স্প্লিটিং (Code Splitting) হলো একটি পারফরম্যান্স অপ্টিমাইজেশন টেকনিক যার মাধ্যমে বিশাল বড় জাভাস্ক্রিপ্ট বান্ডেলকে ছোট ছোট খণ্ডে ভাগ করে প্রয়োজন অনুযায়ী (On-demand) লোড করা হয়।
*   **বাস্তবায়ন:** `React.lazy()` এবং `<React.Suspense>` ব্যবহার করে রাউট অনুযায়ী কোড ভাগ করা হয়, যাতে ইউজার কেবল বর্তমান পেজের কোডটুকুই ডাউনলোড করে।

---

### **Q32: How would one optimize the performance of React contexts to reduce rerenders? / Re-render কমাতে React Context এর পারফরম্যান্স কীভাবে অপ্টিমাইজ করবেন?**

**Answer (English):**
1.  **Split Contexts:** Separate state logically into multiple smaller providers instead of one giant state context.
2.  **Memoize Provider Values:** Wrap context value objects with `useMemo` so child consumers don't re-render on unrelated parent updates.
3.  **Context Selectors:** Use libraries like `use-context-selector` to allow components to subscribe to specific fields only.

**অনুবাদ (Bangla Translation):**
1.  **কনটেক্সট ভাগ করা:** একটি বড় কনটেক্সটের বদলে ছোট ছোট লজিক্যাল প্রোভাইডারে ভাগ করা।
2.  **ভ্যালু মেমোরাইজ করা:** প্রোভাইডার ভ্যালুকে `useMemo` দিয়ে আটকে রাখা।
3.  **Selectors ব্যবহার:** `use-context-selector` ব্যবহার করে নির্দিষ্ট ডাটা ফিল্ড সাবস্ক্রাইব করা।

---

### **Q33: What are higher order components (HOCs) in React? / React-এ Higher Order Components (HOCs) কী?**

**Answer (English):**
A Higher-Order Component (HOC) is a pure function that takes a component as an argument and returns a new, enhanced component with additional props or behavior (`const EnhancedComponent = withAuth(BaseComponent)`).
*   **Purpose:** Reusing component logic (e.g., authentication wrappers, logging, layout wrapping).

**অনুবাদ (Bangla Translation):**
Higher-Order Component (HOC) হলো একটি হায়ার-অর্ডার ফাংশন যা একটি রিয়্যাক্ট কম্পোনেন্টকে ইনপুট নিয়ে একটি নতুন ও শক্তিশালী কম্পোনেন্ট আউটপুট দেয় (`const EnhancedComponent = withAuth(BaseComponent)`)।
*   **উদ্দেশ্য:** একাধিক কম্পোনেন্টের কমন লজিক (যেমন- লগইন চেক বা লেআউট) এক জায়গায় রি-ইউজ করা।

---

### **Q34: What is the Flux pattern and what are its benefits? / Flux pattern কী এবং এর সুবিধাসমূহ কী কী?**

**Answer (English):**
Flux is an architectural pattern created by Facebook for state management using **unidirectional data flow**.
*   **Components:** `Action` -> `Dispatcher` -> `Store` -> `View (Component)`.
*   **Benefits:** Predictable state transitions, easier debugging, and clear separation of data layer from UI logic (the foundation for Redux).

**অনুবাদ (Bangla Translation):**
Flux হলো ফেসবুকের তৈরি **একমুখী ডাটা প্রবাহ (Unidirectional Data Flow)** ভিত্তিক স্টেট ম্যানেজমেন্ট আর্কিটেকচার।
*   **অংশসমূহ:** `Action` -> `Dispatcher` -> `Store` -> `View`.
*   **সুবিধা:** স্টেট পরিবর্তন অনুমানযোগ্য হয় এবং ডিবাগিং সহজ হয় (Redux এর ভিত্তি)।

---

### **Q35: Explain one-way data flow of React and its benefits. / React-এর একমুখী ডেটা প্রবাহ (One-way data flow) এবং এর সুবিধাসমূহ ব্যাখ্যা করুন।**

**Answer (English):**
One-way data flow means data moves in a single direction from parent components down to child components via props. Children cannot mutate parent data directly; they trigger state changes by calling callback functions passed as props.
*   **Benefits:** Makes state predictable, simplifies data tracking, and reduces side-effect bugs.

**অনুবাদ (Bangla Translation):**
একমুখী ডেটা প্রবাহ হলো প্যারেন্ট কম্পোনেন্ট থেকে চাইল্ড কম্পোনেন্টের দিকে প্রপসের মাধ্যমে ডেটা নামার নিয়ম। চাইল্ড সরাসরি প্যারেন্টের ডেটা বদলাতে পারে না; প্রপস হিসেবে আসা কলব্যাক দিয়ে অনুরোধ পাঠায়।
*   **সুবিধা:** ডেটা ট্র্যাকিং সহজ হয় এবং স্টেট পরিবর্তন পরিষ্কার থাকে।

---

### **Q36: How do you handle asynchronous data loading in React applications? / React অ্যাপ্লিকেশনে অ্যাসিনক্রোনাস ডেটা লোডিং কীভাবে হ্যান্ডেল করবেন?**

**Answer (English):**
1.  **Traditional Way:** Trigger async API fetch inside `useEffect` on mount, managing `data`, `loading`, and `error` states using `useState`.
2.  **Modern Way:** Use data fetching libraries like **TanStack Query (React Query)** or **SWR**, which handle caching, auto-refetching, loading states, and error retries out-of-the-box.

**অনুবাদ (Bangla Translation):**
1.  **সনাতন উপায়:** `useEffect`-এর ভেতরে এপিআই কল করা এবং `useState` দিয়ে `data`, `loading` ও `error` স্টেট সামলানো।
2.  **আধুনিক উপায়:** **TanStack Query (React Query)** বা **SWR** ব্যবহার করা, যা স্বয়ংক্রিয়ভাবে ক্যাশিং, রি-ট্রাই এবং লোডিং স্টেট সামলায়।

---

### **Q37: Explain server-side rendering (SSR) of React applications and its benefits. / React অ্যাপ্লিকেশনের Server-Side Rendering (SSR) এবং এর সুবিধা ব্যাখ্যা করুন।**

**Answer (English):**
SSR is a rendering method where the server generates the full HTML markup of a React page for every request and sends it to the browser, which is then hydrated on the client.
*   **Benefits:** Excellent SEO, faster First Contentful Paint (FCP), and better performance on low-power mobile devices. Frameworks like Next.js support SSR via `getServerSideProps` or Server Components.

**অনুবাদ (Bangla Translation):**
SSR হলো এমন রেন্ডারিং পদ্ধতি যেখানে সার্ভার প্রতি রিকোয়েস্টে সম্পূর্ণ HTML রেন্ডার করে ব্রাউজারে পাঠায়, যা পরে ব্রাউজারে হাইড্রেট (Hydrate) হয়।
*   **সুবিধা:** অসাধারণ এসইও (SEO), দ্রুত প্রাথমিক লোড টাইম এবং কম ক্ষমতার মোবাইলে চমৎকার পারফরম্যান্স (যেমন- Next.js)।

---

### **Q38: Explain static generation of React applications and its benefits. / React অ্যাপ্লিকেশনের Static Generation (SSG) এবং এর সুবিধা ব্যাখ্যা করুন।**

**Answer (English):**
Static Site Generation (SSG) pre-renders pages into static HTML files **at build time**.
*   **Benefits:** Blazing fast performance (served directly from global CDNs), ultra-low server costs, and optimal SEO. Ideal for blogs, marketing pages, and documentation sites where content changes infrequently.

**অনুবাদ (Bangla Translation):**
Static Site Generation (SSG) হলো প্রজেক্ট **বিল্ড হওয়ার সময়েই** পেজগুলোকে স্ট্যাটিক HTML ফাইলে রেন্ডার করে রাখা।
*   **সুবিধা:** সুপারফাস্ট লোড স্পিড (সরাসরি CDN থেকে সার্ভ হয়), শূন্য সার্ভার চাপ ও সেরা এসইও। ব্লগ বা ডকুমেন্টেশন ওয়েবসাইটের জন্য বেস্ট।

---

### **Q39: Explain the presentational vs container component pattern in React. / React-এ Presentational বনাম Container কম্পোনেন্ট প্যাটার্ন ব্যাখ্যা করুন।**

**Answer (English):**
*   **Presentational Components (Dumb):** Concerned solely with how things look. Receive data and callbacks via props and rarely manage state (except UI state).
*   **Container Components (Smart):** Concerned with how things work. Handle data fetching, state management, and pass data down to presentational components.

**অনুবাদ (Bangla Translation):**
*   **Presentational Components:** এদের কাজ কেবল ডিজাইন বা ইউআই দেখানো। প্রপস থেকে ডেটা নিয়ে স্ক্রিনে রেন্ডার করে।
*   **Container Components:** এদের কাজ ডেটা লোড ও স্টেট ম্যানেজ করা। এরা লজিক হ্যান্ডেল করে প্রেজেন্টেশনাল কম্পোনেন্টে ডেটা পাঠায়।

---

### **Q40: What are some common pitfalls when doing data fetching in React? / React-এ ডেটা ফেচিংয়ের সময় সাধারণ কী কী সমস্যা বা ঝুঁকি (pitfalls) দেখা যায়?**

**Answer (English):**
1.  **Race Conditions:** Out-of-order responses overwriting latest state (fix via `AbortController`).
2.  **Memory Leaks:** Updating state on unmounted components.
3.  **Infinite Loops:** Forgetting dependency arrays in `useEffect`.
4.  **Missing Error/Loading States:** Poor UX when requests hang or fail.

**অনুবাদ (Bangla Translation):**
1.  **Race Conditions:** আগের স্লো রিকোয়েস্ট পরের নতুন রিকোয়েস্টের ওপর চেপে বসা (`AbortController` দিয়ে ক্যানসেল করতে হয়)।
2.  **মেমোরি লিক:** কম্পোনেন্ট আনমাউন্ট হয়ে যাওয়ার পর স্টেট আপডেট করা।
3.  **ইনফিনিট লুপ:** `useEffect`-এ ডিপেনডেন্সি অ্যারে দিতে ভুলে যাওয়া।
