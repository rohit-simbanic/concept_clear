# React Mastery: Part 7 - React 19, Server Components & Modern Actions

স্বাগতম! এই গাইডে আমরা আধুনিক React 19-এর যুগান্তকারী পরিবর্তনগুলো অত্যন্ত গভীরভাবে শিখব। আমরা আলোচনা করব **Server vs Client Components**, **Action API and useActionState**, **useFormStatus**, **useOptimistic**, এবং নতুন **use API hook** সম্পর্কে।

---

## ১. Server vs Client Components

### ১. Simple definition (বাংলায়)
* **Server Components (RSC):** এটি এমন এক ধরনের React কম্পোনেন্ট যা শুধুমাত্র সার্ভার সাইডে রান বা রেন্ডার হয়। ব্রাউজারে এর কোনো জাভাস্ক্রিপ্ট কোড পাঠানো হয় না।
* **Client Components:** এটি ট্র্যাডিশনাল React কম্পোনেন্ট যা ব্রাউজারে রান বা হাইড্রেট (hydrate) হয়। এটি ব্রাউজারের ইন্টারঅ্যাকশন (যেমন: বাটন ক্লিক, উইন্ডো ইভেন্ট, হুকস) হ্যান্ডেল করতে পারে। একে ফাইলের শুরুতে `'use client'` লিখে চিহ্নিত করতে হয়।

### ২. Why this concept exists
প্রথাগত Single Page Applications (SPA)-এ সমস্ত রিঅ্যাক্ট কম্পোনেন্ট জাভাস্ক্রিপ্ট ফাইল হিসেবে ব্রাউজারে ডাউনলোড হতো। এর ফলে মেগা-বাইট সাইজের জাভাস্ক্রিপ্ট লোড হওয়া, স্লো প্রথম রেন্ডারিং এবং সার্চ ইঞ্জিন অপ্টিমাইজেশন (SEO)-এর মারাত্মক ক্ষতি হতো। সার্ভার কম্পোনেন্টের ফলে আমরা ডাটাবেস কোয়েরি বা ফাইল রিড সরাসরি সার্ভারেই করে প্লেইন HTML ব্রাউজারে পাঠাতে পারি।

### ৩. What problem it solves
এটি জাভাস্ক্রিপ্ট বান্ডেল সাইজ (Bundle Size) বহুগুণ কমিয়ে দেয় এবং সরাসরি সার্ভার সাইড সিকিউরিটি কি বা ডাটাবেস কানেকশন ব্যবহার করার সুযোগ দেয়, যা সিকিউরিটি ও স্পিড বাড়ায়।

### ৪. Real-life analogy
আপনি একটি আসবাবপত্রের দোকান থেকে একটি খাট কিনতে চান। 
* **Client Component (SPA):** দোকানদার আপনাকে কাঠের টুকরো, পেরেক ও হাতুড়ি আপনার বাড়িতে পাঠিয়ে দিল। আপনি নিজে বাড়িতে বসে অনেক সময় নিয়ে খাটটি ফিট করলেন। (এটি বাড়ির জন্য ভারী কাজ এবং বেশি জাভাস্ক্রিপ্ট রান করার মতো)।
* **Server Component:** দোকানদার তার কারখানায় (Server) সম্পূর্ণ খাটটি ফিট করে আপনার বাড়িতে রেডিমেড পাঠিয়ে দিল। আপনার আর কোনো বাড়তি খাটুনি করতে হলো না।

### ৫. How React works internally regarding this concept
সার্ভার কম্পোনেন্ট রান করার সময় React সার্ভারে কোডটি এক্সিকিউট করে এবং একটি বিশেষ JSON-এর মতো স্ট্রাকচার তৈরি করে ব্রাউজারে পাঠায় (যাকে RSC Payload বলে)। ব্রাউজার এই পেলোড রিড করে রিয়েল DOM জেনারেট করে। সার্ভার কম্পোনেন্টে কোনো `useState` বা `useEffect` থাকতে পারে না কারণ সার্ভারে ব্রাউজারের কোনো ইন্টারঅ্যাকশন বা উইন্ডো থাকে না। ক্লায়েন্ট সাইড ইন্টারঅ্যাকশনের জন্য চাইল্ড নোড হিসেবে Client Component যুক্ত করা হয়।

### ৬. Basic example
**Server Component (Default in Next.js / React 19):**
```jsx
// ProductList.jsx (Runs ONLY on server)
import React from 'react';

// Directly importing server database helpers (safe from client eye)
import { db } from '@/lib/db'; 

export default async function ProductList() {
  const products = await db.query('SELECT * FROM products'); // Direct DB call!

  return (
    <div>
      <h2>Products in Stock</h2>
      <ul>
        {products.map(p => (
          <li key={p.id}>{p.name} - ${p.price}</li>
        ))}
      </ul>
    </div>
  );
}
```

**Client Component:**
```jsx
// ToggleButton.jsx (Runs on client)
'use client'; // This directive must be at the very top

import React, { useState } from 'react';

export default function ToggleButton() {
  const [active, setActive] = useState(false);

  return (
    <button onClick={() => setActive(!active)}>
      {active ? 'ON' : 'OFF'}
    </button>
  );
}
```

### ৭. Step-by-step explanation of the code
* `ProductList` হলো একটি সার্ভার কম্পোনেন্ট, তাই এটি `async` ফাংশন হিসেবে সরাসরি সার্ভার ডাটাবেস থেকে প্রমিজ `await` করে ডেটা আনতে পারছে।
* `ToggleButton` ইন্টারঅ্যাক্টিভ বাটন এবং স্টেট হোল্ড করে, তাই ফাইলের শুরুতে `'use client'` লিখে একে ক্লায়েন্ট কম্পোনেন্ট ঘোষণা করা হয়েছে।

### ৮. Another real-world example (Composition Pattern)
```jsx
// Parent (Server Component)
import Sidebar from './Sidebar';
import InteractiveChat from './InteractiveChat'; // Client Component

export default function HomePage() {
  return (
    <div className="layout">
      {/* Server component handles static sidebar */}
      <Sidebar />
      
      {/* Client component handles real-time messaging */}
      <InteractiveChat />
    </div>
  );
}
```

### ৯. Common mistakes beginners make
* **Server Component-এ useState ব্যবহার:** সার্ভার কম্পোনেন্টে `useState` বা `useEffect` লিখলে রিঅ্যাক্ট লাল এরর দিয়ে জানাবে যে এগুলো ক্লায়েন্ট কম্পোনেন্ট ছাড়া ব্যবহার করা সম্ভব নয়।
* **ক্লায়েন্ট ডিরেক্টিভ ভুলে যাওয়া:** বাটনের ক্লিকার লজিক বা হুকস ব্যবহার করার ফাইলে `'use client'` না লিখলে সেটি রান করবে না।

### ১০. Interview questions related to this topic
1. **Server এবং Client কম্পোনেন্টের মূল পার্থক্য কী?**
   * উত্তর: Server component রান করে সার্ভারে, এটি ডাটাবেস সরাসরি অ্যাক্সেস করতে পারে এবং কোনো জাভাস্ক্রিপ্ট ব্রাউজারে পাঠায় না। Client component ব্রাউজারে হাইড্রেট হয় এবং এটি ইভেন্ট লিসেনার ও রিঅ্যাক্ট হুকস ব্যবহার করতে পারে।
2. **সার্ভার কম্পোনেন্টে কি ক্লায়েন্ট কম্পোনেন্ট ইম্পোর্ট করা যায়?**
   * উত্তর: হ্যাঁ, সার্ভার কম্পোনেন্ট তার চাইল্ড বা লিফ নোড হিসেবে ক্লায়েন্ট কম্পোনেন্ট ইম্পোর্ট করতে পারে। তবে ক্লায়েন্ট কম্পোনেন্টের ভেতর সরাসরি সার্ভার কম্পোনেন্ট ইম্পোর্ট করা যায় না ( Composition pattern বা children prop ব্যবহার করে করতে হয়)।

### ১১. Best practices
* বাই-ডিফল্ট সব কম্পোনেন্ট সার্ভার কম্পোনেন্ট হিসেবে রাখুন। শুধুমাত্র যেখানে ইন্টারঅ্যাক্টিভিটি (onClick, useState, useEffect, window API) প্রয়োজন, সেখানে `'use client'` ব্যবহার করুন।
* ক্লায়েন্ট বান্ডেল সাইজ কমাতে ডেটা ম্যাপার বা হেল্পারগুলো সার্ভার কম্পোনেন্টেই এক্সিকিউট করে ফেলুন।

### ১২. Performance considerations
সার্ভার কম্পোনেন্ট ব্যবহারের ফলে ক্লায়েন্ট ব্রাউজারে অনেক কম জাভাস্ক্রিপ্ট ডাউনলোড করতে হয়, যা মোবাইল ডিভাইসের ব্যাটারি ও সিপিইউ লোড অনেকাংশে কমিয়ে দেয়।

### ১৩. When NOT to use it
যদি আপনার কোনো ফ্রেস এবং সম্পূর্ণ ডাইনামিক ক্লায়েন্ট সাইড ওয়েব অ্যাপ হয় যা সার্ভার ছাড়াই পুরোপুরি ব্রাউজারে রান করবে (যেমন: লোকাল ড্রয়িং টুল বা অফলাইন অ্যাপ), সেখানে সার্ভার কম্পোনেন্ট দরকার নেই।

### ১৪. Comparison with similar concepts
* **Server Component vs SSR:** SSR (Server Side Rendering) হলো সার্ভারে HTML তৈরি করে ক্লায়েন্টে পাঠানো, কিন্তু ক্লায়েন্টে গিয়ে তা আবার সম্পূর্ণ রিঅ্যাক্ট কোড দিয়ে হাইড্রেট করতে হয়। Server Component-এর কোড ক্লায়েন্টে



























কখনো হাইড্রেট হয় না, এটি রেন্ডার হওয়ার পর চিরকাল সার্ভারেই থেকে যায়।

### ১৫. Summary in simple Bangla
সার্ভার কম্পোনেন্ট রান করে সার্ভারে (ডাটাবেস কোয়েরির জন্য সেরা) আর ক্লায়েন্ট কম্পোনেন্ট রান করে ব্রাউজারে (ইউজার ইন্টারঅ্যাকশন ও বাটনের জন্য সেরা)।

### ১৬. 5 MCQ questions
1. React 19/Next.js-এ বাই-ডিফল্ট সমস্ত কম্পোনেন্ট কী হিসেবে কাজ করে?
   * A) Client Component
   * B) Server Component
   * C) Higher-Order Component
   * D) Virtual Component
   * *উত্তর: B*
2. ক্লায়েন্ট কম্পোনেন্ট ঘোষণা করার জন্য ফাইলের একদম উপরে কী লিখতে হয়?
   * A) `import client from 'react'`
   * B) `'use client'`
   * C) `clientMode: true`
   * D) `<Client>`
   * *উত্তর: B*
3. সার্ভার কম্পোনেন্টে নিচের কোনটি ব্যবহার করা পুরোপুরি অবৈধ?
   * A) async/await
   * B) Database queries
   * C) useState()
   * D) standard HTML tags
   * *উত্তর: C*
4. Server Component-এর কোড ব্রাউজারে ডাউনলোড না হওয়ার সুবিধা কী?
   * A) কোড হ্যাক করা যায় না
   * B) ব্রাউজারের জাভাস্ক্রিপ্ট বান্ডেল সাইজ কমে
   * C) সিএসএস স্পিড বাড়ে
   * D) কোনো সুবিধা নেই
   * *উত্তর: B*
5. RSC Payload বলতে কী বোঝায়?
   * A) রিঅ্যাক্ট সার্ভার সাইড সিকিউরিটি কি
   * B) সার্ভার কম্পোনেন্ট দ্বারা জেনারেট হওয়া বিশেষ ডাটা ফরম্যাট যা ব্রাউজার রিড করে DOM বানায়
   * C) ডাটাবেসের পাসওয়ার্ড
   * D) ব্রাউজার কুকি
   * *উত্তর: B*

### ১৭. 5 Coding exercises
1. একটি সার্ভার কম্পোনেন্ট তৈরি করুন যা একটি মক লোকাল JSON ফাইল থেকে ডাটা পড়ে স্ক্রিনে একটি আর্টিকেল লিস্ট দেখাবে।
2. একটি ক্লায়েন্ট কম্পোনেন্ট তৈরি করুন যা একটি টেক্সট টাইপিং স্ট্যাটাস ট্র্যাকার হিসেবে কাজ করবে।
3. সার্ভার কম্পোনেন্টের ভেতর ক্লায়েন্ট কম্পোনেন্ট ইম্পোর্ট করে একটি ডাইনামিক কার্ট কাউন্টার ও প্রোডাক্ট লিস্টের লেআউট তৈরি করুন।
4. Composition Pattern ব্যবহার করে একটি সার্ভার কম্পোনেন্টকে ক্লায়েন্ট কম্পোনেন্টের `children` হিসেবে রেন্ডার করে দেখান।
5. একটি সার্ভার এপিআই রাউট বা ডিরেক্ট এপিআই ফেচিং সার্ভার কম্পোনেন্ট বানিয়ে ডিক্লেয়ার করুন।
