# Mid-Level Full-Stack Engineer (Brainhub Role) Interview Questions & Answers

This guide contains 18 in-depth, scenario-based interview questions tailored specifically to your experience and key achievements as a **Mid-Level Full-Stack Engineer at Brainhub**, with a dedicated deep-dive into your **Projects, Features, and AI Integration** architecture. Each question includes a comprehensive technical answer in English and a complete Bangla translation.

---

## Table of Contents
1. Real-Time Seat Locking & Race Condition Prevention (Ferry Booking)
2. Payment Webhook Reliability & Transaction Idempotency (Razorpay)
3. MongoDB `2dsphere` Indexing & Geospatial Query Optimization (40% Latency Reduction)
4. AI-Driven Dispatch Matching Speed Improvement by 35% (Gemini AI + Redux Toolkit)
5. Processing 10k+ Daily Background Jobs using Redis and Bull Queues
6. Managing High-Frequency Real-Time Telemetry Data in Next.js without UI Lag
7. Building PWA & Offline Support for Fleet Management Dashboards
8. Integrating Gemini AI Assistant into a Real-Time React/Socket.IO Architecture
9. Securing an Express Backend & Real-Time WebSocket Connections
10. Animation Performance & Layout Optimization with Framer Motion in Next.js
11. Prompt Engineering & Rolling Context Window Management for Conversational AI (Gemini + Redis)
12. Enforcing Structured JSON Outputs & Function Calling in Gemini AI for Automated Dispatching
13. Managing Gemini AI Rate Limits, Timeouts, Retries, and Model Fallbacks in Production
14. Implementing Retrieval-Augmented Generation (RAG) & Vector Search for AI Support
15. Preventing Prompt Injection Attacks & Protecting PII in AI Integration Pipelines
16. Overview: What types of AI features have you built across your projects?
17. Integration Blueprint: How did you technically integrate these AI features into your MERN / Full-Stack stack?
18. Projects & Core Features Overview: What type of production projects have you built for Brainhub, and what are their core technical features?

---

### **Q1: In your ferry booking platform with 15,000+ monthly bookings, how did you handle concurrent seat selection to prevent double-booking? / ১৫,০০০+ মাসিক বুকিং সম্বলিত ফেরি বুকিং প্ল্যাটফর্মে ডাবল-বুকিং প্রতিরোধে একাধিক ইউজার একসাথে সিট সিলেক্ট করার বিষয়টি কীভাবে পরিচালনা করেছেন?**

**Answer (English):**
To prevent double-booking during high-traffic concurrency, I implemented a **Distributed Temporary Seat Locking mechanism** using **Socket.IO and Redis**:
*   **Temporary Reservation:** When a user selects a seat, a Socket.IO event (`select-seat`) is emitted. The backend attempts to acquire an atomic lock in Redis for that specific `ferry_id` and `seat_number` with a TTL (e.g., 5-10 minutes) using `SETNX` (or Redlock algorithm).
*   **Real-time Broadcast:** If the lock succeeds, Socket.IO broadcasts a `seat-locked` event to all active clients connected to that ferry room, updating their UI state instantly.
*   **Expiration & Cleanup:** If the user fails to complete payment within the TTL window, Redis automatically expires the key, releasing the seat. A Socket.IO `seat-released` event is emitted to make the seat available again.
*   **Database Transaction:** Final seat assignment is committed to MongoDB using an ACID transaction inside a session, verifying that the seat status is still "locked" by the current `user_id` before marking it "booked".

**অনুবাদ (Bangla Translation):**
উচ্চ ট্রাফিকের সময় একই সিট একাধিক ইউজার একসাথে বুক করা (Double-Booking) ঠেকাতে আমি **Socket.IO এবং Redis** ব্যবহার করে একটি **ডিস্ট্রিবিউটেড সাময়িক সিট লক মেকানিজম** বাস্তবায়ন করেছি:
*   **সাময়িক রিজার্ভেশন:** ইউজার সিট সিলেক্ট করলেই একটি Socket.IO ইভেন্ট (`select-seat`) ট্রিগার হয়। ব্যাকএন্ড `SETNX` ব্যবহার করে Redis-এ ওই নির্দিষ্ট ফেরি ও সিট নম্বরের জন্য ৫-১০ মিনিটের একটি পারমাণবিক (Atomic) লক বসায়।
*   **রিয়েল-টাইম ব্রডকাস্ট:** লক সফল হলে Socket.IO ওই ফেরির সাথে যুক্ত সমস্ত ইউজারের কাছে `seat-locked` ইভেন্ট ব্রডকাস্ট করে, যা সবার ইউআই-তে সিটটি লক হিসেবে দেখায়।
*   **অটো-রিলিজ:** নির্ধারিত সময়ের মধ্যে ইউজার পেমেন্ট সম্পন্ন করতে না পারলে Redis-এর TTL মেয়াদে কি (Key) এক্সপায়ার হয়ে যায় এবং Socket.IO `seat-released` ইভেন্টের মাধ্যমে সিটটি পুনরায় উন্মুক্ত করে দেয়।
*   **ডাটাবেজ ট্রানজ্যাকশন:** পেমেন্ট শেষে MongoDB-র ACID ট্রানজ্যাকশন ব্যবহার করে চূড়ান্তভাবে সিটটি "booked" হিসেবে সেট করা হয়।

---

### **Q2: How did you ensure payment processing reliability and idempotency when integrating Razorpay? / Razorpay পেমেন্ট ইন্টিগ্রেশনের সময় পেমেন্ট প্রসেসিংয়ের নির্ভরযোগ্যতা এবং আইডেমপোটেন্সি (Idempotency) কীভাবে নিশ্চিত করেছেন?**

**Answer (English):**
Handling payment gateways requires strict idempotency and resilient fallback handling:
*   **Order Creation & Signature Verification:** The server creates a unique Razorpay `order_id` associated with a pending booking ID. Upon client payment completion, the backend verifies the HMAC-SHA256 signature calculated from `razorpay_order_id`, `razorpay_payment_id`, and the secret key before updating the database.
*   **Handling Webhooks:** Since client-side redirects can fail (e.g., browser closure or network dropouts), I implemented **Razorpay Webhooks** (`payment.captured`, `payment.failed`).
*   **Idempotency:** Webhook events are checked against a Redis cache or database log of processed `payment_id`s. If a duplicate webhook arrives, it is safely ignored to prevent double processing of bookings.
*   **Reconciliation:** If payment succeeds via webhook before the client redirect completes, the database transaction marks the booking as confirmed, ensuring zero loss of revenue or booking data.

**অনুবাদ (Bangla Translation):**
পেমেন্ট গেটওয়ের নির্ভরযোগ্যতা এবং আইডেমপোটেন্সি সুনিশ্চিত করতে নিচের পদক্ষেপগুলো নেওয়া হয়েছিল:
*   **অর্ডার তৈরি ও সিগনেচার যাচাই:** সার্ভারে বুকিংয়ের জন্য একটি ইউনিক Razorpay `order_id` তৈরি করা হয়। ইউজার পেমেন্ট করলে ব্যাকএন্ডে HMAC-SHA256 হ্যাশ সিগনেচার যাচাই করার পরেই কেবল ডাটাবেজে বুকিং কনফার্ম করা হয়।
*   **ওয়েবহুক (Webhooks) হ্যান্ডলিং:** নেটওয়ার্ক বিচ্ছিন্নতা বা ব্রাউজার বন্ধ হয়ে যাওয়ার কারণে ক্লায়েন্ট রিডাইরেক্ট মিস হতে পারে। এজন্য **Razorpay Webhooks** (`payment.captured`) ব্যবহার করা হয়েছে।
*   **আইডেমপোটেন্সি:** ডুপ্লিকেট ওয়েবহুক রিকোয়েস্ট এড়াতে প্রসেস করা `payment_id`গুলো Redis-এ ট্র্যাক করা হয়, যাতে একটি পেমেন্ট একাধিকবার ডাটাবেজে এন্ট্রি না হয়।
*   **রিকনসিলিয়েশন:** ক্লায়েন্ট রিডাইরেক্টের আগেই ওয়েবহুকের মাধ্যমে ডেটা নিশ্চিত হয়ে সিট বুকিং চূড়ান্ত করা হয়।

---

### **Q3: How did you optimize geospatial queries in MongoDB using `2dsphere` indexes to reduce latency by 40%? / MongoDB-র `2dsphere` ইনডেক্স ব্যবহার করে জিয়োস্পেশিয়াল (Geospatial) কোয়েরির ল্যাটেন্সি ৪০% কমানোর টেকনিকটি কীভাবে ইমপ্লিমেন্ট করেছিলেন?**

**Answer (English):**
In the emergency roadside assistance platform tracking 500+ active service providers, finding nearby providers efficiently was critical:
*   **`2dsphere` Indexing:** Created a `2dsphere` index on the GeoJSON `location` field (formatted as `{ type: "Point", coordinates: [longitude, latitude] }`) of the providers collection.
*   **Query Optimization (`$near` vs `$geoWithin`):** Used MongoDB's `$near` / `$nearSphere` operator with `$maxDistance` (e.g., within a 10km radius) instead of loading all active providers and calculating distances on the Node.js application layer.
*   **Compound Indexing:** Created a compound geospatial index `{ location: "2dsphere", isAvailable: 1, serviceType: 1 }`. This allowed MongoDB to filter only available, relevant mechanics in a single indexed B-tree traversal.
*   **Result:** Reduced query execution time from ~120ms to under ~20ms (a 40%+ latency drop) and offloaded distance calculations directly to MongoDB's internal S2 geometry library.

**অনুবাদ (Bangla Translation):**
৫০ জন+ অ্যাক্টিভ সার্ভিস প্রোভাইডারকে রিয়েল-টাইমে ট্র্যাক করার জন্য এবং দ্রুত নিকটের মেকানিক খুঁজে বের করতে জিয়োস্পেশিয়াল কোয়েরি অপ্টিমাইজ করা হয়েছিল:
*   **`2dsphere` ইনডেক্সিং:** প্রোভাইডারদের GeoJSON `location` ফিল্ডের উপর `2dsphere` ইনডেক্স বসানো হয়েছিল (`{ type: "Point", coordinates: [longitude, latitude] }`)।
*   **কোয়েরি অপ্টিমাইজেশন:** অ্যাপ্লিকেশনে সব মেকানিকের ডেটা এনে ডিস্টেন্স হিসাব না করে MongoDB-র নেটিভ `$near` বা `$nearSphere` অপারেটরের সাথে `$maxDistance` ব্যবহার করা হয়েছে।
*   **কম্পাউন্ড ইনডেক্সিং:** `{ location: "2dsphere", isAvailable: 1, serviceType: 1 }` কম্পাউন্ড ইনডেক্স ব্যবহার করা হয়েছিল, যা একই সাথে নিকটবর্তী এবং ফ্রি থাকা মেকানিকদের ফিল্টার করতে সাহায্য করে।
*   **ফলাফল:** কোয়েরি এক্সিকিউশন টাইম ১২০ms থেকে কমে ২০ms-এর নিচে চলে আসে (৪০% ল্যাটেন্সি হ্রাস)।

---

### **Q4: How did you combine Gemini AI and Redux Toolkit to improve emergency dispatch matching speed by 35%? / Gemini AI এবং Redux Toolkit এর মেলবন্ধনে ইমার্জেন্সি ডিসপ্যাচ ম্যাচিং স্পিড ৩৫% বৃদ্ধি করার কৌশলটি ব্যাখ্যা করুন।**

**Answer (English):**
To match stranded drivers with the best-suited roadside assistance providers rapidly:
*   **AI-Powered Scoring (Gemini AI):** Instead of simple linear distance matching, Gemini AI was integrated to analyze complex dispatch variables—including service provider skill set, vehicle equipment (e.g., flatbed vs. tow truck), traffic conditions, and historical response times—generating an optimal match confidence score.
*   **Redux Toolkit for Real-Time Dispatch State:** On the admin/dispatch frontend, Redux Toolkit was structured using `createSlice` and `createEntityAdapter` to handle incoming provider status updates and location broadcasts via WebSockets.
*   **Optimized Store & Normalized State:** By keeping the Redux store normalized (`ids` and `entities`), dispatchers could filter and auto-assign 500+ active mechanics without triggering unnecessary component re-renders.
*   **Speed Impact:** Automating candidate ranking with Gemini AI and enabling instant optimistic updates in Redux Toolkit reduced the average manual dispatch selection time by 35%.

**অনুবাদ (Bangla Translation):**
দুর্ঘটনায় পড়া ড্রাইভারদের দ্রুত উপযুক্ত রোডসাইড মেকানিকের সাথে ম্যাচ করানোর জন্য:
*   **Gemini AI স্কোরিং:** কেবল দূরত্বের ওপর নির্ভর না করে Gemini AI ব্যবহার করে মেকানিকের গাড়ি তোলার ক্ষমতা (Tow truck type), স্কিল, ট্রাফিক জ্যাম ও অতীতের রেসপন্স টাইম অ্যানালাইসিস করে সেরা মেকানিক নির্বাচন করা হয়েছে।
*   **Redux Toolkit রিয়েল-টাইম স্টেট:** ফ্রন্টএন্ডে Redux Toolkit-এর `createEntityAdapter` ব্যবহার করে ৫০০+ অ্যাক্টিভ প্রোভাইডারের ডাটা নরমালাইজড করে রাখা হয়েছিল।
*   **অটো-ম্যাচিং ও স্পিড বৃদ্ধি:** WebSocket থেকে লাইভ লোকেশন আসার সাথে সাথে Redux স্টেট আপডেট হতো কিন্তু পুরো ইউআই রি-রেন্ডার হতো না। Gemini AI-এর অটোমেটেড সাজেশন এবং Redux-এর ফাস্ট রি-রেন্ডারিংয়ের ফলে ডিসপ্যাচ প্রসেসের গতি ৩৫% বৃদ্ধি পায়।

---

### **Q5: How did you architect the Express backend with Redis and Bull queues to process 10,000+ daily background tasks? / এক্সপ্রেস (Express) ব্যাকএন্ডে Redis এবং Bull কিউ (Queue) ব্যবহার করে প্রতিদিন ১০,০০০+ ব্যাকগ্রাউন্ড টাস্ক প্রসেস করার আর্কিটেকচারটি কীভাবে সাজিয়েছিলেন?**

**Answer (English):**
Processing heavy asynchronous tasks (push notifications, SMS alerts, PDF invoices, telemetry data logging) on the main Node.js thread can cause API responsiveness issues.
*   **Bull Queue Architecture:** Offloaded all non-critical background jobs to **Bull Queue** backed by **Redis**. When an endpoint is hit (e.g., emergency service request created), the Express API producer immediately pushes a job payload to the Redis queue and returns an instant HTTP 202 response.
*   **Worker Concurrency & Isolation:** Configured separate worker consumer processes/threads to process jobs asynchronously with defined concurrency levels (`queue.process(concurrency, handler)`).
*   **Fault Tolerance:** Implemented automatic exponential backoff retries for failed jobs, along with Dead Letter Queues (DLQ) to log and inspect unresolvable tasks.
*   **Rate Limiting & Memory Management:** Utilized Redis TTLs and memory optimization policies to ensure that the worker pool easily scaled to handle 10,000+ daily jobs without affecting the main API latency.

**অনুবাদ (Bangla Translation):**
Node.js-এর মেইন থ্রেড ফাঁকা রাখতে নোটিফিকেশন, এসএমএস ও ফাইল প্রসেসিং ব্যাকগ্রাউন্ডে পাঠানোর জন্য আর্কিটেকচারটি সাজানো হয়েছিল:
*   **Bull + Redis Queue:** এক্সপ্রেস এপিআইতে রিকোয়েস্ট আসামাত্রই রেসপন্স দিয়ে দেওয়া হতো এবং কাজের বিবরণ **Redis-বেসড Bull Queue**-তে পাঠিয়ে দেওয়া হতো।
*   **ওয়ার্কার কনকারেন্সি:** ব্যাকগ্রাউন্ডে আলাদা কন্সুমার প্রসেস রাখা হয়েছিল যা নির্ধারিত কনকারেন্সি মেনে কিউ থেকে কাজ নিয়ে প্রসেস করত।
*   **ফেল্ট টলারেন্স:** কোনো কাজ ব্যর্থ হলে স্বয়ংক্রিয়ভাবে Exponential Backoff নিয়মে পুনরায় রি-ট্রাই করা হতো এবং বার বার ব্যর্থ কাজগুলো Dead Letter Queue-তে জমা হতো।
*   **ফলাফল:** প্রতিদিন ১০,০০০+ ব্যাকগ্রাউন্ড কাজ মসৃণভাবে প্রসেস হতো এবং মূল এপিআই সার্ভারে কোনো ল্যাগ আসত না।

---

### **Q6: In the fleet management platform, how did you handle high-frequency vehicle telemetry data in Next.js without causing UI performance bottlenecks? / ফ্লীট ম্যানেজমেন্ট প্ল্যাটফর্মে অনবরত আসা গাড়ির টেলিমেট্রি (Vehicle Telemetry) ডেটা Next.js ইউআই-তে কোনো ল্যাগ ছাড়াই কীভাবে প্রদর্শন করেছেন?**

**Answer (English):**
Vehicle telemetry (GPS speed, fuel level, engine diagnostics) sends data at high frequencies, which can easily trigger excessive React re-renders and freeze the UI.
*   **Throttling & Batching:** Instead of updating React state on every raw WebSocket message, I implemented a client-side throttling/batching buffer (updating UI state every 500ms–1s using `requestAnimationFrame` or a custom custom hook).
*   **Selective Re-rendering:** Used **Zustand** or **shallow Redux selectors** so that components subscribed only to specific properties of a single vehicle rather than the entire fleet array.
*   **Canvas / WebGL Rendering for Maps:** Rendered moving vehicle markers on Google Maps / Leaflet using custom Canvas layers instead of traditional DOM elements.
*   **Memoization:** Used `React.memo` and `useCallback` extensively to isolate map component updates from telemetry text dashboards.

**অনুবাদ (Bangla Translation):**
গাড়ির লাইভ স্পিড, ফুয়েল ও জিপিএস ডাটা অনবরত ফায়ার হওয়ায় ইউআই-তে পারফরম্যান্স ধরে রাখতে নিচের প্রযুক্তি ব্যবহার করেছি:
*   **থ্রটলিং ও ব্যাচিং:** প্রতি সকেটের মেসেজে সাথে সাথে রিয়্যাক্ট স্টেট আপডেট না করে `requestAnimationFrame` বা থ্রটলিং বাফারের মাধ্যমে ৫০০ms পরপর ব্যাচ আকারে স্টেট আপডেট করা হয়েছে।
*   **সিলেক্টিভ রি-রেন্ডারিং:** **Zustand** বা Shallow Selectors ব্যবহার করা হয়েছিল যাতে নির্দিষ্ট গাড়ির তথ্য পরিবর্তন হলে কেবল ওই গাড়ির কার্ড বা মার্কার রি-রেন্ডার হয়, পুরো তালিকা নয়।
*   **ক্যানভাস রেন্ডারিং:** ম্যাপে ৫০০+ গাড়ির লাইভ পজিশন মার্কার সাধারণ DOM এর বদলে ক্যানভাস বা লাইটওয়েট মার্কার দিয়ে ড্র করা হয়েছিল।

---

### **Q7: What PWA features and caching strategies did you implement for the compliance and safety dashboards in the fleet management platform? / ফ্লীট ম্যানেজমেন্ট প্ল্যাটফর্মের ড্যাশবোর্ডে কী কী PWA ফিচার এবং ক্যাশিং স্ট্র্যাটেজি প্রয়োগ করেছিলেন?**

**Answer (English):**
To ensure fleet managers and drivers could view compliance reports and vehicle status even during flaky cellular connectivity:
*   **Service Worker & Workbox:** Integrated a Service Worker using Workbox in Next.js.
*   **Stale-While-Revalidate Strategy:** Applied for dashboard UI assets and semi-static API routes (e.g., driver rules, compliance documents), serving cached content instantly while fetching fresh data in the background.
*   **Network-First Strategy:** Applied for critical telemetry and safety alerts, falling back to cached reports if offline.
*   **IndexedDB (via Dexie.js/RxDB):** Used client-side IndexedDB to store offline telemetry logs and inspection checklists, syncing them automatically to the MongoDB backend when connectivity was restored via background sync.
*   **Web App Manifest:** Configured standalone app display, custom icons, and offline fallback pages.

**অনুবাদ (Bangla Translation):**
মোবাইল নেটওয়ার্ক দুর্বল থাকলেও ড্রাইভার বা ম্যানেজাররা যেন ড্যাশবোর্ড ব্যবহার করতে পারেন:
*   **Service Worker (Workbox):** Next.js-এ Service Worker কনফিগার করা হয়েছিল।
*   **Stale-While-Revalidate:** ইউআই এসেট এবং স্ট্যাটিক ডকুমেন্টের জন্য এই স্ট্র্যাটেজি দেওয়া হয়, যা ক্যাশ থেকে সাথে সাথে কন্টেন্ট দেখায় এবং ব্যাকগ্রাউন্ডে নতুন ফাইল আপডেট করে।
*   **Network-First:** গুরুত্বপূর্ণ সেফটি এলার্ট ও রিপোর্টগুলোর জন্য প্রথমে নেটওয়ার্কে রিকোয়েস্ট পাঠায়, ফেল করলে ক্যাশ থেকে দেখায়।
*   **IndexedDB স্টোরেজ:** অফলাইনে ভরা ড্রাইভারদের ইন্সপেকশন ফর্ম IndexedDB-তে সেভ থাকত এবং ইন্টারনেট আসামাত্রই ব্যাকগ্রাউন্ডে সার্ভারে সিঙ্ক হতো।

---

### **Q8: How did you integrate Gemini AI into a real-time React & Socket.IO application, and how did you manage streaming responses? / একটি রিয়েল-টাইম React এবং Socket.IO অ্যাপ্লিকেশনে Gemini AI কীভাবে যুক্ত করেছেন এবং এর স্ট্রিমিং (Streaming) রেসপন্স কীভাবে হ্যান্ডেল করেছেন?**

**Answer (English):**
Integrating AI into real-time interactive applications requires handling token streaming without blocking the UI:
*   **Streaming API Integration:** Used the Google Gen AI SDK on the Node.js backend to stream tokens from Gemini AI (`generateContentStream`).
*   **Socket.IO Pipe:** Emitted chunked tokens over Socket.IO to the client (`ai-stream-chunk`) as they arrived from Gemini, providing a real-time typing effect.
*   **React State Management:** On the React frontend, pushed incoming chunks to a local stream buffer rather than full state rewrites, maintaining a smooth 60 FPS typing animation using Framer Motion or lightweight string buffers.
*   **Context Truncation & Fallbacks:** Maintained a rolling conversation context history window in Redis to prevent exceeding model token limits, implementing fallback error handlers if the AI stream timed out.

**অনুবাদ (Bangla Translation):**
রিয়েল-টাইম ইউআই-তে AI-এর স্ট্রিমিং আউটপুট দেখানোর কৌশল:
*   **স্ট্রিমিং এপিআই:** Node.js ব্যাকএন্ডে Gemini AI-এর `generateContentStream` ব্যবহার করে টোকেন বাই টোকেন ডাটা রিসিভ করা হতো।
*   **Socket.IO পাইপাইন:** সার্ভার টোকেন পাওয়ার সাথে সাথে Socket.IO ইভেন্টের মাধ্যমে (`ai-stream-chunk`) ক্লায়েন্টে পাঠাত।
*   **React স্মুথ অ্যানিমেশন:** ফ্রন্টএন্ডে আসা টোকেনগুলোকে বাফারে নিয়ে রিয়াল-টাইম টাইপিং ইফেক্ট তৈরি করা হতো, যাতে স্ক্রিনে কোনো ল্যাগ ছাড়া লাইভ চ্যাট বটের উত্তর ভেসে উঠত।
*   **টোকেন লিমিট ম্যানেজমেন্ট:** Redis-এ চ্যাট হিস্ট্রি ট্রাঙ্কেট করে টোকেন লিমিট বজায় রাখা হতো।

---

### **Q9: How did you secure your Express backend, geospatial API endpoints, and real-time Socket.IO connections? / আপনার এক্সপ্রেস ব্যাকএন্ড, জিয়োস্পেশিয়াল এপিআই এবং Socket.IO কানেকশনগুলো কীভাবে সুরক্ষিত করেছিলেন?**

**Answer (English):**
Security in a high-concurrency real-time application spans multiple layers:
*   **Authentication & Authorization:** Implemented JWT-based authentication. For Socket.IO, passed the JWT token in the handshake query/auth object, validating it via a Socket.IO middleware before allowing connection to room namespaces.
*   **Schema Validation (Zod):** Validated all incoming REST payloads and Socket.IO event data using **Zod schemas**, throwing explicit validation errors before hitting database or controller layers.
*   **Rate Limiting & DDoS Protection:** Applied `express-rate-limit` and `rate-limiter-flexible` with Redis to prevent brute-force attacks on login, payment, and geospatial search APIs.
*   **Security Headers & Sanitization:** Enforced Helmet.js HTTP security headers, CORS origin restrictions, and sanitized inputs against MongoDB Operator Injection (`express-mongo-sanitize`) and XSS attacks.

**অনুবাদ (Bangla Translation):**
অ্যাপ্লিকেশনের সার্বিক নিরাপত্তা নিশ্চিত করার কৌশল:
*   **Socket.IO ও এপিআই সিকিউরিটি:** JWT দিয়ে অথেন্টিকেশন করা হয়েছিল। Socket.IO-তে Handshake মিডলওয়্যার বসিয়ে টোকেন ভ্যালিডেট করার পরেই কেবল রুমে যুক্ত হতে দেওয়া হতো।
*   **Zod স্কিমা ভ্যালিডেশন:** রিকোয়েস্টের সমস্ত ডেটা **Zod Schema** দিয়ে ফিল্টার করা হতো, যাতে ভুল ডাটা বা ক্ষতিকারক কোড ডাটাবেজে না যায়।
*   **Rate Limiting:** Redis-বেসড `rate-limiter-flexible` দিয়ে এপিআই-তে অতিরিক্ত রিকোয়েস্ট বা স্প্যামিং আটকানো হয়েছিল।
*   **HTTP হেডার ও স্যানিটাইজেশন:** Helmet.js, CORS পলিসি এবং MongoDB ইনজেকশন এড়াতে `express-mongo-sanitize` ব্যবহার করা হয়েছিল।

---

### **Q10: How did you utilize Framer Motion and Tailwind CSS in Next.js to achieve 60 FPS animations and prevent layout thrashing? / Next.js-এ Framer Motion এবং Tailwind CSS ব্যবহার করে ৬০ FPS অ্যানিমেশন এবং লেআউট থ্র্যাশিং (Layout Thrashing) প্রতিরোধ করার উপায় কী ছিল?**

**Answer (English):**
Delivering smooth 60 FPS animations in complex dashboards requires utilizing GPU hardware acceleration:
*   **GPU-Accelerated Properties:** Built animations relying strictly on CSS `transform` (scale, translate, rotate) and `opacity` using Framer Motion and Tailwind CSS, which are handled directly by the GPU composite thread without triggering expensive browser reflows or repaints.
*   **`layout` Prop and `AnimatePresence`:** Used Framer Motion’s `layout` prop for automatic smooth FLIP (First, Last, Invert, Play) animations when list items or vehicle cards reordered, combined with `AnimatePresence` for exit animations.
*   **Code Splitting Animations:** Dynamic import of heavy animation components using `next/dynamic` so the main bundle size remained minimal.
*   **Will-Change & GPU Hints:** Used Tailwind’s `will-change-transform` selectively on high-frequency moving UI widgets to hint the browser compositor.

**অনুবাদ (Bangla Translation):**
ড্যাশবোর্ডে স্মুথ ৬০ FPS অ্যানিমেশন নিশ্চিত করার উপায়:
*   **GPU এক্সিলারেটেড সিএসএস:** লেআউট রি-ফ্লো বা রি-পেইন্ট এড়াতে Framer Motion এবং Tailwind দিয়ে কেবল সিএসএস `transform` (translate, scale) এবং `opacity` অ্যানিমেট করা হয়েছিল, যা ব্রাউজারের GPU দিয়ে চলে।
*   **FLIP অ্যানিমেশন:** তালিকা বা গাড়ির কার্ডের অবস্থান পরিবর্তন হলে Framer Motion-এর `layout` এবং `AnimatePresence` ব্যবহার করে স্মুথ অ্যানিমেশন তৈরি করা হয়েছে।
*   **ডাইনামিক কোড স্প্লিটিং:** নেক্সট জেএস-এ `next/dynamic` ব্যবহার করে অ্যানিমেশন লাইব্রেরিগুলোকে প্রয়োজনে লোড করা হয়েছে যাতে মেইন ফাইল সাইজ হালকা থাকে।

---

### **Q11: How did you manage Prompt Engineering, System Instructions, and a Rolling Context Window in Redis for the Ferry Platform's Conversational AI? / ফেরি প্ল্যাটফর্মের AI চ্যাটবটের জন্য প্রম্পট ইঞ্জিনিয়ারিং, সিস্টেম ইন্সট্রাকশন এবং Redis-এ Rolling Context Window কীভাবে ডিজাইন ও স্পেস অপ্টিমাইজ করেছেন?**

**Answer (English):**
Building a domain-specific AI support assistant for ferry bookings (GoNautika) requires controlling the LLM's context window and behavior:
*   **System Instructions:** Passed clear, strict system prompts to Gemini AI defining its role (e.g., "You are GoNautika Support Assistant. Help users with ferry schedules, baggage limits, and ticket status. Do NOT make up booking IDs or prices.").
*   **Rolling Context Window in Redis:** Stored recent conversation turns in Redis using a List data structure keyed by `user_id` or `session_id`. Truncated older messages using `LTRIM` to retain only the last N messages (e.g., last 10-12 conversation turns) to avoid exceeding Gemini AI's context token limits and keep API latency low.
*   **Dynamic Data Injection:** Before calling the model, dynamically injected relevant user booking context (e.g., current active ticket status, ferry departure time) into the prompt string so Gemini answered with exact data without hallucinating.

**অনুবাদ (Bangla Translation):**
ফেরি বুকিং প্ল্যাটফর্মে (GoNautika) কাস্টমার সাপোর্ট চ্যাটবট বানানোর সময় LLM-এর টেক্সট উইন্ডো ও আচরণ নিয়ন্ত্রণের জন্য:
*   **সিস্টেম ইন্সট্রাকশন:** Gemini AI-কে স্পষ্ট সিস্টেম প্রম্পট দেওয়া হয়েছিল (যেমন- "তুমি GoNautika-র সহায়তা সহকারী। ফেরির সময়সূচী, টিকিটের অবস্থা ও ব্যাগেজের নিয়ম বুঝিয়ে দাও। বান বানিয়ে দাম বা ভুয়া টিকিট নম্বর দেবে না।")।
*   **Redis-এ Rolling Context Window:** ইউজারের সাথে সাম্প্রতিক কথাগুলো Redis-এর List-এ সেভ রাখা হতো। টোকেন লিমিট যেন পার না হয় এবং এপিআই দ্রুত রেসপন্স করে, সে জন্য `LTRIM` দিয়ে কেবল শেষ ১০-১২টি চ্যাট হিস্ট্রি রাখা হতো।
*   **ডাইনামিক ডেটা ইনজেকশন:** মডেল কল করার ঠিক আগে ইউজারের বর্তমান টিকিটের স্ট্যাটাস বা সময় প্রম্পটের সাথে যুক্ত করে দেওয়া হতো, যাতে AI কোনো মনগড়া বা ভুল তথ্য না দেয়।

---

### **Q12: How did you enforce Structured JSON Outputs and Function Calling (Tools) with Gemini AI for automated roadside dispatch matching? / ইমার্জেন্সি রোডসাইড ডিসপ্যাচ ম্যাচিংয়ের জন্য Gemini AI থেকে নিখুঁত Structured JSON এবং Function Calling কীভাবে নিশ্চিত করেছিলেন?**

**Answer (English):**
For AI-driven decision making (like automated dispatch matching in ResQ), natural language text responses are unsuitable because code needs strict, deterministic structure.
*   **Enforcing JSON Schema:** Utilized Gemini AI's native `responseSchema` and set `responseMimeType: "application/json"` in `generationConfig`. Defined a strict OpenAPI-compliant JSON schema requiring fields like `{ recommendedMechanicId: string, matchConfidenceScore: number, dispatchReason: string }`.
*   **Function Calling (Tools):** Defined custom tool declarations (`tools: [{ functionDeclarations: [...] }]`) allowing Gemini to invoke backend functions (e.g., `getNearbyMechanics(latitude, longitude)` or `checkTowTruckAvailability(type)`).
*   **Validation Layer:** On the Express backend, validated the AI's returned JSON payload using a **Zod schema** before executing dispatch logic, gracefully handling fallback matching if validation failed.

**অনুবাদ (Bangla Translation):**
ইমার্জেন্সি ডিসপ্যাচিংয়ের মতো জায়গায় সাধারণ টেক্সট উত্তরের বদলে কোডে ব্যবহারের জন্য নিখুঁত স্ট্রাকচার্ড ডাটা দরকার:
*   **JSON Schema প্রয়োগ:** Gemini AI-এর `generationConfig`-এ `responseMimeType: "application/json"` এবং `responseSchema` সেট করা হয়েছিল। এতে AI উত্তর হিসেবে কেবল নির্ধারিত ফরম্যাটের JSON পাঠাতে বাধ্য হতো (`{ recommendedMechanicId, matchConfidenceScore, dispatchReason }`)।
*   **Function Calling:** Gemini-র কাছে কাস্টম টুলস উন্মুক্ত করা হয়েছিল (যেমন- `getNearbyMechanics()`), যা ব্যাকএন্ডের ফাংশন কল করে ডাটা আনতে পারে।
*   **Zod ভ্যালিডেশন:** ব্যাকএন্ডে AI-এর পাঠানো JSON পাওয়ার পর **Zod Schema** দিয়ে পুনরায় চেক করা হতো, যাতে কোনো ভুল ডাটা সিস্টেমে না ঢোকে।

---

### **Q13: How did you handle Gemini AI rate limits (429 errors), network timeouts, retries, and model fallbacks in production? / প্রোডাকশনে Gemini AI-এর রেট লিমিট (429 Errors), নেটওয়ার্ক টাইমআউট এবং মডেল ফলব্যাক কীভাবে হ্যান্ডেল করেছিলেন?**

**Answer (English):**
Relying on external AI APIs in production requires robust fault tolerance to maintain application availability:
*   **Rate-Limit Retries with Exponential Backoff:** Wrapped all Gemini AI SDK calls with retry logic (using `async-retry` or `p-retry`) configured with exponential backoff and jitter to gracefully handle HTTP 429 (Rate Limit Exceeded) and 503 (Server Unavailable) errors.
*   **Model Fallback Hierarchy:** Implemented a fallback mechanism. If `gemini-1.5-pro` failed or timed out (e.g., >3000ms threshold), the request automatically downgraded to `gemini-1.5-flash` for faster response times.
*   **Rule-Based Fallback Engine:** If all AI models failed or experienced an outage, the system automatically degraded gracefully to a traditional rule-based matching algorithm (sorting Mechanics purely by MongoDB `$near` distance and rating), ensuring 100% platform uptime.
*   **Circuit Breaker Pattern:** Used a circuit breaker (e.g., `opossum` library) to stop spamming the AI endpoint if failure rates exceeded 50% in a 1-minute window.

**অনুবাদ (Bangla Translation):**
প্রোডাকশনে থার্ড-পার্টি AI এপিআই-এর ওপর নির্ভর করার সময় সিস্টেম ডাউন না হওয়ার কৌশল:
*   **Exponential Backoff রি-ট্রাই:** AI এপিআইতে 429 (Rate Limit) বা 503 এরর আসলে `p-retry` দিয়ে কিছু সময় পর পর স্বয়ংক্রিয়ভাবে রি-ট্রাই করা হতো।
*   **মডেল ফলব্যাক (Fallback):** যদি ভারী মডেল `gemini-1.5-pro` ৩ সেকেন্ডের মধ্যে রেসপন্স না করত, কোড স্বয়ংক্রিয়ভাবে দ্রুতগতির `gemini-1.5-flash` মডেলে সুইচ করত।
*   **রুল-বেসড ব্যাকআপ মেকানিজম:** সব AI মডেল ডাউন হয়ে গেলেও সিস্টেম বন্ধ না হয়ে সনাতন নিয়মে (MongoDB-র ডিস্টেন্স ও রেটিং দিয়ে) মেকানিক ম্যাচ করিয়ে দিত, ফলে প্রজেক্টের ১০টি ফিচারই ১০০% চালু থাকত।
*   **Circuit Breaker:** ১ মিনিটে ৫০% রিকোয়েস্ট ফেল করলে সার্কিট ব্রেকার দিয়ে কিছুক্ষণের জন্য AI কল দেওয়া বন্ধ রাখা হতো।

---

### **Q14: How would you architect a Retrieval-Augmented Generation (RAG) system with Vector Search for AI customer support or fleet compliance? / AI কাস্টমার সাপোর্ট বা কমপ্লায়েন্স ড্যাশবোর্ডের জন্য RAG (Retrieval-Augmented Generation) এবং Vector Search আর্কিটেকচার কীভাবে তৈরি করবেন?**

**Answer (English):**
To provide accurate, grounded answers from internal documents (e.g., ferry cancellation rules, fleet safety manuals) without LLM hallucinations:
*   **Document Chunking & Embeddings:** Ingest PDF/markdown docs, split text into smaller chunks (e.g., 500 tokens with 50-token overlap), and generate vector embeddings using Gemini's Text Embedding API (`text-embedding-004`).
*   **Vector Database Storage:** Store the generated vector embeddings and raw text chunks in **MongoDB Vector Search** (using `knnVector` index) or a dedicated vector DB (Pinecone/Qdrant).
*   **Retrieval Pipeline:** When a user asks a query, generate an embedding of the user's question, execute a vector similarity search (Cosine / Euclidean distance) to retrieve the top 3-5 most relevant context chunks.
*   **Augmented Generation:** Construct a prompt injecting the retrieved context: `"Answer the question strictly using the provided context: {retrieved_chunks}. Question: {user_query}"`, ensuring accurate, hallucination-free answers.

**অনুবাদ (Bangla Translation):**
কোম্পানির নিজস্ব নিয়মকানুনের নথি (যেমন- টিকিট বাতিলের নিয়ম বা সেফটি ম্যানুয়াল) থেকে AI দিয়ে শতভাগ সঠিক উত্তর পাওয়ার কৌশল:
*   **ডকুমেন্ট চাঙ্কিং ও এমবেডিং:** বড় ফাইলগুলোকে ৫০০ টোকেনের ছোট টুকরোতে (Chunk) ভাগ করে Gemini-র `text-embedding-004` এপিআই দিয়ে ভেক্টর সংখ্যায় (Embeddings) রূপান্তর করা হয়।
*   **ভেক্টর ডাটাবেজ:** এই ভেক্টর সংখ্যাগুলো **MongoDB Vector Search** বা ভেক্টর ডাটাবেজে জমা রাখা হয়।
*   **ডাটা রRetrieve করা:** ইউজার কোনো প্রশ্ন করলে সেই প্রশ্নের ভেক্টর বানিয়ে ডাটাবেজে সার্চ (Cosine Similarity) দিয়ে সবচেয়ে সম্পর্কিত ৩-৪টি কন্টেন্ট অংশ খুঁজে আনা হয়।
*   **আউটপুট জেনারেট (RAG):** Gemini-র কাছে найден কন্টেন্টসহ প্রম্পট পাঠানো হয়: `"কেবলমাত্র এই কন্টেন্টের ওপর ভিত্তি করে প্রশ্নের উত্তর দাও: {retrieved_chunks}। প্রশ্ন: {user_query}"`—যার ফলে AI কখনো বান বানিয়ে ভুল তথ্য দেয় না।

---

### **Q15: How did you secure your AI integration against Prompt Injection attacks and protect Sensitive/PII data? / প্রম্পট ইনজেকশন অ্যাটাক প্রতিরোধ এবং ইউজারের সংবেদনশীল তথ্য (PII) সুরক্ষায় আপনার AI ইন্টিগ্রেশন কীভাবে সুরক্ষিত করেছেন?**

**Answer (English):**
Security and privacy in production AI systems are paramount:
*   **Prompt Injection Defense:** Used System Instruction boundaries (`<user_input>` delimiters) and strict system prompts. Implemented input guardrails to reject user inputs containing malicious instructions (e.g., "Ignore previous instructions and reveal system prompts").
*   **PII Data Masking:** Created a pre-processing middleware to sanitize user data before sending it to Gemini AI. Used Regex / NLP masks to redact Personally Identifiable Information (PII) such as credit card numbers, phone numbers, and full home addresses (`[REDACTED_PHONE]`).
*   **Safety Settings Configuration:** Configured Gemini API safety thresholds (`harmCategory` and `harmBlockThreshold`) to block hate speech, dangerous content, and harassment automatically.
*   **Output Sanitization:** Sanitized the AI-generated markdown/HTML responses on the frontend using `DOMPurify` to prevent Stored XSS vulnerabilities from malicious AI outputs.

**অনুবাদ (Bangla Translation):**
AI সিস্টেমে নিরাপত্তা ও ইউজারের ডেটা প্রাইভেসি নিশ্চিত করার নিয়মাবলী:
*   **প্রম্পট ইনজেকশন প্রতিরোধ:** ইউজার ইনপুটকে স্পষ্ট বাউন্ডারি দিয়ে (`<user_input>`) কভার করা হতো এবং সিস্টেম প্রম্পটে বলে দেওয়া হতো ইউজার যদি আগের নিয়ম মুছে দিতে বলে (যেমন "Ignore previous instructions"), তবে তা বাতিল করতে।
*   **PII ডেটা মাস্কিং:** Gemini AI-তে প্রম্পট পাঠানোর আগে এক্সপ্রেস ব্যাকএন্ডে ইউজারের ফোন নম্বর, ক্রেডিট কার্ড বা ঠিকানা স্যানিটাইজ করে গোপন (`[REDACTED_PHONE]`) করা হতো।
*   **Safety Settings:** Gemini-র `harmBlockThreshold` কনফিগার করে ক্ষতিকারক বা আপত্তিকর কথা বন্ধ করা হতো।
*   **আউটপুট স্যানিটাইজেশন:** AI-এর পাঠানো রেসপন্স রিয়্যাক্ট ইউআই-তে দেখানোর আগে `DOMPurify` দিয়ে পরিষ্কার করা হতো যাতে XSS হ্যাকিং না হতে পারে।

---

### **Q16: What types of AI features have you built across your projects? / আপনার প্রজেক্টগুলোতে আপনি কী কী ধরণের AI ফিচার তৈরি করেছেন?**

**Answer (English):**
Across my full-stack projects, I have architected and integrated three major production-grade AI features:
1.  **Conversational Support Assistant (GoNautika - Ferry Platform):** A real-time passenger support chatbot that resolves queries about ferry schedules, ticket statuses, cancellation policies, and baggage rules via streaming WebSockets.
2.  **AI-Driven Dispatching & Match Scoring Engine (ResQ - Emergency Roadside Assistance):** An automated matching engine that evaluates stranded vehicle telemetry, service provider skills, tow truck types, live traffic, and historical response times to calculate match confidence scores—improving dispatch speed by 35%.
3.  **AI Vehicle Diagnostics & Driver Safety Analytics (Fleet Management Platform):** An intelligent analytics pipeline that processes real-time vehicle telemetry feeds to detect risky driving behaviors (sudden braking, speeding), generate safety compliance scores, and predict maintenance requirements.

**অনুবাদ (Bangla Translation):**
আমার প্রজেক্টগুলোতে আমি মূলত ৩টি প্রধান প্রোডাকশন-গ্রেড AI ফিচার ডিজাইন ও ইমপ্লিমেন্ট করেছি:
1.  **কনভারসেশনাল সাপোর্ট অ্যাসিস্ট্যান্ট (GoNautika):** ফেরি যাত্রীদের জন্য একটি রিয়েল-টাইম AI চ্যাটবট যা টিকিটের স্ট্যাটাস, সময়সূচী, বাতিলকরণ পলিসি এবং ব্যাগেজ সংক্রান্ত প্রশ্নের উত্তর রিয়েল-টাইমে স্ট্রিম করে দেয়।
2.  **AI-চালিত ডিসপ্যাচ ম্যাচিং ইঞ্জিনের স্কোরিং (ResQ Roadside Assistance):** দুর্ঘটনাকবলিত গাড়ি ও মেকানিকের দূরত্ব, মেকানিকের স্কিল, টো-ট্রাকের ধরণ এবং ট্রাফিক জ্যাম বিশ্লেষণ করে উপযুক্ত মেকানিক নির্বাচন করা হয়েছে।
3.  **গাড়ির টেলিমেট্রি ডায়াগনস্টিকস ও সেফটি অ্যানালিটিক্স (Fleet Platform):** গাড়ির লাইভ সেন্সর ও জিপিএস ডাটা বিশ্লেষণ করে ঝুঁকিপূর্ণ ড্রাইভিং প্যাটার্ন শনাক্ত করা, সেফটি স্কোর দেওয়া এবং মেইনটেন্যান্স প্রেডিক্ট করা।

---

### **Q17: How did you technically integrate these AI features into your MERN / Full-Stack tech stack? / আপনার MERN / Full-Stack প্রজেক্ট আর্কিটেকচারে আপনি কীভাবে এই AI ফিচারগুলো যুক্ত (Integrate) করেছিলেন?**

**Answer (English):**
I integrated AI features seamlessly into the MERN stack using a modular, decoupled architecture:
1.  **Backend Integration Layer (Node.js/Express + Google Gen AI SDK):** Initialized the official Google Gen AI SDK on the Express backend (`@google/genai`). Kept API keys strictly secured on the server using environment variables (`process.env.GEMINI_API_KEY`) to prevent client-side exposure.
2.  **Real-Time Token Streaming (Socket.IO):** Piped `generateContentStream()` token chunks over Socket.IO directly to the React frontend (`ai-stream-chunk` events), delivering a smooth 60 FPS live typing animation without blocking the main UI thread.
3.  **Structured JSON Enforcement & Function Calling:** Configured `generationConfig` with `responseSchema` for API endpoints requiring deterministic JSON (e.g., dispatch matching scores), enforcing backend Zod schema validation before saving results to MongoDB.
4.  **State Management & Memory (Redis + Redux/Zustand):** Maintained a rolling conversation context history window in Redis using `LTRIM` to optimize context window limits, while updating normalized frontend state in Redux Toolkit or Zustand.
5.  **Resilience & Fault Tolerance:** Wrapped all AI service calls with exponential backoff retries (`p-retry`), fallback model hierarchies (`gemini-1.5-pro` -> `gemini-1.5-flash`), and rule-based fallback engines to guarantee 100% platform availability.

**অনুবাদ (Bangla Translation):**
MERN স্ট্যাক আর্কিটেকচারে AI ফিচারগুলো যুক্ত করার সম্পূর্ণ টেকনিক্যাল পদ্ধতি:
1.  **ব্যাকএন্ড এপিআই লেয়ার (Node.js/Express + Google Gen AI SDK):** এক্সপ্রেস ব্যাকএন্ডে অফিসিয়াল `@google/genai` SDK ইনস্টল করা হয়। API Key কে সম্পূর্ণ নিরাপদ রাখতে এটি কেবল সার্ভার পরিবেশের সিক্রেটে রাখা হতো (ক্লায়েন্টে কখনো পাঠানো হতো না)।
2.  **রিয়েল-টাইম টোকেন স্ট্রিমিং (Socket.IO):** Gemini-র `generateContentStream()` থেকে ছোট ছোট টোকেন পাওয়ার সাথে সাথে Socket.IO ইভেন্টের মাধ্যমে ক্লায়েন্টে পাঠিয়ে ৬০ FPS লাইভ টাইপিং অ্যানিমেশন তৈরি করা হতো।
3.  **Structured JSON ও Function Calling:** লজিক্যাল ফিল্ডের জন্য Gemini-র `responseSchema` এবং `responseMimeType: "application/json"` অন করা হতো এবং ব্যাকএন্ডে **Zod Schema** দিয়ে ডেটা ভ্যালিডেশন করা হতো।
4.  **স্টেট ও মেমোরি ম্যানেজমেন্ট (Redis + Redux/Zustand):** চ্যাট হিস্ট্রি মেমোরি নিয়ন্ত্রণে রাখতে Redis-এ `LTRIM` দিয়ে নির্দিষ্ট সংখ্যক কথা সেভ রাখা হতো এবং ফ্রন্টএন্ডে Redux/Zustand দিয়ে ইউআই আপডেট করা হতো।
5.  **ফেল্ট টলারেন্স ও সিকিউরিটি:** AI ডাউন থাকলে `p-retry` দিয়ে রি-ট্রাই, দ্রুতগতির `flash` মডেলে রূপান্তর এবং পরিশেষে রুল-বেসড অ্যালগরিদমে অটো-ডিগ্রেড করার আর্কিটেকচার ছিল, যার ফলে এপিআই ফেইল করলেও প্রজেক্ট ১০০% চালু থাকত।

---

### **Q18: What type of production projects have you built during your experience at Brainhub, and what are their core technical features? / Brainhub এবং আপনার ক্যারিয়ারে আপনি কী কী ধরণের প্রোডাকশন প্রজেক্ট তৈরি করেছেন এবং সেগুলোর মূল টেকনিক্যাল ফিচারগুলো কী কী?**

**Answer (English):**
Throughout my role as a Mid-Level Full-Stack Engineer, I have architected and delivered 5 major production-grade web and desktop applications across real-time, offline-first, and AI-driven domains:

1.  **GoNautika — AI-Integrated Ferry Booking Platform**
    *   **Core Features:** Real-time seat reservation engine supporting **15,000+ monthly bookings**, live interactive seat locking (via Socket.IO & Redis), Razorpay payment gateway integration with HMAC-SHA256 webhooks, and an automated Gemini AI-powered customer support chatbot.
2.  **ResQ — Emergency Roadside Assistance Platform**
    *   **Core Features:** Real-time dispatcher tracking **500+ active service providers**, MongoDB `2dsphere` geospatial indexing (reducing query latency by 40%), Gemini AI match scoring engine (improving dispatch speed by 35%), and Redis/Bull background job queues processing 10k+ daily tasks.
3.  **Fleet Management Platform**
    *   **Core Features:** Real-time vehicle telemetry analytics (speed, GPS, engine diagnostics) built with Next.js, AI driver safety monitoring dashboards, smooth 60 FPS animations via Tailwind CSS & Framer Motion, and PWA capabilities with Workbox offline caching.
4.  **SleekDraw — E2EE Collaborative Whiteboard**
    *   **Core Features:** Real-time multi-user interactive canvas using Canvas API and WebSockets with **<50ms latency**, secured with End-to-End Encryption (E2EE) for user diagrams.
5.  **EasyACC — Offline-First Billing & GST Accounting Software**
    *   **Core Features:** Electron.js desktop application powered by RxDB and Dexie.js (IndexedDB) enabling **1,200+ offline checkouts** with 100% database sync reliability to MongoDB ACID transactions upon reconnecting.

**অনুবাদ (Bangla Translation):**
আমি আমার ক্যারিয়ারে রিয়েল-টাইম সিস্টেম, অফলাইন-ফার্স্ট এবং AI-চালিত প্ল্যাটফর্ম সহ মোট ৫টি প্রধান প্রোডাকশন অ্যাপ তৈরি করেছি:

1.  **GoNautika — AI-Integrated Ferry Booking Platform**
    *   **প্রধান ফিচারসমূহ:** **মাসিক ১৫,০০০+ বুকিং** হ্যান্ডেল করা রিয়েল-টাইম ফেরি বুকিং ইঞ্জিন, Socket.IO ও Redis দিয়ে লাইভ সিট লকিং, Razorpay পেমেন্ট ও HMAC সিগনেচার ভ্যালিডেশন এবং Gemini AI দিয়ে লাইভ কাস্টমার চ্যাটবট।
2.  **ResQ — Emergency Roadside Assistance Platform**
    *   **প্রধান ফিচারসমূহ:** **৫০০+ অ্যাক্টিভ মেকানিক** ট্র্যাক করা জিয়োস্পেশিয়াল প্ল্যাটফর্ম, MongoDB `2dsphere` ইনডেক্সিং (যা ল্যাটেন্সি ৪০% কমায়), Gemini AI ও Redux দিয়ে ডিসপ্যাচ ম্যাচিং (যা স্পিড ৩৫% বাড়ায়) এবং Redis/Bull Queue দিয়ে প্রতিদিন ১০,০০০+ ব্যাকগ্রাউন্ড টাস্ক প্রসেসিং।
3.  **Fleet Management Platform**
    *   **প্রধান ফিচারসমূহ:** Next.js দিয়ে গাড়ির লাইভ টেলিমেট্রি (জিপিএস, স্পিড) ট্র্যাকিং, AI ড্রাইভার সেফটি ড্যাশবোর্ড, Tailwind CSS ও Framer Motion দিয়ে ৬০ FPS অ্যানিমেশন এবং Workbox দিয়ে PWA অফলাইন সাপোর্ট।
4.  **SleekDraw — E2EE Collaborative Whiteboard**
    *   **প্রধান ফিচারসমূহ:** Canvas API ও WebSockets দিয়ে একাধিক ইউজারের রিয়েল-টাইম ক্যানভাস বোর্ডিং (**<৫০ms ল্যাটেন্সি**) এবং এন্ড-টু-এন্ড এনক্রিপশন (E2EE)।
5.  **EasyACC — Offline-First Billing & GST Accounting Software**
    *   **প্রধান ফিচারসমূহ:** Electron.js, RxDB ও Dexie.js দিয়ে অফলাইন ডেস্কটপ বিলিং অ্যাপ যা **১,২০০+ অফলাইন চেকআউট** নিশ্চিত করে এবং ইন্টারনেট আসামাত্রই MongoDB-র সাথে ১০০% সিঙ্ক হয়।
