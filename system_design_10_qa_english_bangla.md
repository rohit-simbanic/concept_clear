# System Design Interview Questions & Answers (English & Bangla)

This guide contains **10 core technical System Design interview questions**, complete with architectural explanations, trade-offs, code/flow diagrams, and full **Bangla translations**.

---

## 📋 Table of Contents
1. Core Concepts: System Design, Scalability, Availability & Reliability
2. High-Level Design (HLD) vs Low-Level Design (LLD)
3. Load Balancing Algorithms & Sticky Sessions
4. CAP Theorem & Database Selection (CP vs AP)
5. Database Indexing, B-Trees & Query Optimization
6. Caching Strategies (Cache-Aside, Write-Through, Write-Back) & Redis LRU
7. Database Scaling: Replication vs Sharding
8. Message Queues & Asynchronous Processing (Bull Queue / Kafka)
9. Scaling WebSockets Horizontally across Multi-Node Clusters
10. API Gateway Rate Limiting & Sliding Window Log Algorithm

---

### **Q1: What is System Design, and what is the difference between Scalability, Availability, and Reliability? / সিস্টেম ডিজাইন কী এবং Scalability, Availability ও Reliability-এর মধ্যে পার্থক্য কী?**

**Answer (English):**
System Design is the process of architecting the modules, components, databases, network interfaces, and infrastructure for an application to meet specific scaling, security, and performance goals.
* **Scalability:** The system's ability to handle growing workloads (users/traffic) without degrading performance.
  * *Vertical Scaling (Scale-Up):* Adding more RAM/CPU to a single server.
  * *Horizontal Scaling (Scale-Out):* Adding more server instances behind a Load Balancer.
* **Availability:** The percentage of time a system remains operational and accessible to users (e.g., 99.99% Uptime = 52 minutes of downtime/year).
* **Reliability:** The probability that a system will perform its intended function without failure for a specified time (measured by Mean Time Between Failures - MTBF).

**অনুবাদ (Bangla Translation):**
সিস্টেম ডিজাইন হলো একটি অ্যাপ্লিকেশনের সার্ভার, ডাটাবেজ, সিকিউরিটি এবং আর্কিটেকচার নকশা করার প্রক্রিয়া যাতে তা হাজার হাজার ইউজারের ট্রাফিক অনায়াসে সামলাতে পারে।
* **Scalability (স্কেলেবিলিটি):** ইউজার বা ট্রাফিক বাড়লেও সিস্টেমের পারফরম্যান্স খারাপ না হওয়ার ক্ষমতা। (১টি বড় সার্ভার ব্যবহার করা হলো Vertical Scaling এবং একাধিক সার্ভার যুক্ত করা হলো Horizontal Scaling)।
* **Availability (এভেইলিবিলিটি):** সিস্টেম কতটা সময় চালু থাকে (যেমন ৯৯.৯৯% Uptime মানে বছরে সার্ভার সর্বোচ্চ ৫২ মিনিট বন্ধ থাকতে পারে)।
* **Reliability (রিলায়েবিলিটি):** সিস্টেমটি কোনো ভুল বা ক্র্যাশ ছাড়া একটানা সঠিকভাবে কাজ করার নিশ্চয়তা।

---

### **Q2: What is the difference between High-Level Design (HLD) and Low-Level Design (LLD)? / High-Level Design (HLD) এবং Low-Level Design (LLD)-এর মধ্যে পার্থক্য কী?**

**Answer (English):**

| Feature | High-Level Design (HLD) | Low-Level Design (LLD) |
| :--- | :--- | :--- |
| **Scope** | Macro System Architecture (Big Picture) | Micro System Implementation (Detailed Code) |
| **Target Audience** | System Architects, DevOps, Lead Engineers | Developers, Peer Code Reviewers |
| **Core Elements** | Load Balancers, DB Replication, Caching, CDN, Queues | Class Diagrams, SOLID Principles, Zod Schemas, Functions |
| **Focus** | How data flows between distributed components | How methods, algorithms, and data structures execute |

**অনুবাদ (Bangla Translation):**

| বৈশিষ্ট্য | High-Level Design (HLD) | Low-Level Design (LLD) |
| :--- | :--- | :--- |
| **পরিধি** | পুরো সিস্টেমের বড় আর্কিটেকচার চিত্র | কোডের ভেতরের নিখুঁত নকশা ও ইমপ্লিমেন্টেশন |
| **কাদের জন্য** | সিস্টেম আর্কিটেক্ট, ডেবঅপ্স এবং লিড ইঞ্জিনিয়ার | সফটওয়্যার ডেভেলপার ও কোড রিভিউয়ার |
| **প্রধান উপাদান** | লোড ব্যালেন্সার, ডাটাবেজ রেপ্লিকেশন, ক্যাশ, কিউ | ক্লাস ডায়াগ্রাম, SOLID নীতি, Zod স্কিমা, কোড স্ট্রাকচার |
| **মূল লক্ষ্য** | সার্ভার ও মডিউলগুলোর মধ্যে ডাটা কীভাবে প্রবাহিত হবে | কোডের প্রতিটি ফাংশন ও অলগরিদম কীভাবে কাজ করবে |

---

### **Q3: What is Load Balancing and what are the main load balancing algorithms? / লোড ব্যালেন্সিং কী এবং এর প্রধান অ্যালগরিদমগুলো কী কী?**

**Answer (English):**
Load Balancing is the process of distributing incoming network traffic across multiple backend server instances to prevent any single server from becoming a bottleneck.
* **Common Algorithms:**
  1. **Round Robin:** Sequential request distribution to servers in order.
  2. **Least Connections:** Routes traffic to the server with the fewest active connections.
  3. **IP Hash (Sticky Sessions):** Hashes client IP to ensure a specific user hits the exact same server (useful for HTTP polling sessions).
  4. **Weighted Round Robin:** Distributes requests based on server hardware capacity weights.

**অনুবাদ (Bangla Translation):**
ইনকামিং ইউজার ট্রাফিক একাধিক সার্ভারে সমানভাবে ভাগ করে দেওয়ার মেকানিজমকে **Load Balancing** বলে (যেমন Nginx, HAProxy, AWS ALB)।
* **প্রধান অ্যালগরিদমসমূহ:**
  ১. **Round Robin:** পর্যায়ক্রমে ১টি ১টি করে সব সার্ভারে রিকোয়েস্ট পাঠানো।
  ২. **Least Connections:** যে সার্ভারে কানেকশন বা চাপ কম সেখানে রিকোয়েস্ট পাঠানো।
  ৩. **IP Hash (Sticky Sessions):** নির্দিষ্ট ইউজারের রিকোয়েস্ট সবসময় একই সার্ভারে পাঠানো।
  ৪. **Weighted Round Robin:** সার্ভারের র্যাম/সিপিইউ ক্ষমতার ওপর ভিত্তি করে অনুপাত অনুযায়ী রিকোয়েস্ট পাঠানো।

---

### **Q4: Explain the CAP Theorem and how it influences database selection. / CAP Theorem কী এবং এটি ডাটাবেজ নির্বাচনে কীভাবে ভূমিকা রাখে?**

**Answer (English):**
The CAP Theorem states that a distributed data store can simultaneously provide at most **two out of three** guarantees:
1. **Consistency (C):** Every read receives the most recent write or an error.
2. **Availability (A):** Every non-failing node returns a non-error response (without guarantee that it contains the latest write).
3. **Partition Tolerance (P):** The system continues operating despite network message drops between nodes.

* **Database Classification:**
  * **CP Systems (Consistency + Partition Tolerance):** Prefers strict data accuracy over availability (e.g., MongoDB, HBase, Redis). Good for banking/inventory.
  * **AP Systems (Availability + Partition Tolerance):** Prefers serving data even if stale (e.g., Cassandra, DynamoDB, CouchDB). Good for social media feeds.

**অনুবাদ (Bangla Translation):**
CAP Theorem অনুযায়ী একটি ডিস্ট্রিবিউটেড ডাটাবেজ একই সাথে ৩টি সুবিধার মধ্যে **সর্বোচ্চ ২টি** দিতে পারে:
১. **Consistency (C):** সব ইউজার একই সময়ে একদম লেটেস্ট সঠিক ডাটা দেখবে।
২. **Availability (A):** সার্ভার সবসময় উত্তর দেবে (যদিও ডাটা পুরোনো হতে পারে)।
৩. **Partition Tolerance (P):** সার্ভারগুলোর মধ্যকার নেটওয়ার্কের তার ছিঁড়ে গেলেও ডাটাবেজ বন্ধ হবে না।

* **ডাটাবেজ শ্রেণীবিভাগ:**
  * **CP Systems (MongoDB, Redis):** ডাটা শতভাগ সঠিক দেখানোর পক্ষে (পেমেন্ট বা স্টকের জন্য সেরা)।
  * **AP Systems (Cassandra, DynamoDB):** ডাটা কিছু দেরিতে আপডেট হলেও সার্ভিস চાલુ রাখার পক্ষে (লাইক বা সোশ্যাল ফিডের জন্য সেরা)।

---

### **Q5: How does Database Indexing work and what are B-Trees and Compound Indexes? / ডাটাবেজ ইনডেক্সিং কীভাবে কাজ করে এবং B-Trees ও Compound Indexing কী?**

**Answer (English):**
Without an index, the database executes a full table/collection scan (`COLLSCAN`), inspecting every single row ($\mathcal{O}(N)$).
* **B-Tree Indexing:** An index creates a self-balancing search tree structure (B-Tree/B+Tree) on target columns, reducing lookup time from $\mathcal{O}(N)$ to $\mathcal{O}(\log N)$.
* **Compound Indexing:** Creating an index on multiple fields in a specific order:
  ```javascript
  db.providers.createIndex({ location: "2dsphere", isAvailable: 1, serviceType: 1 });
  ```
  The order of keys matters: Leftmost prefix rule must be followed for queries to utilize the index efficiently.

**অনুবাদ (Bangla Translation):**
ইনডেক্স ছাড়া ডাটাবেজ প্রতিটি সারি ধরে ধরে পরীক্ষা করে (COLLSCAN)। ইনডেক্স বসালে একটি B-Tree ডাটা স্ট্রাকচার তৈরি হয়, যা সেকেন্ডের মধ্যে ডাটা খুঁজে আনে (IXSCAN)।
* **Compound Indexing:** একাধিক কলামের ওপর একত্রে ইনডেক্স বসানো (যেমন- `{ location: "2dsphere", isAvailable: 1 }`), যা একই সাথে ফিল্টার ও সর্ট করতে ডাটাবেজকে সাহায্য করে।

---

### **Q6: What is Caching, and what are Cache-Aside, Write-Through, and Write-Back strategies? / ক্যাশিং কী এবং Cache-Aside, Write-Through ও Write-Back স্ট্র্যাটেজি কী?**

**Answer (English):**
Caching stores high-frequency read data in ultra-fast RAM memory (e.g., Redis) to eliminate disk I/O bottlenecks.
* **Cache-Aside (Lazy Loading):** App reads from cache first. If cache miss, app reads from DB, writes to cache, and returns data.
* **Write-Through:** App writes to cache first; cache synchronously writes to DB before returning. Guarantees consistency.
* **Write-Back (Write-Behind):** App writes to cache immediately; cache asynchronously writes to DB in background batches. Ultra-fast writes, but risks data loss if cache crashes.

**অনুবাদ (Bangla Translation):**
ক্যাশিং হলো বারবার পড়া ডাটা র্যামে (RAM/Redis) জমা রাখা যাতে ডাটাবেজের ওপর চাপ না পড়ে।
* **Cache-Aside:** আগে র্যামে ডাটা খোজা হয়, না পেলে ডাটাবেজ থেকে এনে র্যামে জমা করে ক্লায়েন্টকে দেওয়া হয়।
* **Write-Through:** ডাটা সেভ করার সময় র্যাম এবং ডাটাবেজে একই সাথে সেভ করা হয়।
* **Write-Back:** আগে র্যামে দ্রুত সেভ করে দেওয়া হয় এবং ব্যাকগ্রাউন্ডে ধীরে ধীরে ডাটাবেজে রাইট করা হয় (খুবই দ্রুত কিন্তু র্যাম ক্র্যাশ করলে ডাটা হারানোর ঝুঁকি থাকে)।

---

### **Q7: What is Database Sharding versus Database Replication? / ডাটাবেজ Sharding এবং Replication-এর মধ্যে পার্থক্য কী?**

**Answer (English):**
* **Replication:** Copying the entire database across multiple server nodes.
  * *Primary Node:* Accepts all write operations.
  * *Secondary Nodes:* Replicate primary write log (oplog) and serve read operations ($O(N)$ read scaling).
* **Sharding:** Partitioning a huge dataset horizontally across separate database clusters based on a **Shard Key** ($O(N)$ write & storage scaling).
  * *Example:* Users A-M stored on Shard 1; Users N-Z stored on Shard 2.

**অনুবাদ (Bangla Translation):**
* **Replication:** পুরো ডাটাবেজের অবিকল কপি একাধিক সার্ভারে রাখা (১টি Primary লেখার কাজ করে এবং অন্য Secondary গুলো রিড করার কাজ করে)।
* **Sharding:** ডাটাবেজ অনেক বড় হয়ে গেলে টেবিলকে ভেঙে আলাদা আলাদা ডাটাবেজ সার্ভারে ভাগ করে রাখা (যেমন A-M অক্ষরের ইউজার সার্ভার-১ এ এবং N-Z অক্ষরের ইউজার সার্ভার-২ এ)।

---

### **Q8: What is a Message Queue and why is Asynchronous Processing crucial in System Design? / Message Queue কী এবং Asynchronous Processing কেন জরুরি?**

**Answer (English):**
A Message Queue (e.g., Bull Queue, RabbitMQ, Kafka) is an asynchronous communication buffer between Producer services and Consumer workers.
* **Why it's crucial:**
  1. **Decoupling:** Producers add jobs without waiting for workers to complete.
  2. **Event Loop Unblocking:** API endpoints return instant HTTP responses while heavy tasks (PDF generation, SMS dispatch, video transcoding) execute in background.
  3. **Traffic Spikes Buffering:** Absorbs sudden load spikes without crashing workers.

**অনুবাদ (Bangla Translation):**
Message Queue (যেমন Bull Queue, Kafka) হলো ব্যাকগ্রাউন্ড কাজের একটি পাইপলাইন।
* **কেন জরুরি:** ইমেইল পাঠানো, এসএমএস নোটিফিকেশন বা ফাইল কমপ্রেস করার মতো ভারী কাজ এপিআই থেকে সরিয়ে ব্যাকগ্রাউন্ডে করায় এপিআই স্পিড ১০০ms-এর নিচে থাকে এবং সার্ভার ডাউন হওয়া থেকে বাঁচে।

---

### **Q9: How do you scale WebSockets horizontally across multiple server instances? / একাধিক সার্ভারে WebSockets (Socket.IO) কীভাবে স্কেল করবেন?**

**Answer (English):**
* **The Challenge:** WebSocket connections are stateful. If User 1 is on Server A and User 2 is on Server B, Server A emitting an event cannot reach User 2 directly.
* **The Solution:**
  1. **Redis Pub/Sub Adapter (`@socket.io/redis-adapter`):** Server A publishes the event to Redis Pub/Sub. Redis broadcasts it to Server B, which delivers it to User 2's socket.
  2. **Nginx Sticky Sessions:** Configure IP Hash sticky sessions on Nginx so initial HTTP Long-Polling handshakes hit the exact same server instance.

**অনুবাদ (Bangla Translation):**
* **সমস্যা:** ইউজার ১ সার্ভার-A এবং ইউজার ২ সার্ভার-B তে থাকলে সকেট ইভেন্ট এক সার্ভার থেকে অন্য সার্ভারে পৌঁছায় না।
* **সমাধান:** **Redis Pub/Sub Adapter** ব্যবহার করা হয়। সার্ভার-A কোনো ইভেন্ট পাঠালে তা Redis-এ পাবলিশ হয় এবং সার্ভার-B তা রিড করে ইউজার ২-এর কাছে পৌঁছে দেয়।

---

### **Q10: What is a Rate Limiter and how does the Sliding Window Log Algorithm work in Redis? / Rate Limiter কী এবং Redis-এ Sliding Window Log অ্যালগরিদম কীভাবে কাজ করে?**

**Answer (English):**
A Rate Limiter throttles client requests to protect backend services from DDoS attacks, scraping, and resource exhaustion.
* **Sliding Window Log Algorithm (Redis ZSET):**
  1. Store client request timestamps as scores inside a Redis Sorted Set (`ZSET`).
  2. Upon receiving a request, remove all entries older than the current window: `ZREMRANGEBYSCORE key 0 (now - window)`.
  3. Count total remaining requests: `ZCARD key`.
  4. If `ZCARD > limit`, return HTTP `429 Too Many Requests`. Otherwise, add current timestamp `ZADD key now now`.

**অনুবাদ (Bangla Translation):**
হ্যাকারের স্প্যামিং বা DDoS আক্রমণ থেকে সার্ভার বাঁচাতে প্রতি মিনিটে নির্দিষ্ট সংখ্যক রিকোয়েস্টের সীমা বেঁধে দেওয়াকে **Rate Limiter** বলে।
* **Sliding Window Algorithm:** Redis-এর `ZSET` ব্যবহার করে ইউজারের প্রতিটি রিকোয়েস্টের সময় সেভ রাখা হয়। ১ মিনিটের পুরোনো রিকোয়েস্ট মুছে বর্তমান রিকোয়েস্টের সংখ্যা গণনা করা হয়; সীমা পার হলে **HTTP 429** এরর দেওয়া হয়।
