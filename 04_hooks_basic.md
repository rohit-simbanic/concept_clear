# React Mastery: Part 4 - Basic React Hooks (useEffect, useContext, useRef, useMemo, useCallback)

স্বাগতম! React Hooks হলো ফাংশনাল কম্পোনেন্টের প্রাণ। এই গাইডে আমরা হুকসের নিয়মাবলী এবং অত্যন্ত গুরুত্বপূর্ণ ৫টি বেসিক হুক—`useEffect`, `useContext`, `useRef`, `useMemo`, এবং `useCallback` সম্পর্কে বিস্তারিত ও গভীরভাবে আলোচনা করব।

---

## ১. React Hooks & Rules of Hooks

### ১. Simple definition (বাংলায়)
React Hooks হলো বিশেষ কিছু বিল্ট-ইন ফাংশন যা আপনাকে Class Component না লিখেও Functional Component-এর ভেতরে স্টেট, লাইফসাইকেল মেথড এবং অন্যান্য React ফিচার ব্যবহার করতে সাহায্য করে।

### ২. Why this concept exists
পূর্বে Functional Component-কে বলা হতো "Stateless" কম্পোনেন্ট, কারণ তাদের ভেতর কোনো স্টেট রাখার সুযোগ ছিল না। কোনো স্টেটের প্রয়োজন হলে পুরো কম্পোনেন্টটিকে ক্লাস কম্পোনেন্টে কনভার্ট করতে হতো। ক্লাস কম্পোনেন্টের `this` কিওয়ার্ডের জটিলতা এবং কোড সাইজ বড় হওয়ার সমস্যা দূর করতে React 16.8 সংস্করণে Hooks নিয়ে আসে।

### ৩. What problem it solves
* ক্লাস কম্পোনেন্টে কোড রিইউজ করার জন্য HOC (Higher-Order Components) বা Render Props ব্যবহার করতে হতো যা কোডবেসকে জটিল (Wrapper Hell) করত।
* `this` বাইন্ডিং এবং লাইফসাইকেল মেথডের ছড়াছড়ি কমায়।

### ৪. Real-life analogy
হুকস হলো প্লাগ-অ্যান্ড-প্লে (Plug-and-play) ইলেকট্রনিক ডিভাইসের মতো। আপনার কম্পিউটারে যদি ওয়াইফাই না থাকে, তবে মাদারবোর্ড পরিবর্তন না করে আপনি একটি এক্সটারনাল ওয়াইফাই ডঙ্গেল (Wifi Dongle) ইউএসবি পোর্টে কানেক্ট করে ওয়াইফাই ব্যবহার করতে পারেন। হুকসও তেমনি ফাংশনাল কম্পোনেন্টে এক্সটারনাল ফিচার প্লাগইন করার পথ।

### ৫. How React works internally regarding this concept
React ব্যাকগ্রাউন্ডে প্রতিটি কম্পোনেন্টের জন্য একটি লিঙ্কড লিস্ট (Linked List) তৈরি করে যেখানে হুকসগুলোর ডেটা সংরক্ষিত থাকে। React হুকসের পজিশন বা অর্ডারের ওপর নির্ভর করে ডেটা রিড করে। তাই হুকসের কল অর্ডার সবসময় ফিক্সড হতে হবে।

### **Rules of Hooks (হুকসের দুটি সুনির্দিষ্ট নিয়ম):**
1. **Only Call Hooks at the Top Level:** লুপ, কন্ডিশন (if) বা নেস্টেড ফাংশনের ভেতরে হুক কল করা যাবে না। সবসময় কম্পোনেন্টের শুরুতে হুক কল করতে হবে।
2. **Only Call Hooks from React Functions:** সাধারণ জাভাস্ক্রিপ্ট ফাংশনে হুক কল করা যাবে না। কেবল React Functional Component বা Custom Hook-এর ভেতরেই হুক কল করা যাবে।

### ৬. Basic example
```jsx
import React, { useState } from 'react';

function HooksRuleDemo() {
  // CORRECT: Called at the very top level
  const [name, setName] = useState('Anis');

  // INCORRECT: React will throw an error if done inside an 'if'
  // if (name !== '') {
  //   useEffect(() => { ... });
  // }

  return <div>{name}</div>;
}
```

### ७. Step-by-step explanation of the code
* `useState` হুকটি কম্পোনেন্টের एकदम উপরে কল করা হয়েছে।
* যদি কন্ডিশনের ভেতরে হুক কল করা হতো, তবে প্রতি রেন্ডারে হুকের ইডেক্স বা অর্ডারিং এলোমেলো হয়ে যেত এবং React ভুল স্টেট ভ্যালু প্রোভাইড করত।

### ৮. Another real-world example (Custom Hook Hook Rule Validator)
```jsx
// Custom hook utilizing rules of hooks
import { useState, useEffect } from 'react';

function useWindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => setWidth(window.innerWidth);
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return width;
}
```

### ৯. Common mistakes beginners make
* কন্ডিশনাল ব্লকে হুক রাখা: `if (loading) { useState(...) }` যা রেন্ডার সিকোয়েন্স ব্রেক করে অ্যাপ ক্র্যাশ করায়।
* সাধারণ হেল্পার ফাংশনের ভেতরে হুক কল করা।

### ১০. Interview questions related to this topic
1. **React কেন লুপ বা কন্ডিশনের ভেতর হুক কল করতে নিষেধ করে?**
   * উত্তর: কারণ React ইন্টারনালি হুকগুলোকে একটি নির্দিষ্ট সিকোয়েন্সে (Array/Linked List Index) ট্র্যাক করে। কন্ডিশনাল রেন্ডারিংয়ের কারণে সিকোয়েন্স ব্রেক হলে React ভুল হুকের ডেটা রিটার্ন করবে।
2. **হুকস কি ক্লাস কম্পোনেন্টে ব্যবহার করা যায়?**
   * উত্তর: না, হুকস শুধুমাত্র ফাংশনাল কম্পোনেন্ট এবং কাস্টম হুকের ভেতরেই ব্যবহার করা সম্ভব।

### ১১. Best practices
* আপনার কোড এডিটরে ESLint প্লাগইন `eslint-plugin-react-hooks` ইনস্টল করে রাখুন যাতে হুকসের নিয়ম ভঙ্গ হলে লাইভ ওয়ার্নিং দেখতে পান।
* কাস্টম হুক তৈরির সময় নামের শুরুতে অবশ্যই `use` ব্যবহার করুন (যেমন `useAuth`)।

### ১২. Performance considerations
হুকস ব্যবহারের ফলে কোড সাইজ ছোট হয় এবং ব্রাউজার কম্পাইলেশন দ্রুত হয়, যা ক্লাসের তুলনায় পারফরম্যান্স উন্নত করে।

### ১৩. When NOT to use it
ক্লাস কম্পোনেন্টের ভেতরে হুক ব্যবহার করার চেষ্টা করবেন না।

### ১৪. Comparison with similar concepts
* **Hooks vs HOCs:** HOC কম্পোনেন্টকে র্যাপ করে অতিরিক্ত নোড তৈরি করে, Hooks মেমরিতে সরাসরি স্টেট ও ইফেক্ট ইনজেক্ট করে কোনো র‍্যাপার ছাড়াই।

### ১৫. Summary in simple Bangla
Hooks হলো ফাংশনাল কম্পোনেন্টে এক্সটারনাল ফিচার ব্যবহারের জন্য বিশেষ ফাংশন। হুক কল করার সময় মনে রাখতে হবে তা যেন সবসময় কম্পোনেন্টের শুরুতে থাকে এবং কোনো কন্ডিশনের ভেতর না থাকে।

### ১৬. 5 MCQ questions
1. হুকস ব্যবহারের মূল নিয়ম কয়টি?
   * A) ১টি
   * B) ২টি
   * C) ৩টি
   * D) ৪টি
   * *উত্তর: B*
2. নিচের কোন স্থানে হুক কল করা বৈধ?
   * A) `if` কন্ডিশনের ভেতরে
   * B) `for` লুপের ভেতরে
   * C) React Functional Component-এর একদম উপরে
   * D) একটি সাধারণ JS হেল্পার ফাংশনের ভেতরে
   * *উত্তর: C*
3. হুকস ব্যবহারের সুবিধা কোনটি?
   * A) `this` কিওয়ার্ডের ঝামেলা এড়ানো যায়
   * B) Wrapper hell দূর হয়
   * C) কোড রিইউজেবিলিটি বাড়ে
   * D) সবকটি
   * *উত্তর: D*
4. কাস্টম হুকের নামের শুরুতে অবশ্যই কী থাকতে হবে?
   * A) react
   * B) hook
   * C) use
   * D) get
   * *উত্তর: C*
5. React ইন্টারনালি হুকগুলোকে কীভাবে ট্র্যাক করে?
   * A) র্যান্ডম কিওয়ার্ড দিয়ে
   * B) কলিং অর্ডার/ইনডেক্স সিকোয়েন্স দিয়ে
   * C) DOM আইডি দিয়ে
   * D) CSS ক্লাস দিয়ে
   * *উত্তর: B*

### ১৭. 5 Coding exercises
1. একটি ESLint রুল চেক করার জন্য কন্ডিশনাল ব্লকে হুক লিখে এরর মেসেজটি অবজার্ভ করুন।
2. একটি কাস্টম হুক তৈরি করুন যা ব্রাউজারের অনলাইন/অফলাইন স্ট্যাটাস ট্র্যাক করবে।
3. একটি কম্পোনেন্ট তৈরি করুন যা একটি বাটনে ক্লিক করলে আরেকটি হুক-বেসড কম্পোনেন্টকে মাউন্ট ও আনমাউন্ট করবে।
4. একটি সাধারণ কাউন্টার হুক তৈরি করুন যা যেকোনো কম্পোনেন্টে রিইউজ করা যাবে।
5. একটি হুক তৈরি করুন যা ব্রাউজারের লোকালস্টোরেজে ডেটা সেভ এবং রিড করবে ডাইনামিক্যালি।

---

## ২. useEffect Hook

### ১. Simple definition (বাংলায়)
`useEffect` হলো এমন একটি হুক যা ফাংশনাল কম্পোনেন্টের ভেতরে সাইড-ইফেক্ট (Side-effects) যেমন এপিআই থেকে ডেটা আনা, সরাসরি DOM পরিবর্তন করা, টাইমার বা সাবস্ক্রিপশন সেট করার কাজগুলো পরিচালনা করতে ব্যবহৃত হয়।
এখানে রিঅ্যাক্টের দুটি অত্যন্ত গুরুত্বপূর্ণ টার্ম—**Mounting** এবং **Unmounting** যুক্ত:
* **Mounting (মাউন্ট):** যখন কোনো কম্পোনেন্ট প্রথমবার তৈরি হয়ে ব্রাউজারের DOM-এ যুক্ত হয় (অর্থাৎ স্ক্রিনে প্রথমবার দেখা যায়), তখন তাকে মাউন্টিং বা মাউন্ট বলে।
* **Unmounting (আনমাউন্ট):** যখন কোনো কম্পোনেন্ট ব্রাউজারের DOM থেকে মুছে যায় (অর্থাৎ স্ক্রিন থেকে অদৃশ্য বা বিদায় নেয়), তখন তাকে আনমাউন্টিং বা আনমাউন্ট বলে।

### ২. Why this concept exists
ফাংশনাল কম্পোনেন্টের মূল কাজ হলো প্রপস এবং স্টেট নিয়ে UI রিটার্ন করা। এই রেন্ডারিং প্রক্রিয়ার মাঝখানে যদি কোনো বাহ্যিক কাজ (সাইড-ইফেক্ট) সরাসরি করা হয়, তবে তা রেন্ডারকে বাধাগ্রস্ত করবে। ক্লাস কম্পোনেন্টের `componentDidMount` (মাউন্টের কাজ করার জন্য), `componentDidUpdate` (আপডেটের কাজের জন্য), এবং `componentWillUnmount` (আনমাউন্টের ক্লিনআপ কাজের জন্য) এর কাজগুলো এক জায়গায় করার জন্য `useEffect` তৈরি করা হয়েছে।

### ৩. What problem it solves
এটি সাইড-ইফেক্টের কোডগুলোকে আলাদা করে অ্যাপের রেন্ডার সাইকেলের সাথে সিঙ্ক করে। একই সাথে মাউন্ট, আপডেট এবং আনমাউন্ট এর জন্য আলাদা আলাদা মেথড লেখার ঝামেলা দূর করে।

### ৪. Real-life analogy
রিসিপশনিস্টের কথা চিন্তা করুন। তার মূল কাজ অতিথিদের স্বাগত জানানো এবং রুম বুকিং দেওয়া (Rendering UI)। কিন্তু গেস্ট রুম বুক করার পর তাকে বেলবয়কে কল দিয়ে ল্যাগেজ রুমে পাঠাতে হবে এবং রুমে পানির বোতল দিতে হবে (Side-effect)। এই সাইড-কাজটি সে রুম বুকিংয়ের পর আলাদাভাবে সম্পন্ন করে। `useEffect` ও তেমনি রেন্ডারিং শেষ হওয়ার পর সাইড-কাজগুলো করে।

### ৫. How React works internally regarding this concept
React যখন রেন্ডার ফিনিশ করে এবং স্ক্রিন আপডেট করে (Commit Phase-এর পর), কেবল তখনই `useEffect` কলব্যাক ফাংশনটি রান করে। 
* **Mounting (মাউন্ট) এবং Dependency Array `[]` খালি থাকলে:** ইফেক্টটি শুধু প্রথম রেন্ডারের পর (Mounting) একবার রান করে।
* **Dependency Array-তে ভেরিয়েবল থাকলে (যেমন `[count]`):** প্রতি রেন্ডারে React চেক করে পূর্ববর্তী ভ্যালুর সাথে বর্তমান ভ্যালুর কোনো অমিল আছে কিনা। অমিল থাকলে ইফেক্ট রান করে।
* **Unmounting (আনমাউন্ট) এবং Cleanup Function:** ইফেক্ট ফাংশন যদি কোনো ফাংশন রিটার্ন করে, তবে পরবর্তী ইফেক্ট রান করার আগে অথবা কম্পোনেন্ট আনমাউন্ট (Unmount) হওয়ার সময় React সেই ক্লিনআপ (cleanup) ফাংশনটি রান করে মেমরি লিক বা সাবস্ক্রিপশন পরিষ্কার করে।

### ৬. Basic example (Fetching API Data)
```jsx
import React, { useState, useEffect } from 'react';

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(res => res.json())
      .then(data => {
        setUsers(data);
        setLoading(false);
      });
  }, []); // Empty array: Runs only once on mount

  if (loading) return <p>Loading...</p>;

  return (
    <ul>
      {users.map(user => <li key={user.id}>{user.name}</li>)}
    </ul>
  );
}

export default UserList;
```

### ७. Step-by-step explanation of the code
* `useEffect` এর ভেতরে এপিআই কল করা হয়েছে।
* Dependency Array হিসেবে খালি বন্ধনী `[]` দেওয়া হয়েছে, যার মানে এটি পেজ লোড হওয়ার পর শুধু একবার এপিআই কলটি করবে।
* ডেটা আসার পর `setUsers` স্টেট আপডেট করা হয়েছে, যা কম্পোনেন্টকে রি-রেন্ডার করে লিস্ট দেখাবে।

### ৮. Another real-world example (Timer with cleanup)
```jsx
import React, { useState, useEffect } from 'react';

function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setSeconds(prev => prev + 1);
    }, 1000);

    // Cleanup function to prevent memory leaks when component unmounts
    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return <h1>Seconds: {seconds}</h1>;
}
```

### ৯. Common mistakes beginners make
* **Dependency Array বাদ দেওয়া:** দ্বিতীয় আর্গুমেন্ট না দিলে প্রতি রেন্ডারে ইফেক্ট রান করবে। যদি এর ভেতর স্টেট আপডেট করা হয়, তবে **Infinite Loop** তৈরি হবে এবং ব্রাউজার ক্র্যাশ করবে।
* **ক্লিনআপ ফাংশন না লেখা:** `setInterval` বা ইভেন্ট লিসেনার এড করার পর তা রিমুভ না করলে মেমরি লিক হয়।

### ১০. Interview questions related to this topic
1. **খালি ডিপেন্ডেন্সি অ্যারে `[]` এবং ডিপেন্ডেন্সি ছাড়া `useEffect` এর মধ্যে পার্থক্য কী?**
   * উত্তর: খালি ডিপেন্ডেন্সি অ্যারে দিলে ইফেক্টটি শুধু মাউন্টের পর ১ বার রান করবে। ডিপেন্ডেন্সি না দিলে প্রতি রেন্ডারে (যেকোনো স্টেট চেঞ্জে) ইফেক্টটি বারবার রান করবে।
2. **ক্লিনআপ ফাংশন কখন এবং কেন রান করে?**
   * উত্তর: কম্পোনেন্ট আনমাউন্ট হওয়ার সময় এবং পরবর্তী ইফেক্ট রান করার ঠিক আগে রান করে। এটি মূলত মেমরি লিক, টাইমার ও সাবস্ক্রিপশন ক্লিনআপ করতে ব্যবহৃত হয়।

### ১১. Best practices
* ডিপেন্ডেন্সি অ্যারেতে সেই সমস্ত ভ্যারিয়েবল বা ফাংশন যুক্ত করুন যা ইফেক্টের ভেতরে ব্যবহার করা হয়েছে (ক্লিন কোডের জন্য `eslint-plugin-react-hooks` এর অটোফ্লিক্স ব্যবহার করুন)।
* ইফেক্ট ফাংশনকে ছোট রাখুন এবং এক একটি ইফেক্টে কেবল একটি উদ্দেশ্য হাসিল করুন।

### ১২. Performance considerations
ডিপেন্ডেন্সি অ্যারেতে অবজেক্ট বা অ্যারে সরাসরি পাস করলে প্রতি রেন্ডারে তাদের রেফারেন্স চেঞ্জ হওয়ার কারণে ইফেক্ট বারবার ফায়ার হতে পারে। এ সমস্যা সমাধানে প্রিমিটিভ ভ্যালু ব্যবহার করুন অথবা `useMemo`/`useCallback` দিয়ে রেফারেন্স লক করুন।

### ১৩. When NOT to use it
যদি কোনো ডেটা শুধু স্টেট পরিবর্তনের ওপর ভিত্তি করে ক্যালকুলেট করা যায় (যেমন: `fullName = firstName + lastName`), তবে তার জন্য `useEffect` ব্যবহারের প্রয়োজন নেই। সরাসরি রেন্ডার টাইমে ক্যালকুলেট করুন।

### ১৪. Comparison with similar concepts
* **useEffect vs useLayoutEffect:** `useEffect` স্ক্রিনে ইউজার ডেটা দেখতে পাওয়ার পর (Asynchronously) রান করে। `useLayoutEffect` DOM পরিবর্তনের ঠিক পরপর কিন্তু ব্রাউজার স্ক্রিন পেইন্ট করার আগে (Synchronously) রান করে।

### ১৫. Summary in simple Bangla
`useEffect` হলো সাইড-ইফেক্ট হ্যান্ডেল করার হুক। পেজ লোড হওয়ার পর বা কোনো নির্দিষ্ট ডেটা পরিবর্তনের পর কোনো কাজ করতে চাইলে আমরা এটি ব্যবহার করি এবং আনমাউন্টের সময় ক্লিনআপ করতে ভুলি না।

### ১৬. 5 MCQ questions
1. `useEffect` এর ডিপেন্ডেন্সি অ্যারে খালি `[]` থাকলে এটি কখন রান করে?
   * A) প্রতি সেকেন্ডে
   * B) প্রতিটি রেন্ডারের পর
   * C) শুধুমাত্র প্রথমবার মাউন্ট হওয়ার পর
   * D) শুধুমাত্র আনমাউন্ট হওয়ার সময়
   * *উত্তর: C*
2. নিচের কোনটি সাইড-ইফেক্টের উদাহরণ নয়?
   * A) API fetching
   * B) DOM title change
   * C) Calculating two numbers `1 + 1`
   * D) Setting up a setInterval timer
   * *উত্তর: C*
3. `useEffect` এর ভেতর ইনফিনিট লুপ হওয়ার প্রধান কারণ কী?
   * A) ভুল ইউআরএল দেওয়া
   * B) ডিপেন্ডেন্সি অ্যারে না দিয়ে ইফেক্টের ভেতর স্টেট আপডেট করা
   * C) ক্লিনআপ ফাংশন রিটার্ন করা
   * D) ব্রাউজার স্লো থাকা
   * *উত্তর: B*
4. ক্লিনআপ ফাংশন কখন ফায়ার হয়?
   * A) কম্পোনেন্ট মাউন্ট হওয়ার সাথে সাথে
   * B) নেক্সট ইফেক্ট রানের আগে এবং আনমাউন্ট হওয়ার সময়
   * C) এপিআই ডেটা লোড হতে দেরি হলে
   * D) রান হয় না
   * *উত্তর: B*
5. `useLayoutEffect` এবং `useEffect`-এর মধ্যে পার্থক্য কী?
   * A) `useLayoutEffect` ক্লাসে ব্যবহৃত হয়
   * B) `useLayoutEffect` ব্রাউজার স্ক্রিন পেইন্ট করার আগে সিঙ্ক্রোনাসলি রান করে
   * C) কোনো পার্থক্য নেই
   * D) `useEffect` দ্রুত রান করে
   * *উত্তর: B*

### ১৭. 5 Coding exercises
1. একটি সার্চ ইনপুট ফিল্ড তৈরি করুন। ইউজার যখন টাইপ করা বন্ধ করবে তার ৫০০ মিলি-সেকেন্ড পর এপিআই কল করুন (Debouncing with useEffect)।
2. একটি কম্পোনেন্ট মাউন্ট হওয়ার সময় ব্রাউজার ট্যাবের টাইটেল চেঞ্জ করে "Welcome" করুন এবং আনমাউন্ট হওয়ার সময় আগের টাইটেল ফিরিয়ে নিয়ে যান।
3. একটি রি-সাইজেবল উইন্ডো ট্র্যাকার বানান যা স্ক্রিনের প্রস্থ ডাইনামিক্যালি দেখাবে এবং উইন্ডো ইভেন্ট ক্লিনআপ করবে।
4. একটি কম্পোনেন্ট বানান যা একটি আইডি প্রপ হিসেবে নেয় এবং আইডি চেঞ্জ হলে সেই নির্দিষ্ট আইডির ডেটা এপিআই থেকে এনে আপডেট করে।
5. একটি ৫ সেকেন্ডের ডাউন্টডাউন টাইমার বানান যা ০ সেকেন্ডে পৌঁছালে স্ক্রিনে একটি মেসেজ দেখাবে এবং ইন্টারভাল স্টপ করবে।

---

## ৩. useContext Hook

### ১. Simple definition (বাংলায়)
`useContext` হলো এমন একটি হুক যা রিঅ্যাক্ট কন্টেক্সট এপিআই (Context API) ব্যবহার করে কোনো প্রকার Prop Drilling (প্যারেন্ট থেকে একের পর এক চাইল্ডের মাধ্যমে প্রপস পাঠানো) ছাড়াই সরাসরি গ্লোবাল ডেটা অ্যাক্সেস করতে সাহায্য করে।

### ২. Why this concept exists
রিঅ্যাক্টে যখন কোনো স্টেট একদম উপরের কম্পোনেন্ট থেকে অনেক নিচের (যেমন ১০ লেভেল নিচে) কোনো চাইল্ড কম্পোনেন্টে পাঠাতে হয়, তখন মাঝখানের সব কম্পোনেন্টকে প্রপস পাস করতে হয়—যদিও মাঝখানের কম্পোনেন্টগুলোর ওই ডেটার কোনো প্রয়োজন নেই। একেই Prop Drilling বলে। এই কোড নোংরা করার প্রসেস থেকে মুক্তি দিতে Context API এবং `useContext` আনা হয়েছে।

### ৩. What problem it solves
এটি প্রপ ড্রিলিং দূর করে ডেটাকে গ্লোবাল বা সেন্ট্রালাইজড করে তোলে, যা মূলত থিম চেঞ্জ, ইউজার লগইন ইনফো এবং ল্যাঙ্গুয়েজ সেটিংসের ক্ষেত্রে অত্যন্ত দরকারী।

### ৪. Real-life analogy
ভাবুন আপনি একটি বড় অ্যাপার্টমেন্টের ১০ম তলায় থাকেন এবং নিচতলা থেকে পোস্টম্যান আপনাকে একটি চিঠি দিতে এসেছে।
* **Prop Drilling:** পোস্টম্যান নিচতলার দারোয়ানকে চিঠি দিল, দারোয়ান ২য় তলার বাসিন্দাকে দিল, ২য় তলার জন ৩য় তলার জনকে দিল... এভাবে ১০ম তলা পর্যন্ত চিঠি পৌঁছাল। (এটি অত্যন্ত বিরক্তিকর)।
* **useContext:** অ্যাপার্টমেন্টে একটি সেন্ট্রাল লিফট ও নোটিশ বোর্ড বা ক্লাউড ড্রপবক্স (Context) আছে। পোস্টম্যান সরাসরি সেই বক্সে চিঠি রেখে দিল, আর আপনি আপনার ঘর থেকে সরাসরি ক্লাউড অ্যাকাউন্টে ঢুকে চিঠিটি পেয়ে গেলেন। can't be bothered by people in between.

### ৫. How React works internally regarding this concept
React เมมโมรี่ Context Object. Object นี้ประกอบด้วย 2 ส่วน: `Provider` (ตัวแชร์ข้อมูล) และ `Consumer` (ตัวอ่านข้อมูล). `useContext` ทำหน้าที่เหมือน Consumer ในระดับ child node. เมื่อค่า `value` ของ `Provider` มีการเปลี่ยนแปลง React จะทำหน้าที่ re-render component ทั้งหมดที่ subscribe context นี้โดยอัตโนมัติ.

### ৬. Basic example (Theme Context)
```jsx
import React, { createContext, useContext, useState } from 'react';

// 1. Create Context
const ThemeContext = createContext();

// 2. Parent/Provider Component
export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');
  const toggleTheme = () => setTheme(prev => prev === 'light' ? 'dark' : 'light');

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}

// 3. Nested Child Component (Direct Access)
function ThemeButton() {
  const { theme, toggleTheme } = useContext(ThemeContext);
  return (
    <button onClick={toggleTheme} style={{ background: theme === 'light' ? '#fff' : '#333', color: theme === 'light' ? '#000' : '#fff' }}>
      Toggle Theme (Current: {theme})
    </button>
  );
}

export default function App() {
  return (
    <ThemeProvider>
      <div>
        <h2>Welcome to Context API</h2>
        <ThemeButton />
      </div>
    </ThemeProvider>
  );
}
```

### ৭. Step-by-step explanation of the code
* `createContext()` দিয়ে `ThemeContext` তৈরি করা হয়েছে।
* `ThemeProvider`-এর ভেতর `ThemeContext.Provider` ব্যবহার করে গ্লোবাল ভ্যালু (`theme` এবং `toggleTheme`) পাস করা হয়েছে।
* মাঝখানের কোনো কম্পোনেন্টকে প্রপস না পাঠিয়েই `ThemeButton` কম্পোনেন্ট সরাসরি `useContext(ThemeContext)` ব্যবহার করে ডেটা এবং মেথড অ্যাক্সেস করেছে।

### ৮. Another real-world example (User Authentication State)
```jsx
import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  const login = (username) => setUser({ name: username });
  const logout = () => setUser(null);

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function UserProfileHeader() {
  const { user, logout } = useContext(AuthContext);

  if (!user) return <p>Please Log In</p>;

  return (
    <div>
      <p>Hello, {user.name}!</p>
      <button onClick={logout}>Logout</button>
    </div>
  );
}
```

### ৯. Common mistakes beginners make
* **Provider র্যাপ করতে ভুলে যাওয়া:** প্রোভাইডার দিয়ে র্যাপ না করে কন্টেক্সট কনজিউম করার চেষ্টা করলে ডিফল্ট ভ্যালু (যদি থাকে) পাওয়া যাবে, অন্যথায় এরর হবে।
* **পারফরম্যান্স ইস্যু অবহেলা করা:** প্রোভাইডারের ভ্যালু যদি খুব ঘন ঘন চেঞ্জ হয়, তবে এর নিচে থাকা সমস্ত কনজিউমার কম্পোনেন্ট রি-রেন্ডার হবে, যা বড় অ্যাপে পারফরম্যান্স ড্রপ করে।

### ১০. Interview questions related to this topic
1. **Prop Drilling কী এবং এটি কীভাবে সমাধান করা যায়?**
   * উত্তর: প্যারেন্ট থেকে চাইল্ড কম্পোনেন্টে ডেটা পাঠানোর জন্য মাঝখানের অপ্রয়োজনীয় কম্পোনেন্টগুলোর ভেতর দিয়ে প্রপস পাস করাকে Prop Drilling বলে। Context API / `useContext` বা Redux ব্যবহার করে এটি সমাধান করা যায়।
2. **Context Provider-এর `value` প্রপে অবজেক্ট পাস করলে কী সমস্যা হতে পারে?**
   * উত্তর: প্রতি রেন্ডারে নতুন অবজেক্ট রেফারেন্স তৈরি হওয়ার কারণে নিচে থাকা কনজিউমারগুলো অপ্রয়োজনীয়ভাবে রি-রেন্ডার হতে পারে। এটি এড়াতে ভ্যালুটি `useMemo` দিয়ে মেমোইজ করা উচিত।

### ১১. Best practices
* খুব বেশি ঘন ঘন পরিবর্তিত স্টেট (যেমন এনিমেশন স্টেট বা ফর্ম টাইপিং স্টেট) কন্টেক্সটে রাখবেন না।
* প্রতি কন্টেক্সটের জন্য আলাদা ফাইল এবং কাস্টম হুক বানিয়ে নিন (যেমন `useAuth` বা `useTheme`) কোড ক্লিন রাখার জন্য।

### ১২. Performance considerations
কন্টেক্সটের অপ্রয়োজনীয় রি-রেন্ডারিং এড়াতে বড় কন্টেক্সটকে ছোট ছোট মাল্টিপল কন্টেক্সটে ভাগ করুন (যেমন `UserContext` এবং `SettingsContext` আলাদা রাখা)।

### ১৩. When NOT to use it
যদি প্রপস মাত্র ১ বা ২ লেভেল নিচে পাস করতে হয়, তবে অহেতুক কন্টেক্সট এপিআই ব্যবহার করে কোড জটিল করবেন না। প্রপস পাস করাই ভালো।

### ১৪. Comparison with similar concepts
* **Context API vs Redux:** Context API বিল্ট-ইন এবং ছোট-মাঝারি প্রজেক্টের জন্য উপযুক্ত। Redux হলো এক্সটারনাল স্টোর যা জটিল স্টেট ট্র্যাকিং, মিডলওয়্যার এবং বিশাল সাইজের এন্টারপ্রাইজ প্রজেক্টে ব্যবহৃত হয়।

### ১৫. Summary in simple Bangla
`useContext` হলো এমন একটি হুক যা দিয়ে আমরা প্রপ ড্রিলিং ছাড়াই অ্যাপের যেকোনো জায়গা থেকে সরাসরি গ্লোবাল ডাটা রিড করতে পারি।

### ১৬. 5 MCQ questions
1. `useContext` ব্যবহারের প্রধান কারণ কোনটি?
   * A) API Fetching করা
   * B) Prop Drilling দূর করা
   * C) DOM সিলেক্ট করা
   * D) এনিমেশন এড করা
   * *উত্তর: B*
2. Context তৈরি করার জন্য কোন ফাংশনটি ব্যবহৃত হয়?
   * A) useContext()
   * B) createContext()
   * C) makeContext()
   * D) ContextProvider()
   * *উত্তর: B*
3. চাইল্ড কম্পোনেন্টগুলোতে ডেটা সাপ্লাই করার দায়িত্ব কার?
   * A) Consumer
   * B) Provider
   * C) Router
   * D) Action
   * *উত্তর: B*
4. Provider-এর `value` প্রপ চেঞ্জ হলে কী ঘটে?
   * A) পুরো অ্যাপ ক্র্যাশ করে
   * B) শুধুমাত্র প্রোভাইডার রি-রেন্ডার হয়
   * C) ওই কন্টেক্সট ব্যবহার করা সমস্ত চাইল্ড রি-রেন্ডার হয়
   * D) কিছুই হয় না
   * *উত্তর: C*
5. নিচের কোনটি কন্টেক্সটে রাখা অনুচিত?
   * A) ইউজার লগইন স্টেট
   * B) অ্যাপ ল্যাঙ্গুয়েজ সেটিংস
   * C) প্রতি সেকেন্ডে পরিবর্তিত অ্যানিমেশন স্টেট
   * D) ডার্ক/লাইট থিম মোড
   * *উত্তর: C*

### ১৭. 5 Coding exercises
1. একটি `LanguageContext` তৈরি করুন যা 'EN' এবং 'BN' ল্যাঙ্গুয়েজ স্টেট কন্ট্রোল করবে এবং চাইল্ড কম্পোনেন্টে ল্যাঙ্গুয়েজ অনুযায়ী টেক্সট দেখাবে।
2. একটি কাস্টম হুক `useAuth` তৈরি করুন যা আপনার অথরাইজেশন কন্টেক্সটকে র‍্যাপ করবে এবং এরর হ্যান্ডেল করবে।
3. একটি শপিং কার্ট কন্টেক্সট তৈরি করুন যেখানে চাইল্ড প্রোডাক্ট কার্ডে ক্লিক করলে কার্ট কন্টেক্সটের আইটেম লিস্টে প্রোডাক্ট যুক্ত হবে।
4. একটি নোটিফিকেশন সিস্টেম কন্টেক্সট বানান যার মাধ্যমে অ্যাপের যেকোনো জায়গা থেকে `showNotification("Message")` কল করে স্ক্রিনের কর্নারে অ্যালার্ট দেখানো যাবে।
5. মাল্টিপল কন্টেক্সট (Theme + Auth) একসাথে একটি চাইল্ড কম্পোনেন্টে ব্যবহার করে দেখান।

---

## ৪. useRef Hook

### ১. Simple definition (বাংলায়)
`useRef` হলো এমন একটি হুক যা রেন্ডারিং প্রক্রিয়ায় কোনো প্রকার রি-রেন্ডার না ঘটিয়েই মেমরিতে কোনো পরিবর্তনশীল ডেটা ধরে রাখতে এবং সরাসরি ব্রাউজারের DOM এলিমেন্ট অ্যাক্সেস করতে ব্যবহৃত হয়।

### ২. Why this concept exists
React-এ স্টেট (`useState`) পরিবর্তন করলে পুরো কম্পোনেন্ট রি-রেন্ডার হয়। কিন্তু আমাদের এমন অনেক ডেটা প্রয়োজন হয় যা মেমরিতে রাখতে হবে অথচ তার পরিবর্তনের কারণে পেজ রি-রেন্ডার হওয়ার প্রয়োজন নেই (যেমন: টাইমার আইডি, প্রিভিয়াস স্টেট, বা কোনো স্ক্রল পজিশন)। এছাড়া সরাসরি DOM এলিমেন্টকে ফোকাস বা ম্যানিপুলেট করতে `useRef` ব্যবহৃত হয়।

### ৩. What problem it solves
এটি অপ্রয়োজনীয় রি-রেন্ডারিং প্রতিরোধ করে পারফরম্যান্স অপ্টিমাইজ করে এবং রিঅ্যাক্ট অ্যাপ্লিকেশনে সরাসরি DOM ইন্টিগ্রেশনের সুবিধা দেয়।

### ৪. Real-life analogy
আপনার বুকমার্ক (Bookmark) করার ফিতার কথা ভাবুন। আপনি যখন একটি মোটা বই পড়েন, আপনি যেখানে পড়া থামিয়েছেন সেখানে একটি ফিতা রেখে দেন। ফিতাটি সেখানে রাখার কারণে বইয়ের টেক্সট বা গল্পের কোনো পরিবর্তন হয় না (No Render), কিন্তু ফিতাটি দেখে আপনি সহজেই বুঝতে পারেন আপনি কোন লাইনে ছিলেন (Reference)।

### ৫. How React works internally regarding this concept
`useRef(initialValue)` কল করলে React মেমরিতে একটি অবজেক্ট তৈরি করে যার ভেতরে একটি সিঙ্গেল প্রপার্টি থাকে: `{ current: initialValue }`। কম্পোনেন্টের রেন্ডার সাইকেলের মাঝে এই অবজেক্টের রেফারেন্স কখনোই পরিবর্তন হয় না। আপনি যতবার খুশি `ref.current` এর ভ্যালু চেঞ্জ করতে পারেন, React কোনো রি-রেন্ডার ট্রিগার করবে না।

### ৬. Basic example (Focusing an Input Element)
```jsx
import React, { useRef } from 'react';

function AutoFocusInput() {
  const inputRef = useRef(null);

  const handleClick = () => {
    // Accessing the DOM input node and focusing it
    inputRef.current.focus();
  };

  return (
    <div>
      <input ref={inputRef} type="text" placeholder="Click button to focus me" />
      <button onClick={handleClick}>Focus Input</button>
    </div>
  );
}

export default AutoFocusInput;
```

### ৭. Step-by-step explanation of the code
* `const inputRef = useRef(null);` দিয়ে একটি রেফারেন্স অবজেক্ট তৈরি করা হয়েছে।
* `<input ref={inputRef} />` দিয়ে ইনপুট ট্যাগের সাথে রেফারেন্সটি কানেক্ট করা হয়েছে।
* বাটনে ক্লিক করা হলে `inputRef.current` সরাসরি আসল DOM ইনপুট নোডটিকে অ্যাক্সেস করে এবং `focus()` মেথড কল করে।

### ৮. Another real-world example (Storing Timer Instance)
```jsx
import React, { useState, useRef } from 'react';

function Stopwatch() {
  const [seconds, setSeconds] = useState(0);
  const timerRef = useRef(null); // stores the interval ID without re-rendering

  const start = () => {
    if (timerRef.current !== null) return;
    timerRef.current = setInterval(() => {
      setSeconds(prev => prev + 1);
    }, 1000);
  };

  const stop = () => {
    clearInterval(timerRef.current);
    timerRef.current = null;
  };

  return (
    <div>
      <h3>Time: {seconds}s</h3>
      <button onClick={start}>Start</button>
      <button onClick={stop}>Stop</button>
    </div>
  );
}
```

### ৯. Common mistakes beginners make
* **useRef-এর ভ্যালু সরাসরি স্ক্রিনে রেন্ডার করা:** যেহেতু `ref.current` পরিবর্তন হলে রি-রেন্ডার হয় না, তাই যদি আপনি JSX-এ `{myRef.current}` দেখান, তবে ভ্যালু আপডেট হলেও স্ক্রিনে পুরানো ভ্যালুই থেকে যাবে। স্ক্রিনে দেখানোর জন্য সবসময় `useState` ব্যবহার করুন।
* **DOM নোড মাউন্ট হওয়ার আগেই অ্যাক্সেস করা:** মাউন্ট হওয়ার আগে `ref.current` এর ভ্যালু `null` থাকে। তাই রেন্ডার ফেজে সরাসরি `ref.current` অ্যাক্সেস করতে গেলে ক্র্যাশ করতে পারে। ইফেক্ট বা ইভেন্ট হ্যান্ডলারের ভেতর এটি অ্যাক্সেস করা নিরাপদ।

### ১০. Interview questions related to this topic
1. **useState এবং useRef-এর প্রধান পার্থক্য কী?**
   * উত্তর: `useState` পরিবর্তন হলে কম্পোনেন্ট রি-রেন্ডার হয় এবং নতুন UI স্ক্রিনে দেখায়। `useRef` পরিবর্তন হলে কোনো রি-রেন্ডার হয় না, ডেটা মেমরিতে তাৎক্ষণিকভাবে পরিবর্তিত হয়ে থাকে।
2. **`useRef` দিয়ে কীভাবে প্রিভিয়াস স্টেট (Previous State) ট্র্যাক করা যায়?**
   * উত্তর: `useEffect` ব্যবহার করে। যেহেতু ইফেক্ট রেন্ডার হওয়ার পর রান করে, তাই আমরা ইফেক্টের ভেতর `prevRef.current = state` লিখে রাখলে পরবর্তী রেন্ডারে ওই `prevRef.current`-এ পুরানো স্টেটটি পাওয়া যাবে।

### ১১. Best practices
* DOM-এ সরাসরি রাইট করা (যেমন স্টাইল পরিবর্তন বা চাইল্ড এড করা) এভয়েড করুন। রিঅ্যাক্টকে DOM হ্যান্ডেল করতে দিন; `useRef` শুধু রিড বা ফোকাস করার জন্য ব্যবহার করুন।
* রেন্ডারিং লজিকের ঠিক মাঝখানে `ref.current` রিড বা রাইট করবেন না, এটি সাইড-ইফেক্ট বা ইভেন্ট হ্যান্ডলারে করুন।

### ১২. Performance considerations
অপ্রয়োজনীয় স্টেট আপডেট এড়াতে `useRef` ব্যবহার করা একটি চমৎকার অপ্টিমাইজেশন ট্রিক (যেমন ফর্মের ইনপুট সাবমিটের আগে মেমরিতে জমা রাখা)।

### ১৩. When NOT to use it
যদি কোনো ডেটা চেঞ্জের কারণে স্ক্রিনের UI-তে রিয়েল-টাইম পরিবর্তন দেখানোর প্রয়োজন হয়, সেখানে `useRef` ব্যবহার করবেন না।

### ১৪. Comparison with similar concepts
* **useRef vs plain let variable inside component:** প্রতি রেন্ডারে সাধারণ `let` ভেরিয়েবল নতুন করে ইনিশিয়ালাইজ হয়ে যায় এবং তার পুরানো ভ্যালু হারিয়ে যায়। কিন্তু `useRef` প্রতি রেন্ডারে তার পূর্ববর্তী ভ্যালু ধরে রাখতে পারে।

### ১৫. Summary in simple Bangla
`useRef` হলো রি-রেন্ডার না করে মেমরিতে ডেটা রাখার একটি ট্রিক এবং সরাসরি ব্রাউজারের DOM উপাদান অ্যাক্সেস করার একটি চাবি।

### ১৬. 5 MCQ questions
1. `useRef` এর ভ্যালু আপডেট হলে নিচের কোনটি ঘটে?
   * A) কম্পোনেন্ট রি-রেন্ডার হয়
   * B) মেমরি লিক হয়
   * C) কোনো রি-রেন্ডার হয় না
   * D) এপিআই ফায়ার হয়
   * *উত্তর: C*
2. `useRef` রিটার্ন করা অবজেক্টের ভেতরে কোন প্রপার্টিটি থাকে?
   * A) value
   * B) current
   * C) state
   * D) ref
   * *উত্তর: B*
3. কেন সাধারণ `let` ভেরিয়েবল মেমরি ডেটা রাখার জন্য উপযুক্ত নয়?
   * A) এটি খুব ধীরগতির
   * B) এটি প্রতি রেন্ডারে রি-ইনিশিয়ালাইজ হয়ে যায়
   * C) এটি DOM অ্যাক্সেস করতে পারে না
   * D) এটি গ্লোবাল করা যায় না
   * *উত্তর: B*
4. DOM নোড ফোকাস করার জন্য কোন হুক ব্যবহার করা রিকমেন্ডেড?
   * A) useState
   * B) useEffect
   * C) useRef
   * D) useMemo
   * *উত্তর: C*
5. `useRef` ব্যবহার করার পর প্রাথমিক ভ্যালু অ্যাক্সেস করার সঠিক সিনট্যাক্স কোনটি?
   * A) `myRef`
   * B) `myRef.current`
   * C) `myRef.value`
   * D) `myRef.state`
   * *উত্তর: B*

### ১৭. 5 Coding exercises
1. একটি ভিডিও প্লেয়ার কম্পোনেন্ট তৈরি করুন যেখানে "Play" এবং "Pause" বাটনে ক্লিক করলে `useRef` দিয়ে সরাসরি ভিডিও প্লে/পজ হবে।
2. একটি কম্পোনেন্ট কতবার রেন্ডার হয়েছে তা ট্র্যাক করার জন্য একটি কাউন্টার তৈরি করুন `useRef` ব্যবহার করে (কোনো অতিরিক্ত রেন্ডার ছাড়াই)।
3. `useRef` ব্যবহার করে একটি পাসওয়ার্ড ফিল্ডের পাশে "Show/Hide" বাটন তৈরি করুন যা পাসওয়ার্ড ইনপুটের `type` অ্যাট্রিবিউট টেক্সট ও পাসওয়ার্ডে রূপান্তর করবে।
4. একটি স্ক্রল-টু-টপ বাটন তৈরি করুন যা ক্লিক করলে পেজের নির্দিষ্ট এলিমেন্টে স্ক্রল করে নিয়ে যাবে।
5. একটি কম্পোনেন্ট লিখুন যা ইউজার ইনপুটের প্রিভিয়াস ভ্যালু (Previous State) স্ক্রিনে প্রোভাইড করবে।

---

## ৫. useMemo & useCallback Hooks

### ১. Simple definition (বাংলায়)
* **useMemo:** এটি একটি হুক যা কোনো জটিল বা ব্যয়বহুল ক্যালকুলেশনের ফলাফলকে মেমরিতে ক্যাশ (Cache/Memoize) করে রাখে যাতে প্রতি রেন্ডারে অহেতুক ওই ভারী ক্যালকুলেশনটি পুনরায় রান করতে না হয়।
* **useCallback:** এটি একটি হুক যা কোনো ফাংশনের ডেফিনেশনকে মেমরিতে ক্যাশ করে রাখে যাতে প্রতি রেন্ডারে নতুন করে একই ফাংশন তৈরি (Instantiated) না হয় এবং চাইল্ড কম্পোনেন্টের অপ্রয়োজনীয় রি-রেন্ডার ঠেকানো যায়।

### ২. Why this concept exists
জাভাস্ক্রিপ্টে প্রতিবার যখন একটি কম্পোনেন্ট রি-রেন্ডার হয়, তার ভেতরের সমস্ত লজিক ও ফাংশন নতুন করে মেমরিতে রি-ক্রিয়েট হয়। 
* যদি কোনো ভারী ক্যালকুলেশন (যেমন লাখ লাখ ডেটা ফিল্টারিং) থাকে, তবে প্রতি কি-স্ট্রোকে রেন্ডার হওয়ার সময় অ্যাপ ল্যাগ করবে।
* রিঅ্যাক্টে ফাংশনগুলো অবজেক্ট রেফারেন্স বহন করে। তাই চাইল্ড কম্পোনেন্টে কোনো ফাংশন পাস করলে চাইল্ড মনে করে নতুন প্রপস এসেছে এবং চাইল্ডটি রি-রেন্ডার হয়। এই দুটি সমস্যা দূর করতে এই হুক জোড়া ব্যবহার করা হয়।

### ৩. What problem it solves
অপ্রয়োজনীয় কম্পিউটেশন এবং রেফারেন্সিয়াল ইকুয়ালিটি (Referential Equality) জনিত অপ্রয়োজনীয় চাইল্ড রি-রেন্ডারিং সমস্যা সমাধান করে মেমরি অপ্টিমাইজেশন নিশ্চিত করে।

### ৪. Real-life analogy
* **useMemo:** আপনি একজন গণিতবিদ। আপনাকে বলা হলো `5837 * 9827` কত? আপনি অনেক কষ্ট করে হিসাব করে বের করলেন `57,360,299` এবং ডায়েরিতে লিখে রাখলেন (useMemo)। পরবর্তী সময়ে কেউ একই প্রশ্ন করলে আপনি হিসাব না করে ডায়েরি দেখে সাথে সাথে উত্তর দিয়ে দিলেন।
* **useCallback:** আপনি একটি কাজের জন্য একটি চুক্তিনামায় স্বাক্ষর করছেন। প্রতিবার মিটিংয়ে নতুন করে পুরো চুক্তিনামা টাইপ না করে আপনি পুরানো চুক্তিনামার একটি জেরক্স বা কপি ব্যবহার করছেন (useCallback), যাতে সময় বাঁচে।

### ۵. How React works internally regarding this concept
* **useMemo:** React প্রথমবার ক্যালকুলেশন করে ভ্যালুটি সেভ করে। পরবর্তী রেন্ডারগুলোতে React ডিপেন্ডেন্সি অ্যারে চেক করে। যদি ডিপেন্ডেন্সি অপরিবর্তিত থাকে, তবে আগের ক্যাশড ভ্যালু রিটার্ন করে।
* **useCallback:** এটি ঠিক `useMemo` এর মতোই কাজ করে, তবে এটি কোনো মান ক্যাশ না করে সরাসরি **ফাংশন রেফারেন্স** ক্যাশ করে। `useCallback(fn, deps)` মূলত `useMemo(() => fn, deps)` এর সমান।

### ৬. Basic example (useMemo for calculation, useCallback for functions)
```jsx
import React, { useState, useMemo, useCallback } from 'react';

// Heavy calculation helper
const heavyComputation = (num) => {
  console.log('Running heavy calculation...');
  for (let i = 0; i < 1000000000; i++) {} // Artificial delay
  return num * 2;
};

function CalcDemo() {
  const [count, setCount] = useState(0);
  const [themeDark, setThemeDark] = useState(false);

  // useMemo caches the result of the calculation
  const doubleCount = useMemo(() => {
    return heavyComputation(count);
  }, [count]); // Recalculates only when 'count' changes

  // useCallback caches the function reference
  const toggleTheme = useCallback(() => {
    setThemeDark(prev => !prev);
  }, []); // Caches once and never recreates

  return (
    <div style={{ background: themeDark ? '#333' : '#fff', color: themeDark ? '#fff' : '#000', padding: '20px' }}>
      <h2>Count: {count} | Double Count: {doubleCount}</h2>
      <button onClick={() => setCount(count + 1)}>Increment Count</button>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </div>
  );
}

export default CalcDemo;
```

### ৭. Step-by-step explanation of the code
* `doubleCount` ক্যালকুলেশনটি `useMemo` দিয়ে মুড়িয়ে রাখা হয়েছে। তাই যখন ইউজার "Toggle Theme" বাটনে ক্লিক করবে, থিম চেঞ্জ হলেও ভারী হিসাবটি আবার রান করবে না। এটি কেবল তখনই রান করবে যখন `count` চেঞ্জ হবে।
* `toggleTheme` ফাংশনটি `useCallback` দিয়ে র্যাপ করায় প্রতি রেন্ডারে এর মেমরি রেফারেন্স চেঞ্জ হবে না।

### ৮. Another real-world example (Optimizing Child Component Rendering)
```jsx
import React, { useState, useCallback } from 'react';

// Child optimized with React.memo
const ChildList = React.memo(({ items, onItemClick }) => {
  console.log('Child rendered!');
  return (
    <ul>
      {items.map(item => (
        <li key={item} onClick={() => onItemClick(item)}>{item}</li>
      ))}
    </ul>
  );
});

// Parent
function ParentApp() {
  const [text, setText] = useState('');
  const [items] = useState(['Apple', 'Orange', 'Mango']);

  // useCallback prevents child from re-rendering when 'text' changes
  const handleItemClick = useCallback((item) => {
    console.log('Clicked: ', item);
  }, []);

  return (
    <div>
      <input value={text} onChange={(e) => setText(e.target.value)} placeholder="Type something" />
      <ChildList items={items} onItemClick={handleItemClick} />
    </div>
  );
}
```

### ৯. Common mistakes beginners make
* **সব জায়গায় useMemo/useCallback ব্যবহার করা:** অপ্টিমাইজেশন ফ্রিতে আসে না। হুক কল করার এবং ডিপেন্ডেন্সি চেক করার নিজস্ব একটি ওভারহেড আছে। ছোটখাটো সাধারণ ফাংশন বা ক্যালকুলেশনে এগুলো ব্যবহার করলে পারফরম্যান্স বাড়ার বদলে উল্টো কমে যেতে পারে।
* **ডিপেন্ডেন্সি অ্যারেতে ভুল ভেরিয়েবল দেওয়া:** ডিপেন্ডেন্সি খালি রাখলে ইফেক্ট বা ফাংশনে ব্যবহৃত ভেরিয়েবলগুলোর আপডেট ভ্যালু পাওয়া যায় না (Stale Closures)।

### ১০. Interview questions related to this topic
1. **useMemo এবং useCallback-এর মধ্যে প্রধান পার্থক্য কী?**
   * উত্তর: `useMemo` একটি ফাংশন কল করে তার রিটার্ন করা **ভ্যালু** মেমোইজ করে। `useCallback` সরাসরি **ফাংশন অবজেক্টটিকেই** মেমোইজ করে।
2. **কখন useCallback ব্যবহার করা বাধ্যতামূলক?**
   * উত্তর: যখন কোনো ফাংশনকে প্রপ হিসেবে কোনো অপ্টিমাইজড চাইল্ড কম্পোনেন্টে (`React.memo` দিয়ে র্যাপ করা) পাস করা হয় অথবা যখন ফাংশনটি অন্য কোনো হুকের (যেমন `useEffect`) ডিপেন্ডেন্সি হিসেবে ব্যবহৃত হয়।

### ১১. Best practices
* প্রোজেক্ট বানানোর শুরুতেই প্রি-ম্যাচিউর অপ্টিমাইজেশন (Premature Optimization) হিসেবে সব জায়গায় `useMemo` বা `useCallback` ব্যবহার করবেন না। আগে অ্যাপ বানান, তারপর ল্যাগ মনে হলে মেজার করে অপ্টিমাইজ করুন।
* `React.memo` ব্যবহার করলেই কেবল চাইল্ডে পাঠানো ফাংশনগুলোতে `useCallback` ব্যবহার করুন, অন্যথায় চাইল্ড এমনিতেও রি-রেন্ডার হবে।

### ১২. Performance considerations
রেন্ডার টাইমে যদি মেমরি রি-ইনিশিয়ালাইজেশন ঠেকানো যায়, তবে জাভাস্ক্রিপ্ট ইঞ্জিনের Garbage Collection-এর ওপর চাপ কমে, যা পেজের স্ক্রলিং ও জটিল এনিমেশনকে আরও মসৃণ করে।

### ১৩. When NOT to use it
ছোট সাধারণ ক্যালকুলেশন (যেমন `items.length`) বা যেসব চাইল্ড কম্পোনেন্ট অপ্টিমাইজড নয় তাদের ক্ষেত্রে `useMemo` বা `useCallback` ব্যবহার করবেন না।

### ১৪. Comparison with similar concepts
* **useMemo vs useCallback:** `useMemo(() => fn, deps)` returns **value**. `useCallback(fn, deps)` returns **fn**.

### ১৫. Summary in simple Bangla
`useMemo` ক্যালকুলেশনের ভ্যালু ক্যাশ করে রাখে এবং `useCallback` ফাংশনের রেফারেন্স ক্যাশ করে রাখে, যাতে অপ্রয়োজনীয় কাজ ও চাইল্ড রি-রেন্ডারিং রোধ করে পেজ ফাস্ট করা যায়।

### ১৬. 5 MCQ questions
1. `useMemo` কী ক্যাশ বা স্টোর করে?
   * A) HTML নোড
   * B) ফাংশনের রিটার্ন করা ভ্যালু
   * C) সম্পূর্ণ স্টেট অবজেক্ট
   * D) উইন্ডো লোকেশন
   * *উত্তর: B*
2. `useCallback` কী মেমোইজ করে?
   * A) গ্লোবাল স্টেট
   * B) রেন্ডার মেথড
   * C) ফাংশন অবজেক্ট বা রেফারেন্স
   * D) এপিআই রেসপন্স
   * *উত্তর: C*
3. `useCallback(fn, deps)` নিচের কোনটির সমতুল্য?
   * A) `useMemo(() => fn, deps)`
   * B) `useEffect(fn, deps)`
   * C) `useState(fn)`
   * D) `useRef(fn)`
   * *উত্তর: A*
4. অপ্টিমাইজেশনের উদ্দেশ্যে চাইল্ড কম্পোনেন্টকে র্যাপ করার পদ্ধতি কোনটি?
   * A) React.memo()
   * B) useMemo()
   * C) useCallback()
   * D) StrictMode
   * *উত্তর: A*
5. প্রি-ম্যাচিউর অপ্টিমাইজেশনের প্রধান কুফল কী?
   * A) অ্যাপ রান হবে না
   * B) রি-রেন্ডার বন্ধ হয়ে যাবে
   * C) হুক ওভারহেডের কারণে পারফরম্যান্স কমে যেতে পারে
   * D) কোনো কুফল নেই
   * *উত্তর: C*

### ১৭. 5 Coding exercises
1. একটি বড় অ্যারে (১০০০০ আইটেম) ফিল্টার করার জন্য একটি সার্চ সিস্টেম বানান যা `useMemo` দিয়ে অপ্টিমাইজ করা থাকবে।
2. `React.memo` এবং `useCallback` ব্যবহার করে একটি প্যারেন্ট-চাইল্ড রি-রেন্ডারিং ডেমো প্রজেক্ট তৈরি করুন এবং ব্রাউজার কনসোলে এর পারফরম্যান্স ইমপ্রুভমেন্ট প্রুফ করুন।
3. একটি কম্পোনেন্ট তৈরি করুন যেখানে একটি এপিআই ফেচিং ফাংশন `useCallback` দিয়ে মেমোইজ করা থাকবে এবং সেটি `useEffect`-এর ডিপেন্ডেন্সি হিসেবে কাজ করবে।
4. একটি শপিং কার্ট টোটাল প্রাইস ক্যালকুলেশনকে `useMemo` দিয়ে অপ্টিমাইজ করুন যেখানে ডিসকাউন্টের ভ্যালু চেঞ্জ হলেই কেবল রিক্যালকুলেশন হবে।
5. একটি বাটন গ্রিড (যেমন ক্যালকুলেটর) তৈরি করুন যেখানে প্রতিটি বাটনের ক্লিকার হ্যান্ডলার `useCallback` দিয়ে র্যাপ করা থাকবে যাতে বাটনগুলো অপ্রয়োজনীয়ভাবে রেন্ডার না হয়।
