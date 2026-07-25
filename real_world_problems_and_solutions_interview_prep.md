# Real-World Engineering Problems & Solutions (STAR Method Interview Preparation)

This guide details **10 complex technical problems** faced during full-stack development across past roles (Brainhub, Simbanic Software Services, Programming HERO), how they were solved using the **STAR Method (Situation, Task, Action, Result)**, and includes complete Bangla translations for each problem.

---

## 📋 Table of Contents
1. High-Concurrency Double-Booking Race Condition (GoNautika Ferry Platform)
2. High Geospatial Query Latency in Emergency Dispatch (ResQ Roadside Assistance)
3. UI Frame Drops (30-40 FPS) & Large Bundle Size (Simbanic Frontend)
4. Frontend XSS Security Vulnerabilities & Form Re-render Lag
5. Offline Retail Checkout Failures & Inventory Sync Mismatches (EasyAcc POS)
6. Node.js Event Loop Blocking from Heavy Background Jobs (Bull Queue Solution)
7. Gemini AI Context Window Token Overflows & 429 Rate Limit Fallbacks
8. Real-Time Collaborative Canvas Latency & End-to-End Encryption (SleekDraw)
9. Production Deployment Downtime & CDN Stale Asset Caching
10. Electron Desktop Process Security (RCE Prevention) & IPC Thermal Printing

---

### **Q1: How did you solve the High-Concurrency Double-Booking problem in your Ferry Booking Platform (GoNautika)? / ফেরি বুকিং প্ল্যাটফর্মে একই সময়ে একাধিক ইউজারের একই সিট বুকিংয়ের (Double-Booking) সমস্যাটি কীভাবে সমাধান করেছিলেন?**

**Answer (English - STAR Method):**
* **Situation:** During peak holiday traffic on GoNautika (15,000+ monthly bookings), multiple users frequently selected and paid for the exact same seat at the same time, leading to booking collisions and double-booking refunds.
* **Task:** Build a high-performance, real-time concurrency locking system to ensure zero seat collisions without slowing down seat selection.
* **Action:**
  1. Implemented a **Distributed Temporary Seat Locking mechanism** using **Socket.IO** and **Redis**.
  2. When a user taps a seat, an atomic `SETNX` lock is placed in Redis with a 5-minute TTL (Time-To-Live) and a unique transaction token.
  3. Socket.IO immediately broadcasts a `seat-locked` event to all connected room clients to disable that seat on their UI instantly.
  4. Final seat confirmation is committed inside a **MongoDB Session ACID Transaction**, verifying seat lock ownership before marking it `booked`. If payment times out, Redis auto-expires the key and Socket.IO emits `seat-released`.
* **Result:** Successfully eliminated double-booking collisions completely (**0% collision rate**) for 2,000+ daily active users.

**অনুবাদ (Bangla Translation):**
* **পরিস্থিতি:** ছুটির দিনে একই সময়ে হাজার হাজার ইউজার ফেরির একই সিট বুক করার চেষ্টা করায় একাধিক বুকিং (Double-booking) হয়ে যেত এবং টাকা রিফান্ড করতে হতো।
* **লক্ষ্য:** সিট অপশনে কোনো ল্যাগ ছাড়া ডুপ্লিকেট বুকিং সম্পূর্ণ বন্ধ করার একটি রিয়েল-টাইম লকিং সিস্টেম তৈরি করা।
* **পদক্ষেপ:** Socket.IO এবং Redis ব্যবহার করে ডিস্ট্রিবিউটেড সিট লকিং তৈরি করা হয়। ইউজার সিটে চাপ দেওয়া মাত্রই Redis-এ `SETNX` দিয়ে ৫ মিনিটের জন্য সিটটি লক করা হতো এবং সকেটের মাধ্যমে সবার স্ক্রিনে তা লক হিসেবে দেখাত। পেমেন্ট শেষে MongoDB-র ACID ট্রানজ্যাকশন দিয়ে ফাইনাল বুকিং করা হতো।
* **ফলাফল:** ডাবল-বুকিং এরর কমে **০%-এ** নেমে আসে এবং দৈনিক ২,০০০+ ইউজার অনায়াসে সিট বুক করতে সক্ষম হয়।

---

### **Q2: How did you optimize geospatial query latency in your Emergency Roadside Assistance Platform (ResQ)? / ইমার্জেন্সি রোডসাইড অ্যাসিস্ট্যান্স প্ল্যাটফর্মে মেকানিক খোঁজার ল্যাটেন্সি ৪০% কমানোর টেকনিকটি কীভাবে ইমপ্লিমেন্ট করেছিলেন?**

**Answer (English - STAR Method):**
* **Situation:** In ResQ, searching for nearby mechanics among 500+ active service providers took over ~120ms per query. Node.js was pulling all mechanic records into memory to compute Haversine distances, causing server CPU spikes and slowing down emergency dispatches.
* **Task:** Reduce geospatial query latency under 20ms to achieve fast driver-to-mechanic matching requests within 2 minutes.
* **Action:**
  1. Replaced application-layer array distance math with native MongoDB **`2dsphere` Compound Indexing**: `{ location: "2dsphere", isAvailable: 1, serviceType: 1 }`.
  2. Rewrote queries using MongoDB's `$near` geospatial operator with a `$maxDistance` 10km radius constraint, delegating distance calculations directly to MongoDB's internal C++ S2 geometry library.
  3. Offloaded asynchronous driver SMS/Push notification dispatches to a **Redis-backed Bull Queue**.
* **Result:** Query execution latency dropped by **40%+** (from ~120ms to <20ms), resolving **99.9%** of emergency driver matching requests within 2 minutes.

**অনুবাদ (Bangla Translation):**
* **পরিস্থিতি:** ৫০০+ মেকানিকের অবস্থান হিসাব করতে Node.js-এ মেমোরি লোড বেড়ে কোয়েরি রান হতে ১২০ms সময় লাগত, যা জরুরি সেবায় দেরি করাচ্ছিল।
* **লক্ষ্য:** কোয়েরি ল্যাটেন্সি ২০ms-এর নিচে নামিয়ে আনা এবং ২ মিনিটের মধ্যে মেকানিক পাঠানো নিশ্চিত করা।
* **পদক্ষেপ:** MongoDB-তে GeoJSON `2dsphere` কম্পাউন্ড ইনডেক্স বসানো হয়। অ্যাপ্লিকেশনে হিসাব না করে MongoDB-র নেটিভ `$near` ও `$maxDistance` অপারেটর দিয়ে ডাটা ফিল্টার করা হয় এবং নোটিফিকেশন পাঠানোর কাজ Bull Queue-তে অফলোড করা হয়।
* **ফলাফল:** কোয়েরি টাইম **৪০%+ কমে ২০ms-এর নিচে** চলে আসে এবং ৯৯.৯% ইমার্জেন্সি রিকোয়েস্ট ২ মিনিটের মধ্যে প্রসেস হয়।

---

### **Q3: How did you fix UI rendering frame drops (30-40 FPS) and large initial bundle size at Simbanic? / Simbanic-এ ইউআই ল্যাগ (৩০-৪০ FPS) এবং ভারী ফাইল সাইজ কমানোর জন্য কী কী পদক্ষেপ নিয়েছিলেন?**

**Answer (English - STAR Method):**
* **Situation:** The main React dashboard suffered from severe render lag, dropping frame rates to 30-40 FPS during state updates, while the initial JavaScript bundle size inflated to ~1.2MB, slowing initial page load (FCP).
* **Task:** Lock rendering performance at a smooth 60 FPS and shrink the initial JavaScript bundle size by at least 25%.
* **Action:**
  1. Migrated unoptimized React Context/Redux stores to **Zustand**, applying `useShallow` store selectors to prevent unnecessary component tree re-renders.
  2. Restricted Framer Motion dashboard animations strictly to GPU-accelerated CSS properties (`transform`, `opacity`).
  3. Implemented route-based code-splitting using `React.lazy()` and `<Suspense>`, while dynamically importing heavy third-party modules (Chart.js, Rich Text Editor) on demand.
* **Result:** Achieved steady **60 FPS rendering** and reduced the main entry bundle size by **30%** (from ~1.2MB to ~840KB).

**অনুবাদ (Bangla Translation):**
* **পরিস্থিতি:** রিয়্যাক্ট ড্যাশবোর্ডে স্টেট পাল্টালেই পুরো পেজ রি-রেন্ডার হয়ে ফ্রেম রেট ৩০-৪০ FPS-এ নেমে যেত এবং বান্ডেল সাইজ ১.২MB হওয়ার কারণে ওয়েবসাইট স্লো লোড হতো।
* **লক্ষ্য:** পারফরম্যান্স ৬০ FPS-এ স্থায়ী করা এবং ফাইল সাইজ অন্তত ২৫% কমানো।
* **পদক্ষেপ:** Zustand-এর `useShallow` সিলেক্টর ব্যবহার করে অনাকাঙ্ক্ষিত রি-রেন্ডার বন্ধ করা হয়। Framer Motion-এ কেবল সিএসএস `transform` ও `opacity` ব্যবহার করা হয় এবং `React.lazy()` দিয়ে ফাইল কোড-স্প্লিটিং করা হয়।
* **ফলাফল:** রেন্ডারিং পারফরম্যান্স **৬০ FPS**-এ লক হয় এবং মূল ফাইল সাইজ **৩০% কমে ৮৪০KB**-তে চলে আসে।

---

### **Q4: How did you handle frontend XSS security vulnerabilities and input form re-render lag? / ফ্রন্টএন্ড XSS সিকিউরিটি ঝুঁকি এবং ফর্মে টাইপিং ল্যাগ কীভাবে দূর করেছিলেন?**

**Answer (English - STAR Method):**
* **Situation:** Traditional controlled React inputs were re-rendering entire forms on every single keystroke, causing visible typing lag. Additionally, user-generated rich text inputs posed XSS vulnerabilities, and external links lacked secure attributes.
* **Task:** Eliminate form input re-render lag and enforce enterprise-grade frontend security against XSS and tabnabbing.
* **Action:**
  1. Replaced controlled inputs with **React Hook Form** (uncontrolled inputs via `ref`s) paired with **Zod schema validation** (`zodResolver`).
  2. Sanitized all dynamic user-generated HTML rendered on the DOM using **DOMPurify** (`DOMPurify.sanitize()`) to strip malicious `<script>` tags and event handlers.
  3. Enforced `rel="noopener noreferrer"` attributes on all external `<a target="_blank">` links to prevent reverse tabnabbing attacks.
* **Result:** Completely eliminated input re-render lag, achieved instant inline form validation, and fortified application frontend security.

**অনুবাদ (Bangla Translation):**
* **পরিস্থিতি:** ফর্মে প্রতিটা অক্ষর টাইপ করলে পুরো কম্পোনেন্ট রি-রেন্ডার হয়ে ল্যাগ হতো। এছাড়া ইউজারের ইনপুটে XSS হ্যাকিংয়ের ঝুঁকি ছিল।
* **লক্ষ্য:** ফর্মে টাইপিং ল্যাগ দূর করা এবং XSS ও Tabnabbing হ্যাকিং থেকে অ্যাপ সুরক্ষিত করা।
* **পদক্ষেপ:** React Hook Form ও Zod Schema ব্যবহার করে আনকন্ট্রোল্ড ইনপুট আনা হয়। ডম-এ ডাটা দেখানোর আগে **DOMPurify** দিয়ে ক্ষতিকারক কোড ফিল্টার করা হয় এবং বাহ্যিক লিংকে `rel="noopener noreferrer"` বাধ্যতামূলক করা হয়।
* **ফলাফল:** টাইপিং ল্যাগ ১০০% দূর হয় এবং ফ্রন্টএন্ড নিরাপত্তা শক্তিশালী হয়।

---

### **Q5: How did you solve offline retail checkout failures and inventory data mismatches in EasyAcc POS? / EasyAcc POS অ্যাপে ইন্টারনেট অফলাইন হয়ে গেলে চেকআউট ফেল করা এবং ডাটা অমিলের সমস্যা কীভাবে সমাধান করেছিলেন?**

**Answer (English - STAR Method):**
* **Situation:** In retail store environments, internet outages caused traditional web POS checkouts to crash, while manual offline tallying resulted in inventory record mismatches and stock calculation errors.
* **Task:** Build an offline-first desktop POS app capable of processing checkouts without internet and syncing data to MongoDB with 100% reliability upon reconnection.
* **Action:**
  1. Built an Electron.js desktop shell integrated with **RxDB** and **Dexie.js (IndexedDB)** to handle reactive local transaction storage.
  2. Enabled cashiers to complete checkouts locally offline instantly; transactions were saved to IndexedDB's `pending_sync` queue.
  3. Built a background replication engine that detected network status (`online`). Upon reconnection, it pushed queued sales to Express via bulk sync APIs, wrapping backend inventory updates inside **Mongoose ACID Transactions** (`$inc: { stock: -qty }`).
* **Result:** Enabled **1,200+ offline checkouts** with **100% database sync reliability** and reduced inventory stock mismatches to strictly **0%**.

**অনুবাদ (Bangla Translation):**
* **পরিস্থিতি:** দোকানে ইন্টারনেট চলে গেলে ক্যাশিয়ারের চেকআউট বন্ধ হয়ে যেত এবং হাতে কলমে হিসাব রাখায় ডাটাবেজের স্টকের সাথে আসল স্টকের অমিল হতো।
* **লক্ষ্য:** ইন্টারনেট ছাড়াও যেন চেকআউট করা যায় এবং নেট আসামাত্রই ১০০% সঠিক ডাটা সিঙ্ক হওয়ার ব্যবস্থা করা।
* **পদক্ষেপ:** Electron.js, RxDB এবং Dexie.js (IndexedDB) দিয়ে অফলাইন অ্যাপ বানানো হয়। অফলাইনে চেকআউট করলে ডাটা লোকাল ইনডেক্সড-ডিবিতে জমতো। ইন্টারনেট আসামাত্রই ব্যাকগ্রাউন্ড সিঙ্ক দিয়ে MongoDB-র **ACID Transactions**-এর মাধ্যমে স্টক আপডেট করা হতো।
* **ফলাফল:** **১,২০০+ অফলাইন চেকআউট** সফলভাবে সম্পন্ন হয় এবং ডাটাবেজ স্টকের অমিল **০%-এ** নেমে আসে।

---

### **Q6: How did you prevent Node.js API Event Loop Blocking caused by heavy background tasks? / ভারী ব্যাকগ্রাউন্ড কাজের জন্য Node.js API ব্লক হওয়া কীভাবে আটকিয়েছিলেন?**

**Answer (English - STAR Method):**
* **Situation:** Heavy background tasks (generating PDF receipts, processing batch email notifications, telemetry data logging) were executed directly inside Express route handlers, blocking the single-threaded Node.js event loop and causing API HTTP 504 gateway timeouts.
* **Task:** Decouple heavy background jobs from the main HTTP request-response cycle to keep API endpoints fast and responsive (<100ms).
* **Action:**
  1. Integrated **Bull Queue** backed by **Redis**.
  2. When an API endpoint is hit, Express immediately pushes a job payload to Bull (`queue.add(data)`) and returns an instant HTTP `202 Accepted` response.
  3. Created isolated background **Worker Processes** (`queue.process(concurrency, handler)`) to consume and process jobs asynchronously with automatic exponential backoff retries.
* **Result:** Offloaded **10,000+ daily background tasks** without impacting main API latency, maintaining sub-100ms HTTP responses.

**অনুবাদ (Bangla Translation):**
* **পরিস্থিতি:** পিডিএফ ফাইল তৈরি করা বা ইমেইল পাঠানোর ভারী কাজগুলো সরাসরি এপিআইতে করায় Node.js থ্রেড ব্লক হয়ে পেজ স্লো ও টাইমআউট হয়ে যেত।
* **লক্ষ্য:** এপিআই-এর গতি ১০০ms-এর নিচে রাখা এবং কাজগুলোকে ব্যাকগ্রাউন্ডে নিয়ে যাওয়া।
* **পদক্ষেপ:** Redis-বেসড **Bull Queue** যুক্ত করা হয়। এপিআই রিকোয়েস্ট আসামাত্রই রেসপন্স দিয়ে জব কিউতে পাঠিয়ে দেওয়া হতো এবং ব্যাকগ্রাউন্ডে আলাদা কন্সুমার প্রসেস দিয়ে কাজ করানো হতো।
* **ফলাফল:** প্রতিদিন **১০,০০০+ ব্যাকগ্রাউন্ড টাস্ক** স্মুথলি প্রসেস হতো এবং এপিআই রেসপন্স ১০০ms-এর নিচে নেমে আসে।

---

### **Q7: How did you handle Gemini AI Context Window Token Overflows and HTTP 429 Rate Limits in production? / Gemini AI-এর টোকেন পার হয়ে যাওয়া এবং 429 Rate Limit এরর কীভাবে হ্যান্ডেল করেছিলেন?**

**Answer (English - STAR Method):**
* **Situation:** Long user interactions in GoNautika's AI support assistant caused conversation history to exceed Gemini AI's token limit, while peak user traffic triggered HTTP 429 (Too Many Requests) rate limit errors.
* **Task:** Maintain responsive, context-aware AI conversations without exceeding model context windows or crashing on API rate limits.
* **Action:**
  1. Managed a **Rolling Context Window in Redis** using `LTRIM` to retain only the last 10-12 conversation turns per session, truncating older messages before forwarding to Gemini.
  2. Wrapped Gemini SDK API calls with exponential backoff retries (`p-retry`) to handle HTTP 429 responses gracefully.
  3. Built a **Model Fallback Hierarchy**: If `gemini-1.5-pro` timed out (>3000ms), auto-downgraded to `gemini-1.5-flash`. If all AI services failed, automatically degraded to a rule-based algorithm.
* **Result:** Guaranteed **100% platform uptime**, eliminated token overflow errors, and kept AI response latency below 3 seconds.

**অনুবাদ (Bangla Translation):**
* **পরিস্থিতি:** ইউজার বেশিক্ষণ চ্যাট করলে AI-এর টোকেন লিমিট পার হয়ে যেত এবং ট্রাফিক বেশি হলে HTTP 429 (Rate Limit) এরর আসত।
* **লক্ষ্য:** চ্যাট সিস্টেম সবসময় চালু রাখা এবং টোকেন বা রেট লিমিট এরর আটকানো।
* **পদক্ষেপ:** Redis-এ `LTRIM` দিয়ে চ্যাটের শেষ ১০-১২টি মেসেজ সেভ রাখা হতো। 429 এরর আসলে `p-retry` দিয়ে রি-ট্রাই এবং ভারী মডেল `pro` স্লো হলে দ্রুতগতির `flash` মডেলে অটো-সুইচ করানো হতো।
* **ফলাফল:** প্ল্যাটফর্মের Uptime **১০০% অর্জিত হয়** এবং টোকেন বা রেট লিমিটজনিত ক্র্যাশ বন্ধ হয়।

---

### **Q8: How did you achieve <50ms rendering latency and End-to-End Encryption in SleekDraw Collaborative Whiteboard? / SleekDraw কোলাবোরেটিভ বোর্ডে ৫০ms-এর কম ল্যাটেন্সি এবং End-to-End Encryption কীভাবে ইমপ্লিমент করেছিলেন?**

**Answer (English - STAR Method):**
* **Situation:** In SleekDraw, multi-user real-time drawing suffered from cursor stutters and lag over WebSockets, while users demanded strict data privacy so server administrators could not view raw drawing diagrams.
* **Task:** Deliver sub-50ms canvas stroke rendering while securing diagram data with browser-side End-to-End Encryption (E2EE).
* **Action:**
  1. Combined HTML5 **Canvas API** with **WebSockets**. Vector stroke updates were batched and rendered using `requestAnimationFrame` for maximum GPU performance.
  2. Implemented client-side E2EE using browser **Web Crypto API (AES-GCM 256-bit)**. Vector coordinates were encrypted in the browser before being emitted over WebSockets or saved to the DB.
  3. Shared decryption keys strictly via URL hash fragments (`#key=...`), keeping keys client-side only (Zero-Knowledge Backend).
* **Result:** Delivered smooth **<50ms collaborative rendering latency** while ensuring complete zero-knowledge data encryption.

**অনুবাদ (Bangla Translation):**
* **পরিস্থিতি:** একাধিক ইউজার একসাথে বোর্ডে আঁকার সময় কার্সার ল্যাগ করত এবং সার্ভার অনার যেন ড্রয়িং দেখতে না পারে তার সিকিউরিটি দরকার ছিল।
* **লক্ষ্য:** ৫০ms-এর নিচে দ্রুত রেন্ডারিং এবং এন্ড-টু-এন্ড এনক্রিপশন (E2EE) চালু করা।
* **পদক্ষেপ:** HTML5 Canvas ও WebSockets দিয়ে `requestAnimationFrame`-এর মাধ্যমে রেন্ডার করা হয়। ডাটা সকেটে পাঠানোর আগে ব্রাউজারের Web Crypto API (**AES-GCM 256-bit**) দিয়ে এনক্রিপ্ট করা হয়, যার ডিক্রিপশন কি কেবল ইউজারের ইউআরএল হ্যাশে থাকত।
* **ফলাফল:** **<৫০ms ল্যাটেন্সিতে** ড্রয়িং ড্র করা সম্ভব হয় এবং শতভাগ এনক্রিপশন নিশ্চিত হয়।

---

### **Q9: How did you eliminate production deployment downtime and resolve CloudFront CDN stale asset caching? / প্রোডাকশন রিলিজের সময় ওয়েবসাইট ডাউন হওয়া এবং ক্যাশিং সমস্যা কীভাবে দূর করেছিলেন?**

**Answer (English - STAR Method):**
* **Situation:** Restarting Express servers during code deployments caused brief site outages (HTTP 502 Bad Gateway), while deploying updated React frontend bundles to AWS S3 resulted in users seeing old cached versions due to CloudFront CDN caching.
* **Task:** Achieve 100% zero-downtime backend deployments and ensure users instantly receive updated frontend assets upon release.
* **Action:**
  1. Implemented **PM2 Reload / Cluster Mode** on the Node.js backend. `pm2 reload` restarts worker instances sequentially one-by-one, maintaining active workers to serve traffic while others update.
  2. Built a **GitHub Actions CI/CD Pipeline**: Uploaded compiled React build bundles (`dist/`) to AWS S3 with unique content-hashed filenames.
  3. Added an automated step in GitHub Actions executing an **AWS CloudFront Cache Invalidation** (`aws cloudfront create-invalidation --distribution-id ... --paths "/*"`).
* **Result:** Achieved **100% zero-downtime releases** and guaranteed that users immediately fetched updated frontend code upon deployment.

**অনুবাদ (Bangla Translation):**
* **পরিস্থিতি:** নতুন কোড দিলে সার্ভার বন্ধ হয়ে ইউজার ৫০২ এরর পেত এবং ক্যাশিংয়ের কারণে আপডেট ফাইল দেখতে পেত না।
* **লক্ষ্য:** জিরো-ডাউনটাইম রিলিজ এবং ডিপ্লয় হওয়ামাত্রই ইউজারের কাছে নতুন ফাইল পৌঁছানো।
* **পদক্ষেপ:** ব্যাকএন্ডে **PM2 Reload** ব্যবহার করা হয় যাতে প্রসেস একটি একটি করে রিস্টার্ট হয়। গিটহাব অ্যাকশনস CI/CD দিয়ে AWS S3-তে ফাইল আপলোড এবং সাথে সাথে **CloudFront Cache Invalidation** করা হয়।
* **ফলাফল:** **১০০% Zero-Downtime** রিলিজ অর্জিত হয় এবং সাথে সাথে নতুন কোড ক্লায়েন্টে আপডেট হয়।

---

### **Q10: How did you resolve Electron Desktop Main vs Renderer process bottlenecks and secure the app against Remote Code Execution (RCE)? / Electron ডেস্কটপ অ্যাপে RCE হ্যাকিং প্রতিরোধ এবং থার্মাল প্রিন্টিং ল্যাগ কীভাবে সমাধান করেছিলেন?**

**Answer (English - STAR Method):**
* **Situation:** In the EasyAcc desktop app, giving the React renderer process direct Node.js access exposed Remote Code Execution (RCE) vulnerabilities. Furthermore, attempting to execute thermal receipt printing directly from the renderer process froze the React UI.
* **Task:** Secure the Electron application architecture against RCE exploits while offloading thermal receipt printing cleanly to native hardware.
* **Action:**
  1. Hardened Electron security by setting `nodeIntegration: false` and `contextIsolation: true` in `BrowserWindow` options.
  2. Created a secure IPC bridge in `preload.js` using `contextBridge.exposeInMainWorld()`, exposing only explicit whitelisted methods.
  3. When a cashier prints a receipt, React emits an asynchronous `ipcRenderer.invoke('print-receipt', data)` call. The Node.js **Main Process** receives the event via `ipcMain.handle`, formats ESC/POS commands, and prints silently to the USB thermal printer without blocking the UI.
* **Result:** Completely fortified the app against RCE vulnerabilities while enabling smooth, non-blocking silent thermal receipt printing.

**অনুবাদ (Bangla Translation):**
* **পরিস্থিতি:** ফ্রন্টএন্ড রেন্ডারার প্রসেসে নোড-জেএস এক্সেস থাকায় RCE হ্যাকিংয়ের ঝুঁকি ছিল এবং রেন্ডারার থেকে সরাসরি প্রিন্ট দিতে গেলে ইউআই ফ্রিজ হয়ে যেত।
* **লক্ষ্য:** RCE হ্যাকিং থেকে অ্যাপ বাঁচানো এবং ইউআই ল্যাগ ছাড়া থার্মাল প্রিন্ট দেওয়া।
* **পদক্ষেপ:** Electron-এ `nodeIntegration: false` এবং `contextIsolation: true` সেট করা হয়। `preload.js`-এ `contextBridge` দিয়ে নিরাপদ মেথড ব্রাউজারে দেওয়া হয়। প্রিন্টের কাজ IPC ইভেন্টের মাধ্যমে **Main Process**-এ পাঠিয়ে নীরব (Silent) প্রিন্ট দেওয়া হয়।
* **ফলাফল:** RCE হ্যাকিং ঝুঁকি ১০০% বন্ধ হয় এবং কোনো ল্যাগ ছাড়াই থার্মাল রিসিপ্ট প্রিন্ট সম্পন্ন হয়।
