# HTML5 Interview Questions & Answers (with Bangla Translation)

This guide contains 30 comprehensive, industry-standard interview questions on HTML5, covering semantic markup, web storage, multimedia APIs, form validation, responsiveness, security, and accessibility. Each question has a detailed answer in English followed by a complete Bangla translation.

---

## Table of Contents
1. HTML5 vs HTML4 Key Differences
2. Semantic Elements Definition & Importance
3. Difference between `<section>`, `<article>`, and `<div>`
4. Purpose of `<header>`, `<footer>`, `<nav>`, and `<aside>`
5. Native Audio and Video Support
6. LocalStorage vs SessionStorage
7. IndexedDB Overview
8. Application Cache vs Service Workers
9. Canvas vs SVG
10. Geolocation API
11. Web Workers
12. WebSockets
13. Responsive Images with `<picture>` and `<source>`
14. New Input Types in HTML5
15. HTML5 Form Validation Features
16. `<datalist>` Element
17. Custom Data Attributes (`data-*`)
18. HTML5 Drag and Drop API
19. Script Loading: `async` vs `defer`
20. DOCTYPE Declaration in HTML5
21. `<main>` Tag Usage Constraints
22. `<meter>` vs `<progress>` Elements
23. Server-Sent Events (SSE) vs WebSockets
24. Video Format Fallbacks
25. `<figure>` and `<figcaption>` Elements
26. HTML5 SEO Best Practices
27. Viewport Meta Tag for Responsiveness
28. HTML5 Web Components (Custom Elements, Shadow DOM, Templates)
29. Anchor Tag `download` Attribute
30. Web Accessibility (a11y) and ARIA Roles

---

### **Q1: What is HTML5, and what are its key features compared to HTML4? / HTML5 কী এবং HTML4 এর তুলনায় এর প্রধান বৈশিষ্ট্যসমূহ কী কী?**

**Answer (English):**
HTML5 is the fifth and current major version of the HTML standard. It was designed to deliver rich content without requiring additional plugins like Flash.
*   **Key Features Compared to HTML4:**
    1.  **New Semantic Elements:** Introduces structural tags like `<header>`, `<footer>`, `<article>`, and `<section>` for cleaner structure.
    2.  **Native Multimedia Support:** Built-in `<video>` and `<audio>` tags instead of relying on external Flash plugins.
    3.  **Graphics API:** Native support for vector graphics (SVG) and raster-based drawing (`<canvas>`).
    4.  **Web Storage API:** Local storage (`localStorage`, `sessionStorage`) replacing smaller, less secure HTTP cookies.
    5.  **New Input Attributes:** Features like `type="email"`, `type="date"`, placeholder, and required inputs for simplified form validation.

**অনুবাদ (Bangla Translation):**
HTML5 হলো HTML স্ট্যান্ডার্ডের পঞ্চম এবং বর্তমান সংস্করণ। ফ্ল্যাশের (Flash) মতো কোনো অতিরিক্ত প্লাগ-ইন ছাড়াই ডাইনামিক বা রিচ কন্টেন্ট দেখানোর জন্য এটি ডিজাইন করা হয়েছিল।
*   **HTML4 এর সাথে মূল পার্থক্যসমূহ:**
    1.  **নতুন সিম্যান্টিক এলিমেন্ট:** ক্লিন কাঠামোর জন্য `<header>`, `<footer>`, `<article>`, এবং `<section>` এর মতো ট্যাগ যুক্ত হয়েছে।
    2.  **নেটিভ মাল্টিমিডিয়া সাপোর্ট:** কোনো থার্ড-পার্টি ফ্ল্যাশ প্লাগ-ইন ছাড়াই সরাসরি অডিও ও ভিডিও চালানোর জন্য `<video>` এবং `<audio>` ট্যাগ যুক্ত হয়েছে।
    3.  **গ্রাফিক্স এপিআই:** ভেক্টর গ্রাফিক্স (SVG) এবং রাস্টার ইমেজ ড্রইংয়ের জন্য `<canvas>` ব্যবহার করার সুবিধা দেওয়া হয়েছে।
    4.  **ওয়েব স্টোরেজ এপিআই:** কম সুরক্ষিত এবং ছোট সাইজের HTTP কুকির পরিবর্তে ব্রাউজারে ডেটা স্টোর করতে `localStorage` এবং `sessionStorage` আনা হয়েছে।
    5.  **নতুন ইনপুট অ্যাট্রিবিউট:** সহজ ফর্ম ভ্যালিডেশনের জন্য `type="email"`, `type="date"`, placeholder এবং required ইত্যাদি যুক্ত করা হয়েছে।

---

### **Q2: What are semantic elements in HTML5, and why are they important? / HTML5-এ সিম্যান্টিক এলিমেন্ট কী এবং এগুলো কেন গুরুত্বপূর্ণ?**

**Answer (English):**
Semantic elements are HTML elements that clearly describe their meaning to both the browser and the developer. For example, `<form>`, `<table>`, and `<article>` clearly define what content goes inside them, unlike non-semantic tags like `<div>` and `<span>` which say nothing about their content.
*   **Importance:**
    1.  **Accessibility (a11y):** Screen readers and assistive technologies use semantic tags to navigate the page hierarchy for visually impaired users.
    2.  **SEO (Search Engine Optimization):** Search engine bots understand the content structure better, giving higher priority to keywords found inside semantic tags.
    3.  **Code Readability:** Makes the code clean and easier to maintain for developers, avoiding "div soup" (nested divs).

**অনুবাদ (Bangla Translation):**
সিম্যান্টিক এলিমেন্ট হলো এমন ট্যাগ যা ব্রাউজার এবং ডেভেলপার উভয়ের কাছেই তার নিজের অর্থ ও ভূমিকা পরিষ্কারভাবে প্রকাশ করে। যেমন- `<form>`, `<table>` এবং `<article>` ট্যাগগুলো ভেতরে কী ধরণের কন্টেন্ট আছে তা স্পষ্ট করে, যা নন-সিম্যান্টিক ট্যাগ যেমন `<div>` বা `<span>` দিয়ে বোঝা যায় না।
*   **গুরুত্ব:**
    1.  **অ্যাক্সেসিবিলিটি (a11y):** দৃষ্টিপ্রতিবন্ধী ব্যবহারকারীদের জন্য স্ক্রিন রিডার সহজেই পেজের গঠন ও ন্যাভিগেশন বুঝতে পারে।
    2.  **এসইও (SEO):** সার্চ ইঞ্জিনের ক্রলার বা বট কন্টেন্টের গঠন ও থিম সহজে বুঝতে পারে, যা সার্চ র‍্যাংকিং বৃদ্ধিতে সাহায্য করে।
    3.  **কোড রিডাবিলিটি:** ডেভেলপারদের জন্য কোড পড়তে ও মেইনটেইন করতে সুবিধা হয়, ফলে অহেতুক নেস্টেড ডিভের জটলা তৈরি হয় না।

---

### **Q3: Explain the difference between `<section>`, `<article>`, and `<div>`. / `<section>`, `<article>` এবং `<div>` এর মধ্যে পার্থক্য ব্যাখ্যা করুন।**

**Answer (English):**
*   **`<article>`**: Represents a self-contained, independent composition in a document, page, application, or site, which is intended to be independently distributable or reusable (e.g., a blog post, forum post, or news article).
*   **`<section>`**: Represents a thematic grouping of content, typically with a heading. It is used to split a page or article into distinct logical sections (e.g., "About Us" section, "Features" section).
*   **`<div>`**: A generic block-level container with no semantic meaning. It should only be used as a last resort for CSS styling or DOM manipulation purposes when no semantic tag fits.

**অনুবাদ (Bangla Translation):**
*   **`<article>`**: এটি একটি সম্পূর্ণ স্বাধীন ও স্বয়ংসম্পূর্ণ কন্টেন্ট ব্লক নির্দেশ করে, যা অন্য কোনো পেজের সাহায্য ছাড়া নিজেই নিজের অর্থ প্রকাশ করতে পারে এবং যা অন্য কোথাও পুনরায় শেয়ার বা প্রকাশ করা সম্ভব (যেমন: ব্লগ পোস্ট, ফোরাম পোস্ট, সংবাদ)।
*   **`<section>`**: এটি সাধারণত একটি হেডিং সহ কোনো কন্টেন্টের থিমেটিক গ্রুপ বা বড় অংশকে ভাগ করতে ব্যবহৃত হয় (যেমন: "আমাদের সম্পর্কে" সেকশন, "সার্ভিসেস" সেকশন)।
*   **`<div>`**: এটি কোনো সিম্যান্টিক অর্থহীন সাধারণ ব্লক-লেভেল কন্টেইনার। এর নিজস্ব কোনো মানে নেই, এটি কেবল সিএসএস স্টাইলিং বা জাভাস্ক্রিপ্ট ডম ম্যানিপুলেশনের সুবিধার্থে গ্রুপিং করতে ব্যবহৃত হয়।

---

### **Q4: What is the purpose of `<header>`, `<footer>`, `<nav>`, and `<aside>`? / `<header>`, `<footer>`, `<nav>`, এবং `<aside>` এর উদ্দেশ্য কী?**

**Answer (English):**
*   **`<header>`**: Represents introductory content or a set of navigational links. It usually contains headings, logos, search forms, or author names.
*   **`<footer>`**: Contains information about its containing element, typically placed at the bottom. It holds copyright data, links to terms of use, privacy policies, or contact details.
*   **`<nav>`**: Defines a block of major navigation links (links to other pages or sections of the current page).
*   **`<aside>`**: Represents content that is tangentially related to the main content (e.g., sidebars, advertising banners, call-out boxes).

**অনুবাদ (Bangla Translation):**
*   **`<header>`**: এটি পেজ বা কোনো আর্টিকেলের ভূমিকা বা পরিচিতিমূলক অংশ নির্দেশ করে। সাধারণত এতে লোগো, শিরোনাম, সার্চ ইনপুট বা রাইটারের নাম থাকে।
*   **`<footer>`**: এটি সাধারণত পেজের নিচে থাকে এবং কপিরাইট ইনফরমেশন, টার্মস অ্যান্ড পলিসি লিংক, স্যোশাল মিডিয়া লিংক বা কন্টাক্ট ইনফরমেশন ধারণ করে।
*   **`<nav>`**: এটি সাইটের মূল ন্যাভিগেশন লিংকগুলোর জন্য ব্লক বা বার নির্ধারণ করতে ব্যবহৃত হয়।
*   **`<aside>`**: এটি মূল বিষয়ের বাইরে সাইড কন্টেন্ট বা আনুসঙ্গিক তথ্য যেমন সাইডবার, বিজ্ঞাপন, বা কুইক লিংক দেখানোর জন্য ব্যবহৃত হয়।

---

### **Q5: How does the HTML5 `<audio>` and `<video>` integration work without external plug-ins? / কোনো এক্সটারনাল প্লাগ-ইন ছাড়া HTML5-এ `<audio>` এবং `<video>` ইন্টিগ্রেশন কীভাবে কাজ করে?**

**Answer (English):**
Before HTML5, web browsers required plugins like Adobe Flash or Silverlight to play audio and video. HTML5 introduced native `<audio>` and `<video>` elements, which are treated just like regular DOM nodes.
*   **Example Syntax:**
    ```html
    <video width="640" height="360" controls>
      <source src="movie.mp4" type="video/mp4">
      <source src="movie.ogg" type="video/ogg">
      Your browser does not support the video tag.
    </video>
    ```
*   **Attributes:**
    *   `controls`: Displays play/pause, volume, and fullscreen options.
    *   `autoplay`: Plays media automatically upon loading.
    *   `loop`: Repeats the media.
    *   `muted`: Starts the media with sound turned off.

**অনুবাদ (Bangla Translation):**
HTML5 এর আগে ব্রাউজারে অডিও-ভিডিও চালানোর জন্য এডোবি ফ্ল্যাশ প্লেয়ার (Adobe Flash) বা সিলভারলাইটের মতো প্লাগ-ইন লাগত। HTML5 সরাসরি ব্রাউজারে নেটিভ `<audio>` এবং `<video>` এলিমেন্ট যুক্ত করেছে, যা ডম নোডের মতো কাজ করে।
*   **সিনট্যাক্স উদাহরণ:**
    ```html
    <video width="640" height="360" controls>
      <source src="movie.mp4" type="video/mp4">
      <source src="movie.ogg" type="video/ogg">
      আপনার ব্রাউজারটি ভিডিও ট্যাগ সাপোর্ট করে না।
    </video>
    ```
*   **অ্যাট্রিবিউটসমূহ:**
    *   `controls`: প্লে/পজ, সাউন্ড ও ফুলস্ক্রিন বাটন দেখায়।
    *   `autoplay`: পেজ লোড হওয়ার সাথে সাথে মিডিয়া অটোমেটিকালি চালু করে।
    *   `loop`: মিডিয়াটি বারবার লুপে চালাতে থাকে।
    *   `muted`: ডিফল্টভাবে সাউন্ড অফ বা মিউট করে রাখে।

---

### **Q6: What are HTML5 Web Storage APIs? Explain the difference between `localStorage` and `sessionStorage`. / HTML5 ওয়েব স্টোরেজ এপিআই কী? `localStorage` এবং `sessionStorage` এর মধ্যে পার্থক্য ব্যাখ্যা করুন।**

**Answer (English):**
Web Storage APIs allow web applications to store key-value data directly in the user's browser, providing a capacity of up to 5MB–10MB (much larger than 4KB cookies) without sending data to the server on every request.
*   **Differences:**

| Feature | `localStorage` | `sessionStorage` |
| :--- | :--- | :--- |
| **Data Expiry** | Never expires unless deleted manually. | Cleared when the tab or window is closed. |
| **Scope** | Available across all tabs/windows of the same origin. | Restrictive to the specific tab where it was created. |
| **Use Case** | User settings, theme mode preference. | Temporary form data, single session states. |

**অনুবাদ (Bangla Translation):**
ওয়েব স্টোরেজ এপিআই ব্রাউজারে সরাসরি Key-Value আকারে ডেটা স্টোর করতে সাহায্য করে। এটি প্রায় ৫ থেকে ১০ মেগাবাইট পর্যন্ত ডেটা ধারণ করতে পারে (যা ৪ কিলোবাইটের কুকির চেয়ে অনেক বড়) এবং প্রতিটি সার্ভার রিকোয়েস্টে এই ডেটা অপ্রয়োজনে ট্রাভেল করে না।
*   **পার্থক্যসমূহ:**

| বৈশিষ্ট্য | `localStorage` | `sessionStorage` |
| :--- | :--- | :--- |
| **ডেটার স্থায়িত্ব** | ইউজার নিজে থেকে রিমুভ না করা পর্যন্ত মেমোরিতে থাকে। | ব্রাউজার ট্যাব বা উইন্ডো বন্ধ করলেই মুছে যায়। |
| **স্কোপ/সীমানা** | একই অরিজিনের সব ট্যাব ও উইন্ডোতে ডেটা পাওয়া যায়। | শুধুমাত্র যে ট্যাবে ডেটা তৈরি হয়েছে, সেখানেই সীমাবদ্ধ থাকে। |
| **ব্যবহার ক্ষেত্র** | ইউজার সেটিংস, ডার্ক মোড প্রেফারেন্স সেভ রাখতে। | ওয়ান-টাইম ফর্ম ফিলআপের তথ্য, এক সেশনের টেম্পোরারি স্টেট। |

---

### **Q7: What is IndexedDB in HTML5, and when should it be used over Web Storage? / HTML5-এ IndexedDB কী, এবং ওয়েব স্টোরেজের তুলনায় এটি কখন ব্যবহার করা উচিত?**

**Answer (English):**
`IndexedDB` is a low-level API for client-side storage of significant amounts of structured data, including files and blobs. It is a transactional, object-oriented database system built into the browser.
*   **When to use IndexedDB over Web Storage:**
    1.  **Large Datasets:** Web Storage is limited to ~5MB. IndexedDB can hold hundreds of megabytes (up to a percentage of disk space).
    2.  **Complex Queries:** It supports indexes for searching, sorting, and complex querying of objects, unlike LocalStorage which only stores strings.
    3.  **Asynchronous Nature:** IndexedDB operates asynchronously, ensuring that large database operations do not block the browser's UI thread.

**অনুবাদ (Bangla Translation):**
`IndexedDB` হলো ব্রাউজারের ভেতর বিল্ট-ইন ফাইল ও ব্লগ সহ প্রচুর পরিমাণে স্ট্রাকচার্ড ডেটা ক্লায়েন্ট-সাইডে স্টোর করার জন্য একটি লো-লেভেল এপিআই। এটি একটি ট্রানজ্যাকশনাল, অবজেক্ট-ওরিয়েন্টেড ডেটাবেজ সিস্টেম।
*   **ওয়েব স্টোরেজের তুলনায় কখন IndexedDB ব্যবহার করবেন:**
    1.  **বিশাল ডেটাবেজ:** ওয়েব স্টোরেজের ক্ষমতা সর্বোচ্চ ৫ মেগাবাইট। IndexedDB হার্ডডিস্কের ধারণক্ষমতার উল্লেখযোগ্য শতাংশ পর্যন্ত স্পেস নিতে পারে।
    2.  **জটিল সার্চ কোয়েরি:** এটি ইনডেক্সিং সাপোর্ট করে যার ফলে অবজেক্ট সর্টিং ও কুয়েরি করা যায়, যা লোকাল স্টোরেজে করা যায় না (লোকাল স্টোরেজ শুধু স্ট্রিং সেভ করে)।
    3.  **অ্যাসিনক্রোনাস আর্কিটেকচার:** এটি ব্যাকগ্রাউন্ডে অ্যাসিনক্রোনাসলি চলে, তাই ডেটাবেজ অপারেশনের সময় ব্রাউজার থ্রেড হ্যাং বা ব্লক হয় না।

---

### **Q8: Explain HTML5 Application Cache (AppCache) vs Service Workers. / HTML5 অ্যাপ্লিকেশন ক্যাশ (AppCache) এবং সার্ভিস ওয়ার্কার্স (Service Workers) এর মধ্যে পার্থক্য ব্যাখ্যা করুন।**

**Answer (English):**
*   **Application Cache (AppCache):** Deprecated. It used a flat manifest file (`manifest.appcache`) to define offline files. It was hard to configure, buggy, and had major issues with dynamic data updating.
*   **Service Workers:** The modern HTML5 standard for offline-first support. It is a script that the browser runs in the background, separate from the web page.
*   **Key Differences:**
    *   Service Workers act as a network proxy, giving developers granular JavaScript-based control over how caching works, routing intercept, and offline push notifications. AppCache was declarative and rigid.

**অনুবাদ (Bangla Translation):**
*   **Application Cache (AppCache):** এটি বর্তমানে বাতিল (Deprecated)। অফলাইনে ফাইল ক্যাশ করার জন্য এতে একটি ম্যানিফেস্ট ফাইল ব্যবহার করা হতো, যা কনফিগার করা খুব কঠিন ছিল এবং ডাইনামিক ডেটা আপডেটে বাগ তৈরি করত।
*   **Service Workers:** এটি অফলাইন ও PWA (Progressive Web App) সাপোর্টের জন্য আধুনিক স্ট্যান্ডার্ড। এটি একটি ব্যাকগ্রাউন্ড স্ক্রিপ্ট যা মূল ওয়েব পেজের থ্রেড থেকে আলাদাভাবে চলে।
*   **মূল পার্থক্য:** Service Worker একটি নেটওয়ার্ক প্রক্সি হিসেবে কাজ করে, যা ডেভেলপারদের জাভাস্ক্রিপ্ট দিয়ে ক্যাশিং অপ্টিমাইজেশন ও এপিআই রিকোয়েস্ট ইন্টারসেপ্ট করার পূর্ণ নিয়ন্ত্রণ দেয়। অন্য দিকে AppCache ছিল ফিক্সড ও ডিক্লেয়ারেটিভ।

---

### **Q9: What is the HTML5 `<canvas>` element, and how does it differ from SVG? / HTML5-এ `<canvas>` এলিমেন্ট কী এবং এটি SVG থেকে কীভাবে আলাদা?**

**Answer (English):**
The HTML5 `<canvas>` element provides a container to draw graphics on the fly via JavaScript scripts (raster-based).
*   **Differences:**

| Feature | `<canvas>` | SVG |
| :--- | :--- | :--- |
| **Rendering Type** | Raster (pixels). Resolution-dependent. | Vector (XML-based). Resolution-independent (scales cleanly). |
| **Performance** | Excellent for drawing intensive games or animations with 1000s of objects. | Tends to slow down if there are thousands of DOM nodes. |
| **DOM Interaction** | Not accessible via DOM tree (no click events on drawn objects). | Fully part of the DOM tree (supports CSS styling and event listeners). |

**অনুবাদ (Bangla Translation):**
HTML5 এর `<canvas>` এলিমেন্টটি মূলত জাভাস্ক্রিপ্টের স্ক্রিপ্ট রান করে অন-দ্য-ফ্লাই পিক্সেল আর্ট বা রাস্টার গ্রাফিক্স আঁকার জন্য একটি ফাঁকা কন্টেইনার দেয়।
*   **পার্থক্যসমূহ:**

| বৈশিষ্ট্য | `<canvas>` | SVG |
| :--- | :--- | :--- |
| **রেন্ডারিং টাইপ** | রাস্টার বা পিক্সেল-বেসড। জুম করলে ফেটে যায়। | ভেক্টর (XML-বেসড)। জুম করলে নিখুঁত থাকে। |
| **পারফরম্যান্স** | জটিল গেম বা হাজার হাজার পিক্সেল অ্যানিমেশনের জন্য বেস্ট। | অনেক বেশি ডম এলিমেন্ট হয়ে গেলে পারফরম্যান্স কমে যায়। |
| **ডম ইন্টারঅ্যাকশন** | এর ভেতরের এলিমেন্ট ডমের অংশ নয় (ক্লিক ইভেন্ট দেওয়া যায় না)। | প্রতিটি এলিমেন্ট ডম ট্রির অংশ (CSS স্টাইল ও ইভেন্ট লিসেনার সাপোর্ট করে)। |

---

### **Q10: What is HTML5 Geolocation API, and how do you use it? / HTML5 জিওলোকেশন এপিআই কী এবং এটি কীভাবে ব্যবহার করবেন?**

**Answer (English):**
The HTML5 Geolocation API allows users to share their geographic coordinates (latitude and longitude) with web applications. For privacy reasons, the user must explicitly grant permission.
*   **Basic Code Example:**
    ```javascript
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        console.log("Latitude:", position.coords.latitude);
        console.log("Longitude:", position.coords.longitude);
      }, (error) => {
        console.error("Error Code:", error.code);
      });
    }
    ```

**অনুবাদ (Bangla Translation):**
HTML5 জিওলোকেশন এপিআই ব্যবহারকারীকে তার ভৌগোলিক অবস্থান (অক্ষাংশ ও দ্রাঘিমাংশ) ওয়েব অ্যাপ্লিকেশনের সাথে শেয়ার করার অনুমতি দেয়। সুরক্ষার স্বার্থে ব্রাউজারে ইউজারকে অবশ্যই পপআপে "Allow" বাটনে ক্লিক করতে হয়।
*   **কোড উদাহরণ:**
    ```javascript
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition((position) => {
        console.log("অক্ষাংশ:", position.coords.latitude);
        console.log("দ্রাঘিমাংশ:", position.coords.longitude);
      }, (error) => {
        console.error("এরর কোড:", error.code);
      });
    }
    ```

---

### **Q11: What are Web Workers in HTML5, and why are they useful? / HTML5-এ ওয়েব ওয়ার্কার্স কী এবং এগুলো কেন দরকারী?**

**Answer (English):**
JavaScript is single-threaded. Web Workers allow running script calculations in background threads separate from the main browser execution thread.
*   **Why they are useful:**
    *   They prevent UI blocking. For long-running operations (like heavy image processing, large dataset sorting, or cryptography tasks), running them in a Web Worker ensures the user interface remains responsive and fluid.
    *   They communicate with the main thread using messages via `postMessage()` and the `onmessage` listener.

**অনুবাদ (Bangla Translation):**
জাভাস্ক্রিপ্ট একটি সিঙ্গেল-থ্রেডেড ল্যাঙ্গুয়েজ। ওয়েব ওয়ার্কার্স ব্রাউজারের মূল এক্সিকিউশন থ্রেড বা ইউআই থ্রেড থেকে আলাদা একটি ব্যাকগ্রাউন্ড থ্রেড তৈরি করে ভারী স্ক্রিপ্ট বা গণনা সম্পন্ন করতে সাহায্য করে।
*   **কেন দরকারী:**
    *   এটি ইউআই ব্লকিং হওয়া রোধ করে। দীর্ঘ সময় ধরে চলা কোনো হিসাব (যেমন- ছবি প্রসেসিং, বড় ডাটা সর্টিং বা ক্রিপ্টোগ্রাফি) ব্যাকগ্রাউন্ডে পাঠিয়ে দিলে ব্যবহারকারী স্ক্রিনে ল্যাগ ছাড়াই সাবলীলভাবে স্ক্রল বা ক্লিক করতে পারেন।
    *   এরা মেইন থ্রেডের সাথে `postMessage()` এবং `onmessage` ইভেন্ট লিসেনারের মাধ্যমে ডাটা আদান-প্রদান করে।

---

### **Q12: What is WebSockets in HTML5, and how does it enable real-time communication? / HTML5-এ ওয়েব সকেট কী এবং এটি কীভাবে রিয়েল-টাইম যোগাযোগের সুবিধা দেয়?**

**Answer (English):**
The HTML5 WebSocket API establishes a persistent, full-duplex (two-way) TCP connection between the client browser and the server.
*   **How it enables real-time communication:**
    *   Traditional HTTP is unidirectional (client requests, server responds, then connection closes). WebSockets allow the server to push messages directly to the client at any time without the client having to continuously poll the server.
*   **Basic Syntax:**
    ```javascript
    const socket = new WebSocket('ws://example.com/socket');
    socket.onopen = () => socket.send('Hello Server!');
    socket.onmessage = (event) => console.log('Received:', event.data);
    ```

**অনুবাদ (Bangla Translation):**
HTML5 ওয়েব সকেট এপিআই হলো ক্লায়েন্ট ব্রাউজার এবং সার্ভারের মধ্যে একটি দীর্ঘস্থায়ী, ফুল-ডুপ্লেক্স (উভয়মুখী) টিসিপি সংযোগ স্থাপনকারী মেকানিজম।
*   **কীভাবে রিয়েল-টাইম যোগাযোগ করে:**
    *   প্রথাগত HTTP কানেকশন হলো একমুখী (ক্লায়েন্ট রিকোয়েস্ট পাঠাবে এবং সার্ভার উত্তর দিয়ে কানেকশন বন্ধ করে দেবে)। কিন্তু ওয়েব সকেট সার্ভারকে যেকোনো মুহূর্তে ক্লায়েন্টের কাছে সরাসরি নতুন ডাটা পুশ করার ক্ষমতা দেয়, ফলে ক্লায়েন্টকে বারবার সার্ভার পোল করতে হয় না।
*   **সিনট্যাক্স উদাহরণ:**
    ```javascript
    const socket = new WebSocket('ws://example.com/socket');
    socket.onopen = () => socket.send('হ্যালো সার্ভার!');
    socket.onmessage = (event) => console.log('প্রাপ্ত ডাটা:', event.data);
    ```

---

### **Q13: Explain the purpose of `<picture>` and `<source>` elements for responsive images. / রেসপন্সিভ ইমেজের জন্য `<picture>` এবং `<source>` এলিমেন্টগুলোর উদ্দেশ্য ব্যাখ্যা করুন।**

**Answer (English):**
The `<picture>` element is a wrapper that contains one or more `<source>` elements and one `<img>` element. It enables **art direction** for responsive design.
*   **Purpose:**
    *   Allows the browser to load different image sizes or crops based on device screen characteristics (using media queries like max-width).
    *   Enables modern image formats (like WebP/AVIF) while providing a fallback (JPEG/PNG) for older browsers.
*   **Example Syntax:**
    ```html
    <picture>
      <source media="(max-width: 600px)" srcset="small.jpg">
      <source media="(max-width: 1200px)" srcset="medium.jpg">
      <img src="large.jpg" alt="Dynamic Landscape">
    </picture>
    ```

**অনুবাদ (Bangla Translation):**
`<picture>` এলিমেন্ট হলো একটি র্যাপার কন্টেইনার যার ভেতরে এক বা একাধিক `<source>` এলিমেন্ট এবং একটি `<img>` এলিমেন্ট থাকে। এটি রেসপন্সিভ ডিজাইনে **Art Direction** নিয়ন্ত্রণ করতে সাহায্য করে।
*   **উদ্দেশ্য:**
    *   ডিভাইসের স্ক্রিন সাইজ (মিডিয়া কুয়েরির ওপর ভিত্তি করে) অনুযায়ী আলাদা রেজোলিউশন বা ক্রপ করা সাইজের ছবি ব্রাউজারকে স্বয়ংক্রিয়ভাবে লোড করতে দেয়।
    *   আধুনিক হাই-কম্প্রেসড ইমেজ ফরম্যাট (যেমন- WebP/AVIF) ব্যবহারের সুযোগ দেয় এবং পুরাতন ব্রাউজারের জন্য ব্যাকআপ বা ফলব্যাক হিসেবে সাধারণ JPEG/PNG ছবি লোড করে।
*   **সিনট্যাক্স উদাহরণ:**
    ```html
    <picture>
      <source media="(max-width: 600px)" srcset="small.jpg">
      <source media="(max-width: 1200px)" srcset="medium.jpg">
      <img src="large.jpg" alt="ডাইনামিক ল্যান্ডস্কেপ">
    </picture>
    ```

---

### **Q14: What are new input types introduced in HTML5? / HTML5-এ যুক্ত হওয়া নতুন ইনপুট টাইপগুলো কী কী?**

**Answer (English):**
HTML5 introduced several new forms and input types to improve user experience on mobile devices and reduce the reliance on custom JavaScript calendars or validators.
*   **New Input Types:**
    *   `email`: Requires entry to match standard email structures.
    *   `url`: Validates correct web URL syntax.
    *   `number`: Shows a numeric keypad on mobile devices and limits values.
    *   `range`: Renders a slider selector.
    *   `date` / `time` / `datetime-local`: Triggers native OS calendar/time pickers.
    *   `color`: Opens the OS color picker.
    *   `search`: Styles input search bars specifically.

**অনুবাদ (Bangla Translation):**
HTML5 ফর্ম হ্যান্ডলিং উন্নত করতে এবং অতিরিক্ত জাভাস্ক্রিপ্ট ক্যালেন্ডার/ভ্যালিডেটর এড়াতে বেশ কিছু নতুন ইনপুট টাইপ যুক্ত করেছে, যা মোবাইল ডিভাইসের ইউজার এক্সপেরিয়েন্সকে অনেক সমৃদ্ধ করে।
*   **নতুন ইনপুট টাইপসমূহ:**
    *   `email`: ইনপুটের টেক্সট ইমেইল ফরম্যাটের হতে হবে।
    *   `url`: সঠিক ওয়েব ইউআরএল ফরম্যাট ইনপুট নিশ্চিত করে।
    *   `number`: মোবাইলে সরাসরি নম্বর প্যাড দেখায় এবং লিমিট সেট করার সুযোগ দেয়।
    *   `range`: একটি স্লাইডার কন্ট্রোল দেখায়।
    *   `date` / `time` / `datetime-local`: ব্রাউজারের নিজস্ব বিল্ট-ইন ক্যালেন্ডার বা ঘড়ি দেখায়।
    *   `color`: কালার প্যালেট সিলেকশন করার উইন্ডো খোলে।
    *   `search`: সার্চ কুয়েরি ইনপুটের জন্য স্টাইলড বার দেয়।

---

### **Q15: Explain HTML5 form validation features like `required`, `pattern`, and `novalidate`. / HTML5 ফর্ম ভ্যালিডেশন ফিচার যেমন `required`, `pattern`, এবং `novalidate` ব্যাখ্যা করুন।**

**Answer (English):**
HTML5 introduces native client-side validation using attributes, removing the need for manual JavaScript checks for simple validation states.
*   **`required`**: Boolean attribute that prevents form submission if the input field is empty.
*   **`pattern`**: Accepts a regular expression (regex) that the input's value must match (e.g., `pattern="[A-Za-z]{3}"` forces a 3-letter string).
*   **`novalidate`**: Put on the `<form>` element to bypass all browser-native validations (useful when you want to handle all validation logic with a custom library).

**অনুবাদ (Bangla Translation):**
HTML5 ভ্যারিয়েবল চেকিং ও স্ক্রিপ্টিং ছাড়াই ব্রাউজারে বিল্ট-ইন ও নেটিভ ক্লায়েন্ট-সাইড ফর্ম ভ্যালিডেশন করার সুবিধা এনেছে।
*   **`required`**: এই অ্যাট্রিবিউটটি দিলে ইনপুট ফিল্ড খালি রেখে ফর্ম সাবমিট করা যাবে না।
*   **`pattern`**: এটি একটি রেগুলার এক্সপ্রেশন (Regex) গ্রহণ করে, ইনপুটের টেক্সটকে হুবহু ওই প্যাটার্নের সাথে মিলতে হয় (যেমন- `pattern="[A-Za-z]{3}"` ৩টি ইংরেজি অক্ষর ইনপুট নেওয়া বাধ্যতামূলক করে)।
*   **`novalidate`**: এটি `<form>` ট্যাগে বসালে ব্রাউজারের ডিফল্ট ভ্যালিডেশন চেকগুলো বন্ধ হয়ে যায় (যখন আপনি নিজে কাস্টম কোনো লাইব্রেরি দিয়ে ভ্যালিডেশন করতে চান)।

---

### **Q16: What is the `<datalist>` element, and how is it used? / `<datalist>` এলিমেন্ট কী এবং এর ব্যবহার কীভাবে হয়?**

**Answer (English):**
The `<datalist>` element provides an autocomplete drop-down list of predefined options for an `<input>` element. It allows users to select from a list of options or type a custom string.
*   **Example Syntax:**
    ```html
    <input list="browsers" name="browser">
    <datalist id="browsers">
      <option value="Chrome">
      <option value="Firefox">
      <option value="Safari">
    </datalist>
    ```
*   **Benefit:** Unlike a `<select>` dropdown, `<datalist>` allows the user to filter and type custom values that are not in the predefined list.

**অনুবাদ (Bangla Translation):**
`<datalist>` এলিমেন্টটি কোনো সাধারণ `<input>` ফিল্ডের সাথে যুক্ত হয়ে অটোকম্প্লিট এবং সাজেস্টেড ড্রপডাউন অপশন দেখায়। ব্যবহারকারী চাইলে লিস্ট থেকে সিলেক্ট করতে পারেন অথবা নিজের মতো কাস্টম টেক্সট লিখতে পারেন।
*   **সিনট্যাক্স উদাহরণ:**
    ```html
    <input list="browsers" name="browser">
    <datalist id="browsers">
      <option value="Chrome">
      <option value="Firefox">
      <option value="Safari">
    </datalist>
    ```
*   **সুবিধা:** সাধারণ `<select>` ড্রপডাউনের সাথে এর তফাত হলো, এখানে ইউজার ডাটা টাইপ করে অপশন ফিল্টার করতে পারেন এবং লিস্টের বাইরের নতুন কোনো তথ্যও ইনপুট করতে পারেন।

---

### **Q17: What are custom data attributes (`data-*`) in HTML5, and how do you access them? / HTML5-এ কাস্টম ডাটা অ্যাট্রিবিউট (`data-*`) কী এবং কীভাবে এগুলো অ্যাক্সেস করবেন?**

**Answer (English):**
Custom data attributes (`data-*`) allow storing custom application data directly on HTML elements, which can later be accessed via JavaScript or used for CSS styling.
*   **Example Syntax:**
    ```html
    <div id="user-card" data-user-role="admin" data-id="987">Rohit</div>
    ```
*   **Accessing in JavaScript:**
    Use the element's `dataset` property (the custom attribute names are camelCased):
    ```javascript
    const card = document.getElementById("user-card");
    console.log(card.dataset.userRole); // Prints: admin
    console.log(card.dataset.id);       // Prints: 987
    ```

**অনুবাদ (Bangla Translation):**
কাস্টম ডাটা অ্যাট্রিবিউট (`data-*`) কোনো HTML এলিমেন্টের ভেতরে নিজস্ব ডাটা বা প্রপার্টি স্টোর করতে সাহায্য করে, যা পরবর্তীতে জাভাস্ক্রিপ্ট দিয়ে রিড করা যায় বা সিএসএস দিয়ে স্টাইল করা যায়।
*   **সিনট্যাক্স উদাহরণ:**
    ```html
    <div id="user-card" data-user-role="admin" data-id="987">Rohit</div>
    ```
*   **জাভাস্ক্রিপ্টে অ্যাক্সেস করার উপায়:**
    এলিমেন্টের `dataset` প্রপার্টি ব্যবহারের মাধ্যমে (এখানে ড্যাশড নামগুলো camelCase-এ রূপান্তরিত হয়):
    ```javascript
    const card = document.getElementById("user-card");
    console.log(card.dataset.userRole); // আউটপুট: admin
    console.log(card.dataset.id);       // আউটপুট: 987
    ```

---

### **Q18: Explain the HTML5 Drag and Drop API and its main event handlers. / HTML5 ড্র্যাগ অ্যান্ড ড্রপ এপিআই এবং এর প্রধান ইভেন্ট হ্যান্ডলারগুলো ব্যাখ্যা করুন।**

**Answer (English):**
HTML5 introduced native support to make any element draggable on a web page using the `draggable="true"` attribute.
*   **Key Event Handlers:**
    *   **On Draggable Item:**
        *   `ondragstart`: Fires when the user starts dragging the element (use `event.dataTransfer.setData` to store data).
        *   `ondrag`: Fires continuously as the item is dragged.
    *   **On Drop Zone (Target):**
        *   `ondragover`: Fires when the dragged item is over the target (must call `event.preventDefault()` to allow drop).
        *   `ondrop`: Fires when the dragged item is released on the drop target.

**অনুবাদ (Bangla Translation):**
HTML5-এ `draggable="true"` অ্যাট্রিবিউটটি ব্যবহার করে যেকোনো ওয়েব এলিমেন্টকে মাউস দিয়ে টেনে এক স্থান থেকে অন্য স্থানে নিয়ে যাওয়ার (Drag and Drop) নেটিভ সুবিধা দেওয়া হয়েছে।
*   **প্রধান ইভেন্ট হ্যান্ডলারসমূহ:**
    *   **টেনে নেওয়া এলিমেন্টের ক্ষেত্রে (Draggable):**
        *   `ondragstart`: ড্র্যাগ করা শুরু করার মুহূর্তে ট্রিগার হয় (এখানে `event.dataTransfer.setData` দিয়ে ডেটা সেভ করা হয়)।
        *   `ondrag`: ড্র্যাগ করা অবস্থায় অনবরত ফায়ার হতে থাকে।
    *   **ফেলে দেওয়ার জায়গার ক্ষেত্রে (Drop Zone):**
        *   `ondragover`: ড্র্যাগড আইটেমটি ড্রপ জোনের ওপরে থাকার সময় ফায়ার হয় (ড্রপ সফল করতে এখানে `event.preventDefault()` কল করা বাধ্যতামূলক)।
        *   `ondrop`: মাউস রিলিজ বা ছেড়ে দিলে ড্রপ সম্পন্ন হওয়ার মুহূর্তে ফায়ার হয়।

---

### **Q19: What is the difference between `defer` and `async` attributes in the `<script>` tag? / `<script>` ট্যাগে `defer` and `async` অ্যাট্রিবিউটের মধ্যে পার্থক্য কী?**

**Answer (English):**
Both `defer` and `async` allow external scripts to download asynchronously without blocking the HTML parsing. However, their execution cycles differ:
*   **`async` (Asynchronous):** The script executes immediately after it finishes downloading. This pauses HTML parsing. Order of execution is not guaranteed (runs whichever loads first). Use for independent third-party scripts (like Google Analytics).
*   **`defer` (Deferred):** The script executes only after the HTML document parsing is fully completed. Scripts execute in the exact order they are defined in the markup. Use when the script depends on DOM elements or other scripts.

**অনুবাদ (Bangla Translation):**
`defer` এবং `async` উভয় অ্যাট্রিবিউটই মূল HTML পার্সিং ব্লক না করে ব্যাকগ্রাউন্ডে স্ক্রিপ্ট ডাউনলোড করার সুবিধা দেয়। তবে এদের রান করার সময়ে তফাৎ রয়েছে:
*   **`async`**: স্ক্রিপ্ট ডাউনলোড শেষ হওয়া মাত্রই তা সাথে সাথে রান হয়ে যায়। এর ফলে রান হওয়ার মুহূর্তে মূল HTML পার্সিং সাময়িকভাবে বন্ধ থাকে। ডিক্লেয়ার করা ক্রম অনুযায়ী রান হওয়ার গ্যারান্টি নেই (যেটি আগে ডাউনলোড হবে সেটি আগে রান করবে)। গুগল অ্যানালিটিক্সের মতো স্বাধীন স্ক্রিপ্টে এটি ব্যবহৃত হয়।
*   **`defer`**: স্ক্রিপ্টটি ডাউনলোড হলেও তা রান হবে না যতক্ষণ না সম্পূর্ণ HTML ডকুমেন্টের লোড ও রিড সম্পন্ন হয়। এটি ফাইলের লেখার সিকোয়েন্স বা ক্রম বজায় রেখে রান হয়। ডম এলিমেন্টের ওপর নির্ভরশীল স্ক্রিপ্টগুলোতে এটি ব্যবহৃত হয়।

---

### **Q20: What is the purpose of the `<!DOCTYPE html>` declaration in HTML5? / HTML5-এ `<!DOCTYPE html>` ডিক্লারেশনের উদ্দেশ্য কী?**

**Answer (English):**
The `<!DOCTYPE html>` declaration at the top of an HTML document is not an HTML tag; it is an instruction to the web browser about what version of HTML the page is written in.
*   **Purpose in HTML5:**
    1.  It triggers **Standards Mode** in modern browsers, ensuring the page renders consistently according to official standards.
    2.  If omitted, browsers may render the page in **Quirks Mode**, which emulates layout behaviors of very old browsers (like IE6) to prevent breaking legacy sites, causing display bugs.
    3.  It is short and simple in HTML5 compared to the long, complex system identifier paths of HTML4/XHTML doctypes.

**অনুবাদ (Bangla Translation):**
HTML ফাইলের সবার ওপরে থাকা `<!DOCTYPE html>` ডিক্লারেশনটি কোনো HTML ট্যাগ নয়; এটি ব্রাউজারের উদ্দেশ্যে পাঠানো একটি ডিরেক্টিভ যা নির্ধারণ করে পেজটি কোন সংস্করণে লেখা হয়েছে।
*   **HTML5-এ এর উদ্দেশ্য:**
    1.  এটি ব্রাউজারকে **Standards Mode**-এ নিয়ে যায়, যার ফলে আধুনিক রুলস মেনে পেজ রেন্ডার হয়।
    2.  যদি এটি না দেওয়া হয়, তবে ব্রাউজার পেজটি **Quirks Mode**-এ ওপেন করে, যা পেজের লেআউট ইন্টারপ্রিটেশনে ভুল করতে পারে (ইন্টারনেট এক্সপ্লোরার ৬ এর মতো আচরণ করে)।
    3.  HTML4 এর ডকট্যাকের মতো এটি জটিল ও লম্বা নয়, বরং খুবই সহজ ও সংক্ষিপ্ত।

---

### **Q21: What is the `<main>` tag, and how many times can it be used on a single page? / `<main>` ট্যাগ কী এবং এটি একটি পেজে কতবার ব্যবহার করা যেতে পারে?**

**Answer (English):**
The `<main>` tag designates the unique, dominant content of the `<body>` of a document. It should not contain content that is repeated across pages (like headers, sidebars, logos).
*   **Usage Constraints:**
    *   It can only be used **once** per page. 
    *   It must not be placed as a descendant of `<article>`, `<aside>`, `<footer`, `<header>`, or `<nav>`.

**অনুবাদ (Bangla Translation):**
`<main>` ট্যাগটি কোনো ডকুমেন্টের মূল এবং ইউনিক বিষয়বস্তু ধারণ করে। এতে এমন কোনো তথ্য রাখা উচিত নয় যা প্রতি পেজে রি-ইউজ হয় (যেমন সাইডবার, ফুটার, ন্যাভিগেশন লিংক)।
*   **ব্যবহারের সীমাবদ্ধতা:**
    *   একটি ওয়েব পেজে এটি সর্বোচ্চ **একবারই** ব্যবহার করা যেতে পারে।
    *   এটি কখনোই `<article>`, `<aside>`, `<footer>`, `<header>` বা `<nav>` এর চাইল্ড বা ইনার এলিমেন্ট হিসেবে বসানো যাবে না।

---

### **Q22: Explain the difference between `<meter>` and `<progress>` elements in HTML5. / HTML5-এ `<meter>` এবং `<progress>` এলিমেন্টের মধ্যে পার্থক্য ব্যাখ্যা করুন।**

**Answer (English):**
Both display visual bar indicators, but they represent different data types:
*   **`<progress>`**: Represents the completion progress of a task (e.g., file download progress, form completion steps). It has a dynamic context showing "how far along the process is."
*   **`<meter>`**: Represents a scalar measurement within a known range, or a fractional value (e.g., disk usage space, fuel level, or exam scores). It is for static gauge metrics.

**অনুবাদ (Bangla Translation):**
উভয় এলিমেন্টই স্ক্রিনে বার বা প্রোগ্রেস লেভেল দেখালেও তাদের ব্যবহারের উদ্দেশ্য আলাদা:
*   **`<progress>`**: এটি কোনো নির্দিষ্ট কাজ সম্পন্ন হওয়ার ধাপ বা অগ্রগতি নির্দেশ করে (যেমন- ফাইল ডাউনলোড শেষ হওয়ার শতাংশ, ফর্ম ফিলআপ স্ট্যাটাস)।
*   **`<meter>`**: এটি একটি সুনির্দিষ্ট রেঞ্জের ভেতরের পরিমাপ নির্দেশ করে (যেমন- হার্ডডিস্কের ফাঁকা স্পেসের পরিমাপ, গাড়ির ফুয়েল মিটার, বা পরীক্ষার প্রাপ্ত স্কোর)। এটি স্ট্যাটিক মানের গেজ বার হিসেবে কাজ করে।

---

### **Q23: What are HTML5 Server-Sent Events (SSE), and how do they differ from WebSockets? / HTML5 সার্ভার-সেন্ট ইভেন্টস (SSE) কী এবং এগুলো ওয়েব সকেট থেকে কীভাবে আলাদা?**

**Answer (English):**
Server-Sent Events (SSE) allow a web page to receive real-time updates pushed from a server over an HTTP connection using the `EventSource` interface.
*   **Differences from WebSockets:**
    *   **Direction:** SSE is unidirectional (data flows only from server to client). WebSockets are bidirectional (two-way communication).
    *   **Protocol:** SSE works over standard HTTP/HTTPS protocols (supports HTTP/2 natively). WebSockets require a separate handshake and protocol upgrade (`ws://` or `wss://`).
    *   **Reconnection:** SSE has built-in support for auto-reconnection and event IDs; WebSockets require manual implementation of reconnection logic.
    *   **Data Type:** SSE supports only text-based data; WebSockets support both text and binary data.

**অনুবাদ (Bangla Translation):**
সার্ভার-সেন্ট ইভেন্টস (SSE) হলো `EventSource` এপিআই ব্যবহার করে সাধারণ HTTP সংযোগের মাধ্যমে ব্রাউজারে রিয়েল-টাইম তথ্য বা পুশ আপডেট পাঠানোর একটি মেথড।
*   **ওয়েব সকেটের সাথে এর পার্থক্য:**
    *   **যোগাযোগের দিক:** SSE একমুখী (ডাটা কেবল সার্ভার থেকে ক্লায়েন্টে আসবে)। ওয়েব সকেট উভয়মুখী।
    *   **প্রোটোকল:** SSE সাধারণ HTTP/HTTPS প্রোটোকলে চলে (HTTP/2 সাপোর্ট করে)। ওয়েব সকেটের জন্য আলাদা হ্যান্ডশেক ও প্রোটোকল প্রমোশন (`ws://`) লাগে।
    *   **অটো-রিকানেকশন:** কানেকশন ডিসকানেক্ট হলে SSE নিজে থেকেই পুনরায় কানেক্ট করার চেষ্টা করে। ওয়েব সকেটের ক্ষেত্রে এই লজিকটি জাভাস্ক্রিপ্ট দিয়ে লিখতে হয়।
    *   **ডাটা টাইপ:** SSE কেবল টেক্সট ডাটা পাঠাতে পারে। ওয়েব সকেট টেক্সট ও বাইনারি (ছবি/ফাইল) উভয় টাইপই ট্রান্সফার করতে পারে।

---

### **Q24: How does the browser determine which video format to play inside the `<video>` tag? / ব্রাউজার কীভাবে নির্ধারণ করে যে `<video>` ট্যাগের ভেতরে কোন ভিডিও ফর্ম্যাটটি চালানো হবে?**

**Answer (English):**
Browsers scan the `<source>` tags listed inside a `<video>` tag from top to bottom.
*   The browser checks the `type` attribute of each source (e.g., `type="video/mp4"`). It will play the **first** format that it natively supports and completely ignore all subsequent source tags.
*   If none of the formats are supported, it displays the fallback text written at the bottom of the tag.

**অনুবাদ (Bangla Translation):**
ভিডিও ট্যাগের ভেতরে থাকা একাধিক `<source>` ট্যাগগুলো ব্রাউজার ওপর থেকে নিচে সিরিয়ালি রিড করে।
*   ব্রাউজার প্রতিটি সোর্সের `type` অ্যাট্রিবিউট চেক করে (যেমন: `type="video/mp4"`)। যে প্রথম ফরম্যাটটি তার সিস্টেমে চালানো সম্ভব হবে, সে সেটি প্লে করে এবং নিচের বাকি সোর্স ট্যাগগুলো রিড করা বন্ধ করে দেয়।
*   যদি ব্রাউজার কোনো ভিডিও টাইপই সাপোর্ট না করে, তবে সোর্সের নিচে থাকা অল্টারনেটিভ ফলব্যাক টেক্সট মেসেজটি শো করে।

---

### **Q25: What is the `<figure>` and `<figcaption>` elements, and how are they used? / `<figure>` এবং `<figcaption>` এলিমেন্ট কী এবং কীভাবে এগুলো ব্যবহার করা হয়?**

**Answer (English):**
*   **`<figure>`**: Represents self-contained content, frequently with a caption, and is typically referenced as a single unit from the main flow of the document (e.g., images, illustrations, code snippets, or diagrams).
*   **`<figcaption>`**: Defines a caption or legend for its parent `<figure>` element. It must be placed as the first or last child inside the `<figure>` tag.
*   **Example Syntax:**
    ```html
    <figure>
      <img src="chart.png" alt="Sales Growth Chart">
      <figcaption>Figure 1.1: Annual company sales growth analysis.</figcaption>
    </figure>
    ```

**অনুবাদ (Bangla Translation):**
*   **`<figure>`**: এটি কোনো আর্টিকেলের প্রধান কন্টেন্টের সাথে প্রাসঙ্গিক কিন্তু সম্পূর্ণ আলাদা কন্টেন্ট ইউনিট নির্দেশ করে (যেমন- ছবি, কোনো চার্ট, কোনো ডায়াগ্রাম বা কোড ব্লক)।
*   **`<figcaption>`**: এটি তার প্যারেন্ট `<figure>` এলিমেন্টের জন্য একটি শিরোনাম বা ব্যাখ্যা ক্যাপশন হিসেবে কাজ করে। এটি `<figure>` এর ভেতরে প্রথম বা শেষ চাইল্ড হিসেবে বসাতে হয়।
*   **সিনট্যাক্স উদাহরণ:**
    ```html
    <figure>
      <img src="chart.png" alt="সেলস গ্রোথ চার্ট">
      <figcaption>চিত্র ১.১: কোম্পানির বার্ষিক সেলস গ্রোথ রিপোর্ট।</figcaption>
    </figure>
    ```

---

### **Q26: How do you implement SEO best practices using HTML5 markup? / HTML5 মার্কআপ ব্যবহার করে কীভাবে এসইও (SEO) সেরা অনুশীলনগুলো প্রয়োগ করবেন?**

**Answer (English):**
1.  **Use Semantic Elements:** Use `<article>`, `<section>`, and `<nav>` to help search engine spiders categorize the page hierarchy.
2.  **Proper Heading Hierarchy:** Use only one `<h1>` per page for the main topic, followed by sequential `<h2>`, `<h3>` tags for sub-sections.
3.  **Optimize Images:** Use `alt` attributes on all images and implement `<picture>` with responsive sizes for faster load speed (speed is a mobile search ranking factor).
4.  **Use Semantic Markups for Links:** Avoid `<span onclick="...">` for navigation; instead, use `<a href="...">` to allow search engine crawler bots to discover pages.

**অনুবাদ (Bangla Translation):**
1.  **সিম্যান্টিক এলিমেন্ট ব্যবহার:** সার্চ ইঞ্জিন ক্রলারকে পেজের কাঠামো চেনাতে `<div>` এর পরিবর্তে `<article>`, `<section>` ও `<nav>` ট্যাগ ব্যবহার করা।
2.  **সঠিক হেডিং বিন্যাস:** পেজে একটি মাত্র প্রধান `<h1>` ট্যাগ রাখা এবং তার সাব-টপিকে ক্রমানুসারে `<h2>`, `<h3>` ট্যাগ সাজানো।
3.  **ইমেজ অপ্টিমাইজেশন:** প্রতিটি ছবিতে `alt` ট্যাগ ব্যবহার করা এবং রেসপন্সিভ ইমেজের জন্য `<picture>` ব্যবহার করে পেইজ স্পিড বাড়ানো (যেহেতু পেইজ লোড স্পিড এসইও র‍্যাংকিংয়ের অন্যতম বড় ফ্যাক্টর)।
4.  **লিংক ব্যবহারের সঠিক নিয়ম:** পেজ ন্যাভিগেশনের জন্য জাভাস্ক্রিপ্ট অন-ক্লিকের পরিবর্তে সঠিক `<a href="...">` এঙ্কর ট্যাগ ব্যবহার করা, যাতে সার্চ ইঞ্জিন বট লিংক ধরে ডেটা ক্রল করতে পারে।

---

### **Q27: What is HTML5 viewport meta tag, and why is it crucial for responsive web design? / HTML5 ভিউপোর্ট মেটা ট্যাগ কী এবং রেসপন্সিভ ওয়েব ডিজাইনের জন্য এটি কেন অত্যন্ত গুরুত্বপূর্ণ?**

**Answer (English):**
The viewport is the user's visible area of a web page. The viewport meta tag controls how a webpage is scaled and displayed on different devices.
*   **Syntax:**
    ```html
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ```
*   **Why it is crucial:**
    *   `width=device-width` sets the width of the page to follow the screen-width of the device (varying depending on mobile/tablet).
    *   `initial-scale=1.0` sets the initial zoom level when the page is first loaded.
    *   Without this tag, mobile browsers assume a desktop screen width (usually 980px) and shrink the page elements, making the text tiny and unreadable.

**অনুবাদ (Bangla Translation):**
ভিউ-পোর্ট হলো কোনো ডিভাইসে রেন্ডার হওয়া ওয়েব পেজের ব্যবহারকারীর দৃশ্যমান এলাকা। ভিউপোর্ট মেটা ট্যাগটি ব্রাউজারকে নির্দেশ দেয় কীভাবে বিভিন্ন মোবাইল বা ট্যাবলেটে পেজের স্কেল ও জুম সেট করতে হবে।
*   **সিনট্যাক্স:**
    ```html
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    ```
*   **কেন এটি গুরুত্বপূর্ণ:**
    *   `width=device-width` পেজের উইডথ বা প্রস্থকে ডিভাইসের উইডথের সাথে সমান করে দেয়।
    *   `initial-scale=1.0` প্রথমবার লোড হওয়ার সময় জুম লেভেল ১০০% বা ডিফল্ট রাখে।
    *   এই ট্যাগটি না দিলে মোবাইল ব্রাউজার পুরো পেজকে ৯৮০ পিক্সেল উইডথের ডেস্কটপ হিসেবে বিবেচনা করে এবং পুরো জুম আউট করে ফন্টগুলোকে অতি ক্ষুদ্র করে ফেলে, যা পড়ার অযোগ্য হয়ে পড়ে।

---

### **Q28: What are web components in HTML5 (Shadow DOM, Custom Elements, HTML Templates)? / HTML5-এ ওয়েব কম্পোনেন্টস (Shadow DOM, Custom Elements, HTML Templates) কী?**

**Answer (English):**
Web Components is a suite of three technologies that allow creating reusable, encapsulated custom HTML elements.
1.  **Custom Elements:** APIs to define new HTML tags (e.g., `<user-card>`) with custom behaviors using JavaScript classes:
    ```javascript
    customElements.define('user-card', UserCardClass);
    ```
2.  **Shadow DOM:** Provides encapsulation for DOM styles and scripts, keeping them isolated from the rest of the document (preventing style leaks).
3.  **HTML Templates (`<template>`):** Allows writing markup templates that are not rendered on load but can be cloned and instantiated later using JavaScript.

**অনুবাদ (Bangla Translation):**
ওয়েব কম্পোনেন্টস হলো তিনটি বিশেষ প্রযুক্তির সমষ্টি যা ফ্রেমওয়ার্ক ছাড়াই ব্রাউজারে রি-ইউজেবল এবং এনক্যাপসুলেটেড কাস্টম HTML ট্যাগ তৈরি করতে সাহায্য করে।
1.  **Custom Elements:** জাভাস্ক্রিপ্ট ক্লাসের সাহায্যে ব্রাউজারে নতুন কাস্টম HTML ট্যাগ (যেমন: `<user-card>`) ও মেথড রেজিস্টার করার এপিআই।
2.  **Shadow DOM:** এটি ইউআই স্টাইলিং ও সিএসএস কোডকে বাইরের মূল ডকুমেন্টের স্টাইলিং থেকে আলাদা বা লক করে রাখে, যার ফলে একটি এলিমেন্টের স্টাইল বাইরে চুইয়ে পড়ে না।
3.  **HTML Templates (`<template>`):** এটি এমন ট্যাগ যা পেজ লোডের সময় ব্রাউজারে রেন্ডার হয় না, তবে পরবর্তীতে জাভাস্ক্রিপ্ট দিয়ে ক্লোন বা মাউন্ট করা যায়।

---

### **Q29: What is the `download` attribute in HTML5 anchor (`<a>`) tags? / HTML5-এ নোঙ্গর বা অ্যাঙ্কর (`<a>`) ট্যাগে `download` অ্যাট্রিবিউটটির কাজ কী?**

**Answer (English):**
The `download` attribute inside an `<a>` tag instructs the browser to download the target file rather than navigating to or displaying it (useful for PDFs, images, or text files).
*   **Example Syntax:**
    ```html
    <a href="document.pdf" download="Company_Report.pdf">Download Report</a>
    ```
*   **Key Detail:** 
    *   You can assign a value to the download attribute (e.g., `"Company_Report.pdf"`), which will automatically rename the file upon download. 
    *   For security reasons, it only works if the file has the same origin as the webpage.

**অনুবাদ (Bangla Translation):**
অ্যাঙ্কর (`<a>`) ট্যাগে `download` অ্যাট্রিবিউট দিলে ব্রাউজার ফাইলটি ওপেন বা রিডাইরেক্ট না করে সরাসরি ব্যবহারকারীর ডিভাইসে ডাউনলোড শুরু করে (যেমন পিডিএফ বা কোনো ইমেজ ডাউনলোড)।
*   **সিনট্যাক্স উদাহরণ:**
    ```html
    <a href="document.pdf" download="Company_Report.pdf">রিপোর্ট ডাউনলোড করুন</a>
    ```
*   **মূল বিষয়:**
    *   ডাউনলোড অ্যাট্রিবিউটে কোনো স্ট্রিং ভ্যালু দিলে ফাইলটি ডাউনলোড হওয়ার সময় স্বয়ংক্রিয়ভাবে সেই নতুন নামে সেভ হয়।
    *   নিরাপত্তার স্বার্থে এটি কেবল তখনই কাজ করে যদি ফাইলটির মেমোরি সোর্স এবং ওয়েব পেজের অরিজিন বা ডোমেন একই হয়।

---

### **Q30: How do you ensure web accessibility (a11y) using HTML5 semantic elements and ARIA roles? / HTML5 সিম্যান্টিক এলিমেন্ট এবং ARIA রোলস ব্যবহার করে কীভাবে ওয়েব অ্যাক্সেসিবিলিটি (a11y) নিশ্চিত করবেন?**

**Answer (English):**
1.  **Use Native Semantics First:** Always prefer native HTML5 elements like `<button>` over `<div role="button">` because native elements have built-in keyboard navigation support and focus states.
2.  **Accessible Rich Internet Applications (ARIA) Roles:** When custom components are necessary, use ARIA attributes like `role="dialog"`, `aria-expanded="true"`, or `aria-labelledby` to tell screen readers about dynamic changes in screen states.
3.  **Use Document Landmarks:** Tags like `<nav>`, `<main>`, and `<aside>` serve as document landmark navigators, allowing visually impaired users to jump directly to specific sections.
4.  **Alt and Label Attributes:** Provide descriptive alt texts on images, and connect `<label>` elements explicitly with input field IDs using the `for` attribute.

**অনুবাদ (Bangla Translation):**
1.  **নেটিভ সিম্যান্টিক প্রথম পছন্দ:** সবসময় সাধারণ ডিভে রোল দেওয়ার চেয়ে নেটিভ HTML5 বাটন বা লিংক ট্যাগ ব্যবহার করুন, কারণ এগুলোতে কিবোর্ড অ্যাক্সেসিবিলিটি ও ফোকাস স্টেট আগে থেকেই সেট করা থাকে।
2.  **ARIA Roles ব্যবহার:** কাস্টম কম্পোনেন্ট বানানোর প্রয়োজন হলে `role="dialog"`, `aria-expanded="true"`, বা `aria-labelledby` এর মতো অ্যাট্রিবিউট ব্যবহার করে ডাইনামিক ইউআই বাটন সম্পর্কে স্ক্রিন রিডারকে আপডেট জানান।
3.  **ল্যান্ডমার্ক ব্যবহার:** `<nav>`, `<main>` ও `<aside>` ট্যাগগুলো স্ক্রিন রিডারের জন্য মাইলফলক হিসেবে কাজ করে, ফলে ব্যবহারকারী এক ট্যাপেই পেজের মূল অংশে জাম্প করতে পারেন।
4.  **অল্ট এবং লেবেল ট্যাগ:** প্রতিটি ইমেজে অল্ট ট্যাগ বর্ণনা করা এবং `<label>` ট্যাগের `for` প্রপার্টি দিয়ে ইনপুট ফিল্ডের আইডি কানেক্ট রাখা।
