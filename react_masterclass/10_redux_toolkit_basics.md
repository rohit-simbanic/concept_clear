# Redux and Redux Toolkit Basics: Comprehensive Masterclass

এই ডকুমেন্টে আমরা Redux এবং Redux Toolkit (RTK) এর মৌলিক এবং উন্নত বিষয়গুলো গভীরভাবে আলোচনা করব। প্রতিটি বিষয়কে বাস্তব জীবনের উদাহরণ, অভ্যন্তরীণ কাজের মেকানিজম, কোড এবং প্র্যাক্টিকাল অনুশীলনের মাধ্যমে ধাপে ধাপে বোঝানো হয়েছে।

---

# Topic 1: When and Why to Use Redux? (Redux is not mandatory)

## 1. Simple Definition (সহজ সংজ্ঞা)
Redux হলো একটি open-source JavaScript library যা মূলত অ্যাপ্লিকেশনের State management-এর জন্য ব্যবহৃত হয়। এটি অ্যাপ্লিকেশনের সমস্ত State-কে একটি একক central location-এ সংরক্ষণ করে, যাকে "Store" বলা হয়। এর ফলে অ্যাপ্লিকেশনের যেকোনো Component থেকে খুব সহজেই State-কে access এবং update করা সম্ভব হয়। Redux কোনোভাবেই React-এর জন্য mandatory বা snowboarding-এর মতো বাধ্যতামূলক নয়; এটি একটি সম্পূর্ণ independent library যা Angular, Vue, এমনকি plain JavaScript (Vanilla JS)-এর সাথেও চমৎকারভাবে কাজ করে।

## 2. Why This Concept Exists (কেন এই ধারণার উৎপত্তি)
React-এ ডেটা সাধারণত একমুখী বা Unidirectional (Parent থেকে Child-এর দিকে) প্রবাহিত হয়। যখন একটি অ্যাপ্লিকেশনের সাইজ বড় হতে থাকে, তখন একাধিক দূরবর্তী বা nested components-এর মধ্যে ডেটা শেয়ার করার প্রয়োজন পড়ে। React-এর নিজস্ব স্টেট ম্যানেজমেন্ট ব্যবস্থা দিয়ে এটি করতে গেলে Parent component-এ স্টেটকে lift up করতে হয় এবং অপ্রয়োজনীয় অনেক ইন্টারমিডিয়েট কম্পোনেন্টের মধ্য দিয়ে প্রপস পাস করতে হয়। এই স্টেট ট্র্যাকিং এবং ম্যানেজমেন্টকে আরও সুшৃঙ্খল, সুনির্দিষ্ট এবং predictable করার জন্য Redux কনসেপ্টটির উৎপত্তি হয়েছে।

## 3. What Problem It Solves (এটি কোন সমস্যার সমাধান করে)
*   **Prop Drilling**: যখন একটি গভীরভাবে নেস্টেড চাইল্ড কম্পোনেন্টে ডেটা পাঠাতে হয়, তখন মাঝখানের কম্পোনেন্টগুলো (যেগুলোর ওই ডেটার কোনো প্রয়োজন নেই) প্রপস বহন করতে বাধ্য হয়। Redux এই Prop Drilling দূর করে সরাসরি স্টোর থেকে ডেটা অ্যাক্সেস করার সুবিধা দেয়।
*   **State Inconsistency**: যখন অ্যাপ্লিকেশনের বিভিন্ন স্ক্রিন বা সেকশনে একই ডেটার একাধিক কপি থাকে, তখন একটি জায়গায় ডেটা আপডেট হলে অন্য জায়গায় তা সিঙ্ক না হওয়ার ঝুঁকি থাকে। Redux একটি "Single Source of Truth" প্রদান করে এই সমস্যা দূর করে।
*   **Debugging Complexity**: সাধারণ অ্যাপে স্টেট কখন এবং কীভাবে পরিবর্তন হচ্ছে তা ট্র্যাক করা কঠিন। Redux তার কঠোর ডাটা ফ্লো-এর মাধ্যমে প্রতিটি স্টেট পরিবর্তনকে ট্র্যাকযোগ্য এবং ডিবাগযোগ্য করে তোলে।

## 4. Real-Life Analogy (বাস্তব জীবনের উদাহরণ)
একটি কর্পোরেট ব্যাংকের উদাহরণ দেওয়া যাক। যদি ব্যাংকের কোনো কেন্দ্রীয় হিসাবের খাতা বা Central Ledger না থাকত এবং প্রতিটি ব্যাংক কর্মকর্তা বা কাস্টমারকে নিজেদের মধ্যে সরাসরি হিসাব রাখতে হতো, তবে পুরো ব্যাংকিং সিস্টেম ভেঙে পড়ত। Redux হলো সেই সেন্ট্রাল ব্যাংক লেজার বা সেন্ট্রাল ডাটাবেস। আপনি সরাসরি কোনো লকারে হাত দিয়ে টাকা (State) পরিবর্তন করতে পারবেন না। আপনাকে একটি সুনির্দিষ্ট স্লিপ বা রিকোয়েস্ট (Action) পূরণ করে ক্যাশিয়ারের (Reducer) কাছে জমা দিতে হবে। ক্যাশিয়ার লেজার বুক (Store) আপডেট করবে এবং আপনার অ্যাকাউন্টের ব্যালেন্স আপডেট হয়ে যাবে। এর ফলে পুরো ব্যাংকের লেনদেনের ইতিহাস সম্পূর্ণ সুরক্ষিত এবং ট্র্যাক করা সম্ভব হয়।

## 5. How React Works Internally Regarding This Concept (এই বিষয়ে React কীভাবে অভ্যন্তরীণভাবে কাজ করে)
React মূলত একটি UI rendering engine। React-এর নিজস্ব `useState` এবং `useReducer` লোকাল কম্পোনেন্ট লেভেলে স্টেট ট্র্যাক করে। যখন আমরা Redux ব্যবহার করি, তখন `react-redux` লাইব্রেরি React-এর Context API-এর মতো একটি গলোবাল ব্রডকাস্টিং মেকানিজম ব্যবহার করে পুরো অ্যাপটিকে `<Provider>` কম্পোনেন্ট দ্বারা মুড়িয়ে দেয়। Redux store-এ যখনই কোনো স্টেট আপডেট হয়, তখন React-redux ইন্টারনাল সাবস্ক্রিপশন মেকানিজম (`store.subscribe()`) ব্যবহার করে দেখে যে কোন কোন কম্পোনেন্ট ওই নির্দিষ্ট স্টেট স্লাইস ব্যবহার করছে (`useSelector` হুকের মাধ্যমে)। শুধুমাত্র সেই সাবস্ক্রাইবড কম্পোনেন্টগুলোকে রি-রেন্ডার করার সিগন্যাল পাঠানো হয়। React তখন তার Virtual DOM কম্পারিজন এবং reconciliation অ্যালগরিদমের মাধ্যমে কেবল পরিবর্তিত অংশটুকু ব্রাউজারের আসল DOM-এ রেন্ডার করে।

## 6. Basic Example (বেসিক উদাহরণ)

```javascript
// A simple React component showing counter state management WITHOUT Redux
import React, { useState } from 'react';

export function SimpleCounter() {
  const [count, setCount] = useState(0);

  return (
    <div style={{ padding: '20px', textAlign: 'center', border: '1px solid #ccc' }}>
      <h2>Counter without Redux (Local State)</h2>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)}>Decrement</button>
    </div>
  );
}
```

```javascript
// How Redux concepts are written in plain JavaScript/Redux style (No React bindings yet)
const redux = require('redux');

// 1. Initial State
const initialState = {
  count: 0
};

// 2. Reducer
function counterReducer(state = initialState, action) {
  switch (action.type) {
    case 'counter/increment':
      return { ...state, count: state.count + 1 };
    case 'counter/decrement':
      return { ...state, count: state.count - 1 };
    default:
      return state;
  }
}

// 3. Create Store
const store = redux.createStore(counterReducer);

// 4. Subscribe to changes
const unsubscribe = store.subscribe(() => {
  console.log('State updated:', store.getState());
});

// 5. Dispatch Actions
store.dispatch({ type: 'counter/increment' });
store.dispatch({ type: 'counter/decrement' });

// Clean up subscription
unsubscribe();
```

## 7. Step-by-Step Explanation of the Code (কোডের ধাপে ধাপে ব্যাখ্যা)
*   **useState Example**: এখানে `useState(0)` লোকাল রিঅ্যাক্ট স্টেট ইনিশিয়েট করে। `setCount` ব্যবহার করে কম্পোনেন্টের ভেতরেই সরাসরি স্টেট আপডেট করা হচ্ছে, যা অন্য কোনো কম্পোনেন্ট জানতে পারছে না।
*   **Redux Example**:
    *   `initialState` অবজেক্টটি ডিফল্ট স্টেট ধারণ করে।
    *   `counterReducer` একটি pure function যা বর্তমান `state` এবং একটি `action` নেয়। অ্যাকশনের `type` চেক করে এটি সম্পূর্ণ নতুন একটি স্টেট অবজেক্ট রিটার্ন করে (`{ ...state, count: state.count + 1 }`)। এটি মূল স্টেটকে সরাসরি পরিবর্তন (mutate) করে না।
    *   `redux.createStore(counterReducer)` ফাংশনটি দিয়ে গ্লোবাল স্টোর তৈরি করা হয় যা স্টেটকে ধরে রাখে।
    *   `store.subscribe()` মেথডটি রেজিস্টার করে যে যখনই স্টোর আপডেট হবে, তখনই এই কলব্যাক ফাংশনটি রান করবে।
    *   `store.dispatch()` মেথডের মাধ্যমে আমরা অ্যাকশন অবজেক্ট স্টোরে পাঠাই, যা রিডিউসারকে ট্রিগার করে স্টেট পরিবর্তন করতে সাহায্য করে।

## 8. Another Real-World Example (আরেকটি বাস্তব উদাহরণ)
মাল্টি-ল্যাঙ্গুয়েজ সাপোর্ট (i18n) এবং ডার্ক মোড/লাইট মোড সেটিংস। যখন ইউজার প্রোফাইল পেজে গিয়ে ভাষা বা থিম পরিবর্তন করে, তখন হেডার, সাইডবার, ফুটারসহ পুরো ওয়েবসাইটের টেক্সট এবং কালার পরিবর্তন হতে হবে। Redux স্টোরে গ্লোবাল ল্যাঙ্গুয়েজ ও থিম স্টেট রেখে খুব সহজেই সব কম্পোনেন্টে এই পরিবর্তন একযোগে ছড়ানো যায়।

## 9. Common Mistakes Beginners Make (নতুনদের করা সাধারণ ভুলসমূহ)
*   **Redux-কে বাধ্যতামূলক মনে করা**: প্রতিটি সাধারণ বা ছোট প্রজেক্টে শুরুতেই Redux সেটআপ করে জটিলতা বাড়িয়ে ফেলা।
*   **লোকাল স্টেটকে রেডক্সে রাখা**: ইনপুট ফিল্ডের টাইপিং ডাটা বা ড্রপডাউনের ওপেন/ক্লোজড স্টেট যা শুধুমাত্র একটি কম্পোনেন্টের ভেতরেই সীমাবদ্ধ, তাও Redux স্টোরে রাখা।
*   **সরাসরি স্টেট মিউটেট করা**: রিডিউসারের ভেতরে নতুন অবজেক্ট রিটার্ন না করে সরাসরি `state.count++` বা `state.items.push(item)` করা। এর ফলে React বুঝতে পারে না যে স্টেট পরিবর্তিত হয়েছে এবং রি-রেন্ডার হয় না।

## 10. Interview Questions Related to This Topic (ইন্টারভিউয়ের প্রশ্নসমূহ)
1.  **Redux কি এবং এর প্রধান সুবিধাগুলো কি কি?**
    *   *উত্তরঃ* Redux হলো JavaScript অ্যাপের জন্য একটি Predictable State Container। এর প্রধান সুবিধা হলো Single Source of Truth, Predictable State updates, এবং সহজ ডিবাগিং (Time Travel Debugging)।
2.  **React অ্যাপ্লিকেশনের জন্য Redux কি বাধ্যতামূলক? কখন এটি ব্যবহার করা উচিত নয়?**
    *   *উত্তরঃ* না, এটি বাধ্যতামূলক নয়। ছোট বা মাঝারি অ্যাপ্লিকেশন যেখানে স্টেট শেয়ারিংয়ের পরিমাণ খুবই কম, সেখানে Redux ব্যবহার করা উচিত নয়।
3.  **Prop Drilling কি এবং Redux কিভাবে এটি সমাধান করে?**
    *   *উত্তরঃ* Prop Drilling হলো গভীরভাবে নেস্টেড চাইল্ড কম্পোনেন্টে ডাটা পাঠানোর জন্য মাঝখানের অপ্রয়োজনীয় কম্পোনেন্টগুলোর মধ্য দিয়ে প্রপস পাস করা। Redux একটি সেন্ট্রাল স্টোর প্রদান করে, যা থেকে যেকোনো কম্পোনেন্ট সরাসরি ডাটা পেতে পারে, ফলে মাঝখানের কম্পোনেন্টগুলোর মাধ্যমে প্রপস পাস করতে হয় না।
4.  **Local State এবং Global State এর মধ্যে পার্থক্য কি?**
    *   *উত্তরঃ* Local State শুধুমাত্র একটি নির্দিষ্ট কম্পোনেন্ট এবং তার চাইল্ড কম্পোনেন্টের মধ্যে সীমাবদ্ধ থাকে (যেমন: React-এর `useState`)। Global State পুরো অ্যাপ্লিকেশনের যেকোনো কম্পোনেন্ট থেকে অ্যাক্সেস করা যায় (যেমন: Redux Store)।
5.  **Context API এবং Redux-এর মধ্যে পারফরম্যান্সের পার্থক্য কি?**
    *   *উত্তরঃ* Context API-তে কোনো স্টেট পরিবর্তন হলে ওই কনটেক্সটের অধীনে থাকা সমস্ত কনজিউমার কম্পোনেন্ট রি-রেন্ডার হয়, যা বড় অ্যাপে পারফরম্যান্স ড্রপ ঘটাতে পারে। Redux নির্দিষ্ট Selector মেকানিজম ব্যবহার করে কেবল পরিবর্তিত স্টেট স্লাইস গ্রহণকারী কম্পোনেন্টকেই রি-রেন্ডার করে, ফলে এটি অনেক বেশি পারফরম্যান্ট।

## 11. Best Practices (সেরা অভ্যাসসমূহ)
*   **Rule of Thumb**: যদি অ্যাপের স্টেট অন্তত ৩টি বা তার বেশি লেভেলের কম্পোনেন্ট অতিক্রম করে শেয়ার করতে হয়, তবেই Redux-এর কথা ভাবুন।
*   **Keep Local State Local**: ফর্ম ইনপুট, অ্যানিমেশন স্টেট বা UI টগল স্টেট সবসময় React-এর লোকাল `useState` দিয়েই ম্যানেজ করুন।
*   **Normalize State Structure**: স্টোরের স্টেট স্ট্রাকচারকে জটিল বা নেস্টেড না করে যতোটা সম্ভব ফ্ল্যাট রাখুন।

## 12. Performance Considerations (পারফরম্যান্স সংক্রান্ত বিষয়সমূহ)
Redux-এ প্রতিটি অ্যাকশন ডিসপ্যাচ হওয়ার পর সমস্ত সাবস্ক্রাইবড কম্পোনেন্ট চেক করা হয়। যদি `useSelector` সঠিক উপায়ে লেখা না হয়, তবে স্টোরের যেকোনো পরিবর্তনের কারণে অপ্রয়োজনীয় কম্পোনেন্ট রি-রেন্ডার হতে পারে। পারফরম্যান্স ভালো রাখতে নির্দিষ্ট ডেটা সিলেক্ট করতে হবে এবং জটিল হিসাব-নিকাশের ক্ষেত্রে memoized selectors (যেমন `reselect` লাইব্রেরি) ব্যবহার করতে হবে।

## 13. When NOT to Use It (কখন এটি ব্যবহার করবেন না)
*   যদি প্রজেক্টটি খুব ছোট বা মিডিয়াম সাইজের হয় এবং স্টেট শেয়ারিংয়ের পরিমাণ খুবই কম হয়।
*   যদি আপনি খুব দ্রুত প্রোটোটাইপিং বা MVP (Minimum Viable Product) তৈরি করছেন, যেখানে অতিরিক্ত বয়লারপ্লেট কোড লেখার সময় নেই।
*   যদি অ্যাপ্লিকেশনের বেশিরভাগ স্টেটই লোকাল বা ফর্ম ডেটা ভিত্তিক হয়।

## 14. Comparison with Similar Concepts (অনুরূপ ধারণার সাথে তুলনা)

| Feature | React Local State (useState) | Context API | Redux |
| :--- | :--- | :--- | :--- |
| **Scope** | Local to component | Component Tree Branch | Global App State |
| **Complexity** | Extremely Low | Medium | High (Standard Redux) |
| **Performance** | Excellent for local | Can trigger unnecessary re-renders in large trees | Optimized with selectors |
| **Use Case** | Single component UI states | Theme, Language settings | Complex dashboard, eCommerce cart, User Auth |
| **DevTools Support**| Basic (React DevTools) | Basic | Advanced (Time Travel Debugging) |

## 15. Summary in Simple Bangla (সহজ বাংলায় সারসংক্ষেপ)
Redux হলো একটি কেন্দ্রীয় ড্রয়ার বা গুদামঘর যেখানে অ্যাপের সমস্ত গ্লোবাল ডেটা জমা থাকে। বড় রিঅ্যাক্ট অ্যাপ্লিকেশনে ডেটা পাস করার ঝামেলা (Prop drilling) দূর করতে এবং গ্লোবাল ডেটার ধারাবাহিকতা বজায় রাখতে Redux ব্যবহার করা হয়। তবে ছোট অ্যাপে এটি ব্যবহার করার কোনো প্রয়োজন নেই, রিঅ্যাক্ট-এর লোকাল স্টেটই এর জন্য যথেষ্ট।

## 16. 5 MCQ Questions (৫টি বহুনির্বাচনী প্রশ্ন)
1.  **Which of the following is true about Redux?**
    *   A) Redux can only be used with React.
    *   B) Redux is a predictable state container for JavaScript apps.
    *   C) Redux stores state in multiple separate databases.
    *   D) Redux directly replaces React component state completely.
    *   *Correct Answer: B*
    *   *Explanation:* Redux একটি প্রেডিক্টেবল স্টেট কন্টেইনার এবং এটি যেকোনো জেএস ফ্রেমওয়ার্ক বা ভ্যানিলা জাভাস্ক্রিপ্টের সাথেও কাজ করতে পারে।
2.  **What problem does Redux primarily solve in React applications?**
    *   A) Slow API responses
    *   B) CSS styling management
    *   C) Prop drilling and complex global state sharing
    *   D) HTML rendering speed
    *   *Correct Answer: C*
    *   *Explanation:* Redux ব্যবহারের প্রধান কারণ হলো Prop drilling এবং জটিল গ্লোবাল স্টেট ম্যানেজমেন্টের সমস্যা দূর করা।
3.  **Is Redux mandatory to use in every React application?**
    *   A) Yes, React cannot run without Redux.
    *   B) No, it is optional and only recommended for complex state requirements.
    *   C) Yes, but only in production builds.
    *   D) No, it is only for mobile development.
    *   *Correct Answer: B*
    *   *Explanation:* Redux একটি থার্ড-পার্টি লাইব্রেরি এবং এটি ব্যবহার করা ঐচ্ছিক। ছোট বা মাঝারি অ্যাপে রিঅ্যাক্টের নিজস্ব স্টেটই যথেষ্ট।
4.  **What is a "Single Source of Truth" in the context of Redux?**
    *   A) The DB server hosting the database.
    *   B) The only React component that displays data.
    *   C) The single Redux store containing the entire application state.
    *   D) The API endpoint that returns true values.
    *   *Correct Answer: C*
    *   *Explanation:* Redux-এর একটি প্রধান নীতি হলো অ্যাপের পুরো স্টেটটি একটি মাত্র স্টোর অবজেক্ট ট্রিতে থাকবে, যাকে Single source of truth বলা হয়।
5.  **When should you prefer React's useState over Redux?**
    *   A) For managing global user authentication token.
    *   B) For a simple local form input value.
    *   C) For managing shopping cart items in an e-commerce site.
    *   D) For complex chat application messages.
    *   *Correct Answer: B*
    *   *Explanation:* লোকাল ফর্ম ইনপুট বা টগল স্টেটের মতো জিনিসগুলো রিঅ্যাক্টের লোকাল `useState` দিয়েই হ্যান্ডেল করা উচিত, এতে কোড সহজ থাকে।

## 17. 5 Coding Exercises (৫টি কোডিং অনুশীলন)
1.  **Exercise 1**: Create a simple Counter application layout using standard React `useState` and state lifting-up. Identify the prop drilling.
2.  **Exercise 2**: Write a Redux reducer that manages a simple `theme` state ('light' or 'dark'). Ensure it returns a new state object without mutating the original state.
3.  **Exercise 3**: Simulate a Redux store setup in plain JavaScript using `redux` library, and log the state to console whenever an action is dispatched.
4.  **Exercise 4**: Implement a Redux action structure for adding an item to a shopping cart. The action must carry a payload containing `id`, `name`, and `price`.
5.  **Exercise 5**: Refactor a component that has 3 nested children passing down a user's login state, and explain how a central store would eliminate these props.

---

# Topic 2: What are the Three Core Principles of Redux?

## 1. Simple Definition (সহজ সংজ্ঞা)
Redux-এর তিনটি মূল নীতি (Three Core Principles) হলো সেই মৌলিক নিয়মাবলি যা রিডাক্সের পুরো আর্কিটেকচার এবং ডেটা ফ্লো নিয়ন্ত্রণ করে। এই তিনটি নীতি হলো:
1.  **Single Source of Truth**: অ্যাপ্লিকেশনের পুরো স্টেট একটি একক অবজেক্ট ট্রির মধ্যে একটিমাত্র স্টোরে জমা থাকে।
2.  **State is Read-Only**: স্টেট সরাসরি পরিবর্তন করা যায় না; স্টেট পরিবর্তনের একমাত্র উপায় হলো একটি "Action" ডিসপ্যাচ করা।
3.  **Changes are Made with Pure Functions**: অ্যাকশন কীভাবে স্টেটকে পরিবর্তন করবে তা নির্ধারণ করার জন্য "Reducer" নামক পিউর ফাংশন লিখতে হয়।

## 2. Why This Concept Exists (কেন এই ধারণার উৎপত্তি)
এই নীতিগুলো তৈরি করা হয়েছে যাতে অ্যাপ্লিকেশনের ডেটা ফ্লো অত্যন্ত সুনির্দিষ্ট এবং প্রেডিক্টেবল থাকে। যদি যে কেউ যেকোনো স্থান থেকে স্টেট পরিবর্তন করতে পারত, তবে অ্যাপ্লিকেশন বড় হওয়ার সাথে সাথে ডেটা বাগ খুঁজে বের করা অসম্ভব হয়ে পড়ত।

## 3. What Problem It Solves (এটি কোন সমস্যার সমাধান করে)
*   **Unpredictable State Changes**: বিভিন্ন স্থান থেকে একই সাথে স্টেট পরিবর্তন করার ফলে যে ডাটা রেসিং বা করাপশন তৈরি হয় তা রোধ করে।
*   **Lack of Debugging History**: স্টেট পরিবর্তনের কোনো ইতিহাস না থাকার কারণে টাইম-ট্রাভেল ডিবাগিং বা পূর্ববর্তী স্টেটে ফিরে যাওয়া অসম্ভব হতো। এই নীতিগুলো পরিবর্তনের ইতিহাস ধরে রাখে।
*   **State Mutation Bugs**: শ্যালো কপি বনাম ডিপ কপির কারণে রিঅ্যাক্ট কম্পোনেন্ট রেন্ডার না হওয়ার যে বাগগুলো তৈরি হয়, তা ইমিউটেবিলিটি নিয়মের মাধ্যমে সমাধান করা হয়।

## 4. Real-Life Analogy (বাস্তব জীবনের উদাহরণ)
একটি জমির মালিকানা দলিলের (Land Registry Ledger) কথা ভাবা যাক।
*   **Single Source of Truth**: সরকারি রেজিস্ট্রি office হলো একক সত্যের উৎস। শহরের সকল জমির খতিয়ান ওই একটি নির্দিষ্ট অফিসে সংরক্ষিত থাকে।
*   **State is Read-Only**: আপনি নিজে কলম দিয়ে সরকারি খাতা কেটে আপনার নামে জমি লিখে নিতে পারেন না (State is read-only)। জমি আপনার নামে করতে হলে একটি আনুষ্ঠানিক আবেদন বা দলিল রেজিস্ট্রি (Action) করতে হবে।
*   **Changes are Made with Pure Functions**: সাব-রেজিস্ট্রার (Reducer) নামক নির্দিষ্ট সরকারি কর্মকর্তা নিয়মতান্ত্রিকভাবে সমস্ত কাগজপত্র যাচাই করে কেবল খাতার নতুন পৃষ্ঠায় নতুন মালিকের নাম লিখে সাইন করবেন। তিনি কোনো ব্যক্তিগত খেয়ালখুশি মতো কাজ করতে পারবেন না (Pure function)।

## 5. How React Works Internally Regarding This Concept (এই বিষয়ে React কীভাবে অভ্যন্তরীণভাবে কাজ করে)
React-এর Virtual DOM কম্পারিজন মেকানিজম রিডাক্সের ইমিউটেবিলিটি নীতির সাথে গভীরভাবে সম্পৃক্ত। React যখন দেখে কোনো স্টেটের রেফারেন্স পরিবর্তিত হয়েছে (অর্থাৎ নতুন অবজেক্ট তৈরি হয়েছে), তখন এটি অত্যন্ত দ্রুত শ্যালো কম্পারিজনের মাধ্যমে বুঝতে পারে যে ডেটা চেঞ্জ হয়েছে এবং UI আপডেট করা দরকার। যদি স্টেট মিউটেট করা হতো (`state.user.name = 'Rohit'`), তবে অবজেক্টের মেমরি রেফারেন্স একই থাকত, এবং React-এর Virtual DOM রেন্ডার স্কিপ করে যেত, ফলে স্ক্রিনে নতুন ডাটা দেখা যেত না।

## 6. Basic Example (বেসিক উদাহরণ)

```javascript
// Demonstrating the 3 Principles in Code

// 1. Single Source of Truth: All state in one object
const storeState = {
  user: { name: 'Rohit', role: 'Student' },
  theme: 'dark',
  notifications: []
};

// 2. State is Read-only: We do not modify storeState directly.
// Instead, we define Actions (intent to change)
const loginAction = {
  type: 'auth/login',
  payload: { name: 'Rohit Dev' }
};

// 3. Changes are made with Pure Functions (Reducer)
// This function takes current state and action, and returns a NEW state object.
function appReducer(state = storeState, action) {
  switch (action.type) {
    case 'auth/login':
      // Return a completely new object (Immutability)
      return {
        ...state,
        user: { ...state.user, name: action.payload.name }
      };
    case 'theme/toggle':
      return {
        ...state,
        theme: state.theme === 'dark' ? 'light' : 'dark'
      };
    default:
      return state;
  }
}
```

## 7. Step-by-Step Explanation of the Code (কোডের ধাপে ধাপে ব্যাখ্যা)
*   `storeState` হলো পুরো অ্যাপ্লিকেশনের একমাত্র স্টেট অবজেক্ট (Single source of truth)।
*   `loginAction` হলো একটি প্লেইন অবজেক্ট যার একটি `type` প্রোপার্টি আছে। আমরা সরাসরি `storeState.user.name = 'Rohit Dev'` করিনি, কারণ স্টেট রিড-অনলি।
*   `appReducer` হলো একটি pure function। এটি ইনপুট হিসেবে পাওয়া `state` অবজেক্টের সরাসরি কোনো পরিবর্তন করে না। স্প্রেড অপারেটর (`...state`) ব্যবহার করে এটি আগের প্রোপার্টিগুলো কপি করে এবং শুধুমাত্র `user` প্রোপার্টির ভেতরে নতুন ভ্যালু সেট করে একটি নতুন স্টেট অবজেক্ট রিটার্ন করে।

## 8. Another Real-World Example (আরেকটি বাস্তব উদাহরণ)
Git Version Control System। গিট রিপোজিটরি হলো Single Source of Truth। আপনি সরাসরি গিটের হিস্ট্রি এডিট করতে পারেন না (Read-only)। আপনাকে Commit (Action) করতে হয়। গিট ইন্টারনালি প্রতিটি নতুন কমিটের জন্য একটি নতুন স্ন্যাপশট (Reducer-এর মতো) তৈরি করে আগের স্ন্যাপশটের সাথে লিংক করে দেয়, যার ফলে আপনি যেকোনো সময় আগের যেকোনো রিলিজে টাইম-ট্রাভেল করে ফিরে যেতে পারেন।

## 9. Common Mistakes Beginners Make (নতুনদের করা সাধারণ ভুলসমূহ)
*   **রিডিউসারের ভেতরে সরাসরি স্টেট আপডেট করা**: যেমন `state.user = action.payload` লিখে ফেলা। এটি জাভাস্ক্রিপ্টের রেফারেন্স চেঞ্জ করে না, তাই রিঅ্যাক্ট রি-রেন্ডার হয় না।
*   **রিডিউসারের ভেতরে Side Effects রাখা**: যেমন রিডিউসারের ভেতর এপিআই কল করা (`fetch`), বা `Math.random()`, `new Date()` ব্যবহার করা। এর ফলে একই ইনপুটের জন্য রিডিউসার ভিন্ন ভিন্ন আউটপুট দিতে পারে, যা পিউর ফাংশনের নিয়মের পরিপন্থী।

## 10. Interview Questions Related to This Topic (イイータービューの質問)
1.  **Redux-এর তিনটি মূল নীতি কি কি?**
    *   *উত্তরঃ* Single source of truth, State is read-only, এবং Changes are made with pure functions।
2.  **কেন Redux-এ স্টেট ইমিউটেবল রাখা আবশ্যক?**
    *   *উত্তরঃ* ইমিউটেবিলিটি নিশ্চিত করে যে আগের স্টেট এবং নতুন স্টেটের রেফারেন্স ভিন্ন হবে। এর ফলে React অত্যন্ত দ্রুত শ্যালো কম্পারিজনের মাধ্যমে স্টেট পরিবর্তন বুঝতে পারে এবং UI রেন্ডার করতে পারে।
3.  **পিউর ফাংশন বলতে কি বোঝায় এবং রিডিউসার কেন পিউর হতে হবে?**
    *   *উত্তরঃ* পিউর ফাংশন হলো এমন একটি ফাংশন যা একই ইনপুটের জন্য সবসময় একই আউটপুট দেয় এবং এর কোনো সাইড-ইফেক্ট থাকে না। রিডিউসার পিউর হতে হয় যাতে স্টেট পরিবর্তনসমূহ শতভাগ Predictable এবং ট্র্যাকযোগ্য থাকে।
4.  **"Single source of truth" এর সুবিধা কি?**
    *   *উত্তরঃ* এর সুবিধা হলো পুরো অ্যাপ্লিকেশনের স্টেট একটি মাত্র স্থানে থাকায় ডাটা সিনক্রোনাইজেশন সহজ হয়, ডিবাগ করা সহজ হয় এবং সার্ভার-সাইড রেন্ডারিং সহজেই করা যায়।
5.  **কিভাবে রিডাক্সে ইমিউটেবলি স্টেট আপডেট করা যায়?**
    *   *উত্তরঃ* জাভাস্ক্রিপ্টের Spread Operator (`...`), `Object.assign()`, অথবা `immer` লাইব্রেরি ব্যবহার করে স্টেট আপডেট করা যায়।

## 11. Best Practices (সেরা অভ্যাসসমূহ)
*   **Always return a new object**: রিডিউসার থেকে সবসময় একটি নতুন অবজেক্ট রিটার্ন করুন।
*   **Ensure Deterministic Reducers**: রিডিউসারকে এমনভাবে লিখুন যেন একই স্টেট এবং একই অ্যাকশনের জন্য এটি সবসময় ঠিক একই আউটপুট দেয়।
*   **Use Immer**: স্টেট আপডেট লজিক সহজ করতে `immer` (যা Redux Toolkit-এ বিল্ট-ইন থাকে) ব্যবহার করুন, যাতে ব্যাকগ্রাউন্ডে ইমিউটেবিলিটি বজায় রেখেও মিউটেবল কোড লেখার মতো ফিল পাওয়া যায়।

## 12. Performance Considerations (পারফরম্যান্স সংক্রান্ত বিষয়সমূহ)
রিডিউসারে নতুন স্টেট অবজেক্ট তৈরি করার সময় শ্যালো কপি দ্রুত কাজ করে। কিন্তু অবজেক্ট যদি অতিরিক্ত নেস্টেড হয় এবং আমরা যদি ভুলভাবে পুরো স্টেট স্ট্রাকচারকে ডিপ কপি করতে যাই, তবে বড় অ্যাপ্লিকেশনে মেমরি কনজাম্পশন এবং প্রসেসিং ওভারহেড বেড়ে পারফরম্যান্স কমে যেতে পারে।

## 13. When NOT to Use It (কখন এটি ব্যবহার করবেন না)
যদি অ্যাপ্লিকেশনের স্টেট স্ট্রাকচার অত্যন্ত সিম্পল হয় এবং টাইম-ট্রাভেল ডিবাগিং বা স্টেট ট্র্যাকিংয়ের কঠোরতা আপনার প্রজেক্টের গতি কমিয়ে দেয়, তবে এই নীতিগুলো জোরপূর্বক ইমপ্লিমেন্ট করার প্রয়োজন নেই।

## 14. Comparison with Similar Concepts (অনুরূপ ধারণার সাথে তুলনা)
**Redux Principles vs MVC Pattern**: MVC প্যাটার্নে ডেটা বাই-ডাইরেকশনালি ফ্লো হতে পারে এবং কন্ট্রোলার সরাসরি ভিউ বা মডেলের ডেটা মিউটেট করতে পারে। কিন্তু Redux-এ ডাটা ফ্লো কঠোরভাবে একমুখী এবং স্টেট পরিবর্তনের জন্য পিউর রিডিউসার ও অ্যাকশন ব্যবহারের নিয়ম মানতে হয়।

## 15. Summary in Simple Bangla (সহজ বাংলায় সারসংক্ষেপ)
Redux-এর তিনটি মূল নিয়ম আছে: ১. পুরো অ্যাপের সব ডেটা থাকবে একটা বড় বাক্সে (Store)। ২. এই বাক্স থেকে ডেটা সরাসরি বদলানো যাবে না, বদলাতে হলে একটি রিকোয়েস্ট (Action) পাঠাতে হবে। ৩. এই রিকোয়েস্ট অনুযায়ী বাক্সটি আপডেট করার কাজ করবে একটি সৎ ও নিয়মনিষ্ঠ কর্মচারী (Pure Reducer), যে আগের বাক্স ফেলে দিয়ে ঠিক একই রকম একটি নতুন পরিবর্তিত বাক্স তৈরি করে দেবে।

## 16. 5 MCQ Questions (৫টি বহুনির্বাচনী প্রশ্ন)
1.  **What is the meaning of "Single source of truth" in Redux?**
    *   A) The client sends only one truth query to the API.
    *   B) The state of the entire application is stored in an object tree within a single store.
    *   C) Redux can only have one component.
    *   D) There is only one action creator allowed in the app.
    *   *Correct Answer: B*
    *   *Explanation:* অ্যাপ্লিকেশনের সমস্ত স্টেট একটিমাত্র স্টোরের গ্লোবাল অবজেক্ট ট্রিতে সংরক্ষিত থাকে।
2.  **Why is the state in Redux read-only?**
    *   A) To make sure users cannot view the code.
    *   B) To protect the application from hackers.
    *   C) To ensure predictability and allow tracking of state changes via actions.
    *   D) Because JavaScript doesn't support writing to objects.
    *   *Correct Answer: C*
    *   *Explanation:* স্টেট সরাসরি মিউটেট করা আটকাতে এবং প্রতিটি পরিবর্তনকে অ্যাকশনের মাধ্যমে ট্র্যাক করতে স্টেটকে রিড-অনলি রাখা হয়।
3.  **Which of the following is a characteristic of a "Pure Function" like a Reducer?**
    *   A) It must make API requests to fetch fresh data.
    *   B) It returns different outputs for the same inputs depending on the time of day.
    *   C) It has no side effects and returns the exact same output for the same input arguments.
    *   D) It must mutate the original arguments directly.
    *   *Correct Answer: C*
    *   *Explanation:* পিউর ফাংশন কোনো সাইড-ইফেক্ট তৈরি করে না এবং একই আর্গুমেন্টের জন্য সবসময় একই ফলাফল দেয়।
4.  **What happens if you mutate the Redux state directly (e.g., `state.count = 5`) inside a reducer?**
    *   A) Redux will throw a syntax error immediately.
    *   B) React will not re-render the components because the object reference did not change.
    *   C) The component will render twice.
    *   D) The action will be cancelled automatically.
    *   *Correct Answer: B*
    *   *Explanation:* সরাসরি মিউটেশন করলে অবজেক্ট রেফারেন্স পরিবর্তন হয় না, ফলে রিঅ্যাক্ট বুঝতে পারে না যে স্টেট চেঞ্জ হয়েছে, এবং পেজ রি-রেন্ডার হয় না।
5.  **How are state changes triggered in Redux?**
    *   A) By calling `state.update()`
    *   B) By dispatching an action object
    *   C) By re-rendering the root React component
    *   D) By sending a POST request to the server
    *   *Correct Answer: B*
    *   *Explanation:* Redux-এ স্টেট পরিবর্তনের একমাত্র উপায় হলো `store.dispatch(action)` এর মাধ্যমে একটি অ্যাকশন অবজেক্ট পাঠানো।

## 17. 5 Coding Exercises (৫টি কোডিং অনুশীলন)
1.  **Exercise 1**: Write a function `isPure(a, b)` and demonstrate why a function that reads from a global variable is impure, while a function that only uses its arguments is pure.
2.  **Exercise 2**: Create a state object containing a deeply nested array of objects: `{ user: { profile: { hobbies: ['coding', 'gaming'] } } }`. Write code to safely add a new hobby to the list using the JavaScript spread operator, ensuring the original object is not mutated.
3.  **Exercise 3**: Write a Redux reducer that handles a `USER_LOGOUT` action. Ensure that the returned state is completely empty or reset to initial default values.
4.  **Exercise 4**: Use `Object.freeze` to make a mock state object immutable, and show how attempting to mutate it throws an error in strict mode.
5.  **Exercise 5**: Design a custom utility function `shallowCompare(objA, objB)` that checks if two state objects have the same reference or if their top-level keys have different values.

---

# Topic 3: What are the Primary Components of Redux? (Store, Actions, Reducers)

## 1. Simple Definition (সহজ সংজ্ঞা)
Redux-এর তিনটি প্রধান গাঠনিক উপাদান (Primary Components) হলো **Store**, **Actions**, এবং **Reducers**।
*   **Store**: এটি হলো অ্যাপ্লিকেশনের সেন্ট্রাল ডাটাবেস বা স্টেট হোল্ডার, যেখানে অ্যাপের সম্পূর্ণ স্টেট অবজেক্ট সংরক্ষিত থাকে।
*   **Actions**: এটি হলো একটি প্লেইন জাভাস্ক্রিপ্ট অবজেক্ট যা নির্দেশ করে অ্যাপ্লিকেশনে কী ঘটেছে (এটি ডেটা বা ইনটেনশন বহন করে)।
*   **Reducers**: এটি হলো একটি pure function যা বর্তমান স্টেট এবং অ্যাকশন গ্রহণ করে নতুন একটি স্টেট রিটার্ন করে।

## 2. Why This Concept Exists (কেন এই ধারণার উৎপত্তি)
দায়িত্ব বিভাজন বা Separation of Concerns নিশ্চিত করার জন্য এই তিনটি উপাদান তৈরি করা হয়েছে। স্টেট হোল্ডিং (Store), পরিবর্তনের উদ্দেশ্য প্রকাশ (Action), এবং পরিবর্তনের আসল হিসাব-নিকাশ (Reducer) - এই তিনটি কাজ আলাদা থাকলে কোডবেস অনেক মডুলার, মেইনটেইনেবল এবং ইউনিট টেস্ট করার উপযোগী হয়।

## 3. What Problem It Solves (এটি কোন সমস্যার সমাধান করে)
*   **Spaghetti Code**: স্টেট আপডেটের লজিক যদি সরাসরি ভিউ কম্পোনেন্টের ভেতরে ছড়ানো-ছিটানো থাকত, তবে প্রজেক্ট বড় হওয়ার সাথে সাথে কোড জটিল হয়ে যেত। এই তিনটি উপাদান ডেটা আপডেট করার ফ্লোকে একটি নির্দিষ্ট প্যাটার্নে আবদ্ধ করে।
*   **Lack of Transparency**: সিস্টেমে ঠিক কী কী ধরনের পরিবর্তন সম্ভব তা আগে থেকে জানা যায় না। Actions-এর মাধ্যমে সমস্ত সম্ভাব্য ইভেন্ট ডিফাইন থাকায়システムের কাজের ধারা স্বচ্ছ হয়।
*   **Difficult State Testing**: লজিককে কম্পোনেন্ট থেকে আলাদা করে Reducers-এ রাখায়, ভিজ্যুয়াল কম্পোনেন্ট ছাড়াই ব্যাকগ্রাউন্ডে স্টেট লজিক টেস্ট করা যায়।

## 4. Real-Life Analogy (বাস্তব জীবনের উদাহরণ)
একটি রেস্টুরেন্টের অর্ডার প্রসেসের সাথে তুলনা করা যাক:
*   **Store**: রেস্টুরেন্টের কিচেন এবং প্যান্ট্রি (Kitchen Pantry), যেখানে সব খাবার ও কাঁচামাল সংরক্ষিত থাকে।
*   **Actions**: ওয়েটারের লিখে নেওয়া অর্ডার স্লিপ (যেমন: `type: 'ORDER_FOOD', payload: { item: 'Pasta', quantity: 1 }`)। এটি রান্নাঘরের আইটেম পরিবর্তন করার জন্য একটি লিখিত সিগন্যাল।
*   **Reducers**: রেস্টুরেন্টের শেফ (Chef) বা রাঁধুনি। শেফ অর্ডার স্লিপ (Action) দেখেন এবং প্যান্ট্রি থেকে কাঁচামাল (Current State) নিয়ে রেসিপি অনুযায়ী রান্না করে একটি নতুন সুস্বাদু ডিশ (Next State) তৈরি করেন। শেফ নিজের ইচ্ছামতো উপাদান পরিবর্তন করতে পারেন না, অর্ডার অনুযায়ীই তাকে খাবার বানাতে হয়।

## 5. How React Works Internally Regarding This Concept (এই বিষয়ে React কীভাবে অভ্যন্তরীণভাবে কাজ করে)
React-redux লাইব্রেরি ব্যবহার করে যখন আমরা React-এর সাথে Redux ইন্টিগ্রেট করি:
*   React কম্পোনেন্টগুলো `useSelector` হুকের মাধ্যমে Store-এর নির্দিষ্ট অংশে চোখ রাখে (Subscribe করে)।
*   কোনো ইউজার অ্যাক্টিভিটির কারণে কম্পোনেন্ট `useDispatch` হুক ব্যবহার করে একটি Action পাঠায় Store-এর কাছে।
*   Store তখন সেই Action-টি Reducer-এর কাছে পাঠায়।
*   Reducer নতুন State অবজেক্ট রিটার্ন করলে Store তার ইন্টারনাল স্টেট আপডেট করে এবং রিঅ্যাক্ট-রেডক্সকে জানায়।
*   রিঅ্যাক্ট-রেডক্স দেখে যে নতুন স্টেটের মান আগের স্টেটের চেয়ে আলাদা কি না। আলাদা হলে সেটি সংশ্লিষ্ট কম্পোনেন্টকে রি-রেন্ডার করায়।

## 6. Basic Example (বেসিক উদাহরণ)

```javascript
import { createStore } from 'redux';

// 1. Initial State
const initialTodoState = {
  todos: []
};

// 2. Action Creators (Helper functions to create action objects)
const addTodo = (text) => {
  return {
    type: 'todos/add',
    payload: { id: Date.now(), text: text, completed: false }
  };
};

const toggleTodo = (id) => {
  return {
    type: 'todos/toggle',
    payload: id
  };
};

// 3. Reducer
function todosReducer(state = initialTodoState, action) {
  switch (action.type) {
    case 'todos/add':
      return {
        ...state,
        todos: [...state.todos, action.payload]
      };
    case 'todos/toggle':
      return {
        ...state,
        todos: state.todos.map(todo => 
          todo.id === action.payload 
            ? { ...todo, completed: !todo.completed } 
            : todo
        )
      };
    default:
      return state;
  }
}

// 4. Store
const store = createStore(todosReducer);

// Test Dispatching Actions
console.log('Initial state:', store.getState());

store.dispatch(addTodo('Learn Redux Architecture'));
console.log('After add:', store.getState());

const todoId = store.getState().todos[0].id;
store.dispatch(toggleTodo(todoId));
console.log('After toggle:', store.getState());
```

## 7. Step-by-Step Explanation of the Code (কোডের ধাপে ধাপে ব্যাখ্যা)
*   `initialTodoState` একটি অ্যারে নিয়ে শুরু হয় যা শূন্য টাস্ক নির্দেশ করে।
*   `addTodo` এবং `toggleTodo` হলো Action Creators। এরা সরাসরি প্লেইন অবজেক্ট রিটার্ন করে। এটি কোড ডুপ্লিকেশন কমায়।
*   `todosReducer` ফাংশনটি ইনপুট স্টেট অবজেক্টের সরাসরি পরিবর্তন না করে স্প্রেড অপারেটর এবং `map` ফাংশন ব্যবহার করে ইমিউটেবল উপায়ে নতুন অ্যারে এবং অবজেক্ট রিটার্ন করে।
*   `createStore` ফাংশনটি রিডিউসারকে ইনপুট হিসেবে নিয়ে একটি গ্লোবাল স্টোর অবজেক্ট তৈরি করে।
*   `store.dispatch()` অ্যাকশন অবজেক্টকে রিডিউসারের কাছে পাস করে স্টেট পরিবর্তন ঘটায় এবং `store.getState()` দিয়ে পরিবর্তিত স্টেট প্রিন্ট করা হয়।

## 8. Another Real-World Example (আরেকটি বাস্তব উদাহরণ)
ট্রাভেল বুকিং সিস্টেম (Flight booking)।
*   **Store**: বুকিংয়ের যাবতীয় তথ্য (যাত্রীর নাম, সীট নম্বর, ফ্লাইট স্ট্যাটাস)।
*   **Actions**: সীট বুক করা (`BOOK_SEAT`), সীট ক্যানসেল করা (`CANCEL_SEAT`), বা সময় পরিবর্তন করা (`RESCHEDULE_FLIGHT`)।
*   **Reducer**: বুকিং ম্যানেজার সফটওয়্যার, যা নতুন ট্রানজেকশন অনুযায়ী নতুন সীট অ্যালোকেশন প্রসেস করে বুকিং লিস্ট আপডেট করে।

## 9. Common Mistakes Beginners Make (নতুনদের করা সাধারণ ভুলসমূহ)
*   **একাধিক Store তৈরি করা**: Redux অ্যাপে একটির বেশি স্টোর থাকা উচিত নয়। যদি একাধিক স্টেট টাইপ থাকে, তবে `combineReducers` ব্যবহার করে রিডিউসারগুলোকে একত্র করে একটি সিঙ্গেল স্টোর বানাতে হবে।
*   **Reducer-এর ভেতরে API Fetch করা**: রিডিউসার একটি পিউর ফাংশন। এপিআই কল করার মতো অ্যাসিনক্রোনাস কাজ কখনই রিডিউসারের ভেতরে করা যাবে না। এর জন্য Redux Middleware (যেমন Thunk) ব্যবহার করতে হবে।
*   **Action Type বানান ভুল করা**: অ্যাকশন টাইপ স্ট্রিং সরাসরি লেখার কারণে টাইপো (spelling mistake) হওয়ার সম্ভাবনা থাকে, যার ফলে রিডিউসার কাজ করে না। তাই অ্যাকশন টাইপগুলোকে কনস্ট্যান্ট ভেরিয়েবলে ডিফাইন করা উচিত।

## 10. Interview Questions Related to This Topic (ইন্টারভিউয়ের প্রশ্নসমূহ)
1.  **Redux Store-এর প্রধান দায়িত্বগুলো কি কি?**
    *   *উত্তরঃ* গ্লোবাল স্টেট ধরে রাখা, `getState()`-এর মাধ্যমে স্টেট অ্যাক্সেস দেওয়া, `dispatch(action)`-এর মাধ্যমে স্টেট আপডেট করার সুযোগ দেওয়া, এবং `subscribe(listener)`-এর মাধ্যমে লিসেনার রেজিস্টার করা।
2.  **Action Creator কি এবং র অ্যাকশন অবজেক্টের চেয়ে এটি কেন বেশি গ্রহণযোগ্য?**
    *   *উত্তরঃ* Action Creator হলো একটি ফাংশন যা অ্যাকশন অবজেক্ট রিটার্ন করে। এটি ব্যবহার করলে কোড ডুপ্লিকেশন কমে এবং অ্যাকশনের পে-লোড পরিবর্তন করা সহজ হয়।
3.  **large Redux অ্যাপ্লিকেশনে `combineReducers` কিভাবে সাহায্য করে?**
    *   *উত্তরঃ* এটি বড় অ্যাপের বিভিন্ন রিডিউসারকে (যেমন: userReducer, productReducer) একত্র করে একটি সিঙ্গেল রুট রিডিউসার তৈরি করে যা স্টোরে পাস করা যায়।
4.  **রিডিউসার যদি `undefined` রিটার্ন করে তবে কি ঘটবে?**
    *   *উত্তরঃ* Redux একটি এরর থ্রো করবে। রিডিউসারকে সবসময় বর্তমান স্টেট অথবা একটি নতুন স্টেট রিটার্ন করতে হবে।
5.  **React-Redux ব্যবহার করে একটি React কম্পোনেন্ট থেকে কিভাবে Store-কে ব্যবহার করা হয়?**
    *   *উত্তরঃ* `useSelector` হুকের মাধ্যমে স্টোর থেকে স্টেট রিড করা হয় এবং `useDispatch` হুকের মাধ্যমে অ্যাকশন ডিসপ্যাচ করা হয়।

## 11. Best Practices (সেরা অভ্যাসসমূহ)
*   **Define Action Types as Constants**: অ্যাকশন টাইপগুলোকে একটি ফাইলে কনস্ট্যান্ট হিসেবে ডিক্লেয়ার করে রাখুন (যেমন: `const ADD_TODO = 'ADD_TODO';`)।
*   **Use Action Creators**: অ্যাকশন অবজেক্ট ডিসপ্যাচ করার সময় সরাসরি অবজেক্ট না লিখে অ্যাকশন ক্রিয়েটর ফাংশন ব্যবহার করুন।
*   **Keep Reducers Simple**: রিডিউসারের ভেতরে জটিল বিজনেস লজিক না রেখে সেটিকে কেবল স্টেট কপি ও পরিবর্তনের কাজে সীমাবদ্ধ রাখুন।

## 12. Performance Considerations (পারফরম্যান্স সংক্রান্ত বিষয়সমূহ)
বড় প্রজেক্টে স্টেট সাইজ অনেক বড় হলে রিডিউসারের ভেতর অ্যারে ও অবজেক্টের নেস্টিং কমানো উচিত। নেস্টেড অবজেক্টের শ্যালো কপি করার সময় পারফরম্যান্স ইমপ্যাক্ট পড়তে পারে, তাই স্টেট স্ট্রাকচারকে নরমাল বা ফ্ল্যাট রাখা অত্যন্ত জরুরি।

## 13. When NOT to Use It (কখন এটি ব্যবহার করবেন না)
যদি অ্যাপে স্টেট পরিবর্তনের ধরন খুব কম হয় এবং ডাটা ফ্লো জটিল না হয়, তবে এই ৩টি আলাদা উপাদান তৈরি করতে যাওয়া অপ্রয়োজনীয় ওভারহেড সৃষ্টি করবে।

## 14. Comparison with Similar Concepts (অনুরূপ ধারণার সাথে তুলনা)
**Redux Components vs useReducer Hook**: React-এর `useReducer` এবং Redux রিডিউসারের কাজের ধরন প্রায় একই। তবে `useReducer` কেবল একটি নির্দিষ্ট কম্পোনেন্ট বা তার চাইল্ড ব্রাঞ্চের লোকাল স্টেট ম্যানেজ করে এবং এতে কোনো গ্লোবাল স্টোর বা মিডলওয়্যার ইন্টিগ্রেশন থাকে না। অন্যদিকে Redux Store একটি গ্লোবাল এন্টারপ্রাইজ লেভেল স্টেট সলিউশন।

## 15. Summary in Simple Bangla (সহজ বাংলায় সারসংক্ষেপ)
Redux-এর তিনটি প্রধান ভাগ আছে। ১. **Store**: যেখানে সব ডেটা জমা থাকে। ২. **Action**: একটি চিরকুট যা বলে যে কী কাজ করতে হবে এবং এর সাথে কী ডেটা লাগবে। ৩. **Reducer**: একজন বাবুর্চি যে এই চিরকুট দেখে স্টোরের ডেটা ব্যবহার করে নতুন একটি স্টেট তৈরি করে।

## 16. 5 MCQ Questions (৫টি বহুনির্বাচনী প্রশ্ন)
1.  **Which Redux component is responsible for holding the application state?**
    *   A) Action
    *   B) Reducer
    *   C) Store
    *   D) Middleware
    *   *Correct Answer: C*
    *   *Explanation:* Redux Store অ্যাপ্লিকেশনের সম্পূর্ণ স্টেট অবজেক্ট ধরে রাখে।
2.  **What is the role of an Action in Redux?**
    *   A) It executes database queries.
    *   B) It is a plain JavaScript object that describes the change you want to make.
    *   C) It updates the browser DOM directly.
    *   D) It connects the store to the API.
    *   *Correct Answer: B*
    *   *Explanation:* Action হলো একটি প্লেইন অবজেক্ট যা কী পরিবর্তন করতে হবে তা বর্ণনা করে।
3.  **A Reducer in Redux is defined as:**
    *   A) An asynchronous function to fetch data.
    *   B) A middleware that logs actions.
    *   C) A pure function that takes the current state and an action, and returns the next state.
    *   D) A React component that renders UI.
    *   *Correct Answer: C*
    *   *Explanation:* Reducer হলো একটি পিউর ফাংশন যা কারেন্ট স্টেট এবং অ্যাকশন নিয়ে নতুন স্টেট রিটার্ন করে।
4.  **How many stores should a standard Redux application have?**
    *   A) One store per component
    *   B) Exactly one global store
    *   C) Two stores: one for local, one for global
    *   D) A separate store for each reducer
    *   *Correct Answer: B*
    *   *Explanation:* Redux-এর একক সত্যের উৎস নীতি অনুযায়ী পুরো অ্যাপের জন্য একটি মাত্র গ্লোবাল স্টোর থাকা উচিত।
5.  **What will happen if you do not specify a default case in a Redux Reducer switch statement?**
    *   A) Redux will crash.
    *   B) The state will remain unchanged automatically.
    *   C) The state could become `undefined` if an unrecognized action is dispatched.
    *   D) The action will be resent.
    *   *Correct Answer: C*
    *   *Explanation:* যদি ডিফল্ট কেস না থাকে এবং কোনো ম্যাচ না পাওয়া অ্যাকশন আসে, তবে রিডিউসার কিছু রিটার্ন করবে না, যার ফলে স্টেট `undefined` হয়ে যাবে।

## 17. 5 Coding Exercises (৫টি কোডিং অনুশীলন)
1.  **Exercise 1**: Create a reducer `userReducer` that handles actions `SET_USER_NAME` and `CLEAR_USER` with appropriate payloads.
2.  **Exercise 2**: Write a store configuration from scratch using `redux` library and add a custom subscriber that logs `Current Balance: {balance}` to the console.
3.  **Exercise 3**: Write an Action Creator `deleteTodo(todoId)` that returns the proper action structure to delete a todo.
4.  **Exercise 4**: Combine two reducers `authReducer` and `cartReducer` using Redux's `combineReducers` helper function.
5.  **Exercise 5**: Simulate a manual dispatch of three consecutive actions to a mock store and print the final state object structure.

---

# Topic 4: Why are Redux and React Separate Libraries?

## 1. Simple Definition (সহজ সংজ্ঞা)
React এবং Redux সম্পূর্ণ দুটি ভিন্ন এবং স্বাধীন লাইব্রেরি। React হলো একটি **UI Rendering Library (View Layer)**, যার কাজ হলো স্ক্রিনে ডেটা রেন্ডার করা এবং ইউজার ইন্টারঅ্যাকশন হ্যান্ডেল করা। আর Redux হলো একটি **State Management Container**, যার কাজ হলো কোনো নির্দিষ্ট ফ্রেমওয়ার্কের ওপর নির্ভর না করে পিউর জাভাস্ক্রিপ্ট অ্যাপ্লিকেশনের স্টেট ম্যানেজ করা। এই দুটি লাইব্রেরিকে একসাথে যুক্ত করার জন্য **React-Redux** নামক একটি সংযোগকারী (binding) লাইব্রেরি ব্যবহার করা হয়।

## 2. Why This Concept Exists (কেন এই ধারণার উৎপত্তি)
এই ডিজাইনগত বিভাজনটি তৈরি করা হয়েছে **Universal State Management** এবং **Decoupling (লজিক ও ভিউ আলাদা করা)** নিশ্চিত করার জন্য। যদি Redux সরাসরি React-এর অংশ হতো, তবে আমরা এটিকে অন্য কোনো লাইব্রেরি যেমন Angular, Vue, বা Node.js-এর ব্যাকএন্ড সার্ভারে গ্লোবাল স্টেট ম্যানেজ করতে ব্যবহার করতে পারতাম না। এছাড়া, এর ফলে প্রেজেন্টেশনাল লজিক (UI) এবং বিজনেস লজিক (State) সম্পূর্ণ আলাদা থাকে।

## 3. What Problem It Solves (এটি কোন সমস্যার সমাধান করে)
*   **Framework Lock-in**: কোনো নির্দিষ্ট ফ্রেমওয়ার্কের সাথে কোড লক হয়ে যাওয়া রোধ করে। আপনি চাইলে পরবর্তীতে ভিউ লেয়ার React থেকে সলিড বা অন্য কোনো ফ্রেমওয়ার্কে পরিবর্তন করলেও আপনার মূল Redux স্টেট লজিক অবিকৃত রাখতে পারবেন।
*   **Untestable UI Bindings**: স্টেট লজিক টেস্ট করতে রিঅ্যাক্ট কম্পোনেন্ট মাউন্ট করার ঝামেলা পোহাতে হতো। কিন্তু আলাদা হওয়ার কারণে পিউর জাভাস্ক্রিপ্ট দিয়েই লজিক টেস্ট করা যায়।
*   **Bloated React Core**: React লাইব্রেরির সাইজ অযথা বড় হওয়া থেকে রক্ষা করে। যারা গ্লোবাল স্টেট চান না, তারা রিঅ্যাক্ট ব্যবহার করেই হালকা ও দ্রুত অ্যাপ বানাতে পারেন।

## 4. Real-Life Analogy (বাস্তব জীবনের উদাহরণ)
একটি ইউনিভার্সাল ডকিং স্টেশন বা চার্জার এবং একটি スマートフォン (স্মার্টফোন)-এর কথা ভাবা যাক।
*   **React**: আপনার স্মার্টফোন স্ক্রিন ও বডি (যা ব্যবহারকারীর সাথে ভিজ্যুয়ালি ইন্টারঅ্যাক্ট করে)।
*   **Redux**: একটি বড় পাওয়ার ব্যাংক বা চার্জার গ্রিড (যা বিদ্যুৎ/স্টেট স্টোর করে রাখে)।
*   **React-Redux**: চার্জিং কেবল বা ডকিং জ্যাক যা পাওয়ার ব্যাংক থেকে কারেন্ট এনে ফোনে ইনপুট দেয়। পাওয়ার ব্যাংকটি সম্পূর্ণ স্বাধীন; এটি ফোন ছাড়াও আইপ্যাড, ক্যামেরা বা স্পিকার চার্জ করতে পারে। ফোন এবং পাওয়ার ব্যাংক যদি ফিক্সড বা বিল্ট-ইন থাকতো, তবে যেকোনো একটি নষ্ট হলে অন্যটি ফেলে দিতে হতো।

## 5. How React Works Internally Regarding This Concept (এই বিষয়ে React কীভাবে অভ্যন্তরীণভাবে কাজ করে)
React নিজের ভেতরে রেন্ডার ট্রি এবং রিঅ্যাক্টিভ লাইফসাইকেল চালায়। Redux-এর নিজস্ব ডাটা চেঞ্জ মেকানিজম রয়েছে। React-Redux লাইব্রেরি এই দুটির মধ্যে সংযোগ ঘটায়। এটি মূলত React-এর `Context API` ব্যবহার করে। `Provider` কম্পোনেন্টটি Redux store-কে পুরো রিঅ্যাক্ট কম্পোনেন্ট ট্রির কাছে ভিজিবল করে তোলে। যখন কোনো কম্পোনেন্টে `useSelector` ব্যবহার করা হয়, রিঅ্যাক্ট-রেডক্স সেই কম্পোনেন্টকে Redux store-এর একটি লিসেনার (listener) হিসেবে রেজিস্টার করে। যখনই স্টোরে কোনো অ্যাকশন ডিসপ্যাচ হয় এবং সিলেক্ট করা ডেটার মান পরিবর্তিত হয়, React-Redux ইন্টারনালি রিঅ্যাক্টের একটি ফোর্স আপডেট বা ইন্টারনাল স্টেট সেট করে কম্পোনেন্টটিকে রি-রেন্ডার করতে বাধ্য করে।

## 6. Basic Example (বেসিক উদাহরণ)

```javascript
// Part 1: Redux works COMPLETELY independent of React (Vanilla JavaScript)
const { createStore } = require('redux');

const counterReducer = (state = { count: 0 }, action) => {
  if (action.type === 'increment') return { count: state.count + 1 };
  return state;
};

// Pure Redux Store (No React dependency here)
const store = createStore(counterReducer);
const unsubscribe = store.subscribe(() => console.log('Redux State:', store.getState()));
store.dispatch({ type: 'increment' });
unsubscribe();


// Part 2: Connecting it to React using 'react-redux' bindings
import React from 'react';
import { Provider, useSelector, useDispatch } from 'react-redux';

export function CounterApp() {
  const count = useSelector(state => state.count);
  const dispatch = useDispatch();

  return (
    <div>
      <h1>Count: {count}</h1>
      <button onClick={() => dispatch({ type: 'increment' })}>Increment</button>
    </div>
  );
}

// Wrapping React App with Provider to pass the Redux Store
// Usage in root index.js:
// <Provider store={store}>
//   <CounterApp />
// </Provider>
```

## 7. Step-by-Step Explanation of the Code (কোডের ধাপে ধাপে ব্যাখ্যা)
*   **Part 1**: আমরা দেখতে পাচ্ছি যে `redux` লাইব্রেরি থেকে `createStore` ইম্পোর্ট করে একটি স্টোর ও রিডিউসার তৈরি করা হয়েছে। এখানে রিঅ্যাক্টের কোনো অস্তিত্ব বা ফাইল ইম্পোর্ট নেই। এটি নোড বা ব্রাউজারে সরাসরি চলতে পারে।
*   **Part 2**: রিঅ্যাক্ট অ্যাপে এই স্বাধীন স্টোরকে ব্যবহারের জন্য আমরা `react-redux` থেকে `Provider`, `useSelector` এবং `useDispatch` নিয়ে এসেছি।
*   `<Provider store={store}>` রিঅ্যাক্ট অ্যাপের রুটে বসে স্টোরটিকে নিচে ছড়িয়ে দেয়।
*   `useSelector` এর মাধ্যমে রিঅ্যাক্ট কম্পোনেন্ট স্টোরের নির্দিষ্ট `count` স্টেটটি সাবস্ক্রাইব করে।
*   `useDispatch` হুক রিঅ্যাক্ট বাটন ক্লিকের সাথে রিডাক্সের গ্লোবাল ডিসপ্যাচ কানেক্ট করে।

## 8. Another Real-World Example (আরেকটি বাস্তব উদাহরণ)
ক্রস-প্ল্যাটফর্ম ডেক্সটপ ও মোবাইল অ্যাপ্লিকেশন। আপনার কোম্পানির একটি মূল বিজনেস লজিক কোডবেস (Redux Store ও Reducer) আছে যা প্লেইন জাভাস্ক্রিপ্টে লেখা। এটি একই সাথে Electron দিয়ে তৈরি উইন্ডোজ অ্যাপ (React UI), React Native দিয়ে তৈরি মোবাইল অ্যাপ, এবং একটি ওয়েবসাইট (React Web) - তিন জায়গাতেই রিউজ করা হচ্ছে। আলাদা হওয়ার কারণে একই স্টেট লজিক সব জায়গায় সমানভাবে খাপ খাইয়ে যায়।

## 9. Common Mistakes Beginners Make (নতুনদের করা সাধারণ ভুলসমূহ)
*   **ইম্পোর্ট গোলমাল করা**: `redux` এবং `react-redux` এর মধ্যে গুলিয়ে ফেলা। যেমন: `useSelector` বা `Provider` সরাসরি `redux` লাইব্রেরি থেকে ইম্পোর্ট করার চেষ্টা করা, যা ত্রুটি ঘটাবে।
*   **Provider দিতে ভুলে যাওয়া**: রুটে `<Provider store={store}>` দিয়ে র‍্যাপ না করেই সরাসরি চাইল্ড কম্পোনেন্টে `useSelector` ব্যবহার করা, যার ফলে "Could not find react-redux context value" এরর আসে।
*   **মনে করা Redux কেবল React-এর অংশ**: ইন্টারভিউতে বা প্রজেক্টে এই ধারণা রাখা যে Redux ছাড়া React বা React ছাড়া Redux অচল।

## 10. Interview Questions Related to This Topic (ইন্টারভিউয়ের প্রশ্নসমূহ)
1.  **কেন React এবং Redux আলাদা লাইব্রেরি?**
    *   *উত্তরঃ* Redux-কে UI-agnostic রাখা হয়েছে যাতে এটি অন্য ফ্রেমওয়ার্কেও ব্যবহার করা যায় এবং বিজনেস লজিককে ভিউ লেয়ার থেকে বিচ্ছিন্ন রাখা যায়।
2.  **react-redux লাইব্রেরির কাজ কী?**
    *   *উত্তরঃ* এটি React এবং Redux-এর মধ্যে সংযোগ স্থাপন করে। এটি রিঅ্যাক্ট কম্পোনেন্টকে রিডাক্স স্টোরে সাবস্ক্রাইব করার এবং অ্যাকশন ডিসপ্যাচ করার সুবিধা দেয়।
3.  **React-Redux-এ `Provider` কম্পোনেন্টটি কীভাবে ব্যাকগ্রাউন্ডে কাজ করে?**
    *   *উত্তরঃ* এটি React-এর Context API ব্যবহার করে পুরো রিঅ্যাক্ট কম্পোনেন্ট ট্রিতে Redux Store অবজেক্টটি পৌঁছে দেয়।
4.  **React-Redux কীভাবে স্টোর আপডেট অপ্টিমাইজ করে?**
    *   *উত্তরঃ* এটি ইন্টারনালি শ্যালো কম্পারিজনের মাধ্যমে নিশ্চিত করে যে শুধুমাত্র সেই কম্পোনেন্টগুলোই রি-রেন্ডার হবে যেগুলোর সিলেক্টেড ডাটা পরিবর্তিত হয়েছে।
5.  **Angular বা Vue অ্যাপ্লিকেশনে কি Redux ব্যবহার করা যায়?**
    *   *উত্তরঃ* হ্যাঁ, যায়। যেমন Angular-এর জন্য `@ngrx/store` অথবা Vue-এর জন্য `Vuex` বা প্লেইন Redux সরাসরি ব্যবহার করা যায়।

## 11. Best Practices (সেরা অভ্যাসসমূহ)
*   **Decouple Logic**: রিডাক্সের অ্যাকশন এবং রিডিউসার ফাইলে কোনো রিঅ্যাক্ট বা UI সংক্রান্ত কোড (যেমন JSX, Ref বা React Hooks) রাখবেন না।
*   **Use Official Bindings**: রিঅ্যাক্ট অ্যাপে সবসময় অফিশিয়াল `react-redux` লাইব্রেরি এবং এর হুকস (`useSelector`, `useDispatch`) ব্যবহার করুন।
*   **Keep Action Payloads UI-Agnostic**: অ্যাকশন পেলোডে পাঠানো ডাটা যেন কোনো নির্দিষ্ট UI কম্পোনেন্ট ফরম্যাটের ওপর নির্ভর না করে, তা যেন প্লেইন জেএস ডাটা হয়।

## 12. Performance Considerations (পারফরম্যান্স সংক্রান্ত বিষয়সমূহ)
React-Redux ইন্টারনালি সিলেক্টর কম্পারিজনের জন্য কড়া অপ্টিমাইজেশন ব্যবহার করে। এটি শ্যালো ইকুয়ালিটি চেক করে। যদি আমরা `useSelector` এর ভেতরে প্রতিবার নতুন অবজেক্ট রিটার্ন করি (যেমন: `useSelector(state => ({ count: state.count }))`), তবে শ্যালো ইকুয়ালিটি ফেল করবে এবং প্রতি অ্যাকশনে কম্পোনেন্ট অপ্রয়োজনীয়ভাবে রি-রেন্ডার হবে। তাই সিলেক্টর যতোটা সম্ভব স্পেসিফিক হতে হবে।

## 13. When NOT to Use It (কখন এটি ব্যবহার করবেন না)
যদি আপনি রিঅ্যাক্ট ছাড়া অন্য কোনো ভিউ ইঞ্জিন ভবিষ্যতে ব্যবহার করার কথা একেবারেই না ভাবেন এবং রিঅ্যাক্ট-এর নিজস্ব Context API বা `useReducer` আপনার সমস্ত গ্লোবাল স্টেট চাহিদা মেটাতে সক্ষম হয়, তবে অতিরিক্ত `react-redux` বাইন্ডিং লেয়ার যোগ করার প্রয়োজন নেই।

## 14. Comparison with Similar Concepts (অনুরূপ ধারণার সাথে তুলনা)
**React-Redux vs Svelte Stores**: Svelte-এ স্টেট ম্যানেজমেন্ট সরাসরি ফ্রেমওয়ার্কের ভেতরেই বিল্ট-ইন থাকে, কোনো আলাদা সংযোগকারী লাইব্রেরির প্রয়োজন হয় না। অন্যদিকে React এবং Redux আলাদা হওয়ায় `react-redux` নামক সংযোগকারী সেতুর সাহায্য নিতে হয়।

## 15. Summary in Simple Bangla (সহজ বাংলায় সারসংক্ষেপ)
React হলো স্ক্রিনে জিনিসপত্র দেখানোর জন্য (UI), আর Redux হলো ডেটা জমা রাখার জন্য (State)। এরা দুজন আলাদা কোম্পানির প্রোডাক্ট। এদেরকে একসাথে জুড়ে দিয়ে বন্ধুত্ব করানোর জন্য মাঝখানে একটি তার বা মিডলম্যান লাগে, যার নাম হলো `react-redux`।

## 16. 5 MCQ Questions (৫টি বহুনির্বাচনী প্রশ্ন)
1.  **Why are Redux and React packaged as separate libraries?**
    *   A) Because Redux was created before JavaScript was invented.
    *   B) To allow Redux to be used with other frameworks like Angular or Vue, keeping it UI-agnostic.
    *   C) React is written in C++ while Redux is written in Python.
    *   D) To force developers to purchase separate licenses.
    *   *Correct Answer: B*
    *   *Explanation:* Redux-কে UI-agnostic বা যেকোনো ফ্রেমওয়ার্ক স্বাধীন রাখার জন্য আলাদা লাইব্রেরি হিসেবে ডিজাইন করা হয়েছে।
2.  **Which library is required to connect a React application with Redux?**
    *   A) redux-saga
    *   B) react-router
    *   C) react-redux
    *   D) redux-thunk
    *   *Correct Answer: C*
    *   *Explanation:* React এবং Redux-এর মধ্যে যোগাযোগ স্থাপনের অফিশিয়াল লাইব্রেরি হলো `react-redux`।
3.  **What will happen if you use Redux hooks without wrapping the app in `<Provider>`?**
    *   A) The app will run, but run very slowly.
    *   B) The application will throw an error saying it cannot find react-redux context.
    *   C) React will automatically create a default provider.
    *   D) The store will lose all its data.
    *   *Correct Answer: B*
    *   *Explanation:* Provider না থাকলে `react-redux` হুকগুলো স্টোরের কনটেক্সট খুঁজে পায় না এবং এরর দেয়।
4.  **Which React-Redux hook is used to extract data from the Redux store state?**
    *   A) useDispatch
    *   B) useStore
    *   C) useSelector
    *   D) useReducer
    *   *Correct Answer: C*
    *   *Explanation:* `useSelector` হুকের মাধ্যমে স্টোর থেকে সুনির্দিষ্ট স্টেট রিড বা এক্সট্রাক্ট করা হয়।
5.  **How does React-Redux know when to trigger a re-render of a component?**
    *   A) It polls the store every 10 milliseconds.
    *   B) It subscribes to the store and compares the selected state slice values using shallow equality check.
    *   C) It re-renders the component only when the user clicks a button.
    *   D) It re-renders everything in the app on every event automatically.
    *   *Correct Answer: B*
    *   *Explanation:* React-Redux স্টোর সাবস্ক্রাইব করে এবং সিলেক্টেড স্টেটের ভ্যালু পরিবর্তন হলে শ্যালো চেকের মাধ্যমে তা ধরে রি-রেন্ডার করে।

## 17. 5 Coding Exercises (৫টি কোডিং অনুশীলন)
1.  **Exercise 1**: Create a plain Node.js script that installs `redux`, sets up a basic store, and updates it without using any React package.
2.  **Exercise 2**: Write a mock component that subscribes to a store using `store.subscribe()` manually (without using `react-redux` hooks) and updates the local state to force a re-render.
3.  **Exercise 3**: Write a React custom hook `useCustomStore` that simulates the basic functionality of `useSelector` and `useDispatch` using React's context API.
4.  **Exercise 4**: Explain and write a code template illustrating how the same Redux store can be imported and shared between a React web setup and a React Native mobile setup.
5.  **Exercise 5**: Correct the code of a component where `useSelector(state => state)` is causing the component to re-render on every single unrelated action. Optimize the selector.

---

# Topic 5: What is Redux Toolkit (RTK) and What Problems Does It Solve?

## 1. Simple Definition (সহজ সংজ্ঞা)
Redux Toolkit (RTK) হলো Redux-এর অফিশিয়াল, অপিনিওনেটেড (opinionated) এবং রেকমেন্ডেড টুলসেট, যা Redux অ্যাপ্লিকেশন তৈরি করা অনেক সহজ ও নিরাপদ করে তোলে। এটি Redux-এর জটিল কনফিগারেশন, অতিরিক্ত বয়লারপ্লেট কোড এবং ভুল ব্যবহারের ঝুঁকি কমিয়ে দেয়। এটি মূলত Redux-এর স্ট্যান্ডার্ড কাজের ধারাকে সহজ করার জন্য তৈরি করা একটি আধুনিক লেয়ার।

## 2. Why This Concept Exists (কেন এই ধারণার উৎপত্তি)
ট্র্যাডিশনাল বা ক্লাসিক্যাল Redux-এ কাজ করতে গেলে ডেভেলপারদের প্রচুর বয়লারপ্লেট কোড লিখতে হতো। একটি ছোট স্টেট পরিবর্তনের জন্য Action Type, Action Creator, Reducer, combineReducers, Middleware Setup, DevTools Setup ইত্যাদি আলাদাভাবে করতে হতো। এই দীর্ঘ প্রক্রিয়াটি ডেভেলপারদের বিরক্তির কারণ হয়ে দাঁড়িয়েছিল এবং অনেকেই Redux পরিহার করা শুরু করেছিলেন। এই সমস্যা দূর করে Redux-কে সহজে ব্যবহারযোগ্য করতে Redux Toolkit আনা হয়।

## 3. What Problem It Solves (এটি কোন সমস্যার সমাধান করে)
*   **Too Much Boilerplate Code**: স্লাইস (`createSlice`) ব্যবহারের মাধ্যমে অ্যাকশন ও রিডিউসার একই সাথে তৈরি করা যায়, ফলে ফাইলের সংখ্যা ও বয়লারপ্লেট কোড প্রায় ৭০% কমে যায়।
*   **Complicated Store Configuration**: ট্র্যাডিশনাল স্টোর সেটআপে মিডলওয়্যার কনফিগারেশন ও দেবটুলস সেটআপ করা বেশ জটিল ছিল। RTK-এর `configureStore` এটি এক লাইনেই করে দেয়।
*   **Accidental State Mutation**: ভুল করে রিডিউসারের ভেতরে সরাসরি স্টেট আপডেট করার ফলে যে বাগ হতো, তা RTK-তে ডিফল্টভাবে যুক্ত থাকা `immer` লাইব্রেরি স্বয়ংক্রিয়ভাবে সমাধান করে।
*   **Manual Async Setup**: আগে Thunk বা Saga মিডলওয়্যার ম্যানুয়ালি সেটআপ করতে হতো। RTK-তে Thunk ডিফল্টভাবে বিল্ট-ইন থাকে এবং অ্যাসিনক্রোনাস কাজ করার জন্য `createAsyncThunk` রয়েছে।

## 4. Real-Life Analogy (বাস্তব জীবনের উদাহরণ)
একটি ফার্নিচার বানানোর কাজের সাথে তুলনা করা যাক।
*   **Plain Redux**: আপনাকে জঙ্গল থেকে গাছ কেটে কাঠ আনতে হবে, করাত দিয়ে কাটতে হবে, পেরেক ও আঠা কিনে হাতুড়ি দিয়ে পিটিয়ে চেয়ার বানাতে হবে। প্রক্রিয়াটি দীর্ঘ এবং যেকোনো জায়গায় পেরেক ভুল মারলে চেয়ার বাঁকা হয়ে যাবে।
*   **Redux Toolkit**: এটি হলো একটি রেডি-মেড "IKEA Flatpack Furniture" কিট। এখানে সমস্ত অংশ নিখুঁত মাপে আগে থেকেই কাটা আছে, পেরেক-স্ক্রু সবই প্যাকেটে দেওয়া আছে এবং সাথে একটি সহজ গাইডবই আছে। আপনি জাস্ট নাট-বল্টুগুলো অ্যাসেম্বল করলেই চমৎকার ফার্নিচার তৈরি হয়ে যাবে। এতে ভুলের সুযোগ নেই এবং সময়ও বাঁচে।

## 5. How React Works Internally Regarding This Concept (এই বিষয়ে React কীভাবে অভ্যন্তরীণভাবে কাজ করে)
RTK কোনো নতুন ইঞ্জিন নয়; এটি স্ট্যান্ডার্ড রিডাক্সের ওপর তৈরি একটি মোড়ক (Wrapper)। এর `createSlice` ফাংশনটি ইন্টারনালি `immer` লাইব্রেরি ব্যবহার করে। যখন আপনি রিডিউসারে সরাসরি স্টেট মিউটেট করেন (যেমন: `state.items.push(action.payload)`), তখন Immer ইন্টারনালি JavaScript Proxies ব্যবহার করে একটি অস্থায়ী "Draft State" তৈরি করে এবং আপনার করা পরিবর্তনগুলো ট্র্যাক করে। এরপর এটি রিডাক্সের মূল নিয়ম মেনে একটি সম্পূর্ণ নতুন ইমিউটেবল অবজেক্ট রিটার্ন করে। এছাড়া, `configureStore` মেথডটি স্বয়ংক্রিয়ভাবে Redux DevTools-এর সাথে সংযোগ স্থাপন করে এবং স্ট্যান্ডার্ড Thunk মিডলওয়্যার লোড করে।

## 6. Basic Example (বেসিক উদাহরণ)

```javascript
// Step 1: Creating a slice using RTK
import { createSlice, configureStore } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      // Immer allows us to write "mutating" code safely!
      state.value += 1;
    },
    decrement: (state) => {
      state.value -= 1;
    },
    incrementByAmount: (state, action) => {
      state.value += action.payload;
    }
  }
});

// Extracting Auto-generated Actions and Reducer
export const { increment, decrement, incrementByAmount } = counterSlice.actions;
const counterReducer = counterSlice.reducer;

// Step 2: Configure the Store
const store = configureStore({
  reducer: {
    counter: counterReducer
  }
  // Thunk and DevTools are automatically set up!
});

export default store;
```

## 7. Step-by-Step Explanation of the Code (কোডের ধাপে ধাপে ব্যাখ্যা)
*   `createSlice` ফাংশনটি দিয়ে আমরা স্লাইস তৈরি করেছি। এটি একই সাথে নেমস্পেস (`name: 'counter'`), প্রারম্ভিক স্টেট (`initialState`) এবং রিডিউসার ডিফাইন করে।
*   রিডিউসারের ভেতরে আমরা সরাসরি `state.value += 1` লিখছি, যা সাধারণ জাভাস্ক্রিপ্টে মিউটেশন। কিন্তু RTK-র ভেতরে `immer` থাকায় এটি সম্পূর্ণরূপে নিরাপদ এবং ব্যাকগ্রাউন্ডে ইমিউটেবলি হ্যান্ডেল হয়।
*   `counterSlice.actions` থেকে স্বয়ংক্রিয়ভাবে `increment`, `decrement`, এবং `incrementByAmount` নামক Action Creators জেনারেট হয়ে যায়, যা আমরা এক্সপোর্ট করতে পারি।
*   `configureStore` রিডিউসারগুলোকে কম্বাইন করে স্টোর তৈরি করে এবং ব্যাকগ্রাউন্ডে Redux DevTools ও Redux Thunk অ্যাক্টিভেট করে দেয়।

## 8. Another Real-World Example (আরেকটি বাস্তব উদাহরণ)
এপিআই থেকে ডেটা লোড করার সিস্টেম (API Fetching)। ইউজার ডাটা এপিআই থেকে গেট করার জন্য `createAsyncThunk` ব্যবহার করা হয়। এটি স্বয়ংক্রিয়ভাবে তিনটি লাইফসাইকেল অ্যাকশন জেনারেট করে: `pending`, `fulfilled`, এবং `rejected`। স্লাইসের `extraReducers`-এ আমরা এই তিনটি কেস হ্যান্ডেল করে লোডিং স্পিনার ও ডাটা আপডেট কন্ট্রোল করতে পারি।

## 9. Common Mistakes Beginners Make (নতুনদের করা সাধারণ ভুলসমূহ)
*   **স্লাইসের বাইরে মিউটেশন করার চেষ্টা**: মনে রাখা প্রয়োজন যে `immer` শুধুমাত্র `createSlice` বা `createReducer` এর ভেতরেই কাজ করে। স্লাইসের বাইরে বা কম্পোনেন্টের ভেতরে সরাসরি রিডাক্স স্টেট মিউটেট করলে অ্যাপ কাজ করা বন্ধ করে দেবে।
*   **অ্যাকশন টাইপ নিয়ে কনফিউশন**: RTK অ্যাকশন অবজেক্টের টাইপ ইন্টারনালি `[sliceName]/[reducerName]` ফরম্যাটে জেনারেট করে (যেমন: `counter/increment`)। নতুনরা অনেক সময় ম্যানুয়ালি স্ট্রিং টাইপ লিখতে গিয়ে ভুল করে ফেলে।
*   **ক্রিয়েট করা অ্যাকশন কল না করা**: যেমন `dispatch(increment)` লিখে ফেলা, যেখানে এটি আসলে একটি ফাংশন এবং `dispatch(increment())` হিসেবে কল করা উচিত।

## 10. Interview Questions Related to This Topic (ইন্টারভিউয়ের প্রশ্নসমূহ)
1.  **Redux Toolkit (RTK) কি এবং কেন এটি তৈরি করা হয়েছিল?**
    *   *উত্তরঃ* RTK হলো Redux ডেভেলপমেন্টের জন্য রেকমেন্ডেড টুলকিট। এটি বয়লারপ্লেট কমাতে, স্টোর কনফিগারেশন সহজ করতে এবং ইমিউটেবল আপডেটকে সহজ করতে তৈরি হয়েছে।
2.  **RTK-তে `createSlice` কিভাবে স্টেট ম্যানেজমেন্ট সহজ করে?**
    *   *উত্তরঃ* এটি একটি নির্দিষ্ট ফাইলের ভেতরে স্টেট, অ্যাকশন টাইপ, অ্যাকশন ক্রিয়েটর এবং রিডিউসার একসাথে তৈরি করার সুবিধা দেয়, ফলে অতিরিক্ত কোড লিখতে হয় না।
3.  **Redux Toolkit-এ `immer`-এর ভূমিকা কি এবং এটি কিভাবে কাজ করে?**
    *   *উত্তরঃ* Immer রিডিউসারের ভেতরে সরাসরি স্টেট মডিফাই বা মিউটেট করার অনুমতি দেয়। ইন্টারনালি এটি Proxy অবজেক্টের মাধ্যমে একটি ড্রাফট স্টেট তৈরি করে এবং ইমিউটেবল অবজেক্ট রিটার্ন করে।
4.  **traditional `createStore`-এর সাথে `configureStore`-এর তফাত কি?**
    *   *উত্তরঃ* `configureStore` স্বয়ংক্রিয়ভাবে রিডিউসারগুলোকে কম্বাইন করতে পারে, মিডলওয়্যার (যেমন Thunk) এবং Redux DevTools কনফিগার করে দেয়, যা ট্র্যাডিশনাল উপায়ে ম্যানুয়ালি করতে হতো।
5.  **`createAsyncThunk` কি এবং এটি কখন ব্যবহার করা হয়?**
    *   *উত্তরঃ* এটি অ্যাসিনক্রোনাস লজিক যেমন এপিআই রিকোয়েস্ট হ্যান্ডেল করার জন্য একটি ইউটিলিটি। এটি লাইফসাইকেল অ্যাকশন (pending, fulfilled, rejected) ডিসপ্যাচ করে অ্যাসিনক্রোনাস ডাটা রেন্ডারিং সহজ করে।

## 11. Best Practices (সেরা অভ্যাসসমূহ)
*   **Always use RTK for new projects**: এখন থেকে যেকোনো নতুন রিডাক্স প্রজেক্টে ট্র্যাডিশনাল রিডাক্স ব্যবহার না করে সরাসরি RTK ব্যবহার করুন।
*   **Use RTK Query for API calls**: যদি অ্যাপে প্রচুর নেটওয়ার্ক রিকোয়েস্ট থাকে, তবে ডাটা ফেচিং, ক্যাশিং ও সিনক্রোনাইজেশনের জন্য RTK Query ব্যবহার করুন।
*   **Keep logic in Slices**: আপনার স্টেট লজিক ও স্লাইসগুলোকে ফিচার অনুযায়ী আলাদা ফোল্ডারে গুছিয়ে রাখুন (Feature folder structure)।

## 12. Performance Considerations (পারফরম্যান্স সংক্রান্ত বিষয়সমূহ)
RTK-তে বিল্ট-ইন ক্যাশিং লাইব্রেরি ও সিলেক্টর মেকানিজম থাকায় পারফরম্যান্স অনেক বুস্ট হয়। বিশেষ করে RTK Query ব্যবহারের মাধ্যমে একই এপিআই বারবার কল হওয়া বন্ধ হয়, যা নেটওয়ার্ক ব্যান্ডউইথ ও মেমরি সাশ্রয় করে।

## 13. When NOT to Use It (কখন এটি ব্যবহার করবেন না)
*   যদি প্রজেক্টের সাইজ অতি ক্ষুদ্র হয় এবং একটি মাত্র `useState` দিয়েই সম্পূর্ণ কাজ হয়ে যায়।
*   যদি আপনি কোনো অনেক পুরনো লিগ্যাসি কোডবেস আপডেট করছেন যা সম্পূর্ণ ট্র্যাডিশনাল রিডাক্স দিয়ে তৈরি এবং রিফ্যাক্টরিংয়ের বাজেট নেই।

## 14. Comparison with Similar Concepts (অনুরূপ ধারণার সাথে তুলনা)

| Feature | Plain Redux | Redux Toolkit (RTK) |
| :--- | :--- | :--- |
| **Boilerplate** | High (Write Types, Creators, Reducers separately) | Low (All combined in `createSlice`) |
| **Immutability** | Manual (Using spread operator or ImmutableJS) | Automatic (Handled via Immer) |
| **Store Setup** | Manual and complicated | Out-of-the-box (`configureStore`) |
| **Thunk Middleware**| Needs manual setup and installation | Included by default |
| **DevTools** | Requires complex configuration | Automatically enabled |

## 15. Summary in Simple Bangla (সহজ বাংলায় সারসংক্ষেপ)
Redux Toolkit (RTK) হলো রিডাক্সের একটি আধুনিক সংস্করণ। এটি রিডাক্সে কাজ করার বয়লারপ্লেট কোডের পরিমাণ অনেক কমিয়ে দেয়, স্টোর তৈরি করা পানির মতো সহজ করে এবং ইমিউটেবিলিটি মেনটেইন করার মাথা ব্যাথা দূর করে। বর্তমান সময়ে রিডাক্স ব্যবহার করার অর্থই হলো RTK ব্যবহার করা।

## 16. 5 MCQ Questions (৫টি বহুনির্বাচনী প্রশ্ন)
1.  **Which library is used internally by Redux Toolkit to allow safe "mutable" state changes?**
    *   A) React Router
    *   B) Lodash
    *   C) Immer
    *   D) Axios
    *   *Correct Answer: C*
    *   *Explanation:* RTK-র ভেতরে `immer` লাইব্রেরি ব্যবহার করা হয় যা আমাদের মিউটেবল স্টাইলে স্টেট লেখার সুযোগ দেয়, কিন্তু ইন্টারনালি সেটিকে ইমিউটেবল রাখে।
2.  **What is generated automatically when you create a slice using `createSlice`?**
    *   A) Database schemas
    *   B) Both reducer functions and action creators
    *   C) React UI components
    *   D) HTML templates
    *   *Correct Answer: B*
    *   *Explanation:* `createSlice` একই সাথে রিডিউসার এবং কারেসপন্ডিং অ্যাকশন ক্রিয়েটরগুলো স্বয়ংক্রিয়ভাবে তৈরি করে ফেলে।
3.  **What does `configureStore` do automatically under the hood?**
    *   A) Connects directly to a MongoDB database.
    *   B) Compiles the React components to web assemblies.
    *   C) Sets up Redux DevTools and Redux Thunk middleware.
    *   D) Translates JS code into TypeScript.
    *   *Correct Answer: C*
    *   *Explanation:* `configureStore` ডেভেলপমেন্টকে সহজ করতে রিডাক্স ডেভটুলস ও রিডাক্স থাঙ্ক মিডলওয়্যার স্বয়ংক্রিয়ভাবে সক্রিয় করে।
4.  **How do you handle asynchronous actions in Redux Toolkit?**
    *   A) By putting `setTimeout` inside a standard reducer.
    *   B) By using `createAsyncThunk` utility.
    *   C) RTK does not support asynchronous actions.
    *   D) By writing a direct database query in the slice.
    *   *Correct Answer: B*
    *   *Explanation:* RTK-তে অ্যাসিনক্রোনাস কাজ (যেমন এপিআই কল) করার জন্য `createAsyncThunk` ব্যবহার করা হয়।
5.  **Which of the following is NOT a feature of Redux Toolkit?**
    *   A) Boilerplate reduction
    *   B) Automatic CSS minification
    *   C) Built-in Thunk middleware
    *   D) Simplified store configuration
    *   *Correct Answer: B*
    *   *Explanation:* CSS মিনিফিকেশন বিল্ড টুলের কাজ (যেমন Webpack বা Vite), এটি Redux Toolkit-এর কাজ নয়।

## 17. 5 Coding Exercises (৫টি কোডিং অনুশীলন)
1.  **Exercise 1**: Create a slice named `cartSlice` with an initial state of `items: []` and a reducer `addToCart` that appends an item to the list using `state.items.push()`.
2.  **Exercise 2**: Write a store configuration file using `configureStore` that combines a `userSlice` and a `settingsSlice`.
3.  **Exercise 3**: Implement an asynchronous thunk `fetchUsers` using `createAsyncThunk` that fetches data from `https://jsonplaceholder.typicode.com/users` and handles the success case in `extraReducers`.
4.  **Exercise 4**: Write a slice that manages a toggleable sidebar state (`isOpen: false`), showing how to toggle the state in a clean, mutation-like way.
5.  **Exercise 5**: Refactor a traditional Redux codebase containing separate action types, action creators, and a reducer into a single clean RTK slice.
