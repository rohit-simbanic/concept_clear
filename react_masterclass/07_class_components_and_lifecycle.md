# React Class Components & Lifecycle Methods: Masterclass

---

## Topic 1: What is the order of lifecycle method calls in Class Based Components?

### ১. Simple definition (বাংলায়)
React Class Components-এর তৈরি হওয়া থেকে শুরু করে স্ক্রিনে দেখানো, আপডেট হওয়া এবং শেষ পর্যন্ত স্ক্রিন থেকে মুছে যাওয়া (destroy) পর্যন্ত যে বিভিন্ন ধাপ বা পর্যায়গুলো পার হতে হয়, সেগুলোকে **Component Lifecycle** বলে। আর এই বিভিন্ন ধাপে React যে বিশেষ Method-গুলোকে স্বয়ংক্রিয়ভাবে কল করে, সেগুলোকে **Lifecycle Methods** বলা হয়। Lifecycle-কে মূলত তিনটি প্রধান ভাগে ভাগ করা হয়: 
1. **Mounting** (তৈরি হওয়া ও স্ক্রিনে আসা)
2. **Updating** (State বা Props পরিবর্তনের কারণে আপডেট হওয়া)
3. **Unmounting** (স্ক্রিন থেকে চলে যাওয়া)

---

### ২. Why this concept exists
একটি Component যখন ব্রাউজারে রেন্ডার হয়, তখন তার বিভিন্ন ধাপে বিভিন্ন কাজের প্রয়োজন হয়। যেমন: Component তৈরি হওয়ার সময় ডাটাবেজ বা API থেকে ডাটা আনা, স্ক্রিনে দেখানোর পর কোনো timer সেট করা, State চেঞ্জ হলে UI আপডেট করা, এবং Component-টি স্ক্রিন থেকে চলে যাওয়ার সময় মেমোরি খালি করা। এই কাজগুলো যেন নির্দিষ্ট সময়ে সুшৃঙ্খলভাবে করা যায়, সেই জন্য Lifecycle Methods-এর ধারণাটি আনা হয়েছে।

---

### ৩. What problem it solves
যদি Lifecycle methods না থাকত, তবে আমরা বুঝতে পারতাম না কখন API call করতে হবে, কখন DOM ready হয়েছে এবং কখন Event listener রিমুভ করতে হবে। এর ফলে মেমোরি লিক (Memory Leak) হতো, অযথা CPU রিসোর্স নষ্ট হতো এবং অ্যাপ্লিকেশনের পারফরম্যান্স খারাপ হতো। Lifecycle methods ডেভেলপারদের প্রতিটা ধাপের ওপর পূর্ণ নিয়ন্ত্রণ দেয়।

---

### ৪. Real-life analogy
মানুষের জীবনের সাথে এর তুলনা করা যায়:
* **Mounting (জন্ম):** একটি শিশুর জন্ম নেওয়া এবং দুনিয়াতে প্রথমবার আসা।
* **Updating (বৃদ্ধি ও পরিবর্তন):** বয়স বাড়ার সাথে সাথে মানুষের জ্ঞান, চেহারা বা পোশাক পরিবর্তন হওয়া।
* **Unmounting (মৃত্যু):** জীবনাবসান হওয়া এবং পৃথিবী থেকে বিদায় নেওয়া।

প্রতিটি পর্যায়ে যেমন মানুষের কিছু নির্দিষ্ট কাজ থাকে (যেমন জন্মের পর ভ্যাকসিন নেওয়া, বড় হয়ে পড়াশোনা করা, মৃত্যুর আগে সম্পত্তি বন্টন করা), তেমনি React component-এর ক্ষেত্রেও নির্দিষ্ট সময়ে নির্দিষ্ট Lifecycle method কল হয়।

---

### ৫. How React works internally regarding this concept
React internally একটি Component-কে নিয়ে কাজ করার সময় Virtual DOM তৈরি করে।
* **Mounting Phase:** React প্রথমে `constructor` কল করে Component-এর instance তৈরি করে। এরপর `static getDerivedStateFromProps` রান করে (যদি থাকে)। তারপর `render()` মেথড রান করে Virtual DOM তৈরি করে এবং তা ব্রাউজারের Real DOM-এ পুশ করে। DOM আপডেট শেষ হলে React `componentDidMount()` কল করে।
* **Updating Phase:** যখন `setState()` বা নতুন `props` আসে, তখন React প্রথমে `getDerivedStateFromProps` চালায়, তারপর `shouldComponentUpdate` মেথড দিয়ে চেক করে রেন্ডার করা প্রয়োজন কি না। প্রয়োজন হলে `render()` আবার চলে, এরপর `getSnapshotBeforeUpdate` দিয়ে DOM-এর আগের অবস্থা নেওয়া হয় এবং অবশেষে Real DOM আপডেট হওয়ার পর `componentDidUpdate()` কল হয়।
* **Unmounting Phase:** Component-টি যখন স্ক্রিন থেকে রিমুভ হতে যায়, React তখন `componentWillUnmount()` কল করে ক্লিনআপের কাজগুলো সম্পন্ন করে।

---

### ৬. Basic example
Here is a basic React class component showing the lifecycle methods in their exact order of execution:

```javascript
import React, { Component } from 'react';

class LifecycleDemo extends Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };
    console.log('1. constructor called');
  }

  static getDerivedStateFromProps(props, state) {
    console.log('2. getDerivedStateFromProps called');
    return null;
  }

  componentDidMount() {
    console.log('4. componentDidMount called');
  }

  shouldComponentUpdate(nextProps, nextState) {
    console.log('5. shouldComponentUpdate called');
    return true;
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    console.log('6. getSnapshotBeforeUpdate called');
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    console.log('7. componentDidUpdate called');
  }

  componentWillUnmount() {
    console.log('8. componentWillUnmount called');
  }

  increment = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    console.log('3. render called');
    return (
      <div style={{ padding: '20px', border: '1px solid #ccc' }}>
        <p>Count: {this.state.count}</p>
        <button onClick={this.increment}>Increment</button>
      </div>
    );
  }
}

export default LifecycleDemo;
```

---

### ৭. Step-by-step explanation of the code
* **Mounting Phase-এর সময়:**
  1. প্রথমে `constructor` রান হয় এবং কনসোলে `'1. constructor called'` প্রিন্ট হয়। এখানে State ইনিশিয়ালাইজ করা হয়।
  2. তারপর `static getDerivedStateFromProps` রান হয় এবং `'2. getDerivedStateFromProps called'` প্রিন্ট হয়।
  3. এরপর `render()` মেথড চলে, যা UI তৈরি করে এবং `'3. render called'` প্রিন্ট হয়।
  4. DOM-এ Component-টি যুক্ত হওয়ার পর `componentDidMount()` রান হয় এবং `'4. componentDidMount called'` প্রিন্ট হয়।
* **Updating Phase-এর সময় (যখন Increment বাটনে ক্লিক করা হয়):**
  1. State চেঞ্জ হওয়ায় প্রথমে `getDerivedStateFromProps` আবার কল হয়।
  2. তারপর `shouldComponentUpdate` কল হয়ে চেক করে রেন্ডার হবে কি না। কনসোলে `'5. shouldComponentUpdate called'` প্রিন্ট হয়। এটি `true` রিটার্ন করায় প্রসেসটি এগিয়ে যায়।
  3. এরপর পুনরায় `render()` মেথড চলে এবং নতুন UI হিসাব করে। কনসোলে `'3. render called'` আবার দেখায়।
  4. রেন্ডার শেষ হওয়ার পর কিন্তু DOM পরিবর্তনের ঠিক আগে `getSnapshotBeforeUpdate` কল হয় এবং `'6. getSnapshotBeforeUpdate called'` প্রিন্ট করে।
  5. ব্রাউজারের DOM আপডেট সম্পন্ন হওয়ার পর `componentDidUpdate` কল হয় এবং `'7. componentDidUpdate called'` প্রিন্ট করে।
* **Unmounting Phase-এর সময়:**
  1. Component-টি ধ্বংস হওয়ার ঠিক আগে `componentWillUnmount` কল হয় এবং `'8. componentWillUnmount called'` প্রিন্ট হয়।

---

### ৮. Another real-world example
Let's consider a scenario where we fetch data from a public API when the component mounts and log updates to the console whenever the state changes:

```javascript
import React, { Component } from 'react';

class UserProfile extends Component {
  constructor(props) {
    super(props);
    this.state = {
      user: null,
      loading: true,
      userId: 1
    };
    console.log('[Constructor] Initializing state');
  }

  static getDerivedStateFromProps(props, state) {
    console.log('[getDerivedStateFromProps] Synced props to state');
    return null;
  }

  componentDidMount() {
    console.log('[componentDidMount] Component is on screen. Fetching user...');
    this.fetchUserData(this.state.userId);
  }

  shouldComponentUpdate(nextProps, nextState) {
    console.log('[shouldComponentUpdate] Checking if update is necessary');
    return nextState.userId !== this.state.userId || nextState.user !== this.state.user || nextState.loading !== this.state.loading;
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    console.log('[getSnapshotBeforeUpdate] Capturing DOM state before update');
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    console.log('[componentDidUpdate] DOM updated. Checking for user ID change');
    if (prevState.userId !== this.state.userId) {
      this.fetchUserData(this.state.userId);
    }
  }

  componentWillUnmount() {
    console.log('[componentWillUnmount] Clean up tasks before component destroys');
  }

  fetchUserData = (id) => {
    this.setState({ loading: true });
    fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
      .then(response => response.json())
      .then(data => this.setState({ user: data, loading: false }));
  };

  nextUser = () => {
    this.setState(prevState => ({ userId: prevState.userId + 1 }));
  };

  render() {
    console.log('[Render] Generating JSX');
    const { user, loading } = this.state;
    return (
      <div style={{ padding: '20px', border: '1px solid #ccc' }}>
        {loading ? (
          <p>Loading user data...</p>
        ) : (
          <div>
            <h3>{user.name}</h3>
            <p>Email: {user.email}</p>
          </div>
        )}
        <button onClick={this.nextUser}>Load Next User</button>
      </div>
    );
  }
}

export default UserProfile;
```

---

### ৯. Common mistakes beginners make
* **`render()`-এর ভেতর `setState()` কল করা:** এটি একটি ইনফিনিট লুপ (infinite loop) তৈরি করে। কারণ `setState()` কল করলে Component আবার `render` হয়, এবং `render`-এর ভেতর আবার `setState` থাকায় এটি চিরকাল চলতে থাকে।
* **`componentDidUpdate`-এ কন্ডিশন ছাড়া `setState` ব্যবহার করা:** এখানে কন্ডিশন ছাড়া `setState` ব্যবহার করলে আবার ইনফিনিট লুপ তৈরি হবে।
* **`componentWillUnmount`-এ মেমোরি ক্লিনআপ না করা:** Event Listeners বা Timers-কে রিমুভ না করলে Component স্ক্রিন থেকে চলে যাওয়ার পরও মেমোরিতে সেগুলো চলতে থাকে, যা Memory Leak ঘটায়।

---

### ১০. Interview questions related to this topic
* **Question:** What is the correct order of lifecycle methods in the mounting phase?
  * **Answer:** `constructor` -> `getDerivedStateFromProps` -> `render` -> `componentDidMount`.
* **Question:** Why shouldn't we call `setState()` in `shouldComponentUpdate`?
  * **Answer:** কারণ `shouldComponentUpdate` এর কাজ হলো রেন্ডার হবে কি না তা নির্ধারণ করা। এখানে `setState` কল করলে আবার আপডেট ফেজ শুরু হবে এবং এটি ইনফিনিট লুপ তৈরি করবে।
* **Question:** What is the difference between `componentDidMount` and `componentDidUpdate`?
  * **Answer:** `componentDidMount` শুধুমাত্র Component-টি প্রথমবার রেন্ডার হয়ে DOM-এ যুক্ত হওয়ার পর একবার কল হয়। আর `componentDidUpdate` প্রতিটি State বা Props আপডেটের পর ব্রাউজার DOM রি-রেন্ডার হওয়ার পর কল হয়।
* **Question:** What are the deprecated lifecycle methods in React?
  * **Answer:** `componentWillMount`, `componentWillReceiveProps`, এবং `componentWillUpdate` মেথডগুলো এখন অবলুপ্ত (deprecated) এবং এগুলোর নামের আগে `UNSAFE_` যোগ করা হয়েছে।
* **Question:** When is `getSnapshotBeforeUpdate` called?
  * **Answer:** এটি `render` মেথড কল হওয়ার পর এবং ব্রাউজারের DOM আপডেট হওয়ার ঠিক আগে কল হয়। এর মাধ্যমে আমরা DOM-এর আগের কোনো তথ্য (যেমন স্ক্রল পজিশন) সংরক্ষণ করতে পারি।

---

### ১১. Best practices
* সব সময় API কল বা ডিরেক্ট DOM ম্যানিপুলেশনের কাজ `componentDidMount`-এ করতে হবে, `constructor`-এ নয়।
* `componentDidUpdate`-এ `setState` করার আগে সব সময় `prevProps` বা `prevState`-এর সাথে বর্তমান props/state চেক করতে হবে।
* React Hook (Functional Component) ব্যবহারের দিকে ঝুঁকুন, কারণ Class lifecycle মেথডগুলোর তুলনায় `useEffect` দিয়ে কোড অনেক সহজ ও সুন্দর করা যায়।

---

### ১২. Performance considerations (if applicable)
* `shouldComponentUpdate` মেথডটি ব্যবহার করে অপ্রয়োজনীয় রি-রেন্ডার রোধ করা যায়। এটি `false` রিটার্ন করলে পরবর্তী রেন্ডার এবং আপডেট ফেজ বন্ধ হয়ে যায়, যা অ্যাপ্লিকেশনের পারফরম্যান্স বাড়ায়।
* `componentDidUpdate`-এ অপ্রয়োজনীয় ডাটা ফেচ বা লজিক রান করা থেকে বিরত থাকুন।

---

### ১৩. When NOT to use it
* যদি আপনার Component-এ কোনো State বা Side-effect (যেমন API call, timer, listener) না থাকে, তবে Class Component এবং এর Lifecycle methods ব্যবহারের কোনো প্রয়োজন নেই। সরাসরি Functional Component ব্যবহার করা উচিত।
* নতুন React প্রজেক্টে ক্লাস কম্পোনেন্ট ব্যবহার করা এড়িয়ে চলা উচিত, কারণ React টিম এখন Functional Components এবং Hooks-কে উৎসাহিত করে।

---

### ১৪. Comparison with similar concepts
| Feature | Class Component Lifecycle | Functional Component (Hooks) equivalent |
| :--- | :--- | :--- |
| **Mounting** | `componentDidMount` | `useEffect(() => {}, [])` |
| **Updating** | `componentDidUpdate` | `useEffect(() => {}, [dependency])` |
| **Unmounting** | `componentWillUnmount` | `useEffect(() => { return () => { /* cleanup */ } }, [])` |
| **Skip render** | `shouldComponentUpdate` | `React.memo` or `useMemo` |

---

### ১৫. Summary in simple Bangla
ক্লাস কম্পোনেন্ট লাইফসাইকেল হলো একটি কম্পোনেন্টের জন্ম (Mounting), বৃদ্ধি (Updating) এবং বিদায় (Unmounting)-এর বিভিন্ন ধাপ। মাউন্টিং ফেজে প্রথমে `constructor` রান হয়, তারপর `render` এবং শেষে `componentDidMount` রান হয়। কম্পোনেন্ট আপডেট হলে `render` আবার চলে এবং সর্বশেষে `componentDidUpdate` কল হয়। আর কম্পোনেন্টটি স্ক্রিন থেকে চলে যাওয়ার সময় `componentWillUnmount` কল হয় ক্লিনআপ করার জন্য।

---

### ১৬. 5 MCQ questions
1. Component প্রথমবার DOM-এ রেন্ডার হওয়ার পর কোন মেথডটি স্বয়ংক্রিয়ভাবে একবারই কল হয়?
   * A) `componentDidUpdate`
   * B) `componentDidMount`
   * C) `constructor`
   * D) `render`
   * **Correct Answer: B**
2. নিচের কোনটি মাউন্টিং (Mounting) ফেজের সঠিক ক্রম?
   * A) `render` -> `constructor` -> `componentDidMount`
   * B) `constructor` -> `render` -> `componentDidMount`
   * C) `componentDidMount` -> `render` -> `constructor`
   * D) `constructor` -> `componentDidMount` -> `render`
   * **Correct Answer: B**
3. Update ফেজে `render` হওয়ার পর এবং DOM পরিবর্তনের ঠিক আগে কোন মেথডটি কল হয়?
   * A) `shouldComponentUpdate`
   * B) `getDerivedStateFromProps`
   * C) `getSnapshotBeforeUpdate`
   * D) `componentDidUpdate`
   * **Correct Answer: C**
4. `shouldComponentUpdate` মেথডটি কী রিটার্ন করে?
   * A) Object
   * B) Boolean (true/false)
   * C) Array
   * D) String
   * **Correct Answer: B**
5. নিচের কোন মেথডটি অবলুপ্ত (Deprecated)?
   * A) `componentDidMount`
   * B) `componentWillUnmount`
   * C) `componentWillMount`
   * D) `componentDidUpdate`
   * **Correct Answer: C**

---

### ১৭. 5 Coding exercises
1. একটি React Class Component তৈরি করুন যা কনসোলে মাউন্টিং, আপডেটিং এবং আনমাউন্টিংয়ের প্রতিটা মেথডের নাম এবং কল হওয়ার সিকোয়েন্স প্রিন্ট করবে।
2. `shouldComponentUpdate` মেথড ব্যবহার করে এমন একটি কাউন্টার কম্পোনেন্ট তৈরি করুন যা শুধুমাত্র বিজোড় (Odd) সংখ্যাগুলোর জন্য UI আপডেট করবে।
3. একটি কম্পোনেন্ট লিখুন যা `getSnapshotBeforeUpdate` ব্যবহার করে একটি স্ক্রলযোগ্য ডিভ (scrollable div)-এর আগের স্ক্রল হাইট (scroll height) সংরক্ষণ করবে এবং আপডেট হওয়ার পর স্ক্রল পজিশন আগের জায়গায় রাখবে।
4. এমন একটি ক্লাস কম্পোনেন্ট লিখুন যা Props হিসেবে আসা `userId` চেঞ্জ হলে `componentDidUpdate` ব্যবহার করে নতুন ডাটা রিলোড করবে।
5. একটি ক্লাস কম্পোনেন্ট লিখুন যেখানে `static getDerivedStateFromProps` ব্যবহার করে Props থেকে আসা ডাটা সরাসরি State-এ সিঙ্ক (sync) করা হবে।

---
---

## Topic 2: Why do we use componentDidMount?

### ১. Simple definition (বাংলায়)
`componentDidMount()` হলো React-এর একটি লাইফসাইকেল মেথড যা কোনো Component প্রথমবার ব্রাউজারের DOM-এ যুক্ত (mount) হওয়ার ঠিক পরপরই স্বয়ংক্রিয়ভাবে একবারের জন্য কল হয়। এটি মূলত Side Effects-এর কাজ (যেমন- API থেকে ডাটা আনা, DOM উপাদানগুলোতে সরাসরি হাত দেওয়া বা Timer শুরু করা)-এর জন্য সবচেয়ে আদর্শ জায়গা।

---

### ২. Why this concept exists
React যখন একটি Component রেন্ডার করে, তখন এর HTML এলিমেন্টগুলো সাথে সাথেই ব্রাউজারে দৃশ্যমান হয় না। রেন্ডার প্রসেস সম্পন্ন হয়ে যখন ব্রাউজার DOM-এ Component-এর নোডগুলো যুক্ত হয়, ঠিক তখনই কোনো স্ক্রিপ্ট রান করার প্রয়োজন হতে পারে। ব্রাউজার DOM প্রস্তুত হওয়ার আগে যদি আমরা DOM এলিমেন্ট অ্যাক্সেস করতে চাই বা ডাটা লোড করতে চাই, তবে এরর দেখা দেবে। এই সমস্যা সমাধানের জন্যই `componentDidMount` তৈরি করা হয়েছে।

---

### ৩. What problem it solves
* **অপ্রস্তুত DOM অ্যাক্সেস রোধ করা:** `constructor` বা `render` মেথডের মধ্যে DOM এলিমেন্ট অ্যাক্সেস করতে গেলে ব্রাউজার তা খুঁজে পায় না, কারণ তখনো DOM তৈরিই হয়নি। `componentDidMount` নিশ্চিত করে যে DOM সম্পূর্ণ রেডি।
* **ডাটা ফেচিং সঠিক সময়ে করা:** প্রথমবার স্ক্রিন লোড হওয়ার সাথে সাথে API থেকে ডাটা নিয়ে এসে UI-তে দেখানোর কাজটা খুব সহজে এবং নিরাপদভাবে এখানে করা যায়।

---

### ৪. Real-life analogy
ধরুন, আপনি একটি নতুন দোকান (Shop) উদ্বোধন করছেন। দোকানটি উদ্বোধন করে শাটার খোলার পর এবং সব সাজসজ্জা শেষ হওয়ার পরই তো আপনি কাস্টমারদের ভেতরে ঢুকতে দেবেন এবং বেচাকেনা শুরু করবেন। তার আগে নিশ্চয়ই নয়। এখানে দোকান উদ্বোধন করা ও শাটার খোলা হলো `componentDidMount`। দোকান সম্পূর্ণ প্রস্তুত হওয়ার পরই লাইভ কাজ শুরু হয়।

---

### ৫. How React works internally regarding this concept
React যখন Component মাউন্ট করতে শুরু করে, তখন প্রথমে Virtual DOM তৈরি করে এবং তা ব্রাউজারের Real DOM-এ কনভার্ট করে পুশ করে। ব্রাউজার যখন সেই HTML নোডগুলো রিসিভ করে এবং লেআউট পেন্টিং সম্পন্ন করে, তখন React তার অভ্যন্তরীণ ট্র্যাকিং থেকে বুঝতে পারে যে Component-টি সফলভাবে স্ক্রিনে মাউন্ট হয়েছে। ঠিক তখনই React কলস্ট্যাকে `componentDidMount` মেথডটিকে ট্রিগার করে।

---

### ৬. Basic example
Here is a basic example of calling an API inside `componentDidMount` to fetch data and update the component's state:

```javascript
import React, { Component } from 'react';

class DataFetcher extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      loading: true
    };
  }

  componentDidMount() {
    // Fetching data right after the component mounts
    fetch('https://jsonplaceholder.typicode.com/posts?_limit=5')
      .then(response => response.json())
      .then(posts => this.setState({ data: posts, loading: false }))
      .catch(error => console.error('Error fetching data:', error));
  }

  render() {
    const { data, loading } = this.state;

    if (loading) {
      return <h2>Loading posts...</h2>;
    }

    return (
      <div>
        <h3>Posts List:</h3>
        <ul>
          {data.map(post => (
            <li key={post.id}>{post.title}</li>
          ))}
        </ul>
      </div>
    );
  }
}

export default DataFetcher;
```

---

### ৭. Step-by-step explanation of the code
1. `constructor`-এর মধ্যে `data` খালি অ্যারে এবং `loading` `true` দিয়ে State ইনিশিয়ালাইজ করা হয়েছে।
2. প্রথমবার যখন `render()` রান হয়, তখন `loading` এর মান `true` থাকায় স্ক্রিনে "Loading posts..." দেখায়।
3. রেন্ডার শেষ হয়ে DOM ব্রাউজারে মাউন্ট হওয়ার ঠিক পরেই `componentDidMount()` রান হয়।
4. `componentDidMount()`-এর ভেতর `fetch` API-এর মাধ্যমে ফেক পোস্টের ডাটা আনা হয়।
5. ডাটা সাকসেসফুলি ফেচ হওয়ার পর `this.setState({ data: posts, loading: false })` কল করে State আপডেট করা হয়।
6. State চেঞ্জ হওয়ার ফলে Component আবার রি-রেন্ডার হয়। এবার `loading` এর মান `false` হওয়ায় পোস্টগুলোর লিস্ট স্ক্রিনে সুন্দরভাবে রেন্ডার হয়।

---

### ৮. Another real-world example
Let's look at another example where we focus a text input field automatically and set a timer after the page renders:

```javascript
import React, { Component } from 'react';

class AutoFocusInput extends Component {
  constructor(props) {
    super(props);
    this.inputRef = React.createRef();
    this.state = {
      seconds: 0
    };
  }

  componentDidMount() {
    // 1. Focus the input field automatically
    this.inputRef.current.focus();

    // 2. Setup a timer to update seconds state every second
    this.timer = setInterval(() => {
      this.setState(prevState => ({ seconds: prevState.seconds + 1 }));
    }, 1000);
  }

  componentWillUnmount() {
    // Clear timer when component destroys
    clearInterval(this.timer);
  }

  render() {
    return (
      <div style={{ padding: '20px' }}>
        <h3>Time Spent: {this.state.seconds} seconds</h3>
        <label htmlFor="username">Username: </label>
        <input 
          id="username" 
          ref={this.inputRef} 
          type="text" 
          placeholder="Type here..." 
        />
      </div>
    );
  }
}

export default AutoFocusInput;
```

---

### ৯. Common mistakes beginners make
* **Constructor-এ API Fetch করা:** অনেকে ডাটা দ্রুত লোড করার জন্য constructor-এর ভেতর `fetch` কল করে বসেন। এটি ভুল, কারণ তখনো DOM নোড তৈরি হয়নি এবং React এই সময়ে কোনো প্রকার Side effects চালানো সাপোর্ট করে না।
* **`componentDidMount`-এর ভেতর অহেতুক ডিরেক্ট DOM ম্যানিপুলেশন:** যদিও এটি নিরাপদ, তবুও অপ্রয়োজনে জাভাস্ক্রিপ্ট দিয়ে DOM এলিমেন্ট সরাসরি পরিবর্তন করা উচিত নয়, কারণ React-এর নিজস্ব স্টেট ম্যানেজমেন্ট এতে ব্যাহত হতে পারে।
* **Timer/Event Listener ক্লিনআপ না করা:** এখানে কোনো `setInterval` বা Event listener এড করলে অনেকেই তা `componentWillUnmount`-এ রিমুভ করতে ভুলে যান।

---

### ১০. Interview questions related to this topic
* **Question:** Can we call `setState()` in `componentDidMount()`?
  * **Answer:** হ্যাঁ, কল করা যায়। এটি করার ফলে সাথে সাথে একটি অতিরিক্ত রি-রেন্ডার ট্রিগার হবে, তবে ব্যবহারকারী এটি দেখতে পাওয়ার আগেই ব্রাউজার স্ক্রিন আপডেট করে নেয়। তবে অযথা পারফরম্যান্স নষ্ট রোধে অতিরিক্ত রি-রেন্ডার এড়িয়ে চলাই ভালো।
* **Question:** Why should API calls be made in `componentDidMount` instead of `constructor`?
  * **Answer:** Constructor-এর কাজ শুধু State ইনিশিয়ালাইজ করা এবং বাইন্ডিং করা। এখানে ডাটা ফেচ করলে রেন্ডারিং ব্লক হতে পারে এবং ব্রাউজার ফ্রিজ হয়ে যাওয়ার সম্ভাবনা থাকে। এছাড়া, SSR (Server-Side Rendering)-এর ক্ষেত্রে Constructor একাধিকবার রান হতে পারে কিন্তু `componentDidMount` সার্ভারে রান হয় না, কেবল ক্লায়েন্ট সাইডে রান হয়।
* **Question:** Does `componentDidMount` run on Server-Side Rendering (SSR)?
  * **Answer:** না, `componentDidMount` মেথডটি শুধুমাত্র ক্লায়েন্ট সাইড (Client-side/Browser)-এ রান হয়, সার্ভার-সাইড রেন্ডারিংয়ের সময় এটি চলে না।
* **Question:** What is the equivalent of `componentDidMount` in React Hooks?
  * **Answer:** Functional component-এ খালি ডিপেন্ডেন্সি অ্যারেসহ `useEffect` Hook ব্যবহার করা হয়: `useEffect(() => {}, [])`।
* **Question:** How many times does `componentDidMount` run during a component's lifecycle?
  * **Answer:** এটি একটি কম্পোনেন্টের পুরো লাইফটাইমে বা প্রতিবার ব্রাউজারে মাউন্ট হওয়ার পর মাত্র একবারই (exactly once) রান হয়।

---

### ১১. Best practices
* যে কোনো External API requests, Web sockets কানেকশন, এবং Event listeners এড করার কাজ এখানেই করুন।
* থার্ড-পার্টি লাইব্রেরি (যেমন- Chart.js, D3.js) যা DOM এর ওপর সরাসরি কাজ করে, সেগুলোর ইনিশিয়ালাইজেশন এখানে করুন।
* কোড ক্লিন রাখার জন্য সরাসরি `componentDidMount`-এ পুরো ফেচ লজিক না লিখে আলাদা মেথড বানিয়ে তা কল করুন।

---

### ১২. Performance considerations (if applicable)
* `componentDidMount` এ `setState` করলে এক্সট্রা রি-রেন্ডার হয়। তাই সম্ভব হলে ইনিশিয়াল স্টেট সরাসরি constructor-এই ডিফাইন করে দেওয়া ভালো, যাতে এখানে এসে আবার স্টেট চেঞ্জ করতে না হয়।
* বড় আকারের এপিআই কল করার ক্ষেত্রে ইউজারকে যেন স্ক্রিনে লোডার বা কঙ্কাল (Skeleton) স্ক্রিন দেখানো হয়, তা নিশ্চিত করুন।

---

### ১৩. When NOT to use it
* যদি কম্পোনেন্টের কোনো ডেটা ব্রাউজার রেন্ডারের সাথে সাথে দেখানোর প্রয়োজন না থাকে, কিংবা এটি যদি একটি পিওর প্রেজেন্টেশনাল (Stateless/Presentational) কম্পোনেন্ট হয়, তবে এটি ব্যবহার করবেন না।
* লোকাল ভেরিয়েবল বা প্রপ্স থেকে প্রাপ্ত ডাটা ক্যালকুলেট করার জন্য এটি ব্যবহার করবেন না; এই কাজগুলো সরাসরি `render()` বা `constructor` মেথডে করা যায়।

---

### ১৪. Comparison with similar concepts
* **`constructor` vs `componentDidMount`**: Constructor চলে কম্পোনেন্ট তৈরি হওয়ার সময় (DOM-এ যাওয়ার আগে), আর `componentDidMount` চলে কম্পোনেন্ট DOM-এ সেট হওয়ার পর।
* **`componentDidUpdate` vs `componentDidMount`**: `componentDidMount` শুধু প্রথম মাউন্টের পর একবারই চলে। `componentDidUpdate` প্রতিবার State/Props চেঞ্জের পর চলে।

---

### ১৫. Summary in simple Bangla
`componentDidMount` হলো একটি দরকারী ফাংশন যা কম্পোনেন্টটি স্ক্রিনে প্রথমবার দেখানোর সাথে সাথেই কাজ করে। আমরা যখন প্রজেক্টে এপিআই থেকে ডেটা আনতে চাই, উইন্ডোর সাইজ ট্র্যাকিংয়ের জন্য লিসেনার বসাতে চাই কিংবা স্ক্রিন লোড হওয়ার সাথে সাথে ইনপুট ফিল্ড ফোকাস করতে চাই, তখন এই মেথডটি ব্যবহার করি।

---

### ১৬. 5 MCQ questions
1. `componentDidMount` মেথডটি লাইফসাইকেলের কোন ফেজে রান হয়?
   * A) Updating Phase
   * B) Unmounting Phase
   * C) Mounting Phase
   * D) Error Handling Phase
   * **Correct Answer: C**
2. একটি কম্পোনেন্ট প্রথমবার রেন্ডার ও মাউন্ট হওয়ার পর `componentDidMount` কতবার রান হয়?
   * A) ১ বার
   * B) ২ বার
   * C) প্রতিবার স্টেট পরিবর্তনের পর
   * D) মোটেই রান হয় না
   * **Correct Answer: A**
3. সার্ভার সাইড রেন্ডারিং (SSR)-এ নিচের কোন মেথডটি রান হয় না?
   * A) `constructor`
   * B) `render`
   * C) `componentDidMount`
   * D) `getDerivedStateFromProps`
   * **Correct Answer: C**
4. `componentDidMount` এর ভেতর `setState` কল করলে কী ঘটে?
   * A) এরর দেখায়
   * B) অতিরিক্ত রি-রেন্ডার হয়
   * C) কম্পোনেন্ট ক্র্যাশ করে
   * D) মাউন্টিং বন্ধ হয়ে যায়
   * **Correct Answer: B**
5. `componentDidMount`-এর সমতুল্য React Hook কোনটি?
   * A) `useState`
   * B) `useEffect(() => {}, [])`
   * C) `useMemo`
   * D) `useCallback`
   * **Correct Answer: B**

---

### ১৭. 5 Coding exercises
1. একটি ক্লাস কম্পোনেন্ট লিখুন যা মাউন্ট হওয়ার পর ব্রাউজারের উইন্ডো সাইজ ট্র্যাক করার জন্য একটি event listener যুক্ত করবে এবং স্ক্রিনে উইন্ডোর উইডথ (width) দেখাবে।
2. এমন একটি প্রোফাইল কার্ড কম্পোনেন্ট তৈরি করুন যা মাউন্ট হওয়ার সাথে সাথে `componentDidMount` থেকে গিটহাব এপিআই (GitHub API) কল করে আপনার গিটহাব ইউজারনেম এবং ফলোয়ার সংখ্যা দেখাবে।
3. একটি ইমেজ গ্যালারি কম্পোনেন্ট তৈরি করুন যা মাউন্ট হওয়ার পর একটি র্যান্ডম ইমেজ এপিআই থেকে ছবি লোড করে স্ক্রিনে রেন্ডার করবে।
4. একটি কাউন্টডাউন টাইমার তৈরি করুন যা মাউন্ট হওয়ার পর ৫ থেকে গণনা শুরু করে ০ তে এসে শেষ হবে।
5. একটি কম্পোনেন্ট তৈরি করুন যা মাউন্ট হওয়ার ৩ সেকেন্ড পর একটি মেসেজ স্ক্রিনে দেখাবে (Hint: `setTimeout` ব্যবহার করুন `componentDidMount`-এ)।

---
---

## Topic 3: Why do we use componentWillUnmount? Show with example.

### ১. Simple definition (বাংলায়)
`componentWillUnmount()` হলো React-এর একটি লাইফসাইকেল মেথড যা কোনো Component-কে DOM থেকে সম্পূর্ণভাবে রিমুভ বা ধ্বংস (destroy) করে দেওয়ার ঠিক আগে স্বয়ংক্রিয়ভাবে একবারের জন্য কল হয়। এই মেথডটি মূলত মেমোরি ক্লিনআপ বা বিভিন্ন রিসোর্স খালি করার জন্য ব্যবহৃত হয়।

---

### ২. Why this concept exists
একটি সিঙ্গেল পেজ অ্যাপ্লিকেশন (SPA) বা রিঅ্যাক্ট অ্যাপে ব্যবহারকারী যখন এক পেজ থেকে অন্য পেজে যান বা কোনো কম্পোনেন্টকে স্ক্রিন থেকে হাইড করেন, তখন সেই কম্পোনেন্টটি আর মেমোরিতে রাখার প্রয়োজন থাকে না। কিন্তু কম্পোনেন্টটি মাউন্ট থাকার সময় যদি কোনো Event Listener, WebSocket Connection বা `setInterval` চালু করা হয়ে থাকে, তবে কম্পোনেন্টটি স্ক্রিন থেকে চলে গেলেও ওই ব্যাকগ্রাউন্ড প্রসেসগুলো মেমোরিতে চালু থেকে যায়। এগুলোকে বন্ধ করার জন্যই `componentWillUnmount` মেথডটি দরকার।

---

### ৩. What problem it solves
* **মেমোরি লিক (Memory Leak) রোধ করা:** ব্যাকগ্রাউন্ডে চলতে থাকা অপ্রয়োজনীয় প্রসেসগুলোকে বন্ধ করে র‍্যাম (RAM) এবং সিপিইউ (CPU)-এর ওপর অতিরিক্ত চাপ পড়া থেকে অ্যাপ্লিকেশনকে বাঁচায়।
* **অনাকাঙ্ক্ষিত স্টেট আপডেট এরর রোধ করা:** একটি কম্পোনেন্ট আনমাউন্ট হয়ে যাওয়ার পর যদি কোনো এপিআই কল বা টাইমার স্টেট আপডেট (`setState`) করতে চেষ্টা করে, তখন রিঅ্যাক্ট কনসোলে একটি ওয়ার্নিং দেয়: *"Can't perform a React state update on an unmounted component..."*। `componentWillUnmount` এই এরর দূর করে।

---

### ৪. Real-life analogy
ধরুন, আপনি একটি লাইব্রেরি থেকে একটি বই পড়ার জন্য টেবিলে বাতি (Lamp) জ্বালিয়ে বসেছেন। পড়া শেষ করে যখন আপনি লাইব্রেরি ছেড়ে চলে যাবেন, তখন নিয়ম হলো বাতিটি নিভিয়ে যাওয়া এবং বইটি যথাস্থানে ফেরত দেওয়া। আপনি যদি লাইব্রেরি ত্যাগ করার সময় বাতি জ্বালিয়ে রেখে যান, তবে বিদ্যুৎ অপচয় হবে। এখানে লাইব্রেরি ছেড়ে চলে যাওয়ার আগের মুহূর্তটি হলো `componentWillUnmount` এবং বাতি নেভানো হলো ক্লিনআপ প্রসেস।

---

### ৫. How React works internally regarding this concept
React যখন দেখে যে একটি Component আর ব্রাউজারের DOM ট্রিতে থাকবে না (যেমন কন্ডিশনাল রেন্ডারিং বা রাউটিং চেঞ্জের কারণে), তখন React সরাসরি DOM থেকে এলিমেন্টগুলো মুছে ফেলার প্রস্তুতি নেয়। এলিমেন্টগুলো রিমুভ করার ঠিক পূর্ববর্তী ধাপে, React তার ইন্টারনাল ফাইবার নোড (Fiber node) থেকে ওই Component-এর instance-এর আন্ডারে থাকা `componentWillUnmount` মেথডটি রান করায়। এই মেথডের সব কোড রান শেষ হলে React DOM থেকে কম্পোনেন্টটিকে ডিলিট করে দেয়।

---

### ৬. Basic example
Here is a complete example showing a child component that runs a timer and cleans it up inside `componentWillUnmount` when the parent toggles it:

```javascript
import React, { Component } from 'react';

// Child Component that displays a timer
class TimerComponent extends Component {
  constructor(props) {
    super(props);
    this.state = { time: 0 };
    this.timerId = null;
  }

  componentDidMount() {
    console.log('Timer mounted. Starting interval...');
    // Start interval timer
    this.timerId = setInterval(() => {
      this.setState(prevState => ({ time: prevState.time + 1 }));
    }, 1000);
  }

  componentWillUnmount() {
    console.log('Timer will unmount. Clearing interval...');
    // Crucial step: clearing the interval to prevent memory leak
    clearInterval(this.timerId);
  }

  render() {
    return (
      <div style={{ background: '#f0f0f0', padding: '15px', margin: '10px 0' }}>
        <h4>Timer: {this.state.time} seconds</h4>
      </div>
    );
  }
}

// Parent Component toggling the Child Component
class ParentApp extends Component {
  state = { showTimer: true };

  toggleTimer = () => {
    this.setState(prevState => ({ showTimer: !prevState.showTimer }));
  };

  render() {
    return (
      <div style={{ padding: '20px' }}>
        <button onClick={this.toggleTimer}>
          {this.state.showTimer ? 'Hide Timer' : 'Show Timer'}
        </button>
        {this.state.showTimer && <TimerComponent />}
      </div>
    );
  }
}

export default ParentApp;
```

---

### ৭. Step-by-step explanation of the code
1. `ParentApp` এর একটি স্টেট `showTimer` রয়েছে যা ডিফল্টভাবে `true` থাকে। এর ফলে স্ক্রিনে `TimerComponent` রেন্ডার হয়।
2. `TimerComponent` যখন মাউন্ট হয়, তখন তার `componentDidMount` মেথড রান করে এবং ১ সেকেন্ড পর পর স্টেট পরিবর্তনের জন্য একটি `setInterval` সেট করে, যার আইডিটি `this.timerId`-তে স্টোর করা হয়।
3. যখন ব্যবহারকারী "Hide Timer" বাটনে ক্লিক করেন, তখন `ParentApp` এর স্টেট পরিবর্তিত হয়ে `showTimer: false` হয়।
4. কন্ডিশনাল রেন্ডারিংয়ের কারণে React তখন `TimerComponent` কে DOM থেকে সরাতে উদ্যত হয়।
5. সরানোর ঠিক আগ মুহূর্তে `TimerComponent`-এর `componentWillUnmount` মেথডটি স্বয়ংক্রিয়ভাবে কল হয়।
6. এই মেথডের ভেতর `clearInterval(this.timerId)` মেথডটি রান হয়ে ব্যাকগ্রাউন্ডে চলতে থাকা টাইমারটি চিরতরে স্টপ করে দেয়। এর ফলে কোনো মেমোরি লিক ঘটে না।

---

### ৮. Another real-world example
Let's see an example where we track mouse movements globally and remove the event listener when the component is unmounted:

```javascript
import React, { Component } from 'react';

class MouseTracker extends Component {
  constructor(props) {
    super(props);
    this.state = { x: 0, y: 0 };
  }

  componentDidMount() {
    console.log('Adding global mousemove listener');
    window.addEventListener('mousemove', this.handleMouseMove);
  }

  componentWillUnmount() {
    console.log('Removing global mousemove listener');
    // Removing listener prevents it from running after component is destroyed
    window.removeEventListener('mousemove', this.handleMouseMove);
  }

  handleMouseMove = (event) => {
    this.setState({ x: event.clientX, y: event.clientY });
  };

  render() {
    return (
      <div style={{ border: '2px dashed blue', padding: '20px', marginTop: '10px' }}>
        <h4>Mouse Position:</h4>
        <p>X: {this.state.x}, Y: {this.state.y}</p>
      </div>
    );
  }
}

class TrackerContainer extends Component {
  state = { active: true };

  render() {
    return (
      <div style={{ padding: '20px' }}>
        <button onClick={() => this.setState({ active: !this.state.active })}>
          Toggle Mouse Tracker
        </button>
        {this.state.active ? <MouseTracker /> : <p>Tracker is inactive.</p>}
      </div>
    );
  }
}

export default TrackerContainer;
```

---

### ৯. Common mistakes beginners make
* **ক্লিনআপ করতে ভুলে যাওয়া:** অনেকেই ইভেন্ট লিসেনার কিংবা `setInterval` তৈরি করেন কিন্তু `componentWillUnmount` মেথডটি তৈরিই করেন না। এর ফলে ব্রাউজারের মেমোরি ক্র্যাশ করতে পারে।
* **`componentWillUnmount`-এ `setState()` কল করা:** এটি একটি বড় ভুল। যেহেতু কম্পোনেন্টটি চিরতরে মুছে যাচ্ছে, তাই এখানে নতুন করে স্টেট আপডেট করার কোনো যৌক্তিকতা নেই এবং এটি করলে রিঅ্যাক্ট এরর থ্রো করবে।
* **ভুল ফাংশন রেফারেন্স দিয়ে Listener রিমুভ করা:** `addEventListener`-এ যে ফাংশনটি পাস করা হয়েছে, ঠিক সেই একই ফাংশন রেফারেন্সই `removeEventListener`-এ পাস করতে হবে। অ্যানোনিমাস ফাংশন ব্যবহার করলে তা রিমুভ হবে না।

---

### ১০. Interview questions related to this topic
* **Question:** What is the primary purpose of `componentWillUnmount`?
  * **Answer:** এর মূল কাজ হলো রিসোর্স ক্লিনআপ করা। যেমন: `clearTimeout`, `clearInterval`, event listeners রিমুভ করা, এবং অ্যাক্টিভ WebSocket বা API requests ক্যান্সেল করা।
* **Question:** Can we call `setState` in `componentWillUnmount`? Why or why not?
  * **Answer:** না, এখানে `setState` কল করা যাবে না। কারণ কম্পোনেন্টটি স্ক্রিন থেকে চলে যাচ্ছে, তাই এটি আর কখনো রি-রেন্ডার হবে না।
* **Question:** What happens if we do not clean up global event listeners in `componentWillUnmount`?
  * **Answer:** ইভেন্ট লিসেনারটি ব্যাকগ্রাউন্ডে চলতে থাকবে এবং মেমোরিতে থেকে যাবে। একেই মেমোরি লিক (Memory Leak) বলে। এটি অ্যাপ্লিকেশনের স্পিড কমিয়ে দেয় এবং ব্রাউজারকে স্লো করে ফেলে।
* **Question:** How do you cancel an API request in `componentWillUnmount`?
  * **Answer:** আমরা JavaScript-এর `AbortController` ব্যবহার করে Fetch API রিকোয়েস্ট বাতিল করতে পারি অথবা Axios ব্যবহার করলে Axios-এর CancelToken ব্যবহার করতে পারি।
* **Question:** What is the equivalent of `componentWillUnmount` in React Hooks?
  * **Answer:** Functional components-এ `useEffect` এর ভেতর থেকে একটি ক্লিনআপ ফাংশন রিটার্ন করতে হয়: `useEffect(() => { return () => { /* cleanup */ } }, [])`।

---

### ১১. Best practices
* `componentDidMount`-এ যে যে সার্ভিস চালু করবেন, তার প্রতিটি `componentWillUnmount`-এ বন্ধ করার নিশ্চয়তা রাখুন।
* ইভেন্ট হ্যান্ডলারগুলোকে মেম্বার মেথড (যেমন `this.handleResize`) হিসেবে ডিফাইন করুন যাতে খুব সহজে রিমুভ করা যায়।
* ক্লিনআপ লজিকগুলো অত্যন্ত সহজ ও পরিষ্কার রাখুন।

---

### ১২. Performance considerations (if applicable)
* সঠিক সময়ে ক্লিনআপ না করলে ব্রাউজারের র‍্যাম ও সিপিইউ ইউসেজ ক্রমাগত বাড়তে থাকে, যার ফলে মোবাইল বা কম পাওয়ারের ডিভাইসে অ্যাপ্লিকেশন হ্যাং করতে পারে।

---

### ১৩. When NOT to use it
* যদি আপনার কম্পোনেন্টে কোনো গ্লোবাল ইভেন্ট লিসেনার, টাইমার, রিকোয়েস্ট বা অন্য কোনো ব্যাকগ্রাউন্ড কানেকশন না থাকে, তবে এই মেথড লেখার কোনো প্রয়োজন নেই।

---

### ১৪. Comparison with similar concepts
* **`componentWillUnmount` vs `useEffect` Cleanup**: প্রথমটি ক্লাস কম্পোনেন্টে ব্যবহৃত হয় যা অবজেক্ট ওরিয়েন্টেড স্টাইলে চলে। দ্বিতীয়টি ফাংশনাল কম্পোনেন্টে ব্যবহৃত হয় যা ক্লোজার (Closure) মেকানিজম মেনে চলে।

---

### ১৫. Summary in simple Bangla
`componentWillUnmount` হলো রিঅ্যাক্টের একটি ক্লিনআপ মেথড। কম্পোনেন্ট স্ক্রিন থেকে চলে যাওয়ার আগে এটি কল হয়। এর কাজ হলো রুমে তালা দেওয়ার আগে বাতি নিভিয়ে যাওয়ার মতো—যাতে কোনো অপ্রয়োজনীয় টাইমার বা লিসেনার ব্যাকগ্রাউন্ডে চালু থেকে ব্রাউজার মেমোরি নষ্ট না করে।

---

### ১৬. 5 MCQ questions
1. `componentWillUnmount` কখন কল হয়?
   * A) কম্পোনেন্ট মাউন্ট হওয়ার ঠিক পর
   * B) স্টেট আপডেট হওয়ার ঠিক পর
   * C) কম্পোনেন্ট DOM থেকে রিমুভ হওয়ার ঠিক পূর্বে
   * D) রি-রেন্ডার হওয়ার পর
   * **Correct Answer: C**
2. নিচের কোন কাজটি `componentWillUnmount`-এ করা নিষিদ্ধ?
   * A) `clearInterval`
   * B) `setState`
   * C) `removeEventListener`
   * D) Console log
   * **Correct Answer: B**
3. মেমোরি লিক (Memory Leak) এড়াতে আমাদের কী করা উচিত?
   * A) প্রতিবার রি-রেন্ডার করা
   * B) `componentWillUnmount` এ টাইমার এবং লিসেনার বন্ধ করা
   * C) স্টেট পরিবর্তন না করা
   * D) কম্পোনেন্ট ডিলিট না করা
   * **Correct Answer: B**
4. `useEffect` এর মাধ্যমে আনমাউন্টিং হ্যান্ডেল করতে হলে কী করতে হয়?
   * A) ডিপেন্ডেন্সি অ্যারেতে স্টেট রাখা
   * B) `useEffect` এর ভেতর থেকে একটি ফাংশন রিটার্ন করা
   * C) `useEffect` এর বাইরে কোড লেখা
   * D) `useState` ব্যবহার করা
   * **Correct Answer: B**
5. `componentWillUnmount` লাইফসাইকেলে মোট কতবার কল হয়?
   * A) প্রতি সেকেন্ডে একবার
   * B) প্রতিবার স্টেট পরিবর্তনের পর
   * C) সর্বাধিক একবার (কম্পোনেন্ট ধ্বংসের পূর্বে)
   * D) আনলিমিটেড বার
   * **Correct Answer: C**

---

### ১৭. 5 Coding exercises
1. একটি ক্লাস কম্পোনেন্ট লিখুন যা মাউন্ট হওয়ার পর ১ সেকেন্ড পর পর একটি করে শব্দ (beep sound) বাজাবে এবং আনমাউন্ট হওয়ার সময় অডিও প্লেয়ারটি বন্ধ ও মেমোরি থেকে ডিলিট করবে।
2. একটি চ্যাট উইন্ডো কম্পোনেন্ট লিখুন যা মাউন্ট হওয়ার সময় একটি WebSocket কানেকশন ওপেন করে এবং আনমাউন্ট হওয়ার সময় কানেকশনটি ক্লোজ করে।
3. এমন একটি ক্লাস কম্পোনেন্ট তৈরি করুন যা উইন্ডো স্ক্রল (scroll) ইভেন্ট ট্র্যাক করবে এবং আনমাউন্ট করার সময় লিসেনারটি রিমুভ করবে।
4. একটি স্লাইডশো কম্পোনেন্ট তৈরি করুন যেখানে প্রতি ৩ সেকেন্ড পর পর ছবি চেঞ্জ হবে এবং কম্পোনেন্ট আনমাউন্ট হওয়ার সময় টাইমারটি বন্ধ হবে।
5. একটি বাটন টগল ইন্টারফেস তৈরি করুন যা একটি সাইডবার শো/হাইড করবে। সাইডবার যখন হাইড হবে, তার আনমাউন্ট প্রসেসে কনসোলে একটি গুডবাই মেসেজ প্রিন্ট হতে হবে।

---
---

## Topic 4: Why do we use super(props) in constructor?

### ১. Simple definition (বাংলায়)
জাভাস্ক্রিপ্টের ক্লাস ইনহেরিটেন্সের (Class Inheritance) নিয়ম অনুযায়ী, একটি চাইল্ড ক্লাসে `constructor` ডিফাইন করলে তার প্যারেন্ট ক্লাসের `constructor`-কে কল করতে হয়, আর এই কাজের জন্য `super()` ব্যবহার করা হয়। React-এ `super(props)` ব্যবহার করার মূল কারণ হলো, প্যারেন্ট ক্লাস `React.Component` এর কনস্ট্রাক্টরকে কল করা এবং চাইল্ড কম্পোনেন্টের ভেতর `this.props` কে সঠিকভাবে কাজ করার সুযোগ দেওয়া।

---

### ২. Why this concept exists
React-এর Class Component মূলত ES6-এর Class এবং Inheritance মেকানিজম মেনে চলে। যখন আমরা `class MyComponent extends Component` লিখি, তখন `MyComponent` হলো একটি চাইল্ড ক্লাস এবং `React.Component` হলো প্যারেন্ট ক্লাস। জাভাস্ক্রিপ্ট অনুযায়ী, যতক্ষণ না চাইল্ড ক্লাসের কনস্ট্রাক্টর `super()` কল করছে, ততক্ষণ পর্যন্ত চাইল্ড ক্লাসে `this` কিওয়ার্ডটি তৈরিই হয় না। তাই `this` ব্যবহার করার আগে `super()` কল করা বাধ্যতামূলক। আর প্রপস পাস করতে `super(props)` ব্যবহার করতে হয়।

---

### ৩. What problem it solves
* **`this` এরর হ্যান্ডেল করা:** কনস্ট্রাক্টরের ভেতর `super()` কল না করে যদি আমরা `this.state` বা অন্য কিছু লিখতে যাই, তবে জাভাস্ক্রিপ্ট একটি ReferenceError দিবে: *"this is not defined"*।
* **কনস্ট্রাক্টরের ভেতর `this.props` অ্যাক্সেস করা:** যদি আমরা শুধু `super()` কল করি (প্রপস ছাড়া), তবে কনস্ট্রাক্টরের ভেতর `this.props` এর মান `undefined` আসবে। `super(props)` পাঠালে কনস্ট্রাক্টরের ভেতরেও `this.props` সরাসরি ব্যবহার করা যায়।

---

### ৪. Real-life analogy
ধরুন, আপনি আপনার বাবার একটি কোম্পানি বা ব্যবসার উত্তরাধিকারী (Inheritor) হলেন। আপনি নিজের মতো ব্যবসা পরিচালনা (Child Class) করার আগে আপনার বাবার তৈরি করা কোম্পানির মূল নিয়ম ও লাইসেন্স (Parent Class constructor) সই করতে হবে। এই সই করার প্রক্রিয়াটি হলো `super()`। আর বাবার দেওয়া মূল মূলধন বা শর্তগুলো সাথে নিয়ে কাজ শুরু করা হলো `super(props)`।

---

### ৫. How React works internally regarding this concept
React যখন কোনো ক্লাস কম্পোনেন্টকে রেন্ডার করতে যায়, তখন সেটির অবজেক্ট বা ইনস্ট্যান্স তৈরি করতে `new MyComponent(props)` কল করে।
জাভাস্ক্রিপ্ট ব্যাকগ্রাউন্ডে চাইল্ড ক্লাসের `constructor(props)` রান করে। সেখানে যখন `super(props)` কল করা হয়, তখন প্যারেন্ট ক্লাস `React.Component` এর কনস্ট্রাক্টর এক্সিকিউট হয়। প্যারেন্ট ক্লাসের কনস্ট্রাক্টর তখন এই কোডটি রান করে:
```javascript
this.props = props;
```
এর ফলেই চাইল্ড কম্পোনেন্টটি তার নিজস্ব স্কোপে `this.props` এর অ্যাক্সেস পায়।

---

### ৬. Basic example
Here is a basic example illustrating why `super(props)` is necessary if we want to use `this.props` inside the constructor:

```javascript
import React, { Component } from 'react';

class WelcomeCard extends Component {
  constructor(props) {
    // Calling the parent class constructor with props
    super(props);

    // Initializing state using props, which requires super(props)
    this.state = {
      formattedName: props.username.toUpperCase(),
      message: `Welcome, ${this.props.username}!` // Safe to use this.props here
    };

    console.log('Props inside constructor:', this.props);
  }

  render() {
    return (
      <div style={{ border: '1px solid black', padding: '10px' }}>
        <h2>{this.state.message}</h2>
        <p>Formatted Name: {this.state.formattedName}</p>
      </div>
    );
  }
}

export default WelcomeCard;
```

---

### ৭. Step-by-step explanation of the code
1. `WelcomeCard` নামক চাইল্ড ক্লাসটি `Component` প্যারেন্ট ক্লাসকে এক্সটেন্ড করে।
2. এর কনস্ট্রাক্টর প্রপস রিসিভ করে: `constructor(props)`.
3. কনস্ট্রাক্টরের একদম প্রথম লাইনেই `super(props)` কল করা হয়েছে। এর মাধ্যমে প্যারেন্ট ক্লাসের কনস্ট্রাক্টর কল হয়েছে এবং প্রপস প্যারেন্টে পাস হয়েছে।
4. এর ফলে কনস্ট্রাক্টরের ভেতর `this.props` সফলভাবে ডিফাইন হয়েছে।
5. স্টেট ইনিশিয়ালাইজ করার সময় আমরা সরাসরি `props.username` অথবা `this.props.username` ব্যবহার করতে পেরেছি কোনো এরর ছাড়াই।
6. যদি আমরা শুধু `super()` কল করতাম (ভিতরে `props` না দিয়ে), তবে `this.props.username` লাইনটিতে এরর আসত কারণ `this.props` তখন `undefined` থাকতো।

---

### ৮. Another real-world example
Let's see what happens if we only use `super()` instead of `super(props)` and try to log props in the constructor:

```javascript
import React, { Component } from 'react';

class BadExample extends Component {
  constructor(props) {
    super(); // Notice props is missing here!

    // This will work: props parameter is local to constructor
    console.log('Local props:', props);

    // This will print undefined because super() did not initialize this.props!
    console.log('this.props inside constructor:', this.props); 
  }

  render() {
    // Interestingly, React automatically sets this.props AFTER the constructor finishes!
    // So this.props WILL work in render() even if we called super() without props.
    return (
      <div>
        <h3>User: {this.props.name}</h3>
      </div>
    );
  }
}

export default BadExample;
```

---

### ৯. Common mistakes beginners make
* **`super()` এর আগে `this` ব্যবহার করা:** কনস্ট্রাক্টরের প্রথম লাইনে `super()` লেখার আগেই অনেকে `this.state = {}` লিখে ফেলেন। জাভাস্ক্রিপ্ট এটি মোটেও অ্যালাউ করে না।
* **`super` কল না করে শুধু কনস্ট্রাক্টর লেখা:** এটি সরাসরি জাভাস্ক্রিপ্ট ReferenceError তৈরি করবে।
* **ভুলে `super()` ব্র্যাকেটে `props` না দেওয়া এবং পরে কনস্ট্রাক্টরে `this.props` ব্যবহার করা:** এর ফলে `undefined` রিলেটেড বাগ (bugs) তৈরি হয় যা ট্র্যাক করা কঠিন।

---

### ১০. Interview questions related to this topic
* **Question:** What is the difference between `super()` and `super(props)`?
  * **Answer:** `super()` প্যারেন্ট ক্লাসের কনস্ট্রাক্টর কল করে এবং `this` কে সচল করে, কিন্তু কনস্ট্রাক্টরের ভেতরে `this.props` কে `undefined` রাখে। আর `super(props)` প্যারেন্ট ক্লাসের কাছে প্রপস পাস করে দেয়, ফলে কনস্ট্রাক্টরের ভেতরেও `this.props` অ্যাক্সেস করা সম্ভব হয়।
* **Question:** What happens if we define a constructor without calling `super()`?
  * **Answer:** জাভাস্ক্রিপ্ট একটি ReferenceError দিবে কারণ সাব-ক্লাসের কনস্ট্রাক্টরে `super()` কল করা বাধ্যতামূলক।
* **Question:** Does `this.props` work in `render()` if we only called `super()` without props in the constructor?
  * **Answer:** হ্যাঁ, কাজ করবে। কনস্ট্রাক্টর রান হওয়ার পর এবং `render` রান হওয়ার আগে React নিজে থেকেই চাইল্ড ইনস্ট্যান্সে প্রপস অ্যাসাইন করে দেয়। কিন্তু কনস্ট্রাক্টরের ভেতরে তা কাজ করবে না।
* **Question:** Do we need to write constructor and `super(props)` in every class component?
  * **Answer:** না। যদি আপনার স্টেট ইনিশিয়ালাইজ করার বা মেথড বাইন্ড করার প্রয়োজন না থাকে, তবে কনস্ট্রাক্টর লেখারই কোনো দরকার নেই। React ডিফল্ট কনস্ট্রাক্টর দিয়ে নিজেই এটি হ্যান্ডেল করে।
* **Question:** Can we use arrow functions to avoid binding in the constructor?
  * **Answer:** হ্যাঁ, ক্লাস মেথডগুলোকে অ্যারো ফাংশন (Arrow Functions) হিসেবে লিখলে কনস্ট্রাক্টরের ভেতর আলাদাভাবে `bind` করার ঝামেলা এড়ানো যায়।

---

### ১১. Best practices
* ক্লাস কম্পোনেন্টে কনস্ট্রাক্টর ডিফাইন করলে সবসময় চোখ বন্ধ করে `super(props)` ব্যবহার করুন।
* আধুনিক জাভাস্ক্রিপ্ট সিনট্যাক্স অনুযায়ী কনস্ট্রাক্টর ছাড়াই সরাসরি `state = {}` (Class Fields) ব্যবহার করুন, এতে কোড অনেক ছোট ও পরিষ্কার হয়।

---

### ১২. Performance considerations (if applicable)
* পারফরম্যান্সে এর কোনো বড় প্রভাব নেই, তবে কনস্ট্রাক্টর পরিহার করে ক্লাস ফিল্ড সিনট্যাক্স ব্যবহার করলে কোডের সাইজ সামান্য ছোট হয়।

---

### xiii. When NOT to use it
* যদি কম্পোনেন্টে কনস্ট্রাক্টর ব্যবহারের প্রয়োজন না থাকে, তবে শুধু শুধু কনস্ট্রাক্টর লিখে `super(props)` লিখবেন না।
* ফাংশনাল কম্পোনেন্ট (Functional Component)-এ কোনো ক্লাস বা কনস্ট্রাক্টর থাকে না, তাই সেখানে `super` ব্যবহারের প্রশ্নই আসে না।

---

### ১৪. Comparison with similar concepts
* **`super()` vs `super(props)`**:
  * `super()`: কনস্ট্রাক্টরে `this` তৈরি করে কিন্তু `this.props` ওয়ান-টাইম খালি রাখে।
  * `super(props)`: কনস্ট্রাক্টরে `this` তৈরি করে এবং `this.props` কে ভ্যালু দিয়ে সচল করে।

---

### ১৫. Summary in simple Bangla
`super(props)` হলো জাভাস্ক্রিপ্টের নিয়ম অনুযায়ী চাইল্ড ক্লাসের কনস্ট্রাক্টর থেকে প্যারেন্ট ক্লাসের কনস্ট্রাক্টরকে ডাকার উপায়। এটি ব্যবহার করলে আমরা কনস্ট্রাক্টরের ভেতরেও `this.props` ব্যবহার করার ক্ষমতা পাই এবং কম্পোনেন্টটি কোনো এরর ছাড়াই স্টেট তৈরি করতে পারে।

---

### ১৬. 5 MCQ questions
1. কনস্ট্রাক্টরের প্রথম লাইনে নিচের কোনটি অবশ্যই কল করতে হয়?
   * A) `this.state`
   * B) `super()` অথবা `super(props)`
   * C) `this.props`
   * D) `render()`
   * **Correct Answer: B**
2. কনস্ট্রাক্টরে `super()` এর আগে `this` ব্যবহার করলে কোন এররটি আসে?
   * A) TypeError
   * B) SyntaxError
   * C) ReferenceError
   * D) RangeError
   * **Correct Answer: C**
3. যদি আমরা কনস্ট্রাক্টরে শুধু `super()` কল করি (প্রপস ছাড়া), তবে কনস্ট্রাক্টরের ভেতর `this.props` এর মান কী হবে?
   * A) Null
   * B) Empty Object `{}`
   * C) Undefined
   * D) Error
   * **Correct Answer: C**
4. চাইল্ড ক্লাসে প্যারেন্ট ক্লাসের মেথড ও কনস্ট্রাক্টর কল করার জন্য জাভাস্ক্রিপ্টের কোন কিওয়ার্ডটি ব্যবহৃত হয়?
   * A) `parent`
   * B) `this`
   * C) `super`
   * D) `extends`
   * **Correct Answer: C**
5. `super(props)` ব্যবহারের মূল উদ্দেশ্য কী?
   * A) কনস্ট্রাক্টরের ভেতর `this.props` সঠিকভাবে ব্যবহার করা
   * B) কম্পোনেন্ট মাউন্ট করা
   * C) স্টেট ডিলিট করা
   * D) রি-রেন্ডার কমানো
   * **Correct Answer: A**

---

### ১৭. 5 Coding exercises
1. এমন একটি ক্লাস কম্পোনেন্ট লিখুন যা `super(props)` ব্যবহার করে এবং প্রপস থেকে আসা একটি সংখ্যা দ্বিগুণ করে কনস্ট্রাক্টরের ভেতর স্টেট ইনিশিয়ালাইজ করবে।
2. একটি ক্লাস কম্পোনেন্ট লিখুন যা কনস্ট্রাক্টরের ভেতর `this.props` ব্যবহার করে মেম্বারদের ইমেইল ভ্যালিডেশন করে একটি `isValidEmail` স্টেট রাখবে।
3. এমন একটি ক্লাস কম্পোনেন্ট ডিজাইন করুন যা প্রপস হিসেবে `theme` (dark/light) রিসিভ করে এবং কনস্ট্রাক্টরের ভেতর প্রপসের ভ্যালু অনুযায়ী বডি ব্যাকগ্রাউন্ডের জন্য ইনিশিয়াল স্টেট সেট করে।
4. একটি কম্পোনেন্ট লিখুন যেখানে কোনো কনস্ট্রাক্টর ব্যবহার করা হবে না (Class Fields syntax ব্যবহার করে স্টেট ডিফাইন করুন) এবং এটি সঠিকভাবে রেন্ডার করবে।
5. একটি চাইল্ড ক্লাস ও প্যারেন্ট ক্লাস তৈরি করে সাধারণ জাভাস্ক্রিপ্ট কোড লিখুন (React ছাড়া) যেখানে `super()` ব্যবহার না করার কারণে এরর শো করবে এবং `super()` যোগ করার পর তা ঠিক হবে।
