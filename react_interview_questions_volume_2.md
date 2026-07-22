# React Interview Questions Guide: Volume 2 (Questions 41 - 75)

This guide contains detailed answers in English alongside complete Bangla translations for questions 41 to 75 from the uploaded React Interview Questions PDF.

---

### **Q41: What is the role of keys in React lists and why are they important? / React লিস্টে `key`-এর ভূমিকা কী এবং কেন এগুলো গুরুত্বপূর্ণ?**

**Answer (English):**
Keys provide a stable identity to list elements between renders.
*   **Role:** During the reconciliation phase, React uses `key` attributes to match previous Virtual DOM list items with new ones.
*   **Importance:** Prevents re-rendering unchanged list items, optimizes list updates, and ensures component local state (like input focus or checkbox states) is not incorrectly transferred between reordered items.

**অনুবাদ (Bangla Translation):**
`key` রেন্ডারিংয়ের মাঝে লিস্টের উপাদানগুলোকে একটি স্থায়ী পরিচিতি দেয়।
*   **ভূমিকা:** রিঅ্যাক্ট Reconciliation পর্ব চলাকালীন আগের ও নতুন লিস্টের উপাদানের মধ্যে মিল খুঁজে পেতে `key` ব্যবহার করে।
*   **গুরুত্ব:** অপরিবর্তিত আইটেম আবার রেন্ডার হতে দেয় না, ডম আপডেট অপ্টিমাইজ করে এবং লিস্টে উপাদান ওলটপালট হলেও চাইল্ডের লোকাল স্টেট অক্ষুণ্ণ রাখে।

---

### **Q42: What are fragments in React and why are they useful? / React-এ Fragments কী এবং কেন এগুলো দরকারী?**

**Answer (English):**
React Fragments (`<React.Fragment>` or `<>...</>`) are container elements that wrap multiple JSX children without introducing an actual HTML wrapper element into the browser DOM.
*   **Usefulness:** Keeps DOM trees clean, preserves CSS Grid/Flexbox layouts, avoids invalid HTML markup (e.g., inside `<table>` or `<ul>`), and slightly improves performance by creating fewer DOM nodes.

**অনুবাদ (Bangla Translation):**
React Fragments হলো এমন পাত্র যা ব্রাউজার ডমে কোনো অতিরিক্ত HTML ট্যাগ (যেমন `<div>`) যোগ না করেই একাধিক JSX উপাদানকে একত্রে রিটার্ন করতে দেয়।
*   **উপকারিতা:** HTML কাঠামো পরিষ্কার রাখে, সিএসএস গ্রিড/ফ্লেক্সবক্স ভাঙতে দেয় না এবং টেবিল বা লিস্টের ভেতরের অবৈধ এইচটিএমএল রোধ করে।

---

### **Q43: What are controlled and uncontrolled components in React? / Controlled এবং Uncontrolled কম্পোনেন্ট কী?**

**Answer (English):**
*   **Controlled Components:** Input form data is handled directly by **React State**. Input `value` prop is tied to state, and updates are driven by `onChange` listeners.
*   **Uncontrolled Components:** Input data is managed directly by the **browser DOM**. Values are accessed on demand using React `refs` (`useRef`).

**অনুবাদ (Bangla Translation):**
*   **Controlled Components:** ফর্মে ইনপুটের মান সরাসরি **React State** দিয়ে নিয়ন্ত্রিত হয়। ইনপুটের ভ্যালু স্টেটের সাথে যুক্ত থাকে এবং `onChange` দিয়ে আপডেট হয়।
*   **Uncontrolled Components:** ইনপুটের মান সরাসরি **DOM** নিজেই সামলায়। প্রয়োজন হলে রিয়্যাক্ট `ref` (`useRef`) দিয়ে মান গ্রহণ করা হয়।

---

### **Q44: Explain the use of the Context API in React. / React-এ Context API-এর ব্যবহার ব্যাখ্যা করুন।**

**Answer (English):**
The Context API provides a way to pass data through the component tree without manually passing props down through every intermediate level (prop drilling).
*   **Usage:** Ideal for global or broadly shared data like UI themes (light/dark), user authentication state, current language locale, or shopping cart states.
*   **Components:** `createContext()`, `Provider`, and `useContext()`.

**অনুবাদ (Bangla Translation):**
Context API প্রপস ড্রিলিং (Prop Drilling) ছাড়াই কম্পোনেন্ট ট্রির যেকোনো গভীরতায় সরাসরি ডেটা পাঠানোর পথ তৈরি করে।
*   **ব্যবহার:** গ্লোবাল থিম (Light/Dark), ইউজার লগইন স্টেট, ভাষা পছন্দ বা কার্ট স্টেটের জন্য সেরা।
*   **উপাদান:** `createContext()`, `Provider`, এবং `useContext()`।

---

### **Q45: What are React hooks and why were they introduced? / React Hooks কী এবং কেন এগুলো আনা হয়েছিল?**

**Answer (English):**
Hooks are special functions (introduced in React 16.8) that let functional components use state, lifecycle methods, and other React features.
*   **Why Introduced:**
    1.  Eliminated class component complexities (like `this` binding and verbose constructors).
    2.  Allowed sharing stateful logic cleanly across components via Custom Hooks.
    3.  Grouped related code (e.g., data fetching + subscription cleanup) in one place rather than splitting across lifecycle methods (`componentDidMount`/`componentWillUnmount`).

**অনুবাদ (Bangla Translation):**
হুকস (Hooks) হলো বিশেষ কিছু ফাংশন (React 16.8-এ যুক্ত) যা ক্লাস না লিখে সাধারণ ফাংশনাল কম্পোনেন্টেই স্টেট ও লাইফসাইকেল ব্যবহারের সুবিধা দেয়।
*   **আনার কারণ:**
    1.  ক্লাস কম্পোনেন্টের `this` বাইন্ডিং ও বয়লারপ্লেট কোডের জটিলতা দূর করা।
    2.  কাস্টম হুকের মাধ্যমে একাধিক কম্পোনেন্টে স্টেটফুল লজিক রি-ইউজ করা।
    3.  সম্পর্কিত লজিক এক জায়গায় সাজানো।

---

### **Q46: How does the virtual DOM in React work? What are its benefits and downsides? / React-এ Virtual DOM কীভাবে কাজ করে? এর সুবিধা ও অসুবিধা কী কী?**

**Answer (English):**
The Virtual DOM (VDOM) is a lightweight JavaScript representation of the real DOM.
*   **How it works:** When state changes, React creates a new VDOM tree, compares it with the previous VDOM tree (Diffing), calculates the minimal changes required, and updates only those specific parts in the real DOM (Reconciliation).
*   **Benefits:** High rendering speed, batching updates, declarative API.
*   **Downsides:** Consumes extra memory to keep VDOM trees in memory, slightly slower than raw handwritten JS for extremely simple static pages.

**অনুবাদ (Bangla Translation):**
ভার্চুয়াল ডম (VDOM) হলো ব্রাউজার ডমের একটি হালকা জাভাস্ক্রিপ্ট অনুলিপি।
*   **কীভাবে কাজ করে:** স্টেট বদলালে নতুন VDOM তৈরি হয়, আগেরটির সাথে তুলনা (Diffing) হয় এবং কেবল পরিবর্তিত অংশটুকু মূল ডমে আপডেট হয়।
*   **সুবিধা:** দ্রুত রেন্ডারিং স্পিড, ব্যাচ আপডেট এবং নিখুঁত ইউআই।
*   **অসুবিধা:** মেমোরিতে VDOM ফাইল রাখার কারণে অতিরিক্ত মেমোরি লাগে।

---

### **Q47: What is React Fiber and how is it an improvement over the previous approach? / React Fiber কী এবং এটি আগের পদ্ধতির চেয়ে কীভাবে উন্নত?**

**Answer (English):**
React Fiber is a complete rewrite of React's core reconciliation algorithm introduced in React 16.
*   **Previous Approach (Stack Reconciler):** Render work was synchronous and un-interruptible, which caused UI freezes during heavy rendering tasks.
*   **Fiber Improvements:**
    1.  **Incremental Rendering:** Breaks render work into small units (fibers) that can be paused, aborted, or resumed.
    2.  **Prioritization:** High-priority updates (user input, animations) execute first; low-priority tasks (offscreen lists) are deferred.
    3.  **Concurrency Support:** Enabled features like Concurrent Mode, Suspense, and Time Slicing.

**অনুবাদ (Bangla Translation):**
React Fiber হলো React 16-এ আনা রিঅ্যাক্ট কোর অ্যালগরিদমের সম্পূর্ণ নতুন সংস্করণ।
*   **আগের পদ্ধতি (Stack Reconciler):** রেন্ডারিং কাজ সিনক্রোনাস ছিল, যা মাঝপথে থামানো যেত না। ফলে বড় কাজ হলে স্ক্রিন হ্যাং হতো।
*   **Fiber-এর উন্নতি:**
    1.  **ইনক্রিমেন্টাল রেন্ডারিং:** কাজকে ছোট ছোট এককে ভাগ করে যা প্রয়োজনমতো পজ বা রি-স্টার্ট করা যায়।
    2.  **অগ্রাধিকার (Prioritization):** ইউজারের টাইপিং বা অ্যানিমেশনকে উচ্চ অগ্রাধিকার দিয়ে ব্যাকগ্রাউন্ড কাজ পরে করায়।
    3.  **কনকারেন্সি:** Suspense এবং Time Slicing চলাতে সাহায্য করে।

---

### **Q48: What is reconciliation in React? / React-এ Reconciliation কী?**

**Answer (English):**
Reconciliation is the process through which React updates the browser DOM. When state or props change, React constructs a new Virtual DOM tree and runs its heuristic **Diffing Algorithm** ($O(n)$ time complexity) against the old tree to calculate the minimal number of DOM operations needed.

**অনুবাদ (Bangla Translation):**
Reconciliation হলো সেই প্রসেস যার মাধ্যমে রিয়্যাক্ট ভার্চুয়াল ডমের পরিবর্তন হিসাব করে ব্রাউজার ডমকে আপডেট করে। স্টেট পাল্টালে নতুন VDOM তৈরি হয় এবং **Diffing Algorithm** দিয়ে পার্থক্য বের করে সর্বনিম্ন ডম অপারেশনে রেন্ডার সম্পন্ন করে।

---

### **Q49: What is React Suspense and what does it enable? / React Suspense কী এবং এটি কী সুবিধা দেয়?**

**Answer (English):**
React Suspense is a component wrapper that lets components "wait" for an asynchronous operation (code-splitting bundle load or data fetch) before rendering, displaying a fallback UI (like a spinner) in the meantime.
*   **Enables:** Declarative handling of loading states for `React.lazy()` component chunks and async data fetching streams.

**অনুবাদ (Bangla Translation):**
React Suspense হলো একটি কম্পোনেন্ট র্যাপার যা কোনো অ্যাসিনক্রোনাস কাজ (যেমন- কোড স্প্লিটিং ফাইল বা ডেটা ফেচিং) শেষ না হওয়া পর্যন্ত রেন্ডার থামিয়ে রেখে একটি সুন্দর ফলব্যাক ইউআই (যেমন স্পিনার) দেখায়।

---

### **Q50: Explain what happens when the `useState` setter function is called in React. / React-এ `useState` সেটার ফাংশন কল করলে কী ঘটে তা ব্যাখ্যা করুন।**

**Answer (English):**
1.  React queues the new state value.
2.  If the value is unchanged (`Object.is(oldState, newState)`), React bails out early and skips re-rendering.
3.  Otherwise, React schedules a re-render of the component and its children.
4.  State updates are **batched** together for performance, applying changes before the next browser paint.

**অনুবাদ (Bangla Translation):**
1.  রিঅ্যাক্ট নতুন স্টেট মানটি কিউতে (Queue) রাখে।
2.  যদি আগের ও নতুন মান হুবহু একই হয় (`Object.is`), তবে রি-রেন্ডারিং বাতিল করে দেয়।
3.  মান ভিন্ন হলে কম্পোনেন্টটিকে রি-রেন্ডার করার শিডিউল দেয়।
4.  একাধিক স্টেট আপডেট একসাথে ব্যাচ (Batch) করে প্রসেস করে।

---

### **Q51: What is the difference between `React.memo` and `useMemo`? When would you use each? / `React.memo` এবং `useMemo` এর মধ্যে পার্থক্য কী? কোনটি কখন ব্যবহার করবেন?**

**Answer (English):**
*   **`React.memo`:** A Higher-Order Component that memoizes an entire **Component**. Skips re-rendering the component if its props have not changed.
*   **`useMemo`:** A Hook used **inside** a component to memoize the **result of an expensive calculation** or object/array reference.

**অনুবাদ (Bangla Translation):**
*   **`React.memo`:** এটি একটি Higher-Order Component যা পুরো একটি **কম্পোনেন্টকে** মেমোরাইজ করে। প্রপস না পাল্টালে কম্পোনেন্ট রি-রেন্ডার হওয়া আটকায়।
*   **`useMemo`:** এটি কম্পোনেন্টের **ভেতরে** ব্যবহৃত হুক যা কোনো **জটিল হিসাবের ফলাফলকে** মেমোরাইজ করে রাখে।

---

### **Q52: How does React handle events differently from native DOM events? / React কীভাবে নেটিভ ডম ইভেন্টের চেয়ে আলাদাভাবে ইভেন্ট হ্যান্ডেল করে?**

**Answer (English):**
1.  **Synthetic Events:** React wraps native browser events in a cross-browser `SyntheticEvent` wrapper for consistent behavior.
2.  **Event Delegation:** React attaches a single event listener at the root container (e.g., `#root`) rather than attaching listeners to individual DOM nodes.
3.  **Naming & Syntax:** Uses camelCase (`onClick`) instead of lowercase (`onclick`), and passes functions rather than strings.

**অনুবাদ (Bangla Translation):**
1.  **Synthetic Events:** সব ব্রাউজারে একইরকম আচরণের জন্য রিয়্যাক্ট নেটিভ ইভেন্টকে `SyntheticEvent` দিয়ে র্যাপ করে।
2.  **ইভেন্ট ডেলিগেশন:** প্রতিটি নোডে আলাদা ইভেন্ট না বসিয়ে রিয়্যাক্ট মূল রুট এলিমেন্টে (`#root`) একটিমাত্র ইভেন্ট লিসেনার বসায়।
3.  **সিনট্যাক্স:** `onclick`-এর বদলে camelCase `onClick` ব্যবহার করা হয়।

---

### **Q53: Explain React reconciliation in detail. How does React decide which components to update? / React reconciliation বিস্তারিত ব্যাখ্যা করুন। রিয়্যাক্ট কীভাবে সিদ্ধান্ত নেয় কোন কম্পোনেন্ট আপডেট করতে হবে?**

**Answer (English):**
React uses a heuristic $O(n)$ Diffing Algorithm based on two rules:
1.  **Different Element Types:** If two root elements have different types (e.g., changing `<div>` to `<span>`), React tears down the old tree completely (unmounts) and builds a new tree from scratch.
2.  **Same Element Types:** React keeps the DOM node and updates only the changed attributes or props.
3.  **List Keys:** Uses `key` attributes to match children across renders to avoid re-rendering untouched list elements.

**অনুবাদ (Bangla Translation):**
রিঅ্যাক্ট ২টি মূল নিয়মের ওপর ভিত্তি করে Diffing অ্যালগরিদম চালায়:
1.  **ভিন্ন এলিমেন্ট টাইপ:** ট্যাগের টাইপ বদলে গেলে (যেমন `<div>` থেকে `<span>`) রিয়্যাক্ট পুরোনো গাছ পুরো ভেঙে ফেলে নতুন করে আনমাউন্ট ও মাউন্ট করে।
2.  **একই এলিমেন্ট টাইপ:** কেবল পরিবর্তিত প্রপস বা অ্যাট্রিবিউটটুকু ব্রাউজার ডমে আপডেট করে।
3.  **লিস্ট কি:** `key` দেখে লিস্টের আইটেম শনাক্ত করে অপ্রয়োজনীয় রি-রেন্ডার আটকায়।

---

### **Q54: What is “time slicing” in React Fiber? How does it improve performance? / React Fiber-এ “Time Slicing” কী এবং এটি কীভাবে পারফরম্যান্স বাড়ায়?**

**Answer (English):**
Time Slicing breaks large rendering tasks into small work units and spreads them across multiple browser animation frames (~16ms per frame).
*   **Performance Benefit:** Keeps the main browser thread free to handle urgent user interactions (typing, clicks, hover animations), eliminating UI input lag during heavy component renders.

**অনুবাদ (Bangla Translation):**
Time Slicing হলো বড় রেন্ডারিং কাজকে ছোট ছোট টুকরোতে ভাগ করে ব্রাউজারের বিভিন্ন ফ্রেমের (~16ms) মাঝে ছড়িয়ে দেওয়া।
*   **পারফরম্যান্স সুবিধা:** ইউজার ইনপুট বা অ্যানিমেশন যেন আটকে না যায় সে জন্য মেইন থ্রেডকে ফ্রি রাখে, ফলে ভারী কাজের সময়েও স্ক্রিন ল্যাগ করে না।

---

### **Q55: What are custom hooks? Can you show an example of when to use one? / Custom Hooks কী? একটি ব্যবহারের উদাহরণ দিন।**

**Answer (English):**
Custom Hooks are JavaScript functions whose names start with `use` and can call other React hooks inside.
*   **Example (Window Resize Tracker):**
    ```javascript
    function useWindowSize() {
      const [size, setSize] = useState(window.innerWidth);
      useEffect(() => {
        const handleResize = () => setSize(window.innerWidth);
        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
      }, []);
      return size;
    }
    ```

**অনুবাদ (Bangla Translation):**
কাস্টম হুক হলো এমন জাভাস্ক্রিপ্ট ফাংশন যার নাম `use` দিয়ে শুরু হয় এবং যার ভেতরে অন্যান্য রিয়্যাক্ট হুক ব্যবহার করা যায়।
*   **উদাহরণ (উইন্ডো সাইজ ট্র্যাকার):**
    ```javascript
    function useWindowSize() {
      const [size, setSize] = useState(window.innerWidth);
      useEffect(() => {
        const handleResize = () => setSize(window.innerWidth);
        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
      }, []);
      return size;
    }
    ```

---

### **Q56: How would you optimize a large React application for performance? / একটি বড় React অ্যাপ্লিকেশন অপ্টিমাইজ করার জন্য আপনি কী কী করবেন?**

**Answer (English):**
1.  **Code Splitting:** Route-level dynamic imports using `React.lazy()` & `Suspense`.
2.  **Prevent Unnecessary Renders:** Use `React.memo`, `useCallback`, `useMemo`.
3.  **List Virtualization:** Render large lists using `react-window` or `react-virtualized`.
4.  **Optimize Context:** Split large contexts and memoize values.
5.  **Efficient Data Fetching:** Use TanStack Query to manage server cache efficiently.

**অনুবাদ (Bangla Translation):**
1.  **কোড স্প্লিটিং:** `React.lazy()` ও `Suspense` দিয়ে পেজ ভিত্তিক ফাইল আলাদা লোড করা।
2.  **অহেতুক রেন্ডার আটকানো:** `React.memo`, `useCallback`, `useMemo` ব্যবহার।
3.  **লিস্ট ভার্চুয়ালাইজেশন:** বড় লিস্টের জন্য `react-window` ব্যবহার করা।
4.  **কনটেক্সট অপ্টিমাইজেশন:** কনটেক্সট ছোট ছোট খণ্ডে ভাগ করা।
5.  **সার্ভার ক্যাশিং:** TanStack Query ব্যবহার করা।

---

### **Q57: Explain React Suspense for Data Fetching. How is it different from `useEffect`? / Data Fetching-এর ক্ষেত্রে React Suspense কীভাবে কাজ করে? এটি `useEffect` থেকে কীভাবে আলাদা?**

**Answer (English):**
*   **`useEffect` Data Fetching:** Component renders empty/loading UI first, fetches data in the effect, updates state, then re-renders with data (Fetch-on-Render waterfall).
*   **Suspense Data Fetching:** React "pauses" component rendering while data is being fetched in parallel, rendering a fallback UI at a higher level until the data stream resolves (Render-as-You-Fetch).

**অনুবাদ (Bangla Translation):**
*   **`useEffect` ফেচিং:** কম্পোনেন্ট আগে খালি ফ্রেমে রেন্ডার হয়, তারপর ইফেক্টে এপিআই কল করে স্টেট আপডেট করে আবার রেন্ডার হয় (Fetch-on-Render)।
*   **Suspense ফেচিং:** ডেটা লোড চলাকালীন রিয়্যাক্ট কম্পোনেন্ট রেন্ডার আটকে রেখে প্রোভাইডার লেভেলে সুন্দর স্পিনার দেখায় (Render-as-You-Fetch)।

---

### **Q58: What is the difference between client-side routing and server-side routing in React? / React-এ Client-Side Routing এবং Server-Side Routing-এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Client-Side Routing (CSR - e.g., React Router):** Navigation is handled in the browser JS without requesting a new HTML file from the server. Only components change dynamically.
*   **Server-Side Routing (SSR - e.g., Next.js App Router):** Every new route request hits the server, which renders and returns a full HTML document.

**অনুবাদ (Bangla Translation):**
*   **Client-Side Routing (CSR):** ব্রাউজারের জাভাস্ক্রিপ্ট দিয়েই পেজ চেঞ্জ হয় (যেমন React Router)। কোনো নতুন HTML পেজ সার্ভার থেকে রিকোয়েস্ট করতে হয় না।
*   **Server-Side Routing (SSR):** প্রতিটি ইউআরএল (URL) পরিবর্তনের সাথে সাথে সার্ভারে রিকোয়েস্ট যায় এবং নতুন সম্পূর্ণ HTML পেজ আসে।

---

### **Q59: How does `React.StrictMode` help detect unsafe lifecycles and side effects? / `React.StrictMode` কীভাবে আনসেফ লাইফসাইকেল ও সাইড এফেক্ট ধরতে সাহায্য করে?**

**Answer (English):**
In development mode, `StrictMode` intentionally executes component functions and `useEffect` callbacks **twice**. This intentionally highlights hidden side-effects, state mutation bugs, and uncleaned subscriptions that would cause bugs in concurrent rendering.

**অনুবাদ (Bangla Translation):**
ডেভেলপমেন্ট মোডে `StrictMode` ইচ্ছে করেই কম্পোনেন্ট ও `useEffect`-কে **দুইবার করে রান ফায়ার করায়**। এর ফলে কোডে লুকিয়ে থাকা অসাবধানতাবশত সাইড এফেক্ট বা আনক্লিন মেমোরি লিক বাগ সহজে সামনে চলে আসে।

---

### **Q60: Explain the difference between `ReactDOM.render` and `ReactDOM.hydrate`. When do you use each? / `ReactDOM.render` এবং `ReactDOM.hydrate` এর মধ্যে পার্থক্য কী? কোনটি কখন ব্যবহার করবেন?**

**Answer (English):**
*   **`ReactDOM.render`:** Used for client-only applications. It wipes out existing HTML inside the root container and builds the DOM tree from scratch.
*   **`ReactDOM.hydrate` (now `hydrateRoot` in React 18):** Used for Server-Side Rendered (SSR) HTML. It preserves existing HTML markup and attaches event listeners to make it interactive.

**অনুবাদ (Bangla Translation):**
*   **`ReactDOM.render`:** কেবল ক্লায়েন্ট-সাইড অ্যাপে ব্যবহৃত হয়। এটি রুট কন্টেইনারের সব কিছু মুছে নতুন করে ডম বানায়।
*   **`ReactDOM.hydrate` (`hydrateRoot`):** সার্ভার-সাইড রেন্ডার (SSR) হওয়া HTML-এর জন্য ব্যবহৃত হয়। এটি বিদ্যমান স্ট্যাটিক কোড না মুছে তার ওপর ইভেন্ট লিসেনার বসায়।

---

### **Q61: What are render props and how do they differ from higher-order components (HOCs)? / Render Props কী এবং এগুলো HOC থেকে কীভাবে আলাদা?**

**Answer (English):**
*   **Render Props:** A pattern where a component receives a function as a prop and calls it to determine what to render (`<Mouse render={pos => <h1>{pos.x}</h1>} />`).
*   **Difference:** Render props composition happens inside JSX dynamically, avoiding wrapper component nesting and static prop collisions common with HOCs.

**অনুবাদ (Bangla Translation):**
*   **Render Props:** এমন একটি প্যাটার্ন যেখানে একটি কম্পোনেন্ট প্রপস হিসেবে একটি ফাংশন নেয় এবং কীভাবে রেন্ডার করবে তা ওই ফাংশন দিয়ে ঠিক করে।
*   **পার্থক্য:** এটি JSX-এর ভেতরে ডাইনামিকালি কাজ করে, যার ফলে HOC-এর মতো অতিরিক্ত নেস্টেড কম্পোনেন্ট তৈরি হয় না।

---

### **Q62: Explain the difference between `useEffect` cleanup and `componentWillUnmount` in class components. / `useEffect` cleanup এবং `componentWillUnmount` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`componentWillUnmount`:** Runs **only once** right before the class component is unmounted from the DOM.
*   **`useEffect` Cleanup:** Runs when the component unmounts, BUT ALSO runs **before every re-execution of the effect** if dependencies change, ensuring old subscriptions are cleaned up before new ones open.

**অনুবাদ (Bangla Translation):**
*   **`componentWillUnmount`:** কেবল কম্পোনেন্টটি ডম থেকে মুছে যাওয়ার ঠিক **পূর্বে একবার** রান করে।
*   **`useEffect` Cleanup:** কম্পোনেন্ট আনমাউন্টের সময় তো রান করেই, সাথে **প্রতিবার নতুন করে ইফেক্ট চলার আগেও** পুরোনো ইফেক্টের সাফাই বা ক্লিনআপ সম্পন্ন করে।

---

### **Q63: How would you implement a React component that subscribes to an external data source and cleans up correctly? / কোনো এক্সটারনাল ডেটা সোর্সে সাবস্ক্রাইব করা এবং সঠিকভাবে ক্লিনআপ করার জন্য রিয়্যাক্ট কম্পোনেন্ট কীভাবে লিখবেন?**

**Answer (English):**
Using `useEffect` with a return cleanup function:
```javascript
useEffect(() => {
  const subscription = dataSource.subscribe(handleData);
  return () => {
    subscription.unsubscribe(); // Cleanup on unmount/re-effect
  };
}, [dataSource]);
```

**অনুবাদ (Bangla Translation):**
`useEffect`-এর ভেতর রিটার্ন ক্লিয়ার ফাংশন ব্যবহার করে:
```javascript
useEffect(() => {
  const subscription = dataSource.subscribe(handleData);
  return () => {
    subscription.unsubscribe(); // আনমাউন্ট হলে কানেকশন বন্ধ হবে
  };
}, [dataSource]);
```

---

### **Q64: What is the difference between React server components and client components? / React Server Components এবং Client Components এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Server Components (RSC):** Render exclusively on the server. Zero client JS bundle size, direct database access, no hooks or browser interactivity (`useState`/`useEffect`).
*   **Client Components (`'use client'`):** Rendered on client (and pre-rendered on server). Full support for interactivity, state, hooks, and DOM event listeners.

**অনুবাদ (Bangla Translation):**
*   **Server Components:** কেবল সার্ভারেই রেন্ডার হয়। ব্রাউজারে কোনো জাভাস্ক্রিপ্ট বান্ডেল পাঠায় না, সরাসরি ডেটাবেজ অ্যাক্সেস করতে পারে, তবে এতে `useState` বা ইভেন্ট লিসেনার থাকে না।
*   **Client Components (`'use client'`):** ব্রাউজারে কাজ করে। সব ধরনের হুকস, ইভেন্ট লিসেনার ও ইউজার ইন্টারঅ্যাকশন সাপোর্ট করে।

---

### **Q65: How do you prevent unnecessary re-renders in React components? / React কম্পোনেন্টে অপ্রয়োজনীয় Re-render কীভাবে আটকাবেন?**

**Answer (English):**
1.  Wrap components with `React.memo()`.
2.  Memoize objects/arrays with `useMemo()`.
3.  Memoize functions with `useCallback()`.
4.  Keep state local rather than lifting it unnecessarily high.

**অনুবাদ (Bangla Translation):**
১. কম্পোনেন্ট `React.memo()` দিয়ে র্যাপ করা।
২. অবজেক্ট/অ্যারে প্রপস `useMemo()` দিয়ে মেমোরাইজ করা।
৩. ফাংশন `useCallback()` দিয়ে স্থায়ী রাখা।
৪. গ্লোবাল স্টেট না বাড়িয়ে লোকাল স্টেট ব্যবহার করা।

---

### **Q66: What is `React.memo` and when should you use it? / `React.memo` কী এবং এটি কখন ব্যবহার করবেন?**

**Answer (English):**
`React.memo` is a performance HOC that skips re-rendering a component if its incoming props are shallowly equal to its previous props.
*   **When to use:** Pure visual components that re-render often with the exact same props inside heavy parent component trees.

**অনুবাদ (Bangla Translation):**
`React.memo` হলো একটি পারফরম্যান্স HOC যা প্রপস না পাল্টালে চাইল্ড কম্পোনেন্ট রি-রেন্ডার হওয়া আটকে দেয়।
*   **কখন ব্যবহার করবেন:** যখন প্যারেন্ট বারবার রি-রেন্ডার হলেও চাইল্ডের প্রপস অপরিবর্তিত থাকে।

---

### **Q67: What is the difference between `React.memo` and `useMemo`? / `React.memo` এবং `useMemo` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
(Duplicate Q51 summary): `React.memo` wraps and memoizes an entire **Component**, while `useMemo` is a hook that memoizes a **calculated value** inside a component function.

**অনুবাদ (Bangla Translation):**
(প্রশ্ন ৫১ এর সংক্ষেপ): `React.memo` পুরো একটি **কম্পোনেন্টকে** মেমোরাইজ করে, আর `useMemo` কম্পোনেন্টের ভেতরের একটি **নির্দিষ্ট ভ্যালু বা হিসাবকে** মেমোরাইজ করে।

---

### **Q68: What is the React event system and how is it different from native DOM events? / React ইভেন্ট সিস্টেম কী এবং এটি নেটিভ ডম ইভেন্টের চেয়ে কীভাবে আলাদা?**

**Answer (English):**
(Duplicate Q52 summary): React wraps native browser events into cross-browser `SyntheticEvent` instances and uses root-level **Event Delegation** for performance and cross-browser consistency.

**অনুবাদ (Bangla Translation):**
(প্রশ্ন ৫২ এর সংক্ষেপ): রিয়্যাক্ট ব্রাউজার ইভেন্টকে `SyntheticEvent` দিয়ে র্যাপ করে এবং পারফরম্যান্সের জন্য রুট লেভেলে **Event Delegation** ব্যবহার করে।

---

### **Q69: What are custom hooks and why should you use them? / Custom Hooks কী এবং কেন এগুলো ব্যবহার করবেন?**

**Answer (English):**
(Duplicate Q55 summary): Custom hooks extract component logic into reusable functions starting with `use`. They reduce code repetition and keep components focused on UI rendering.

**অনুবাদ (Bangla Translation):**
(প্রশ্ন ৫৫ এর সংক্ষেপ): কাস্টম হুকস হলো `use` দিয়ে শুরু হওয়া ফাংশন যা একাধিক কম্পোনেন্টের লজিক এক জায়গায় নিয়ে কোড রি-ইউজ করতে সাহায্য করে।

---

### **Q70: What is time slicing in React and why is it important? / React-এ Time Slicing কী এবং এটি কেন গুরুত্বপূর্ণ?**

**Answer (English):**
(Duplicate Q54 summary): Time slicing divides render calculations into small frames, preventing heavy rendering from blocking the main thread, keeping user inputs fluid.

**অনুবাদ (Bangla Translation):**
(প্রশ্ন ৫৪ এর সংক্ষেপ): রেন্ডারিং কাজকে ক্ষুদ্র ফ্রেমে ভাগ করে চালানো যাতে মেইন থ্রেড ব্লক না হয় এবং টাইপিং বা অ্যানিমেশন স্মুথ থাকে।

---

### **Q71: How would you implement optimistic UI updates in React applications? / React অ্যাপ্লিকেশনে Optimistic UI Updates কীভাবে ইমপ্লিমেন্ট করবেন?**

**Answer (English):**
Optimistic UI updates immediately update the UI state assuming the server request will succeed, and roll back if it fails.
*   **Implementation:** Update state instantly -> send API fetch request -> if API fails in `.catch()`, revert state to previous value and show error toast (or use React 19 `useOptimistic` hook).

**অনুবাদ (Bangla Translation):**
Optimistic UI Update হলো সার্ভার রিকোয়েস্ট সফল হবে ধরে নিয়ে ইউজার বাটনে চাপ দেওয়া মাত্রই স্ক্রিনের ইউআই সাথে সাথে বদলে দেওয়া।
*   **বাস্তবায়ন:** সাথে সাথে স্টেট আপডেট করা -> সার্ভারে পোস্ট রিকোয়েস্ট পাঠানো -> যদি সার্ভার ফেল করে তবে `.catch()` এ আগের স্টেটে ফিরিয়ে নেওয়া (রোলব্যাক) (React 19-এ এর জন্য `useOptimistic` হুক রয়েছে)।

---

### **Q72: How do you handle accessibility (a11y) in a React application? / React অ্যাপ্লিকেশনে অ্যাক্সেসিবিলিটি (a11y) কীভাবে হ্যান্ডেল করবেন?**

**Answer (English):**
1.  **Semantic HTML:** Use native elements (`<button>`, `<nav>`, `<main>`).
2.  **ARIA Attributes:** Use `aria-label`, `aria-expanded`, `role="dialog"` for custom components.
3.  **Keyboard Navigation:** Manage focus using `refs` and ensure `tabIndex` flow.
4.  **Audit Tools:** Use `react-axe` or Lighthouse to audit accessibility issues.

**অনুবাদ (Bangla Translation):**
১. নেটিভ সিম্যান্টিক HTML ব্যবহার করা (`<button>`, `<nav>`)।
২. কাস্টম কম্পোনেন্টে `aria-label` ও `role` ব্যবহার করা।
৩. কিবোর্ড নেভিগেশন ও ফোকাস ঠিক রাখা।
৪. `react-axe` দিয়ে অডিট করা।

---

### **Q73: What are React Portals and when would you use them? Can you give a complex example? / React Portals কী এবং এটি কখন ব্যবহার করবেন? একটি জটিল উদাহরণ দিন।**

**Answer (English):**
(Expanded from Q27): Portals render children outside their parent DOM hierarchy.
*   **Complex Example (Modal with Focus Trap):** A Modal component rendered into `document.body` via Portal, managing keyboard focus trapping (`Tab` key inside modal), closing on `Escape` key press, and disabling background scroll.

**অনুবাদ (Bangla Translation):**
(প্রশ্ন ২৭ এর বিস্তারিত): পোর্টাল প্যারেন্টের বাইরে ডম এলিমেন্টে রেন্ডার করায়।
*   **জটিল উদাহরণ:** একটি মডাল (Modal) যা `document.body`-তে রেন্ডার হয়ে কিবোর্ডের `Tab` কি-এর ফোকাস লক করে রাখে, `Escape` চাপলে বন্ধ হয় এবং ব্যাকগ্রাউন্ড স্ক্রলিং বন্ধ করে।

---

### **Q74: Explain the difference between shallow rendering and full DOM rendering in React testing. / React টেস্টিংয়ে Shallow rendering এবং Full DOM rendering এর মধ্যে পার্থক্য ব্যাখ্যা করুন।**

**Answer (English):**
*   **Shallow Rendering (Enzyme):** Renders only the current component **one level deep**, ignoring child components. Fast unit testing for isolated logic.
*   **Full DOM Rendering (React Testing Library / mount):** Renders the component along with its **entire child tree** in a simulated DOM. Better for integration testing and user behavior validation.

**অনুবাদ (Bangla Translation):**
*   **Shallow Rendering:** কেবল বর্তমান কম্পোনেন্টটিকে টেস্ট করে, এর ভেতরের চাইল্ড কম্পোনেন্টগুলোকে রেন্ডার করে না (আইসোলেটেড ইউনিট টেস্টের জন্য)।
*   **Full DOM Rendering:** কম্পোনেন্টের পাশাপাশি তার নিচের পুরো চাইল্ড ট্রি ব্রাউজার ডমে রেন্ডার করে টেস্ট করে (ইন্টিগ্রেশন টেস্টের জন্য)।

---

### **Q75: What is the difference between server components and client components in React? / React-এ Server Components এবং Client Components এর মধ্যে পার্থক্য কী?**

**Answer (English):**
(Duplicate Q64 summary): Server Components render strictly on the server with zero client JS payload and direct backend access. Client Components (`'use client'`) run on the browser and handle interactive features, state (`useState`), and event listeners (`onClick`).

**অনুবাদ (Bangla Translation):**
(প্রশ্ন ৬৪ এর সংক্ষেপ): Server Components কেবল সার্ভারে চলে, ক্লায়েন্টে কোনো জাভাস্ক্রিপ্ট বান্ডেল পাঠায় না। Client Components ব্রাউজারে চলে এবং সব ধরনের ইউজার ইন্টারঅ্যাকশন ও হুকস সামলায়।
