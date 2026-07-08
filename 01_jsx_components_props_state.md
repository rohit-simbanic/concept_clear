# React Mastery: Part 1 - JSX, Components, Props, and State

স্বাগতম! একজন React ডেভেলপার হিসেবে আপনার যাত্রাকে আরও মজবুত করতে এই গাইডটি তৈরি করা হয়েছে। এখানে প্রতিটি কনসেপ্ট অত্যন্ত গভীরভাবে আলোচনা করা হবে।

---

## ১. JSX (JavaScript XML)

### ১. Simple definition (বাংলায়)
JSX হলো JavaScript-এর একটি সিনট্যাক্স এক্সটেনশন (Syntax Extension)। সহজ কথায়, এটি দেখতে HTML-এর মতো হলেও আসলে এটি JavaScript-এর ক্ষমতা ব্যবহার করে ব্রাউজারের জন্য UI ডিজাইন করার একটি সহজ উপায়। JSX দিয়ে আমরা JavaScript ফাইলের ভেতরেই সরাসরি HTML-এর মতো কোড লিখতে পারি।

### ২. Why this concept exists
React-এর মূল দর্শন হলো—UI এবং UI-এর পেছনের লজিক (Logic) আলাদা কোনো জায়গায় থাকা উচিত নয়, তারা একে অপরের সাথে ওতপ্রোতভাবে জড়িত। প্রথাগত ওয়েব ডেভেলপমেন্টে HTML এবং JavaScript আলাদা ফাইলে লেখা হতো, যা বড় অ্যাপ্লিকেশনের ক্ষেত্রে কোড মেইনটেইন করা কঠিন করে তুলত। JSX-এর মাধ্যমে React ডেভেলপারদের একই ফাইলে লজিক এবং মার্কআপ লেখার সুবিধা দেয়, যা ডেভেলপমেন্ট গতি বাড়ায়।

### ৩. What problem it solves
JSX আসার আগে React-এ UI তৈরি করতে `React.createElement()` ফাংশন ব্যবহার করতে হতো। যদি কোনো কমপ্লেক্স বা নেস্টেড UI তৈরি করতে হতো, তবে কোডটি পড়তে এবং লিখতে অনেক কষ্ট হতো। যেমন:
```javascript
// JSX ছাড়া:
React.createElement('div', {className: 'container'}, 
  React.createElement('h1', null, 'Hello World')
);
```
JSX এই জটিলতাকে দূর করেছে। এখন আমরা সহজেই লিখতে পারি:
```javascript
// JSX সহ:
<div className="container">
  <h1>Hello World</h1>
</div>
```

### ৪. Real-life analogy
চিন্তা করুন আপনি একটি রেস্টুরেন্টে গিয়ে খাবার অর্ডার করছেন। 
* **JSX ছাড়া:** আপনি ওয়েটারকে বলছেন, "আমাকে একটি প্লেট দিন, তার ওপর কিছু ভাত দিন, ভাতের ওপর ডাল দিন এবং পাশে একটি আলুভর্তা দিন।" (এটি হলো `React.createElement` ব্যবহারের মতো জটিল)।
* **JSX সহ:** আপনি সরাসরি মেনু দেখে বললেন, "আমাকে ১ প্লেট ডাল-ভাত আলুভর্তা দিন।" (এটি হলো সরাসরি মার্কআপ লেখার মতো সহজ)।

### ৫. How React works internally regarding this concept
ব্রাউজার সরাসরি JSX বোঝে না। তাই বিল্ড টাইমে (Build Time) Babel বা Vite-এর মতো কম্পাইলার JSX-কে সাধারণ JavaScript অবজেক্টে রূপান্তর করে। React 17+-এর পর থেকে এটি `react/jsx-runtime` এর সাহায্যে রূপান্তরিত হয়।
```javascript
// JSX কোড:
const element = <h1 className="title">Hello</h1>;

// কম্পাইলার দ্বারা রূপান্তরিত কোড (React 17+):
import { jsx as _jsx } from 'react/jsx-runtime';
const element = _jsx('h1', { className: 'title', children: 'Hello' });
```
এই রূপান্তরিত ফাংশনটি একটি প্লেইন JavaScript অবজেক্ট রিটার্ন করে যাকে আমরা "Virtual DOM Node" বলি।

### ৬. Basic example
```jsx
import React from 'react';

function WelcomeMessage() {
  const userName = "Amit Hassan";
  const isLoggedIn = true;

  return (
    <div className="welcome-card">
      <h1 className="title">Hello, {userName}!</h1>
      {isLoggedIn ? (
        <p className="status-active">Welcome back to the dashboard.</p>
      ) : (
        <p className="status-guest">Please log in to continue.</p>
      )}
    </div>
  );
}

export default WelcomeMessage;
```

### ৭. Step-by-step explanation of the code
* `{userName}`: JSX-এর ভেতরে যেকোনো ডাইনামিক JavaScript এক্সপ্রেশন ব্যবহারের জন্য কার্লি ব্রেসেস `{}` ব্যবহার করা হয়।
* `{isLoggedIn ? ... : ...}`: JSX-এর ভেতর সরাসরি `if-else` স্টেটমেন্ট লেখা যায় না, তাই কন্ডিশনাল রেন্ডারিংয়ের জন্য টার্নারি অপারেটর (Ternary Operator) ব্যবহার করা হয়েছে।
* `className`: HTML-এ আমরা `class` ব্যবহার করি, কিন্তু JavaScript-এ `class` একটি রিজার্ভড কিওয়ার্ড (Reserved Keyword)। তাই JSX-এ CSS ক্লাসের জন্য `className` ব্যবহার করতে হয়।

### ৮. Another real-world example (Product Card)
```jsx
import React from 'react';

function ProductCard() {
  const product = {
    name: "MacBook Pro M3",
    price: 1999,
    inStock: true,
    features: ["16GB Unified Memory", "512GB SSD", "Liquid Retina XDR"]
  };

  return (
    <div className="product-card" style={{ border: '1px solid #ccc', padding: '16px', borderRadius: '8px' }}>
      <h2>{product.name}</h2>
      <p>Price: ${product.price}</p>
      <p>{product.inStock ? "Available" : "Out of Stock"}</p>
      <ul>
        {product.features.map((feature, index) => (
          <li key={index}>{feature}</li>
        ))}
      </ul>
    </div>
  );
}
```

### ৯. Common mistakes beginners make
* **একটির বেশি প্যারেন্ট এলিমেন্ট রাখা:** JSX-এ সবসময় একটি সিঙ্গেল রুট/প্যারেন্ট এলিমেন্ট থাকতে হবে। একাধিক এলিমেন্ট রেন্ডার করতে চাইলে React Fragment (`<> ... </>`) ব্যবহার করতে হবে।
* **সরাসরি Statement ব্যবহার:** কার্লি ব্রেসের ভেতর সরাসরি `if-else` বা `for` লুপ লেখার চেষ্টা করা (সেখানে শুধু Expressions ব্যবহার করতে হবে যা কোনো ভ্যালু রিটার্ন করে)।
* **lowercase-এ কম্পোনেন্ট নাম লেখা:** React-এ কাস্টম কম্পোনেন্টের নাম সবসময় Uppercase (বড় হাতের অক্ষর) দিয়ে শুরু হতে হবে (যেমন: `<ProductCard />`, `<productCard />` নয়)।

### ১০. Interview questions related to this topic
1. **ব্রাউজার কি সরাসরি JSX রান করতে পারে? না পারলে কীভাবে রান করে?**
   * উত্তর: না, ব্রাউজার বোঝে না। Babel বা এসোসিয়াটেড ট্রান্সপাইলার JSX-কে `React.createElement` বা `jsx-runtime` এর প্লেইন JavaScript অবজেক্টে কনভার্ট করে।
2. **JSX-এ কেন `class` এর বদলে `className` এবং `for` এর বদলে `htmlFor` ব্যবহার করা হয়?**
   * উত্তর: কারণ JSX আলটিমেটলি JavaScript-এ রূপান্তর হয় এবং `class` ও `for` হলো JavaScript-এর রিজার্ভড কিওয়ার্ড।
3. **React Fragment কী এবং এটি কেন ব্যবহার করা হয়?**
   * উত্তর: DOM-এ অতিরিক্ত কোনো নোড (যেমন অতিরিক্ত `<div>`) যোগ না করে একাধিক JSX এলিমেন্ট গ্রুপ করার জন্য Fragment ব্যবহার করা হয়।

### ১১. Best practices
* কোড রিডাবিলিটি বাড়াতে জটিল টার্নারি কন্ডিশনকে কম্পোনেন্টের বাইরে বা ছোট ছোট হেল্পার ফাংশনে নিয়ে যান।
* সবসময় ইনলাইন স্টাইল এভয়েড করার চেষ্টা করুন, ডাইনামিক স্টাইল ছাড়া ক্লাসনেম ব্যবহার করুন।
* ফ্র্যাগমেন্টের জন্য শর্টকাট `<> ... </>` ব্যবহার করুন, যদি না সেখানে `key` প্রপসের প্রয়োজন হয়।

### ১২. Performance considerations
JSX নিজে কোনো অতিরিক্ত ওভারহেড তৈরি করে না কারণ এটি কম্পাইলড কোড। তবে ডাইনামিক্যালি রেন্ডার করা লিস্টের ক্ষেত্রে প্রতিটির জন্য ইউনিক `key` প্রপ প্রদান করা উচিত যাতে Reconciliation প্রসেসে React সহজে এলিমেন্টগুলোকে ট্র্যাক করতে পারে।

### ১৩. When NOT to use it
যদি আপনি কোনো খুবই সাধারণ প্রজেক্ট তৈরি করেন যেখানে কোনো ডাইনামিক স্টেট চেঞ্জ বা ইন্টার‍্যাকশন নেই, সেখানে প্লেইন HTML/JS ব্যবহার করাই ভালো।

### ১৪. Comparison with similar concepts
* **JSX vs HTML:** HTML ব্রাউজার সরাসরি বোঝে, কিন্তু এটি স্ট্যাটিক। JSX হলো ডাইনামিক, যা JavaScript-এর পূর্ণ শক্তি ব্যবহার করতে পারে এবং এটি পরে ব্রাউজার-রিডাবল JS অবজেক্টে রূপান্তরিত হয়।
* **JSX vs Templates (Angular/Vue):** Angular বা Vue-তে স্পেশাল ডাইরেক্টিভ (যেমন `*ngIf`, `v-if`) শেখা লাগে। কিন্তু JSX-এ আমরা সাধারণ JavaScript লজিক (টার্নারি, ম্যাপ) ব্যবহার করি।

### ১৫. Summary in simple Bangla
JSX হলো JavaScript ফাইলের ভেতরে HTML লেখার একটি সুন্দর ও সহজ উপায়। এটি ব্যবহারের ফলে আমরা কোডের ডিজাইন ও লজিক একসাথে গুছিয়ে লিখতে পারি। ব্যাকগ্রাউন্ডে এটি প্লেইন JavaScript অবজেক্টে রূপান্তরিত হয়ে ব্রাউজারে রান করে।

### ১৬. 5 MCQ questions
1. JSX-এর পুরো নাম কী?
   * A) JavaScript XML
   * B) Java Syntax Extension
   * C) JavaScript Extension
   * D) JSON XML
   * *উত্তর: A*
2. JSX-এ CSS ক্লাস ডিফাইন করার জন্য কোনটি ব্যবহৃত হয়?
   * A) class
   * B) className
   * C) classId
   * D) styleClass
   * *উত্তর: B*
3. JSX ট্রান্সপাইলেশনের কাজ মূলত কে করে?
   * A) Node.js
   * B) Chrome V8
   * C) Babel / Build bundlers
   * D) React Router
   * *উত্তর: C*
4. JSX-এর রুট এলিমেন্ট হিসেবে DOM-এ বাড়তি নোড না যোগ করে গ্রুপ করার উপায় কোনটি?
   * A) `<div>`
   * B) `<span>`
   * C) `<Fragment>` বা `<>`
   * D) `<section>`
   * *উত্তর: C*
5. নিচের কোনটি JSX-এ সঠিক কন্ডিশনাল রেন্ডারিং এক্সপ্রেশন?
   * A) `{if(user) { <p>Hi</p> }}`
   * B) `{user ? <p>Hi</p> : null}`
   * C) `{user && <p>Hi</p>}`
   * D) Both B and C
   * *উত্তর: D*

### ১৭. 5 Coding exercises
1. একটি React কম্পোনেন্ট লিখুন যা একটি `items` অ্যარე গ্রহণ করে এবং JSX-এ `<ul>` ও `<li>` দিয়ে তা রেন্ডার করে।
2. একটি ইউজার কার্ড তৈরি করুন যেখানে কন্ডিশনাল রেন্ডারিং ব্যবহার করে দেখাবেন ইউজার যদি এডমিন হন তবে একটি "Admin" ব্যাজ দেখাবে, নতুবা "Regular User" দেখাবে।
3. একটি কম্পোনেন্ট লিখুন যা ইনলাইন স্টাইলিং ব্যবহার করে টেক্সটের কালার ডাইনামিক্যালি পরিবর্তন করবে (একটি ভ্যারিয়েবলের ওপর ভিত্তি করে)।
4. JSX Fragment ব্যবহার করে পাশাপাশি দুটি সেকশন (`Header` এবং `Footer`) রেন্ডার করুন কোনো রুট `div` ছাড়াই।
5. একটি প্রোডাক্টের নাম ও ডিসকাউন্ট প্রাইস রেন্ডার করুন। যদি ডিসকাউন্ট প্রাইস মূল প্রাইসের চেয়ে কম হয় তবে মূল প্রাইসের ওপর স্ট্রাইক-থ্রু (strike-through) লাইন দেখান।

---

## ২. Component (Functional vs Class)

### ১. Simple definition (বাংলায়)
Component হলো React অ্যাপ্লিকেশনের মূল চালিকাশক্তি বা বিল্ডিং ব্লক (Building Block)। এটি একটি স্বাধীন, পুনরায় ব্যবহারযোগ্য (reusable) কোডের অংশ যা অ্যাপের একটি নির্দিষ্ট ইউজার ইন্টারফেস (UI) তৈরি এবং নিয়ন্ত্রণ করে।

### ২. Why this concept exists
বড় বড় প্রজেক্টে পুরো ওয়েবসাইটটি যদি একটিমাত্র ফাইলে লেখা হতো, তবে কোড ম্যানেজ করা অসম্ভব হয়ে পড়ত। কম্পোনেন্টের ধারণার ফলে আমরা একটি বড় পেজকে ছোট ছোট অংশে ভাগ করতে পারি (যেমন: Header, Sidebar, Footer, Product Card ইত্যাদি)। এতে কোড রিইউজেবিলিটি এবং মেইনটেইনেবিলিটি বহুগুণ বেড়ে যায়।

### ৩. What problem it solves
কম্পোনেন্ট না থাকলে একই ধরনের UI এবং লজিক বারবার বিভিন্ন জায়গায় কপি-পেস্ট করতে হতো। কম্পোনেন্ট প্রথার মাধ্যমে আমরা একবার কোড লিখে তা হাজার বার বিভিন্ন ডেটা দিয়ে ডাইনামিক্যালি ব্যবহার করতে পারি।

### ৪. Real-life analogy
একটি LEGO সেট বা খেলনা বাড়ি তৈরির কথা ভাবুন। পুরো বাড়িটি কিন্তু ছোট ছোট প্লাস্টিক ব্লক বা LEGO পিস দিয়ে তৈরি। প্রতিটি ব্লক আলাদা স্বাধীন অংশ, কিন্তু একসাথে জুড়ে দিলে একটি বড় সুন্দর বাড়ি তৈরি হয়। এখানে একেকটি ব্লক হলো একেকটি Component।

### ৫. How React works internally regarding this concept
React যখন কোনো কম্পোনেন্টকে রেন্ডার করে:
1. **Functional Component:** React সরাসরি ফাংশনটিকে কল করে এবং এর রিটার্ন করা JSX অবজেক্টটি নিয়ে নেয়।
2. **Class Component:** React প্রথমে ক্লাসের একটি ইন্সট্যান্স (Instance) তৈরি করে (`new ComponentName()`), তারপর তার `render()` মেথডটি কল করে। ক্লাসের লাইফসাইকেল মেথডগুলো ট্র্যাক করার জন্য React মেমরিতে এই ইন্সট্যান্সটি ধরে রাখে।

### ৬. Basic example
**Functional Component:**
```jsx
import React from 'react';

function UserProfile(props) {
  return (
    <div className="profile-card">
      <h3>Name: {props.name}</h3>
      <p>Role: {props.role}</p>
    </div>
  );
}

export default UserProfile;
```

**Class Component:**
```jsx
import React, { Component } from 'react';

class UserProfileClass extends Component {
  render() {
    return (
      <div className="profile-card">
        <h3>Name: {this.props.name}</h3>
        <p>Role: {this.props.role}</p>
      </div>
    );
  }
}

export default UserProfileClass;
```

### ७. Step-by-step explanation of the code
* Functional Component-এ প্রপস সরাসরি ফাংশনের আর্গুমেন্ট (`props`) হিসেবে পাওয়া যায়।
* Class Component-এ `React.Component` ক্লাসকে এক্সটেন্ড করতে হয় এবং প্রপস অ্যাক্সেস করতে `this.props` ব্যবহার করতে হয়। এখানে অবশ্যই একটি `render()` মেথড থাকতে হবে যা JSX রিটার্ন করবে।

### ৮. Another real-world example (Counter Component)
```jsx
// Functional Component with Hooks
import React, { useState } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

```jsx
// Equivalent Class Component
import React, { Component } from 'react';

class CounterClass extends Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
  }

  increment = () => {
    this.setState({ count: this.state.count + 1 });
  }

  render() {
    return (
      <div>
        <p>Count: {this.state.count}</p>
        <button onClick={this.increment}>Increment</button>
      </div>
    );
  }
}
```

### ৯. Common mistakes beginners make
* **মেমরি লিক ও লাইফসাইকেল মিস-ম্যাচ:** Class component থেকে Functional component-এ আসার সময় লাইফসাইকেল মেথড (`componentDidMount`, `componentWillUnmount`) সঠিকভাবে `useEffect`-এ কনভার্ট করতে না পারা।
* **স্টেট আপডেট ভুল করা:** Class component-এ `this.setState` স্টেটকে শ্যালো মার্জ (shallow merge) করে, কিন্তু Functional component-এর `useState` সেটার পুরো ভ্যালু রিপ্লেস করে দেয়।

### ১০. Interview questions related to this topic
1. **Functional and Class Component-এর মধ্যে প্রধান পার্থক্যগুলো কী কী?**
   * উত্তর: Functional component হলো প্লেইন JS ফাংশন যা প্রপস নিয়ে JSX রিটার্ন করে এবং এটি Hooks ব্যবহার করে। Class component হলো ES6 ক্লাস যা লাইফসাইকেল মেথড ও লোকাল স্টেট সরাসরি ক্লাসের মেম্বার হিসেবে ব্যবহার করে।
2. **কেন বর্তমানে Functional Component বেশি জনপ্রিয়?**
   * উত্তর: এটি সহজে পড়া যায়, কোড কম লিখতে হয়, টেস্ট করা সহজ এবং React Hooks-এর কারণে ক্লাসের সমস্ত সুবিধা এখন ফাংশনেই পাওয়া যায়।
3. **Class component-এর `constructor` এ কেন `super(props)` কল করতে হয়?**
   * উত্তর: প্যারেন্ট ক্লাস `React.Component`-এর কনস্ট্রাক্টর কল করার জন্য এবং ক্লাসের ভেতরে `this.props` সঠিকভাবে ইনিশিয়েলাইজ করার জন্য।

### ১১. Best practices
* নতুন প্রজেক্টে সবসময় Functional Component ব্যবহার করুন।
* প্রতিটি কম্পোনেন্টকে সিঙ্গেল রেসপন্সিবিলিটি প্রিন্সিপাল (SRP) অনুযায়ী ডিজাইন করুন—অর্থাৎ একটি কম্পোনেন্ট যেন একটি নির্দিষ্ট কাজই করে।
* ছোট ছোট রিইউজেবল সাব-কম্পোনেন্টে ভাগ করুন।

### ১২. Performance considerations
Functional components হালকা কারণ এদের জন্য ব্যাকগ্রাউন্ডে কোনো ক্লাস ইন্সট্যান্স তৈরি করতে হয় না। এছাড়া `React.memo` ব্যবহার করে অপ্রয়োজনীয় রি-রেন্ডারিং এড়ানো যায়।

### ১৩. When NOT to use it
যদি কোনো থার্ড-পার্টি লাইব্রেরি বা পুরোনো কোডবেস থাকে যেখানে Class Component ব্যবহার বাধ্যতামূলক, সেখানে Class Component ব্যবহার করতে হতে পারে। এছাড়া নতুন সমস্ত অ্যাপে ফাংশনাল কম্পোনেন্ট ব্যবহার করা উচিত।

### ১৪. Comparison with similar concepts
* **Functional vs Class Component:** Functional-এ কোড কম, রেন্ডারিং স্পিড ভালো এবং হুকস সাপোর্ট করে। Class component কিছুটা ভারী, `this` বাইন্ডিংয়ের জটিলতা আছে।

### ১৫. Summary in simple Bangla
কম্পোনেন্ট হলো React-এর এক একটি ছোট স্বাধীন অংশ। Functional Component হলো সাধারণ ফাংশন এবং Class Component হলো ES6 ক্লাস। আধুনিক React-এ Hooks আসার পর Functional Component-ই ইন্ডাস্ট্রি স্ট্যান্ডার্ড।

### ১৬. 5 MCQ questions
1. আধুনিক React ডেভেলপমেন্টে কোন ধরনের কম্পোনেন্ট বেশি রিকমেন্ডেড?
   * A) Class Component
   * B) Functional Component
   * C) Higher Order Component
   * D) Controlled Component
   * *উত্তর: B*
2. Class Component-এ কোন মেথডটি অবশ্যই থাকতে হবে?
   * A) constructor()
   * B) componentDidMount()
   * C) render()
   * D) setState()
   * *উত্তর: C*
3. Class Component-এ প্যারেন্ট কনস্ট্রাক্টর কল করার জন্য কোনটি ব্যবহৃত হয়?
   * A) parent()
   * B) super()
   * C) this.super()
   * D) extend()
   * *উত্তর: B*
4. Functional Component-এ স্টেট ম্যানেজ করার জন্য কি ব্যবহার করা হয়?
   * A) this.state
   * B) setState()
   * C) React Hooks (useState)
   * D) getInitialState()
   * *উত্তর: C*
5. Class component-এ স্টেট আপডেট করার সঠিক নিয়ম কোনটি?
   * A) `this.state.count = 5`
   * B) `this.setState({ count: 5 })`
   * C) `this.state({ count: 5 })`
   * D) `useState(5)`
   * *উত্তর: B*

### ১৭. 5 Coding exercises
1. একটি Class Component তৈরি করুন যা একটি ইউজারনেম এবং বয়স রেন্ডার করে।
2. উপরোক্ত Class Component-টিকে Functional Component-এ রূপান্তর করুন।
3. একটি Functional Component তৈরি করুন যা প্রপস হিসেবে একটি ইমেজ URL গ্রহণ করে সেটি দেখাবে।
4. একটি Class Component তৈরি করুন যাতে একটি বাটন থাকবে এবং বাটনে ক্লিক করলে কনসোলে "Clicked!" দেখাবে।
5. একটি Functional Component তৈরি করুন যা একটি কন্ডিশন চেক করে কার্ডের বর্ডার কালার গ্রিন বা রেড করবে।

---

## ৩. Props (Properties)

### ১. Simple definition (বাংলায়)
Props (Properties-এর সংক্ষিপ্ত রূপ) হলো এমন কিছু ডেটা যা এক কম্পোনেন্ট থেকে অন্য কম্পোনেন্টে (সাধারণত প্যারেন্ট থেকে চাইল্ড কম্পোনেন্টে) পাঠানো হয়। এটি অনেকটা ফাংশনের আর্গুমেন্ট (argument)-এর মতো কাজ করে।

### ২. Why this concept exists
কম্পোনেন্টগুলোকে ডাইনামিক এবং রিইউজেবল করতে প্রপস দরকার। যদি প্রপস না থাকত, তবে প্রতিটি কম্পোনেন্টের ভেতর ফিক্সড ডেটা থাকত, ফলে একই ডিজাইনের ভিন্ন ডেটা দেখানোর জন্য আলাদা আলাদা কম্পোনেন্ট লিখতে হতো।

### ৩. What problem it solves
প্রপস আমাদের অ্যাপ্লিকেশনকে কনফিগারযোগ্য (configurable) করে তোলে। ডেটা ফ্লো একমুখী (Uni-directional data flow) রেখে ডেটা পাস করার সমস্যার সমাধান করে প্রপস।

### ৪. Real-life analogy
আপনি যখন একটি মোবাইল ফোন কেনেন, ফোনের স্ক্রিন সাইজ, র‍্যাম বা মেমরি হলো তার প্রপস। ফোন কোম্পানি একই ডিজাইন (Component) ব্যবহার করে কিন্তু ভিন্ন ভিন্ন কনফিগারেশনের (Props) ফোন বাজারজাত করে।

### ৫. How React works internally regarding this concept
Reactเมื่อ render Component, จะแปลง attribute ใน JSX ให้เป็น Object และส่งเป็น argument แรกของ function component. Props เป็น **Read-only** หรือ **Immutable** ไม่สามารถแก้ไขโดยตรงภายใน component ลูกได้.

### ৬. Basic example
```jsx
import React from 'react';

// Child Component
function Book(props) {
  return (
    <div className="book-card">
      <h4>Title: {props.title}</h4>
      <p>Author: {props.author}</p>
    </div>
  );
}

// Parent Component
function Library() {
  return (
    <div>
      <h2>My Bookshelf</h2>
      <Book title="The Alchemist" author="Paulo Coelho" />
      <Book title="Gitanjali" author="Rabindranath Tagore" />
    </div>
  );
}

export default Library;
```

### ৭. Step-by-step explanation of the code
* প্যারেন্ট কম্পোনেন্ট `Library` চাইল্ড কম্পোনেন্ট `Book`-কে দুইবার রেন্ডার করেছে।
* প্রতিবার ভিন্ন `title` এবং `author` প্রপ হিসেবে পাঠানো হয়েছে।
* `Book` কম্পোনেন্ট তার `props` অবজেক্ট থেকে `{props.title}` এবং `{props.author}` রিড করে স্ক্রিনে দেখচ্ছে।

### ৮. Another real-world example (Destructuring and Children Props)
```jsx
import React from 'react';

// Child Component using Destructuring & children prop
function Button({ onClick, color = 'blue', children }) {
  return (
    <button 
      onClick={onClick} 
      style={{ backgroundColor: color, color: '#white', padding: '8px 16px', border: 'none' }}
    >
      {children}
    </button>
  );
}

// Parent Component
function App() {
  return (
    <div>
      <Button onClick={() => alert('Saved!')} color="green">
        Save Changes
      </Button>
      <Button onClick={() => alert('Deleted!')} color="red">
        Delete
      </Button>
    </div>
  );
}
```

### ৯. Common mistakes beginners make
* **প্রপস মিউটেশন করা:** চাইল্ড কম্পোনেন্টের ভেতর সরাসরি `props.title = "New Title"` লেখার চেষ্টা করা। এটি করলে React এর একমুখী ডেটা ফ্লো নষ্ট হয় এবং বাগে রূপ নেয়।
* **ভুল টাইপের ডেটা পাঠানো:** নাম্বার বা বুলিয়ান প্রপ পাঠানোর সময় কার্লি ব্রেস ব্যবহার না করা (যেমন: `price="20"`, সঠিক হবে `price={20}`).

### ১০. Interview questions related to this topic
1. **Props এবং State-এর প্রধান পার্থক্য কী?**
   * উত্তর: Props হলো বাইরে থেকে আসা রিড-অনলি ডেটা যা পরিবর্তন করা যায় না (Immutable)। State হলো কম্পোনেন্টের নিজস্ব লোকাল ডেটা যা যেকোনো সময় পরিবর্তন করা যায় (Mutable)।
2. **`props.children` কী?**
   * উত্তর: কোনো কম্পোনেন্টের ওপেনিং এবং ক্লোজিং ট্যাগের মাঝে যে কনটেন্ট বা চাইল্ড এলিমেন্ট দেওয়া হয়, তা রিসিভ করার জন্য `props.children` ব্যবহার করা হয়।
3. **React-এ প্রপস কি পরিবর্তনযোগ্য (Mutable)?**
   * উত্তর: না, প্রপস পুরোপুরি ইমিউটেবল (Immutable)।

### ১১. Best practices
* প্রপস রিসিভ করার সময় ES6 Destructuring ব্যবহার করুন (যেমন: `function User({ name, age })`).
* ডিফল্ট ভ্যালু সেট করার জন্য ES6 Default parameters ব্যবহার করুন (যেমন: `color = 'blue'`).
* বড় প্রজেক্টে প্রপসের টাইপ ভ্যালিডেশনের জন্য TypeScript বা `prop-types` লাইব্রেরি ব্যবহার করুন।

### ১২. Performance considerations
খুব বেশি নিচে প্রপস পাস করাকে **Props Drilling** বলে। এটি করলে মাঝখানের কম্পোনেন্টগুলো অপ্রয়োজনীয়ভাবে রি-রেন্ডার হতে পারে। এই সমস্যা এড়াতে React Context API বা Redux ব্যবহার করা হয়।

### ১৩. When NOT to use it
যদি কোনো ডেটা শুধুমাত্র একটি কম্পোনেন্টের ভেতরেই ব্যবহৃত হয় এবং অন্য কোনো কম্পোনেন্টের তা জানার দরকার না থাকে, তবে তা প্রপস হিসেবে না পাঠিয়ে লোকাল স্টেট হিসেবে রাখাই শ্রেয়।

### ১৪. Comparison with similar concepts
* **Props vs State:** Props হলো ইনপুট প্যারামিটার (বাইরে থেকে আসে), State হলো ইন্টারনাল স্টেট (ভেতরে তৈরি ও পরিবর্তিত হয়)।

### ১৫. Summary in simple Bangla
Props হলো প্যারেন্ট কম্পোনেন্ট থেকে চাইল্ড কম্পোনেন্টে ডেটা পাঠানোর একটা উপায়। এটি রিড-অনলি এবং একে পরিবর্তন করা যায় না।

### ১৬. 5 MCQ questions
1. Props সম্পর্কে কোনটি সঠিক?
   * A) এটি পরিবর্তনযোগ্য
   * B) এটি রিড-অনলি (ইমিউটেবল)
   * C) এটি শুধুমাত্র চাইল্ড থেকে প্যারেন্টে পাঠানো যায়
   * D) এটি শুধুমাত্র ক্লাস কম্পোনেন্টে চলে
   * *উত্তর: B*
2. প্রপস রিসিভ করার পর সরাসরি পরিবর্তন করার চেষ্টা করলে কী ঘটে?
   * A) React এরর দেয় (ইন-স্ট্রিক্ট মোড) অথবা ডেটা ফ্লো নষ্ট হয়
   * B) সফলভাবে আপডেট হয়ে যায়
   * C) ব্রাউজার ক্র্যাশ করে
   * D) কিছুই হয় না
   * *উত্তর: A*
3. চাইল্ড এলিমেন্ট পাস করার জন্য React-এর স্পেশাল প্রপ কোনটি?
   * A) props.content
   * B) props.elements
   * C) props.children
   * D) props.nodes
   * *উত্তর: C*
4. ডাইনামিক ইন্টিজার (যেমন `age = 25`) প্রপস হিসেবে পাঠানোর সঠিক উপায় কোনটি?
   * A) `age="25"`
   * B) `age={25}`
   * C) `age=[25]`
   * D) `age=25`
   * *উত্তর: B*
5. Props drilling দূর করার সমাধান কোনটি?
   * A) Context API
   * B) Redux
   * C) Component Composition
   * D) All of the above
   * *উত্তর: D*

### ১৭. 5 Coding exercises
1. একটি `UserCard` কম্পোনেন্ট বানান যা `name`, `email`, এবং `avatarUrl` প্রপস হিসেবে গ্রহণ করে রেন্ডার করবে।
2. একটি বাটন কম্পোনেন্ট তৈরি করুন যাতে প্রপ হিসেবে `color` ও `size` পাঠানো যাবে এবং সে অনুযায়ী বাটনের স্টাইল চেঞ্জ হবে।
3. `props.children` ব্যবহার করে একটি `Modal` কম্পোনেন্টের লেআউট ডিজাইন করুন।
4. একটি কম্পোনেন্ট লিখুন যা প্রপ হিসেবে একটি ফাংশন গ্রহণ করে এবং বাটনে ক্লিক করলে সেই ফাংশনটি এক্সিকিউট করে।
5. একটি প্রোডাক্ট লিস্ট কম্পোনেন্ট বানান যেখানে একটি প্রোডাক্টের অবজেক্ট প্রপ হিসেবে পাঠানো হবে এবং ডেস্ট্রাকচারিং ব্যবহার করে প্রপার্টিগুলো রেন্ডার করা হবে।

---

## ৪. State

### ১. Simple definition (বাংলায়)
State হলো একটি কম্পোনেন্টের নিজস্ব মেমরি বা অভ্যন্তরীণ ডেটা ভান্ডার। এটি কম্পোনেন্টের ভেতরেই তৈরি হয় এবং যেকোনো সময় পরিবর্তন হতে পারে। যখনই স্টেট পরিবর্তিত হয়, React সাথে সাথে সেই কম্পোনেন্ট এবং তার চাইল্ড কম্পোনেন্টগুলোকে রি-রেন্ডার (Re-render) করে নতুন ডেটা স্ক্রিনে দেখায়।

### ২. Why this concept exists
ইউজার ইন্টারফেসকে ইন্টারঅ্যাক্টিভ (dynamic/interactive) করার জন্য স্টেট প্রয়োজন। যেমন কোনো বাটন ক্লিক করলে কাউন্টার বাড়া, ফর্ম ফিল্ডে টাইপ করা, এপিআই থেকে ডেটা এনে পেজে দেখানো—এই সবকিছুই স্টেটের পরিবর্তনের মাধ্যমে হ্যান্ডেল করা হয়।

### ৩. What problem it solves
সাধারণ JavaScript ভ্যারিয়েবল পরিবর্তন করলে ব্রাউজারের UI নিজে থেকে আপডেট হয় না। State এই সমস্যার সমাধান করে। React স্টেটের পরিবর্তনের ওপর নজর রাখে এবং স্বয়ংক্রিয়ভাবে DOM আপডেট করে।

### ৪. Real-life analogy
একটি স্মার্ট বাল্বের কথা চিন্তা করুন। বাল্বটির বর্তমান অবস্থা (State) হতে পারে "ON" অথবা "OFF", এবং এর ব্রাইটনেস হতে পারে "50%"। আপনি যখন সুইচে চাপ দেন, তখন বাল্বটির ভেতরের স্টেট পরিবর্তিত হয় এবং সেই পরিবর্তন আপনি আলো জ্বলা বা নিভার মাধ্যমে সরাসরি দেখতে পান।

### ৫. How React works internally regarding this concept
React-এর Functional component-এ `useState` হুক ব্যবহার করে স্টেট ডিফাইন করা হয়। React মেমরিতে এই স্টেটের ভ্যালু একটি চেইনের মতো অর্ডারে সংরক্ষণ করে। যখন স্টেট আপডেট করার ফাংশন (যেমন `setCount`) কল করা হয়, React একটি রেন্ডার রিকোয়েস্ট শিডিউল করে। পরবর্তী রেন্ডারে React নতুন ভ্যালুটি প্রোভাইড করে এবং ভার্চুয়াল DOM কম্পারিজন করে স্ক্রিনে শুধু পরিবর্তিত অংশটুকু আপডেট করে।
স্টেট আপডেট সবসময় **Asynchronous** এবং **Batched** উপায়ে ঘটে (একই ইভেন্টে একাধিক স্টেট আপডেট থাকলে React সবগুলোকে একসাথে প্রসেস করে পারফরম্যান্স অপ্টিমাইজ করার জন্য)।

### ৬. Basic example
```jsx
import React, { useState } from 'react';

function LikeButton() {
  // Declaring state variable 'likes' with initial value 0
  const [likes, setLikes] = useState(0);

  return (
    <div style={{ textAlign: 'center', marginTop: '20px' }}>
      <p>Total Likes: {likes}</p>
      <button onClick={() => setLikes(likes + 1)}>
        Like
      </button>
    </div>
  );
}

export default LikeButton;
```

### ७. Step-by-step explanation of the code
* `const [likes, setLikes] = useState(0);`: এখানে `useState` হুকটি কল করে ইনিশিয়াল ভ্যালু `0` দেওয়া হয়েছে। এটি একটি অ্যারে রিটার্ন করে যার প্রথম ইলিমেন্ট বর্তমান স্টেট (`likes`) এবং দ্বিতীয় ইলিমেন্ট স্টেট পরিবর্তনের ফাংশন (`setLikes`)।
* `onClick={() => setLikes(likes + 1)}`: বাটনে ক্লিক করলে `setLikes` কল হয়ে স্টেট ১ বাড়িয়ে দেয়।
* স্টেট পরিবর্তন হওয়ার সাথে সাথে React পুরো কম্পোনেন্ট আবার রেন্ডার করে এবং নতুন `likes` ভ্যালু দেখায়।

### ৮. Another real-world example (Form input & toggle state)
```jsx
import React, { useState } from 'react';

function LoginForm() {
  const [username, setUsername] = useState('');
  const [showPassword, setShowPassword] = useState(false);

  return (
    <div className="login-box">
      <input 
        type="text" 
        placeholder="Enter username" 
        value={username} 
        onChange={(e) => setUsername(e.target.value)} 
      />
      <br />
      <input 
        type={showPassword ? "text" : "password"} 
        placeholder="Enter password" 
      />
      <button onClick={() => setShowPassword(!showPassword)}>
        {showPassword ? "Hide" : "Show"} Password
      </button>
      <p>Typing: {username}</p>
    </div>
  );
}
```

### ৯. Common mistakes beginners make
* **স্টেট সরাসরি পরিবর্তন করা:** `likes = likes + 1` লিখে স্টেট পরিবর্তনের চেষ্টা করা। এটি করলে React বুঝতে পারে না যে স্টেট চেঞ্জ হয়েছে, ফলে UI রি-রেন্ডার হয় না।
* **অ্যাসিনক্রোনাস বিহেভিয়ার না বোঝা:** স্টেট আপডেট করার সাথে সাথেই কনসোলে স্টেট দেখতে গেলে পুরোনো ভ্যালু পাওয়া যায়, কারণ স্টেট আপডেট অ্যাসিনক্রোনাসলি ঘটে।
  ```javascript
  setCount(count + 1);
  console.log(count); // এখানে পুরোনো count-ই দেখাবে!
  ```

### ১০. Interview questions related to this topic
1. **React State কেন অ্যাসিনক্রোনাসভাবে কাজ করে?**
   * উত্তর: পারফরম্যান্স অপ্টিমাইজেশনের জন্য। একাধিক স্টেট আপডেট একসাথে করার জন্য (Batching) React অ্যাসিনক্রোনাস মেকানিজম ব্যবহার করে, যাতে বারবার রেন্ডার হয়ে অ্যাপ স্লো না হয়।
2. **যদি পূর্ববর্তী স্টেটের (Previous State) ওপর ভিত্তি করে স্টেট আপডেট করতে হয়, তবে কীভাবে করা উচিত?**
   * উত্তর: ফাংশনাল স্টেট আপডেট ব্যবহার করে। যেমন: `setCount(prevCount => prevCount + 1)`.
3. **useState-এর ইনিশিয়াল স্টেট যদি কোনো জটিল ক্যালকুলেশন থেকে আসে, তবে কীভাবে অপ্টিমাইজ করবেন?**
   * উত্তর: Lazy Initialization ব্যবহার করে। `useState(() => computedHeavyValue())` এভাবে ফাংশন পাস করলে সেটি শুধু প্রথম রেন্ডারেই রান করবে।

### ১১. Best practices
* পূর্ববর্তী স্টেটের ওপর নির্ভর করে আপডেট করার সময় সবসময় callback ফাংশন ব্যবহার করুন (`setCount(prev => prev + 1)`)।
* স্টেটের স্ট্রাকচার যতটা সম্ভব ফ্ল্যাট (Flat) রাখুন, অতিরিক্ত নেস্টেড অবজেক্ট এভয়েড করুন।
* রিলেটেড স্টেটগুলোকে গ্রুপ করে একটি অবজেক্টে রাখতে পারেন যদি তারা সবসময় একসাথে পরিবর্তিত হয়।

### ১২. Performance considerations
স্টেট চেঞ্জ হলে পুরো কম্পোনেন্ট সাব-ট্রি রি-রেন্ডার হয়। তাই স্টেটকে সবসময় প্রয়োজনের চেয়ে ওপরে না রেখে যেখানে প্রয়োজন ঠিক সেই কম্পোনেন্টে রাখা উচিত (State Colocation)।

### ১৩. When NOT to use it
যদি কোনো ডেটা UI রেন্ডারে সরাসরি ভূমিকা না রাখে (যেমন কোনো API কী, টাইমার আইডি বা এনিমেশন অবজেক্ট), তবে তার জন্য স্টেট ব্যবহার করবেন না। সেক্ষেত্রে `useRef` ব্যবহার করা শ্রেয়।

### ১৪. Comparison with similar concepts
* **State vs Ref:** State আপডেট হলে UI রি-রেন্ডার হয়। `useRef` আপডেট হলে কোনো রি-রেন্ডার হয় না, মেমরিতে ডেটা ইনস্ট্যান্টলি আপডেট হয়।

### ১৫. Summary in simple Bangla
State হলো কম্পোনেন্টের ভেতরের ডাইনামিক মেমরি। কোনো ডেটা পরিবর্তনের কারণে যদি UI-তে পরিবর্তন আনার প্রয়োজন হয়, তবে আমরা স্টেট ব্যবহার করি। স্টেট পরিবর্তন হলে কম্পোনেন্ট স্বয়ংক্রিয়ভাবে রি-রেন্ডার হয়।

### १६. 5 MCQ questions
1. State পরিবর্তনের পর স্ক্রিনে আপডেট দেখানোর প্রক্রিয়াকে কী বলে?
   * A) Compiling
   * B) Mounting
   * C) Re-rendering
   * D) Transpiling
   * *উত্তর: C*
2. নিচের কোনটি স্টেট সরাসরি পরিবর্তন করার সঠিক উদাহরণ?
   * A) `count = count + 1`
   * B) `setCount(count + 1)`
   * C) `this.state.count = 2`
   * D) `count.update(2)`
   * *উত্তর: B*
3. স্টেট আপডেট করার সাথে সাথে কনসোল লক করলে আপডেট ভ্যালু না পাওয়ার কারণ কী?
   * A) State আপডেট Synchronous
   * B) State আপডেট Asynchronous
   * C) State পুরোপুরি Immutable
   * D) React Bug
   * *উত্তর: B*
4. Lazy Initialization-এর সঠিক সিনট্যাক্স কোনটি?
   * A) `useState(calculate())`
   * B) `useState(() => calculate())`
   * C) `useState(new calculate)`
   * D) `useState(async () => calculate())`
   * *উত্তর: B*
5. স্টেট পরিবর্তনের পর React UI আপডেট করার জন্য কী তুলনা করে?
   * A) Real DOM
   * B) Virtual DOM
   * C) CSSOM
   * D) Shadow DOM
   * *উত্তর: B*

### ১৭. 5 Coding exercises
1. একটি টোডো লিস্টের কাউন্টার তৈরি করুন যেখানে টোডো যোগ বা ডিলিট করলে টোটাল কাউন্ট আপডেট হবে।
2. একটি টগল বাটন বানান যা ক্লিক করলে একটি টেক্সট বক্স শো এবং হাইড করবে।
3. একটি সার্চ ইনপুট ফিল্ড তৈরি করুন এবং নিচে লিখুন "You are searching for: [input value]" যা রিয়েল-টাইমে আপডেট হবে।
4. একটি শপিং কার্ট কাউন্টার তৈরি করুন যেখানে `+` বাটনে ক্লিক করলে ১ বাড়বে এবং `-` বাটনে ক্লিক করলে ১ কমবে (কিন্তু কাউন্ট কখনো ০-এর নিচে যাবে না)।
5. একটি ফর্ম তৈরি করুন যেখানে নেস্টেড অবজেক্ট স্টেট (যেমন: `user: { name: '', city: '' }`) ব্যবহার করে ইউজারের ইনপুট আপডেট করবেন।
