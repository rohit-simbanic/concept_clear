# Full-Stack Master Technical Interview Guide

This guide contains in-depth interview questions, architectural breakdowns, code examples, and complete Bangla translations for:
1. **Payment Gateway Integration (Razorpay / Stripe)**
2. **Top 10 MongoDB Questions**
3. **Top 10 TypeScript Questions**
4. **Top 5 Redis Questions**
5. **Top 5 Docker Questions**
6. **Top 5 Bull Queue Questions**
7. **Top 5 Jest Questions**
8. **Top 5 CI/CD & Deployment Questions**

---

## 💳 1. Payment Gateway Integration Architecture

### **Q: How do you implement Payment Gateway Integration (e.g., Razorpay / Stripe) in a full-stack production application? / একটি ফুল-স্ট্যাক প্রজেক্টে পেমেন্ট গেটওয়ে (Razorpay / Stripe) কীভাবে বাস্তবায়ন করবেন?**

**Answer (English):**
Implementing payment integration requires an end-to-end multi-step flow focusing on security, data integrity, and idempotency:

```
[Client App] ─── (1. Request Order) ───> [Express Server] ─── (2. Create Order API) ───> [Payment Gateway]
     │                                         │                                               │
     │ <─── (4. Launch SDK with Order ID) ─────┴───── (3. Return Order ID) <───────────────────────┘
     │
     ├─── (5. User Pays via Card/UPI) ───> [Payment Gateway]
     │                                           │
     │ <─── (6. Returns Payment Signature) ──────┤
     │                                           ├─── (7. Asynchronous Webhook) ───> [Express Server]
     └─── (8. Verify Signature API) ───────────> [Express Server]
                                                       │
                                                       └─── (9. Update DB Transaction)
```

1. **Order Creation (Backend):**
   * Client requests a purchase (`POST /api/checkout`).
   * The Express backend initiates an order creation API call to Razorpay/Stripe with amount, currency, and receipt ID.
   * Server returns the generated `order_id` to the client.

2. **Client Checkout (Frontend):**
   * React frontend launches the Razorpay/Stripe Checkout SDK passing the `order_id`.
   * User enters payment details (Card, UPI, Netbanking).

3. **Signature Verification (Backend):**
   * After payment, the SDK returns `razorpay_payment_id`, `razorpay_order_id`, and `razorpay_signature`.
   * Frontend sends these details to backend (`POST /api/verify-payment`).
   * Backend verifies HMAC-SHA256 signature using the secret key:
     `generated_signature = hmac_sha256(order_id + "|" + payment_id, secret_key)`
   * If signatures match, mark booking/order as paid.

4. **Webhooks for Fail-Safe Processing:**
   * Client-side redirects can fail if the user closes the browser or network drops.
   * Implement Webhooks (`payment.captured`, `payment.failed`).
   * Server listens to raw webhook events, verifies webhook signatures, and updates order status asynchronously.

5. **Idempotency & Race Condition Prevention:**
   * Check if `payment_id` has already been processed in Redis or MongoDB before executing updates to prevent double-fulfillment.

**অনুবাদ (Bangla Translation):**
পেমেন্ট ইন্টিগ্রেশন বাস্তবায়নের সম্পূর্ণ পদ্ধতি:
১. **অর্ডার তৈরি (ব্যাকএন্ড):** ক্লায়েন্ট কেনার রিকোয়েস্ট পাঠালে এক্সপ্রেস সার্ভার পেমেন্ট গেটওয়েতে (Razorpay/Stripe) রিকোয়েস্ট পাঠিয়ে একটি `order_id` তৈরি করে ক্লায়েন্টে পাঠায়।
২. **ক্লায়েন্ট চেকআউট (ফ্রন্টএন্ড):** রিয়্যাক্ট ফ্রন্টএন্ড পেমেন্ট গেটওয়ের SDK অন করে এবং `order_id` দিয়ে ইউজারের থেকে পেমেন্ট (Card/UPI) গ্রহণ করে।
৩. **সিগনেচার যাচাই (সিকিউরিটি):** পেমেন্ট শেষে গেটওয়ে `payment_id` ও `signature` দেয়। সার্ভারে HMAC-SHA256 হ্যাশ অ্যালগরিদম দিয়ে গোপন Secret Key দিয়ে সিগনেচার মেলালেই কেবল অর্ডারের স্ট্যাটাস "Paid" করা হয়।
৪. **ওয়েবহুক (Webhooks):** ইউজার ব্রাউজার বন্ধ করে দিলে যেন টাকা পাওয়ার তথ্য হারিয়ে না যায়, তাই সার্ভার গেটওয়ের আসিনক্রোনাস ওয়েবহুক থেকে ডাটা রিসিভ করে অর্ডার নিশ্চিত করে।
৫. **আইডেমপোটেন্সি:** ডুপ্লিকেট পেমেন্ট প্রসেস বন্ধ করতে প্রসেস করা `payment_id` Redis বা ডাটাবেজে ট্র্যাক রাখা হয়।

---

## 🍃 2. Top 10 MongoDB Questions

### **Q1: What is the difference between Document-Oriented (NoSQL) and Relational (SQL) databases, and when should you choose MongoDB? / NoSQL এবং SQL ডাটাবেজের মধ্যে পার্থক্য কী এবং কখন MongoDB বেছে নেবেন?**

**Answer (English):**
* **Relational (SQL):** Tables with fixed schemas, structured rows, and strict foreign key relationships. Best for complex multi-table joins and ACID transactions (e.g., banking).
* **Document-Oriented (MongoDB):** Flexible JSON-like (BSON) dynamic schemas. High write throughput, horizontal scaling via sharding, and embedded document structures. Best for real-time analytics, rapid prototyping, catalog management, and high-velocity unstructured/semi-structured data.

**অনুবাদ (Bangla Translation):**
* **SQL:** নির্দিষ্ট টেবিল ও কলাম স্কিমা এবং রিলেশনশিপ যুক্ত ডাটাবেজ (যেমন PostgreSQL, MySQL)। ব্যাংকিং বা জটিল রিলেশন ভিত্তিক কাজের জন্য সেরা।
* **MongoDB (NoSQL):** ফ্লেক্সিবল BSON/JSON ডকুমেন্ট ভিত্তিক ডাটাবেজ। গতিশীল স্কিমা, দ্রুত ডাটা পড়া/লেখা এবং ডাইনামিক ফিল্ডের কাজের জন্য সেরা (যেমন ই-কমার্স ক্যাটালগ, রিয়েল-টাইম অ্যাপ)।

---

### **Q2: How does Indexing work in MongoDB and how do you analyze query performance using `explain()`? / MongoDB-তে ইনডেক্সিং কীভাবে কাজ করে এবং `explain()` দিয়ে কীভাবে পারফরম্যান্স অ্যানালাইসিস করবেন?**

**Answer (English):**
MongoDB uses B-Tree data structures to maintain indexes. Without an index, MongoDB must execute a **COLLSCAN (Collection Scan)**, inspecting every single document in a collection ($\mathcal{O}(N)$).
* **Types of Indexes:** Single Field, Compound Index, `2dsphere` (Geospatial), Text Index, TTL Index.
* **Analyzing Queries:** Calling `.explain("executionStats")` on a query shows:
  * `executionStage`: `IXSCAN` (Index Scan - Fast) vs `COLLSCAN` (Collection Scan - Slow).
  * `totalDocsExamined`: Number of documents scanned.
  * `executionTimeMillis`: Total execution duration.

**অনুবাদ (Bangla Translation):**
ইনডেক্স ছাড়া MongoDB পুরো কালেকশনের প্রতিটি ডকুমেন্ট চেক করে (COLLSCAN)। ইনডেক্স বসালে B-Tree ডাটা স্ট্রাকচার ব্যবহার করে দ্রুত ডাটা খুঁজে আনে (IXSCAN)। `.explain("executionStats")` ব্যবহার করে কোয়েরি কত সময় নিচ্ছে এবং ইনডেক্স ব্যবহার করছে কিনা তা পরীক্ষা করা হয়।

---

### **Q3: Explain the MongoDB Aggregation Pipeline and its core stages. / MongoDB Aggregation Pipeline কী এবং এর প্রধান ধাপসমূহ ব্যাখ্যা করুন।**

**Answer (English):**
The Aggregation Pipeline is a framework for data transformation and analytics, processing documents through multi-stage pipelines:
* `$match`: Filters documents (like SQL `WHERE`).
* `$group`: Groups documents by a specified key and performs aggregate calculations (like SQL `GROUP BY`, `$sum`, `$avg`).
* `$lookup`: Performs left outer joins with other collections (like SQL `LEFT JOIN`).
* `$unwind`: Deconstructs an array field into individual documents.
* `$project`: Reshapes output fields (includes, excludes, or computes new fields).

**অনুবাদ (Bangla Translation):**
Aggregation Pipeline হলো ডাটা এনালাইসিস ও ট্রান্সফর্ম করার শক্তিশালী ফ্রেমওয়ার্ক:
* `$match`: ডাটা ফিল্টার করা।
* `$group`: নির্দিষ্ট ফিল্ড ধরে গ্রুপ করে যোগ/গড় বের করা।
* `$lookup`: অন্য কালেকশনের সাথে জয়েন (Join) করা।
* `$unwind`: অ্যারে ভেঙে আলাদা আলাদা ডকুমেন্ট করা।
* `$project`: আউটপুটে কোন কোন ফিল্ড দেখাবে তা ঠিক করা।

---

### **Q4: How do Multi-Document ACID Transactions work in MongoDB? / MongoDB-তে Multi-Document ACID Transactions কীভাবে কাজ করে?**

**Answer (English):**
Since MongoDB v4.0, multi-document ACID transactions are supported across replica sets using sessions:
```javascript
const session = await mongoose.startSession();
session.startTransaction();
try {
  await Account.updateOne({ _id: fromAcc }, { $inc: { balance: -100 } }, { session });
  await Account.updateOne({ _id: toAcc }, { $inc: { balance: 100 } }, { session });
  await session.commitTransaction();
} catch (error) {
  await session.abortTransaction();
} finally {
  session.endSession();
}
```
If any operation fails, `abortTransaction()` rolls back all modifications to maintain 100% data consistency.

**অনুবাদ (Bangla Translation):**
MongoDB-তে `startSession()` এবং `startTransaction()` দিয়ে মাল্টি-ডকুমেন্ট ট্রানজ্যাকশন করা হয়। এতে মাঝপথে কোনো কাজ ফেল করলে `abortTransaction()` সম্পূর্ণ কাজ আগের অবস্থায় ফিরিয়ে নেয় (Rollback)।

---

### **Q5: When should you Embed documents versus Reference documents in MongoDB schema design? / MongoDB-তে কখন Embedding এবং কখন Referencing ব্যবহার করবেন?**

**Answer (English):**
* **Embed (Denormalization):** Put child documents inside parent document. Use when there is a 1-to-1 or 1-to-Few relationship, data is queried together frequently, and atomic updates are needed. (e.g., User addresses).
* **Reference (Normalization):** Store document IDs linking collections. Use when there is a 1-to-Many or Many-to-Many relationship, data is updated independently, or child documents grow infinitely exceeding the 16MB document limit. (e.g., User and Orders).

**অনুবাদ (Bangla Translation):**
* **Embed (একের ভেতর সব):** ১-টু-১ বা কম সংখ্যক ডাটার ক্ষেত্রে (যেমন ইউজারের ঠিকানা)। একসাথে দ্রুত লোড হয়।
* **Reference (আইডি লিংক):** ১-টু-মেনি বা বড় ডাটার ক্ষেত্রে (যেমন ইউজার ও তার হাজার হাজার অর্ডার)। এটি ডকুমেন্টের ১৬MB সাইজ লিমিট অতিক্রম করা থেকে বাঁচায়।

---

### **Q6: What is a MongoDB Replica Set and how does automated failover work? / MongoDB Replica Set কী এবং অটোমেটিক ফেলওভার কীভাবে কাজ করে?**

**Answer (English):**
A Replica Set is a group of MongoDB nodes maintaining identical data sets for high availability and redundancy.
* **Nodes:** 1 Primary node (handles all writes) and 2+ Secondary nodes (replicate oplog, serve read operations).
* **Failover:** If Primary node crashes, Secondaries hold an automated election using Heartbeat signals and elect a new Primary within seconds without application downtime.

**অনুবাদ (Bangla Translation):**
Replica Set হলো একাধিক সার্ভার নোডের গ্রুপ। এতে ১টি Primary Node (পড়া ও লেখা হ্যান্ডেল করে) এবং একাধিক Secondary Node (ডাটার কপি রাখে) থাকে। প্রাইমারি ডাউন হলে সেকেন্ডারি নোডগুলো নিজেরাই ভোট দিয়ে নতুন প্রাইমারি সার্ভার বানিয়ে নেয়।

---

### **Q7: What is Database Sharding in MongoDB and how do you choose a good Shard Key? / MongoDB Sharding কী এবং কীভাবে একটি ভালো Shard Key বেছে নেবেন?**

**Answer (English):**
Sharding is a method for horizontal scaling, distributing data across multiple physical servers (Shards) using a **Shard Key**.
* **Good Shard Key Qualities:** High Cardinality (many unique values), High Variance (even data distribution), and Non-Monotonically Increasing (prevents write hotspotting on a single shard). E.g., Hashed User ID or `{ country: 1, userId: 1 }`.

**অনুবাদ (Bangla Translation):**
Sharding হলো একাধিক ফিজিক্যাল সার্ভারে ডাটা ভাগ করে রাখার উপায়। একটি ভালো Shard Key-তে প্রচুর বৈচিত্র্যময় মান (High Cardinality) থাকতে হয় যাতে সব সার্ভারে সমানভাবে ডাটা বন্টন হয়।

---

### **Q8: What are Capped Collections and Time-To-Live (TTL) Indexes in MongoDB? / MongoDB-তে Capped Collections এবং TTL Indexes কী?**

**Answer (English):**
* **Capped Collections:** Fixed-size circular collections that maintain insertion order. Once allocated space is full, oldest documents are overwritten automatically. Best for high-throughput logging.
* **TTL Indexes:** Special single-field indexes that automatically delete documents after a specified time threshold (using `expireAfterSeconds`). Best for sessions, OTPs, and temporary tokens.

**অনুবাদ (Bangla Translation):**
* **Capped Collections:** ফিক্সড সাইজের গোলাকার কালেকশন। জায়গা ভরে গেলে নতুন ডাটা ঢোকার সময় অটোমেটিক সবচেয়ে পুরোনো ডাটা মুছে যায় (লগ ফাইলের জন্য সেরা)।
* **TTL Indexes:** নির্দিষ্ট সময় পার হলে স্বয়ংক্রিয়ভাবে ডাটা মুছে ফেলার ইনডেক্স (যেমন OTP বা সেশন মেয়াদ শেষ করা)।

---

### **Q9: Explain MongoDB Write Concern and Read Concern. / MongoDB Write Concern এবং Read Concern বলতে কী বোঝায়?**

**Answer (English):**
* **Write Concern:** Controls the level of acknowledgement requested from MongoDB for write operations. `w: 1` acknowledges primary write; `w: "majority"` acknowledges after majority of replica nodes confirm the write.
* **Read Concern:** Controls the consistency level of data read. `readConcern: "majority"` ensures read data has been committed by a majority of replica nodes and cannot be rolled back.

**অনুবাদ (Bangla Translation):**
* **Write Concern:** সার্ভারে ডাটা সেভ হওয়ার পর কনফার্মেশন চাওয়ার মাত্রা (`w: majority` দিলে বেশিরভাগ নোডে সেভ হওয়ার পর কনফার্মেশন পাঠায়)।
* **Read Concern:** রিড করা ডাটা কতটা সুরক্ষিত তা নির্ধারণ করে (`majority` নিশ্চিত করে ডাটা আর বাতিল হবে না)।

---

### **Q10: What are common performance bottlenecks in MongoDB and how do you fix them? / MongoDB-র পারফরম্যান্স স্লো হওয়ার প্রধান কারণ ও তা সমাধানের উপায় কী?**

**Answer (English):**
1. **Unindexed Queries:** Missing indexes cause FULL scans $\rightarrow$ Fix by adding indexes.
2. **RAM Exhaustion:** Working set size exceeds available RAM $\rightarrow$ Upgrade RAM or scale horizontally via Sharding.
3. **Over-fetching:** Returning entire 16MB documents when 2 fields are needed $\rightarrow$ Use Projections (`select('name email')`).
4. **Connection Exhaustion:** Creating new DB connection per HTTP request $\rightarrow$ Use Mongoose connection pooling (`maxPoolSize: 100`).

**অনুবাদ (Bangla Translation):**
১. ইনডেক্স না থাকা $\rightarrow$ কলামে ইনডেক্স বসানো।
২. মেমোরি (RAM) কম থাকা $\rightarrow$ র্যাম বাড়ানো বা শার্ডিং করা।
৩. অপ্রয়োজনীয় ডাটা ফেচ করা $\rightarrow$ Projection ব্যবহার করে নির্দিষ্ট ফিল্ড আনা।
৪. অতিরিক্ত কানেকশন খোলা $\rightarrow$ Connection Pool ব্যবহার করা।

---

## 🟦 3. Top 10 TypeScript Questions

### **Q1: What is the difference between `interface` and `type` alias in TypeScript, and when should you use which? / TypeScript-এ `interface` এবং `type` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
* **Interface:** Designed for object structure definitions and OOP contract definitions. Supports **Declaration Merging** (multiple interface declarations with same name merge automatically) and extension (`extends`).
* **Type Alias:** More flexible. Can define primitives, Unions (`type A = B | C`), Tuples, and Mapped types. Does not support declaration merging.
* *Best Practice:* Use `interface` for public API models, libraries, and object-oriented contracts; use `type` for unions, primitives, and utility types.

**অনুবাদ (Bangla Translation):**
* **Interface:** অবজেক্টের স্ট্রাকচার এবং অবজেক্ট-ওরিয়েন্টেড ডিজাইনের জন্য সেরা। একই নামের একাধিক Interface স্বয়ংক্রিয়ভাবে একত্রিত (Declaration Merging) হতে পারে।
* **Type:** ইউনিয়ন টাইপ (`A | B`), টাপল বা প্রিমিটিভ ডাটা ডিফাইন করতে ব্যবহৃত হয়।

---

### **Q2: What is the difference between `any`, `unknown`, and `never` types? / `any`, `unknown`, এবং `never` টাইপের মধ্যে পার্থক্য কী?**

**Answer (English):**
* **`any`:** Disables all type-checking. Allows assigning any value and calling any property (unsafe).
* **`unknown`:** Type-safe counterpart of `any`. Accepts any value, but forces type checking/narrowing before performing any operation on it.
* **`never`:** Represents values that **never occur**. Returned by functions that throw exceptions or enter infinite loops, or exhaustive type checking in switch statements.

**অনুবাদ (Bangla Translation):**
* **`any`:** টাইপ চেকিং বন্ধ করে দেয় (নিরাপদ নয়)।
* **`unknown`:** যেকোনো মান গ্রহণ করে, কিন্তু ব্যবহারের আগে টাইপ নিশ্চিত (Type Check) করতে বাধ্য করে (নিরাপদ)।
* **`never`:** যা কখনো ঘটবে না (যেমন যে ফাংশন থেকে সবসময় এরর থ্রো করা হয়)।

---

### **Q3: What are Generics in TypeScript and how do Constraints work? / TypeScript-এ Generics কী এবং Constraints কীভাবে কাজ করে?**

**Answer (English):**
Generics allow creating reusable components/functions that work over a variety of types rather than a single one:
```typescript
function getFirstElement<T>(arr: T[]): T {
  return arr[0];
}
// Generic Constraint (T must have length property)
function logLength<T extends { length: number }>(item: T): void {
  console.log(item.length);
}
```
Generics capture type safety dynamically at invocation time.

**অনুবাদ (Bangla Translation):**
Generics হলো একটি মেকানিজম যার মাধ্যমে টাইপ ফিক্সড না করে যেকোনো টাইপের জন্য পুনর্ব্যবহারযোগ্য ফাংশন বা ক্লাস তৈরি করা যায় (`<T>`)। `extends` দিয়ে জেনারেক্সের টাইপ সীমাবদ্ধ (Constraint) করা যায়।

---

### **Q4: Explain common Built-in Utility Types (`Partial`, `Required`, `Readonly`, `Pick`, `Omit`, `Record`). / TypeScript-এর প্রধান Utility Types গুলো ব্যাখ্যা করুন।**

**Answer (English):**
* `Partial<T>`: Makes all properties optional.
* `Required<T>`: Makes all properties required.
* `Readonly<T>`: Makes all properties immutable.
* `Pick<T, K>`: Constructs a type by picking specific keys `K` from `T`.
* `Omit<T, K>`: Constructs a type by removing keys `K` from `T`.
* `Record<K, T>`: Constructs an object type with key type `K` and value type `T`.

**অনুবাদ (Bangla Translation):**
* `Partial<T>`: সব ফিল্ড ঐচ্ছিক (Optional) বানায়।
* `Required<T>`: সব ফিল্ড বাধ্যতামূলক বানাায়।
* `Readonly<T>`: ফিল্ডের মান পরিবর্তন বন্ধ করে।
* `Pick<T, K>`: নির্দিষ্ট কিছু ফিল্ড বেছে নেয়।
* `Omit<T, K>`: নির্দিষ্ট কিছু ফিল্ড বাদ দেয়।
* `Record<K, T>`: Key-Value অবজেক্টের টাইপ ডিফাইন করে।

---

### **Q5: What is Type Narrowing and how do Type Guards work? / Type Narrowing এবং Type Guards কীভাবে কাজ করে?**

**Answer (English):**
Type Narrowing reduces a broader type to a more specific type using conditional checks:
1. `typeof` checks (primitives).
2. `instanceof` checks (classes).
3. `in` operator (property presence).
4. **Custom Type Predicates (`is`):**
   ```typescript
   function isUser(obj: any): obj is User {
     return typeof obj.name === 'string';
   }
   ```

**অনুবাদ (Bangla Translation):**
Type Narrowing হলো কোনো বিস্তৃত টাইপকে কন্ডিশনাল চেকের মাধ্যমে নির্দিষ্ট টাইপে রূপান্তর করা। `is` কিওয়ার্ড দিয়ে কাস্টম টাইপ গার্ড ফাংশন লেখা যায়।

---

### **Q6: What are essential `tsconfig.json` compiler flags for production code safety? / প্রোডাকশন কোডের নিরাপত্তার জন্য `tsconfig.json`-এর জরুরি ফ্লাগগুলো কী কী?**

**Answer (English):**
* `"strict": true`: Enables all strict type-checking options.
* `"noImplicitAny": true`: Throws error on expressions with implied `any` type.
* `"strictNullChecks": true`: Ensures `null` and `undefined` are handled explicitly.
* `"noUnusedLocals": true` & `"noUnusedParameters": true`: Prevents dead code accumulation.
* `"exactOptionalPropertyTypes": true`: Prevents setting `undefined` to optional properties unless specified.

**অনুবাদ (Bangla Translation):**
* `"strict": true`: সব টাইপ চেকিং কড়াভাবে অন করা।
* `"strictNullChecks": true`: `null` বা `undefined` এরর আটকানো।
* `"noImplicitAny": true`: অজানা যেকোনো মানকে `any` হতে না দেওয়া।

---

### **Q7: What are `keyof` and `typeof` operators in TypeScript? / TypeScript-এ `keyof` এবং `typeof` অপারেটর কীভাবে কাজ করে?**

**Answer (English):**
* `typeof`: Extracts the TypeScript type from a runtime JavaScript variable/object.
* `keyof`: Takes an object type and produces a string/number union of its keys.
```typescript
const person = { name: "Rohit", age: 25 };
type PersonType = typeof person; // { name: string, age: number }
type PersonKeys = keyof PersonType; // "name" | "age"
```

**অনুবাদ (Bangla Translation):**
* `typeof`: সাধারণ অবজেক্ট থেকে রিয়্যাল-টাইম টাইপ বের করে আনে।
* `keyof`: অবজেক্টের সবগুলোর Key নিয়ে ইউনিয়ন টাইপ তৈরি করে।

---

### **Q8: What are Conditional Types and how does the `infer` keyword work? / Conditional Types এবং `infer` কিওয়ার্ডের কাজ কী?**

**Answer (English):**
Conditional types select one of two types based on a condition (`T extends U ? X : Y`).
The `infer` keyword allows introducing a type variable to be inferred within the true branch of a conditional type:
```typescript
type ReturnTypeCustom<T> = T extends (...args: any[]) => infer R ? R : any;
```

**অনুবাদ (Bangla Translation):**
Conditional Types কন্ডিশনের ওপর ভিত্তি করে টাইপ পছন্দ করে (`T extends U ? X : Y`)। `infer` কিওয়ার্ড টাইপ থেকে ভেতরের গোপন টাইপ (যেমন ফাংশনের রিটার্ন টাইপ) অনুমিত করতে ব্যবহৃত হয়।

---

### **Q9: Enums versus `as const` Objects: Which should you use in TypeScript? / TypeScript-এ Enums নাকি `as const` অবজেক্ট ব্যবহার করা ভালো?**

**Answer (English):**
* **Numeric/String Enums:** Generate actual JavaScript code objects at compile time. Can increase bundle size and have subtle behavior quirks.
* **`as const` Objects (Const Assertions):** Immutable JavaScript objects whose keys and values are inferred as literal types:
  ```typescript
  const ROLES = { ADMIN: "ADMIN", USER: "USER" } as const;
  type Role = typeof ROLES[keyof typeof ROLES]; // "ADMIN" | "USER"
  ```
* *Best Practice:* Prefer `as const` objects for zero-overhead, clean JS compilation and tree-shaking support.

**অনুবাদ (Bangla Translation):**
Enums জাভাস্ক্রিপ্ট ফাইলে অতিরিক্ত কোড তৈরি করে। কিন্তু `as const` দিয়ে অবজেক্ট তৈরি করলে কোনো অতিরিক্ত কোড জেনারেট হয় না এবং সেরা পারফরম্যান্স পাওয়া যায়।

---

### **Q10: What is Declaration Merging and how do you extend ambient module declarations (`.d.ts`)? / Declaration Merging কী এবং কীভাবে টাইপ এক্সটেন্ড করবেন?**

**Answer (English):**
Declaration Merging allows multiple declarations with the same name to automatically merge into a single definition.
Used to extend third-party library types (e.g., adding a `user` object to Express Request):
```typescript
// express.d.ts
declare global {
  namespace Express {
    interface Request {
      user?: { id: string; role: string };
    }
  }
}
```

**অনুবাদ (Bangla Translation):**
Declaration Merging হলো একই নামের একাধিক ইন্টারফেসকে রিয়্যাক্ট/এক্সপ্রেস টাইপের সাথে যুক্ত করা। যেমন Express Request-এর ভেতরে কাস্টম `user` অবজেক্ট যুক্ত করার পদ্ধতি।

---

## 🔴 4. Top 5 Redis Questions

### **Q1: What is Redis and why is it extremely fast? / Redis কী এবং এটি কেন এত দ্রুতগতির?**

**Answer (English):**
Redis (Remote Dictionary Server) is an open-source, in-memory key-value data structure store used as a database, cache, streaming engine, and message broker.
* **Why it's fast:**
  1. **In-Memory Operations:** All data resides in RAM (eliminating disk I/O bottlenecks).
  2. **Single-Threaded Event Loop:** Uses an efficient single-threaded event loop architecture (I/O multiplexing), eliminating context switching overhead and locks.
  3. **Efficient C Data Structures:** Built natively in C using optimized data structures (ZipLists, SkipLists).

**অনুবাদ (Bangla Translation):**
Redis হলো মেমোরিতে (RAM) চলা ফাস্ট কী-ভ্যালু ডাটাবেজ। এটি দ্রুত কারণ: ১. সব ডাটা সরাসরি র্যামে থাকে, ২. সিঙ্গেল-থ্রেডেড ইভেন্ট লুপের কারণে কনটেক্সট সুইচিং লাগে না, এবং ৩. সি (C) ভাষায় অপ্টিমাইজড ডাটা স্ট্রাকচার দিয়ে তৈরি।

---

### **Q2: Explain the core Redis Data Structures and their use cases. / Redis-এর প্রধান ডাটা স্ট্রাকচার ও তাদের ব্যবহার ব্যাখ্যা করুন।**

**Answer (English):**
* **Strings:** Simple text or binary data (Max 512MB). Used for caching, counters (`INCR`).
* **Hashes:** Key-value pairs inside a key. Best for storing objects (e.g., user profile).
* **Lists:** Linked list of strings. Used for message queues, recent activity feeds.
* **Sets:** Unordered unique strings. Used for tracking tags, online users.
* **Sorted Sets (ZSET):** Unique strings ordered by a float score. Best for leaderboards and rate-limiting sliders.

**অনুবাদ (Bangla Translation):**
* **Strings:** সাধারণ ক্যাশিং বা কাউন্টারের জন্য।
* **Hashes:** অবজেক্ট জমা রাখার জন্য।
* **Lists:** ব্যাকগ্রাউন্ড কিউ বা মেসেজের জন্য।
* **Sets:** ইউনিক ডাটা বা অনলাইন ইউজার লিস্ট ট্র্যাকিং।
* **Sorted Sets (ZSET):** পয়েন্ট বা স্কোর ধরে গেম লিডারবোর্ড বানানোর জন্য।

---

### **Q3: What are Redis Persistence Mechanisms (RDB vs AOF)? / Redis Persistence মেকানিজম (RDB এবং AOF) কী?**

**Answer (English):**
Since Redis stores data in RAM, persistence mechanisms save data to disk to survive crashes:
* **RDB (Redis Database Backup):** Takes point-in-time snapshots of dataset at specified intervals. Compact, fast to restore, but may lose data between snapshots.
* **AOF (Append-Only File):** Logs every write operation received by the server. Highly durable, but generates larger files and slower recovery.
* *Best Practice:* Use hybrid persistence (RDB + AOF combined).

**অনুবাদ (Bangla Translation):**
র্যামের ডাটা যেন হারিয়ে না যায় সে জন্য ডিস্কে সেভ করার ২টি উপায়:
* **RDB:** নির্দিষ্ট সময় পর পর ডাটাবেজের ছবি (Snapshot) সেভ করে।
* **AOF:** প্রতি লাইনের কোডের পরিবর্তন ব্যাকগ্রাউন্ডে লিখে সেভ রাখে (অত্যন্ত নিরাপদ)।

---

### **Q4: Explain common Caching Strategies and Eviction Policies in Redis. / Redis ক্যাশিং স্ট্র্যাটেজি এবং Eviction Policies ব্যাখ্যা করুন।**

**Answer (English):**
* **Cache-Aside Pattern:** App checks Redis first. If cache miss, fetches from DB, saves to Redis, and returns data.
* **Eviction Policies (When RAM is full):**
  * `volatile-lru`: Removes Least Recently Used keys with TTL expiration.
  * `allkeys-lru`: Removes Least Recently Used keys across all keys.
  * `noeviction`: Returns memory error on new write attempts.

**অনুবাদ (Bangla Translation):**
* **Cache-Aside Pattern:** আগে Redis-এ ডাটা খোঁজা হয়, না পেলে মূল ডাটাবেজ থেকে এনে Redis-এ সেভ করে ইউজারকে দেওয়া হয়।
* **LRU (Least Recently Used):** র্যাম ভরে গেলে সবচেয়ে পুরোনো অব্যবহৃত ডাটা মুছে নতুন ডাটা জায়গা দেয়।

---

### **Q5: How do you implement Distributed Locking using Redis (Redlock)? / Redis দিয়ে ডিস্ট্রিবিউটেড লকিং (Redlock) কীভাবে কাজ করে?**

**Answer (English):**
To prevent race conditions across multiple server instances (e.g., ticket booking):
```bash
SET lock_key unique_token NX PX 30000
```
* `NX`: Only set the key if it does not already exist.
* `PX 30000`: Expire lock automatically in 30 seconds (prevents deadlocks).
* To release: Execute a Lua script that verifies `unique_token` matches before deleting the key.

**অনুবাদ (Bangla Translation):**
একাধিক সার্ভারে একই কাজ একসাথে হওয়া (Race condition) ঠেকাতে `SETNX` দিয়ে লক বসানো হয়। কাজ শেষ হলে গোপন টোকেন মেলালেই কেবল লক খোলা (Release) যায়।

---

## 🐳 5. Top 5 Docker Questions

### **Q1: What is Containerization versus Virtualization (Docker Containers vs Virtual Machines)? / Containerization এবং Virtualization এর মধ্যে পার্থক্য কী?**

**Answer (English):**
* **Virtual Machines (VMs):** Runs a full guest Operating System (OS) on top of a Hypervisor. Heavy RAM usage, slow boot time (minutes), large storage footprint (GBs).
* **Docker Containers:** Share the host OS kernel and package only application code and dependencies. Ultra-lightweight, boots in milliseconds, minimal RAM/disk footprint.

**অনুবাদ (Bangla Translation):**
* **VM:** পুরো নতুন অপারেটিং সিস্টেম (Guest OS) চালায়। মেমোরি খরচ বেশি এবং চালু হতে সময় নেয়।
* **Docker Container:** মেন অপারেটিং সিস্টেমের কার্নেল শেয়ার করে চলে। হালকা, খুব দ্রুত চালু হয় এবং কম র্যাম নেয়।

---

### **Q2: What is the difference between a Dockerfile, Docker Image, and Docker Container? / Dockerfile, Docker Image এবং Docker Container-এর মধ্যে পার্থক্য কী?**

**Answer (English):**
* **Dockerfile:** A plain-text script containing instructions to build a Docker image.
* **Docker Image:** An immutable, read-only template with executable code, runtime, and libraries.
* **Docker Container:** A running, isolated instance of a Docker image.

**অনুবাদ (Bangla Translation):**
* **Dockerfile:** রেসিপি বা নির্দেশনার টেক্সট ফাইল।
* **Docker Image:** পড়া যায় এমন স্ট্যাটিক টেমপ্লেট (ব্লুপ্রিন্ট)।
* **Docker Container:** ইমেজ থেকে চলা জীবন্ত প্রসেস।

---

### **Q3: What are Multi-Stage Builds in Docker and why are they critical for production? / Docker Multi-Stage Builds কী এবং প্রোডাকশনে এটি কেন জরুরি?**

**Answer (English):**
Multi-Stage builds allow using multiple `FROM` instructions in a single `Dockerfile` to separate the build environment from the runtime environment.
```dockerfile
# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY . .
RUN npm ci && npm run build

# Stage 2: Production Runtime
FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./
RUN npm ci --only=production
CMD ["node", "dist/main.js"]
```
* **Benefit:** Shrinks production image size from ~1GB to ~100MB by leaving behind build tools, compilers, and devDependencies.

**অনুবাদ (Bangla Translation):**
Multi-Stage Build দিয়ে বিল্ড করার মেটেরিয়াল (যেমন সাইজ ১GB) বাদ দিয়ে প্রোডাকশনের জন্য শুধু প্রসেস হওয়া হালকা ফাইলটি (সাইজ ১০০MB) নেওয়া হয়, যা সার্ভারের গতি বাড়ায়।

---

### **Q4: Explain Docker Storage: Volumes versus Bind Mounts versus `tmpfs`. / Docker Storage: Volumes, Bind Mounts এবং `tmpfs` ব্যাখ্যা করুন।**

**Answer (English):**
* **Volumes:** Managed directly by Docker inside host file system (`/var/lib/docker/volumes/`). Best for persistent database data.
* **Bind Mounts:** Maps a specific directory on host machine to container directory. Best for local development live-reloading.
* **`tmpfs` Mounts:** Stores data strictly in host system RAM memory (never written to disk). Best for sensitive temporary data.

**অনুবাদ (Bangla Translation):**
* **Volumes:** ডাটাবেজ ডাটা চিরতরে সেভ রাখতে।
* **Bind Mounts:** লোকাল কোড লাইভ চেঞ্জ দেখার জন্য।
* **`tmpfs`:** র্যামে সাময়িক গোপন তথ্য রাখার জন্য।

---

### **Q5: What is Docker Compose and how does Container Networking work? / Docker Compose কী এবং কন্টেইনার নেটওয়ার্কিং কীভাবে কাজ করে?**

**Answer (English):**
* **Docker Compose:** A tool for defining and running multi-container applications using a `docker-compose.yml` file.
* **Networking:** Containers on the same Docker bridge network communicate with each other using their service names as DNS hostnames (e.g., `redis:6379` or `mongodb:27017`).

**অনুবাদ (Bangla Translation):**
Docker Compose দিয়ে একাধিক সার্ভিস (যেমন Node API + Redis + MongoDB) একসাথে চালানো যায়। সার্ভিস নাম (যেমন `redis:6379`) ধরে এরা একে অপরের সাথে কথা বলতে পারে।

---

## 🐂 6. Top 5 Bull Queue Questions

### **Q1: What is Bull Queue and why is it essential in Node.js architectures? / Bull Queue কী এবং Node.js আর্কিটেকচারে এটি কেন প্রয়োজন?**

**Answer (English):**
Bull Queue is a Redis-backed job queue for Node.js. It offloads heavy asynchronous tasks (PDF generation, email dispatch, telemetry calculations) out of the main Node.js Event Loop, preventing API lag and HTTP timeouts.

**অনুবাদ (Bangla Translation):**
Bull Queue হলো Redis ভিত্তিক ব্যাকগ্রাউন্ড টাস্ক ম্যানেজার। এটি ভারী কাজ এপিআই থেকে সরিয়ে ব্যাকগ্রাউন্ডে করায়, ফলে এপিআই দ্রুত ফায়ার হয়।

---

### **Q2: Explain the Core Architecture of Bull Queue (Redis, Producer, Queue, Consumer/Worker). / Bull Queue-এর মূল আর্কিটেকচার ব্যাখ্যা করুন।**

**Answer (English):**
* **Producer:** Express API adding jobs (`queue.add(data)`).
* **Redis:** Stores job states and metadata atomically.
* **Queue:** The pipeline buffer.
* **Consumer/Worker:** Separate background process executing jobs (`queue.process(handler)`).

**অনুবাদ (Bangla Translation):**
Express এপিআই কাজ জমা দেয় (Producer), Redis ডাটা সেভ রাখে, এবং আলাদা ব্যাকগ্রাউন্ড প্রোগ্রাম কাজগুলো সম্পূর্ণ করে (Worker)।

---

### **Q3: How do you handle Job Failures, Exponential Backoff Retries, and Dead Letter Queues (DLQ)? / কাজ ফেল করলে Exponential Backoff ও Dead Letter Queue দিয়ে কীভাবে সামলাবেন?**

**Answer (English):**
```javascript
queue.add(data, {
  attempts: 5,
  backoff: { type: 'exponential', delay: 1000 }
});
```
If a job fails all attempts, listen to `failed` event and push the payload to a Dead Letter Queue (DLQ) for manual inspection and alerting.

**অনুবাদ (Bangla Translation):**
কাজ ফেল করলে ১s, ২s, ৪s পর পর অটো রি-ট্রাই করবে। বারবার ফেল করলে ডাটা হারিয়ে না গিয়ে পর্যবেক্ষণ করার জন্য Dead Letter Queue-তে জমা হবে।

---

### **Q4: How do Concurrency, Rate Limiting, and Delayed Jobs work in Bull Queue? / Bull Queue-তে Concurrency, Rate Limiting এবং Delayed Jobs কীভাবে কাজ করে?**

**Answer (English):**
* **Concurrency:** `queue.process(5, handler)` processes 5 jobs concurrently.
* **Rate Limiting:** `limiter: { max: 100, duration: 60000 }` limits to 100 jobs/minute.
* **Delayed Jobs:** `{ delay: 600000 }` holds the job for 10 minutes before pushing to waiting state.

**অনুবাদ (Bangla Translation):**
* **Concurrency:** একসাথে একাধিক কাজ করা।
* **Rate Limiting:** মিনিটে ১০০টির বেশি কাজ আটকানো।
* **Delayed Jobs:** নির্দিষ্ট সময় পর কাজ শুরু করা।

---

### **Q5: What are the differences between Bull (v4) and BullMQ (v5+)? / Bull (v4) এবং BullMQ (v5+) এর মধ্যে পার্থক্য কী?**

**Answer (English):**
BullMQ is a TypeScript-native rewrite utilizing modern Redis Streams instead of Lua scripts, featuring native Parent-Child job dependencies, improved stream performance, and cleaner separation of Queue/Worker instances.

**অনুবাদ (Bangla Translation):**
BullMQ হলো টাইপস্ক্রিপ্টে তৈরি নতুন ভার্সন, যা দ্রুততর Redis Streams ব্যবহার করে এবং জটিল পাইপলাইন সাপোর্ট করে।

---

## 🃏 7. Top 5 Jest Questions

### **Q1: What is the difference between Unit Testing, Integration Testing, and End-to-End (E2E) Testing in Jest? / Jest-এ Unit, Integration এবং E2E টেস্টিং-এর মধ্যে পার্থক্য কী?**

**Answer (English):**
* **Unit Testing:** Tests an isolated function/component in complete isolation (mocking all external dependencies). Fast.
* **Integration Testing:** Tests how multiple modules/components work together (e.g., API endpoint + DB).
* **E2E Testing:** Tests full application flow from user perspective (browser simulation).

**অনুবাদ (Bangla Translation):**
* **Unit:** ছোট একটি ফাংশন একা টেস্ট করা।
* **Integration:** একাধিক মডিউল একসাথে টেস্ট করা।
* **E2E:** পুরো অ্যাপটি ইউজারের মতো টেস্ট করা।

---

### **Q2: What is the difference between `jest.fn()`, `jest.spyOn()`, and `jest.mock()`? / `jest.fn()`, `jest.spyOn()`, এবং `jest.mock()` এর মধ্যে পার্থক্য কী?**

**Answer (English):**
* `jest.fn()`: Creates a dummy mock function.
* `jest.spyOn()`: Tracks calls to an existing object method while keeping its original implementation intact (or mocking it).
* `jest.mock()`: Mocks an entire imported module/package.

**অনুবাদ (Bangla Translation):**
* `jest.fn()`: ভুয়া ফাংশন বানায়।
* `jest.spyOn()`: আসল মেথড পর্যবেক্ষণ করে।
* `jest.mock()`: পুরো থার্ড-পার্টি লাইব্রেরি মক করে।

---

### **Q3: How do you test Asynchronous Code in Jest? / Jest-এ অ্যাসিনক্রোনাস কোড কীভাবে টেস্ট করবেন?**

**Answer (English):**
```javascript
test('fetches user data', async () => {
  const data = await fetchUser(1);
  expect(data.name).toBe('Rohit');
});

// Testing promise rejection
test('fails with error', async () => {
  await expect(fetchUser(-1)).rejects.toThrow('User not found');
});
```

**অনুবাদ (Bangla Translation):**
`async/await` ব্যবহার করে প্রমিজের ডাটা রেজাল্ট বা এরর (`rejects.toThrow()`) টেস্ট করা হয়।

---

### **Q4: Explain Setup and Teardown lifecycle hooks in Jest (`beforeEach`, `afterEach`, `beforeAll`, `afterAll`). / Jest-এর Setup ও Teardown হুকস ব্যাখ্যা করুন।**

**Answer (English):**
* `beforeAll`: Runs ONCE before any tests in the file run (e.g., connect to test DB).
* `beforeEach`: Runs before EVERY test (e.g., seed test data).
* `afterEach`: Runs after EVERY test (e.g., clear mocks).
* `afterAll`: Runs ONCE after all tests complete (e.g., disconnect DB).

**অনুবাদ (Bangla Translation):**
* `beforeAll`: ফাইল টেস্টের শুরুতে ১ বার চলে (ডাটাবেজ কানেক্ট করতে)।
* `beforeEach`: প্রতিটি টেস্টের আগে চলে (মক রিসেট করতে)।
* `afterAll`: সব টেস্ট শেষে ১ বার চলে (ডাটাবেজ ডিসকানেক্ট করতে)।

---

### **Q5: What are Code Coverage Metrics and Snapshot Testing in Jest? / Code Coverage Metrics এবং Snapshot Testing কী?**

**Answer (English):**
* **Code Coverage:** Reports percentage of Statements, Branches (`if/else`), Functions, and Lines executed by tests.
* **Snapshot Testing:** Compares rendered component output against a saved reference snapshot file to detect unexpected UI changes.

**অনুবাদ (Bangla Translation):**
* **Code Coverage:** টেস্ট কোডের কতটা শতাংশ কভার করেছে তার রিপোর্ট।
* **Snapshot:** ইউআই ডিজাইনে না জানিয়ে পরিবর্তন হয়েছে কিনা তা ফাইলের সাথে মিলিয়ে ধরা।

---

## 🚀 8. Top 5 CI/CD & Deployment Questions

### **Q1: What is CI/CD (Continuous Integration & Continuous Deployment/Delivery)? / CI/CD বলতে কী বোঝায়?**

**Answer (English):**
* **Continuous Integration (CI):** Automatically building, linting, and running tests on every code push/PR to merge code safely.
* **Continuous Delivery/Deployment (CD):** Automatically deploying validated code changes to staging or production servers without manual intervention.

**অনুবাদ (Bangla Translation):**
* **CI:** কোড পুশ করলেই অটোমেটিক বিল্ড ও টেস্ট করা।
* **CD:** টেস্ট পাস হলে অটোমেটিক লাইভ সার্ভারে প্রজেক্ট ডিপ্লয় করা।

---

### **Q2: How do you structure a GitHub Actions Workflow for a Full-Stack MERN Application? / Full-Stack প্রজেক্টের জন্য GitHub Actions Workflow কীভাবে সাজাবেন?**

**Answer (English):**
```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [ main ]
jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: 20
      - run: npm ci
      - run: npm run lint
      - run: npm test
      - run: npm run build
  deploy:
    needs: build-and-test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Server via SSH
        uses: appleboy/ssh-action@master
        with:
          host: ${{ secrets.SERVER_HOST }}
          username: ${{ secrets.SERVER_USER }}
          key: ${{ secrets.SSH_PRIVATE_KEY }}
          script: |
            cd /var/www/myapp
            git pull origin main
            npm ci
            npm run build
            pm2 reload all
```

**অনুবাদ (Bangla Translation):**
GitHub Actions-এ `.github/workflows/deploy.yml` দিয়ে ফাইল বানিয়ে অটো বিল্ড, টেস্ট, SSH দিয়ে সার্ভারে গিট পুল এবং PM2 রিলোড করানো হয়।

---

### **Q3: How do you securely manage Secrets and Environment Variables in CI/CD? / CI/CD-তে সিক্রেট এবং Environment Variables কীভাবে নিরাপদে রাখবেন?**

**Answer (English):**
* Never commit secrets (`.env`) to Git repositories.
* Inject secrets via GitHub Repository Secrets (`${{ secrets.API_KEY }}`).
* In production, use AWS Secrets Manager, Vault, or Encrypted Docker secrets.

**অনুবাদ (Bangla Translation):**
সিক্রেট ফাইল গিটহাবে পুশ না করে GitHub Repository Secrets এ সেভ রাখতে হয় এবং প্রোডাকশনে AWS Secrets Manager ব্যবহার করতে হয়।

---

### **Q4: Explain Deployment Strategies: Blue-Green Deployment vs Canary Release vs Rolling Update. / Blue-Green, Canary এবং Rolling Update ডিপ্লয়মেন্ট কৌশলগুলো ব্যাখ্যা করুন।**

**Answer (English):**
* **Blue-Green:** Maintains two identical production environments (Blue=Live, Green=New). Router switches 100% traffic instantly to Green after validation. Zero downtime.
* **Canary Release:** Routes 5% of traffic to the new version first. If no errors occur, slowly ramps to 100%.
* **Rolling Update:** Gradually replaces instances one by one until all instances run the new version.

**অনুবাদ (Bangla Translation):**
* **Blue-Green:** ২টি সার্ভার রাখা। একটিতে টেস্ট ঠিক থাকলে রাউটার মুহূর্তের মধ্যে নতুন সার্ভারে সব ইউজার ডাইভার্ট করে দেয়।
* **Canary:** প্রথমে ৫% ইউজারের কাছে নতুন ভার্সন পাঠানো, সমস্যা না থাকলে ধীরে ধীরে ১০০% করা।
* **Rolling Update:** একটি একটি করে সার্ভার প্রসেস নতুন করে রিলিজ দেওয়া।

---

### **Q5: How do you achieve Zero-Downtime Deployments in Node.js using PM2 or Nginx? / Node.js প্রজেক্টে PM2 বা Nginx দিয়ে Zero-Downtime Deployment কীভাবে অর্জন করবেন?**

**Answer (English):**
Use **PM2 Reload** in Cluster Mode:
```bash
pm2 reload all
```
Unlike `pm2 restart` (which shuts down all processes simultaneously), `pm2 reload` restarts worker processes **one by one in sequence**, keeping at least one process active to serve incoming requests while others boot up.

**অনুবাদ (Bangla Translation):**
`pm2 restart` দিলে সব সার্ভার একসাথে বন্ধ হয়। কিন্তু `pm2 reload all` দিলে একটি একটি করে সার্ভার প্রসেস রিস্টার্ট হয়, ফলে সার্ভার ১ সেকেন্ডের জন্যও বন্ধ হয় না (Zero Downtime)।
