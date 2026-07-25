# Socket.IO & REST API Technical Interview Guide

This guide contains **top technical interview questions**, architecture comparisons, code examples, and complete **Bangla translations** for:
1. **Socket.IO Core Concepts, Deep Dive & Security (Top 5 Questions)**
2. **Socket.IO vs REST API Architectural Comparison**
3. **REST API Core Principles, Design & Security (Top 5 Questions)**

---

## ⚡ Part 1: Top 5 Socket.IO Questions & Answers

### **Q1: What is Socket.IO and how does it work under the hood (Engine.IO & Fallbacks)? / Socket.IO কী এবং এর ভেতরে (Engine.IO & Fallbacks) কীভাবে কাজ করে?**

**Answer (English):**
Socket.IO is an event-driven library for real-time, bi-directional communication between web clients and servers. It is **not** purely a WebSocket implementation, but an abstraction built on top of **Engine.IO**.
* **Under the Hood Flow:**
  1. **Handshake & Fallback:** Socket.IO starts connection using HTTP Long-Polling first (`/socket.io/?transport=polling`).
  2. **WebSocket Upgrade:** Once the initial HTTP handshake succeeds, Engine.IO tests if WebSockets are supported by the client browser and network proxies. If supported, it upgrades the transport connection to native **WebSockets** (`transport=websocket`).
  3. **Auto-Reconnection:** If the WebSocket connection drops, Socket.IO automatically downgrades back to HTTP Long-Polling and attempts auto-reconnection in the background.

**অনুবাদ (Bangla Translation):**
Socket.IO হলো রিয়েল-টাইম, উভয়মুখী (Bi-directional) যোগাযোগের জন্য একটি ইভেন্ট-ড্রিভেন লাইব্রেরি। এটি সরাসরি কেবল WebSocket নয়, বরং **Engine.IO**-এর ওপর নির্মিত একটি ফ্রেমওয়ার্ক।
* **অভ্যন্তরীণ কাজের নিয়ম:**
  ১. কানেকশন শুরুর সময় এটি প্রথমে **HTTP Long-Polling** দিয়ে হ্যান্ডশেক তৈরি করে।
  ২. এরপর ক্লায়েন্ট ব্রাউজার ও নেটওয়ার্ক সমর্থন করলে এটি সংযোগটিকে আসল **WebSocket**-এ আপগ্রেড (Upgrade) করে নেয়।
  ৩. কোনো কারণে WebSocket সংযোগ বিচ্ছিন্ন হলে এটি স্বয়ংক্রিয়ভাবে পুনরায় Long-Polling-এ ফিরে যায় এবং অটো-রিকানেক্ট করতে থাকে।

---

### **Q2: What is the difference between Socket.IO and REST API, and when should you choose which? / Socket.IO এবং REST API-এর মধ্যে পার্থক্য কী এবং কখন কোনটি ব্যবহার করবেন?**

**Answer (English):**

| Feature | Socket.IO | REST API |
| :--- | :--- | :--- |
| **Communication Model** | Full-Duplex Bi-Directional (Persistent Connection) | Request-Response Half-Duplex (Stateless) |
| **Connection Lifecycle** | Single open TCP connection kept alive | New HTTP connection established per request |
| **Protocol** | WebSockets / Engine.IO transport | HTTP / HTTPS (`GET`, `POST`, `PUT`, `DELETE`) |
| **Overhead & Speed** | Ultra-low header overhead (~2-8 bytes per frame) | Higher HTTP header overhead (KB per request) |
| **Server Initiative** | Server can push data to client anytime | Server cannot push data without client request |
| **Best Use Cases** | Live chat, sports scores, live seat locking, stock tickers, collaborative whiteboards | CRUD operations, user login, payment checkout, report retrieval |

**When to Choose Which:**
* **Choose Socket.IO:** When data updates frequently in real time (<1 second intervals), or when the server must send spontaneous alerts to the client (e.g., GoNautika Ferry seat locking, ResQ emergency dispatch tracking).
* **Choose REST API:** For standard data fetching, submission, resource modification, and operations where caching and statelessness are beneficial.

**অনুবাদ (Bangla Translation):**

| বৈশিষ্ট্য | Socket.IO | REST API |
| :--- | :--- | :--- |
| **যোগাযোগের মডেল** | উভয়মুখী (Full-Duplex) স্থায়ী কানেকশন | একমুখী রিকোয়েস্ট-রেসপন্স (Half-Duplex) |
| **কানেকশন স্থায়ীত্ব** | একটি TCP কানেকশন অনবরত খোলা থাকে | প্রতি রিকোয়েস্টে নতুন HTTP কানেকশন তৈরি হয় |
| **প্রোটোকল** | WebSockets / Engine.IO | HTTP / HTTPS (`GET`, `POST`, `PUT`, `DELETE`) |
| **ফাইল সাইজ ও গতি** | খুবই সামান্য হেডার সাইজ (২-৮ বাইট), দ্রুতগতির | প্রতি রিকোয়েস্টে বড় HTTP হেডার পাঠানো হয় |
| **সার্ভার ইনিশিয়েটিভ** | সার্ভার ইচ্ছা করলেই ক্লায়েন্টে ডাটা পাঠাতে পারে | ইউজার রিকোয়েস্ট ছাড়া সার্ভার নিজে থেকে ডাটা পাঠাতে পারে না |
| **ব্যবহারের জায়গা** | লাইভ চ্যাট, রিয়েল-টাইম সিট লক, লাইভ মার্কার ট্র্যাকিং, শেয়ার্ড ক্যানভাস | ইউজার লগইন, তথ্য সেভ বা আপডেট (CRUD), পেমেন্ট |

---

### **Q3: How do Rooms, Namespaces, and Event Broadcasting work in Socket.IO? / Socket.IO-তে Rooms, Namespaces এবং Broadcasting কীভাবে কাজ করে?**

**Answer (English):**
Socket.IO provides powerful abstraction layers to organize connected clients:
1. **Namespaces (`io.of('/admin')`):** Split the Socket.IO server into separate communication channels running over the same single TCP connection.
2. **Rooms (`socket.join('ferry_101')`):** Arbitrary channels that sockets can `join` and `leave` on the server side. Used to group clients (e.g., users viewing the same ferry seat layout).
3. **Broadcasting Types:**
   * `socket.emit('event', data)`: Sends event ONLY to the current sender socket.
   * `socket.broadcast.emit('event', data)`: Sends event to ALL clients EXCEPT the sender.
   * `io.to('ferry_101').emit('event', data)`: Sends event to ALL sockets inside the specified room.
   * `io.emit('event', data)`: Sends event to ALL connected clients on the namespace.

**অনুবাদ (Bangla Translation):**
Socket.IO-তে ইউজারদের আলাদা করার উপায়:
১. **Namespaces:** একই কানেকশনের ভেতর আলাদা চ্যানেল তৈরি করা (যেমন `/admin` বা `/user`)।
২. **Rooms:** সার্ভার সাইডে ক্লায়েন্টদের গ্রুপ করা (যেমন একটি নির্দিষ্ট ফেরি রুমে যুক্ত থাকা সকল ইউজার)।
৩. **ইভেন্ট ব্রডকাস্টের নিয়ম:**
   * `socket.emit`: কেবল যে পাঠিয়েছে তাকে উত্তর দেওয়া।
   * `socket.broadcast.emit`: যে পাঠিয়েছে তাকে ছাড়া বাকি সব ইউজারকে ডাটা পাঠানো।
   * `io.to('room').emit`: একটি নির্দিষ্ট রুমের সবাইকে ডাটা পাঠানো (যেমন সিট লক হওয়া দেখানো)।
   * `io.emit`: সার্ভারের সাথে যুক্ত সমস্ত ইউজারকে ব্রডকাস্ট করা।

---

### **Q4: How do you handle Authentication and Middleware Security in Socket.IO? / Socket.IO-তে কীভাবে JWT অথেন্টিকেশন এবং সিকিউরিটি হ্যান্ডেল করবেন?**

**Answer (English):**
Authenticating real-time WebSocket connections is critical to prevent unauthorized event spoofing:
* **Client Handshake Auth:** The client passes the JWT token in the initial connection handshake object:
  ```javascript
  const socket = io('https://api.example.com', {
    auth: { token: 'Bearer eyJhbGciOi...' }
  });
  ```
* **Server Handshake Middleware:** The Socket.IO server uses a middleware (`io.use()`) to verify the JWT token before accepting the connection:
  ```javascript
  io.use((socket, next) => {
    const token = socket.handshake.auth.token;
    try {
      const decoded = jwt.verify(token, process.env.JWT_SECRET);
      socket.user = decoded; // Attach user info to socket
      next();
    } catch (err) {
      next(new Error('Authentication Error: Invalid Token'));
    }
  });
  ```

**অনুবাদ (Bangla Translation):**
Socket.IO-তে নিরাপদ অথেন্টিকেশনের নিয়ম:
* **ক্লায়েন্ট:** রিয়্যাক্ট ক্লায়েন্ট কানেকশন শুরু করার সময় `auth` অবজেক্টের ভেতর JWT টোকেন পাঠিয়ে দেয়।
* **সার্ভার মিডলওয়্যার:** সার্ভার সাইডে `io.use()` মিডলওয়্যার হ্যান্ডশেক থেকে টোকেন নিয়ে `jwt.verify()` করে। টোকেন সঠিক হলে সকেট কানেক্ট করতে দেয়, না হলে কানেকশন রিজেক্ট করে দেয়।

---

### **Q5: How do you scale Socket.IO horizontally across multiple server instances using Redis Adapter? / একাধিক সার্ভারে Socket.IO স্কেল (Horizontal Scaling) করতে Redis Adapter কীভাবে সাহায্য করে?**

**Answer (English):**
* **The Problem:** In a multi-server setup (e.g., Server A and Server B behind a Load Balancer), Client 1 is connected to Server A and Client 2 is connected to Server B. If Server A emits `io.to('room1').emit()`, Client 2 on Server B will **never receive the message** because Socket.IO memory states are isolated.
* **The Solution (Redis Adapter):**
  * Integrate `@socket.io/redis-adapter` backed by Redis Pub/Sub.
  * When Server A emits an event, the Redis Adapter publishes the event message to Redis Pub/Sub.
  * Server B subscribes to Redis, receives the event, and emits it to Client 2.
  * Enforce **Sticky Sessions** (IP Hash) on Nginx load balancer so HTTP polling handshakes hit the same server instance.

**অনুবাদ (Bangla Translation):**
* **সমস্যা:** লোড ব্যালেন্সারের অধীনে একাধিক সার্ভার থাকলে ১ নম্বর ইউজার সার্ভার-A এবং ২ নম্বর ইউজার সার্ভার-B তে যুক্ত থাকে। সার্ভার-A ইভেন্ট পাঠালে সার্ভার-B-এর ইউজার তা পায় না।
* **সমাধান:** `@socket.io/redis-adapter` এবং Redis Pub/Sub ব্যবহার করা হয়। সার্ভার-A কোনো ইভেন্ট পাঠালে তা Redis-এ পাবলিশ হয়, এবং সার্ভার-B তা রিড করে সাথে সাথে তার ইউজারের কাছে পৌঁছে দেয়।

---

## 🌐 Part 2: Top 5 REST API Questions & Answers

### **Q1: What is a REST API and what are the 6 Guiding Architectural Constraints of REST? / REST API কী এবং REST-এর ৬টি মূল স্থাপত্য নীতি (Constraints) কী কী?**

**Answer (English):**
REST (Representational State Transfer) is an architectural style for designing networked HTTP applications.
* **The 6 Guiding Constraints:**
  1. **Client-Server Architecture:** Separation of UI concerns from data storage concerns.
  2. **Statelessness:** Every request from client to server must contain all information necessary to understand and process the request; server stores no client session context.
  3. **Cacheability:** Responses must explicitly define themselves as cacheable or non-cacheable (`Cache-Control`).
  4. **Uniform Interface:** Standardized resources using URIs and HTTP verbs (`GET`, `POST`, `PUT`, `DELETE`).
  5. **Layered System:** Client cannot tell whether it is connected directly to the end server or an intermediate proxy/load balancer.
  6. **Code on Demand (Optional):** Ability to transfer executable code (e.g., JavaScript scripts) to the client.

**অনুবাদ (Bangla Translation):**
REST হলো ওয়েব এপিআই বানানোর আন্তর্জাতিক আর্কিটেকচারাল স্টাইল।
* **৬টি মূল নিয়ম:**
  ১. **Client-Server:** ফ্রন্টএন্ড এবং ব্যাকএন্ড সম্পূর্ণ আলাদা রাখা।
  ২. **Stateless:** সার্ভার কোনো সেশন মনে রাখবে না; প্রতিটি রিকোয়েস্টে প্রয়োজনীয় সব তথ্য (যেমন টোকেন) থাকতে হবে।
  ৩. **Cacheable:** রেসপন্স ব্রাউজারে ক্যাশ করা যাবে কিনা তা নির্দিষ্ট করা।
  ৪. **Uniform Interface:** সুনির্দিষ্ট URL ও HTTP Verbs (`GET`, `POST`) মেনে কাজ করা।
  ৫. **Layered System:** মাঝে লোড ব্যালেন্সার বা প্রক্সি থাকলে তা যেন ক্লায়েন্টের কাজে সমস্যা না করে।
  ৬. **Code on Demand:** প্রয়োজন সাপেক্ষে ক্লায়েন্টে এক্সিকিউটেবল কোড পাঠানো।

---

### **Q2: What is the difference between HTTP Verbs (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) and Idempotency? / HTTP Verbs এবং Idempotency বলতে কী বোঝায়?**

**Answer (English):**
* **Idempotency Definition:** An HTTP method is idempotent if executing it multiple times produces the exact same server state as executing it once.

| Verb | Usage | Safe? | Idempotent? |
| :--- | :--- | :--- | :--- |
| **GET** | Retrieve resource | Yes (Read-only) | Yes |
| **POST** | Create new resource | No (Modifies state) | **No** (Multiple calls create duplicate records) |
| **PUT** | Replace entire existing resource | No | **Yes** (Repeated calls overwrite with same state) |
| **PATCH** | Partial update of resource | No | **No** (Unless written deterministically) |
| **DELETE** | Remove resource | No | **Yes** (Resource stays deleted on repeated calls) |

**অনুবাদ (Bangla Translation):**
* **Idempotency:** কোনো এপিআই বারবার কল করলেও সার্ভারের ডাটার অবস্থা যদি প্রথমবারের মতোই থাকে, তাকে Idempotent বলে।
* **GET:** ডাটা পড়ার জন্য (Idempotent)।
* **POST:** নতুন ডাটা তৈরি করতে (Not Idempotent - বারবার দিলে ডুপ্লিকেট ডাটা হবে)।
* **PUT:** পুরো অবজেক্ট নতুন করে রিপ্লেস করতে (Idempotent)।
* **PATCH:** অবজেক্টের কিছু ফিল্ড আংশিক আপডেট করতে।
* **DELETE:** ডাটা মুছে ফেলতে (Idempotent)।

---

### **Q3: What are common HTTP Status Codes and their specific categories? / সাধারণ HTTP Status Codes এবং তাদের ক্যাটাগরিগুলো কী কী?**

**Answer (English):**
HTTP Status Codes indicate the result of an HTTP request:
* **2xx (Success):**
  * `200 OK`: Request succeeded.
  * `201 Created`: Resource successfully created (used in `POST`).
  * `204 No Content`: Request succeeded, no body returned (used in `DELETE`).
* **3xx (Redirection):**
  * `301 Moved Permanently` / `304 Not Modified` (Use cached version).
* **4xx (Client Errors):**
  * `400 Bad Request`: Invalid payload or parameters.
  * `401 Unauthorized`: Missing or invalid authentication token.
  * `403 Forbidden`: Authenticated, but lacks required permission/role.
  * `404 Not Found`: Resource URL does not exist.
  * `409 Conflict`: Resource state conflict (e.g., duplicate email).
  * `429 Too Many Requests`: Rate limit exceeded.
* **5xx (Server Errors):**
  * `500 Internal Server Error` / `502 Bad Gateway` / `503 Service Unavailable`.

**অনুবাদ (Bangla Translation):**
* **2xx (সফল):** 200 (সফল), 201 (নতুন ডাটা ক্রিয়েট), 204 (সফল কিন্তু বডি নেই)।
* **4xx (ক্লায়েন্ট ভুল):** 400 (ভুল ডাটা পাঠানো), 401 (টোকেন নেই বা ভুয়া), 403 (পারমিশন নেই), 404 (খুঁজে পাওয়া যায়নি), 409 (ডুপ্লিকেট ডাটার কনফ্লিক্ট), 429 (অতিরিক্ত রিকোয়েস্ট)।
* **5xx (সার্ভার ভুল):** 500 (সার্ভার কোড ক্র্যাশ), 502 (ব্যাড গেটওয়ে), 503 (সার্ভার ব্যস্ত/বন্ধ)।

---

### **Q4: How do you handle Versioning, Pagination, Filtering, and Sorting in REST APIs? / REST API-তে ভার্সনিং, পেজিনেশন, ফিল্টারিং এবং সর্টিং কীভাবে সাজাবেন?**

**Answer (English):**
Proper API design requires clean request semantics:
1. **API Versioning:** Use URI Versioning for backward compatibility: `/api/v1/users` or `/api/v2/users`.
2. **Pagination:**
   * **Offset-Based:** `/api/v1/orders?page=2&limit=20` (Uses DB `skip` and `limit`).
   * **Cursor-Based (Better):** `/api/v1/orders?cursor=64a7b2...&limit=20` (Faster for infinite scroll, avoids skip penalty).
3. **Filtering & Sorting:** Use query parameters cleanly:
   * `/api/v1/products?category=electronics&status=active&sort=-price` (`-price` denotes descending order).

**অনুবাদ (Bangla Translation):**
১. **ভার্সনিং:** ভবিষ্যতে কোড আপডেট হলেও আগের অ্যাপ যেন না ভেঙে যায় সে জন্য URL-এ ভার্সন দেওয়া (`/api/v1/users`)।
২. **পেজিনেশন:** অফসেট ভিত্তিক (`page=2&limit=20`) অথবা দ্রুতগতির কার্সার ভিত্তিক (`cursor=id`) পেজিনেশন করা।
৩. **ফিল্টারিং ও সর্টিং:** ক্যোয়ারি প্যারামিটার ব্যবহার করা (যেমন- `/api/v1/products?sort=-price`)।

---

### **Q5: How do you secure REST APIs against common security vulnerabilities? / REST API-কে সাইবার অ্যাটাক ও নিরাপত্তা ঝুঁকি থেকে কীভাবে সুরক্ষিত করবেন?**

**Answer (English):**
Securing REST APIs requires enforcing multiple security layers:
1. **Authentication & Authorization:** Use JWT tokens with short TTL stored in `HttpOnly` cookies, coupled with Role-Based Access Control (RBAC).
2. **Input Validation (Zod):** Validate and sanitize all incoming request bodies and query parameters to block MongoDB Operator Injection and SQL Injection.
3. **HTTP Security Headers (Helmet.js):** Hide `X-Powered-By: Express` header, enforce HSTS, and block Clickjacking.
4. **Rate Limiting:** Use Redis-backed `rate-limiter-flexible` to limit requests (e.g., max 100 requests per 15 minutes per IP).
5. **CORS (Cross-Origin Resource Sharing):** Whitelist specific frontend domains (`origin: 'https://myapp.com'`) instead of wildcard `*`.

**অনুবাদ (Bangla Translation):**
REST API সুরক্ষিত করার পদক্ষেপসমূহ:
১. **অথেন্টিকেশন:** `HttpOnly` কুকিতে JWT টোকেন রাখা ও রোল ভিত্তিক পারমিশন দেওয়া।
২. **ইনপুট ভ্যালিডেশন:** Zod স্কিমা দিয়ে ডাটা স্যানিটাইজ করে ডাটাবেজ ইনজেকশন বন্ধ করা।
৩. **Helmet.js:** সিআরএফ ও এইচটিটিপি সিকিউরিটি হেডার বসানো।
৪. **Rate Limiting:** অতিরিক্ত স্প্যামিং আটকাতে IP ভিত্তিক রিকোয়েস্ট লিমিট করা।
৫. **CORS:** নির্দিষ্ট ফ্রন্টএন্ড ডোমেইন চিনে এক্সেস দেওয়া।
