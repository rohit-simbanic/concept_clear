# Frontend Mastery: HTML5, CSS3, Responsive Design & Animations Prep

This guide contains comprehensive answers and Bangla translations for the 70 interview questions across four key categories: HTML5, CSS3, Responsive Design, and CSS3 Animations & Transitions.

---

## 01. HTML5 - INTERVIEW QUESTIONS

### **Q1: What is HTML5? / HTML5 কী?**
**Answer (English):**
HTML5 is the fifth and latest major version of HTML (HyperText Markup Language), the standard language used to structure and present content on the World Wide Web. It was developed by W3C and WHATWG to standardize multimedia integration, improve semantic structure, and provide powerful API interfaces (like local storage and Geolocation) natively in the browser without requiring external plugins like Flash or Silverlight.

**অনুবাদ (Bangla Translation):**
HTML5 হলো HTML (HyperText Markup Language) এর পঞ্চম এবং সর্বশেষ সংস্করণ, যা ওয়ার্ল্ড ওয়াইড ওয়েব-এ কন্টেন্ট সাজাতে এবং প্রদর্শন করতে ব্যবহৃত হয়। এটিকে W3C এবং WHATWG তৈরি করেছে যাতে কোনো ফ্ল্যাশ বা সিলভারলাইটের মতো বাহ্যিক প্লাগ-ইন ছাড়াই সরাসরি ব্রাউজারে অডিও-ভিডিও চালানো, সুন্দর সিম্যান্টিক গঠন তৈরি করা এবং শক্তিশালী এপিআই (যেমন- লোকাল স্টোরেজ ও জিওলোকেশন) ব্যবহার করা যায়।

---

### **Q2: What are the new features introduced in HTML5? / HTML5-এ নিয়ে আসা নতুন ফিচারসমূহ কী কী?**
**Answer (English):**
HTML5 introduced several key features:
1.  **Semantic Elements:** `<header>`, `<footer>`, `<section>`, `<article>`, `<nav>`, `<aside>`.
2.  **Native Multimedia:** `<audio>` and `<video>` tags.
3.  **Graphics:** Embedded SVG support and the `<canvas>` element for dynamic 2D/3D drawing.
4.  **Web Storage APIs:** `localStorage` and `sessionStorage` (replacing cookies for non-server data).
5.  **New Form Inputs:** `type="email"`, `type="date"`, `type="number"`, `type="color"`, `placeholder`, `required` validation.
6.  **Advanced APIs:** Geolocation, Web Workers, IndexedDB, and Drag and Drop API.

**অনুবাদ (Bangla Translation):**
HTML5-এ বেশ কিছু নতুন ফিচার যুক্ত করা হয়েছে:
1.  **সিম্যান্টিক এলিমেন্টস:** `<header>`, `<footer>`, `<section>`, `<article>`, `<nav>`, `<aside>` ইত্যাদি।
2.  **নেটিভ মাল্টিমিডিয়া:** সরাসরি ভিডিও ও অডিও চালানোর জন্য `<video>` এবং `<audio>` ট্যাগ।
3.  **গ্রাফিক্স:** সরাসরি SVG কোড লেখার সুবিধা এবং ডাইনামিক ড্রইংয়ের জন্য `<canvas>` ট্যাগ।
4.  **ওয়েব স্টোরেজ:** ব্রাউজারে ডেটা সেভ রাখার জন্য `localStorage` এবং `sessionStorage`।
5.  **নতুন ফর্ম ইনপুট:** ইমেইল, ডেট, নাম্বার ও কালার পিকারের মতো ইনপুট টাইপ এবং ভ্যালিডেশনের জন্য required ও placeholder।
6.  **অ্যাডভান্সড এপিআই:** জিওলোকেশন, ওয়েব ওয়ার্কার্স, ইনডেক্স-ডিবি এবং ড্র্যাগ-অ্যান্ড-ড্রপ এপিআই।

---

### **Q3: What is the difference between HTML and HTML5? / HTML এবং HTML5 এর মধ্যে পার্থক্য কী?**
**Answer (English):**

| Feature | HTML (Older versions like HTML4) | HTML5 |
| :--- | :--- | :--- |
| **Multimedia Support** | Needed external plugins like Adobe Flash. | Native support via `<audio>` and `<video>` tags. |
| **Storage** | Used browser cookies (limited to 4KB). | Uses Web Storage (`localStorage` up to 10MB). |
| **Graphics** | Did not support vector graphics directly. | Native support for SVG and Canvas drawing. |
| **Multithreading** | JavaScript ran on the main UI thread only. | Supports Web Workers to run scripts in the background. |
| **Geopositioning** | Not supported natively. | Has built-in Geolocation API. |

**অনুবাদ (Bangla Translation):**

| বৈশিষ্ট্য | HTML (পুরাতন সংস্করণ যেমন HTML4) | HTML5 |
| :--- | :--- | :--- |
| **মাল্টিমিডিয়া সাপোর্ট** | চালানোর জন্য ফ্ল্যাশ প্লেয়ার বা প্লাগ-ইন লাগত। | সরাসরি `<audio>` ও `<video>` ট্যাগ দিয়ে চলে। |
| **ডাটা স্টোরেজ** | ব্রাউজার কুকি ব্যবহার করত (যার সাইজ মাত্র ৪ কিলোবাইট)। | ওয়েব স্টোরেজ ব্যবহার করে (যার সাইজ ৫-১০ মেগাবাইট)। |
| **গ্রাফিক্স** | সরাসরি ভেক্টর গ্রাফিক্স আঁকা যেত না। | সরাসরি SVG এবং Canvas আঁকার মেকানিজম রয়েছে। |
| **মাল্টিথ্রেডিং** | জাভাস্ক্রিপ্ট কেবল প্রধান ইউআই থ্রেডেই চলত। | ব্যাকগ্রাউন্ডে স্ক্রিপ্ট চালাতে ওয়েব ওয়ার্কার্স সাপোর্ট করে। |
| **জিওলোকেশন** | জিপিএস ট্র্যাকিংয়ের নিজস্ব কোনো এপিআই ছিল না। | বিল্ট-ইন জিওলোকেশন এপিআই রয়েছে। |

---

### **Q4: What is the purpose of the `<!DOCTYPE html>` declaration? / `<!DOCTYPE html>` ডিক্লারেশনের উদ্দেশ্য কী?**
**Answer (English):**
The `<!DOCTYPE html>` declaration is an instruction to the web browser that the document is written in HTML5. It is not an HTML tag. Its main purpose is to trigger the browser's **Standards Mode** rather than **Quirks Mode**, ensuring that the web page renders consistently across different modern browsers according to W3C specifications.

**অনুবাদ (Bangla Translation):**
`<!DOCTYPE html>` ডিক্লারেশনটি কোনো HTML ট্যাগ নয়; এটি ব্রাউজারের জন্য একটি নির্দেশনা যা জানায় যে ফাইলটি HTML5 সংস্করণে লেখা হয়েছে। এর মূল উদ্দেশ্য হলো ব্রাউজারকে **Standards Mode**-এ চালিত করা (Quirks Mode এড়ানো), যার ফলে ডব্লিউ-থ্রি-সি (W3C) নিয়ম অনুযায়ী পেজটি সব ব্রাউজারে নিখুঁত ও একইভাবে রেন্ডার হয়।

---

### **Q5: What are semantic elements in HTML5? Give examples. / HTML5-এ সিম্যান্টিক এলিমেন্ট কী? উদাহরণ দিন।**
**Answer (English):**
Semantic elements are tags that clearly communicate the meaning and purpose of their content to both the browser and the developer. Unlike generic layout tags like `<div>` or `<span>`, semantic tags describe what they are.
*   **Examples:**
    *   `<header>`: Defines the introduction section.
    *   `<nav>`: Defines navigation links.
    *   `<main>`: Represents the primary content area.
    *   `<article>`: Represents independent, distributable content.
    *   `<footer>`: Represents copyright and policy sections at the bottom.

**অনুবাদ (Bangla Translation):**
সিম্যান্টিক এলিমেন্ট হলো এমন ট্যাগ যা নিজের অর্থ ও কন্টেন্টের ধরণ ব্রাউজার এবং ডেভেলপার উভয়ের কাছে স্পষ্ট করে তোলে। সাধারণ লেআউট ট্যাগ যেমন `<div>` বা `<span>` এর মতো না হয়ে এরা নিজের ভূমিকা নিজেই প্রকাশ করে।
*   **উদাহরণ:**
    *   `<header>`: পেজ বা আর্টিকেলের সূচনা অংশ নির্ধারণ করে।
    *   `<nav>`: ন্যাভিগেশন বার বা লিংক ধারণ করে।
    *   `<main>`: পেজের প্রধান কন্টেন্ট জোন নির্দেশ করে।
    *   `<article>`: স্বাধীন ব্লগ বা সংবাদ কন্টেন্ট প্রকাশ করে।
    *   `<footer>`: পেজের নিচের কপিরাইট ও টার্মস অংশ নির্দেশ করে।

---

### **Q6: What is the difference between `<div>` and `<span>`? / `<div>` এবং `<span>` এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`<div>` (Division):** It is a **block-level** element. It starts on a new line and takes up the full width available. It is used to group large sections of HTML for layout styling.
*   **`<span>`:** It is an **inline-level** element. It does not start on a new line and only takes up as much width as its content. It is used to style specific words or small portions of text inside block elements.

**অনুবাদ (Bangla Translation):**
*   **`<div>` (Division):** এটি একটি **ব্লক-লেভেল** এলিমেন্ট। এটি ব্রাউজারে সবসময় নতুন লাইন থেকে শুরু হয় এবং স্ক্রিনের পুরো উইডথ দখল করে। এটি মূলত বড় বড় সেকশন গ্রুপ করতে ব্যবহৃত হয়।
*   **`<span>`:** এটি একটি **ইনলাইন-লেভেল** এলিমেন্ট। এটি কোনো নতুন লাইন তৈরি করে না এবং কেবল নিজের কন্টেন্টের সমান উইডথ নেয়। এটি প্যারাগ্রাফ বা টেক্সটের ভেতরে নির্দিষ্ট অংশকে সিএসএস দিয়ে স্টাইল করতে ব্যবহৃত হয়।

---

### **Q7: What is the difference between `<section>`, `<article>`, `<aside>` and `<nav>`? / `<section>`, `<article>`, `<aside>` এবং `<nav>` এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`<section>`:** Defines a thematic grouping of content, typically with a heading (e.g., "Services", "About Us").
*   **`<article>`:** Defines independent, self-contained content that can stand alone and be syndicated (e.g., blog posts, newspaper articles).
*   **`<aside>`:** Defines content aside from the page content, like sidebars, advertisements, or related link boxes.
*   **`<nav>`:** Defines a block of major navigation links for navigating the site.

**অনুবাদ (Bangla Translation):**
*   **`<section>`:** কোনো কন্টেন্টের থিমেটিক গ্রুপ বা বড় অংশ প্রকাশ করে, সাধারণত একটি হেডিং থাকে (যেমন- "সার্ভিসেস" সেকশন)।
*   **`<article>`:** সম্পূর্ণ স্বাধীন ও স্বয়ংসম্পূর্ণ কোনো কন্টেন্ট নির্দেশ করে যা অন্য পেইজেও পুনরায় ব্যবহারযোগ্য (যেমন- ব্লগ পোস্ট)।
*   **`<aside>`:** মূল বিষয়ের বাইরে আনুসঙ্গিক তথ্য যেমন সাইডবার, বিজ্ঞাপন বা সহায়ক লিংক দেখানোর জন্য ব্যবহৃত হয়।
*   **`<nav>`:** সাইটের প্রধান ন্যাভিগেশন লিংক বার তৈরি করতে ব্যবহৃত হয়।

---

### **Q8: What is the purpose of the `<header>`, `<footer>` and `<main>` tags? / `<header>`, `<footer>` এবং `<main>` ট্যাগের উদ্দেশ্য কী?**
**Answer (English):**
*   **`<header>`:** Represents a container for introductory content, logos, search bars, or global navigations at the top of a page or article.
*   **`<footer>`:** Renders closing metadata at the bottom of the page, holding copyrights, privacy policies, or sitemaps.
*   **`<main>`:** Contains the unique, main content of the web page. There must not be more than one `<main>` tag per HTML document, and it cannot be nested inside `<header>`, `<footer>`, or `<article>`.

**অনুবাদ (Bangla Translation):**
*   **`<header>`:** পেজ বা কোনো আর্টিকেলের পরিচিতিমূলক অংশ, লোগো, সার্চ বার বা গ্লোবাল ন্যাভিগেশন লিংক ধারণ করে।
*   **`<footer>`:** পেজের শেষ বা ফুট অংশ নির্দেশ করে, যেখানে কপিরাইট, পলিসি বা সাইটম্যাপ থাকে।
*   **`<main>`:** পেজের প্রধান ইউনিক কন্টেন্ট ধারণ করে। একটি HTML পেজে একের বেশি `<main>` ট্যাগ থাকতে পারবে না এবং এটি অন্য কোনো লেআউট ট্যাগের ভেতর নেস্ট করা যায় না।

---

### **Q9: What is the difference between `<strong>`, `<b>`, `<em>` and `<i>`? / `<strong>`, `<b>`, `<em>` এবং `<i>` এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`<strong>` and `<b>` (Bold):** Both display bold text. However, `<strong>` carries **semantic importance** (screen readers speak it with emphasis, indicating critical info). `<b>` is for purely visual decoration without added importance.
*   **`<em>` (Emphasis) and `<i>` (Italic):** Both render text in italics. However, `<em>` indicates semantic emphasis that changes the meaning of a sentence when read aloud. `<i>` is purely for visual italicization (e.g., technical terms, thoughts, or idioms) without semantic weight.

**অনুবাদ (Bangla Translation):**
*   **`<strong>` এবং `<b>`:** দুটির মাধ্যমেই লেখা মোটা (Bold) হয়। তবে `<strong>` দ্বারা লেখার **সিম্যান্টিক গুরুত্ব** প্রকাশ পায় (স্ক্রিন রিডার এটি জোর দিয়ে পড়ে)। আর `<b>` দিয়ে কেবলই লেখাটি দেখতে মোটা করা হয়, এর কোনো আলাদা গুরুত্ব থাকে না।
*   **`<em>` এবং `<i>`:** দুটির মাধ্যমেই লেখা বাঁকা (Italic) হয়। তবে `<em>` সিম্যান্টিক জোর (Emphasis) প্রকাশ করে যা বাক্যের উচ্চারণগত ভাব পরিবর্তন করে। আর `<i>` কেবল লেখাটিকে বাঁকা করে দেখায়, এর পেছনে কোনো অতিরিক্ত গুরুত্ব থাকে না।

---

### **Q10: What is the difference between `<figure>`, `<figcaption>` and `<img>`? / `<figure>`, `<figcaption>` এবং `<img>` এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`<img>`:** A self-closing tag used simply to embed an image resource on a page.
*   **`<figure>`:** A block-level semantic container used to group the image (`<img>`) and its description together as a single standalone unit.
*   **`<figcaption>`:** A semantic tag placed inside `<figure>` to write the caption or title of the enclosed image, diagram, or code block.

**অনুবাদ (Bangla Translation):**
*   **`<img>`:** এটি কেবল ওয়েব পেজে একটি ইমেজ ফাইল বা ছবি যুক্ত করার জন্য ব্যবহৃত হয়।
*   **`<figure>`:** এটি একটি ব্লক-লেভেল কন্টেইনার যা ছবি (`<img>`) এবং তার বর্ণনাকে একসাথে একটি ইউনিট হিসেবে গ্রুপ করে রাখে।
*   **`<figcaption>`:** এটি `<figure>` ট্যাগের ভেতরে ছবি বা ডায়াগ্রামের নিচে বা ওপরে তার ক্যাপশন বা শিরোনাম লিখতে ব্যবহৃত হয়।

---

### **Q11: What is the use of the `<canvas>` element? / `<canvas>` এলিমেন্টের কাজ কী?**
**Answer (English):**
The HTML5 `<canvas>` element provides a blank, raster-based drawing container on the web page. It uses JavaScript APIs to dynamically render and manipulate graphics, animations, chart diagrams, and interactive 2D/3D games on the fly. It is resolution-dependent, meaning it renders pixels and can pixelate when zoomed.

**অনুবাদ (Bangla Translation):**
HTML5 এর `<canvas>` ট্যাগটি ব্রাউজারে রাস্টার গ্রাফিক্স আঁকার জন্য একটি ফাঁকা কন্টেইনার দেয়। এটি জাভাস্ক্রিপ্ট এপিআই ব্যবহার করে রানটাইমে ডাইনামিক ছবি, চার্ট, অ্যানিমেশন এবং ২ডি/৩ডি গেম ড্র করতে সাহায্য করে। এটি পিক্সেল-বেসড হওয়ায় জুম করলে ফেটে যাওয়ার সম্ভাবনা থাকে।

---

### **Q12: What is the use of the `<audio>` and `<video>` elements? / `<audio>` এবং `<video>` এলিমেন্টের কাজ কী?**
**Answer (English):**
The `<audio>` and `<video>` tags are used to embed multimedia content directly into HTML documents natively. They allow play, pause, volume adjust, and seek operations directly through browser engine controllers, eliminating the need for Adobe Flash player or third-party plug-ins.

**অনুবাদ (Bangla Translation):**
`<audio>` এবং `<video>` ট্যাগগুলো কোনো থার্ড-পার্টি ফ্ল্যাশ প্লেয়ার ছাড়াই ব্রাউজারে সরাসরি অডিও এবং ভিডিও প্লে করার নেটিভ সুবিধা দেয়। এর মাধ্যমে ব্রাউজার নিজেই প্লে, পজ, সাউন্ড কন্ট্রোল এবং সিক বার হ্যান্ডেল করতে পারে।

---

### **Q13: What are the supported video formats in HTML5? / HTML5-এ সমর্থিত ভিডিও ফরম্যাটগুলো কী কী?**
**Answer (English):**
HTML5 officially supports three standard video container formats:
1.  **MP4 (MPEG-4):** H.264 video codec + AAC audio codec (Most widely supported).
2.  **WebM:** VP8/VP9 video codec + Vorbis/Opus audio codec (Optimized for web).
3.  **Ogg:** Theora video codec + Vorbis audio codec.

**অনুবাদ (Bangla Translation):**
HTML5 মূলত তিনটি ভিডিও ফরম্যাট সাপোর্ট করে:
1.  **MP4:** H.264 ভিডিও কোডেক + AAC অডিও কোডেক (সবচেয়ে বেশি ব্যবহৃত)।
2.  **WebM:** VP8/VP9 ভিডিও কোডেক + Vorbis/Opus অডিও কোডেক (ওয়েব লোডিংয়ের জন্য অপ্টিমাইজড)।
3.  **Ogg:** Theora ভিডিও কোডেক + Vorbis অডিও কোডেক।

---

### **Q14: What is the difference between `<audio>` and `<video>`? / `<audio>` এবং `<video>` এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`<audio>`:** Built specifically for playing sound files. It does not have a visual screen display canvas and only shows volume/track navigation controls.
*   **`<video>`:** Built for playing visual moving pictures with sound. It requires a specific layout viewport (`width`/`height`) to render the video frame stream, and includes a fallback image poster property.

**অনুবাদ (Bangla Translation):**
*   **`<audio>`:** এটি কেবল সাউন্ড বা অডিও ট্র্যাক প্লে করার জন্য ব্যবহৃত হয়। এর কোনো ভিজ্যুয়াল ডিসপ্লে এরিয়া থাকে না, এটি শুধু সাউন্ড কন্ট্রোল বার দেখায়।
*   **`<video>`:** এটি স্ক্রিনে ভিডিও ফ্রেম দেখানোর জন্য ব্যবহৃত হয়। এর একটি নির্দিষ্ট উইডথ/হাইট লেআউট ভিউপোর্ট থাকে এবং ভিডিও লোড হওয়ার আগে থাম্বনেইল হিসেবে একটি ইমেজ 'poster' দেখানোর সুবিধা থাকে।

---

### **Q15: What is localStorage and sessionStorage? / localStorage এবং sessionStorage কী?**
**Answer (English):**
Both are parts of the HTML5 Web Storage API allowing key-value data storage directly in the user's browser:
*   **`localStorage`:** Stores data with no expiration time. The data remains in the browser even after the browser tab or window is closed or the computer is restarted.
*   **`sessionStorage`:** Stores data only for the duration of the current page session. The data is cleared as soon as the specific browser tab is closed.

**অনুবাদ (Bangla Translation):**
উভয়ই ব্রাউজারে Key-Value আকারে ডেটা সেভ রাখার এপিআই:
*   **`localStorage`:** এর ডেটা স্থায়ীভাবে ব্রাউজারে থেকে যায়। ব্রাউজার উইন্ডো বা কম্পিউটার বন্ধ করলেও এই ডেটা মুছে যায় না।
*   **`sessionStorage`:** এর ডেটা কেবল সেশন চলাকালীন বা নির্দিষ্ট ট্যাব খোলা থাকা পর্যন্ত থাকে। ট্যাবটি বন্ধ করার সাথে সাথে ডেটা ডিলিট হয়ে যায়।

---

### **Q16: What is the difference between localStorage, sessionStorage and cookies? / localStorage, sessionStorage এবং cookies এর মধ্যে পার্থক্য কী?**
**Answer (English):**

| Feature | Cookies | LocalStorage | SessionStorage |
| :--- | :--- | :--- | :--- |
| **Capacity** | ~4 KB | ~5MB to 10MB | ~5MB |
| **Expiration** | Set manually via code. | Never expires. | Cleared when tab closes. |
| **Server Transfer** | Sent to server on every HTTP request. | Stays client-side only. | Stays client-side only. |
| **Security** | Vulnerable if not flagged HTTPOnly. | Accessible via JS (XSS risk). | Accessible via JS (XSS risk). |

**অনুবাদ (Bangla Translation):**

| বৈশিষ্ট্য | Cookies (কুকি) | LocalStorage | SessionStorage |
| :--- | :--- | :--- | :--- |
| **ধারণক্ষমতা** | মাত্র ৪ কিলোবাইট। | ৫ থেকে ১০ মেগাবাইট। | ৫ মেগাবাইট। |
| **স্থায়িত্ব** | কোড দিয়ে নির্দিষ্ট সময় সেট করা যায়। | কখনো নিজে থেকে মুছে যায় না। | ট্যাব বন্ধ করলে সাথে সাথে মুছে যায়। |
| **সার্ভার ট্রান্সফার** | প্রতিটি HTTP রিকোয়েস্টে সার্ভারে যায়। | কেবল ক্লায়েন্টেই থাকে, সার্ভারে যায় না। | কেবল ক্লায়েন্টেই থাকে, সার্ভারে যায় না। |
| **নিরাপত্তা** | HTTPOnly ফ্লাগ না দিলে হ্যাক হতে পারে। | জাভাস্ক্রিপ্ট দিয়ে রিড করা যায়। | জাভাস্ক্রিপ্ট দিয়ে রিড করা যায়। |

---

### **Q17: What is the purpose of the `data-*` attribute? / `data-*` অ্যাট্রিবিউটের উদ্দেশ্য কী?**
**Answer (English):**
The `data-*` attribute allows developers to store custom data directly on HTML elements without using non-standard tags. The stored data can be easily accessed in JavaScript using `element.dataset.propName` or targeted in CSS selectors for dynamic styling.

**অনুবাদ (Bangla Translation):**
`data-*` অ্যাট্রিবিউটটি কোনো স্ট্যান্ডার্ড রুলস না ভেঙে সরাসরি HTML এলিমেন্টের ভেতরে নিজস্ব ডেটা সেভ রাখতে সাহায্য করে। এই ডেটা জাভাস্ক্রিপ্ট কোডে `element.dataset` প্রপার্টির মাধ্যমে রিড করা যায় এবং সিএসএস স্টাইলিংয়েও ব্যবহার করা যায়।

---

### **Q18: What is the difference between `<progress>` and `<meter>`? / `<progress>` এবং `<meter>` এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`<progress>`:** Used to show the completion progress of a task (e.g., "70% of the file downloaded"). It represents dynamic task completion.
*   **`<meter>`:** Used to show a scalar measurement within a known range, or a fractional gauge (e.g., Disk Space Used, CPU temp, or exam grade scale).

**অনুবাদ (Bangla Translation):**
*   **`<progress>`**: কোনো নির্দিষ্ট কাজের চলমান অগ্রগতি বা কতটুকু কাজ সম্পন্ন হয়েছে তা দেখাতে ব্যবহৃত হয় (যেমন- "ফাইল ডাউনলোড প্রোগ্রেস")।
*   **`<meter>`**: কোনো সুনির্দিষ্ট সীমানার ভেতরে থাকা স্ট্যাটিক বা মাপা মান নির্দেশ করে (যেমন- মেমোরি কার্ডে কতটুকু জায়গা ব্যবহার হয়েছে তার গেজ বার)।

---

### **Q19: What is the use of the `<details>` and `<summary>` tags? / `<details>` এবং `<summary>` ট্যাগের কাজ কী?**
**Answer (English):**
The `<details>` tag creates an interactive disclosure widget that the user can open or close to view extra content. The `<summary>` tag inside it acts as the visible header or toggle handle for the widget. When clicked, it expands or collapses the details content natively without any JavaScript.

**অনুবাদ (Bangla Translation):**
`<details>` ট্যাগটি কোনো অতিরিক্ত তথ্য দেখানো বা লুকানোর জন্য একটি ইন্টারঅ্যাক্টিভ উইজেট তৈরি করে। আর এর ভেতরে থাকা `<summary>` ট্যাগটি ওই উইজেটের হেডার বা বাটন হিসেবে কাজ করে, যাতে ক্লিক করলে কোনো জাভাস্ক্রিপ্ট ছাড়াই কন্টেন্ট খোলে এবং বন্ধ হয়।

---

### **Q20: How do you embed SVG in HTML5? / HTML5-এ SVG কীভাবে যুক্ত করবেন?**
**Answer (English):**
In HTML5, you can embed SVG (Scalable Vector Graphics) in several ways:
1.  **Inline SVG:** Directly pasting `<svg>` tags inside the HTML document.
2.  **`<img>` Tag:** `<img src="image.svg" alt="vector">`
3.  **`<object>` Tag:** `<object data="image.svg" type="image/svg+xml"></object>`
4.  **CSS Background:** Using it in CSS as `background-image: url('image.svg')`.

**অনুবাদ (Bangla Translation):**
HTML5-এ বিভিন্নভাবে SVG (ভেক্টর গ্রাফিক্স) যুক্ত করা যায়:
1.  **ইনলাইন SVG:** সরাসরি HTML ফাইলের ভেতরে `<svg>` ট্যাগ পেস্ট করে দিয়ে।
2.  **`<img>` ট্যাগ:** ছবির মতো করে `<img src="image.svg">` লিখে।
3.  **`<object>` ট্যাগ:** এম্বেড করার জন্য `<object data="image.svg" type="image/svg+xml">` ব্যবহার করে।
4.  **CSS ব্যাকগ্রাউন্ড:** সিএসএস ফাইলে `background-image: url('image.svg')` দিয়ে।

---
---

## 02. CSS3 - INTERVIEW QUESTIONS

### **Q1: What is CSS3? / CSS3 কী?**
**Answer (English):**
CSS3 is the latest evolution of the Cascading Style Sheets language. Unlike CSS2, which was a single large specification, CSS3 is split into independent modules (such as Selectors, Box Model, Backgrounds, Animations, Flexbox, and Grid) allowing faster specifications update by W3C.

**অনুবাদ (Bangla Translation):**
CSS3 হলো ক্যাসকেডিং স্টাইল শিট (CSS) ল্যাঙ্গুয়েজের সর্বশেষ সংস্করণ। CSS2 এর মতো একটি বড় ফাইলের পরিবর্তে CSS3-কে বেশ কিছু আলাদা মডিউলে (যেমন- সিলেক্টর, বক্স মডেল, ফ্লেক্সবক্স, গ্রিড, অ্যানিমেশন) ভাগ করা হয়েছে যাতে ব্রাউজারগুলো দ্রুত নতুন নতুন ফিচার এডাপ্ট করতে পারে।

---

### **Q2: What are the new features introduced in CSS3? / CSS3-তে নিয়ে আসা নতুন ফিচারসমূহ কী কী?**
**Answer (English):**
CSS3 introduced powerful styling properties:
1.  **Layout Models:** Flexbox and CSS Grid.
2.  **Transitions & Animations:** Native animations via `@keyframes` and `transition`.
3.  **Visual Effects:** Border radius (`border-radius`), box shadows (`box-shadow`), text shadows (`text-shadow`), linear/radial gradients.
4.  **Transforms:** 2D/3D transformations (`translate`, `rotate`, `scale`, `skew`).
5.  **Media Queries:** Core of responsive web designs.
6.  **Custom Fonts:** `@font-face` support for hosting web fonts.

**অনুবাদ (Bangla Translation):**
CSS3-তে অসাধারণ সব নতুন প্রপার্টি যুক্ত করা হয়েছে:
1.  **লেআউট সিস্টেম:** ফ্লেক্সবক্স (Flexbox) এবং সিএসএস গ্রিড (CSS Grid)।
2.  **ট্রানজিশন ও অ্যানিমেশন:** কোনো ফ্ল্যাশ ছাড়াই সিএসএস দিয়ে সরাসরি অ্যানিমেশন তৈরির সুবিধা।
3.  **ভিজ্যুয়াল এফেক্ট:** কোণা গোল করা (`border-radius`), বক্স শ্যাডো, টেক্সট শ্যাডো এবং কালার গ্রেডিয়েন্ট।
4.  **ট্রান্সফর্ম:** ২ডি এবং ৩ডি ট্রান্সফর্মেশন (ঘোরানো, স্কেল করা, পজিশন সরানো)।
5.  **মিডিয়া কোয়েরি:** রেসপন্সিভ ওয়েব ডিজাইনের মূল ভিত্তি।
6.  **কাস্টম ফন্ট:** ব্রাউজারে নিজস্ব ফন্ট ব্যবহারের জন্য `@font-face` সাপোর্ট।

---

### **Q3: What is the difference between CSS2 and CSS3? / CSS2 এবং CSS3 এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **CSS2** was a single document, did not support responsive design natively, required background images for round corners, and could not handle animations without Flash/JS.
*   **CSS3** is split into modules, supports responsive design natively via media queries, has native features for round corners (`border-radius`), gradients, shadows, transitions, animations, and has advanced layout managers (Flexbox/Grid).

**অনুবাদ (Bangla Translation):**
*   **CSS2** ছিল একটি বড় সিঙ্গেল ডকুমেন্টের স্টাইল শিট, এতে রেসপন্সিভ ডিজাইন করা যেত না এবং গোল কোণার জন্য ইমেজ কেটে বসাতে হতো।
*   **CSS3** আলাদা আলাদা মডিউলে বিভক্ত, মিডিয়া কোয়েরির সাহায্যে সরাসরি রেসপন্সিভ লেআউট বানানো যায়, এবং সিএসএস কোড দিয়েই শ্যাডো, গ্রেডিয়েন্ট, অ্যানিমেশন ও ফ্লেক্সবক্স/গ্রিড লেআউট তৈরি করা যায়।

---

### **Q4: What is the box model in CSS? / CSS-এ বক্স মডেল কী?**
**Answer (English):**
The CSS Box Model is a conceptual box that wraps around every HTML element. It consists of four concentric layers from inside to outside:
1.  **Content:** The actual text or image inside the element.
2.  **Padding:** The clear space immediately around the content (inside the border).
3.  **Border:** A line surrounding the padding and content.
4.  **Margin:** The clear space outside the border separating it from other elements.
*   **Formula for element total width:** `Width + Padding + Border + Margin`.

**অনুবাদ (Bangla Translation):**
CSS বক্স মডেল হলো একটি বিশেষ ধারণা যা প্রতিটি HTML এলিমেন্টকে একটি চারকোনা বক্স হিসেবে বিবেচনা করে। এটি ভেতর থেকে বাইরে ক্রমানুসারে ৪টি লেয়ার নিয়ে গঠিত:
1.  **Content (কন্টেন্ট):** এলিমেন্টের মূল লেখা বা ছবি।
2.  **Padding (প্যাডিং):** কন্টেন্টের চারপাশের ফাঁকা জায়গা (যা বর্ডারের ভেতরে থাকে)।
3.  **Border (বর্ডার):** প্যাডিং ও কন্টেন্টকে ঘিরে থাকা চারপাশের সীমারেখা।
4.  **Margin (মার্জিন):** বর্ডারের বাইরের ফাঁকা জায়গা যা অন্য এলিমেন্ট থেকে দূরত্ব বজায় রাখে।
*   **এলিমেন্টের মোট উইডথ:** `উইডথ + প্যাডিং + বর্ডার + মার্জিন`।

---

### **Q5: What is the difference between margin and padding? / margin এবং padding এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **Padding:** The space *inside* the element's border, separating the content from its own border. Adding padding increases the element's click area and reveals its background color.
*   **Margin:** The space *outside* the element's border, creating distance between the element and other surrounding elements. Margin is transparent and does not show the element's background.

**অনুবাদ (Bangla Translation):**
*   **Padding (প্যাডিং):** এটি বর্ডারের *ভেতরের* ফাঁকা জায়গা যা কন্টেন্টকে তার নিজের বর্ডার থেকে দূরে রাখে। প্যাডিং বাড়ালে বাটনের ক্লিকেবল এরিয়া বাড়ে এবং এতে ব্যাকগ্রাউন্ড কালার দেখা যায়।
*   **Margin (মার্জিন):** এটি বর্ডারের *বাইরের* ফাঁকা জায়গা যা একটি এলিমেন্টকে তার চারপাশের অন্য এলিমেন্ট থেকে দূরে সরিয়ে দেয়। মার্জিন সবসময় ট্রান্সপারেন্ট বা স্বচ্ছ থাকে।

---

### **Q6: What is the difference between display: none, visibility: hidden and opacity: 0? / display: none, visibility: hidden এবং opacity: 0 এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`display: none`:** The element is completely removed from the document flow. It occupies zero space and cannot receive pointer clicks.
*   **`visibility: hidden`:** The element becomes invisible but still occupies its physical space in the layout. It cannot receive pointer click events.
*   **`opacity: 0`:** The element becomes completely transparent but remains in the layout and still occupies space. Importantly, it **can** still receive user clicks and keyboard focuses.

**অনুবাদ (Bangla Translation):**
*   **`display: none`:** এলিমেন্টটি লেআউট থেকে পুরোপুরি উধাও হয়ে যায় এবং কোনো জায়গা দখল করে না।
*   **`visibility: hidden`:** এলিমেন্টটি অদৃশ্য হয়ে যায় কিন্তু লেআউটে তার নিজের জায়গাটি ঠিকই দখল করে রাখে। এতে ক্লিক করা যায় না।
*   **`opacity: 0`:** এলিমেন্টটি ১০০% স্বচ্ছ হয়ে যায় কিন্তু জায়গায় বহাল থাকে। এটি অদৃশ্য হলেও ইউজার এতে ক্লিক করতে বা কিবোর্ড ফোকাস করতে পারেন।

---

### **Q7: What is the difference between relative, absolute, fixed and sticky positioning? / relative, absolute, fixed এবং sticky পজিশনিংয়ের মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`position: relative`:** Positioned relative to its normal document flow position. Moving it using top/left does not affect surrounding elements.
*   **`position: absolute`:** Removed from normal document flow. Positioned relative to its closest parent that has a position other than `static`.
*   **`position: fixed`:** Removed from document flow and positioned relative to the browser viewport window. It stays in the same place even when scrolled.
*   **`position: sticky`:** A hybrid of relative and fixed. It behaves like relative until the user scrolls past a threshold, at which point it sticks (behaves like fixed).

**অনুবাদ (Bangla Translation):**
*   **`position: relative`:** এটি তার স্বাভাবিক অবস্থানের সাপেক্ষে পজিশন নির্ধারণ করে। একে টপ/লেফট দিয়ে সরালেও চারপাশের অন্য কোড সরে যায় না।
*   **`position: absolute`:** এটি ডকুমেন্টের স্বাভাবিক ফ্লো থেকে বের হয়ে যায় এবং তার সবচেয়ে কাছের পজিশনড (Relative/Absolute) প্যারেন্ট এলিমেন্টের সাপেক্ষে জায়গা নেয়।
*   **`position: fixed`:** এটি স্ক্রিন বা ব্রাউজার ভিউপোর্টের সাপেক্ষে লক হয়ে যায়। পেজ স্ক্রল করলেও এটি একই জায়গায় স্থির থাকে।
*   **`position: sticky`:** এটি রিলেটিভ ও ফিক্সড এর সংমিশ্রণ। স্ক্রল করে একটি নির্দিষ্ট সীমায় না পৌঁছানো পর্যন্ত এটি সাধারণ রিলেটিভের মতো চলে এবং সীমা পার হলে সেখানে আটকে (fixed) থাকে।

---

### **Q8: What is the z-index and how does it work? / z-index কী এবং এটি কীভাবে কাজ করে?**
**Answer (English):**
`z-index` controls the stack order of overlapping elements along the Z-axis (depth). 
*   **How it works:**
    *   It only works on elements that have a defined position other than `static` (e.g., relative, absolute, fixed).
    *   Elements with a higher `z-index` number render on top of elements with lower numbers.
    *   It is subject to the **Stacking Context** (an element's z-index is only compared against its siblings in the same stacking context, not across the entire page).

**অনুবাদ (Bangla Translation):**
`z-index` হলো ওভারল্যাপ করা বা একটার ওপর আরেকটা চেপে বসা এলিমেন্টগুলোর Z-অক্ষ (গভীরতা) বরাবর কে ওপরে থাকবে আর কে নিচে থাকবে তা নিয়ন্ত্রণ করার প্রপার্টি।
*   **কাজ করার নিয়ম:**
    *   এটি কেবল তখনই কাজ করে যখন এলিমেন্টের পজিশন `static` বাদে অন্য কিছু (Relative, Absolute) সেট করা থাকে।
    *   যার `z-index` মান বেশি হবে সে ওপরে দেখাবে, আর যার মান কম সে নিচে চলে যাবে।
    *   এটি **Stacking Context** এর নিয়মে চলে (অর্থাৎ একটি নির্দিষ্ট প্যারেন্টের চাইল্ডদের z-index কেবল তাদের নিজেদের মাঝেই তুলনা করা হয়, বাইরের অন্য কোনো গ্রপের সাথে নয়)।

---

### **Q9: What is CSS specificity and how is it calculated? / CSS specificity কী এবং এটি কীভাবে হিসাব করা হয়?**
**Answer (English):**
Specificity is the weight/priority rule applied by browsers to determine which CSS rule wins when multiple rules target the same HTML element.
*   **Calculation Hierarchy (Highest to Lowest):**
    1.  **Inline styles:** `style="..."` (Score: 1000)
    2.  **ID selectors:** `#my-id` (Score: 100)
    3.  **Classes, attributes, pseudo-classes:** `.my-class`, `[type="text"]`, `:hover` (Score: 10)
    4.  **Elements and pseudo-elements:** `div`, `h1`, `::before` (Score: 1)
*   *Note:* The `!important` rule overrides all specificity scoring.

**অনুবাদ (Bangla Translation):**
স্পেসিফিসিটি হলো ব্রাউজারের অগ্রাধিকার হিসেব করার নিয়ম, যার মাধ্যমে ব্রাউজার সিদ্ধান্ত নেয় যে একটি এলিমেন্টের ওপর একাধিক ভিন্ন সিএসএস রুলস টার্গেট করা হলে শেষ পর্যন্ত কোন রুলটি কার্যকর হবে।
*   **অগ্রাধিকারের স্কোর হিসাব (বেশি থেকে কম):**
    1.  **ইনলাইন স্টাইল:** `style="..."` (স্কোর: ১০০০)
    2.  **আইডি সিলেক্টর:** `#my-id` (স্কোর: ১০০)
    3.  **ক্লাস, অ্যাট্রিবিউট ও সিউডো-ক্লাস:** `.my-class`, `:hover` (স্কোর: ১০)
    4.  **এলিমেন্ট বা ট্যাগ নেম ও সিউডো-এলিমেন্ট:** `div`, `::before` (স্কোর: ১)
*   *বিশেষ দ্রষ্টব্য:* সিএসএস-এ `!important` লিখলে তা সব স্পেসিফিসিটি স্কোর টপকে কার্যকর হয়।

---

### **Q10: What is the difference between id, class and element selector? / id, class এবং element সিলেক্টরের মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **ID Selector (`#id`):** Targets a single, unique element on the page. An ID must only be used once per HTML document. High specificity.
*   **Class Selector (`.class`):** Targets multiple elements. Classes can be reused as many times as needed across different elements. Medium specificity.
*   **Element Selector (`tag`):** Targets all elements matching the HTML tag name (e.g., `p`, `div`). Low specificity.

**অনুবাদ (Bangla Translation):**
*   **ID সিলেক্টর (`#id`):** পেজের একটি মাত্র ইউনিক এলিমেন্টকে টার্গেট করতে ব্যবহৃত হয়। এক পেজে একটি আইডি একবারই ব্যবহার করা যায়। এর স্পেসিফিসিটি বেশি।
*   **Class সিলেক্টর (`.class`):** একই সাথে একাধিক এলিমেন্টকে টার্গেট করতে পারে। এক পেজের যত খুশি তত এলিমেন্টে একই ক্লাস ব্যবহার করা সম্ভব। এর স্পেসিফিসিটি মাঝারি।
*   **Element সিলেক্টর (`tag`):** নির্দিষ্ট নামের সমস্ত HTML ট্যাগকে টার্গেট করে (যেমন- `p`, `h1`)। এর স্পেসিফিসিটি সবচেয়ে কম।

---

### **Q11: What is the difference between ::before and ::after? / ::before এবং ::after এর মধ্যে পার্থক্য কী?**
**Answer (English):**
Both are pseudo-elements used to inject decorative content into an HTML element from CSS without modifying the HTML markup. They require the `content` property to render.
*   **`::before`:** Injects content immediately *before* the actual content inside the targeted element.
*   **`::after`:** Injects content immediately *after* the actual content inside the targeted element.

**অনুবাদ (Bangla Translation):**
উভয়ই হলো সিউডো-এলিমেন্ট, যা মূল HTML ফাইল এডিট না করেই সিএসএস কোডের মাধ্যমে কোনো এলিমেন্টের ভেতরে কন্টেন্ট বা ডিজাইন যোগ করতে সাহায্য করে। এদের সচল করতে `content` প্রপার্টি ব্যবহার করা বাধ্যতামূলক।
*   **`::before`:** টার্গেট করা এলিমেন্টের ভেতরের কন্টেন্টের ঠিক *আগে* নতুন কন্টেন্ট বা ডিজাইন যোগ করে।
*   **`::after`:** টার্গেট করা এলিমেন্টের ভেতরের কন্টেন্টের ঠিক *পরে* নতুন কন্টেন্ট বা ডিজাইন যোগ করে।

---

### **Q12: What is the use of !important in CSS? / CSS-এ !important এর কাজ কী?**
**Answer (English):**
The `!important` rule in CSS is used to override all previous styling declarations and specificity calculations for a property. Once applied, this rule takes top priority over inline styles, ID selectors, or class selectors. It should be used sparingly as it makes debugging and stylesheet maintenance difficult.

**অনুবাদ (Bangla Translation):**
CSS-এ `!important` রুলটি যেকোনো প্রপার্টির পূর্ববর্তী সমস্ত স্টাইল ডিক্লারেশন এবং স্পেসিফিসিটি স্কোরকে ওভাররাইড বা বাতিল করে নিজে বলবৎ হতে ব্যবহৃত হয়। এটি ইনলাইন স্টাইল বা আইডি সিলেক্টরের ওপরও প্রভাব বিস্তার করে। এটি খুব বেশি ব্যবহার করা অনুচিত, কারণ এটি পরবর্তীতে সিএসএস ডিবাগিং ও কোড রি-রাইট করা কঠিন করে তোলে।

---

### **Q13: What are pseudo-classes in CSS? Give examples. / CSS-এ pseudo-classes কী? উদাহরণ দিন।**
**Answer (English):**
A pseudo-class is a keyword added to a selector that specifies a special state of the targeted element (such as hover states or child order).
*   **Examples:**
    *   `:hover`: Applies styles when the mouse cursor rolls over the element.
    *   `:focus`: Applies styles when the input element receives keyboard focus.
    *   `:nth-child(n)`: Targets the nth child element of a parent.
    *   `:disabled`: Targets disabled form inputs.

**অনুবাদ (Bangla Translation):**
সিউডো-ক্লাস হলো সিলেক্টরের শেষে যুক্ত হওয়া কিছু কিওয়ার্ড যা নির্দেশ করে এলিমেন্টটি বর্তমানে কোন বিশেষ অবস্থায় (State) আছে (যেমন মাউস হোভার করা বা চাইল্ড সিরিয়াল)।
*   **উদাহরণ:**
    *   `:hover`: মাউস কার্সার এলিমেন্টের ওপর নিয়ে গেলে স্টাইল কার্যকর করে।
    *   `:focus`: ইনপুট ফিল্ডে ক্লিক বা কিবোর্ড ফোকাস গেলে স্টাইল দেয়।
    *   `:nth-child(n)`: প্যারেন্ট এলিমেন্টের নির্দিষ্ট সিরিয়ালের চাইল্ডকে টার্গেট করে।
    *   `:disabled`: ডিসেবল করা ফর্ম ইনপুটগুলোকে টার্গেট করে।

---

### **Q14: What are pseudo-elements in CSS? Give examples. / CSS-এ pseudo-elements কী? উদাহরণ দিন।**
**Answer (English):**
A pseudo-element is a keyword added to a selector that lets you style a specific part of an HTML element, or insert virtual content.
*   **Examples:**
    *   `::first-letter`: Styles only the very first letter of a text block.
    *   `::placeholder`: Styles the placeholder text inside inputs.
    *   `::selection`: Styles the text portion highlighted or selected by the user.
    *   `::before` / `::after`: Injects virtual content inside elements.

**অনুবাদ (Bangla Translation):**
সিউডো-এলিমেন্ট হলো সিলেক্টরের শেষে যুক্ত হওয়া কিওয়ার্ড যা কোনো HTML এলিমেন্টের নির্দিষ্ট কোনো অংশকে স্টাইল করতে অথবা ভার্চুয়াল কন্টেন্ট তৈরি করতে ব্যবহৃত হয়।
*   **উদাহরণ:**
    *   `::first-letter`: প্যারাগ্রাফের শুধুমাত্র প্রথম অক্ষরটিকে স্টাইল করে।
    *   `::placeholder`: ইনপুট বক্সের প্লেসহোল্ডার টেক্সটটিকে স্টাইল করে।
    *   `::selection`: ইউজার মাউস দিয়ে যতটুকু টেক্সট সিলেক্ট করবেন তা স্টাইল করে।
    *   `::before` / `::after`: এলিমেন্টের আগে বা পরে ভার্চুয়াল ডিজাইন যুক্ত করে।

---

### **Q15: What is the difference between inline, inline-block and block elements? / inline, inline-block এবং block এলিমেন্টের মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`display: block`:** Takes up the full width, starts on a new line. Respects `width`, `height`, `margin`, and `padding`.
*   **`display: inline`:** Takes only as much width as its content, does not start on a new line. **Does not** respect `width` and `height` properties, and top/bottom margin/padding are ignored.
*   **`display: inline-block`:** Renders inline (does not start on a new line, takes only required width) but behaves like a block element by respecting `width`, `height`, `margin`, and `padding`.

**অনুবাদ (Bangla Translation):**
*   **`display: block`:** নতুন লাইনে শুরু হয় এবং স্ক্রিনের পুরো উইডথ নেয়। এটি উইডথ, হাইট, মার্জিন ও প্যাডিং রুলস মেনে চলে।
*   **`display: inline`:** কোনো নতুন লাইন তৈরি করে না, কন্টেন্টের সমপরিমাণ উইডথ নেয়। এটি উইডথ ও হাইট প্রপার্টি মানে না এবং এর টপ/বটম মার্জিন-প্যাডিং ঠিকমতো কাজ করে না।
*   **`display: inline-block`:** এটি ইনলাইনের মতো পাশাপাশি বসে (নতুন লাইনে যায় না) কিন্তু এটি ব্লক এলিমেন্টের মতো উইডথ, হাইট, মার্জিন এবং প্যাডিং প্রপার্টিগুলো পুরোপুরি মেনে চলে।

---

### **Q16: What is Flexbox in CSS? / CSS-এ Flexbox কী?**
**Answer (English):**
Flexbox (Flexible Box Layout) is a one-dimensional layout model in CSS3. It is designed to lay out elements in a row or a column, dynamically adjusting their width, height, and spacing to fill the available space in their container, making alignment and distribution highly efficient.

**অনুবাদ (Bangla Translation):**
ফ্লেক্সবক্স (Flexbox) হলো CSS3-এর একটি এক-মাত্রিক (One-dimensional) লেআউট মডেল। এটি কন্টেইনারের ভেতরের উপাদানগুলোকে একটি সারি (Row) বা একটি কলাম (Column) বরাবর সাজাতে এবং তাদের সাইজ ও স্পেসিং ডাইনামিকালি সাজাতে সাহায্য করে।

---

### **Q17: What are the properties of a Flex container? / একটি Flex কন্টেইনারের প্রপার্টিসমূহ কী কী?**
**Answer (English):**
The parent element containing `display: flex` gets these container properties:
1.  `flex-direction`: Sets row or column layout flow (`row`, `column`).
2.  `flex-wrap`: Controls wrapping if items exceed container width (`nowrap`, `wrap`).
3.  `justify-content`: Aligns items along the main axis (`flex-start`, `center`, `space-between`).
4.  `align-items`: Aligns items along the cross axis (`stretch`, `center`, `flex-end`).
5.  `align-content`: Controls space between flex lines when wrapping occurs.

**অনুবাদ (Bangla Translation):**
প্যারেন্ট এলিমেন্ট যাতে `display: flex` দেওয়া থাকে, তাতে এই প্রপার্টিগুলো কাজ করে:
1.  `flex-direction`: আইটেমগুলো লম্বালম্বি নাকি পাশাপাশি বসবে তা ঠিক করে (`row`, `column`)।
2.  `flex-wrap`: জায়গা না থাকলে আইটেমগুলো ভেঙে পরবর্তী লাইনে যাবে কি না তা ঠিক করে (`wrap`)।
3.  `justify-content`: মেইন অ্যাক্সিস (Main Axis) বরাবর এলাইনমেন্ট ঠিক করে (`center`, `space-between`)।
4.  `align-items`: ক্রস অ্যাক্সিস (Cross Axis) বরাবর এলাইনমেন্ট ঠিক করে (`center`, `stretch`)।
5.  `align-content`: র্যাপ হওয়া ফ্লেক্স লাইনগুলোর মাঝখানের স্পেসিং ঠিক করে।

---

### **Q18: What are the properties of a Flex item? / Flex আইটেমের প্রপার্টিসমূহ কী কী?**
**Answer (English):**
The child elements inside a flex container can accept these properties:
1.  `flex-grow`: Defines how much an item will grow relative to others if space permits.
2.  `flex-shrink`: Defines how much an item will shrink if container space is small.
3.  `flex-basis`: Defines default initial size of an item before space distribution.
4.  `flex`: Shorthand for `flex-grow`, `flex-shrink`, and `flex-basis` combined.
5.  `align-self`: Overrides default `align-items` setting for that specific item.
6.  `order`: Controls the visual display order of the item inside the container.

**অনুবাদ (Bangla Translation):**
ফ্লেক্স কন্টেইনারের ভেতরে থাকা চাইল্ড বা আইটেমগুলোতে এই প্রপার্টিগুলো দেওয়া যায়:
1.  `flex-grow`: খালি জায়গা থাকলে একটি আইটেম অন্যের তুলনায় কতটা বড় হবে তা ঠিক করে।
2.  `flex-shrink`: জায়গা কম থাকলে একটি আইটেম কতটা ছোট হবে তা ঠিক করে।
3.  `flex-basis`: স্পেস বন্টনের আগে আইটেমটির ডিফল্ট সাইজ কত হবে তা ঠিক করে।
4.  `flex`: এটি মূলত `flex-grow`, `flex-shrink` এবং `flex-basis` এর শর্টহ্যান্ড বা সংক্ষিপ্ত রূপ।
5.  `align-self`: প্যারেন্ট কন্টেইনারের `align-items` বাতিল করে নির্দিষ্ট আইটেমের নিজস্ব এলাইনমেন্ট ঠিক করে।
6.  `order`: আইটেমগুলোর ভিজ্যুয়াল পজিশন বা সিরিয়াল আগে-পিছে সরাতে সাহায্য করে।

---

### **Q19: What is CSS Grid? / CSS Grid কী?**
**Answer (English):**
CSS Grid Layout is a two-dimensional grid-based layout system. Unlike Flexbox, it handles both columns and rows at the same time, making it highly effective for designing complex web page structures, dashboards, and layouts without relying on nested divs.

**অনুবাদ (Bangla Translation):**
সিএসএস গ্রিড (CSS Grid) হলো একটি দ্বিমাত্রিক (Two-dimensional) লেআউট সিস্টেম। ফ্লেক্সবক্সের বিপরীত হিসেবে এটি একই সাথে রো (Row) এবং কলাম (Column)—উভয় অক্ষের গ্রিড লেআউট একযোগে নিয়ন্ত্রণ করতে পারে, যা জটিল ওয়েবসাইট বা ড্যাশবোর্ড বানাতে ব্যবহৃত হয়।

---

### **Q20: What is the difference between Flexbox and Grid? / Flexbox এবং Grid এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **Flexbox** is **one-dimensional** (lays out items in a single row OR single column). It is content-driven (items decide their size and layout adapts). Best for navbars or small component alignments.
*   **CSS Grid** is **two-dimensional** (lays out items in rows AND columns simultaneously). It is container-driven (the parent defines the grid tracks, and elements occupy slots). Best for complex full-page structures.

**অনুবাদ (Bangla Translation):**
*   **Flexbox** হলো **এক-মাত্রিক** (এটি কেবল সারি অথবা কলাম যেকোনো একটি অক্ষ ধরে কাজ করে)। এটি কন্টেন্ট-ড্রিভেন (ভেতরের আইটেমের সাইজ অনুযায়ী লেআউট মানিয়ে নেয়)। এটি মেনুবার বা ছোট বাটন সাজাতে ভালো।
*   **CSS Grid** হলো **দ্বি-মাত্রিক** (এটি একই সাথে সারি ও কলাম নিয়ে কাজ করে)। এটি কন্টেইনার-ড্রিভেন (প্যারেন্ট কন্টেইনারে গ্রিডের ছক কাটা থাকে এবং চাইল্ডগুলো সেই ছক দখল করে)। এটি জটিল ওয়েবসাইট লেআউটের জন্য বেস্ট।

---
---

## 03. RESPONSIVE DESIGN - INTERVIEW QUESTIONS

### **Q1: What is Responsive Web Design? / Responsive Web Design কী?**
**Answer (English):**
Responsive Web Design (RWD) is a web development approach that ensures web pages render and scale correctly across all device types and screen sizes (such as desktops, laptops, tablets, and smartphones) using a single codebase, fluid grids, flexible images, and CSS media queries.

**অনুবাদ (Bangla Translation):**
রেসপন্সিভ ওয়েব ডিজাইন (RWD) হলো এমন একটি ওয়েব ডেভেলপমেন্ট পদ্ধতি যার মাধ্যমে একটিমাত্র কোডবেস ব্যবহার করে ওয়েবসাইটকে সব ধরনের স্ক্রিন সাইজের ডিভাইসে (যেমন- ডেস্কটপ, ল্যাপটপ, ট্যাবলেট এবং স্মার্টফোন) নিখুঁতভাবে রি-সাইজ ও রেন্ডার করানো নিশ্চিত করা যায়।

---

### **Q2: Why is responsive design important? / responsive design কেন গুরুত্বপূর্ণ?**
**Answer (English):**
Responsive design is crucial because:
1.  **Mobile Traffic:** Over 50% of global web traffic comes from mobile devices.
2.  **User Experience (UX):** Users don't need to manually zoom in or scroll horizontally to read text.
3.  **SEO (Google Mobile-First Indexing):** Google ranks mobile-friendly sites higher in search results.
4.  **Cost Effective:** Building one responsive site is cheaper than maintaining separate desktop and mobile sites.

**অনুবাদ (Bangla Translation):**
রেসপন্সিভ ডিজাইন অত্যন্ত গুরুত্বপূর্ণ কারণ:
1.  **মোবাইল ট্রাফিক:** বিশ্বের ৫০% এর বেশি ট্রাফিক এখন মোবাইল ডিভাইস থেকে আসে।
2.  **ইউজার এক্সপেরিয়েন্স (UX):** ব্যবহারকারীকে মোবাইল স্ক্রিনে জুম করে বা ডানে-বামে স্ক্রল করে লেখা পড়তে হয় না।
3.  **এসইও (SEO):** গুগল মোবাইল-ফ্রেন্ডলি সাইটগুলোকে সার্চ রেজাল্টে বেশি অগ্রাধিকার দেয় (Mobile-First Indexing)।
4.  **সাশ্রয়ী:** আলাদাভাবে ডেস্কটপ ও মোবাইলের জন্য অ্যাপ না বানিয়ে একটিমাত্র রেসপন্সিভ সাইট চালানো বেশি সাশ্রয়ী।

---

### **Q3: What are the key principles of responsive design? / responsive design এর মূল নীতিসমূহ কী কী?**
**Answer (English):**
Responsive Web Design relies on three core principles:
1.  **Fluid Grids:** Layout widths must be defined in relative units like percentages (`%`) or viewport units (`vw`), rather than fixed pixels (`px`).
2.  **Flexible Media:** Images and videos must scale with their containers using properties like `max-width: 100%`.
3.  **Media Queries:** Using CSS `@media` rules to apply different styles depending on the screen width breakpoints.

**অনুবাদ (Bangla Translation):**
রেসপন্সিভ ডিজাইনের তিনটি মূল স্তম্ভ রয়েছে:
1.  **ফ্লুইড গ্রিড (Fluid Grids):** লেআউটের উইডথ পিক্সেলে (`px`) না লিখে রিলেটিভ ইউনিট যেমন পারসেন্টেজ (`%`) বা ভিউপোর্ট ইউনিটে (`vw`) লিখতে হয়।
2.  **ফ্লেক্সিবল মিডিয়া (Flexible Media):** ছবি ও ভিডিও যাতে স্ক্রিনের বাইরে চলে না যায়, তার জন্য সিএসএস-এ `max-width: 100%` ব্যবহার করা।
3.  **মিডিয়া কোয়েরি (Media Queries):** সিএসএস `@media` রুলসের সাহায্যে স্ক্রিন উইডথের ওপর ভিত্তি করে বিভিন্ন স্টাইল প্রয়োগ করা।

---

### **Q4: What is the difference between responsive design and adaptive design? / responsive design এবং adaptive design এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **Responsive Design** is fluid. The layout changes continuously and smoothly as the window is resized. It uses media queries to fluidly scale one single layout.
*   **Adaptive Design** uses static, pre-defined layouts. The server or browser detects the device type and serves a specific layout tailored for that screen resolution (e.g., serving a distinct 320px layout for mobile and 1200px layout for desktop), causing snap transitions.

**অনুবাদ (Bangla Translation):**
*   **Responsive Design** হলো ফ্লুইড বা পানির মতো তরল। ব্রাউজারের সাইজ ছোট-বড় করার সাথে সাথে লেআউটটিও মসৃণভাবে মানিয়ে নেয়। এটি একক ডিজাইনে কাজ করে।
*   **Adaptive Design** হলো ফিক্সড বা ছক-বাধা। এটি আগে থেকে তৈরি কয়েকটি নির্দিষ্ট সাইজের লেআউটের ওপর চলে (যেমন মোবাইলের জন্য ৩২০ পিক্সেল আর ডেস্কটপের জন্য ১২০০ পিক্সেলের আলাদা ডিজাইন)। ডিভাইস চিনে এটি সেই নির্দিষ্ট ডিজাইনটি লোড করায়।

---

### **Q5: What is Mobile First approach? / Mobile First অ্যাপ্রোচ কী?**
**Answer (English):**
Mobile-First design is a strategy where developers design and code the layout for the smallest screen size (mobile phone) first, and then add styles progressively for larger screens (tablets, desktops) using media queries (`min-width`). This keeps the base stylesheet lightweight and optimized for mobile performance.

**অনুবাদ (Bangla Translation):**
মোবাইল-ফার্স্ট হলো এমন একটি ডিজাইন স্ট্র্যাটেজি যেখানে ডেভেলপার প্রথমে সবচেয়ে ছোট স্ক্রিনের (মোবাইল ফোন) জন্য কোড লেখেন এবং পরবর্তীতে মিডিয়া কোয়েরির (`min-width` ব্যবহার করে) সাহায্যে ক্রমান্বয়ে বড় স্ক্রিন যেমন ট্যাবলেট ও ডেস্কটপের স্টাইল যুক্ত করেন। এতে মোবাইলের সাইটটি দ্রুত লোড হয়।

---

### **Q6: What is the use of viewport meta tag? / viewport মেটা ট্যাগের কাজ কী?**
**Answer (English):**
The viewport meta tag tells the browser how to control the scaling and dimensions of the webpage on mobile devices.
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
*   `width=device-width` matches the page width to the device's physical screen.
*   `initial-scale=1.0` sets the default zoom level.
*   *Without it*, mobile devices render the page at a standard desktop width (usually 980px) and scale down, rendering text unreadably small.

**অনুবাদ (Bangla Translation):**
ভিউ-পোর্ট মেটা ট্যাগ মোবাইল ব্রাউজারকে ওয়েব পেজের উইডথ এবং স্কেলিং কন্ট্রোল করতে বলে।
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
*   `width=device-width` পেজের উইডথকে মোবাইলের ফিজিক্যাল উইডথের সমান করে।
*   `initial-scale=1.0` ডিফল্ট জুম ১০০% রাখে।
*   *এটি না দিলে* মোবাইল ব্রাউজার ডেস্কটপ উইডথ ধরে নিয়ে পুরো পেজকে অনেক ছোট করে দেখায়, ফলে জুম করা ছাড়া লেখা পড়া যায় না।

---

### **Q7: What are media queries in CSS? / CSS-এ মিডিয়া কোয়েরি কী?**
**Answer (English):**
Media Queries are a module in CSS3 that allows applying specific styles to an HTML document depending on device characteristics, such as viewport width, orientation (portrait/landscape), or screen resolution. It uses the `@media` rule to activate CSS declarations conditionally.

**অনুবাদ (Bangla Translation):**
মিডিয়া কোয়েরি হলো CSS3-এর একটি মডিউল যা ডিভাইসের বিভিন্ন অবস্থা বা বৈশিষ্ট্যের (যেমন স্ক্রিন উইডথ, ওরিয়েন্টেশন পোর্ট্রেট/ল্যান্ডস্কেপ) ওপর ভিত্তি করে কন্ডিশনাল স্টাইল সেট করতে সাহায্য করে। এটি সিএসএস-এর `@media` রুল দিয়ে কাজ করে।

---

### **Q8: How do media queries work? / মিডিয়া কোয়েরি কীভাবে কাজ করে?**
**Answer (English):**
Media queries work by checking if a conditional expression is true. If the device matches the condition (e.g., screen width matches the breakpoint), the browser applies the CSS rules defined inside the media block, overriding default values:
```css
/* Base styles (Mobile) */
body { background: white; }

/* Media Query (Tablet/Desktop) */
@media screen and (min-width: 768px) {
  body { background: lightgrey; }
}
```

**অনুবাদ (Bangla Translation):**
মিডিয়া কোয়েরি মূলত সত্য/মিথ্যা কন্ডিশনাল রুল চেক করে কাজ করে। যদি ব্যবহারকারীর ব্রাউজার স্ক্রিন সাইজ কন্ডিশনের সাথে মিলে যায়, তবে ব্রাউজার তার ভেতরের সিএসএস কোডটি চালু করে পূর্বের স্টাইল বাতিল করে দেয়:
```css
/* বেসিক স্টাইল (মোবাইলের জন্য) */
body { background: white; }

/* মিডিয়া কোয়েরি (৭৬৮ পিক্সেলের বেশি চওড়া স্ক্রিনের জন্য) */
@media screen and (min-width: 768px) {
  body { background: lightgrey; }
}
```

---

### **Q9: What are the different media types in media queries? / মিডিয়া কোয়েরিতে বিভিন্ন মিডিয়া টাইপগুলো কী কী?**
**Answer (English):**
CSS3 supports four main media types:
1.  **`all`:** Targets all media devices.
2.  **`screen`:** Targets computer screens, smartphones, tablets (most commonly used).
3.  **`print`:** Targets documents viewed in print preview mode or printed pages.
4.  **`speech`:** Targets screen readers that read the webpage out loud.

**অনুবাদ (Bangla Translation):**
CSS3-এ মূলত চার ধরণের মিডিয়া টাইপ ব্যবহার করা যায়:
1.  **`all`:** সব ধরনের ডিভাইসের জন্য একযোগে কাজ করে।
2.  **`screen`:** কম্পিউটার স্ক্রিন, স্মার্টফোন বা ট্যাবলেটের জন্য (সবচেয়ে বেশি ব্যবহৃত)।
3.  **`print`:** প্রিন্ট প্রিভিউ বা পেজ প্রিন্ট করার সময় কেমন দেখাবে তার জন্য।
4.  **`speech`:** দৃষ্টি প্রতিবন্ধীদের জন্য স্ক্রিন রিডারের ভয়েস প্রসেসিং নির্ধারণে।

---

### **Q10: What is the difference between min-width and max-width? / min-width এবং max-width এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`min-width`:** Applies styles to screens *equal to or wider* than the specified value. Used in **Mobile-First** designs (e.g., `@media (min-width: 768px)` targets tablet screens and larger).
*   **`max-width`:** Applies styles to screens *equal to or narrower* than the specified value. Used in **Desktop-First** designs (e.g., `@media (max-width: 768px)` targets screens that are 768px wide or smaller).

**অনুবাদ (Bangla Translation):**
*   **`min-width`:** নির্দিষ্ট মানের সমান বা তার চেয়ে *বড়* চওড়া স্ক্রিনে স্টাইল প্রয়োগ করে। এটি **Mobile-First** ডিজাইনে ব্যবহৃত হয় (যেমন- min-width: 768px দিলে তার ওপরের সব বড় ডিভাইসে স্টাইল পাবে)।
*   **`max-width`:** নির্দিষ্ট মানের সমান বা তার চেয়ে *ছোট* চওড়া স্ক্রিনে স্টাইল প্রয়োগ করে। এটি **Desktop-First** ডিজাইনে ব্যবহৃত হয় (যেমন- max-width: 768px দিলে তার নিচের সব ছোট ডিভাইসে স্টাইল পাবে)।

---

### **Q11: What are breakpoints in responsive design? / responsive design-এ ব্রেকপয়েন্ট কী?**
**Answer (English):**
Breakpoints are defined screen width thresholds (usually in pixels) where the layout of the webpage changes using media queries to maintain a readable user experience.
*   **Standard Breakpoints:**
    *   Mobile: `< 576px`
    *   Tablet: `576px` to `768px`
    *   Laptops/Desktops: `768px` to `1200px`
    *   Large screens: `> 1200px`

**অনুবাদ (Bangla Translation):**
ব্রেকপয়েন্ট হলো নির্দিষ্ট স্ক্রিন উইডথ বা সীমা (সাধারণত পিক্সেলে নির্ধারিত) যেখানে পৌঁছানোর পর ওয়েব পেজের লেআউটটি মিডিয়া কোয়েরির মাধ্যমে পরিবর্তিত হয়ে নতুন রূপ নেয়।
*   **স্ট্যান্ডার্ড ব্রেকপয়েন্টসমূহ:**
    *   মোবাইল: `< ৫৭৬ পিক্সেল`
    *   ট্যাবলেট: `৫৭৬ পিক্সেল` থেকে `৭৬৮ পিক্সেল`
    *   ল্যাপটপ/ডেস্কটপ: `৭৬৮ পিক্সেল` থেকে `১২০০ পিক্সেল`
    *   বড় স্ক্রিন: `> ১২০০ পিক্সেল`

---

### **Q12: How do you handle images in responsive design? / responsive design-এ ছবি কীভাবে হ্যান্ডেল করতে হয়?**
**Answer (English):**
Images are made responsive using these techniques:
1.  **Fluid Scaling:** Set `max-width: 100%; height: auto;` in CSS. This prevents images from spilling outside their containers.
2.  **HTML `<picture>` Tag:** Serve different crops or file sizes for mobile vs desktop.
3.  **`srcset` Attribute:** Give the browser a list of different resolutions and let it choose the optimal size based on display pixel density (Retina screens).

**অনুবাদ (Bangla Translation):**
রেসপন্সিভ ডিজাইনে ইমেজ বা ছবি কন্ট্রোল করার পদ্ধতিসমূহ:
1.  **ফ্লুইড স্কেলিং:** সিএসএস-এ `max-width: 100%; height: auto;` কোড সেট করা। এতে ছবি কন্টেইনারের বাইরে বড় হতে পারে না।
2.  **HTML `<picture>` ট্যাগ:** ছোট স্ক্রিনে ছোট সাইজের ছবি ও বড় স্ক্রিনে বড় ছবি লোড করানো।
3.  **`srcset` অ্যাট্রিবিউট:** ব্রাউজারকে স্ক্রিনের ডেনসিটি (যেমন রেটিনা ডিসপ্লে) অনুযায়ী সঠিক রেজোলিউশনের ছবি ডাউনলোড করতে অপশন দেওয়া।

---

### **Q13: What is fluid grid layout? / fluid grid layout কী?**
**Answer (English):**
A fluid grid layout is a layout grid that scales proportionally depending on the screen size. Instead of locking columns to fixed pixel widths (like 300px), column widths are defined in relative percentage units (`%`) or grid fractions (`fr`), allowing columns to shrink or expand dynamically.

**অনুবাদ (Bangla Translation):**
ফ্লুইড গ্রিড লেআউট হলো এমন গ্রিড সিস্টেম যা ফিক্সড পিক্সেলে (যেমন ৩০০px) কলাম না সাজিয়ে পারসেন্টেজ (`%`) বা গ্রিড ফ্র্যাকশন (`fr`) এর মতো রিলেটিভ ইউনিটে সাজায়, যাতে স্ক্রিন পরিবর্তনের সাথে সাথে কলামগুলো সমান অনুপাতে সংকুচিত বা প্রসারিত হতে পারে।

---

### **Q14: What are relative units in CSS? (em, rem, %, vw, vh) / CSS-এ রিলেটিভ ইউনিটগুলো কী কী? (em, rem, %, vw, vh)**
**Answer (English):**
Relative units scale dynamically based on another element's size or the screen viewport dimensions:
*   **`%` (Percentage):** Relative to the parent element's size.
*   **`em`:** Relative to the font-size of the element itself (or parent).
*   **`rem` (Root EM):** Relative to the root HTML (`<html>`) font-size (defaults to 16px).
*   **`vw` (Viewport Width):** Relative to 1% of the browser window's width.
*   **`vh` (Viewport Height):** Relative to 1% of the browser window's height.

**অনুবাদ (Bangla Translation):**
রিলেটিভ ইউনিটগুলো স্ক্রিন বা প্যারেন্ট এলিমেন্টের সাইজের ওপর ভিত্তি করে ডাইনামিকালি পরিবর্তিত হয়:
*   **`%` (পারসেন্টেজ):** প্যারেন্ট এলিমেন্টের সাইজের সাপেক্ষে কাজ করে।
*   **`em`:** এলিমেন্টের নিজের ফন্ট সাইজের সাপেক্ষে কাজ করে।
*   **`rem` (রুট ইএম):** রুট HTML ট্যাগ বা ব্রাউজারের মূল ফন্ট সাইজের সাপেক্ষে কাজ করে (যা সাধারণত ১৬ পিক্সেল থাকে)।
*   **`vw` (ভিপোর্ট উইডথ):** ব্রাউজার উইন্ডোর প্রস্থ বা উইডথের ১% এর সমান।
*   **`vh` (ভিপোর্ট হাইট):** ব্রাউজার উইন্ডোর উচ্চতা বা হাইটের ১% এর সমান।

---

### **Q15: What is the difference between % and vw/vh units? / % এবং vw/vh ইউনিটের মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`%` (Percentage)** is always relative to the parent element's width/height. If a parent is 500px wide, an child with `width: 50%` will be 250px.
*   **`vw` and `vh`** are always relative to the root browser viewport window, completely ignoring the parent element's dimensions. If the viewport is 1000px, `50vw` will always be 500px, even if nested inside a 200px container.

**অনুবাদ (Bangla Translation):**
*   **`%` (পারসেন্টেজ):** এটি সর্বদা তার প্যারেন্ট বা মাদার এলিমেন্টের সাইজের সাপেক্ষে কাজ করে। প্যারেন্ট ৫০০px চওড়া হলে `width: 50%` দিলে চাইল্ড হবে ২৫০px।
*   **`vw` এবং `vh`:** এটি প্যারেন্ট এলিমেন্টকে তোয়াক্কা না করে সরাসরি পুরো ব্রাউজার স্ক্রিন বা উইন্ডোর উইডথ/হাইটের সাপেক্ষে কাজ করে। ভিউপোর্ট ১০০০px হলে `50vw` সবসময় ৫০০px হবে, তা যেকোনো ছোট ডিভের ভেতর থাকুক না কেন।

---

### **Q16: How do you make navigation menu responsive? / ন্যাভিগেশন মেনু কীভাবে রেসপন্সিভ করবেন?**
**Answer (English):**
To make a navigation menu responsive:
1.  **Desktop view:** Render links side-by-side using Flexbox or inline-blocks.
2.  **Breakpoint transition:** When reaching small screens (e.g., `< 768px`), hide the desktop navbar links using `display: none` or CSS translate.
3.  **Mobile view:** Reveal a hidden menu toggle button (hamburger icon). When clicked, use JavaScript to toggle a CSS class that slides the menu open vertically or from the side (sidebar drawer) using CSS transitions.

**অনুবাদ (Bangla Translation):**
ন্যাভিগেশন মেনু রেসপন্সিভ করার উপায়:
1.  **ডেস্কটপ ভিউ:** ফ্লেক্সবক্স দিয়ে মেনু লিংকগুলো পাশাপাশি সোজা লাইনে দেখানো হয়।
2.  **ব্রেকপয়েন্ট রূপান্তর:** মোবাইল স্ক্রিনে পৌঁছালে ডেস্কটপ মেনুটি `display: none` বা সিএসএস ট্রান্সফর্ম দিয়ে হাইড বা স্ক্রিনের বাইরে পাঠিয়ে দেওয়া হয়।
3.  **মোবাইল ভিউ:** একটি হ্যামবার্গার টগল বাটন দেখানো হয়, যাতে ক্লিক করলে জাভাস্ক্রিপ্ট ক্লাসের মাধ্যমে মেনু ড্রয়ারটি নিচ থেকে বা সাইড থেকে স্লাইড হয়ে স্ক্রিনে ভেসে ওঠে।

---

### **Q17: What is the hamburger menu? / হ্যামবার্গার মেনু কী?**
**Answer (English):**
A hamburger menu is an icon button consisting of three stacked horizontal lines (resembling a hamburger patty between two buns). It is used on mobile websites and applications to hide navigation links and save valuable screen space, expanding into a full list of menu options only when clicked.

**অনুবাদ (Bangla Translation):**
হ্যামবার্গার মেনু হলো তিনটি সমান্তরাল রেখা দিয়ে তৈরি একটি আইকন বা বাটন (যা দেখতে হ্যামবার্গারের মতো দেখায়)। এটি মোবাইল ডিভাইসে মেনু লিংকগুলো লুকিয়ে রেখে স্ক্রিনের জায়গা বাঁচাতে ব্যবহৃত হয় এবং ক্লিক করার পর মূল ন্যাভিগেশন লিংকগুলো খুলে দেয়।

---

### **Q18: How do you hide/show elements on different screen sizes? / বিভিন্ন স্ক্রিন সাইজে এলিমেন্ট লুকানো বা দেখানোর উপায় কী?**
**Answer (English):**
Elements are hidden or shown conditionally using media queries combined with the `display` property:
```css
/* Hide on mobile by default */
.desktop-only { display: none; }

/* Show on desktop screen breakpoint */
@media (min-width: 768px) {
  .desktop-only { display: block; }
}
```

**অনুবাদ (Bangla Translation):**
মিডিয়া কোয়েরি এবং `display` প্রপার্টির কম্বিনেশনে এটি করা হয়:
```css
/* মোবাইলে ডিফল্টভাবে লুকিয়ে রাখা */
.desktop-only { display: none; }

/* স্ক্রিন ৭৬৮ পিক্সেল বা তার বড় হলে দেখানো */
@media (min-width: 768px) {
  .desktop-only { display: block; }
}
```

---

### **Q19: What is the difference between px, em, rem, % and vw? / px, em, rem, % এবং vw এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`px` (Pixel):** Absolute unit, stays fixed regardless of other sizes or screens.
*   **`em`:** Relative unit. Based on the element's parent size or own font size.
*   **`rem`:** Relative unit. Based on the root `<html>` tag's font size. Best for accessibility font scaling.
*   **`%`:** Relative unit. Based on the width/height of the parent container.
*   **`vw`:** Relative unit. Based on 1% of the browser viewport width.

**অনুবাদ (Bangla Translation):**
*   **`px` (পিক্সেল):** এবসোলিউট বা ফিক্সড ইউনিট, স্ক্রিন সাইজ পরিবর্তনে এর মান পরিবর্তন হয় না।
*   **`em`:** রিলেটিভ ইউনিট, এলিমেন্টের নিজের ফন্ট সাইজ বা তার প্যারেন্টের সাইজের ওপর ভিত্তি করে বাড়ে বা কমে।
*   **`rem`:** রিলেটিভ ইউনিট, রুট HTML ফন্ট সাইজের ওপর নির্ভর করে। টেক্সট অ্যাক্সেসিবিলিটি স্কেলিংয়ের জন্য এটি সেরা।
*   **`%` (পারসেন্টেজ):** রিলেটিভ ইউনিট, মাদার কন্টেইনারের সাইজের ওপর ভিত্তি করে কাজ করে।
*   **`vw`:** রিলেটিভ ইউনিট, ব্রাউজার উইন্ডোর উইডথ বা প্রস্থের ১% এর সমান।

---

### **Q20: How do you test a website for responsiveness? / কোনো ওয়েবসাইটের রেসপন্সিভনেস কীভাবে টেস্ট করবেন?**
**Answer (English):**
You can test web responsiveness using:
1.  **Chrome DevTools (Device Mode):** Press `F12`, click the device icon, and toggle between mobile screen presets or drag the responsive handles.
2.  **Real Device Testing:** Testing on actual mobile phones and tablets.
3.  **Online Emulators:** Using tools like BrowserStack or Responsive Design Checker.
4.  **Window Resizing:** Manually resizing the desktop browser window to observe layout shifts.

**অনুবাদ (Bangla Translation):**
রেসপন্সিভনেস টেস্ট করার উপায়সমূহ:
1.  **Chrome DevTools (ডিভাইস মোড):** ব্রাউজারে `F12` চেপে কাস্টম ডিভাইস টগল অন করে বিভিন্ন মোবাইল ফ্রেম চেক করা বা হ্যান্ডেল টেনে স্ক্রিন ছোট-বড় করে দেখা।
2.  **বাস্তব ডিভাইস টেস্টিং:** সরাসরি নিজের মোবাইল বা ট্যাবলেটে ওয়েবসাইটটি ভিজিট করে টেস্ট করা।
3.  **অনলাইন এমুলেটর:** BrowserStack বা Responsive Design Checker-এর মতো অনলাইন টুল ব্যবহার করা।
4.  **উইন্ডো রিসাইজিং:** সাধারণ ব্রাউজার উইন্ডোটিকে মাউস দিয়ে টেনে ছোট-বড় করে লেআউট শিফট লক্ষ্য করা।

---
---

## 04. CSS3 ANIMATIONS & TRANSITIONS - INTERVIEW QUESTIONS

### **Q1: What is the difference between transition and animation? / transition এবং animation এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **Transition:** Animates changes of property states *triggered* by user actions (like `:hover`, `:focus`). It only has a start state and an end state, and cannot loop indefinitely.
*   **Animation:** Can run automatically without any user trigger. It is configured using `@keyframes`, allows multiple intermediate steps (frames), can loop infinitely, and supports play, pause, and reverse options.

**অনুবাদ (Bangla Translation):**
*   **Transition (ট্রানজিশন):** ব্যবহারকারীর কোনো ক্লিকের বা হোভার ইভেন্টের অ্যাকশনের পর স্টাইলের পরিবর্তনের প্রক্রিয়াকে স্মুথ বা অ্যানিমেটেড করে। এর কেবল শুরু এবং শেষ—দুটি নির্দিষ্ট স্টেট থাকে এবং এটি লুপে বারবার চালানো যায় না।
*   **Animation (অ্যানিমেশন):** ব্যবহারকারীর ইভেন্ট ছাড়াই স্বয়ংক্রিয়ভাবে চলতে পারে। এটি `@keyframes` দিয়ে নিয়ন্ত্রণ করা হয়, এতে অনেকগুলো ধাপ বা ফ্রেম তৈরি করা যায় এবং এটি ইনফিনিট লুপে চালানো সম্ভব।

---

### **Q2: What is a CSS transition? / CSS transition কী?**
**Answer (English):**
A CSS transition controls the speed of change when a CSS property value changes (e.g., color changes from blue to red on hover). It requires the properties: `transition-property`, `transition-duration` (e.g., `0.3s`), `transition-timing-function` (e.g., `ease-in`), and `transition-delay`.

**অনুবাদ (Bangla Translation):**
সিএসএস ট্রানজিশন হলো কোনো একটি প্রপার্টির মান পরিবর্তনের সময় তার ট্রানজিশন স্পিড বা গতি নির্ধারণ করার উপায় (যেমন মাউস হোভার করলে কালার নীল থেকে লাল হওয়ার গতি)। এর ৪টি অংশ থাকে: প্রপার্টি নেম, ডিউরেশন বা সময়কাল, টাইমিং ফাংশন এবং ডিলে বা বিলম্ব।

---

### **Q3: What is a CSS animation? / CSS animation কী?**
**Answer (English):**
A CSS animation is a technique that lets an HTML element transition from one style configuration to another over a timeline. It utilizes the `@keyframes` block to define styles at specific percentage points (0% to 100%) and uses the `animation` property to control duration, iteration count, and direction.

**অনুবাদ (Bangla Translation):**
সিএসএস অ্যানিমেশন হলো এমন একটি প্রযুক্তি যা সিএসএস কোডের মাধ্যমে টাইমলাইন অনুযায়ী কোনো এলিমেন্টকে স্বয়ংক্রিয়ভাবে বিভিন্ন স্টাইল বা শেপে পরিবর্তন করে। এটি নিয়ন্ত্রণে `@keyframes` ব্লকের ভেতর পারসেন্টেজ টাইমিং (০% থেকে ১০০%) সেট করে অ্যানিমেশন রুলস অ্যাসাইন করতে হয়।

---

### **Q4: What is the difference between @keyframes and transition? / @keyframes এবং transition এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`@keyframes`** is the timeline builder used by **CSS Animations**. It defines the style frames at multiple points during the animation cycle (e.g., 0%, 25%, 50%, 100%).
*   **`transition`** is a simple duration mapping. It does not use keyframes or timelines, but only manages how to interpolate values between a simple A state and B state.

**অনুবাদ (Bangla Translation):**
*   **`@keyframes`:** এটি সিএসএস অ্যানিমেশনে ব্যবহৃত টাইমলাইন তৈরির টুল। এর সাহায্যে অ্যানিমেশনের বিভিন্ন ধাপে (যেমন- ২৫%, ৫০%, ১০০%) আইটেমের অবস্থান ও কালার কেমন হবে তা স্পষ্ট ফ্রেম আকারে নির্ধারণ করা যায়।
*   **`transition`:** এটি কেবল দুটি সাধারণ স্টেট (শুরু ও শেষ) এর মধ্যকার মান পরিবর্তনের ট্রানজিশন মোশন কন্ট্রোল করে, এর কোনো টাইমলাইন বা কি-ফ্রেম থাকে না।

---

### **Q5: What are timing functions in CSS animations? / CSS animations-এ টাইমিং ফাংশন বলতে কী বোঝায়?**
**Answer (English):**
Timing functions define the acceleration curve of the animation or transition. They control how the speed varies over its duration.
*   **Common values:**
    *   `linear`: Constant speed from start to end.
    *   `ease`: Starts slow, speeds up, then ends slow (Default).
    *   `ease-in`: Starts slow, then speeds up at the end.
    *   `ease-out`: Starts fast, then slows down at the end.
    *   `cubic-bezier(p1, p2, p3, p4)`: Custom acceleration curve configured by coordinates.

**অনুবাদ (Bangla Translation):**
টাইমিং ফাংশন অ্যানিমেশন বা ট্রানজিশনের গতিবেগ বা ত্বরণ (Acceleration) কেমন হবে তা নির্ধারণ করে।
*   **কমন ভ্যালুসমূহ:**
    *   `linear`: শুরু থেকে শেষ পর্যন্ত একই স্পিডে চলে।
    *   `ease`: ধীর গতিতে শুরু হয়ে মাঝে গতি বাড়ে এবং শেষে আবার ধীর হয়।
    *   `ease-in`: ধীর গতিতে শুরু হয়ে শেষে গতি বাড়ে।
    *   `ease-out`: দ্রুত শুরু হয়ে শেষে গতি কমে যায়।
    *   `cubic-bezier()`: কাস্টম কোঅর্ডিনেট ব্যবহার করে নিজের মতো স্পিড গ্রাফ তৈরি করা।

---

### **Q6: What is the use of transform in CSS? / CSS-এ transform এর কাজ কী?**
**Answer (English):**
The `transform` property applies visual 2D or 3D transformations to an HTML element. It allows you to:
*   `translate(x, y)`: Move the element's position.
*   `scale(x, y)`: Change the element's size/zoom level.
*   `rotate(angle)`: Turn the element clockwise or counter-clockwise.
*   `skew(x-angle, y-angle)`: Slant the element along the axes.

**অনুবাদ (Bangla Translation):**
সিএসএস-এ `transform` প্রপার্টিটি কোনো এলিমেন্টকে ২ডি বা ৩ডি স্পেসে পরিবর্তন করতে সাহায্য করে। এর প্রধান মেথডসমূহ:
*   `translate(x, y)`: এলিমেন্টের অবস্থান আগে-পিছে বা ওপরে-নিচে সরায়।
*   `scale(x, y)`: এলিমেন্টের সাইজ বড় বা ছোট (Zoom) করে।
*   `rotate(angle)`: এলিমেন্টটিকে নির্দিষ্ট কোণে বা ডিগ্রিতে ঘোরায়।
*   `skew()`: এলিমেন্টটিকে কাত বা স্ল্যান্ট করে দেয়।

---

### **Q7: What are 2D and 3D transforms? Give examples. / 2D এবং 3D ট্রান্সফর্ম কী? উদাহরণ দিন।**
**Answer (English):**
*   **2D Transforms:** Alter elements along the flat X and Y axes.
    *   *Example:* `transform: translate(50px, 100px) rotate(45deg);`
*   **3D Transforms:** Alter elements along X, Y, and the Z axis (depth). It requires defining `perspective` on the parent to visualize depth.
    *   *Example:* `transform: perspective(500px) translate3d(10px, 20px, 50px) rotateY(180deg);` (creates a card flipping animation).

**অনুবাদ (Bangla Translation):**
*   **2D Transforms:** এটি ফ্ল্যাট দ্বিমাত্রিক X এবং Y অক্ষ বরাবর এলিমেন্টকে পরিবর্তন করে।
    *   *উদাহরণ:* `transform: translate(50px, 100px) rotate(45deg);`
*   **3D Transforms:** এটি X, Y এর পাশাপাশি গভীরতা বা Z-অক্ষ বরাবর কাজ করে। এটি দেখার জন্য প্যারেন্ট এলিমেন্টে `perspective` ভ্যালু সেট করতে হয়।
    *   *উদাহরণ:* `transform: rotateY(180deg);` (এটি কার্ড ফ্লিপ বা ওল্টানোর মতো অ্যানিমেশন তৈরি করে)।

---

### **Q8: What is the difference between translate(), scale(), rotate() and skew()? / translate(), scale(), rotate() এবং skew() এর মধ্যে পার্থক্য কী?**
**Answer (English):**
All are transform sub-functions:
*   **`translate()`** moves the element to a different X/Y coordinate relative to its normal position without affecting surrounding elements.
*   **`scale()`** resizes the element, magnifying it or shrinking it.
*   **`rotate()`** spins the element clockwise or counter-clockwise around a fixed transform origin point.
*   **`skew()`** distorts the element by stretching it diagonally along a specified angle.

**অনুবাদ (Bangla Translation):**
সবগুলোই ট্রান্সফর্মের সাব-মেথড:
*   **`translate()`** এলিমেন্টকে তার স্বাভাবিক অবস্থান থেকে নির্দিষ্ট উইডথ/হাইট দূরত্বে সরিয়ে দেয়।
*   **`scale()`** এলিমেন্টকে জুম বা সাইজে বড়-ছোট করে।
*   **`rotate()`** এলিমেন্টটিকে তার কেন্দ্রবিন্দুকে অক্ষ করে চারদিকে ঘোরায়।
*   **`skew()`** এলিমেন্টটিকে কোনাকুনি বা তেরছাভাবে টেনে বিকৃত বা কাত করে।

---

### **Q9: What is the use of opacity in animations? / animations-এ opacity-র কাজ কী?**
**Answer (English):**
The `opacity` property defines the transparency of an element (ranging from `0` completely invisible to `1` fully visible). In animations, it is heavily used to create **Fade-in** and **Fade-out** effects, transitions of loading overlay, and hardware-accelerated animations because changing opacity is computationally cheap and handled directly by the GPU, keeping animation frames smooth.

**অনুবাদ (Bangla Translation):**
`opacity` প্রপার্টিটি কোনো এলিমেন্টের স্বচ্ছতা নির্ধারণ করে (যার মান ০ থেকে ১ এর মধ্যে থাকে)। অ্যানিমেশনের ক্ষেত্রে এটি সাধারণত **Fade-in** (ধীরে ধীরে ভেসে ওঠা) এবং **Fade-out** (ধীরে ধীরে মিলিয়ে যাওয়া) ইফেক্ট তৈরিতে ব্যবহৃত হয়। এটি জিপিইউ (GPU) দ্বারা প্রসেস হয় বলে এর অ্যানিমেশন অত্যন্ত মসৃণ চলে।

---

### **Q10: What is the difference between visibility: hidden and opacity: 0? / visibility: hidden এবং opacity: 0 এর মধ্যে পার্থক্য কী?**
**Answer (English):**
*   **`visibility: hidden`:** The element is invisible and cannot receive any mouse click events or focus. However, it still occupies its space in the layout.
*   **`opacity: 0`:** The element is completely transparent and occupies space in the layout. Importantly, it **can still receive click events** and keyboard focuses, meaning users can accidentally click hidden buttons.

**অনুবাদ (Bangla Translation):**
*   **`visibility: hidden`:** এলিমেন্টটি অদৃশ্য হয়ে যায় এবং এটি কোনো মাউস ক্লিক বা ফোকাস গ্রহণ করতে পারে না, যদিও লেআউটে এটি নিজের জায়গাটি ধরে রাখে।
*   **`opacity: 0`:** এলিমেন্টটি সম্পূর্ণ স্বচ্ছ হয়ে যায় এবং নিজের জায়গা ধরে রাখে। তবে এটি **ক্লিক এবং কিবোর্ড ফোকাস রিসিভ করতে পারে**, অর্থাৎ কোনো অদৃশ্য বাটনেও ইউজার দুর্ঘটনাবশত ক্লিক করে ফেলতে পারেন।
