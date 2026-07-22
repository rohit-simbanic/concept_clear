# JavaScript Interview Questions Guide: Volume 4 (Questions 111 - 150)

This guide contains detailed answers in English alongside complete Bangla translations for questions 111 to 150 from the uploaded JavaScript Interview Questions PDF.

---

### **Q111: What are workers in JavaScript used for? / JavaScript-এ ওয়ার্কার্স (Workers) কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
Web Workers allow JavaScript to run scripts in background threads separate from the main browser UI execution thread.
*   **Purpose:** Prevents UI freezing by offloading heavy CPU computations (image processing, data parsing, complex sorting) to a dedicated worker thread.
*   **Types:** Web Workers (Dedicated), Service Workers (Caching/PWA), Shared Workers.
*   **Constraint:** Workers cannot directly access or manipulate the DOM. They communicate with the main thread using `postMessage()` and `onmessage`.

**অনুবাদ (Bangla Translation):**
ওয়েব ওয়ার্কার্স (Web Workers) ব্রাউজারের মূল ইউআই (UI) এক্সিকিউশন থ্রেড থেকে আলাদা একটি ব্যাকগ্রাউন্ড থ্রেডে জাভাস্ক্রিপ্ট কোড চালানোর সুযোগ দেয়।
*   **উদ্দেশ্য:** ভারী সিপিইউ প্রসেসিং (যেমন- বিশাল ডেটা পার্সিং বা ছবি অ্যানালাইসিস) ব্যাকগ্রাউন্ডে পাঠিয়ে মূল থ্রেডকে সচল রাখে যাতে ব্রাউজার স্ক্রিন ফ্রিজ না হয়।
*   **ধরন:** Web Workers, Service Workers (অফলাইন/PWA), Shared Workers।
*   **সীমাবদ্ধতা:** ওয়ার্কার্স সরাসরি ডম (DOM) পরিবর্তন করতে পারে না। মেইন থ্রেডের সাথে এটি `postMessage()` দিয়ে মেসেজ আদান-প্রদান করে।

---

### **Q112: Explain the concept of the Web Socket API. / Web Socket API ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
The WebSocket API establishes a persistent, full-duplex (two-way), low-latency TCP connection between a client browser and a server.
*   **How it differs from HTTP:** HTTP is request-response based (one-way). WebSockets keep the connection open, allowing the server to push real-time data to the client anytime (ideal for chat apps, live stock quotes, multiplayer games).

**অনুবাদ (Bangla Translation):**
ওয়েব সকেট এপিআই (WebSocket API) হলো ক্লায়েন্ট ব্রাউজার এবং সার্ভারের মধ্যে একটি দীর্ঘস্থায়ী, উভয়মুখী (Full-Duplex) এবং অত্যন্ত দ্রুত ডেটা আদান-প্রদানের কানেকশন মেকানিজম।
*   **HTTP এর সাথে পার্থক্য:** HTTP হলো একমুখী রিকোয়েস্ট-রেসপন্স সিস্টেম। কিন্তু ওয়েব সকেট কানেকশন উন্মুক্ত রাখে, ফলে সার্ভার যেকোনো মুহূর্তে ক্লায়েন্টের রিকোয়েস্ট ছাড়াই রিয়েল-টাইম তথ্য পাঠাতে পারে (যেমন- চ্যাট অ্যাপ, লাইভ স্কোর বা গেম)।

---

### **Q113: What are JavaScript polyfills for? / JavaScript-এ Polyfill কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
A polyfill is a piece of code (usually JavaScript) used to provide modern web functionality to older browsers that natively lack support for those features.
*   **Example:** If an old browser doesn't support `Array.prototype.includes()`, a polyfill script implements that method manually using ES5 code. Libraries like `core-js` provide standard polyfills.

**অনুবাদ (Bangla Translation):**
পলিফিল (Polyfill) হলো সিএসএস বা জাভাস্ক্রিপ্ট কোডের টুকরো যা পুরাতন ব্রাউজারে অনুপস্থিত আধুনিক ফিচারগুলোকে ম্যানুয়ালি কোড লিখে সাপোর্ট দেওয়ার কাজে ব্যবহৃত হয়।
*   **উদাহরণ:** পুরাতন ব্রাউজারে `Array.prototype.includes()` না থাকলে পলিফিল কোড লিখে সেই ফাংশনটি তৈরি করে দেওয়া হয় যাতে অ্যাপ ক্র্যাশ না করে। `core-js` এর একটি বড় উদাহরণ।

---

### **Q114: How do you detect if JavaScript is disabled on a page? / কোনো পেজে জাভাস্ক্রিপ্ট ডিসেবল বা বন্ধ করা আছে কিনা তা কীভাবে ডিটেক্ট করবেন?**

**Answer (English):**
Use the HTML `<noscript>` tag. HTML inside `<noscript>` is rendered by the browser **only** if JavaScript execution is disabled in the user's browser settings.
*   **Example:**
    ```html
    <noscript>
      <div class="warning">Please enable JavaScript to view this website properly.</div>
    </noscript>
    ```

**অনুবাদ (Bangla Translation):**
HTML-এর `<noscript>` ট্যাগ ব্যবহার করে। ইউজার যদি ব্রাউজার সেটিংসে জাভাস্ক্রিপ্ট অফ করে রাখে, তবেই কেবল এই `<noscript>` ট্যাগের ভেতরের লেখা বা ওয়ার্নিং মেসেজটি ব্রাউজারে দৃশ্যমান হয়।
*   **উদাহরণ:**
    ```html
    <noscript>
      <div class="warning">এই ওয়েবসাইটটি সঠিকভাবে দেখার জন্য অনুগ্রহ করে জাভাস্ক্রিপ্ট অন করুন।</div>
    </noscript>
    ```

---

### **Q115: What is the `Intl` namespace object for? / `Intl` নেমস্পেস অবজেক্ট কী কাজে ব্যবহৃত হয়?**

**Answer (English):**
The `Intl` object is the ECMAScript Internationalization API namespace. It provides language-sensitive string comparison, number formatting, currency formatting, and date/time formatting.
*   **Example:**
    ```javascript
    const number = 123456.78;
    console.log(new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(number));
    // Output: ₹1,23,456.78
    ```

**অনুবাদ (Bangla Translation):**
`Intl` অবজেক্ট হলো জাভাস্ক্রিপ্টের ইন্টারন্যাশনালইজেশন (Internationalization) এপিআই। এটি বিভিন্ন দেশের ভাষা ও আঞ্চলিক রীতি অনুযায়ী সংখ্যা, মুদ্রা (Currency) এবং তারিখ/সময় সুন্দরভাবে ফরম্যাট করতে সাহায্য করে।
*   **উদাহরণ:**
    ```javascript
    const number = 123456.78;
    console.log(new Intl.NumberFormat('en-IN', { style: 'currency', currency: 'INR' }).format(number));
    // আউটপুট: ₹1,23,456.78
    ```

---

### **Q116: How do you validate form elements using the Constraint Validation API? / Constraint Validation API ব্যবহার করে কীভাবে ফর্ম এলিমেন্ট ভ্যালিডেট করবেন?**

**Answer (English):**
The Constraint Validation API provides DOM properties and methods to check input validity natively:
*   **Properties:** `element.validity` (returns flags like `valueMissing`, `typeMismatch`), `element.validationMessage`.
*   **Methods:** `element.checkValidity()` (returns boolean), `element.setCustomValidity('Custom error message')`.

**অনুবাদ (Bangla Translation):**
Constraint Validation API হলো ব্রাউজারের নেটিভ মেথড যা দিয়ে অতিরিক্ত লাইব্রেরি ছাড়া ইনপুট ভ্যালিডেশন করা যায়:
*   **প্রপার্টি:** `element.validity` (যেমন `valueMissing` বা `typeMismatch` চেক করে), `element.validationMessage` (এরর মেসেজ)।
*   **মেথড:** `element.checkValidity()` (সঠিক কিনা ট্রু/ফলস দেয়), `element.setCustomValidity('কাস্টম এরর')` (নিজস্ব এরর মেসেজ সেট করা)।

---

### **Q117: How do you use `window.history` API? / `window.history` API কীভাবে ব্যবহার করবেন?**

**Answer (English):**
The `window.history` API allows manipulating browser session history stack:
*   `history.back()`: Goes to previous page.
*   `history.forward()`: Goes to next page.
*   `history.go(-2)`: Navigates back by 2 pages.
*   `history.pushState(state, title, url)`: Adds a new entry to the browser history without triggering a page refresh (Core mechanism of Client-Side Single Page Application routing).
*   `history.replaceState(state, title, url)`: Modifies current history entry.

**অনুবাদ (Bangla Translation):**
`window.history` এপিআই ব্রাউজারের হিস্ট্রি স্ট্যাক ম্যানিপুলেট করতে ব্যবহৃত হয়:
*   `history.back()`: পেছনের পেজে ফিরে যায়।
*   `history.forward()`: সামনের পেজে যায়।
*   `history.pushState(state, title, url)`: পেজ রিফ্রেশ না করেই ব্রাউজারের ইউআরএল এবং হিস্ট্রি চেঞ্জ করে (SPA রাউটিংয়ের মূল ভিত্তি)।
*   `history.replaceState()`: বর্তমান হিস্ট্রি অ্যান্ট্রি আপডেট করে।

---

### **Q118: How do `<iframe>` on a page communicate? / কোনো পেজে থাকা `<iframe>` কীভাবে একে অপরের সাথে যোগাযোগ করে?**

**Answer (English):**
Using the `window.postMessage()` API for secure cross-origin communication between parent page and iframe window.
*   **Sending:** `iframeWindow.postMessage(data, targetOrigin);`
*   **Receiving:**
    ```javascript
    window.addEventListener('message', (event) => {
      if (event.origin !== 'https://trusted-domain.com') return; // Security check
      console.log(event.data);
    });
    ```

**অনুবাদ (Bangla Translation):**
প্যারেন্ট পেজ এবং iframe-এর মধ্যে নিরাপদ যোগাযোগের জন্য `window.postMessage()` এপিআই ব্যবহার করা হয়।
*   **মেসেজ পাঠানো:** `iframeWindow.postMessage(data, targetOrigin);`
*   **মেসেজ রিসিভ করা:**
    ```javascript
    window.addEventListener('message', (event) => {
      if (event.origin !== 'https://trusted-domain.com') return; // নিরাপত্তা চেক
      console.log(event.data);
    });
    ```

---

### **Q119: Difference between `document load` event and `DOMContentLoaded` event? / `document load` এবং `DOMContentLoaded` ইভেন্টের মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **`DOMContentLoaded`:** Fires as soon as the initial HTML document is completely loaded and parsed, without waiting for external stylesheets, images, or async frames to finish loading.
*   **`load` (window.onload):** Fires only after the entire page and **all dependent resources** (images, CSS, subframes, scripts) have fully loaded.

**অনুবাদ (Bangla Translation):**
*   **`DOMContentLoaded`:** মূল HTML ডকুমেন্টের রিড ও পার্সিং শেষ হওয়া মাত্রই ফায়ার হয়। এটি সিএসএস, ছবি বা এক্সটারনাল ফাইল লোড হওয়া পর্যন্ত অপেক্ষা করে না।
*   **`load` (window.onload):** পুরো পেজ এবং তার **সমস্ত ফাইল** (ছবি, স্টাইলশিট, ফ্রেম) পুরোপুরি ডাউনলোড শেষ হওয়ার পর ফায়ার হয়।

---

### **Q120: How do you redirect to a new page in JavaScript? / JavaScript-এ কীভাবে নতুন পেজে রিডাইরেক্ট করবেন?**

**Answer (English):**
1.  **`window.location.href = 'https://example.com'`:** Simulates a user clicking on a link. Adds an entry to browser history (back button works).
2.  **`window.location.replace('https://example.com')`:** Replaces current document entry in browser history (back button will NOT return to current page).

**অনুবাদ (Bangla Translation):**
1.  **`window.location.href = 'url'`:** লিংকে চাপ দেওয়ার মতো কাজ করে। ব্রাউজার হিস্ট্রিতে অ্যান্ট্রি থাকে (ব্যাক বাটন চাপলে আগের পেজে আসা যায়)।
2.  **`window.location.replace('url')`:** বর্তমান পেজকে হিস্ট্রি থেকে মুছে নতুন পেজ বসায় (ব্যাক বাটন চাপলে এই পেজে ফিরে আসা যায় না)।

---

### **Q121: How do you get the query string values of the current page in JavaScript? / JavaScript-এ বর্তমান পেজের ইউআরএল কুয়েরি স্ট্রিংয়ের মান কীভাবে পাবেন?**

**Answer (English):**
Use the built-in `URLSearchParams` object with `window.location.search`.
*   **Example:**
    ```javascript
    // URL: https://site.com?name=Rohit&age=25
    const params = new URLSearchParams(window.location.search);
    console.log(params.get('name')); // "Rohit"
    console.log(params.get('age'));  // "25"
    ```

**অনুবাদ (Bangla Translation):**
`window.location.search`-এর সাথে ব্রাউজারের `URLSearchParams` অবজেক্ট ব্যবহার করে।
*   **উদাহরণ:**
    ```javascript
    // URL: https://site.com?name=Rohit&age=25
    const params = new URLSearchParams(window.location.search);
    console.log(params.get('name')); // "Rohit"
    console.log(params.get('age'));  // "25"
    ```

---

### **Q122: What are server-sent events (SSE)? / Server-Sent Events (SSE) কী?**

**Answer (English):**
Server-Sent Events (SSE) allow a server to push real-time text updates to the client browser over a persistent HTTP connection using the `EventSource` API.
*   **Key Attributes:** Unidirectional (server -> client only), text data only, automatically reconnects if connection drops.

**অনুবাদ (Bangla Translation):**
সার্ভার-সেন্ট ইভেন্টস (SSE) হলো `EventSource` এপিআই ব্যবহার করে সাধারণ HTTP সংযোগের মাধ্যমে ক্লায়েন্ট ব্রাউজারে সার্ভার থেকে রিয়েল-টাইম পুশ নোটিফিকেশন বা টেক্সট আপডেট পাঠানোর একমুখী (Unidirectional) প্রযুক্তি।

---

### **Q123: What are Progressive Web Applications (PWAs)? / Progressive Web Applications (PWAs) কী?**

**Answer (English):**
PWAs are web applications built using modern web capabilities (Service Workers, Web App Manifests, HTTPS) to deliver a native app-like user experience.
*   **Key Features:** Works offline, installable on mobile home screens, fast load speeds, and push notifications.

**অনুবাদ (Bangla Translation):**
PWA হলো আধুনিক ওয়েব প্রযুক্তি (Service Workers, Web App Manifest) দিয়ে তৈরি এমন ওয়েবসাইট যা দেখতে ও ব্যবহার করতে হুবহু মোবাইলের নেটিভ অ্যাপের মতো অভিজ্ঞতা দেয়। অফলাইনে কাজ করা, হোম স্ক্রিনে ইনস্টল করা ও পুশ নোটিফিকেশন পাঠানো এর অন্যতম ক্ষমতা।

---

### **Q124: What are modules and why are they useful? / মডিউল (Modules) কী এবং এগুলো কেন দরকারী?**

**Answer (English):**
Modules are self-contained pieces of JavaScript code that encapsulate variables and functions, allowing them to be explicitly imported and exported across different files.
*   **Benefits:** Prevents global scope pollution, improves code maintainability, reusability, and dependency organization.

**অনুবাদ (Bangla Translation):**
মডিউল হলো জাভাস্ক্রিপ্ট কোডের স্বাধীন ও আলাদা অংশ যা নিজের ভেতরে ভ্যারিয়েবল ও ফাংশন লুকিয়ে রাখে এবং `import`/`export`-এর মাধ্যমে ফাইলের মধ্যে আদান-প্রদান করা যায়।
*   **সুবিধা:** গ্লোবাল স্কোপ দূষণ এড়ায়, কোড সহজে মেইনটেইন ও বারবার রি-ইউজ করা যায়।

---

### **Q125: Explain the differences between CommonJS modules and ES modules in JavaScript. / CommonJS মডিউল এবং ES মডিউলের মধ্যে পার্থক্য ব্যাখ্যা করুন।**

**Answer (English):**
*   **CommonJS (CJS):** Legacy Node.js standard. Uses `require()` and `module.exports`. Synchronous loading at runtime.
*   **ES Modules (ESM):** Official ECMAScript standard. Uses `import` and `export`. Asynchronous static loading at parse time (supports Tree-Shaking). Supported natively in browsers and modern Node.js.

**অনুবাদ (Bangla Translation):**
*   **CommonJS (CJS):** Node.js-এর সনাতন স্ট্যান্ডার্ড। এটি `require()` এবং `module.exports` ব্যবহার করে। রানটাইমে সিনক্রোনাসলি লোড হয়।
*   **ES Modules (ESM):** আধুনিক অফিশিয়াল স্ট্যান্ডার্ড। এটি `import` এবং `export` ব্যবহার করে। এটি পার্স টাইমে অ্যাসিনক্রোনাসলি লোড হয় এবং ব্রাউজারে সরাসরি চলে।

---

### **Q126: How do you import and export modules in JavaScript? / JavaScript-এ কীভাবে মডিউল import এবং export করবেন?**

**Answer (English):**
*   **Named Export & Import:**
    ```javascript
    // export
    export const name = 'Rohit';
    // import
    import { name } from './file.js';
    ```
*   **Default Export & Import:**
    ```javascript
    // export
    export default function add(a, b) { return a + b; }
    // import
    import add from './file.js';
    ```

**অনুবাদ (Bangla Translation):**
*   **Named Export & Import:**
    ```javascript
    // export
    export const name = 'Rohit';
    // import
    import { name } from './file.js';
    ```
*   **Default Export & Import:**
    ```javascript
    // export
    export default function add(a, b) { return a + b; }
    // import
    import add from './file.js';
    ```

---

### **Q127: What are the benefits of using a module bundler? / Module bundler ব্যবহার করার সুবিধা কী কী?**

**Answer (English):**
Module bundlers (like Webpack, Vite, Rollup) combine multiple JS files and assets into optimized static bundle files.
*   **Benefits:** Reduces HTTP requests, supports Tree-Shaking, enables Code Splitting, transpiles modern JS via Babel, and manages dependency resolution automatically.

**অনুবাদ (Bangla Translation):**
মডিউল বান্ডলার (যেমন Webpack, Vite) প্রজেক্টের শতাধিক ফাইলকে প্রসেস করে ছোট ও অপ্টিমাইজড বান্ডেল ফাইলে রূপান্তর করে।
*   **সুবিধা:** নেটওয়ার্ক রিকোয়েস্ট কমায়, ট্রা-শেকিং ও কোড স্প্লিটিং করে এবং বিভিন্ন সিএসএস/জেএস ডিপেনডেন্সি ঠিকভাবে ম্যানেজ করে।

---

### **Q128: Explain the concept of tree shaking in module bundling. / Module bundling-এ Tree Shaking ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
Tree Shaking is an optimization technique used by modern module bundlers to eliminate "dead code" (unused exports/functions) from the final JavaScript production bundle, reducing file size. Requires ES Module static `import`/`export` syntax.

**অনুবাদ (Bangla Translation):**
ট্রি শেকিং (Tree Shaking) হলো একটি পারফরম্যান্স অপ্টিমাইজেশন টেকনিক যা প্রজেক্টের ফাইনাল বান্ডেল বানানোর সময় কোডের অব্যবহৃত ফাংশন বা রিমুভড কোডগুলোকে ঝেড়ে ফেলে দিয়ে বান্ডেল সাইজ অনেক ছোট করে ফেলে।

---

### **Q129: What are the metadata fields of a module? / মডিউলের মেটাডেটা ফিল্ডগুলো কী কী?**

**Answer (English):**
Metadata fields (found in `package.json`) specify information about a module package:
*   `name`, `version`, `main` (CJS entry point), `module` (ESM entry point), `type` (`"module"` or `"commonjs"`), `dependencies`, `devDependencies`, `license`.

**অনুবাদ (Bangla Translation):**
মডিউলের মেটাডেটা ফিল্ডগুলো (যা `package.json`-এ থাকে) মডিউলের পরিচিতি প্রকাশ করে:
*   `name`, `version`, `main` (প্রধান ফাইল), `type` (`"module"` বা `"commonjs"`), `dependencies` ইত্যাদি।

---

### **Q130: What do you think of CommonJS vs ESM? / CommonJS বনাম ESM সম্পর্কে আপনার মত কী?**

**Answer (English):**
ESM is the future and standard of JavaScript. ESM works natively across browsers and Node.js, enables tree-shaking, and supports top-level await. CommonJS is legacy, restricted mainly to Node.js server environments, but remains heavily used in older npm packages.

**অনুবাদ (Bangla Translation):**
ESM হলো জাভাস্ক্রিপ্টের ভবিষ্যৎ ও অফিশিয়াল মানদণ্ড। এটি ব্রাউজার ও নড উভয় জায়গায় চলে এবং কোড অপ্টিমাইজেশনে সেরা। CommonJS কেবল Node.js ব্যাকএন্ডে কাজ করে এবং নতুন প্রজেক্টে ESM ব্যবহার করাই শ্রেয়।

---

### **Q131: What are the different types of errors in JavaScript? / JavaScript-এ বিভিন্ন ধরনের এররসমূহ কী কী?**

**Answer (English):**
1.  **SyntaxError:** Invalid JavaScript syntax parsing error.
2.  **ReferenceError:** Accessing an undeclared or uninitialized variable.
3.  **TypeError:** Operation on wrong data type (e.g., calling a non-function).
4.  **RangeError:** Number outside allowable range (e.g., infinite recursion stack overflow).
5.  **URIError:** Invalid parameters in `encodeURI()` or `decodeURI()`.

**অনুবাদ (Bangla Translation):**
1.  **SyntaxError:** সিএসএস/জেএস কোড ভুল ব্যাকরণে লিখলে।
2.  **ReferenceError:** ডিক্লেয়ার না করা বা TDZ ভ্যারিয়েবল কল করলে।
3.  **TypeError:** ভুল ডাটা টাইপে মেথড কল করলে (যেমন নাম্বারে লুপ চালানো)।
4.  **RangeError:** সীমার বাইরের সংখ্যা দিলে (যেমন অসীম রিকার্শন)।
5.  **URIError:** ইউআরএল এনকোডিংয়ে ভুল করলে।

---

### **Q132: How do you handle errors using `try...catch` blocks? / `try...catch` ব্লক ব্যবহার করে কীভাবে এরর হ্যান্ডেল করবেন?**

**Answer (English):**
Wrap code that might throw an error inside the `try` block. If an error occurs, control immediately jumps to the `catch` block where the error object can be logged or handled without crashing the app.
```javascript
try {
  let result = JSON.parse(invalidJson);
} catch (error) {
  console.error(error.name, error.message);
}
```

**অনুবাদ (Bangla Translation):**
যে কোডে এরর হওয়ার ঝুঁকি থাকে তা `try` ব্লকে রাখতে হয়। এরর হলে কোড ক্র্যাশ না করে সরাসরি `catch` ব্লকে চলে যায় যেখানে এরর হ্যান্ডেল করা হয়।
```javascript
try {
  let result = JSON.parse(invalidJson);
} catch (error) {
  console.error(error.name, error.message);
}
```

---

### **Q133: What is the purpose of the `finally` block? / `finally` ব্লকের উদ্দেশ্য কী?**

**Answer (English):**
The `finally` block executes **always**, regardless of whether the `try` block succeeded or an error was caught in `catch`.
*   **Use Case:** Cleanup tasks like closing loading spinners, hiding UI loaders, or releasing database connections.

**অনুবাদ (Bangla Translation):**
`finally` ব্লকের কোড **সর্বদা রান করবে**, `try` সফল হোক বা `catch`-এ এরর ধরা পড়ুক না কেন।
*   **ব্যবহার:** লোডিং স্পিনার বন্ধ করা, মেমোরি রিলিজ করা বা ডেটাবেজ কানেকশন ক্লোজ করার কাজে ব্যবহৃত হয়।

---

### **Q134: How can you create custom error objects? / কীভাবে কাস্টম এরর অবজেক্ট তৈরি করবেন?**

**Answer (English):**
By extending the built-in `Error` class in ES6:
```javascript
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}
throw new ValidationError("Invalid email address!");
```

**অনুবাদ (Bangla Translation):**
ES6-এর বিল্ট-ইন `Error` ক্লাসকে `extends` করে কাস্টম এরর ক্লাস বানানো যায়:
```javascript
class ValidationError extends Error {
  constructor(message) {
    super(message);
    this.name = "ValidationError";
  }
}
throw new ValidationError("Invalid email address!");
```

---

### **Q135: Explain the concept of error propagation in JavaScript. / JavaScript-এ Error Propagation (এরর ছড়ানো) ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
Error propagation refers to how uncaught errors travel up the Call Stack. If a function throws an error and has no `try...catch` block, the error propagates to the calling parent function, and continues up until it is caught or reaches the global environment (crashing the script).

**অনুবাদ (Bangla Translation):**
এরর প্রপাগেশন হলো হ্যান্ডেল না করা এরর কীভাবে কল স্ট্যাকের ওপরে উঠতে থাকে। কোনো ফাংশনে এরর ক্যাচ না করা হলে তা তার প্যারেন্ট ফাংশনে চলে যায়, এভাবে উপরে উঠতে উঠতে গ্লোবাল এনভায়রনমেন্টে পৌঁছে পেজ ক্র্যাশ করায়।

---

### **Q136: What is currying and how does it work? / Currying কী এবং এটি কীভাবে কাজ করে?**

**Answer (English):**
Currying is a functional programming technique where a function with multiple arguments is transformed into a sequence of nesting functions that each take a **single argument**.
*   `f(a, b, c)` becomes `f(a)(b)(c)`.
*   **Example:**
    ```javascript
    const add = a => b => c => a + b + c;
    console.log(add(1)(2)(3)); // 6
    ```

**অনুবাদ (Bangla Translation):**
কারিইং (Currying) হলো ফাংশনাল প্রোগ্রামিংয়ের একটি কৌশল, যেখানে একাধিক আর্গুমেন্ট যুক্ত একটি ফাংশনকে একের পর এক **একটি মাত্র আর্গুমেন্ট গ্রহণকারী** নেস্টেড ফাংশন চেইনে রূপান্তর করা হয়।
*   `f(a, b, c)` রূপান্তরিত হয় `f(a)(b)(c)`-তে।
*   **উদাহরণ:**
    ```javascript
    const add = a => b => c => a + b + c;
    console.log(add(1)(2)(3)); // ৬
    ```

---

### **Q137: Explain the concept of partial application. / Partial Application ধারণাটি ব্যাখ্যা করুন।**

**Answer (English):**
Partial Application is a technique where a function is bound to **some** of its arguments, producing a new function that takes the remaining arguments. E.g., using `bind()` to lock 1 argument.

**অনুবাদ (Bangla Translation):**
পার্শিয়াল অ্যাপ্লিকেশন হলো একটি ফাংশনের কিছু আর্গুমেন্ট আগে থেকেই নির্দিষ্ট বা লক করে রেখে একটি নতুন ফাংশন তৈরি করা যা কেবল বাকি আর্গুমেন্টগুলো গ্রহণ করবে (যেমন `bind()` দিয়ে ১টি আর্গুমেন্ট লক করা)।

---

### **Q138: What are the benefits of using currying and partial application? / Currying এবং Partial Application ব্যবহারের সুবিধাগুলো কী কী?**

**Answer (English):**
1.  **Reusability:** Helps create highly reusable utility helper functions.
2.  **Modularity:** Encourages clean, composable functional programming code structures.
3.  **Avoids Repetitive Code:** Pre-binds fixed constants to functions.

**অনুবাদ (Bangla Translation):**
1.  **পুনর্ব্যবহারযোগ্যতা:** ছোট ছোট হেল্পার ফাংশন বানিয়ে বারবার রি-ইউজ করা যায়।
2.  **মডুলারিটি:** কোডকে পরিচ্ছন্ন ও ফাংশনাল প্রোগ্রামিং ফ্রেন্ডলি করে।
3.  **কোডের পুনরাবৃত্তি এড়ানো:** ফিক্সড কনস্ট্যান্ট আগে থেকেই ফাংশনে সেট করে রাখা যায়।

---

### **Q139: Provide some examples of how currying and partial application can be used. / Currying এবং Partial Application ব্যবহারের কিছু উদাহরণ দিন।**

**Answer (English):**
*   **Currying Example (Logger):**
    ```javascript
    const log = level => msg => console.log(`[${level}] ${msg}`);
    const errorLog = log('ERROR');
    errorLog('Server Down!'); // [ERROR] Server Down!
    ```
*   **Partial Application Example:**
    ```javascript
    function multiply(a, b) { return a * b; }
    const double = multiply.bind(null, 2);
    console.log(double(5)); // 10
    ```

**অনুবাদ (Bangla Translation):**
*   **Currying উদাহরণ (লগার):**
    ```javascript
    const log = level => msg => console.log(`[${level}] ${msg}`);
    const errorLog = log('ERROR');
    errorLog('Server Down!'); // [ERROR] Server Down!
    ```
*   **Partial Application উদাহরণ:**
    ```javascript
    function multiply(a, b) { return a * b; }
    const double = multiply.bind(null, 2);
    console.log(double(5)); // ১০
    ```

---

### **Q140: How do currying and partial application differ from each other? / Currying এবং Partial Application এর মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Currying:** Strictly transforms a function to take **exactly 1 argument per returned function** in a chain until all arguments are satisfied (`f(a)(b)(c)`).
*   **Partial Application:** Binds a fixed number of arguments (1 or more) at once and returns a function expecting **all remaining arguments at once** (`f(a, b)(c, d)`).

**অনুবাদ (Bangla Translation):**
*   **Currying:** প্রতিটি ফাংশন লেয়ারে বাধ্যতামূলকভাবে **ঠিক ১টি করে আর্গুমেন্ট** রিসিভ করার চেইন তৈরি করে (`f(a)(b)(c)`)।
*   **Partial Application:** একসাথে এক বা একাধিক আর্গুমেন্ট ফিক্সড করে দিয়ে বাকি সমস্থ আর্গুমেন্ট একবারে গ্রহণকারী নতুন ফাংশন বানায় (`f(a, b)(c, d)`)।

---

### **Q141: What are Sets and Maps and how are they used? / Sets এবং Maps কী এবং কীভাবে এগুলো ব্যবহার করা হয়?**

**Answer (English):**
*   **`Set`:** A collection of **unique values** of any data type. Automatically discards duplicates.
    ```javascript
    const set = new Set([1, 2, 2, 3]); // Set(3) { 1, 2, 3 }
    ```
*   **`Map`:** A collection of key-value pairs where **keys can be of any data type** (objects, functions, primitives). Maintains key insertion order.

**অনুবাদ (Bangla Translation):**
*   **`Set`:** যেকোনো ডাটা টাইপের **ইউনিক (অনন্য) মানের কালেকশন**। এটি স্বয়ংক্রিয়ভাবে ডুপ্লিকেট মান বাদ দিয়ে দেয়।
    ```javascript
    const set = new Set([1, 2, 2, 3]); // Set(3) { 1, 2, 3 }
    ```
*   **`Map`:** Key-Value পেয়ারের কালেকশন যেখানে **Key যেকোনো ডাটা টাইপ** (এমনকি অবজেক্ট বা ফাংশন) হতে পারে।

---

### **Q142: What are the differences between Map / Set and WeakMap / WeakSet in JavaScript? / Map/Set এবং WeakMap/WeakSet এর মধ্যে পার্থক্য কী কী?**

**Answer (English):**
1.  **Key/Element Types:** `Map`/`Set` accept any type. `WeakMap`/`WeakSet` accept **only objects**.
2.  **Garbage Collection:** Keys in `WeakMap`/`WeakSet` are held **weakly**. If an object key has no other references in code, it is automatically garbage collected.
3.  **Enumeration:** `Map`/`Set` can be iterated (`forEach`, `keys()`). `WeakMap`/`WeakSet` are non-iterable and have no `.size` property.

**অনুবাদ (Bangla Translation):**
1.  **টাইপ:** `Map`/`Set`-এ যেকোনো টাইপ রাখা যায়। `WeakMap`/`WeakSet`-এ কেবল **অবজেক্ট** রাখা যায়।
2.  **গার্বেজ কালেকশন:** `WeakMap`/`WeakSet`-এর চাবিগুলো **দুর্বলভাবে (Weakly)** যুক্ত থাকে, ফলে বাইরে কোনো রেফারেন্স না থাকলে অবজেক্টগুলো স্বয়ংক্রিয়ভাবে মেমোরি থেকে গার্বেজ কালেক্টেড হয়।
3.  **ইটারেশন:** `Map`/`Set`-এ লুপ চালানো যায়, কিন্তু `WeakMap`/`WeakSet`-এ লুপ চালানো যায় না এবং এদের কোনো `.size` প্রপার্টি নেই।

---

### **Q143: How do you convert a Set to an array in JavaScript? / JavaScript-এ কীভাবে একটি Set-কে অ্যারেতে রূপান্তর করবেন?**

**Answer (English):**
1.  Spread operator: `const arr = [...mySet];`
2.  `Array.from()`: `const arr = Array.from(mySet);`

**অনুবাদ (Bangla Translation):**
1.  স্প্রেড অপারেটর ব্যবহার করে: `const arr = [...mySet];`
2.  `Array.from()` মেথড ব্যবহার করে: `const arr = Array.from(mySet);`

---

### **Q144: What is the difference between a Map object and a plain object in JavaScript? / Map অবজেক্ট এবং প্লেন অবজেক্টের মধ্যে পার্থক্য কী?**

**Answer (English):**
*   **Key Types:** Plain object keys must be Strings/Symbols. Map keys can be *any* type (objects, functions).
*   **Key Ordering:** Maps preserve insertion order strictly. Plain objects do not guarantee clean ordering across all key types.
*   **Size:** Map has a built-in `.size` property. Plain objects require `Object.keys(obj).length`.
*   **Performance:** Map is optimized for frequent additions and deletions.

**অনুবাদ (Bangla Translation):**
*   **Key এর টাইপ:** সাধারণ অবজেক্টের চাবি কেবল String/Symbol হতে পারে। Map-এর চাবি যেকোনো টাইপ (এমনকি অবজেক্ট) হতে পারে।
*   **ক্রম:** Map-এ কি ঢোকানোর ক্রমানুসার বজায় থাকে।
*   **সাইজ:** Map-এ সরাসরি `.size` দিয়ে সাইজ জানা যায়, অবজেক্টে `Object.keys(obj).length` লাগে।

---

### **Q145: How do Sets and Maps handle equality checks for objects? / Sets এবং Maps অবজেক্টের সমতা (equality check) কীভাবে হ্যান্ডেল করে?**

**Answer (English):**
`Set` and `Map` use **Reference Equality** (SameValueZero algorithm) for objects, not deep structural equality. Two different object literals with identical contents `{a: 1}` and `{a: 1}` are treated as **distinct keys/elements** because their memory references differ.

**অনুবাদ (Bangla Translation):**
`Set` এবং `Map` অবজেক্টের কনটেন্ট রিড না করে তাদের **মেমোরি রেফারেন্স (Reference Equality)** দিয়ে তুলনা করে। দুটি আলাদা অবজেক্টে হুবহু একই তথ্য `{a: 1}` থাকলেও মেমোরি এড্রেস আলাদা হওয়ায় তারা আলাদা চাবি হিসেবে গণ্য হবে।

---

### **Q146: What are some common performance bottlenecks in JavaScript applications? / JavaScript অ্যাপ্লিকেশনের সাধারণ পারফরম্যান্স সমস্যা বা Bottleneck-গুলো কী কী?**

**Answer (English):**
1.  **Excessive DOM Manipulation & Layout Thrashing:** Unnecessary reads/writes to DOM.
2.  **Long Running Main Thread Tasks:** Heavy synchronous loops blocking UI updates.
3.  **Memory Leaks:** Uncleared event listeners, detached DOM nodes, forgotten timers.
4.  **Unoptimized Network Requests:** Large uncompressed bundle sizes, lack of caching.

**অনুবাদ (Bangla Translation):**
1.  **অতিরিক্ত ডম ম্যানিপুলেশন:** বারবার ডম রিড/রাইট করে লেআউট স্লো করা।
2.  **মেইন থ্রেড ব্লক করা:** ভারী গণনা মূল থ্রেডে চালিয়ে ইউআই ফ্রিজ করা।
3.  **মেমোরি লিক:** অকেজো ইভেন্ট লিসেনার বা টাইমার মেমোরিতে রেখে দেওয়া।
4.  **বড় বান্ডেল সাইজ:** কোড স্প্লিটিং ও ক্যাশিং না করা।

---

### **Q147: Explain the concept of debouncing and throttling. / Debouncing এবং Throttling ধারণা দুটি ব্যাখ্যা করুন।**

**Answer (English):**
Both are rate-limiting techniques to control how often a function is executed:
*   **Debouncing:** Delays execution until a specified delay has passed **since the last event call**. Resets timer on new calls (e.g., search input autocomplete).
*   **Throttling:** Ensures a function executes **at most once per fixed time interval**, regardless of how many times the event triggers (e.g., scroll/resize listeners).

**অনুবাদ (Bangla Translation):**
উভয়ই ফাংশন কলের গতি নিয়ন্ত্রণ করার পারফরম্যান্স টেকনিক:
*   **Debouncing:** ব্যবহারকারী শেষবার টাইপ করা বন্ধ করার পর নির্দিষ্ট ডিলে পার হলে তবেই ফাংশন কল করে (যেমন- সার্চ বাটন ডাইনামিক ফিল্টার)।
*   **Throttling:** ঘনঘন ইভেন্ট ফায়ার হলেও একটি নির্দিষ্ট সময়ের ব্যবধানে সর্বোচ্চ **একবারই** ফাংশন রান হতে দেয় (যেমন- পেজ স্ক্রলিং বা উইন্ডো রিসাইজিং)।

---

### **Q148: How can you optimize DOM manipulation for better performance? / উন্নত পারফরম্যান্সের জন্য কীভাবে DOM ম্যানিপুলেশন অপ্টিমাইজ করবেন?**

**Answer (English):**
1.  **Batch DOM Updates:** Use `DocumentFragment` to build nodes offline before inserting once.
2.  **Virtual DOM:** Leverage libraries like React.
3.  **Use `requestAnimationFrame()`:** Schedule visual changes right before browser paint.
4.  **Event Delegation:** Reduce listener count on child nodes.

**অনুবাদ (Bangla Translation):**
1.  **ব্যাচ ডম আপডেট:** `DocumentFragment` ব্যবহার করে অফলাইনে নোড বানিয়ে একবারে ডমে পুশ করা।
2.  **ভার্চুয়াল ডম:** React-এর মতো লাইব্রেরি ব্যবহার করা।
3.  **`requestAnimationFrame()` ব্যবহার:** অ্যানিমেশন ও স্টাইল চেঞ্জ পেইন্টিংয়ের আগে শিডিউল করা।
4.  **ইভেন্ট ডেলিগেশন:** আলাদা চাইল্ডে ইভেন্ট না বসিয়ে প্যারেন্টে একটি ইভেন্ট বসানো।

---

### **Q149: What are some techniques for reducing reflows and repaints? / Reflows এবং Repaints কমানোর কৌশলগুলো কী কী?**

**Answer (English):**
*   **Reflow:** Recalculating geometry and layout of elements.
*   **Repaint:** Redrawing pixels on screen.
*   **Techniques to reduce:**
    1.  Avoid reading layout properties (like `offsetHeight`, `getBoundingClientRect`) right after modifying styles.
    2.  Use CSS transforms and opacity (processed on GPU) instead of changing `top`/`left`/`width`.
    3.  Use `will-change` CSS property selectively.

**অনুবাদ (Bangla Translation):**
*   **Reflow:** এলিমেন্টের পজিশন ও লেআউট নতুন করে হিসাব করা।
*   **Repaint:** স্ক্রিনে নতুন পিক্সেল আঁকা।
*   **কমানোর উপায়:**
    1.  স্টাইল পরিবর্তনের সাথে সাথে `offsetHeight` বা `getBoundingClientRect` রিড না করা।
    2.  `top`/`left` না বদলে সিএসএস `transform` ও `opacity` ব্যবহার করা (যা জিপিইউ দিয়ে স্মুথলি চলে)।

---

### **Q150: Explain the concept of lazy loading and how it can improve performance. / Lazy loading ধারণাটি ব্যাখ্যা করুন এবং এটি কীভাবে পারফরম্যান্স উন্নত করে?**

**Answer (English):**
Lazy Loading delays the initialization and loading of non-critical resources (like offscreen images or scripts) until they are actually needed (e.g., scrolled into viewport).
*   **Benefits:** Reduces initial load time, page bundle size, and saves user network data. Implemented natively on images via `loading="lazy"`.

**অনুবাদ (Bangla Translation):**
লেজি লোডিং (Lazy Loading) হলো অ-জরুরি রিসোর্স (যেমন স্ক্রিনের নিচের অংশের ছবি বা মডিউল) পেজ লোডের সময় ডাউনলোড না করে, ইউজার স্ক্রল করে সেই জায়গায় পৌঁছানোর পর লোড করার পদ্ধতি।
*   **সুবিধা:** পেজের প্রারম্ভিক লোডিং টাইম অনেক কমে যায় এবং ডাটা সাশ্রয় হয় (HTML ছবিতে `loading="lazy"` দিয়ে নেটিভালি করা যায়)।
