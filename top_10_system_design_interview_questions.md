# Top 10 System Design Interview Questions & Solutions

This guide contains the **top 10 most frequently asked System Design interview questions** at product companies (Google, Meta, Amazon, Uber, Netflix, Stripe), featuring high-level architecture breakdowns, database schemas, caching strategies, scaling trade-offs, and complete **Bangla translations** for each question.

---

## 📋 Table of Contents
1. Design a URL Shortening Service (TinyURL / Bitly)
2. Design an Emergency Dispatch & Ride-Sharing System (Uber / ResQ)
3. Design a Real-Time Chat & Messaging Platform (WhatsApp / Slack)
4. Design an E-Commerce Flash Sale & Inventory Reservation System (Amazon / Flipkart)
5. Design a Distributed Rate Limiter (API Gateway Rate Limiter)
6. Design a High-Throughput Notification System (Push, Email, SMS)
7. Design a Video Streaming Platform (Netflix / YouTube)
8. Design a Collaborative Real-Time Canvas / Document Editor (Figma / SleekDraw)
9. Design an API Gateway Architecture for Microservices
10. Design a Web Crawler System (Google Search Crawler)

---

### **Q1: Design a URL Shortening Service like TinyURL or Bitly. / TinyURL বা Bitly-এর মতো URL Shortener সিস্টেম কীভাবে ডিজাইন করবেন?**

**Answer (English):**
* **Requirements:** Convert long URLs into a short 6-7 character alias (e.g., `https://tiny.url/xyz123`), redirect users instantaneously (HTTP 301/302), handle 100M daily links, and enforce analytics tracking.
* **Key Components:**
  1. **Short Key Generation:** Use Base62 Encoding (`[0-9][a-z][A-Z]`). A 7-character Base62 string yields $62^7 \approx 3.5 \text{ Trillion}$ unique combinations.
  2. **Key Generation Service (KGS):** Pre-generate unique random keys in a dedicated Key DB and store unused keys in Redis memory to eliminate runtime collisions.
  3. **Database Schema (NoSQL / MongoDB or DynamoDB):**
     * `urls` collection: `{ shortKey: String (Primary Key), longUrl: String, userId: String, createdAt: Timestamp, expiresAt: Timestamp }`.
  4. **Caching Layer (Redis):** Cache high-frequency short keys (`shortKey -> longUrl`) with `allkeys-lru` eviction policy. 20% of links drive 80% of redirect traffic.
  5. **HTTP Redirect:** Use **HTTP 302 Found** (Temporary Redirect) so every click hits the server for analytics tracking, or **HTTP 301** for permanent browser caching.

**অনুবাদ (Bangla Translation):**
* **ডিজাইন পরিচিতি:** বড় একটি ওয়েবসাইট লিংক ছোট ৭ অক্ষরের লিংকে রূপান্তর করা (যেমন `tiny.url/xyz123`) এবং ক্লিকে মুহূর্তের মধ্যে মূল পেজে নিয়ে যাওয়া।
* **মূল কৌশল:**
  ১. **Base62 এনকোডিং:** 숫자 (0-9), ছোট ও বড় অক্ষর ব্যবহার করে ৭ অক্ষরের ইউনিক স্ট্রিং বানানো, যা সাড়ে ৩ ট্রিলিয়ন লিংক সাপোর্ট করে।
  ২. **KGS সার্ভিস:** আগে থেকেই তৈরি করা ইউনিক কি (Key) Redis র্যামে জমা রাখা যাতে লিংকে চাপ দিলে সরাসরি কি পাওয়া যায়।
  ৩. **ডাটাবেজ ও ক্যাশিং:** NoSQL ডাটাবেজে `shortKey -> longUrl` সেভ রাখা এবং দ্রুতগতির জন্য **Redis** ক্যাশ ব্যবহার করা।
  ৪. **রিডাইরেক্ট:** HTTP 302 রেসপন্স দেওয়া যাতে প্রতিটি ক্লিকের এনালাইটিক্স হিসাব রাখা যায়।

---

### **Q2: Design an Emergency Assistance & Ride-Sharing System like Uber or ResQ. / Uber বা ResQ-এর মতো লাইভ ট্র্যাকিং ও ডিসপ্যাচ সিস্টেম কীভাবে ডিজাইন করবেন?**

**Answer (English):**
* **Requirements:** Track live location of 500k+ active drivers/mechanics every 4 seconds, match nearest available providers within a 10km radius in under 2 seconds, and stream live map movements to users.
* **Key Components:**
  1. **Geospatial Indexing (MongoDB 2dsphere / Redis Geo):** Store provider coordinates as GeoJSON points. Use `Redis GEOADD` and `GEORADIUS` or MongoDB `2dsphere` compound indexes (`{ location: "2dsphere", isAvailable: 1 }`) for $\mathcal{O}(\log N)$ spatial lookups.
  2. **Location Tracking (WebSockets / Socket.IO):** Mobile apps stream GPS telemetry (`{ driverId, lat, lng }`) via WebSockets to a Location Service.
  3. **Decoupled Match Engine (Gemini AI + Bull Queue):** When a user requests help, an Express API pushes a dispatch job to Bull Queue. Worker processes use Gemini AI / Scoring algorithms to evaluate driver distance, vehicle type, and traffic score, assigning the best candidate.
  4. **Distributed Locking (Redis Redlock):** Wrap driver assignment in Redis `SETNX` lock to prevent multiple dispatchers from assigning the exact same mechanic simultaneously.

**অনুবাদ (Bangla Translation):**
* **ডিজাইন পরিচিতি:** প্রতি ৪ সেকেন্ডে প্রোভাইডারের জিপিএস ট্র্যাকিং করা এবং ২ কিলোমিটারের মধ্যে সবচেয়ে কাছে থাকা মেকানিক বা গাড়ি খুঁজে দেওয়া।
* **মূল কৌশল:**
  ১. **জিয়োস্পেশিয়াল ইনডেক্সিং:** MongoDB-র `2dsphere` বা Redis-এর `GEOADD` ব্যবহার করে মুহূর্তের মধ্যে ১০ কিলোমিটার ব্যাসার্ধের কাছের মেকানিক খুঁজে বের করা।
  ২. **লাইভ ট্র্যাকিং:** Socket.IO দিয়ে লাইভ জিপিএস লোকেশন আপডেট পাঠানো।
  ৩. **অটোমেটেড ম্যাচিং:** রিকোয়েস্ট আসামাত্রই **Bull Queue**-তে জব পাঠিয়ে AI বা অ্যালগরিদম দিয়ে সেরা ড্রাইভার নির্বাচন করা।
  ৪. **ডাবল অ্যাসাইনমেন্ট রোধ:** একই ড্রাইভারে যেন ২ জন ইউজার একসাথে যুক্ত না হয় সে জন্য Redis `SETNX` দিয়ে লক বসানো।

---

### **Q3: Design a Real-Time Chat & Messaging Platform like WhatsApp or Slack. / WhatsApp বা Slack-এর মতো রিয়েল-টাইম চ্যাট প্ল্যাটফর্ম কীভাবে ডিজাইন করবেন?**

**Answer (English):**
* **Requirements:** 1-on-1 private messaging, group chats, online/offline presence status, message delivery receipts (Sent, Delivered, Read), and multi-device synchronization.
* **Key Components:**
  1. **Gateway Layer (WebSockets + Socket.IO):** Clients maintain persistent WebSocket connections to Gateway nodes.
  2. **Session & Presence Service (Redis):** Tracks online status (`userId -> { status: "online", socketId, serverNode }`).
  3. **Message Storage (Cassandra / MongoDB / ScyllaDB):** High write throughput database.
     * Schema: `{ messageId, conversationId, senderId, content, timestamp, status: "READ" }`.
  4. **Scaling Across Servers (Redis Pub/Sub Adapter):** If User A is on Server 1 and User B is on Server 2, Server 1 publishes the message to Redis Pub/Sub, and Server 2 delivers it over User B's WebSocket.
  5. **Offline Delivery Queue:** If User B is offline, push message payload to a persistent Push Notification queue (FCM/Apple APNS) and store in unread message database tables.

**অনুবাদ (Bangla Translation):**
* **ডিজাইন পরিচিতি:** দুজন ইউজার বা গ্রুপের মধ্যে রিয়েল-টাইমে মেসেজ ও অনলাইন স্ট্যাটাস লেনদেন করা।
* **মূল কৌশল:**
  ১. **সকেট কানেকশন:** Socket.IO দিয়ে ক্লায়েন্ট ও সার্ভারের মধ্যে স্থায়ী কানেকশন রাখা।
  ২. **অনলাইন স্ট্যাটাস:** Redis-এ ট্র্যাকিং রাখা কে কে অনলাইন আছে।
  ৩. **মেসেজ সেভ:** প্রতি সেকেন্ডে হাজার হাজার মেসেজ সেভ করতে MongoDB বা Cassandra ব্যবহার করা।
  ৪. **মাল্টি-সার্ভার সিঙ্ক:** একাধিক সার্ভার থাকলে **Redis Pub/Sub** দিয়ে মেসেজ পাস করানো।
  ৫. **অফলাইন মেসেজ:** ইউজার অফলাইনে থাকলে Push Notification পাঠানো।

---

### **Q4: Design an E-Commerce Flash Sale & Inventory Reservation System like Amazon. / Amazon-এর মতো ফ্ল্যাশ সেল এবং স্টক ইনভেন্টরি রিজার্ভেশন সিস্টেম কীভাবে ডিজাইন করবেন?**

**Answer (English):**
* **Requirements:** Handle 100,000 requests/sec for limited stock items (e.g., 1,000 iPhones during a flash sale), zero overselling, and automatic stock release if payment fails within 10 minutes.
* **Key Components:**
  1. **Rate Limiting & Traffic Shedding:** Gatekeeper Nginx / Redis rate limiters restrict bot traffic and drop requests exceeding server capacity.
  2. **In-Memory Inventory Cache (Redis Atomic Decrement):** Store available stock in Redis: `product:101:stock = 1000`. Use Redis `DECRBY` (atomic operation). If stock $> 0$, reservation succeeds; if $< 0$, return "Out of Stock" instantly without hitting the primary database.
  3. **Temporary Reservation (Redis TTL Lock):** Place reserved items in a Redis Hash with a 10-minute TTL tied to `user_id`.
  4. **Asynchronous Order Queue (Bull Queue / Kafka):** Successful stock reservations push order payloads to Bull Queue to create orders asynchronously.
  5. **Database ACID Commitment:** Final payment commits Mongoose ACID transactions (`$inc: { stock: -1 }`). If payment fails, Redis expires the TTL lock and returns stock back to the pool (`INCRBY`).

**অনুবাদ (Bangla Translation):**
* **ডিজাইন পরিচিতি:** নির্দিষ্ট ১,০০০টি প্রোডাক্ট কিনতে লাখ লাখ ইউজার একসাথে চাপ দিলে যেন স্টক খালি হওয়ার পর অতিরিক্ত বিক্রি (Overselling) না হয়।
* **মূল কৌশল:**
  ১. **ইন-মেমোরি কাউন্টার:** মেইন ডাটাবেজে চাপ না দিয়ে Redis-এ `DECRBY` দিয়ে ১টি ১টি করে বিয়োগ করা। স্টক ০ হওয়ার সাথে সাথে এক সেকেন্ডে "Out of Stock" দেখানো।
  ২. **১০ মিনিটের রিজার্ভেশন:** ইউজার কার্টে প্রোডাক্ট নিলে ১০ মিনিটের জন্য স্টক লক করা। পেমেন্ট না করলে অটো রিলিজ করে দেওয়া।
  ৩. **কিউ ও ACID ট্রানজ্যাকশন:** ব্যাকগ্রাউন্ড কিউতে অর্ডার প্রসেস করা এবং পেমেন্ট শেষে ডাটাবেজে সেভ করা।

---

### **Q5: Design a Distributed Rate Limiter Service like Stripe API Gateway Rate Limiter. / Stripe-এর মতো ডিস্ট্রিবিউটেড Rate Limiter কীভাবে ডিজাইন করবেন?**

**Answer (English):**
* **Requirements:** Throttle excessive API requests per client/IP (e.g., max 100 requests per minute), support distributed servers, low latency (<2ms overhead), and return HTTP `429 Too Many Requests`.
* **Algorithms:**
  * **Token Bucket Algorithm:** Tokens added at constant rate; each request consumes a token.
  * **Sliding Window Log (Redis Sorted Set ZSET):** Best accuracy. Store timestamps in a Redis ZSET. Remove elements older than window interval (`ZREMRANGEBYSCORE`). Count remaining tokens (`ZCARD`).
* **Implementation:**
```javascript
const currentWindowMs = Date.now();
const windowStart = currentWindowMs - 60000;
await redis.zremrangebyscore(ip, 0, windowStart); // Clean old logs
const requestCount = await redis.zcard(ip);
if (requestCount >= 100) {
  return res.status(429).json({ error: "Too Many Requests" });
}
await redis.zadd(ip, currentWindowMs, currentWindowMs);
```

**অনুবাদ (Bangla Translation):**
* **ডিজাইন পরিচিতি:** একজন ইউজার বা হ্যাকার যেন প্রতি মিনিটে ১০০টির বেশি এপিআই কল করে সার্ভার ডাউন না করতে পারে।
* **মূল কৌশল:**
  ১. **Sliding Window Algorithm:** Redis-এর `Sorted Set (ZSET)` ব্যবহার করে ইউজারের প্রতিটা রিকোয়েস্টের সময় সেভ রাখা।
  ২. ১ মিনিটের পুরোনো সময়ের রেকর্ডগুলো মুছে দিয়ে বর্তমান রিকোয়েস্ট সংখ্যা ১০০ পার হলে **HTTP 429 (Too Many Requests)** এরর দেওয়া।

---

### **Q6: Design a High-Throughput Notification System (Push, Email, SMS). / লাখ লাখ ইমেইল, এসএমএস এবং পুশ নোটিফিকেশন পাঠানোর রিয়েল-টাইম সিস্টেম কীভাবে ডিজাইন করবেন?**

**Answer (English):**
* **Requirements:** Send millions of daily notifications across multi-channels (FCM Push, SendGrid Email, Twilio SMS), support user notification preferences, rate limiting, and priority queues.
* **Key Components:**
  1. **Notification Router API:** Accepts notification payloads from internal microservices.
  2. **User Preferences DB:** Checks user settings (`email_enabled: true, push_enabled: false`).
  3. **Priority Job Queues (Redis + Bull Queue):** Split queues into high-priority (OTP/Password Reset) and low-priority (Marketing emails).
  4. **Third-Party Rate Limit Handlers:** Implement rate limiters per provider to avoid being blocked by Twilio/SendGrid.
  5. **Dead Letter Queue (DLQ):** Log and retry failed dispatches with exponential backoff.

**অনুবাদ (Bangla Translation):**
* **ডিজাইন পরিচিতি:** ইমেইল, এসএমএস ও অ্যাপ নোটিফিকেশন দ্রুত পাঠানোর আর্কিটেকচার।
* **মূল কৌশল:**
  ১. **Priority Queue:** OTP বা পাসওয়ার্ড রিসেট নোটিফিকেশনকে হাই-প্রাইওরিটি কিউতে এবং অফার ইমেইলকে লো-প্রাইওরিটি কিউতে রাখা।
  ২. **Bull Queue:** ব্যাকগ্রাউন্ড প্রসেসিং করে পাঠানো যাতে মূল অ্যাপ স্লো না হয়।
  ৩. **DLQ:** নোটিফিকেশন পাঠাতে ফেইল করলে তা জমা রেখে পুনরায় চেষ্টা করা।

---

### **Q7: Design a Video Streaming Platform like Netflix or YouTube. / Netflix বা YouTube-এর মতো ভিডিও স্ট্রিমিং প্ল্যাটফর্ম কীভাবে ডিজাইন করবেন?**

**Answer (English):**
* **Requirements:** Upload videos, transcode into multiple resolutions (1080p, 720p, 480p, 360p), adaptive bitrate streaming (HLS / DASH), and global low-latency playback.
* **Key Components:**
  1. **Video Ingestion:** Chunked video upload to AWS S3 bucket.
  2. **Transcoding Pipeline:** S3 event triggers a worker queue (FFmpeg / AWS Elemental MediaConvert) to split video into chunks and encode into HLS `.m3u8` playlists at varying resolutions.
  3. **Adaptive Bitrate Streaming (HLS):** Client video player monitors network speed and dynamically switches resolution chunks (e.g., drops to 480p on 3G, bumps to 1080p on WiFi).
  4. **CDN Edge Caching:** Distribute `.ts` video chunks across global CDN edge locations (CloudFront).

**অনুবাদ (Bangla Translation):**
* **ডিজাইন পরিচিতি:** ভিডিও আপলোড, বিভিন্ন কোয়ালিটিতে কনভার্ট (4K, 1080p, 720p) এবং ইন্টারনেটের স্পিড অনুযায়ী ভিডিও প্লে করা।
* **মূল কৌশল:**
  ১. **ট্রান্সকোডিং:** ভিডিও আপলোড হলে FFmpeg দিয়ে তা ছোট ছোট টুকরোতে কেটে HLS ফরম্যাটে (`.m3u8`) রূপান্তর করা।
  ২. **Adaptive Bitrate:** ইউজারের ইন্টারনেট স্লো হলে স্বয়ংক্রিয়ভাবে ভিডিও ৪৮০p-তে এবং ফাস্ট হলে ১০৮০p-তে প্লে করা।
  ৩. **CDN Caching:** বিশ্বের বিভিন্ন প্রান্তের ইউজারের কাছে পৌঁছাতে CDN ব্যবহার করা।

---

### **Q8: Design a Collaborative Real-Time Whiteboard / Canvas Editor like Figma or SleekDraw. / Figma বা SleekDraw-এর মতো রিয়েল-টাইম ক্যানভাস প্ল্যাটফর্ম কীভাবে ডিজাইন করবেন?**

**Answer (English):**
* **Requirements:** Multi-user live mouse cursor tracking, vector canvas state rendering with <50ms latency, conflict resolution, and End-to-End Encryption (E2EE).
* **Key Components:**
  1. **Canvas Rendering:** HTML5 Canvas API rendered using `requestAnimationFrame` on GPU composite thread.
  2. **Operational Transformation (OT) / CRDTs:** Use Conflict-Free Replicated Data Types (CRDTs) to resolve concurrent editing conflicts without server intervention.
  3. **WebSocket Pipeline & Ephemeral Cursor Messages:** High-frequency mouse cursor movements are emitted over WebSockets as un-persisted ephemeral messages.
  4. **Client-Side E2EE Encryption:** Encrypt stroke vector coordinates locally in browser using Web Crypto API (AES-GCM 256-bit) before broadcasting.

**অনুবাদ (Bangla Translation):**
* **ডিজাইন পরিচিতি:** একাধিক ইউজার একসাথে বোর্ডে ছবি আঁকার সময় ল্যাগ ছাড়া রিয়েল-টাইমে ডাটা দেখানো।
* **মূল কৌশল:**
  ১. **Canvas rendering:** HTML5 Canvas এবং GPU দিয়ে ৫০ms-এর কম সময়ে ছবি আঁকা।
  ২. **CRDTs:** একাধিক ইউজার একসাথে ক্লিক করলে কার দাগ আগে বসবে সেই কনফ্লিক্ট মেটানো।
  ৩. **E2EE Enryption:** সার্ভারে পাঠানোর আগে ব্রাউজারেই ড্রয়িং এনক্রিপ্ট করে দেওয়া।

---

### **Q9: Design an API Gateway Architecture for Microservices. / মাইক্রোসার্ভিস আর্কিটেকচারের জন্য API Gateway কীভাবে ডিজাইন করবেন?**

**Answer (English):**
* **Requirements:** Single entry point for all mobile/web clients, request routing, centralized authentication, rate limiting, payload SSL termination, and circuit breaking.
* **Key Components:**
  1. **Reverse Proxy & Routing:** Route `/api/v1/auth/*` to Auth Service, `/api/v1/orders/*` to Order Service.
  2. **Centralized Authentication Middleware:** Verify JWT tokens at the gateway before forwarding request to downstream microservices, injecting `x-user-id` headers.
  3. **Circuit Breaker Pattern:** Use tools like Opossum. If a downstream microservice failure rate exceeds 50%, circuit trips open, immediately returning fallback responses without overwhelming the broken service.
  4. **SSL Termination:** Decrypt HTTPS traffic at the Gateway and use lightweight HTTP inside internal private network.

**অনুবাদ (Bangla Translation):**
* **ডিজাইন পরিচিতি:** একাধিক মাইক্রোসার্ভিসের (Auth, Order, Payment) সামনে একটি একক গেটওয়ে বসানো।
* **মূল কৌশল:**
  ১. **রাউটিং:** রিকোয়েস্ট চিনে নির্দিষ্ট সার্ভিস অনুযায়ী পাঠাল।
  ২. **সেন্ট্রালাইজড লগইন:** টোকেন গেটওয়েতে চেক করে ভেতরে পাঠানো।
  ৩. **Circuit Breaker:** কোনো সার্ভিস ভেঙে পড়লে কিছুক্ষণের জন্য রিকোয়েস্ট পাঠানো বন্ধ রেখে সিস্টেম বাঁচানো।

---

### **Q10: Design a Web Crawler System like Google Search Crawler. / Google Search-এর মতো বিশাল ওয়েবের ডাটা স্ক্যান ও ক্রল করার সিস্টেম কীভাবে ডিজাইন করবেন?**

**Answer (English):**
* **Requirements:** Crawl billions of web pages, extract text and HTML links, store page contents efficiently, avoid duplicate crawls, and respect `robots.txt`.
* **Key Components:**
  1. **URL Frontier:** A priority queue storing URLs waiting to be crawled, ordered by domain authority and update frequency.
  2. **Politeness Module:** Avoid spamming a single domain by enforcing delays per host.
  3. **HTML Fetcher & Extractor:** Download web pages, parse HTML tags, and extract new outbound links.
  4. **Duplicate Removal (Bloom Filter):** Use a space-efficient **Bloom Filter** data structure to test whether a URL has already been crawled in $\mathcal{O}(1)$ time using minimal memory.
  5. **Storage:** Save raw web pages to HDFS / S3 and page index keywords to MongoDB/Elasticsearch.

**অনুবাদ (Bangla Translation):**
* **ডিজাইন পরিচিতি:** কোটি কোটি ওয়েবসাইট থেকে তথ্য পড়ে ডাটা সেভ রাখা।
* **মূল কৌশল:**
  ১. **URL Frontier:** অগ্রাধিকার অনুযায়ী যে ওয়েবসাইটগুলো ক্রল করা দরকার তাদের কিউতে সাজানো।
  ২. **Bloom Filter:** মেমোরিতে সামান্য ডাটা রেখে এক সেকেন্ডে যাচাই করা লিংকটি আগে পড়া হয়েছে কিনা।
  ৩. **Politeness:** কোনো একটি ওয়েবসাইটে একসাথে হাজার হাজার রিকোয়েস্ট না পাঠিয়ে ধীরে ধীরে পড়া (`robots.txt` মেনে)।
