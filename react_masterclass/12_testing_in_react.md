# React Testing Masterclass: Concept Clear Series

এই ডকুমেন্টে রিঅ্যাক্ট অ্যাপ্লিকেশনের টেস্টিং নিয়ে বিস্তারিত আলোচনা করা হয়েছে। প্রতিটি টপিকের জন্য ১৭-পয়েন্ট স্ট্রাকচার অনুসরণ করে গভীর ব্যাখ্যা প্রদান করা হলো।

---

## Topic 1: What are the different types of testing from a developer's perspective? (Manual, Unit, Integration, and End-to-End testing)

### ১. Simple Definition (বাংলায়)
ডেভেলপারের দৃষ্টিকোণ থেকে টেস্টিং হলো এমন একটি প্রক্রিয়া যার মাধ্যমে কোডের কার্যকারিতা, নির্ভরযোগ্যতা এবং আচরণ পরীক্ষা করা হয়। এটি প্রধানত চার প্রকার:
*   **Manual Testing:** কোনো অটোমেটেড স্ক্রিপ্ট ছাড়াই একজন মানুষ নিজে অ্যাপ্লিকেশনের বিভিন্ন ফিচার ক্লিক করে এবং ব্যবহার করে পরীক্ষা করে।
*   **Unit Testing:** অ্যাপ্লিকেশনের ক্ষুদ্রতম অংশ বা ইউনিট (যেমন একটি নির্দিষ্ট ফাংশন, মেথড বা কম্পোনেন্ট) অন্যান্য অংশ থেকে সম্পূর্ণ আলাদা বা আইসোলেটেড রেখে টেস্ট করা।
*   **Integration Testing:** একাধিক ইউনিট বা কম্পোনেন্ট যখন একত্রে যুক্ত হয়, তখন তারা একে অপরের সাথে সঠিকভাবে ডেটা আদান-প্রদান ও ইন্টারঅ্যাক্ট করছে কিনা তা পরীক্ষা করা।
*   **End-to-End (E2E) Testing:** বাস্তব গ্রাহক বা ইউজারের দৃষ্টিভঙ্গি থেকে সম্পূর্ণ অ্যাপ্লিকেশনটির শুরু থেকে শেষ পর্যন্ত (যেমন ডেটাবেস, নেটওয়ার্ক, ফ্রন্টএন্ড ও ব্যাকএন্ড) একসাথে টেস্ট করা।

### ২. Why this concept exists
সফটওয়্যার কোড বেস যত বড় হতে থাকে, এর জটিলতা তত বাড়ে। একটি ছোট পরিবর্তন অ্যাপ্লিকেশনের অন্য কোনো কোণায় থাকা ফিচারকে ভেঙে দিতে পারে। এই ঝুঁকি এড়াতে এবং কোডের মান বজায় রাখতে টেস্টিংয়ের ধারণার উৎপত্তি হয়েছে। প্রতিটি স্তরের টেস্টিংয়ের নিজস্ব উদ্দেশ্য রয়েছে, যা কোডের বিভিন্ন লেভেলের বাগ সনাক্ত করতে সাহায্য করে।

### ৩. What problem it solves
*   **Regression Issues:** নতুন কোড বা ফিচার যোগ করার পর পুরোনো ফিচার যেন ভেঙে না যায় (Regression) তা নিশ্চিত করে।
*   **Manual Effort reduction:** প্রতিবার সামান্য পরিবর্তনের পর পুরো অ্যাপ্লিকেশন ম্যানুয়ালি চেক করার সময় ও শ্রম বাঁচায়।
*   **High Confidence:** কোড প্রোডাকশনে পুশ করার আগে ডেভেলপারদের আত্মবিশ্বাস বাড়ায় যে তাদের কোড সঠিক এবং সুরক্ষিত।
*   **Faster Delivery:** অটোমেটেড পাইপলাইনের মাধ্যমে দ্রুত রিলিজ দেওয়া সম্ভব হয়।

### ৪. Real-life analogy
একটি গাড়ি প্রস্তুতকারী কোম্পানির সাথে তুলনা করা যাক:
*   **Unit Testing:** চাকা, পিস্টন, গিয়ার বা লাইটের মতো প্রতিটি যন্ত্রাংশ আলাদাভাবে ল্যাবে পরীক্ষা করা যে সেগুলো ঠিকমতো ঘোরে বা জ্বলে কিনা।
*   **Integration Testing:** ইঞ্জিন এবং গিয়ার বক্স একত্রে ফিট করার পর গিয়ার পরিবর্তন করলে ইঞ্জিনের স্পিড বাড়ে কিনা তা পরীক্ষা করা।
*   **End-to-End Testing:** সম্পূর্ণ গাড়িটি এসেম্বল করার পর একজন চালক নিজে স্টিয়ারিং হুইলে বসে গাড়িটি স্টার্ট দিয়ে রাস্তায় চালিয়ে দেখা যে সেটি ব্রেক, হর্ন এবং এসি সহ গন্তব্যে পৌঁছাতে পারছে কিনা।
*   **Manual Testing:** গাড়ি শোরুমে তোলার আগে একজন পরিদর্শক হেঁটে হেঁটে বডি স্ক্র্যাচ বা সিটের কভার হাত দিয়ে চেপে দেখা।

### ৫. How React works internally regarding this concept
React মূলত একটি Virtual DOM (VDOM) ভিত্তিক লাইব্রেরি।
*   **Unit Testing (React):** React internally কম্পোনেন্টটিকে একটি লাইটওয়েট মেমোরি রিপ্রেজেন্টেশনে (Virtual DOM) রেন্ডার করে। Jest বা JSDOM-এর মতো টুল ব্যবহার করে React.createElement বা JSX-কে নোড অবজেক্টে রূপান্তর করা হয় এবং প্রপস (Props) বা স্টেট (State)-এর পরিবর্তনের ফলে সঠিক আউটপুট তৈরি হচ্ছে কিনা তা পরীক্ষা করা হয়।
*   **Integration Testing (React):** একাধিক প্যারেন্ট-চাইল্ড কম্পোনেন্টের রি-রেন্ডারিং সাইকেল এবং স্টেট আপডেটের ট্র্যাকিং কীভাবে একে অপরের ডম ট্রি-তে প্রভাব ফেলছে তা রেন্ডার করে টেস্ট করা হয়।
*   **E2E Testing (React):** Cypress বা Playwright-এর মতো ফ্রেমওয়ার্কগুলো রিঅ্যাক্টের ভার্চুয়াল ডমের বাইরে গিয়ে সরাসরি রিয়েল ব্রাউজারে অ্যাপটি লোড করে। ব্রাউজারের মূল Rendering Engine-এ রিঅ্যাক্টের প্রোডাকশন বান্ডেলটি রেন্ডার হয় এবং রিয়েল ক্লিক ও ইনপুট ইভেন্ট ট্রিগার করা হয়।

### ৬. Basic example
এখানে একটি সহজ `Counter` কম্পোনেন্ট এবং এর Unit ও Integration টেস্টের উদাহরণ দেওয়া হলো:

**Counter.jsx**
```jsx
import React, { useState } from 'react';

export function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div>
      <h1 data-testid="counter-value">{count}</h1>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </div>
  );
}
```

**Counter.test.jsx**
```jsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Counter } from './Counter';

describe('Counter Unit and Integration Test', () => {
  test('should render initial value as 0 (Unit Test)', () => {
    render(<Counter />);
    const counterValue = screen.getByTestId('counter-value');
    expect(counterValue).toHaveTextContent('0');
  });

  test('should increment value on button click (Integration/Behavior Test)', () => {
    render(<Counter />);
    const button = screen.getByRole('button', { name: /increment/i });
    const counterValue = screen.getByTestId('counter-value');

    fireEvent.click(button);

    expect(counterValue).toHaveTextContent('1');
  });
});
```

### ৭. Step-by-step explanation of the code
১. `render(<Counter />)`-এর মাধ্যমে আমরা কম্পোনেন্টটিকে মেমোরিতে একটি ভার্চুয়াল ডম (JSDOM) ট্রিতে রূপান্তর করি।
২. `screen.getByTestId('counter-value')` কুয়েরি ব্যবহার করে আমরা `data-testid="counter-value"` বিশিষ্ট নির্দিষ্ট HTML এলিমেন্টটি খুঁজে বের করি।
৩. প্রথম টেস্ট কেসে, `expect(counterValue).toHaveTextContent('0')` অ্যাসারশন চেক করে যে ইনিশিয়াল স্টেট অনুযায়ী কাউন্টারের মান শূন্য (0) আছে কিনা।
৪. দ্বিতীয় টেস্ট কেসে, আমরা `screen.getByRole` দিয়ে বাটনটি ধরি এবং `fireEvent.click(button)` ব্যবহারের মাধ্যমে ভার্চুয়াল ডমে বাটনের ক্লিক ইভেন্টটি ফায়ার করি।
৫. ক্লিক করার পর React-এর ইন্টারনাল `useState` ট্রিগার হয়, কম্পোনেন্টটি রি-রেন্ডার হয় এবং ডমে নতুন কাউন্টার ভ্যালু ১ আপডেট করে।
৬. সবশেষে, `expect(counterValue).toHaveTextContent('1')` যাচাই করে যে স্টেট আপডেট এবং UI রি-রেন্ডারিং ইন্টিগ্রেশন ঠিকভাবে কাজ করেছে।

### ৮. Another real-world example
ধরা যাক একটি e-Commerce সাইটের Shopping Cart ফিচার।
*   **Unit Test:** একটি একক `ProductCard` কম্পোনেন্ট রেন্ডার করে প্রপস হিসেবে পাঠানো নাম ও দাম ঠিকমতো দেখাচ্ছে কিনা তা চেক করা।
*   **Integration Test:** `ProductList` এবং `CartSummary` একসাথে রেন্ডার করা। `ProductCard`-এর "Add to Cart" বাটনে ক্লিক করলে `CartSummary` কম্পোনেন্টে মোট পণ্যের সংখ্যা ও মোট মূল্য স্বয়ংক্রিয়ভাবে বাড়ছে কিনা তা পরীক্ষা করা।
*   **E2E Test:** ইউজার সাইটে প্রবেশ করবে, প্রোডাক্ট সার্চ করবে, কার্টে যুক্ত করবে, শিপিং অ্যাড্রেস ফিলাপ করবে এবং একটি মক পেমেন্ট গেটওয়ের মাধ্যমে অর্ডার সফলভাবে প্লেস করবে।

### ৯. Common mistakes beginners make
*   **Writing too many E2E tests:** E2E টেস্ট অনেক স্লো এবং রিসোর্স ইনটেনসিভ। নতুনরা প্রায় সব ফিচারের জন্য E2E টেস্ট লিখতে চায়, যা রান হতে প্রচুর সময় নেয়।
*   **Testing Implementation Details in Unit Tests:** কম্পোনেন্টের ইন্টারনাল স্টেট বা ফাংশন সরাসরি টেস্ট করা (যেমন: `wrapper.state('count')`) ভুল। টেস্ট সবসময় ইউজারের ভিজ্যুয়াল বিহেভিয়ারের উপর ভিত্তি করে হওয়া উচিত।
*   **Not Mocking API Calls:** ইউনিট ও ইন্টিগ্রেশন টেস্টের সময় আসল সার্ভারে API রিকোয়েস্ট পাঠানো। এর ফলে ইন্টারনেট কানেকশন বা সার্ভার ডাউন থাকলে টেস্ট ফেইল করবে।

### ১০. Interview questions related to this topic
১. **Question:** What is the Testing Pyramid?
   *   **Answer:** Testing Pyramid হলো এমন একটি ধারণা যা নির্দেশ করে যে টেস্ট স্যুটে ইউনিট টেস্টের সংখ্যা সবচেয়ে বেশি হওয়া উচিত, ইন্টিগ্রেশন টেস্ট মাঝারি এবং এন্ড-টু-এন্ড (E2E) টেস্টের সংখ্যা সবচেয়ে কম হওয়া উচিত কারণ E2E টেস্ট অনেক স্লো এবং রক্ষণাবেক্ষণ করা কঠিন।
২. **Question:** How do you test a component that makes an asynchronous API fetch call?
   *   **Answer:** `jest.mock` বা `msw` (Mock Service Worker) ব্যবহার করে নেটওয়ার্ক রিকোয়েস্ট মক করতে হবে এবং React Testing Library-র `findBy` কুয়েরি ও `await` ব্যবহার করে অ্যাসিনক্রোনাস ডেটা ডমে রেন্ডার হওয়া পর্যন্ত অপেক্ষা করতে হবে।
৩. **Question:** What is regression testing?
   *   **Answer:** যখন কোডবেসে কোনো পরিবর্তন বা বাগ ফিক্সিং করা হয়, তখন পূর্বের ফিচারগুলো নষ্ট হয়ে যায়নি তা নিশ্চিত করার জন্য যে টেস্টগুলো পুনরায় চালানো হয় তাকে রিগ্রেশন টেস্টিং বলে।
৪. **Question:** What is the difference between Integration testing and E2E testing in React?
   *   **Answer:** Integration টেস্টে রিঅ্যাক্ট কম্পোনেন্টগুলোর পারস্পরিক ডেটা আদান-প্রদান JSDOM-এ টেস্ট করা হয় (কোনো রিয়েল ডেটাবেস বা লাইভ নেটওয়ার্ক ছাড়াই)। E2E টেস্টে একটি রিয়েল ব্রাউজারের সাহায্যে পুরো সিস্টেম (ডাটাবেস, ব্যাকএন্ড API এবং ফ্রন্টএন্ড) একসাথে এন্ড-টু-এন্ড পরীক্ষা করা হয়।
৫. **Question:** Why is Manual Testing not sufficient for modern web applications?
   *   **Answer:** ম্যানুয়াল টেস্টিং সময়সাপেক্ষ, মানুষের ভুলের (Human error) সম্ভাবনা থাকে, রিগ্রেশন ট্র্যাকিং কঠিন এবং কোড স্কেল করার সাথে সাথে ম্যানুয়ালি সব ফিচার চেক করা অসম্ভব হয়ে দাঁড়ায়।

### ১১. Best practices
*   **Follow the Testing Trophy:** ফ্রন্টএন্ড অ্যাপ্লিকেশনের জন্য ইন্টিগ্রেশন টেস্টের উপর বেশি জোর দিন, কারণ এটি কম খরচে সর্বোচ্চ রিটার্ন এবং কনফিডেন্স দেয়।
*   **Focus on User Interactions:** টেস্টের কোড এমনভাবে লিখুন যেন তা একজন আসল ইউজারের কার্যকলাপ নকল করে (যেমন `fireEvent` বা `userEvent` ব্যবহার করা)।
*   **Run tests in CI/CD:** প্রতিবার গিটহাবে কোড পুশ করার সময় GitHub Actions বা Jenkins-এর মাধ্যমে অটোমেটিক টেস্ট রান করুন।

### ১২. Performance considerations
*   **Avoid excessive nesting in describe blocks:** অতিরিক্ত নেস্টিং টেস্ট এক্সিকিউশন রিডারবিলিটি ও পারফরম্যান্স কমায়।
*   **Parallelization:** Jest ডিফল্টভাবে প্যারালালি টেস্ট ফাইল রান করে। এই ফিচারটি ব্যবহার করার জন্য টেস্ট ফাইলগুলোকে আলাদা আলাদা মডিউলে ছোট করে রাখুন।
*   **Limit E2E runs:** শুধুমাত্র প্রোডাকশন রিলিজের আগে বা বড় পুল রিকোয়েস্ট মার্জ করার সময় E2E টেস্ট রান করার জন্য পাইপলাইন সেট করুন।

### ১৩. When NOT to use it
*   **Static and trivial components:** যে কম্পোনেন্টগুলোতে কোনো ডাইনামিক লজিক বা স্টেট নেই (যেমন একটি সাধারণ লোগো বা ফুটার টেক্সট), সেগুলোতে জটিল ইন্টিগ্রেশন বা E2E টেস্ট লেখার প্রয়োজন নেই।
*   **Rapid Prototyping:** যখন আপনি একটি কনসেপ্ট প্রমাণ করার জন্য দ্রুত রাফ কোড লিখছেন, তখন টেস্ট না লিখে ফিচার ডেভেলপমেন্টে ফোকাস করা উচিত।

### ১৪. Comparison with similar concepts

| Feature | Manual Testing | Unit Testing | Integration Testing | E2E Testing |
| :--- | :--- | :--- | :--- | :--- |
| **Execution Speed** | Very Slow | Extremely Fast | Fast / Medium | Very Slow |
| **Setup Cost** | Low | Medium | Medium | High |
| **Confidence Level** | Medium | Low | High | Extremely High |
| **Maintenance** | Low | High | Medium | High |
| **Mocking Needed** | No | Highly Needed | Partially Needed| Minimal / None |

### ১৫. Summary in simple Bangla
ডেভেলপারদের জন্য চার ধরণের টেস্টিং জানা জরুরি। ইউনিট টেস্ট ছোট ছোট অংশগুলোকে আলাদাভাবে পরীক্ষা করে। ইন্টিগ্রেশন টেস্ট একাধিক অংশ একসাথে কাজ করছে কিনা তা দেখে। এন্ড-টু-এন্ড (E2E) টেস্ট ব্রাউজারে আসল ইউজারের মতো করে সম্পূর্ণ অ্যাপ রান করায়। আর ম্যানুয়াল টেস্ট হলো নিজেই হাত দিয়ে ক্লিক করে দেখা। আমাদের লক্ষ্য হওয়া উচিত এমন একটি ব্যালেন্স তৈরি করা যাতে খুব দ্রুত ও কম খরচে সর্বোচ্চ কোয়ালিটি নিশ্চিত করা যায়।

### ১৬. 5 MCQ questions (with answers)
১. কোন ধরণের টেস্টিংয়ে একটি কম্পোনেন্টকে তার চারপাশের সমস্ত ডিপেন্ডেন্সি থেকে আলাদা করে টেস্ট করা হয়?
   ক) Integration Testing
   খ) Unit Testing
   গ) E2E Testing
   ঘ) Manual Testing
   **উত্তর:** খ

২. Testing Trophy-তে কোন ধরণের টেস্টিংকে সবচেয়ে বেশি গুরুত্ব দেওয়া হয়?
   ক) Static
   খ) Unit
   গ) Integration
   ঘ) E2E
   **উত্তর:** গ

৩. E2E টেস্টিং করার জন্য নিচের কোন টুলটি বহুল ব্যবহৃত?
   ক) Jest
   খ) Enzyme
   গ) Cypress
   ঘ) React Testing Library
   **উত্তর:** গ

৪. কোডে নতুন ফিচার যোগ করার পর পূর্বের ফিচারগুলো ভেঙে গেছে কিনা তা নিশ্চিত করার পরীক্ষাকে কী বলে?
   ক) Alpha Testing
   খ) Beta Testing
   গ) Regression Testing
   ঘ) Stress Testing
   **উত্তর:** গ

৫. নিচের কোন টেস্টিং টাইপটি সবচেয়ে স্লো এবং রান করতে সবচেয়ে বেশি রিসোর্স ও সময় নেয়?
   ক) Unit Test
   খ) Manual Test
   গ) Integration Test
   ঘ) E2E Test
   **উত্তর:** ঘ

### ১৭. 5 Coding exercises (with solutions)

**Exercise 1:** একটি `Greeting` কম্পোনেন্ট দেওয়া হলো যা প্রপস হিসেবে নাম গ্রহণ করে। এটার জন্য একটি Unit Test লিখুন যা যাচাই করবে যে নামটি স্ক্রিনে রেন্ডার হচ্ছে কিনা।
```jsx
// Greeting.jsx
import React from 'react';
export function Greeting({ name }) {
  return <h1>Hello, {name}!</h1>;
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Greeting } from './Greeting';

test('renders hello with correct name', () => {
  render(<Greeting name="Rohit" />);
  const heading = screen.getByRole('heading', { level: 1 });
  expect(heading).toHaveTextContent('Hello, Rohit!');
});
```

**Exercise 2:** একটি `ToggleButton` কম্পোনেন্ট আছে যা ক্লিক করলে টেক্সট "ON" এবং "OFF" এর মধ্যে পরিবর্তন হয়। এর জন্য একটি Integration/Behavior Test লিখুন।
```jsx
// ToggleButton.jsx
import React, { useState } from 'react';
export function ToggleButton() {
  const [isOn, setIsOn] = useState(false);
  return (
    <button onClick={() => setIsOn(!isOn)}>
      {isOn ? 'ON' : 'OFF'}
    </button>
  );
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ToggleButton } from './ToggleButton';

test('toggles text on click', () => {
  render(<ToggleButton />);
  const button = screen.getByRole('button');
  expect(button).toHaveTextContent('OFF');
  
  fireEvent.click(button);
  expect(button).toHaveTextContent('ON');
  
  fireEvent.click(button);
  expect(button).toHaveTextContent('OFF');
});
```

**Exercise 3:** একটি `UserInfo` কম্পোনেন্ট এপিআই থেকে ডেটা ফেচ করে দেখায়। Jest-এর মকিং ব্যবহার করে এর ইউনিট টেস্ট লিখুন।
```jsx
// UserInfo.jsx
import React, { useEffect, useState } from 'react';
export function UserInfo() {
  const [user, setUser] = useState(null);
  useEffect(() => {
    fetch('/api/user')
      .then(res => res.json())
      .then(data => setUser(data.name));
  }, []);
  if (!user) return <div>Loading...</div>;
  return <div data-testid="username">{user}</div>;
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import { UserInfo } from './UserInfo';

beforeEach(() => {
  global.fetch = jest.fn(() =>
    Promise.resolve({
      json: () => Promise.resolve({ name: 'John Doe' }),
    })
  );
});

afterEach(() => {
  jest.restoreAllMocks();
});

test('fetches and displays username', async () => {
  render(<UserInfo />);
  expect(screen.getByText('Loading...')).toBeInTheDocument();
  
  const username = await screen.findByTestId('username');
  expect(username).toHaveTextContent('John Doe');
});
```

**Exercise 4:** এমন একটি টেস্ট লিখুন যা যাচাই করবে কোনো একটি বাটন এলিমেন্ট ডিজেবলড (disabled) অবস্থায় আছে কিনা।
```jsx
// CustomButton.jsx
import React from 'react';
export function CustomButton({ disabled }) {
  return <button disabled={disabled}>Submit</button>;
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { CustomButton } from './CustomButton';

test('button is disabled when disabled prop is true', () => {
  render(<CustomButton disabled={true} />);
  const button = screen.getByRole('button', { name: /submit/i });
  expect(button).toBeDisabled();
});
```

**Exercise 5:** একটি `Form` কম্পোনেন্টে ইউজার ইনপুট দিয়ে সাবমিট করার পর ফর্মের সাবমিট হ্যান্ডলার ট্রিগার হচ্ছে কিনা তার ইন্টিগ্রেশন টেস্ট লিখুন।
```jsx
// Form.jsx
import React, { useState } from 'react';
export function Form({ onSubmit }) {
  const [text, setText] = useState('');
  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(text);
  };
  return (
    <form onSubmit={handleSubmit}>
      <input 
        type="text" 
        value={text} 
        onChange={(e) => setText(e.target.value)} 
        placeholder="Enter text"
      />
      <button type="submit">Submit</button>
    </form>
  );
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Form } from './Form';

test('calls onSubmit with entered text', () => {
  const mockOnSubmit = jest.fn();
  render(<Form onSubmit={mockOnSubmit} />);
  
  const input = screen.getByPlaceholderText('Enter text');
  const button = screen.getByRole('button', { name: /submit/i });
  
  fireEvent.change(input, { target: { value: 'Hello Jest' } });
  fireEvent.click(button);
  
  expect(mockOnSubmit).toHaveBeenCalledTimes(1);
  expect(mockOnSubmit).toHaveBeenCalledWith('Hello Jest');
});
```

---

## Topic 2: What is the role of React Testing Library (RTL) vs Jest?

### ১. Simple Definition (বাংলায়)
রিঅ্যাক্ট অ্যাপ্লিকেশনে টেস্টিং করার সময় দুটি আলাদা ক্যাটাগরির টুল ব্যবহার করা হয়:
*   **Jest:** এটি একটি পূর্ণাঙ্গ **Test Runner** এবং **Assertion Library**। এটি টেস্ট ফাইল খুঁজে বের করে, সেগুলো রান করে, কোড মকিংয়ের সুবিধা দেয় এবং টেস্টের ফলাফল দেখায়।
*   **React Testing Library (RTL):** এটি একটি **Rendering/Utility Library** যা রিঅ্যাক্ট কম্পোনেন্টকে JSDOM-এ রেন্ডার করতে এবং ডম এলিমেন্ট কুয়েরি ও ট্র্যাক করতে সাহায্য করে।

### ২. Why this concept exists
টেস্ট করার জন্য আমাদের দুটি জিনিসের প্রয়োজন হয়:
১. এমন একটি পরিবেশ যা টেস্ট কোডটি চালাবে এবং ফলাফল দেবে (Test Runner)।
২. এমন একটি টুল যা রিঅ্যাক্ট কম্পোনেন্ট রেন্ডার করবে এবং ইউজারের মতো ইন্টারঅ্যাক্ট করার সুবিধা দেবে (DOM Renderer)।
এই দায়িত্ব দুটি আলাদা করার জন্য Jest এবং RTL আলাদাভাবে কাজ করে এবং একসাথে মিলে একটি চমৎকার টেস্টিং ইকোসিস্টেম তৈরি করে।

### ৩. What problem it solves
*   Jest ছাড়া আপনি কম্পোনেন্ট টেস্ট রান করার জন্য টেস্ট স্যুটের স্ট্রাকচার (`describe`, `test`), অ্যাসারশন (`expect`) এবং মকিং ইভেন্ট পাবেন না।
*   RTL ছাড়া Jest একা একা রিঅ্যাক্ট কম্পোনেন্ট (JSX)-কে ব্রাউজার বা JSDOM-এর উপযোগী করে রেন্ডার করতে পারে না এবং ডমের এলিমেন্টগুলোকে ইউজারের মতো করে সিলেক্ট করতে পারে না।

### ৪. Real-life analogy
একটি নাটক বা থিয়েটারের সাথে এটি তুলনা করা যেতে পারে:
*   **Jest হলো থিয়েটার হল ও তার ম্যানেজার:** এটি ঠিক করে কখন নাটক শুরু হবে, দর্শকরা সিটে বসবে কিনা (test running), আলো জ্বলবে কিনা এবং সব নিয়ম ঠিকমতো মানা হচ্ছে কিনা (assertion)।
*   **React Testing Library (RTL) হলো মঞ্চের অভিনেতা ও সাজসজ্জা:** এটি সরাসরি পারফর্ম করে (render components) এবং কার পরে কে ডায়লগ দেবে বা কোন প্রপ্স ব্যবহার করবে তা নিয়ন্ত্রণ করে। ম্যানেজার (Jest) ছাড়া নাটক টিম কাজ শুরু করতে পারে না, আবার পারফর্মার (RTL) ছাড়া ম্যানেজার কাকে দিয়ে কাজ করাবে!

### ৫. How React works internally regarding this concept
*   RTL ইন্টারনালি রিঅ্যাক্টের `react-dom/client` এর `createRoot` এবং `render` মেথড ব্যবহার করে কম্পোনেন্টকে JSDOM (একটি ইন-মেমোরি ব্রাউজার ডম সিমুলেটর)-এ মাউন্ট করে।
*   রেন্ডার করার পর RTL ব্রাউজার-এর ডম এপিআই (যেমন `querySelector`, `evaluate`) ব্যবহার করে ডম নোডগুলো কুয়েরি করার ইন্টারফেস দেয়।
*   Jest ইন্টারনালি Node.js এনভায়রনমেন্টে চলে। এটি গ্লোবাল অবজেক্ট হিসেবে `describe`, `it`, `expect` ইনজেক্ট করে। যখন RTL কোনো নোড খুঁজে পায়, তখন Jest সেই নোডের অ্যাকচুয়াল স্ট্যাটাস (যেমন টেক্সট কন্টেন্ট বা ক্লাস) নিয়ে তার নিজস্ব এসারশন ইঞ্জিন দিয়ে ভ্যালিডেট করে।

### ৬. Basic example
**SimpleComponent.jsx**
```jsx
import React from 'react';
export function SimpleComponent() {
  return <p>Welcome to React testing!</p>;
}
```

**SimpleComponent.test.jsx**
```jsx
import React from 'react';
import { render, screen } from '@testing-library/react'; // RTL imports
import { SimpleComponent } from './SimpleComponent';

describe('Simple Component Tests', () => { // Jest global function
  test('should display welcome message', () => { // Jest global function
    render(<SimpleComponent />); // RTL API
    const message = screen.getByText('Welcome to React testing!'); // RTL API
    expect(message).toBeInTheDocument(); // Jest matcher (extended by jest-dom)
  });
});
```

### ৭. Step-by-step explanation of the code
১. `describe` এবং `test` হলো Jest-এর গ্লোবাল মেথড যা টেস্টকে সংগঠিত এবং রান করতে সাহায্য করে।
২. `render(<SimpleComponent />)` হলো RTL-এর ফাংশন যা `SimpleComponent`-কে JSDOM-এ রেন্ডার করে।
৩. `screen.getByText` হলো RTL-এর কোয়েরি যা ডমের ভেতরে নির্দিষ্ট টেক্সটটি খুঁজে বের করে।
৪. `expect(message).toBeInTheDocument()` অংশে `expect` হলো Jest-এর অ্যাসারশন লাইব্রেরি এবং `toBeInTheDocument()` হলো `@testing-library/jest-dom` দ্বারা বর্ধিত একটি Jest ম্যাচার, যা চেক করে এলিমেন্টটি আসলেই ডমে উপস্থিত আছে কিনা।

### ৮. Another real-world example
একটি শপিং অ্যাপে লয়ালটি ডিসকাউন্ট ক্যালকুলেটর ফাংশন এবং একটি কার্ট কম্পোনেন্ট রয়েছে।
*   **শুধু Jest ব্যবহার:** ডিসকাউন্ট লজিক ফাংশন `calculateDiscount(price, userLevel)` এর ইনপুট-আউটপুট টেস্ট করতে কোনো রিঅ্যাক্ট কম্পোনেন্ট রেন্ডার করা লাগে না। তাই শুধু Jest দিয়ে `expect(calculateDiscount(100, 'VIP')).toBe(80)` টেস্ট করা হয়।
*   **Jest + RTL ব্যবহার:** সেই ডিসকাউন্টটি যখন `CheckoutForm` রিঅ্যাক্ট কম্পোনেন্টে স্ক্রিনে রেন্ডার করে দেখাতে হবে, তখন RTL ব্যবহার করে কম্পোনেন্টটি রেন্ডার করতে হবে এবং Jest দিয়ে চেক করতে হবে স্ক্রিনের মোট মূল্য আপডেট হয়েছে কিনা।

### ৯. Common mistakes beginners make
*   **Confusing wrapper with screen:** অনেক সময় বিগিনাররা `const wrapper = render(<App />)` করে `wrapper` দিয়ে সবকিছু করার চেষ্টা করে। আধুনিক বেস্ট প্র্যাকটিস হলো সরাসরি `screen` অবজেক্ট ব্যবহার করে কুয়েরি করা।
*   **Adding unnecessary cleanups:** RTL বর্তমানে প্রতিটি টেস্টের পর স্বয়ংক্রিয়ভাবে ডম ক্লিনআপ করে নেয়। নতুনরা বারবার ম্যানুয়ালি `afterEach(cleanup)` লেখে যা অপ্রয়োজনীয়।
*   **Using container query selectors:** `container.querySelector('div > button')` টাইপ কুয়েরি ব্যবহার করা। এটি ইমপ্লিমেন্টেশন ডিটেইলের সাথে কোডকে টাইটলি কাপল্ড করে দেয়।

### ১০. Interview questions related to this topic
১. **Question:** Can we run React Testing Library without Jest?
   *   **Answer:** হ্যাঁ, RTL রানার নিরপেক্ষ (runner agnostic)। Jest-এর পরিবর্তে Mocha, Jasmine, Vitest বা অন্য যেকোনো টেস্ট রানারের সাথে RTL ব্যবহার করা সম্ভব।
২. **Question:** What is the difference between `queryBy`, `getBy`, and `findBy` in RTL?
   *   **Answer:**
       *   `getBy`: এলিমেন্ট না পেলে সাথে সাথে এরর থ্রো করে।
       *   `queryBy`: এলিমেন্ট না পেলে `null` রিটার্ন করে (এলিমেন্ট ডমে নেই তা টেস্ট করার জন্য উপযোগী)।
       *   `findBy`: একটি প্রমিজ (Promise) রিটার্ন করে যা অ্যাসিনক্রোনাস এলিমেন্ট আসার জন্য অপেক্ষা করে।
৩. **Question:** What does `@testing-library/jest-dom` do?
   *   **Answer:** এটি Jest-এর জন্য কিছু কাস্টম ডম ম্যাচার প্রদান করে (যেমন `toBeInTheDocument()`, `toHaveClass()`, `toBeDisabled()`), যা ডম এলিমেন্ট টেস্ট করা সহজ করে।
৪. **Question:** How does Jest search for test files?
   *   **Answer:** Jest তার কনফিগারেশনে থাকা `testRegex` বা `testMatch` প্যাটার্ন অনুযায়ী `__tests__` ফোল্ডারের ভেতরের ফাইল অথবা `.test.js` / `.spec.js` এক্সটেনশনের ফাইলগুলো খুঁজে বের করে।
৫. **Question:** What is Jest mocking?
   *   **Answer:** Jest-এর মাধ্যমে আমরা কোনো মডিউল, ফাংশন বা এপিআই কলকে ফেক বা ডামি ডেটা দিয়ে রিপ্লেস করে টেস্ট রান করতে পারি যাতে বাইরের নেটওয়ার্ক বা জটিল লজিকের ওপর টেস্টের ফলাফল নির্ভর না করে।

### ১১. Best practices
*   **Use `screen.debug()` for debugging:** টেস্টের কোনো পর্যায়ে ডমের অবস্থা দেখতে চাইলে `screen.debug()` ব্যবহার করুন।
*   **Prefer accessibility queries:** এলিমেন্ট খোঁজার জন্য আইডি বা ক্লাস ব্যবহার না করে অ্যাক্সেসিবিলিটি ভিত্তিক কোয়েরি যেমন `getByRole`, `getByLabelText` ব্যবহার করুন।
*   **Keep tests independent:** প্রতিটি টেস্ট যেন আগের টেস্টের স্টেট বা ফলাফলের উপর নির্ভর না করে তা নিশ্চিত করুন।

### ১২. Performance considerations
*   **Use `userEvent` instead of `fireEvent` carefully:** `userEvent` অনেক বেশি বাস্তবসম্মত ইভেন্ট ফায়ার করে (যেমন টাইপ করার সময় কী-ডাউন, কী-আপ ট্রিগার হওয়া), তবে এটি `fireEvent` থেকে কিছুটা স্লো হতে পারে। খুব বড় ফাইলে ব্যালেন্স করে ব্যবহার করা উচিত।
*   **Optimize Jest config:** `jest.config.js` ফাইলে `watchPlugins` এবং `moduleNameMapper` অপ্রয়োজনীয়ভাবে জটিল না করা।

### ১৩. When NOT to use it
*   **Testing pure javascript helper functions:** যখন কোনো ফাংশন রিঅ্যাক্ট কম্পোনেন্ট বা UI-এর সাথে যুক্ত নয় (যেমন ইউটিলিটি ফরম্যাটার বা গাণিতিক হিসাব), তখন RTL ব্যবহার করার কোনো প্রয়োজন নেই। শুধু Jest ব্যবহার করলেই চলে।

### ১৪. Comparison with similar concepts

| Criteria | Jest | React Testing Library (RTL) |
| :--- | :--- | :--- |
| **Primary Role** | Test Runner, Assertion & Mocks | Component DOM Rendering & Querying |
| **Dependency** | Works independently | Needs a Test Runner (like Jest/Vitest) to execute |
| **DOM access** | No direct DOM utilities | Provides rich set of DOM querying APIs |
| **Global variables** | Provides `describe`, `test`, `expect`, `jest` | Does not provide any globals |

### ১৫. Summary in simple Bangla
সহজ কথায়, Jest হলো চালক (Driver) যে পুরো টেস্ট স্যুট চালায় এবং চেক করে ফলাফল সঠিক কিনা। আর React Testing Library হলো একটি মেকানিক টুলবক্স যা দিয়ে আমরা রিঅ্যাক্ট কম্পোনেন্টকে স্ক্রিনে এনে তার ভেতরের বাটন, টেক্সট ইত্যাদি টেনে বের করে ইউজারের মতো টগল করে দেখতে পারি। এই দুটি টুল একসাথে চমৎকারভাবে কাজ করে।

### ১৬. 5 MCQ questions (with answers)
১. কোনটি টেস্ট রানার হিসেবে কাজ করে?
   ক) React Testing Library
   খ) Jest
   গ) Enzyme
   ঘ) JSDOM
   **উত্তর:** খ

২. এলিমেন্ট ডমে না থাকলে কোন কোয়েরি মেথডটি এরর থ্রো না করে `null` রিটার্ন করে?
   ক) getByText
   খ) findByText
   গ) queryByText
   ঘ) screen.text
   **উত্তর:** গ

৩. `@testing-library/jest-dom` এর কাজ কী?
   ক) রিঅ্যাক্ট কম্পোনেন্ট কম্পাইল করা
   খ) Jest-এ কাস্টম ডম ম্যাচার যোগ করা
   গ) ব্রাউজার উইন্ডো ওপেন করা
   ঘ) টেস্ট ফাইল খোঁজা
   **উত্তর:** খ

৪. Jest টেস্ট ফাইলগুলো খোঁজার জন্য ডিফল্টভাবে কোন এক্সটেনশন ট্র্যাক করে?
   ক) .config.js
   খ) .test.js বা .spec.js
   গ) .component.js
   ঘ) .run.js
   **উত্তর:** খ

৫. React Testing Library মূলত কোনটির ওপর ফোকাস করে টেস্ট লেখার উৎসাহ দেয়?
   ক) Component's internal state
   খ) Component's private methods
   গ) User behavior and accessibility
   ঘ) Database connection efficiency
   **উত্তর:** গ

### ১৭. 5 Coding exercises (with solutions)

**Exercise 1:** Jest-এর কাস্টম মক ফাংশন (`jest.fn()`) ব্যবহার করে একটি বাটনের ক্লিক ইভেন্ট ট্র্যাক করার টেস্ট কোড লিখুন।
```jsx
// ClickMe.jsx
import React from 'react';
export function ClickMe({ onClick }) {
  return <button onClick={onClick}>Click Here</button>;
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { ClickMe } from './ClickMe';

test('calls onClick handler when clicked', async () => {
  const handleClick = jest.fn();
  render(<ClickMe onClick={handleClick} />);
  
  const button = screen.getByRole('button', { name: /click here/i });
  await userEvent.click(button);
  
  expect(handleClick).toHaveBeenCalledTimes(1);
});
```

**Exercise 2:** একটি টেস্ট কেস লিখুন যা ভ্যালিডেট করবে যে একটি নির্দিষ্ট টেক্সট এলিমেন্ট ডমে অনুপস্থিত (not in document) রয়েছে।
**Solution:**
```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';

function CheckText({ show }) {
  return <div>{show && <p>Visible Text</p>}</div>;
}

test('does not render text when show is false', () => {
  render(<CheckText show={false} />);
  const text = screen.queryByText('Visible Text');
  expect(text).toBeNull();
  expect(text).not.toBeInTheDocument();
});
```

**Exercise 3:** RTL-এর `findBy` কোয়েরি ব্যবহার করে ২ সেকেন্ড পর রেন্ডার হওয়া একটি হেডিংয়ের ওপর অ্যাসারশন টেস্ট লিখুন।
```jsx
// AsyncHeader.jsx
import React, { useEffect, useState } from 'react';
export function AsyncHeader() {
  const [show, setShow] = useState(false);
  useEffect(() => {
    const timer = setTimeout(() => setShow(true), 1500);
    return () => clearTimeout(timer);
  }, []);
  return <div>{show && <h1>Loaded Header</h1>}</div>;
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { AsyncHeader } from './AsyncHeader';

test('renders header after delay', async () => {
  render(<AsyncHeader />);
  const header = await screen.findByRole('heading', { name: /loaded header/i }, { timeout: 2000 });
  expect(header).toBeInTheDocument();
});
```

**Exercise 4:** Jest-এর মকিং ব্যবহার করে `axios` লাইব্রেরির মাধ্যমে হওয়া একটি এপিআই কল মক করুন।
**Solution:**
```jsx
import React, { useEffect, useState } from 'react';
import { render, screen } from '@testing-library/react';
import axios from 'axios';
import '@testing-library/jest-dom';

jest.mock('axios');

function FetchData() {
  const [data, setData] = useState('');
  useEffect(() => {
    axios.get('/some-url').then(res => setData(res.data.title));
  }, []);
  return <div>{data}</div>;
}

test('mocks axios get request', async () => {
  axios.get.mockResolvedValueOnce({ data: { title: 'Mocked Title' } });
  render(<FetchData />);
  
  const title = await screen.findByText('Mocked Title');
  expect(title).toBeInTheDocument();
});
```

**Exercise 5:** একটি ইমেজ কম্পোনেন্ট টেস্ট করুন যা যাচাই করবে ইমেজ ট্যাগটির `src` এবং `alt` অ্যাট্রিবিউট সঠিক ভ্যালু পাচ্ছে কিনা।
```jsx
// ProfileImage.jsx
import React from 'react';
export function ProfileImage({ url, alt }) {
  return <img src={url} alt={alt} />;
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProfileImage } from './ProfileImage';

test('renders image with correct src and alt attributes', () => {
  const testUrl = 'https://example.com/avatar.jpg';
  const testAlt = 'User avatar';
  
  render(<ProfileImage url={testUrl} alt={testAlt} />);
  const image = screen.getByRole('img');
  
  expect(image).toHaveAttribute('src', testUrl);
  expect(image).toHaveAttribute('alt', testAlt);
});
```

---

## Topic 3: What is the difference between Enzyme and React Testing Library?

### ১. Simple Definition (বাংলায়)
রিঅ্যাক্ট ইকোসিস্টেমে কম্পোনেন্ট টেস্ট করার দুটি ভিন্ন দর্শনের লাইব্রেরি হলো Enzyme এবং React Testing Library (RTL):
*   **Enzyme (Airbnb দ্বারা নির্মিত):** এটি রিঅ্যাক্ট কম্পোনেন্টের অভ্যন্তরীণ কোডিং স্ট্রাকচার, স্টেট (State), মেথড (Methods) এবং প্রপ্স (Props) সরাসরি অ্যাক্সেস করে টেস্ট করার সুযোগ দেয়। একে **Implementation-driven Testing** বলা হয়।
*   **React Testing Library (Kent C. Dodds দ্বারা নির্মিত):** এটি কম্পোনেন্টের অভ্যন্তরীণ কোডিং কাঠামো কেমন তা পুরোপুরি উপেক্ষা করে, শুধুমাত্র একজন ইউজার স্ক্রিনে কী দেখতে পাচ্ছে ও কীভাবে ইন্টারঅ্যাক্ট করছে তার ওপর ভিত্তি করে টেস্ট করার সুযোগ দেয়। একে **Behavior-driven / User-centric Testing** বলা হয়।

### ২. Why this concept exists
সফটওয়্যার রিফ্যাক্টরিং করার সময় যদি কোডের ভেতরের স্ট্রাকচার পরিবর্তন হয় কিন্তু ইউজার ইন্টারফেস (UI) একই থাকে, তবে টেস্টগুলো ভেঙে যাওয়া উচিত নয়। Enzyme দিয়ে টেস্ট লিখলে কোড রিফ্যাক্টরিংয়ের পর টেস্ট ফেইল করত, কারণ এটি স্টেটের নাম বা ইন্টারনাল মেথডের ওপর নির্ভরশীল ছিল। এই সমস্যার স্থায়ী সমাধানের জন্য RTL-এর প্রবর্তন করা হয়, যা টেস্টগুলোকে আরো টেকসই ও নির্ভরযোগ্য করে তোলে।

### ৩. What problem it solves
*   **Brittle Tests:** Enzyme-এ লেখা টেস্টগুলো সহজেই ভেঙে যেত সামান্য ভ্যারিয়েবলের নাম বা স্টেট পরিবর্তন করলে। RTL এই ভঙ্গুরতা রোধ করে।
*   **False Positives/Negatives:** Enzyme দিয়ে স্টেট সরাসরি পরিবর্তন করে টেস্ট পাস করানো যেত কিন্তু বাস্তবে ইউজার বাটন ক্লিক করলে হয়তো সেটি কাজ করত না। RTL নিশ্চিত করে যে টেস্ট তখনই পাস করবে যখন তা ইউজারের জন্য আসলেই কাজ করবে।
*   **React Upgrade compatibility:** Enzyme রিঅ্যাক্টের ইন্টারনাল ফাইবারের সাথে টাইটলি কাপল্ড হওয়ায় নতুন রিঅ্যাক্ট ভার্সন (যেমন React 18) এলে কাজ করা বন্ধ করে দেয়। RTL ডম লেভেলে কাজ করায় রিঅ্যাক্ট আপগ্রেড করা অত্যন্ত সহজ হয়।

### ৪. Real-life analogy
একটি ঘড়ি কেনার পর তা পরীক্ষা করার সাথে তুলনা করা যাক:
*   **Enzyme হলো ঘড়ির মেকানিজম খোলা:** আপনি ঘড়ির পেছনের ঢাকনা খুলে ভেতরের গিয়ার, স্প্রিং এবং ব্যাটারি ঠিক পজিশনে ঘুরছে কিনা তা দেখছেন। যদি আপনি গিয়ারের ম্যাটেরিয়াল তামা থেকে প্লাস্টিক করেন কিন্তু ঘড়ি ঠিক সময় দেয়, তাও আপনার টেস্ট ফেইল করতে পারে কারণ পেছনের লজিক বদলে গেছে।
*   **React Testing Library হলো ঘড়ির ডায়াল দেখা:** আপনি কেবল ঘড়ির ডায়ালের দিকে তাকাচ্ছেন এবং দেখছেন কাঁটা ঠিকমতো টিকটিক করে ঘুরছে কিনা এবং সঠিক সময় দেখাচ্ছে কিনা। ঘড়ির ভেতরে কী বসানো আছে তা আপনার দেখার বিষয় নয়।

### ৫. How React works internally regarding this concept
*   **Enzyme:** এটি রিঅ্যাক্টের ইন্টারনাল ইনস্ট্যান্স (React Component Instances) এবং রিঅ্যাক্টের নিজস্ব ফাইবার নোড (Fiber nodes)-এর সাথে কানেক্ট হয়। এর `shallow` রেন্ডারার রিঅ্যাক্ট এলিমেন্টগুলোর চাইল্ড কম্পোনেন্ট রেন্ডার না করে শুধুমাত্র চাইল্ডের সিগনেচার মেমোরিতে ধরে রাখে।
*   **RTL:** এটি রিঅ্যাক্টের কোনো ইন্টারনাল ইনস্ট্যান্স অ্যাক্সেস করার সুবিধা দেয়ই না। এটি `react-dom/client` ব্যবহার করে সরাসরি JSDOM-এ রেন্ডার করে। এরপর এটি স্ট্যান্ডার্ড ব্রাউজার API (`DOM API`) এর মতো করে অ্যাক্ট করে। যেহেতু ডম সবসময় স্ট্যান্ডার্ড ব্রাউজার রুলস ফলো করে, তাই রিঅ্যাক্টের অভ্যন্তরীণ মেকানিজম বা ফাইবার যেভাবে চেঞ্জ হোক না কেন, ডম এলিমেন্ট রিপ্রেজেন্টেশন একই থাকে।

### ৬. Basic example
এখানে একটি কাউন্টার কম্পোনেন্টকে দুটি লাইব্রেরিতে কীভাবে টেস্ট করা হতো তার তুলনা দেওয়া হলো:

**Enzyme Test (Implementation focus):**
```jsx
// Enzyme test snippet
import { shallow } from 'enzyme';
import Counter from './Counter';

describe('Counter with Enzyme', () => {
  it('should increment state count by 1', () => {
    const wrapper = shallow(<Counter />);
    expect(wrapper.state('count')).toEqual(0); // Accessing state directly
    wrapper.find('button').simulate('click');
    expect(wrapper.state('count')).toEqual(1); // Verifying implementation detail
  });
});
```

**React Testing Library Test (Behavior focus):**
```jsx
// RTL test snippet
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { Counter } from './Counter';

describe('Counter with RTL', () => {
  it('should display incremented value to the user', async () => {
    render(<Counter />);
    const counterValue = screen.getByRole('heading');
    const button = screen.getByRole('button', { name: /increment/i });
    
    expect(counterValue).toHaveTextContent('0'); // Checking visual text
    await userEvent.click(button);
    expect(counterValue).toHaveTextContent('1'); // Checking updated visual text
  });
});
```

### ৭. Step-by-step explanation of the code
১. Enzyme টেস্টে `shallow(<Counter />)` চাইল্ড কম্পোনেন্টগুলোকে রেন্ডার না করে শুধু কারেন্ট ডম লেভেল ম্যাপ করে।
২. `wrapper.state('count')` ব্যবহার করে মেমরির স্টেট সরাসরি রিড করা হচ্ছে। এটি একটি ইমপ্লিমেন্টেশন ডিটেইল যা ব্যবহারকারী দেখতে পায় না।
৩. RTL টেস্টে `render(<Counter />)` সম্পূর্ণ কম্পোনেন্ট ট্রি রেন্ডার করে।
৪. `screen.getByRole` ব্যবহার করে স্ট্যান্ডার্ড হেডিং ও বাটন খোঁজা হচ্ছে, যা অ্যাক্সেসিবিলিটি রুল মেনে চলে।
৫. `userEvent.click` আসল মাউস ক্লিকের মতোই ইভেন্ট চেইন ট্রিগার করে।
৬. অ্যাসারশন `toHaveTextContent('1')` সরাসরি স্ক্রিনের টেক্সট চেক করছে, রিঅ্যাক্ট ভ্যারিয়েবলের মান নয়।

### ৮. Another real-world example
একটি কাস্টম ড্রপডাউন সার্চ ফিল্টার:
*   **Enzyme approach:** ডেভেলপার চেক করবে যে ফিল্টার এরিয়াতে টাইপ করলে `this.state.searchQuery` ভ্যারিয়েবলটি আপডেট হচ্ছে কিনা এবং কাস্টম ফিল্টার মেথডটি কল হচ্ছে কিনা।
*   **RTL approach:** ডেভেলপার ফিল্টার বক্সে টাইপ করবে এবং দেখবে যে নিচের লিস্টে থাকা আইটেমগুলোর সংখ্যা কমে গেছে কিনা এবং শুধুমাত্র রিলেটেড আইটেমগুলো স্ক্রিনে শো করছে কিনা।

### ৯. Common mistakes beginners make
*   **Trying to access wrapper state in RTL:** RTL-এ এসে `wrapper.state()` বা `wrapper.instance()` খোঁজা। RTL এটি ইচ্ছাকৃতভাবেই সাপোর্ট করে না।
*   **Simulating fake events in RTL:** RTL-এ `fireEvent` দিয়ে কৃত্রিমভাবে টেস্ট করা যেখানে `userEvent` দিয়ে সম্পূর্ণ রিয়েল ইন্টারঅ্যাকশন সিমুলেট করা উচিত ছিল।
*   **Overusing shallow rendering in RTL:** RTL-এ কোনো `shallow` রেন্ডারার নেই। অনেকে মক কম্পোনেন্ট ম্যানুয়ালি তৈরি করে চাইল্ড হাইড করতে চায়, যা অধিকাংশ ক্ষেত্রে অপ্রয়োজনীয়।

### ১০. Interview questions related to this topic
১. **Question:** Why has Enzyme fallen out of favor in the React community?
   *   **Answer:** কারণ Enzyme রিঅ্যাক্টের ইন্টারনাল রিঅ্যাক্ট ইনস্ট্যান্সের ওপর অত্যন্ত নির্ভরশীল। React 17 এবং বিশেষ করে React 18 আসার পর Enzyme অফিশিয়ালি আর কোনো আপডেট পায়নি এবং এটি নতুন রিঅ্যাক্ট আর্কিটেকচার সাপোর্ট করতে পারে না।
২. **Question:** What is "Implementation Detail" and why should we not test it?
   *   **Answer:** ইমপ্লিমেন্টেশন ডিটেইল হলো এমন কোড লজিক যা ইউজার সরাসরি দেখতে পায় না (যেমন স্টেটের নাম, প্রাইভেট মেথড)। এটি টেস্ট করলে সামান্য রিফ্যাক্টরিং বা রিঅ্যাক্ট আপগ্রেডে পুরো টেস্ট স্যুট ভেঙে যায় কিন্তু অ্যাপ্লিকেশনের মূল কাজে কোনো পরিবর্তন হয় না।
৩. **Question:** Does RTL support shallow rendering? Why or why not?
   *   **Answer:** না, RTL ডাইরেক্টলি `shallow` রেন্ডারিং সাপোর্ট করে না। কারণ একজন ইউজার যখন কোনো ওয়েব পেজ দেখে, সে কিন্তু শ্যালো পেজ দেখে না, সে পুরো রেন্ডার হওয়া পেজ দেখে। RTL ইউজার বিহেভিয়ার ফলো করে বলেই এটি ফুল কম্পোনেন্ট রেন্ডারিং করে।
৪. **Question:** How do you handle heavy child components in RTL without shallow rendering?
   *   **Answer:** যদি কোনো চাইল্ড কম্পোনেন্ট অনেক ভারী হয় বা থার্ড পার্টি লাইব্রেরি ব্যবহার করে, তবে আমরা `jest.mock` ব্যবহার করে সেই নির্দিষ্ট চাইল্ড কম্পোনেন্টটিকে মক করতে পারি।
৫. **Question:** What is the core guiding principle of React Testing Library?
   *   **Answer:** "The more your tests resemble the way your software is used, the more confidence they can give you." (আপনার টেস্টগুলো যত বেশি আপনার সফটওয়্যার ব্যবহারের ব্লু-প্রিন্ট ফলো করবে, তত বেশি নির্ভরযোগ্যতা নিশ্চিত হবে)।

### ১১. Best practices
*   **Refactor code without rewriting tests:** যদি আপনি কোনো ক্লাসের স্টেট নাম চেঞ্জ করেন, টেস্ট কোড পরিবর্তন না করেই টেস্ট পাস করা উচিত।
*   **Rely on accessibility labels:** `getByRole` ব্যবহার করে বাটন ও ইনপুট ট্র্যাক করুন, যা অন্ধ বা স্পেশাল ইউজারদের জন্য সাইটটিকে অ্যাক্সেসিবল করতে সাহায্য করবে।
*   **Keep your mock scope small:** শুধুমাত্র জটিল নেটওয়ার্ক ডিপেন্ডেন্সি মক করুন, পুরো কম্পোনেন্ট ট্রি নয়।

### ১২. Performance considerations
*   **Full DOM render cost:** ফুল মাউন্টিং JSDOM-এ কিছুটা মেমোরি বেশি ব্যবহার করতে পারে। তবে মডার্ন টেস্ট রানার (যেমন Vitest বা Jest) মাল্টি-থ্রেডিং ও মেমোরি অপ্টিমাইজেশন দিয়ে এই কনসার্ন মিনিমাইজ করে।

### १३. When NOT to use it
*   **Legacy Codebase:** যদি আপনার প্রজেক্টটি অনেক পুরোনো হয় (React 15/16) এবং Enzyme-এ হাজার হাজার টেস্ট অলরেডি লেখা থাকে, তবে প্রজেক্টটি রিঅ্যাক্ট ১৮-এ মাইগ্রেট না করা পর্যন্ত Enzyme রেখে দেওয়া লাগতে পারে।

### ১৪. Comparison with similar concepts

| Feature | Enzyme | React Testing Library (RTL) |
| :--- | :--- | :--- |
| **Testing Philosophy** | Implementation Details | User Behavior / Visual UI |
| **Component Rendering** | Shallow, Mount, and Render | Full Mounting inside JSDOM |
| **State & Props access**| Yes, highly supported | No, discouraged |
| **React 18+ Support** | No (Deprecated) | Yes, fully supported |
| **Learning Curve** | Complex | Simple and intuitive |

### ১৫. Summary in simple Bangla
Enzyme আমাদের কোডের ভেতরে কী ভ্যারিয়েবল আছে তা চেক করতে বাধ্য করে, যা কোড রিফ্যাক্টর করলেই ভেঙে যায়। অন্যদিকে, React Testing Library ব্রাউজারে ইউজার যেভাবে আপনার অ্যাপ দেখবে ও ব্যবহার করবে ঠিক সেভাবে টেস্ট করে। তাই বর্তমানে Enzyme বন্ধ হয়ে গেছে এবং রিঅ্যাক্ট অ্যাপ টেস্ট করার জন্য RTL গ্লোবাল স্ট্যান্ডার্ড হয়ে উঠেছে।

### ১৬. 5 MCQ questions (with answers)
১. Enzyme মূলত কোন ধরণের টেস্টিং দর্শনের ওপর প্রতিষ্ঠিত?
   ক) Behavior-driven
   খ) Implementation-driven
   গ) Database-driven
   ঘ) Zero-config
   **উত্তর:** খ

২. React 18-এর সাথে নিচের কোন লাইব্রেরিটি অফিশিয়ালি কাজ করে না বা Deprecated?
   ক) Vitest
   খ) Cypress
   গ) Enzyme
   ঘ) React Testing Library
   **উত্তর:** গ

৩. RTL-এ কেন `shallow rendering` এর সুবিধা দেওয়া হয়নি?
   ক) কোড পারফরম্যান্স বাড়ানোর জন্য
   খ) ইউজার যেভাবে অ্যাপ দেখে সেভাবে রেন্ডারিংয়ের সুযোগ রাখার জন্য
   গ) জাভাস্ক্রিপ্ট সিকিউরিটির জন্য
   ঘ) এরর হ্যান্ডলিং সহজ করতে
   **উত্তর:** খ

৪. "The more your tests resemble the way your software is used, the more confidence they can give you" - উক্তিটি কার?
   ক) Dan Abramov
   খ) Kent C. Dodds
   গ) Ryan Dahl
   ঘ) Evan You
   **উত্তর:** খ

৫. Enzyme-এর `shallow` মেথডের পরিবর্তে RTL-এ কোনো কম্পোনেন্টকে মক করার জন্য সাধারণত কী ব্যবহার করা হয়?
   ক) jest.mock()
   খ) screen.mock()
   গ) enzyme.shallow()
   ঘ) cypress.route()
   **উত্তর:** ক

### ১৭. 5 Coding exercises (with solutions)

**Exercise 1:** নিচের Enzyme টেস্টটিকে React Testing Library টেস্টে রূপান্তর করুন।
```jsx
// Enzyme Code
it('renders active class based on prop', () => {
  const wrapper = shallow(<Badge active={true} />);
  expect(wrapper.hasClass('active')).toBe(true);
});
```
**Solution:**
```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Badge } from './Badge'; // assuming Badge component is imported

test('renders active class based on prop', () => {
  render(<Badge active={true} />);
  const badgeElement = screen.getByTestId('badge'); // assuming test-id is given
  expect(badgeElement).toHaveClass('active');
});
```

**Exercise 2:** একটি `ExpandableText` কম্পোনেন্ট আছে যা ক্লিক করলে পুরো বিবরণ প্রকাশ করে। এর জন্য একটি ইউজার বিহেভিয়ার ভিত্তিক RTL টেস্ট লিখুন।
```jsx
// ExpandableText.jsx
import React, { useState } from 'react';
export function ExpandableText({ text }) {
  const [expanded, setExpanded] = useState(false);
  return (
    <div>
      <p>{expanded ? text : `${text.substring(0, 10)}...`}</p>
      <button onClick={() => setExpanded(!expanded)}>
        {expanded ? 'Show Less' : 'Show More'}
      </button>
    </div>
  );
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom';
import { ExpandableText } from './ExpandableText';

test('expands text when clicking Show More', async () => {
  const longText = 'This is a very long text that will be truncated.';
  render(<ExpandableText text={longText} />);
  
  expect(screen.getByText('This is a ...')).toBeInTheDocument();
  const button = screen.getByRole('button', { name: /show more/i });
  
  await userEvent.click(button);
  expect(screen.getByText(longText)).toBeInTheDocument();
  expect(button).toHaveTextContent('Show Less');
});
```

**Exercise 3:** এমন একটি কন্টেইনার মক করুন যেখানে একটি ভারী চাইল্ড কম্পোনেন্ট `HugeChart` আছে। RTL-এর মাধ্যমে প্যারেন্ট রেন্ডার করে চাইল্ড মক ভেরিফাই করুন।
```jsx
// Dashboard.jsx
import React from 'react';
import { HugeChart } from './HugeChart';
export function Dashboard() {
  return (
    <div>
      <h1>Analytics</h1>
      <HugeChart data={[1, 2, 3]} />
    </div>
  );
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Dashboard } from './Dashboard';

jest.mock('./HugeChart', () => ({
  HugeChart: () => <div data-testid="mock-chart">Mocked Chart</div>
}));

test('renders dashboard with mocked chart', () => {
  render(<Dashboard />);
  expect(screen.getByRole('heading', { name: /analytics/i })).toBeInTheDocument();
  expect(screen.getByTestId('mock-chart')).toBeInTheDocument();
});
```

**Exercise 4:** একটি কম্পোনেন্ট ইনপুটে টাইপ করলে বাটন এনাবল হয়। Enzyme স্টাইলে স্টেট এসারশন না করে RTL-এ ইউজার ইন্টারঅ্যাকশন দিয়ে টেস্টটি লিখুন।
```jsx
// AgreeTerms.jsx
import React, { useState } from 'react';
export function AgreeTerms() {
  const [checked, setChecked] = useState(false);
  return (
    <div>
      <label>
        <input type="checkbox" checked={checked} onChange={() => setChecked(!checked)} />
        I agree to the terms
      </label>
      <button disabled={!checked}>Proceed</button>
    </div>
  );
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom';
import { AgreeTerms } from './AgreeTerms';

test('proceed button is only enabled when checkbox is checked', async () => {
  render(<AgreeTerms />);
  const checkbox = screen.getByRole('checkbox', { name: /i agree to the terms/i });
  const button = screen.getByRole('button', { name: /proceed/i });
  
  expect(button).toBeDisabled();
  
  await userEvent.click(checkbox);
  expect(button).toBeEnabled();
});
```

**Exercise 5:** একটি `Notification` কম্পোনেন্ট রেন্ডার করার পর ৩ সেকেন্ড পর অটো-ডিসমিস (dismiss) হয়ে যায়। এর জন্য টাইমআউট সহ RTL টেস্ট লিখুন।
```jsx
// Notification.jsx
import React, { useEffect, useState } from 'react';
export function Notification({ message }) {
  const [visible, setVisible] = useState(true);
  useEffect(() => {
    const timer = setTimeout(() => setVisible(false), 3000);
    return () => clearTimeout(timer);
  }, []);
  if (!visible) return null;
  return <div>{message}</div>;
}
```
**Solution:**
```jsx
import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import '@testing-library/jest-dom';
import { Notification } from './Notification';

test('notification disappears after 3 seconds', async () => {
  jest.useFakeTimers();
  render(<Notification message="Saved successfully!" />);
  
  expect(screen.getByText('Saved successfully!')).toBeInTheDocument();
  
  // Fast-forward time
  jest.advanceTimersByTime(3000);
  
  await waitFor(() => {
    expect(screen.queryByText('Saved successfully!')).not.toBeInTheDocument();
  });
  
  jest.useRealTimers();
});
```

---

## Topic 4: How to configure and set up testing in a React App? (Configuring Babel, JSDOM, Jest initialization, and bundler/Parcel configurations)

### ১. Simple Definition (বাংলায়)
একটি সাধারণ রিঅ্যাক্ট অ্যাপ্লিকেশনে টেস্ট রান করানোর আগে আমাদের কিছু ব্যাকএন্ড কনফিগারেশন করতে হয়। কারণ রিঅ্যাক্ট কোড JSX এবং আধুনিক ES6+ সিনট্যাক্স ব্যবহার করে লেখা হয় যা Node.js সরাসরি চেনে না। এই কনফিগারেশনে কোড ট্রান্সলেট করার জন্য **Babel**, ব্রাউজার এপিআই সিমুলেট করার জন্য **JSDOM**, টেস্ট চালানোর জন্য **Jest Initialization** এবং প্রজেক্টের অ্যাসেট ম্যানেজ করতে **Parcel/Webpack Bundler** এর সাথে টেস্টিং প্লাগইন যুক্ত করতে হয়।

### ২. Why this concept exists
সফটওয়্যার ইন্ডাস্ট্রি অনেক দ্রুত পরিবর্তনশীল। রিঅ্যাক্ট কোড ব্রাউজারে চালানোর জন্য Bundler কোডকে ট্রান্সপাইল ও বান্ডেল করে। কিন্তু Jest ব্রাউজারের বদলে টার্মিনালে (Node.js) সরাসরি রান করে। নোড জেনারেটেড কোডে JSX বুঝতে পারে না এবং `window` বা `document` অবজেক্ট নোডে অনুপস্থিত থাকে। এই কারণে রিঅ্যাক্ট টেস্ট চালু করার জন্য একটি রিয়্যালিস্টিক এনভায়রনমেন্ট কনফিগারেশনের প্রয়োজন হয়।

### ৩. What problem it solves
*   **Syntax Error:** JSX বা `import/export` স্টেটমেন্ট রান করার সময় Jest যাতে ক্র্যাশ না করে (Babel এটি সমাধান করে)।
*   **Missing Window object:** Node.js-এ রান করলেও যেন `document.createElement` বা `window.location` এর মতো ব্রাউজার এপিআইগুলো কাজ করে (JSDOM এটি সমাধান করে)।
*   **Asset Import Errors:** প্রজেক্টে `.css` বা `.svg` ইম্পোর্ট করলে Jest যাতে সেগুলো পার্স করতে গিয়ে এরর না দেখায় (Jest Mock/Bundler configs এটি সমাধান করে)।

### ৪. Real-life analogy
এটি একটি আন্তর্জাতিক কনফারেন্সে বিদেশি অথিতিদের সেবা দেওয়ার মতো:
*   **Babel হলো দোভাষী (Translator):** অথিতিরা যদি এমন ভাষায় কথা বলেন যা আয়োজকরা বোঝেন না, তবে দোভাষী তা লোকাল ভাষায় রূপান্তর করে দেন। (JSX কে ES5 এ রূপান্তর)।
*   **JSDOM হলো কৃত্রিম ঘর (Simulation Room):** মরুভূমির মানুষের জন্য ল্যাবের ভেতরে কৃত্রিম এসি দিয়ে পাহাড়ি ঠাণ্ডা পরিবেশ তৈরি করা যাতে তারা স্বাভাবিক ফিল করেন। (Node-এর ভেতর ব্রাউজার ডমের ভার্চুয়াল পরিবেশ)।
*   **Bundler (Parcel) হলো লজিস্টিক ম্যানেজার:** যে অতিথির ট্রাভেল টিকিট, লাগেজ ও থাকার হোটেল ঠিকঠাকভাবে অর্গানাইজ করে দেয়।

### ৫. How React works internally regarding this concept
*   যখন আমরা `npm test` রান করি, Jest প্রথমে টেস্ট ফাইলগুলো মেমরিতে লোড করে।
*   Jest ফাইলগুলোর ওপর দিয়ে `babel-jest` ট্রান্সফরমার চালায়। Babel তার `.babelrc` বা `babel.config.js` পড়ে JSX ট্যাগগুলোকে `React.createElement` বা আধুনিক `_jsx` ট্রান্সফর্মে কনভার্ট করে।
*   এরপর Jest কনফিগারেশন ফাইল থেকে `testEnvironment: 'jsdom'` রিড করে। Jest ব্যাকএন্ডে `jsdom` মডিউলটি লোড করে গ্লোবাল স্কোপে `window`, `document`, `navigator` ডিফাইন করে।
*   এবার রিঅ্যাক্ট কম্পোনেন্ট রেন্ডার হওয়ার সময় `react-dom` যখন ইন্টারনাল ডম নোড তৈরি করতে যাবে, সে আসলে JSDOM-এর মেমোরি নোডে পুশ করে।

### ৬. Basic example
এখানে একটি মিনিমাল কনফিগারেশন সেটআপ দেওয়া হলো যা আপনি স্ক্র্যাচ থেকে করতে পারেন:

**package.json** (Dependencies)
```json
{
  "name": "react-testing-setup",
  "version": "1.0.0",
  "scripts": {
    "test": "jest"
  },
  "devDependencies": {
    "@babel/core": "^7.20.0",
    "@babel/preset-env": "^7.20.0",
    "@babel/preset-react": "^7.20.0",
    "@testing-library/jest-dom": "^6.0.0",
    "@testing-library/react": "^14.0.0",
    "babel-jest": "^29.0.0",
    "jest": "^29.0.0",
    "jest-environment-jsdom": "^29.0.0"
  }
}
```

**babel.config.json**
```json
{
  "presets": [
    ["@babel/preset-env", { "targets": { "node": "current" } }],
    ["@babel/preset-react", { "runtime": "automatic" }]
  ]
}
```

**jest.config.js**
```javascript
module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  moduleNameMapper: {
    '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
    '\\.(gif|ttf|eot|svg|png)$': '<rootDir>/__mocks__/fileMock.js'
  }
};
```

**jest.setup.js**
```javascript
import '@testing-library/jest-dom';
```

**__mocks__/fileMock.js**
```javascript
module.exports = 'test-file-stub';
```

### ৭. Step-by-step explanation of the code
১. **`babel.config.json`:** `@babel/preset-env` কোডটিকে কারেন্ট নোড সংস্করণের উপযোগী করে এবং `@babel/preset-react` এর `{ "runtime": "automatic" }` আমাদের প্রতিটি ফাইলে ম্যানুয়ালি `import React from 'react'` লেখা ছাড়াই JSX ব্যবহারের সুযোগ দেয়।
২. **`jest.config.js`:** `testEnvironment: 'jsdom'` নির্দেশ করে যে আমাদের টেস্টগুলো ব্রাউজার ডম সিমুলেশনে রান হবে।
৩. **`setupFilesAfterEnv`:** এই অ্যারেতে থাকা ফাইলগুলো প্রতিটি টেস্ট ফাইল এক্সেকিউট হওয়ার ঠিক আগে রান হয়। আমরা এখানে `jest.setup.js` দিয়ে `@testing-library/jest-dom` লোড করেছি যাতে গ্লোবাল ডম ম্যাচিং ফিচার সরাসরি পাওয়া যায়।
৪. **`moduleNameMapper`:** সিএসএস এবং ইমেজ ফাইলের জন্য মক ফাইল ম্যাপিং। Jest যাতে ইমেজ বা সিএসএস লোড করতে গিয়ে ফাইল ক্র্যাশ না করে, তাই `identity-obj-proxy` এবং `fileMock.js` দিয়ে সেগুলোকে মক আউট করা হয়েছে।

### ৮. Another real-world example (Parcel Integration)
যদি আমরা **Parcel Bundler** ব্যবহার করি, তবে পার্সেল অটোমেটিক্যালি Babel ডিটেক্ট করতে পারে। তবে Jest ব্যবহারের জন্য আমাদের `.babelrc` ফাইলটি কনফিগার করে দিতে হবে। প্রজেক্টে যদি কোনো ইমেজ বা ফন্ট ইম্পোর্ট থাকে, তবে Parcel সেগুলোকে যেভাবে কম্পাইল করে, Jest যাতে ঠিক সেভাবেই ফাইলগুলোকে বুঝতে পারে সেজন্যে Jest কনফিগারে `moduleNameMapper` ব্যবহার করতেই হবে। পার্সেল কম্পোনেন্টে মডিউল রেজোলিউশন সহজ করার জন্য `jest-transformer-svg` এর মতো প্লাগইন অ্যাড করা হয়।

### ৯. Common mistakes beginners make
*   **Missing `jest-environment-jsdom` package:** Jest 28+ সংস্করণ থেকে JSDOM এনভায়রনমেন্ট ডিফল্ট প্যাকেজ থেকে সরিয়ে আলাদা প্যাকেজ করা হয়েছে। এটি ইন্সটল না করলে `Test environment "jsdom" cannot be found` এরর আসে।
*   **Babel configuration conflicts:** ক্রিয়েট রিয়্যাক্ট অ্যাপ (CRA) বা অন্য কোনো টুলের কনফিগারেশন ফাইলের সাথে প্রজেক্টের কাস্টম `.babelrc` কনফ্লিক্ট করা।
*   **Not ignoring CSS/Assets:** ডাস্টবিন বা নোংরা ছবির ফাইল ইম্পোর্ট করার পর Jest-এ ম্যাপার না রাখায় সিনট্যাক্স এরর আসা।

### ১০. Interview questions related to this topic
১. **Question:** Why do we need `jest-environment-jsdom` since Jest is running on Node.js?
   *   **Answer:** Node.js-এ ব্রাউজার ডম অবজেক্টগুলো (যেমন `document`, `window`) থাকে না। JSDOM হলো জাভাস্ক্রিপ্ট দিয়ে তৈরি ডম মেকানিজম যা নোডে রিয়েল ব্রাউজারের মতো এনভায়রনমেন্ট দেয়।
২. **Question:** What is the role of `identity-obj-proxy` in Jest config?
   *   **Answer:** এটি CSS Module-এর ক্লাসগুলোকে অবজেক্ট আকারে ম্যাপ করে (যেমন `styles.container` কে `'container'` স্ট্রিং এ রূপান্তর করে), যার ফলে স্টাইলিং ফাইল ইম্পোর্টের কারণে Jest টেস্ট ক্র্যাশ করে না।
৩. **Question:** Why does Jest need Babel transpilation?
   *   **Answer:** Jest বাই-ডিফল্ট মডার্ন জাভাস্ক্রিপ্ট (যেমন `import/export` সিনট্যাক্স) এবং JSX বুঝতে পারে না। Babel এই কোডগুলোকে সাধারণ জাভাস্ক্রিপ্ট মডিউলে রূপান্তর করে যা Node.js সহজেই রিড করতে পারে।
৪. **Question:** How do you configure Jest to run in watch mode?
   *   **Answer:** `package.json` এর স্ক্রিপ্টে `"test:watch": "jest --watch"` যোগ করে রান করতে হবে। এটি ফাইল সেভ করার সাথে সাথে শুধুমাত্র পরিবর্তিত ফাইলের টেস্ট পুনরায় চালাবে।
৫. **Question:** What is the purpose of `jest.setup.js`?
   *   **Answer:** টেস্ট এনভায়রনমেন্ট প্রস্তুত হওয়ার পর কিন্তু টেস্ট ফাইলগুলো রান হওয়ার আগে কোনো কোড এক্সিকিউট করতে (যেমন গ্লোবাল পলিফিল বা কাস্টম ম্যাচার অ্যাড করতে) এটি ব্যবহার করা হয়।

### ১১. Best practices
*   **Use Babel config over package.json config:** Babel কনফিগারেশন ফাইল আলাদা ফাইলে (`babel.config.json`) রাখা ভালো, এতে কনফিগারেশন ফাইল গুছানো থাকে।
*   **Keep your mock folder clean:** ইমেজের জন্য একটি সিম্পল মক অবজেক্ট প্রজেক্টের রুট ডিরেক্টরিতে রাখুন।
*   **Cache Jest files:** Jest ক্যাশ মেমোরি ক্লিয়ার করতে মাঝে মাঝে `jest --clearCache` রান করতে পারেন যদি কোনো কনফিগারেশন অদ্ভুত আচরণ করে।

### ১২. Performance considerations
*   **Fast compilation with SWC or Vitest:** বড় প্রজেক্টে Babel স্লো হয়ে যেতে পারে। সেক্ষেত্রে `@swc/jest` বা **Vitest** ব্যবহার করলে টেস্ট রান টাইম কয়েক গুণ কমে যায়।

### ১৩. When NOT to use it
*   **Vite Projects:** আপনি যদি প্রজেক্ট তৈরিতে **Vite** ব্যবহার করেন, তবে Jest + Babel কনফিগার না করে সরাসরি **Vitest** ব্যবহার করুন। কারণ Vitest কোনো অতিরিক্ত কনফিগ ছাড়াই সরাসরি Vite-এর কনফিগারেশন দিয়ে কাজ করতে পারে।

### ১৪. Comparison with similar concepts

| Setup Type | Complexity | Build Speed | Browser API Simulation | Transpiler Required |
| :--- | :--- | :--- | :--- | :--- |
| **Jest + Babel Setup** | Medium | Medium | JSDOM | Yes (Babel/SWC) |
| **Vitest Setup** | Low | Extremely Fast | JSDOM / Happy DOM | No (Uses Vite pipeline)|
| **Cypress Component Testing**| High | Slow | Real Browser | Built-in |

### ১৫. Summary in simple Bangla
রিঅ্যাক্ট কোডকে নোড এবং টেস্ট ফ্রেমওয়ার্কের সাথে সামঞ্জস্যপূর্ণ করার জন্য কনফিগারেশন লাগে। Babel আমাদের JSX ও আধুনিক সিনট্যাক্স সাধারণ জাভাস্ক্রিপ্টে অনুবাদ করে। JSDOM নোড এনভায়রনমেন্টের ভেতরে একটি নকল ব্রাউজার বানিয়ে দেয় যাতে ডম এলিমেন্ট টেস্ট করা যায়। এই পুরো সিস্টেমটি Jest ইনিশিয়ালাইজেশন এবং পার্সেলের মতো বান্ডলারের সাথে কানেক্ট হয়ে কাজ করে।

### ১৬. 5 MCQ questions (with answers)
১. Jest 28+ ভার্সনে JSDOM ব্যবহার করতে চাইলে এক্সট্রা কোন প্যাকেজটি ইন্সটল করতে হয়?
   ক) jest-jsdom
   খ) jest-environment-jsdom
   গ) jsdom-setup
   ঘ) react-jsdom
   **উত্তর:** খ

২. identity-obj-proxy কোন ধরনের ফাইলের এরর এড়াতে সাহায্য করে?
   ক) .js ফাইল
   খ) .jsx ফাইল
   গ) .css বা .scss ফাইল
   ঘ) .json ফাইল
   **উত্তর:** গ

৩. Babel কনফিগারেশনে `"runtime": "automatic"` দিয়ে কী লাভ হয়?
   ক) টেস্ট ফাইল নিজে নিজে রান হয়
   খ) প্রতি ফাইলে `import React` লেখা ছাড়াই JSX ব্যবহার করা যায়
   গ) কোড পারফরম্যান্স দ্বিগুণ হয়
   ঘ) ডেটাবেস অটোমেটিকালি কানেক্ট হয়
   **উত্তর:** খ

৪. `jest.config.js` ফাইলে `setupFilesAfterEnv` এর কাজ কী?
   ক) টেস্ট ফাইলের জন্য ক্যাশ মেমোরি তৈরি করা
   খ) টেস্টগুলো রান হওয়ার পূর্বে নির্দিষ্ট মডিউল বা কাস্টম ম্যাচার সেটআপ করা
   গ) সিএসএস ফাইল মক করা
   ঘ) প্রোডাকশন বিল্ড জেনারেট করা
   **উত্তর:** খ

৫. নোড ডট জেএস এ `window` বা `document` অবজেক্টের ঘাটতি কে পূরণ করে?
   ক) Babel
   খ) Webpack
   গ) JSDOM
   ঘ) Parcel
   **উত্তর:** গ

### ১৭. 5 Coding exercises (with solutions)

**Exercise 1:** একটি কাস্টম `jest.config.js` ফাইল লিখুন যা টেস্ট কভারেজ (code coverage) ট্র্যাক করবে এবং কভারেজ ডিরেক্টরি সেট করবে।
**Solution:**
```javascript
// jest.config.js
module.exports = {
  testEnvironment: 'jsdom',
  collectCoverage: true,
  coverageDirectory: 'coverage',
  collectCoverageFrom: [
    'src/**/*.{js,jsx}',
    '!src/index.js',
    '!src/reportWebVitals.js'
  ],
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js']
};
```

**Exercise 2:** প্রজেক্টে SVG ফাইলগুলো হ্যান্ডেল করার জন্য Jest-এর মক কনফিগারেশন লিখুন।
**Solution:**
১. `jest.config.js` এ ম্যাপার সেট করুন:
```javascript
module.exports = {
  testEnvironment: 'jsdom',
  moduleNameMapper: {
    '\\.svg$': '<rootDir>/__mocks__/svgMock.js'
  }
};
```
২. `__mocks__/svgMock.js` ফাইলটি তৈরি করুন:
```javascript
const React = require('react');
module.exports = {
  __esModule: true,
  default: 'SvgrURL',
  ReactComponent: React.forwardRef((props, ref) => (
    <span ref={ref} {...props} />
  )),
};
```

**Exercise 3:** Babel ছাড়াই Jest যাতে ফাইল ট্রান্সপাইল করতে পারে সে জন্য `@swc/jest` লাইব্রেরি কনফিগারেশন `jest.config.js`-এ সেট করুন।
**Solution:**
```javascript
// jest.config.js using SWC instead of Babel
module.exports = {
  testEnvironment: 'jsdom',
  transform: {
    '^.+\\.(t|j)sx?$': '@swc/jest',
  },
};
```

**Exercise 4:** এমন একটি ফাইল মক কনফিগার করুন যা প্রজেক্টের গ্লোবাল `localStorage` এপিআই-কে মক করবে, যাতে JSDOM-এ লোকালস্টোরেজ ব্যবহারে কোনো এরর না আসে।
**Solution:**
`jest.setup.js` ফাইলে নিম্নলিখিত কোডটি যুক্ত করুন:
```javascript
const localStorageMock = (() => {
  let store = {};
  return {
    getItem: (key) => store[key] || null,
    setItem: (key, value) => { store[key] = value.toString(); },
    clear: () => { store = {}; },
    removeItem: (key) => { delete store[key]; }
  };
})();

Object.defineProperty(window, 'localStorage', {
  value: localStorageMock
});
```

**Exercise 5:** একটি সম্পূর্ণ স্ক্র্যাচ `babel.config.js` ফাইল তৈরি করুন যা প্রজেক্টের টাইপস্ক্রিপ্ট (TypeScript) এবং রিঅ্যাক্ট (React) কনফিগারেশনকে একসাথে সমর্থন করবে।
**Solution:**
```javascript
// babel.config.js
module.exports = {
  presets: [
    ['@babel/preset-env', { targets: { node: 'current' } }],
    ['@babel/preset-react', { runtime: 'automatic' }],
    '@babel/preset-typescript'
  ],
};
```

---

## Topic 5: Why is testing an essential part of the development process?

### ১. Simple Definition (বাংলায়)
সফটওয়্যার ডেভেলপমেন্টে টেস্টিং হলো এমন একটি ফিল্টারিং বা কোয়ালিটি কন্ট্রোল প্রসেস যা কোডের ভুলভ্রান্তি এবং ত্রুটি প্রোডাকশন বা সাধারণ ব্যবহারকারীর কাছে পৌঁছানোর আগেই আটকে দেয়। এটি কেবল বাগ খোঁজার প্রক্রিয়া নয়, এটি কোডের আর্কিটেকচার উন্নত করতে, টিমের কর্মদক্ষতা বাড়াতে এবং দীর্ঘমেয়াদে সফটওয়্যারের স্থায়িত্ব বজায় রাখার একটি শক্তিশালী বৈজ্ঞানিক মাধ্যম।

### ২. Why this concept exists
সফটওয়্যার ডেভেলপমেন্ট কোনো ওয়ান-টাইম কাজ নয়। একটি সাকসেসফুল প্রজেক্ট প্রতিনিয়ত আপডেট ও মেইনটেইন করতে হয়। মানুষ হিসেবে ডেভেলপারদের ভুল হওয়া অত্যন্ত স্বাভাবিক। টেস্টিং ছাড়া বড় প্রজেক্টে সামান্য কোড চেঞ্জ করা মানে অন্ধকার ঘরে তলোয়ার চালানো। কোডবেস যেন যেকোনো সময় রিফ্যাক্টরিং করার উপযোগী ও নিরাপদ থাকে, সেই নিশ্চয়তা দিতে এই কনসেপ্টটি এসেছে।

### ৩. What problem it solves
*   **Fear of Refactoring:** কোড পরিবর্তন করতে ভয় পাওয়ার প্রবণতা দূর করে। টেস্ট স্যুট থাকলে আপনি নির্ভয়ে বড় ধরনের পরিবর্তন করতে পারবেন।
*   **Production Disasters:** প্রোডাকশনে হঠাৎ অ্যাপ ক্র্যাশ করা বা গুরুত্বপূর্ণ পেমেন্ট ফিচার নষ্ট হওয়া থেকে বাঁচায়।
*   **Poor Code Design:** টেস্ট লিখতে গেলে কোডকে মড্যুলার করতে হয়। ফলে স্প্যাগেটি কোড (Spaghetti code) তৈরি হওয়া স্বয়ংক্রিয়ভাবে বন্ধ হয়।
*   **Long-term Maintenance Cost:** প্রোডাকশনে যাওয়া বাগ ফিক্স করার খরচ ডেভেলপমেন্টের সময় ফিক্স করার চেয়ে ১০০ গুণ বেশি। টেস্টিং এই বিশাল খরচ কমায়।

### ৪. Real-life analogy
একটি বিমান তৈরির প্রক্রিয়ার সাথে এটি তুলনা করা যাক।
বিমান প্রস্তুত করার পর যদি সরাসরি ১০০০ যাত্রী নিয়ে আকাশে উড়িয়ে দেওয়া হয় এবং সেখানে গিয়ে কোনো ত্রুটি দেখা যায়, তবে সেটি হবে এক মহা বিপর্যয়। তাই বিমান আকাশে ওড়ানোর আগে উইন্ড টানেলে কৃত্রিম ঝড় তৈরি করে ডানাগুলোর স্থায়িত্ব পরীক্ষা করা হয়, ইঞ্জিনের প্রতিটি পার্টস স্ট্রেস টেস্ট করা হয় এবং টেস্ট পাইলট দিয়ে একা রানওয়েতে পরীক্ষা করা হয়। সফটওয়্যার ডেভেলপমেন্টের প্রতিটি টেস্ট কেস হলো বিমানের সেই প্রাক-উড্ডয়ন পরীক্ষা।

### ৫. How React works internally regarding this concept
*   React একটি ডিক্লেয়ারেটিভ ও কম্পোনেন্ট-বেসড লাইব্রেরি। এর ইন্টারনাল ফিচারগুলো যেমন: স্টেট আপডেট, রিঅ্যাক্ট লাইফসাইকেল এবং কনটেক্সট এপিআই ডেটা ফ্লো অত্যন্ত দ্রুত ও পরিবর্তনশীল।
*   যখন কোড টেস্ট করা হয়, তখন React-এর ইন্টারনাল কম্পোনেন্ট স্ট্যাক এবং মেমোরি রেন্ডারিং ট্র্যাক করা যায়।
*   অটোমেটেড টেস্টিং মূলত রিঅ্যাক্টের রেন্ডারিং ইঞ্জিনকে প্রতিটি স্টেটের জন্য সঠিক আউটপুট জেনারেট করতে বাধ্য করে। এটি ডেভেলপারকে কোডের আর্কিটেকচারাল ভুল (যেমন: ভুল ইফেক্ট ডিপেন্ডেন্সি, মেমোরি লিক) কোড রান করার মুহূর্তেই ওয়ার্নিং দিয়ে ধরিয়ে দেয়।

### ৬. Basic example
এখানে একটি জটিল ট্যাক্স ক্যালকুলেশন ফিচারের উদাহরণ দেওয়া হলো। টেস্ট কেস ছাড়া এই কোডে বাগ থাকলে বিশাল আর্থিক ক্ষতি হতে পারে।

**TaxCalculator.jsx**
```jsx
export function calculateTax(income) {
  if (income <= 0) return 0;
  if (income <= 10000) return income * 0.1;
  if (income <= 50000) return 1000 + (income - 10000) * 0.15;
  return 7000 + (income - 50000) * 0.2;
}
```

**TaxCalculator.test.jsx**
```jsx
import { calculateTax } from './TaxCalculator';

describe('Tax Calculation Logic', () => {
  test('should return 0 for zero or negative income', () => {
    expect(calculateTax(0)).toBe(0);
    expect(calculateTax(-500)).toBe(0);
  });

  test('should calculate 10% tax for income under 10k', () => {
    expect(calculateTax(5000)).toBe(500);
  });

  test('should calculate correct tax for middle income bracket', () => {
    expect(calculateTax(30000)).toBe(4000); // 1000 + 20000 * 0.15 = 4000
  });

  test('should calculate correct tax for high income bracket', () => {
    expect(calculateTax(60000)).toBe(9000); // 7000 + 10000 * 0.2 = 9000
  });
});
```

### ৭. Step-by-step explanation of the code
১. `calculateTax` হলো একটি পিওর ফাংশন যা ইনকাম ব্র্যাকেটের ওপর ভিত্তি করে ট্যাক্স হিসাব করে।
২. টেস্ট কোডে আমরা বিভিন্ন বাউন্ডারি ভ্যালু (যেমন ঋণাত্মক ইনকাম, সীমার একদম ভেতরের ভ্যালু ইত্যাদি) ইনপুট হিসেবে পাঠিয়ে আউটপুট চেক করছি।
৩. যদি ভবিষ্যতে কোনো ডেভেলপার ভুলে ট্যাক্সের পার্সেন্টেজ ওলটপালট করে দেয়, তবে এই টেস্টগুলো সাথে সাথে ফেইল করবে এবং প্রোডাকশনে ভুল ট্যাক্স ক্যালকুলেশন যাওয়া আটকে যাবে।

### ৮. Another real-world example
একটি হেলথকেয়ার ড্যাশবোর্ড অ্যাপ যেখানে রোগীর পালস রেট ও রক্তচাপ মনিটর করা হয়।
*   যদি কোনো রোগীর রিডিং বিপদজনক মাত্রায় থাকে, তবে সিস্টেম থেকে অটোমেটিক অ্যালার্ট ইমেইল পাঠানোর কথা।
*   টেস্টিং ছাড়া কোনো ডেভেলপার যদি ভুলবশত অ্যালার্টের `>` চিহ্নকে `<` বানিয়ে দেয়, তবে বিপদজনক অবস্থায় কোনো ইমেইল যাবে না। অটোমেটেড টেস্ট কেস সহজেই এই লজিক্যাল ত্রুটি সেকেন্ডের মধ্যে সনাক্ত করতে পারে।

### ৯. Common mistakes beginners make
*   **Treating tests as an afterthought:** প্রজেক্টের সব কাজ শেষ করে একদম শেষে টেস্ট লিখতে যাওয়া। এতে কোড টেস্ট-উপযোগী থাকে না এবং টেস্ট লেখা খুব কঠিন মনে হয়।
*   **Testing every single detail:** কোডের কভারেজ ১০০% করার জন্য লাইব্রেরির ভেতরের মেথড বা একদম অর্থহীন কোড লাইনের টেস্ট লেখা যা কোনো ভ্যালু ক্রিয়েট করে না।
*   **Not writing assertions:** টেস্ট কেসের ভেতর রেন্ডারিং ঠিকই করা কিন্তু কোনো `expect` বা এসারশন না রাখা। এর ফলে কোড ক্র্যাশ না করলে টেস্ট পাস হয়ে যায়, যা সঠিক টেস্ট নয়।

### ১০. Interview questions related to this topic
১. **Question:** What is Test-Driven Development (TDD)?
   *   **Answer:** TDD হলো এমন একটি সফটওয়্যার ডেভেলপমেন্ট পদ্ধতি যেখানে কোড লেখার আগেই সেই কোডের জন্য টেস্ট কেস লেখা হয় (Red phase), এরপর টেস্ট পাস করার জন্য ন্যূনতম কোড লেখা হয় (Green phase) এবং সবশেষে কোড রিফ্যাক্টর করা হয় (Refactor phase)।
২. **Question:** What is Code Coverage and how much of it is ideal?
   *   **Answer:** Code Coverage হলো একটি পরিমাপ যা দেখায় আপনার অ্যাপ্লিকেশনের মোট কোডের কত শতাংশ অংশ টেস্ট স্যুট দ্বারা টেস্ট করা হয়েছে। সাধারণত ৮০% কোড কভারেজ অত্যন্ত ভালো এবং আদর্শ ধরা হয়। ১০০% কভারেজ করতে গিয়ে অনেক সময় অপ্রয়োজনীয় টেস্টে সময় নষ্ট হয়।
৩. **Question:** Can automated testing replace manual QA teams?
   *   **Answer:** না, অটোমেটেড টেস্ট কখনোই হিউম্যান এক্সপেরিয়েন্স এবং ইউজার ফিডব্যাক ট্র্যাকিংকে সম্পূর্ণ রিপ্লেস করতে পারে না। এটি কিউএ টিমের কাজকে সহজ করে দেয় যেন তারা জটিল সিনারিও এবং ইউজার ইন্টারফেস এক্সপেরিয়েন্সে বেশি সময় দিতে পারে।
৪. **Question:** How does testing improve the software architecture?
   *   **Answer:** একটি কম্পোনেন্ট বা ফাংশনের টেস্ট লিখতে গেলে সেটিকে অবশ্যই ডিপেন্ডেন্সি মুক্ত ও মড্যুলার হতে হয়। যদি কোড ভালো না হয়, তবে তার টেস্ট লেখা অত্যন্ত কঠিন হয়ে যায়। তাই টেস্টিং ডেভেলপারকে ভালো আর্কিটেকচার অনুসরণ করতে বাধ্য করে।
৫. **Question:** What are the consequences of not writing tests in a large-scale project?
   *   **Answer:** কোডে নতুন ফিচার যোগ করতে অনেক বেশি সময় লাগবে, প্রচুর রিগ্রেশন বাগ প্রোডাকশনে যাবে, কোডের স্থায়িত্ব নষ্ট হবে এবং এক সময় প্রজেক্টটি মেইনটেইন করা অসম্ভব বা অত্যন্ত ব্যয়বহুল হয়ে যাবে।

### ১১. Best practices
*   **Practice TDD when possible:** বিশেষ করে যখন কোনো জটিল লজিক্যাল ফাংশন লিখছেন, আগে টেস্ট লিখে তারপর কোড লেখা শুরু করুন।
*   **Write clear test descriptions:** টেস্টের নামগুলো এমনভাবে লিখুন যাতে সেটি পড়লে বোঝা যায় কম্পোনেন্টটির আসল দায়িত্ব কী।
*   **Use testing libraries to block bad commits:** `husky` বা `lint-staged` ব্যবহার করে গিট কমিট করার আগে টেস্ট রান হওয়া বাধ্যতামূলক করুন।

### ১২. Performance considerations
*   **Run critical tests first:** আপনার টেস্ট স্যুটে ফাস্ট এবং গুরুত্বপূর্ণ টেস্টগুলো আগে চালান।
*   **Isolate DB/Network side-effects:** টেস্টের সময় যেন কখনো আসল নেটওয়ার্ক কল না হয়, যা টেস্ট রান অনেক ধীরগতির করে দেয়।

### ১৩. When NOT to use it
*   **Disposable prototypes:** যখন কোনো প্রজেক্ট মাত্র ১ বা ২ সপ্তাহের জন্য সাময়িক উদ্দেশ্যে তৈরি করা হচ্ছে যা পরে ফেলে দেওয়া হবে, তখন টেস্ট লেখা সময়ের অপচয়।

### ১৪. Comparison with similar concepts

| Concept | Manual QA | Automated Testing | TypeScript / Static Analysis |
| :--- | :--- | :--- | :--- |
| **Execution Time** | Hours to Days | Seconds to Minutes | Real-time during coding |
| **Cost of Setup** | Low | High (Initial investment) | Low |
| **Catching Logic Bugs**| High (Human perspective) | High (Consistent) | Low (Focuses only on Types) |
| **Regression Safety** | Low | Extremely High | Medium |

### ১৫. Summary in simple Bangla
টেস্টিং হলো একটি প্রজেক্টের নিরাপত্তা কবচ। এটি আমাদের কোডকে মড্যুলার করতে সাহায্য করে, রিফ্যাক্টরিংয়ের ভয় দূর করে এবং প্রোডাকশনে বড় ধরণের বাগ যাওয়া থেকে রক্ষা করে। যদিও শুরুতে টেস্ট লিখতে একটু বেশি সময় লাগে, কিন্তু দীর্ঘমেয়াদে এটি ডেভেলপারের হাজার হাজার ঘণ্টা সময় এবং প্রজেক্টের মেইনটেন্যান্স খরচ বাঁচিয়ে দেয়।

### ১৬. 5 MCQ questions (with answers)
১. কোড লেখার পূর্বে টেস্ট লেখার প্রক্রিয়াকে কী বলা হয়?
   ক) BDD
   খ) TDD
   গ) CI/CD
   ঘ) Dry Run
   **উত্তর:** খ

২. একটি অ্যাপ্লিকেশনের আদর্শ টেস্ট কভারেজ কত শতাংশ হওয়া উচিত?
   ক) ১০০% সব সময়
   খ) অন্তত ৮০%
   গ) ১০% হলেই চলে
   ঘ) কভারেজের প্রয়োজন নেই
   **উত্তর:** খ

৩. গিট কমিট করার পূর্বে অটোমেটিক টেস্ট রান করার জন্য নিচের কোনটি ব্যবহৃত হয়?
   ক) Redux
   খ) Husky
   গ) Babel
   ঘ) Webpack
   **উত্তর:** খ

৪. টেস্টিং সফটওয়্যার আর্কিটেকচারকে কীভাবে উন্নত করে?
   ক) কোডকে জটিল করে তোলে
   খ) কোডকে মড্যুলার ও ডিপেন্ডেন্সি মুক্ত করতে উৎসাহিত করে
   গ) ডাটাবেস কোয়েরি ফাস্ট করে
   ঘ) সিএসএস ডিজাইন উন্নত করে
   **উত্তর:** খ

৫. প্রোডাকশনে যাওয়া বাগ ফিক্স করার খরচ ডেভেলপমেন্টের সময় ফিক্স করার খরচের চেয়ে কেমন?
   ক) অনেক কম
   খ) সমান
   গ) অনেক গুণ বেশি
   ঘ) কোনো খরচই নেই
   **উত্তর:** গ

### 17. 5 Coding exercises (with solutions)

**Exercise 1:** একটি শপিং কার্ট আইটেমের প্রাইজ ক্যালকুলেটর ফাংশনের জন্য TDD অনুসরণ করে ৪টি টেস্ট কেস লিখুন।
```javascript
// Function signature: calculateTotal(items, discountCode)
// items is an array: [{ id: 1, name: 'Book', price: 100, qty: 2 }]
// discountCode 'SAVE10' gives 10% discount.
```
**Solution:**
```javascript
// calculateTotal.js
export function calculateTotal(items = [], discountCode = '') {
  let subtotal = items.reduce((sum, item) => sum + (item.price * item.qty), 0);
  if (discountCode === 'SAVE10') {
    subtotal = subtotal * 0.9;
  }
  return Number(subtotal.toFixed(2));
}

// calculateTotal.test.js
import { calculateTotal } from './calculateTotal';

describe('calculateTotal unit tests', () => {
  test('returns 0 for empty item list', () => {
    expect(calculateTotal([])).toBe(0);
  });

  test('calculates correct total without discount', () => {
    const items = [
      { price: 100, qty: 2 },
      { price: 50, qty: 1 }
    ];
    expect(calculateTotal(items)).toBe(250);
  });

  test('applies 10% discount with SAVE10 code', () => {
    const items = [{ price: 200, qty: 1 }];
    expect(calculateTotal(items, 'SAVE10')).toBe(180);
  });

  test('ignores invalid discount codes', () => {
    const items = [{ price: 200, qty: 1 }];
    expect(calculateTotal(items, 'INVALID')).toBe(200);
  });
});
```

**Exercise 2:** একটি পাসওয়ার্ড স্ট্রেন্থ চেকার ফাংশন আছে। এর জন্য এজ কেস (edge case) ও লজিক ভ্যালিডেট করার জন্য টেস্ট লিখুন।
```javascript
// isStrongPassword(password)
// Conditions: length >= 8, has at least 1 number, has at least 1 special char
```
**Solution:**
```javascript
// passwordValidator.js
export function isStrongPassword(password) {
  if (password.length < 8) return false;
  const hasNumber = /\d/.test(password);
  const hasSpecial = /[!@#$%^&*(),.?":{}|<>]/.test(password);
  return hasNumber && hasSpecial;
}

// passwordValidator.test.js
import { isStrongPassword } from './passwordValidator';

describe('isStrongPassword', () => {
  test('returns false if length is less than 8', () => {
    expect(isStrongPassword('Ab1!')).toBe(false);
  });

  test('returns false if no number is present', () => {
    expect(isStrongPassword('WeakPass!')).toBe(false);
  });

  test('returns false if no special character is present', () => {
    expect(isStrongPassword('WeakPass12')).toBe(false);
  });

  test('returns true for a strong password', () => {
    expect(isStrongPassword('StrongPass@123')).toBe(true);
  });
});
```

**Exercise 3:** এমন একটি ইমেইল ভ্যালিডেটর ফাংশন টেস্ট করুন যা ইনপুট স্ট্রিং সঠিক ইমেইল ফরম্যাটে না থাকলে `false` রিটার্ন করে।
**Solution:**
```javascript
// emailValidator.js
export function isValidEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

// emailValidator.test.js
import { isValidEmail } from './emailValidator';

describe('isValidEmail tests', () => {
  test('returns true for valid email formats', () => {
    expect(isValidEmail('rohit@example.com')).toBe(true);
  });

  test('returns false when missing @ sign', () => {
    expect(isValidEmail('rohitexample.com')).toBe(false);
  });

  test('returns false when missing domain suffix', () => {
    expect(isValidEmail('rohit@example')).toBe(false);
  });

  test('returns false for empty input or whitespace', () => {
    expect(isValidEmail(' ')).toBe(false);
  });
});
```

**Exercise 4:** রিঅ্যাক্ট `TodoList` কম্পোনেন্টে নতুন টাস্ক ইনপুট দিয়ে অ্যাড বাটনে ক্লিক করলে তা তালিকায় যুক্ত হচ্ছে কিনা তা পরীক্ষা করার ইন্টিগ্রেশন টেস্ট লিখুন।
**Solution:**
```jsx
// TodoList.jsx
import React, { useState } from 'react';
export function TodoList() {
  const [todos, setTodos] = useState([]);
  const [input, setInput] = useState('');
  
  const handleAdd = () => {
    if (input.trim()) {
      setTodos([...todos, input]);
      setInput('');
    }
  };

  return (
    <div>
      <input value={input} onChange={e => setInput(e.target.value)} placeholder="New Task" />
      <button onClick={handleAdd}>Add Task</button>
      <ul>
        {todos.map((todo, idx) => <li key={idx}>{todo}</li>)}
      </ul>
    </div>
  );
}

// TodoList.test.jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom';
import { TodoList } from './TodoList';

test('adds a todo item to the list', async () => {
  render(<TodoList />);
  const input = screen.getByPlaceholderText('New Task');
  const button = screen.getByRole('button', { name: /add task/i });
  
  await userEvent.type(input, 'Learn React Testing');
  await userEvent.click(button);
  
  expect(screen.getByText('Learn React Testing')).toBeInTheDocument();
  expect(input).toHaveValue(''); // Input should clear after submit
});
```

**Exercise 5:** একটি `UserDashboard` কম্পোনেন্ট আছে যা মক সার্ভার থেকে ব্যবহারকারীর রোল এনে যদি রোল "Admin" হয় তবে স্পেশাল "Admin Panel" লিঙ্ক দেখায়, অন্যথায় দেখায় না। এর জন্য টেস্ট কোড লিখুন।
**Solution:**
```jsx
// UserDashboard.jsx
import React, { useEffect, useState } from 'react';
export function UserDashboard({ fetchRole }) {
  const [role, setRole] = useState('');
  useEffect(() => {
    fetchRole().then(res => setRole(res));
  }, [fetchRole]);

  return (
    <div>
      <h1>Dashboard</h1>
      {role === 'Admin' && <a href="/admin">Admin Panel</a>}
    </div>
  );
}

// UserDashboard.test.jsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import { UserDashboard } from './UserDashboard';

test('shows admin panel link if role is Admin', async () => {
  const mockFetchRole = jest.fn().mockResolvedValue('Admin');
  render(<UserDashboard fetchRole={mockFetchRole} />);
  
  const link = await screen.findByRole('link', { name: /admin panel/i });
  expect(link).toBeInTheDocument();
});

test('does not show admin panel link if role is User', async () => {
  const mockFetchRole = jest.fn().mockResolvedValue('User');
  render(<UserDashboard fetchRole={mockFetchRole} />);
  
  // Wait for loading to finish (we query next tick)
  await screen.findByRole('heading', { name: /dashboard/i });
  const link = screen.queryByRole('link', { name: /admin panel/i });
  expect(link).not.toBeInTheDocument();
});
```
