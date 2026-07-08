# React Mastery: Part 6 - Error Boundaries, Suspense & Code Splitting

স্বাগতম! এই গাইডে আমরা শিখব কীভাবে রিয়েল-ওয়ার্ল্ড অ্যাপ্লিকেশনের ক্র্যাশ বা লোডিং টাইম নিখুঁতভাবে হ্যান্ডেল করতে হয়। আমরা জানব **Error Boundaries** এবং **Suspense with Code Splitting** সম্পর্কে।

---

## ১. Error Boundaries

### ১. Simple definition (বাংলায়)
Error Boundary হলো React-এর একটি বিশেষ ক্লাস কম্পোনেন্ট (Class Component) যা তার চাইল্ড কম্পোনেন্ট ট্রির যেকোনো জায়গায় ঘটে যাওয়া জাভাস্ক্রিপ্ট এররগুলোকে ক্যাচ বা ক্যাপচার করে এবং পুরো অ্যাপ্লিকেশন ক্র্যাশ হতে না দিয়ে স্ক্রিনে একটি সুন্দর "Fallback UI" (বিকল্প স্ক্রিন) প্রদর্শন করে।

### ২. Why this concept exists
React 16-এর আগে, যদি কোনো একটি ছোট চাইল্ড কম্পোনেন্টে জাভাস্ক্রিপ্ট এরর ঘটত (যেমন কোনো প্রপার্টি `undefined` পড়া), তবে পুরো পেজটি সাদা (blank screen) হয়ে যেত এবং পুরো অ্যাপ্লিকেশন ক্র্যাশ করত। এতে ইউজার এক্সপেরিয়েন্স চরমভাবে ব্যাহত হতো। এই সমস্যা সমাধান করতে Error Boundary আনা হয়েছে।

### ৩. What problem it solves
এটি জাভাস্ক্রিপ্ট এররগুলোর কারণে সম্পূর্ণ ইউজার ইন্টারফেস ক্র্যাশ হওয়া প্রতিরোধ করে এবং এররগুলোকে সেন্ট্রালি লগ (log) বা ট্র্যাক করার সুযোগ দেয়।

### ৪. Real-life analogy
একটি বড় জাহাজের জলরোধী কামরার (watertight compartments) কথা চিন্তা করুন। যদি জাহাজের এক কোণায় কোনো লিক হয় এবং পানি ঢুকতে শুরু করে, তবে ক্যাপ্টেন ওই নির্দিষ্ট কামরাটি সিল বা লক করে দেন যাতে পানি জাহাজের অন্য কামরাগুলোতে ছড়াতে না পারে এবং জাহাজটি ডুবে যাওয়া থেকে বেঁচে যায়। এখানে এক একটি কামরা হলো চাইল্ড কম্পোনেন্ট এবং সিল করার পদ্ধতিটি হলো Error Boundary।

### ৫. How React works internally regarding this concept
Error Boundary শুধুমাত্র Class Component দিয়ে তৈরি করা যায়। এর কারণ হলো এটি দুটি বিশেষ লাইফসাইকেল মেথডের ওপর কাজ করে যা ফাংশনাল কম্পোনেন্টে নেই:
1. `static getDerivedStateFromError(error)`: এটি যখনই কোনো চাইল্ডে এরর ঘটে, তখন রান করে এবং একটি অবজেক্ট রিটার্ন করে যা স্টেট আপডেট করে এররের ফলব্যাক দেখায়।
2. `componentDidCatch(error, errorInfo)`: এটি এররের ডিটেইলস এবং কোন ফাইলের কোন লাইনে এরর হয়েছে তার ইনফরমেশন পায়। এটি দিয়ে আমরা এরর ট্র্যাকিং সার্ভিসে (যেমন Sentry) লগ পাঠাতে পারি।

### ৬. Basic example
```jsx
import React, { Component } from 'react';

// 1. Creating the Error Boundary Class Component
class ErrorBoundary extends Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI.
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    // You can log the error to an error reporting service
    console.error("ErrorBoundary caught an error:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      // You can render any custom fallback UI
      return (
        <div style={{ padding: '20px', textAlign: 'center', border: '2px solid red' }}>
          <h2>Something went wrong.</h2>
          <p>Please refresh the page or contact support.</p>
        </div>
      );
    }

    return this.props.children;
  }
}

// 2. Child component that will crash on a specific state
function BuggyComponent() {
  const [counter, setCounter] = React.useState(0);

  if (counter === 5) {
    // Simulate a JavaScript error
    throw new Error('I crashed!');
  }

  return (
    <button onClick={() => setCounter(counter + 1)}>
      Increment Counter (Crashes at 5): {counter}
    </button>
  );
}

// 3. Usage
export default function App() {
  return (
    <div>
      <h1>My Awesome App</h1>
      <ErrorBoundary>
        <BuggyComponent />
      </ErrorBoundary>
    </div>
  );
}
```

### ৭. Step-by-step explanation of the code
* `ErrorBoundary` নামক ক্লাস কম্পোনেন্টটিতে `getDerivedStateFromError` এবং `componentDidCatch` মেথড ইমপ্লিমেন্ট করা হয়েছে।
* `BuggyComponent`-এ কাউন্টার ৫ হলে একটি এরর থ্রো করা হচ্ছে।
* যখন এরর থ্রো হবে, `ErrorBoundary` সেটি ধরে তার `hasError` স্টেট ট্রু করে ফলব্যাক স্ক্রিন দেখাবে, কিন্তু পেজের ওপরে থাকা `<h1>My Awesome App</h1>` ঠিকঠাক থাকবে, অর্থাৎ পুরো অ্যাপ ক্র্যাশ করবে না।

### ৮. Another real-world example (User Dashboard Widgets)
```jsx
// Wrapper for independent widgets so one failing doesn't break the whole dashboard
import React from 'react';
import ErrorBoundary from './ErrorBoundary';

function WeatherWidget() {
  // Let's assume weather data API returns null and crashes
  const weather = null;
  return <p>Temp: {weather.temp}°C</p>; // Will crash
}

function NewsWidget() {
  return <p>Latest News: React is amazing!</p>;
}

export function Dashboard() {
  return (
    <div style={{ display: 'flex', gap: '20px' }}>
      <ErrorBoundary>
        <WeatherWidget />
      </ErrorBoundary>
      <ErrorBoundary>
        <NewsWidget />
      </ErrorBoundary>
    </div>
  );
}
```
এখানে ওয়েদার উইজেট ক্র্যাশ করলেও নিউজ উইজেটটি স্ক্রিনে ঠিকভাবে দেখা যাবে কারণ প্রতিটির জন্য আলাদা আলাদা Error Boundary ব্যবহার করা হয়েছে।

### ৯. Common mistakes beginners make
* **ইভেন্ট হ্যান্ডলারের এরর ধরার চেষ্টা করা:** Error Boundary রেন্ডার হওয়ার সময় ঘটা এররগুলো ধরে। কিন্তু ইভেন্ট হ্যান্ডলার (যেমন বাটনের `onClick`), অ্যাসিনক্রোনাস কোড (যেমন `setTimeout` বা এপিআই রেসপন্স) এবং সার্ভার সাইড রেন্ডারিংয়ের এরর এটি ক্যাচ করতে পারে না। ইভেন্ট হ্যান্ডলারের এরর ক্যাচ করতে সাধারণ `try-catch` ব্যবহার করতে হবে।
* **ভুল জায়গায় র্যাপ করা:** পুরো অ্যাপকে একটিমাত্র এরর বাউন্ডারি দিয়ে র্যাপ করলে সামান্য এররেও পুরো অ্যাপের স্ক্রিন ব্ল্যাঙ্ক হয়ে যাবে। সাব-সেকশনগুলোকে আলাদা এরর বাউন্ডারি দিয়ে র্যাপ করা উচিত।

### ১০. Interview questions related to this topic
1. **Error Boundary কেন ফাংশনাল কম্পোনেন্ট দিয়ে তৈরি করা যায় না?**
   * উত্তর: কারণ ফাংশনাল কম্পোনেন্টে এরর হ্যান্ডল করার জন্য এখনো কোনো সমতুল্য হুক বা লাইফসাইকেল মেথড (`componentDidCatch` বা `getDerivedStateFromError`) তৈরি করা হয়নি।
2. **Error Boundary কোন কোন এরর ধরতে পারে না?**
   * উত্তর: ইভেন্ট হ্যান্ডলারের এরর, অ্যাসিনক্রোনাস কোড (যেমন `setTimeout`), সার্ভার সাইড রেন্ডারিং এবং স্বয়ং এরর বাউন্ডারির নিজের ভেতরের এরর।
3. **`getDerivedStateFromError` এবং `componentDidCatch` এর মধ্যে পার্থক্য কী?**
   * উত্তর: `getDerivedStateFromError` হলো সিঙ্ক্রোনাস এবং এটি স্টেট আপডেট করে ফলব্যাক UI রেন্ডার করার জন্য ব্যবহৃত হয়। `componentDidCatch` হলো সাইড-ইফেক্ট রান করার জায়গা, যেখানে এরর লগিং সার্ভিসে ডাটা পাঠানো হয়।

### ১১. Best practices
* প্রোজেক্টে সেন্ট্রাল একটি কাস্টম `ErrorBoundary` ক্লাস বানিয়ে রাখুন এবং প্রয়োজনে সেটি বিভিন্ন মডিউলে রিইউজ করুন।
* প্রোডাকশন লেভেলে এররের ডেটা জানার জন্য Sentry, LogRocket বা Bugsnag এর মতো সার্ভিসের সাথে কানেক্ট করুন।
* আপনি চাইলে `react-error-boundary` নামক চমৎকার ওপেন-সোর্স লাইব্রেরিটি ব্যবহার করতে পারেন যা ফাংশনাল স্টাইলে ডিক্লেয়ারেটিভ এরর বাউন্ডারি ব্যবহারের সুযোগ দেয়।

### ১২. Performance considerations
রেন্ডার টাইমে এরর ক্যাচ করা জাভাস্ক্রিপ্ট ইঞ্জিনের জন্য কিছুটা মেমরি কস্টলি, তবে অ্যাপের স্ট্যাবিলিটি ও ইউজার এক্সপেরিয়েন্সের তুলনায় এটি খুবই সামান্য।

### ১৩. When NOT to use it
সাধারণ বিজনেস লজিক ভ্যালিডেশন (যেমন ফর্মের ইমেইল ভুল হওয়া) এর জন্য Error Boundary ব্যবহার করবেন না। এগুলোর জন্য কম্পোনেন্ট লোকাল স্টেট ও কন্ডিশনাল রেন্ডারিং ব্যবহার করুন।

### ১৪. Comparison with similar concepts
* **Error Boundary vs Try-Catch:** Try-catch ব্যবহার করা হয় ইম্পারেটিভ কোডে (যেমন ইভেন্ট হ্যান্ডলার বা ফাংশনের ভেতর)। Error Boundary কাজ করে ডিক্লেয়ারেটিভ কোডে (JSX Component Trees)।

### ১৫. Summary in simple Bangla
Error Boundary হলো এমন একটি সিকিউরিটি দেয়াল যা চাইল্ড কম্পোনেন্টের এররকে আটকে পুরো অ্যাপ ক্র্যাশ হওয়া ঠেকায় এবং বদলে একটি সুন্দর এরর মেসেজ দেখায়।

### ১৬. 5 MCQ questions
1. Error Boundary নিচের কোন কম্পোনেন্ট দিয়ে তৈরি করতে হয়?
   * A) Functional Component
   * B) Class Component
   * C) Higher-Order Component
   * D) Controlled Component
   * *উত্তর: B*
2. Error Boundary নিচের কোন এররটি ক্যাচ করতে পারে না?
   * A) JSX রেন্ডার এরর
   * B) চাইল্ড কম্পোনেন্টের ভুল প্রপার্টি রিড করা
   * C) বাটন ক্লিকের onClick হ্যান্ডলারের এরর
   * D) চাইল্ডের কনস্ট্রাক্টরের এরর
   * *উত্তর: C*
3. ফলব্যাক UI দেখানোর জন্য স্টেট আপডেট করার কাজ কোন মেথডে করা হয়?
   * A) componentDidMount
   * B) componentDidCatch
   * C) static getDerivedStateFromError
   * D) render
   * *উত্তর: C*
4. এরর ট্র্যাকিং সিস্টেমে লগ পাঠানোর জন্য কোন মেথডটি ব্যবহৃত হয়?
   * A) static getDerivedStateFromError
   * B) componentDidCatch
   * C) componentWillUnmount
   * D) constructor
   * *উত্তর: B*
5. React 16-এর আগে চাইল্ড কম্পোনেন্ট ক্র্যাশ করলে সম্পূর্ণ অ্যাপে কী হতো?
   * A) অটো রিসেট হতো
   * B) সম্পূর্ণ স্ক্রিন সাদা বা ব্ল্যাঙ্ক হয়ে ক্র্যাশ করত
   * C) এরর বাউন্ডারি রেন্ডার হতো
   * D) কিছুই হতো না
   * *উত্তর: B*

### ১৭. 5 Coding exercises
1. একটি ক্লাস কম্পোনেন্ট ভিত্তিক `ErrorBoundary` তৈরি করুন যা এরর দেখালে একটি রিলোড বাটন দেখাবে এবং বাটনে ক্লিক করলে স্টেট রিসেট হবে।
2. একটি শপিং কার্ট কম্পোনেন্ট বানান যেখানে কোনো আইটেমের প্রাইস না থাকলে এরর থ্রো করবে এবং তা এরর বাউন্ডারি দিয়ে ক্যাচ করে আইটেম লেভেলে ফলব্যাক দেখাবে।
3. `react-error-boundary` লাইব্রেরিটি ডাউনলোড না করে ম্যানুয়ালি এরর বাউন্ডারির ভেতরের `componentDidCatch`-এ মক এপিআই কল করে এরর সার্ভারে লগ করুন।
4. একটি ইউজার প্রোফাইল পেজ তৈরি করুন যেখানে সাইডবার এবং মেইন কনটেন্ট আলাদা আলাদা এরর বাউন্ডারিতে থাকবে যাতে যেকোনো একটি ক্র্যাশ করলেও অন্যটি সচল থাকে।
5. একটি ইনপুট ফিল্ড ও বাটন তৈরি করুন। বাটনে ক্লিক করলে একটি এরর ম্যানুয়ালি থ্রো করান এবং দেখুন এরর বাউন্ডারি কীভাবে কাজ করছে।

---

## ২. Suspense and Code Splitting

### ১. Simple definition (বাংলায়)
* **Code Splitting:** কোড স্প্লিটিং হলো এমন একটি টেকনিক যার মাধ্যমে একটি বিশাল সাইজের React অ্যাপ্লিকেশন বান্ডেলকে (bundle) ছোট ছোট ছোট টুকরোতে ভাগ করা হয় এবং প্রয়োজন অনুযায়ী (lazy load) ব্রাউজারে ডাউনলোড করা হয়।
* **Suspense:** এটি React-এর একটি বিশেষ বিল্ট-ইন কম্পোনেন্ট যা ডাইনামিকালি লোড হতে থাকা কোনো চাইল্ড কম্পোনেন্ট বা ডেটার জন্য একটি সুন্দর লোডিং স্পিনার বা ফলব্যাক স্ক্রিন দেখায় যতক্ষণ না চাইল্ডের ডেটা লোড ফিনিশ হয়।

### ২. Why this concept exists
আধুনিক ওয়েব অ্যাপে প্রচুর কোড এবং থার্ড-পার্টি লাইব্রেরি থাকে। সাধারণ বিল্ড প্রসেসে সমস্ত কোড একসাথে একটিমাত্র বড় জাভাস্ক্রিপ্ট ফাইলে বান্ডেল হয়ে ব্রাউজারে লোড হয়। এর ফলে মোবাইল বা স্লো নেটের ইউজারদের প্রথমবার পেজ লোড হতে অনেক সময় লাগে। কোড স্প্লিটিং ব্রাউজারের ইনিশিয়াল লোড টাইম ও ব্যান্ডউইথ সাশ্রয় করতে সাহায্য করে।

### ৩. What problem it solves
এটি প্রথমবার পেজ লোড হওয়ার সময় অহেতুক সমস্ত ফাইল ডাউনলোড না করে অ্যাপের পারফরম্যান্স বাড়ায় (FCP - First Contentful Paint উন্নত করে)।

### ৪. Real-life analogy
আপনি একটি বড় বই অর্ডার করেছেন যা ২০টি অধ্যায় আছে। 
* **কোড স্প্লিটিং ছাড়া:** কুরিয়ার সার্ভিস পুরো বিশাল ২০ অধ্যায়ের বই একসাথে আপনার বাড়িতে ডেলিভারি দিল এবং সেটি বহন করা আপনার জন্য ভারী হলো।
* **কোড স্প্লিটিং ও সাসপেন্স সহ:** কুরিয়ার সার্ভিস আপনাকে শুধু ১ম অধ্যায় পাঠাল। আপনি সেটি পড়তে লাগলেন। যখন আপনি ২য় অধ্যায় পড়ার বাটনে চাপ দেবেন, ঠিক তখনই ক্ষণিকের জন্য একটি "অধ্যায় ২ লোড হচ্ছে..." স্টিকার আসবে (Suspense Fallback) এবং কুরিয়ার সার্ভিস ২য় অধ্যায়টি ডেলিভারি করবে। এতে আপনার মেমরি ও শক্তির অপচয় কম হলো।

### ৫. How React works internally regarding this concept
React-এ কোড স্প্লিট করার জন্য `React.lazy()` ফাংশন ব্যবহার করা হয়।
```javascript
const LazyComponent = React.lazy(() => import('./LazyComponent'));
```
`import()` হলো একটি ডাইনামিক ইম্পোর্ট যা একটি Promise রিটার্ন করে। React যখন এই ডাইনামিক ইম্পোর্টকে প্রথমবার রেন্ডার করতে যায়, তখন ইম্পোর্টটি রিজলভ হওয়ার আগ পর্যন্ত চাইল্ড থ্রেড একটি প্রমিজ (Promise) "throw" করে। প্যারেন্টে থাকা `<Suspense>` কম্পোনেন্ট এই প্রমিজটি ক্যাচ করে এবং প্রমিজ পেন্ডিং থাকা অবস্থায় তার `fallback` প্রপসের UI (যেমন স্পিনার) রেন্ডার করে। প্রমিজ সাকসেসফুলি রিজলভ হলে স্পিনারের জায়গায় আসল চাইল্ড কম্পোনেন্টটি বসে যায়।

### ৬. Basic example
```jsx
import React, { Suspense, lazy } from 'react';

// 1. Lazy Loading the Child Component
const LazyProfileCard = lazy(() => {
  // Simulating a delay to see the suspense effect
  return new Promise(resolve => {
    setTimeout(() => resolve(import('./ProfileCard')), 2000);
  });
});

// Mock ProfileCard for demonstration
// inside ProfileCard.jsx: export default function ProfileCard() { return <h3>I am lazy loaded!</h3> }

function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Dashboard</h1>
      
      {/* 2. Wrapping lazy component with Suspense */}
      <Suspense fallback={<div>Loading component, please wait...</div>}>
        <LazyProfileCard />
      </Suspense>
    </div>
  );
}

export default App;
```

### ৭. Step-by-step explanation of the code
* `lazy(() => import('./ProfileCard'))` দিয়ে কোড স্প্লিট করা হয়েছে। বিল্ড তৈরি করার সময় `ProfileCard` একটি আলাদা চঙ্ক বা ফাইলে বিভক্ত হবে।
* `<Suspense fallback={...}>` চাইল্ডটি পুরোপুরি ডাউনলোড হওয়ার আগ পর্যন্ত স্ক্রিনে "Loading component..." টেক্সটটি দেখাবে।
* ২ সেকেন্ড পর যখন প্রমিজ রিজলভ হবে, তখন কার্ডটি ভিজিবল হবে।

### ৮. Another real-world example (Route-Based Code Splitting)
```jsx
import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';

// Route components are lazy loaded
const Home = lazy(() => import('./routes/Home'));
const About = lazy(() => import('./routes/About'));
const Contact = lazy(() => import('./routes/Contact'));

function NavigationApp() {
  return (
    <Router>
      <nav>
        <Link to="/">Home</Link> | <Link to="/about">About</Link> | <Link to="/contact">Contact</Link>
      </nav>

      <Suspense fallback={<h2>Loading Page...</h2>}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </Suspense>
    </Router>
  );
}
```
এখানে ইউজার যখন শুধু `/about` লিংকে ক্লিক করবেন, কেবল তখনই ব্রাউজার নেটওয়ার্ক ট্যাব থেকে `About.js` চঙ্কটি ডাউনলোড করবে।

### ৯. Common mistakes beginners make
* **Suspense র্যাপ করতে ভুলে যাওয়া:** `React.lazy()` কম্পোনেন্টকে কোনো `<Suspense>` প্রোভাইডার ছাড়া রেন্ডার করলে রানটাইমে রিঅ্যাক্ট এরর দেবে যে অ্যাপ ক্র্যাশ করেছে।
* **ভুল এক্সপোর্ট ব্যবহার:** `React.lazy()` শুধুমাত্র **Default Export** করা কম্পোনেন্ট সাপোর্ট করে, এটি Named Export করা কম্পোনেন্ট সরাসরি লোড করতে পারে না।

### ১০. Interview questions related to this topic
1. **Code Splitting কী এবং কেন করা হয়?**
   * উত্তর: বড় বান্ডেলকে ছোট ছোট ফাইলে বিভক্ত করার পদ্ধতিকে কোড স্প্লিটিং বলে। এটি ব্রাউজারের ইনিশিয়াল লোড টাইম কমাতে এবং সাইটের গতি বাড়াতে ব্যবহৃত হয়।
2. **`React.lazy` কীভাবে কাজ করে এবং এর সাথে Suspense-এর সম্পর্ক কী?**
   * উত্তর: `React.lazy` ডাইনামিক ইম্পোর্টের মাধ্যমে ফাইলকে অলস বা লেজি লোড করে। লোড হওয়ার সময় এটি একটি প্রমিজ থ্রো করে যা `<Suspense>` ক্যাচ করে এবং প্রমিজ রিজলভ হওয়ার আগ পর্যন্ত ফলব্যাক লোডার দেখায়।
3. **সার্ভার সাইড রেন্ডারিং (SSR)-এ কি `React.lazy` ব্যবহার করা যায়?**
   * উত্তর: রিঅ্যাক্টের বেসিক `React.lazy` ট্র্যাডিশনাল SSR-এ কাজ করতে পারে না। সেক্ষেত্রে Next.js এর `next/dynamic` বা `@loadable/component` ব্যবহার করা হয়।

### ১১. Best practices
* রুট লেভেলে কোড স্প্লিটিং (Route-based splitting) করা সবচেয়ে সহজ ও কার্যকর।
* হেভি মডাল, জটিল গ্রাফ/চার্ট লাইব্রেরি বা রিচ টেক্সট এডিটর যেগুলো পেজ লোডের সাথে সাথে দরকার হয় না, সেগুলোকে কম্পোনেন্ট লেভেলে লেজি লোড করুন।

### ১২. Performance considerations
অতিরিক্ত কোড স্প্লিটিং করলে ছোট ছোট ফাইল ডাউনলোড করার নেটওয়ার্ক রিকোয়েস্ট ওভারহেড বেড়ে যেতে পারে। তাই যৌক্তিকভাবে বড় পার্টগুলোকে স্প্লিট করুন।

### ১৩. When NOT to use it
ছোট আকারের অ্যাপ্লিকেশনে কোড স্প্লিটিং করার কোনো প্রয়োজন নেই। এটি বান্ডেল ফাইল সাইজ খুব বড় (যেমন ১০০kb-র বেশি) হলেই কেবল প্র্যাকটিস করা উচিত।

### ১৪. Comparison with similar concepts
* **Lazy Loading vs Preloading:** Lazy loading হলো যখন দরকার তখন ডাউনলোড করা। Preloading হলো ব্রাউজার ফ্রি থাকলে ব্যাকগ্রাউন্ডে আগে থেকেই পরবর্তী সম্ভাব্য ফাইলটি ডাউনলোড করে রাখা।

### ১৫. Summary in simple Bangla
কোড স্প্লিটিং হলো সাইট ফাস্ট করার জন্য ফাইলগুলোকে ছোট ছোট টুকরো করা। আর সাসপেন্স হলো সেই টুকরোগুলো ইন্টারনেট থেকে ডাউনলোড হওয়ার সময় ব্রাউজারে একটি স্পিনার বা লোডার দেখানো।

### ১৬. 5 MCQ questions
1. কোড স্প্লিট করার জন্য রিঅ্যাক্টের বিল্ট-ইন ফাংশন কোনটি?
   * A) React.split()
   * B) React.lazy()
   * C) React.suspense()
   * D) React.load()
   * *উত্তর: B*
2. `React.lazy()` কম্পোনেন্ট লোড হওয়ার সময় স্ক্রিনে ফলব্যাক দেখানোর প্রোভাইডার কোনটি?
   * A) `<Error>`
   * B) `<Loading>`
   * C) `<Suspense>`
   * D) `<StrictMode>`
   * *উত্তর: C*
3. `React.lazy()` কোন ধরনের এক্সপোর্ট সমর্থন করে?
   * A) Named Export
   * B) Default Export
   * C) Global Export
   * D) CommonJS `module.exports`
   * *উত্তর: B*
4. কোড স্প্লিটিং করার মূল সুবিধা কোনটি?
   * A) কোড সিকিউর হয়
   * B) ইনিশিয়াল পেজ লোড স্পিড উন্নত হয়
   * C) ডাটাবেস কোয়েরি ফাস্ট হয়
   * D) ডবল রেন্ডারিং বন্ধ হয়
   * *উত্তর: B*
5. `<Suspense>`-এর ভেতরের আবশ্যক প্রপ কোনটি?
   * A) load
   * B) loading
   * C) fallback
   * D) child
   * *উত্তর: C*

### ১৭. 5 Coding exercises
1. একটি ড্যাশবোর্ড উইজেট বানান যেখানে হেভি চার্ট কম্পোনেন্টকে (যেমন Recharts ব্যবহার করে) লেজি লোড করবেন এবং সাসপেন্সে একটি সুন্দর কাস্টম স্কেলেটন লোডার (Skeleton Loader) দেখাবেন।
2. React Router ডোমে ৩টি আলাদা পেজ বানিয়ে রুট লেভেলে কোড স্প্লিটিং সেটআপ করুন।
3. একটি বাটন তৈরি করুন। বাটনে ক্লিক করলেই কেবল একটি ভারী লিগ্যাসি লাইব্রেরি লেজি লোড হয়ে রান করবে।
4. একাধিক সাসপেন্স বাউন্ডারি নেস্ট করে প্র্যাকটিস করুন এবং দেখুন কীভাবে চাইল্ড সাসপেন্স আগে রি-রেন্ডার শেষ করে।
5. এপিআই ডেটা সাসপেন্স ইন্টিগ্রেশন প্র্যাকটিস করার জন্য একটি প্রমিজ থ্রো করার কাস্টম ফেচার তৈরি করুন এবং সাসপেন্স দিয়ে রেন্ডার করুন।
