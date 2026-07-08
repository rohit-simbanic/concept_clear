# Redux Toolkit Architecture & Concepts Masterclass

---

## Topic 1: What is the architecture of Redux Toolkit? (Store, Slices, Selectors, Middleware)

### 1. Simple Definition (বাংলায়)
রেডাক্স টুলকিট (Redux Toolkit বা RTK) হলো একটি আর্কিটেকচারাল প্যাটার্ন ও লাইব্রেরি যা অ্যাপ্লিকেশনের সমস্ত ডেটা বা স্টেটকে (State) একটি কেন্দ্রীয় ভাণ্ডারে জমা রাখে। এর মূল আর্কিটেকচার ৪টি প্রধান উপাদানের সমন্বয়ে গঠিত:
*   **Store**: অ্যাপের সমস্ত স্টেটের একক উৎস (Single Source of Truth)।
*   **Slices**: অ্যাপ্লিকেশনের বিভিন্ন ফিচারের ডেটা ও লজিকের ছোট ছোট স্বাধীন বিভাগ।
*   **Selectors**: স্টোর থেকে নির্দিষ্ট ডেটা খুঁজে বের করার জন্য ব্যবহৃত কুয়েরি ফাংশন।
*   **Middleware**: অ্যাকশন ডিসপ্যাচ হওয়া এবং রিডিউসারে পৌঁছানোর মাঝখানের প্রক্রিয়াজাতকরণ স্তর (যেমন- এপিআই কল বা লগিং)।

---

### 2. Why This Concept Exists
ঐতিহ্যগত বা ভ্যানিলা রেডাক্সে (Vanilla Redux) স্টোর সেটআপ করা, অ্যাকশন ও রিডিউসার আলাদা করা এবং ইমিউটেবিলিটি বজায় রাখা অত্যন্ত জটিল ছিল। প্রচুর পরিমাণে কোড (Boilerplate Code) লিখতে হতো, যা কোডের কার্যকারিতা কমিয়ে দিত এবং ডেভেলপারদের বিভ্রান্ত করত। Redux Toolkit আর্কিটেকচারটি তৈরি করা হয়েছে যাতে ডেভেলপাররা খুব কম কোড লিখে স্ট্যান্ডার্ড রেডাক্স আর্কিটেকচার অনুসরণ করতে পারেন এবং সহজে স্টেট ম্যানেজ করতে পারেন।

---

### 3. What Problem It Solves
*   **অতিরিক্ত বয়লারপ্লেট কোড (Boilerplate Code):** আলাদা করে অ্যাকশন ক্রিয়েটর ও অ্যাকশন টাইপস লেখার ঝামেলা দূর করে।
*   **জটিল কনফিগারেশন:** স্টোর কনফিগার করার প্রক্রিয়া সহজ করে (`configureStore` দিয়ে মিডলওয়্যার এবং রেডাক্স ডেভটুলস অটোমেটিক সেটআপ হয়ে যায়)।
*   **ইমিউটেবল আপডেট জটিলতা:** সরাসরি স্টেট পরিবর্তন করার ভয় দূর করে, কারণ এটি ইন্টারনালি Immer.js লাইব্রেরি ব্যবহার করে।
*   **অ্যাসিনক্রোনাস লজিক:** মিডলওয়্যার সেটআপ এবং অ্যাসিনক্রোনাস অ্যাকশন হ্যান্ডেল করার জটিলতা সমাধান করে।

---

### 4. Real-life Analogy
ধরা যাক একটি বিশাল সুপারশপের কথা:
*   **Store (সুপারশপের গোডাউন):** যেখানে দোকানের সব পণ্য একসাথে সংরক্ষিত থাকে।
*   **Slices (আলাদা ডিপার্টমেন্ট):** যেমন গ্রোসারি, ইলেকট্রনিক্স বা কসমেটিকস বিভাগ। প্রতিটি বিভাগের নিজস্ব পণ্য (State) এবং ক্যাশিয়ার (Reducer) থাকে।
*   **Selectors (পণ্য খুজে দেওয়ার কর্মী):** একজন সেলসম্যান যে আপনার অনুরোধ অনুযায়ী নির্দিষ্ট প্রোডাক্টটি গোডাউন থেকে এনে দেয়।
*   **Middleware (নিরাপত্তা ও যাচাইকরণ):** ক্যাশ কাউন্টারে টাকা জমা দেওয়ার আগে বারকোড স্ক্যানার এবং সিকিউরিটি চেক, যা নিশ্চিত করে লেনদেনটি সঠিক ও বৈধ।

---

### 5. How Redux/React Works Internally
Redux Toolkit-এর আর্কিটেকচার ব্যাকগ্রাউন্ডে রেডাক্সের মূল নীতিগুলো অনুসরণ করে কাজ করে:
1.  `configureStore` রান করার সময় এটি রেডাক্সের `createStore` কল করে এবং স্বয়ংক্রিয়ভাবে `redux-thunk` ও `Redux DevTools` মিডলওয়্যার যুক্ত করে।
2.  `createSlice` ব্যবহার করলে এটি ইন্টারনালি **Immer.js** লাইব্রেরি ব্যবহার করে একটি ড্রাফট স্টেট (Draft State) তৈরি করে। এর ফলে ডেভেলপাররা সরাসরি `state.value = 1` লিখতে পারেন। Immer এই পরিবর্তনগুলো ট্র্যাক করে একটি নতুন সম্পূর্ণ ইমিউটেবল অবজেক্ট রিটার্ন করে।
3.  যখন একটি অ্যাকশন ডিসপ্যাচ করা হয়, তখন এটি মিডলওয়্যার চেইনের মধ্য দিয়ে যায়। যদি কোনো মিডলওয়্যার একে না আটকায়, তবে এটি স্লাইসের রিডিউসারে পৌঁছায়।
4.  রিডিউসার স্টেট আপডেট করার পর, React-Redux এর `useSelector` এর মাধ্যমে রিঅ্যাক্ট কম্পোনেন্টকে নোটিফাই করা হয় এবং কম্পোনেন্টটি রি-রেন্ডার হয়।

---

### 6. Basic Example (English Code)
```javascript
import { configureStore, createSlice } from '@reduxjs/toolkit';

// 1. Slice Definition
const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value += 1; // Mutating code allowed by Immer
    },
    decrement: (state) => {
      state.value -= 1;
    }
  }
});

// Extracting Actions
export const { increment, decrement } = counterSlice.actions;

// 2. Selector Definition
export const selectCounterValue = (state) => state.counter.value;

// 3. Store Configuration
const store = configureStore({
  reducer: {
    counter: counterSlice.reducer
  }
});

export default store;
```

---

### 7. Step-by-step Explanation of the Code
*   `import { configureStore, createSlice }` এর মাধ্যমে আমরা প্রয়োজনীয় ফাংশনগুলো RTK থেকে ইমপোর্ট করেছি।
*   `createSlice` ফাংশনটির মাধ্যমে `counter` নামের একটি স্লাইস তৈরি করা হয়েছে। এর `initialState` হলো `{ value: 0 }`।
*   `reducers` অবজেক্টের ভেতরে `increment` এবং `decrement` ফাংশন দুটি স্টেটকে সরাসরি আপডেট করার কোড লেখে। Immer লাইব্রেরির মাধ্যমে এটি নিরাপদে নতুন ইমিউটেবল স্টেট তৈরি করে।
*   `counterSlice.actions` থেকে অ্যাকশন ক্রিয়েটরগুলোকে এক্সপোর্ট করা হয়েছে।
*   `selectCounterValue` নামক সিলেক্টরটি গ্লোবাল স্টেট থেকে শুধুমাত্র `counter` স্লাইসের `value` অংশটি রিটার্ন করে।
*   `configureStore` ফাংশনটি দিয়ে স্টোর তৈরি করে স্লাইসের রিডিউসারকে রেজিস্টার করা হয়েছে।

---

### 8. Another Real-world Example (English Code)
**Task Management Store Architecture:**
```javascript
import { configureStore, createSlice } from '@reduxjs/toolkit';

// Task Slice
const taskSlice = createSlice({
  name: 'tasks',
  initialState: { list: [], loading: false },
  reducers: {
    addTask: (state, action) => {
      state.list.push({ id: Date.now(), title: action.payload, completed: false });
    },
    toggleTask: (state, action) => {
      const task = state.list.find(t => t.id === action.payload);
      if (task) {
        task.completed = !task.completed;
      }
    }
  }
});

export const { addTask, toggleTask } = taskSlice.actions;

// Selector
export const selectAllTasks = (state) => state.tasks.list;
export const selectPendingTasksCount = (state) => state.tasks.list.filter(t => !t.completed).length;

// Store config
const store = configureStore({
  reducer: {
    tasks: taskSlice.reducer
  }
});

export default store;
```

---

### 9. Common Mistakes Beginners Make
*   **স্লাইসকে সরাসরি রিডিউসারের স্থানে পাস করা:** `configureStore` এ `reducer: { tasks: taskSlice }` লেখা ভুল। সঠিক হলো `reducer: { tasks: taskSlice.reducer }`।
*   **মিডলওয়্যার সেটআপের সময় ভুল:** কাস্টম মিডলওয়্যার অ্যাড করার সময় ডিফল্ট মিডলওয়্যারগুলো (`getDefaultMiddleware()`) ওভাররাইড বা মুছে ফেলা।
*   **অ্যাকশন ফাংশন কল না করা:** ডিসপ্যাচ করার সময় `dispatch(increment)` লেখা (সঠিক হলো `dispatch(increment())`)।

---

### 10. Interview Questions
1.  **Question:** What are the core pillars of Redux Toolkit architecture?
    *   **Answer:** The core pillars are the Store (global state container), Slices (modular logic), Selectors (data extractors), and Middleware (side-effects processor).
2.  **Question:** How does Redux Toolkit manage store configuration under the hood?
    *   **Answer:** It uses `configureStore` which wraps the standard Redux `createStore`, automatically sets up the Redux DevTools extension, and includes `redux-thunk` by default.
3.  **Question:** What is the role of Immer.js in Redux Toolkit architecture?
    *   **Answer:** Immer.js acts as an intermediary that allows developers to write mutating state update logic (e.g., `state.push`), which it safely translates into immutable state updates.
4.  **Question:** How do Selectors optimize React component performance in RTK?
    *   **Answer:** Selectors allow components to extract only the specific data they need. In combination with libraries like Reselect, they cache results and prevent unnecessary re-renders.
5.  **Question:** What happens if we bypass RTK architecture rules and mutate the state directly outside reducers?
    *   **Answer:** React will not detect the state change, the component subscription won't trigger re-renders, and the application's state will become inconsistent and hard to debug.

---

### 11. Best Practices
*   **ফিচার-ভিত্তিক ডিরেক্টরি ব্যবহার করুন:** স্লাইস, সিলেক্টর এবং কম্পোনেন্ট একটি নির্দিষ্ট ফিচারের ফোল্ডারে রাখুন (যেমন: `features/tasks/`)।
*   **সিলেক্টর সেন্ট্রালাইজ করুন:** প্রতিবার কম্পোনেন্টে সরাসরি স্টেট রিড না করে স্লাইস ফাইলে সিলেক্টর তৈরি করে এক্সপোর্ট করুন।
*   **সবসময় ডেভটুলস অন রাখুন:** ডেভেলপমেন্ট মোডে Redux DevTools ব্যবহার করে স্টেট পরিবর্তন ট্র্যাক করুন।

---

### 12. Performance Considerations
*   স্টোরে অপ্রয়োজনীয় বড় বড় ডেটা রাখবেন না। ডেটা নরমালাইজ করার জন্য `@reduxjs/toolkit` এর `createEntityAdapter` ব্যবহার করুন।
*   সিলেক্টরে জটিল লজিক (যেমন ফিল্টার বা সর্ট) থাকলে মেমোইজড সিলেক্টর (`createSelector`) ব্যবহার করুন।

---

### 13. When NOT to Use It
*   অত্যন্ত ছোট অ্যাপ্লিকেশনে যেখানে গ্লোবাল স্টেট শেয়ার করার প্রয়োজন নেই এবং রিঅ্যাক্ট `useState` বা `useReducer` দিয়েই কাজ চালানো যায়।
*   যদি সম্পূর্ণ আলাদা কোনো স্টেট ডোমেন ব্যবহার করতে চান (যেমন সিগন্যালস বা রিঅ্যাক্টিভ ওভজারভেবলস)।

---

### 14. Comparison with Similar Concepts
| Feature | Redux Toolkit (RTK) | Vanilla Redux | React Context API | Zustand |
| :--- | :--- | :--- | :--- | :--- |
| **Boilerplate** | Low | Very High | Minimal | Extremely Low |
| **Performance** | High (Built-in) | High (Manual optimization) | Low (Causes re-renders) | High |
| **Learning Curve** | Medium | High | Low | Low |
| **DevTools Support** | Excellent (Built-in) | Needs manual setup | No official support | Good |

---

### 15. Summary (বাংলায়)
রেডাক্স টুলকিট আর্কিটেকচার হলো রেডাক্সের একটি আধুনিক রূপ। এটি ৪টি মূল অংশ নিয়ে কাজ করে: তথ্য সংরক্ষণের জন্য 'Store', বিভিন্ন ফিচারের লজিক ও ডেটা ভাগ করার জন্য 'Slices', তথ্য তুলে আনার জন্য 'Selectors' এবং যেকোনো অতিরিক্ত কাজ করার জন্য 'Middleware'। এটি ব্যবহারের ফলে কোডের পরিমাণ অনেক কমে যায় এবং অ্যাপের পারফরম্যান্স বৃদ্ধি পায়।

---

### 16. 5 MCQ Questions with Explanations
1.  **Redux Toolkit আর্কিটেকচারের কোন অংশটি সরাসরি অ্যাসিনক্রোনাস কাজ করার জন্য দায়ী?**
    a) Store
    b) Selector
    c) Middleware
    d) Slice
    *উত্তর: c) Middleware। ব্যাখ্যা: Middleware (যেমন redux-thunk) অ্যাসিনক্রোনাস অ্যাকশন এবং এপিআই কল নিয়ন্ত্রণ করে।*
2.  **RTK-তে `configureStore` স্বয়ংক্রিয়ভাবে কোন মিডলওয়্যারটি যুক্ত করে?**
    a) Redux-Saga
    b) Redux-Thunk
    c) Redux-Logger
    d) Redux-Observable
    *উত্তর: b) Redux-Thunk। ব্যাখ্যা: RTK তার ডিফল্ট মিডলওয়্যার হিসেবে থাঙ্ক (thunk) যুক্ত করে।*
3.  **স্টোর থেকে নির্দিষ্ট ডেটা কুয়েরি করার জন্য নিচের কোনটি ব্যবহৃত হয়?**
    a) Reducer
    b) Selector
    c) Action Creator
    d) Provider
    *উত্তর: b) Selector। ব্যাখ্যা: Selector হলো এমন ফাংশন যা বড় স্টেট থেকে নির্দিষ্ট অংশ ছেঁকে নিয়ে আসে।*
4.  **Immer.js রেডাক্স টুলকিটের কোথায় কাজ করে?**
    a) Store creation-এ
    b) Selectors-এ
    c) Reducers-এর ভেতরে স্টেট আপডেটে
    d) Middleware চেইনে
    *উত্তর: c) Reducers-এর ভেতরে স্টেট আপডেটে। ব্যাখ্যা: Immer রিডিউসারে সরাসরি মিউটেবল কোড লেখার সুবিধা দেয় এবং তা ব্যাকগ্রাউন্ডে ইমিউটেবল আপডেটে রূপান্তর করে।*
5.  **নিচের কোন ফাংশনটি ভ্যানিলা রেডাক্সের `createStore` কে র‍্যাপ করে?**
    a) createSlice
    b) configureStore
    c) createReducer
    d) combineReducers
    *উত্তর: b) configureStore। ব্যাখ্যা: configureStore রান করলে ইন্টারনালি createStore রান করে ও অতিরিক্ত সেটিংস কনফিগার করে।*

---

### 17. 5 Coding Exercises
1.  **Task:** একটি `authSlice` তৈরি করুন যার ইনিশিয়াল স্টেট `{ isLoggedIn: false, userName: '' }` এবং এতে `login` ও `logout` দুটি অ্যাকশন থাকবে।
    *Hint:* `createSlice` ফাংশন ব্যবহার করে এটি ডিফাইন করুন।
2.  **Task:** একটি সিলেক্টর তৈরি করুন যা উপরের `authSlice` থেকে ইউজারের লগইন স্ট্যাটাস রিটার্ন করবে।
3.  **Task:** একটি কাস্টম মিডলওয়্যার লিখুন যা যেকোনো অ্যাকশন ডিসপ্যাচ হলে কনসোলে তার পেলোড (payload) প্রিন্ট করবে।
4.  **Task:** একটি স্টোর কনফিগার করুন যেখানে `auth` এবং `counter` দুটি স্লাইস থাকবে।
5.  **Task:** একটি স্লাইস তৈরি করুন যেখানে ইনিশিয়াল স্টেট একটি ফাঁকা অ্যারে এবং এর ভেতরে `addItem` ও `removeItem` নামক দুটি অ্যাকশন থাকবে।

---
---

## Topic 2: What is a Slice in Redux Toolkit?

### 1. Simple Definition (বাংলায়)
রেডাক্স টুলকিটে স্লাইস (Slice) হলো অ্যাপ্লিকেশনের স্টেটের একটি সুনির্দিষ্ট অংশ এবং সেই অংশের জন্য প্রয়োজনীয় রিডিউসার ও অ্যাকশন ক্রিয়েটরগুলোর একটি সমন্বিত রূপ। সহজ কথায়, এটি একই জায়গায় একটি সিঙ্গেল ফিচারের সমস্ত রেডাক্স লজিক ধারণ করে।

---

### 2. Why This Concept Exists
ভ্যানিলা রেডাক্সে ডেভেলপারের একটি নির্দিষ্ট ফিচার তৈরির জন্য তিনটি আলাদা ফাইলে কাজ করতে হতো: `actions.js`, `constants.js` এবং `reducers.js`। এই পদ্ধতিকে অনেক ডেভেলপার অপছন্দ করতেন কারণ সামান্য পরিবর্তনের জন্য অনেক ফাইলে জাম্প করতে হতো। স্লাইস এই তিনটি আলাদা ফাইলকে একটি ফাইলে নিয়ে এসে রিডাক্স ডেভেলপমেন্টকে আরও গতিশীল করতে সাহায্য করে।

---

### 3. What Problem It Solves
*   **File Hopping (ফাইলের মধ্যে ঘন ঘন যাতায়াত):** অ্যাকশন ও রিডিউসারের জন্য আলাদা আলাদা ফাইল মেইনটেইন করতে হয় না।
*   **অ্যাকশন টাইপ নেমিং কোলিশন:** অ্যাকশনগুলোর টাইপ স্বয়ংক্রিয়ভাবে স্লাইসের নাম অনুসারে তৈরি হয় (যেমন `sliceName/actionName`), যার ফলে ডুপ্লিকেট অ্যাকশন টাইপের সমস্যা হয় না।
*   **অ্যাকশন ক্রিয়েটর লেখার ক্লান্তি:** রিডিউসারের মেথডের নাম দেখেই RTK নিজ থেকে অ্যাকশন ক্রিয়েটর ফাংশন জেনারেট করে।

---

### 4. Real-life Analogy
একটি বড় লাইব্রেরির কথা চিন্তা করুন। লাইব্রেরিতে বিভিন্ন ক্যাটাগরির বই থাকে (যেমন- বিজ্ঞান, কল্পকাহিনী, ইতিহাস)। লাইব্রেরি যদি সব বই এলোমেলোভাবে এক জায়গায় রাখত, তবে বই খুঁজে পাওয়া কঠিন হতো। কিন্তু লাইব্রেরিতে বিজ্ঞানের বইয়ের জন্য আলাদা একটি সেলফ বা আলমারি থাকে। এই বিজ্ঞানের আলমারিটিই হলো একটি Slice। এর নিজস্ব বই (State) আছে এবং বই সাজানোর বা বের করার সুনির্দিষ্ট নিয়ম (Reducers) আছে।

---

### 5. How Redux/React Works Internally
`createSlice` মেথডটি কল করার সময় আমরা একটি কনফিগারেশন অবজেক্ট পাস করি।
1.  RTK অবজেক্টের `reducers` ফিল্ডে থাকা প্রতিটি ফাংশনের জন্য একটি অ্যাকশন ক্রিয়েটর তৈরি করে।
2.  যদি স্লাইসের নাম `cart` হয় এবং রিডিউসারের নাম `addItem` হয়, তবে জেনারেট হওয়া অ্যাকশন টাইপ হবে `cart/addItem`।
3.  ইন্টারনালি এটি Immer.js ব্যবহার করে। যখন আপনি স্লাইস রিডিউসারের ভেতরে কোনো অবজেক্ট মডিফাই করেন, তখন Immer ব্যাকগ্রাউন্ডে একটি কপি নিয়ে পরিবর্তনগুলো সম্পন্ন করে নতুন অবজেক্ট সাবমিট করে।
4.  স্লাইস তৈরি হওয়ার পর এর আউটপুট অবজেক্টে `actions` (যা অ্যাকশন ক্রিয়েটর ফাংশন ধারণ করে) এবং `reducer` (যা মূল রিডিউসার ফাংশন) পাওয়া যায়।

---

### 6. Basic Example (English Code)
```javascript
import { createSlice } from '@reduxjs/toolkit';

const cartSlice = createSlice({
  name: 'cart',
  initialState: { items: [], totalAmount: 0 },
  reducers: {
    addToCart: (state, action) => {
      // Immer allows direct mutation here safely
      state.items.push(action.payload);
      state.totalAmount += action.payload.price;
    },
    clearCart: (state) => {
      state.items = [];
      state.totalAmount = 0;
    }
  }
});

// Auto-generated action creators
export const { addToCart, clearCart } = cartSlice.actions;

// Auto-generated reducer
export default cartSlice.reducer;
```

---

### 7. Step-by-step Explanation of the Code
*   `createSlice` মেথডের মাধ্যমে আমরা `cart` নামের একটি স্লাইস তৈরি করেছি।
*   `initialState` হিসেবে একটি অবজেক্ট দেওয়া হয়েছে যাতে `items` অ্যারে এবং `totalAmount` নাম্বার ভ্যালু রয়েছে।
*   `reducers` ব্লকে `addToCart` ফাংশনটি প্যারামিটার হিসেবে `state` এবং `action` গ্রহণ করে। `state.items.push(action.payload)` কোডের সাহায্যে সহজেই পেলোড কার্টে পুশ করা হচ্ছে।
*   `cartSlice.actions` থেকে রিডিউসার মেথডগুলোর নামের সাথে মিল রেখে অ্যাকশন ক্রিয়েটরগুলো বের করে এক্সপোর্ট করা হয়েছে।
*   `cartSlice.reducer` কে ডিফল্ট এক্সপোর্ট করা হয়েছে যাতে এটি স্টোরে যুক্ত করা যায়।

---

### 8. Another Real-world Example (English Code)
**Theme Control Slice:**
```javascript
import { createSlice } from '@reduxjs/toolkit';

const themeSlice = createSlice({
  name: 'theme',
  initialState: { mode: 'light' },
  reducers: {
    toggleTheme: (state) => {
      state.mode = state.mode === 'light' ? 'dark' : 'light';
    },
    setTheme: (state, action) => {
      state.mode = action.payload; // payload can be 'light', 'dark' or 'blue'
    }
  }
});

export const { toggleTheme, setTheme } = themeSlice.actions;
export default themeSlice.reducer;
```

---

### 9. Common Mistakes Beginners Make
*   **ভুল মিউটেশন করা:** রিডিউসারের ভেতরে সম্পূর্ণ স্টেট ভ্যারিয়েবলকে রি-অ্যাসাইন করার চেষ্টা করা, যেমন: `state = action.payload`। Immer রেফারেন্স প্রতিস্থাপন করা সমর্থন করে না। সম্পূর্ণ স্টেট পরিবর্তন করতে হলে এটি সরাসরি `return action.payload` করতে হবে।
*   **অ্যাকশন ইমপোর্ট করার সময় ভুল:** স্লাইস থেকে অ্যাকশন ইমপোর্ট করার সময় ব্র্যাকেট দিতে ভুলে যাওয়া, যেমন: `import clearCart from './cartSlice'` (সঠিক হলো `import { clearCart } from './cartSlice'`)।

---

### 10. Interview Questions
1.  **Question:** What does `createSlice` return in Redux Toolkit?
    *   **Answer:** It returns an object containing the generated reducer function (under `.reducer`) and auto-generated action creators (under `.actions`).
2.  **Question:** Can you mutate state inside a slice reducer? Why?
    *   **Answer:** Yes, it looks like mutation (e.g., `state.items.push()`), but it's safe because Immer.js intercepts it and updates the state immutably under the hood.
3.  **Question:** What is the difference between `reducers` and `extraReducers` in a slice?
    *   **Answer:** `reducers` generates action creators for that slice. `extraReducers` allows a slice to respond to actions generated by other slices or asynchronous thunks.
4.  **Question:** What will be the action type for a slice named 'auth' with a reducer named 'login'?
    *   **Answer:** The auto-generated action type string will be `'auth/login'`.
5.  **Question:** How can you completely reset the state of a slice?
    *   **Answer:** You can return the initial state value directly from the reducer function, e.g., `clearState: () => initialState`.

---

### 11. Best Practices
*   প্রতিটি স্লাইস ফাইলে তার ইনিশিয়াল স্টেট পরিষ্কারভাবে ডিফাইন করুন।
*   অ্যাকশন ক্রিয়েটর এবং স্লাইস রিডিউসার একই ফাইলে রাখুন (যা Ducks pattern নামে পরিচিত)।
*   স্লাইসের নাম সবসময় ইউনিক রাখুন।

---

### 12. Performance Considerations
*   অত্যন্ত জটিল নেস্টেড অবজেক্ট স্লাইস স্টেটে রাখলে Immer এর পারফরম্যান্স কিছুটা কমতে পারে। স্টেট স্ট্রাকচারকে যথাসম্ভব ফ্ল্যাট বা সাধারণ রাখার চেষ্টা করুন।

---

### 13. When NOT to Use It
*   যখন কোনো নির্দিষ্ট স্টেট শুধুমাত্র একটি লোকাল রিঅ্যাক্ট কম্পোনেন্টে ব্যবহৃত হয় এবং অন্য কোনো কম্পোনেন্টের তা জানার দরকার নেই। সেখানে রিঅ্যাক্টের নিজস্ব `useState` ব্যবহার করা ভালো।

---

### 14. Comparison with Similar Concepts
| Criteria | RTK Slice | Vanilla Reducer | React Context |
| :--- | :--- | :--- | :--- |
| **Action Creation** | Automatic | Manual | N/A |
| **Immutability** | Handled by Immer | Manual (`...state`) | Manual |
| **Separation** | Modular | Monolithic / Complex | Context specific |

---

### 15. Summary (বাংলায়)
স্লাইস হলো একটি ফিচারের জন্য তৈরি রেডাক্সের অল-ইন-ওয়ান প্যাকেজ। এটি দিয়ে আমরা একই স্থানে স্টেট, অ্যাকশন এবং রিডিউসারের কাজ সম্পাদন করতে পারি। এর ফলে কোড মেইনটেইন করা অত্যন্ত সহজ এবং দ্রুত হয়।

---

### 16. 5 MCQ Questions with Explanations
1.  **`createSlice` থেকে উৎপন্ন অ্যাকশন ক্রিয়েটরগুলো কোন প্রপার্টির মাধ্যমে পাওয়া যায়?**
    a) `slice.reducers`
    b) `slice.actions`
    c) `slice.events`
    d) `slice.types`
    *উত্তর: b) `slice.actions`। ব্যাখ্যা: createSlice তার অ্যাকশন ক্রিয়েটরগুলোকে .actions প্রপার্টিতে অবজেক্ট হিসেবে প্রদান করে।*
2.  **স্লাইসে অ্যাকশন টাইপ জেনারেট হওয়ার স্ট্যান্ডার্ড ফরম্যাট কোনটি?**
    a) `action/slice`
    b) `name_action`
    c) `sliceName/reducerKey`
    d) `reducerKey/sliceName`
    *উত্তর: c) `sliceName/reducerKey`। ব্যাখ্যা: স্লাইসের নাম এবং রিডিউসার মেথডের নাম স্ল্যাশ দিয়ে যুক্ত হয়ে অ্যাকশন টাইপ তৈরি করে।*
3.  **যদি আপনি স্লাইস রিডিউসারের ভেতরে সম্পূর্ণ স্টেট পরিবর্তন করতে চান, তবে আপনাকে কী করতে হবে?**
    a) `state = action.payload` লিখতে হবে
    b) স্টেট ভ্যালুটি `return` করতে হবে
    c) কিছুই করতে হবে না, Immer সব করে দেবে
    d) `state.replace(action.payload)` করতে হবে
    *উত্তর: b) স্টেট ভ্যালুটি `return` করতে হবে। ব্যাখ্যা: সরাসরি state ভ্যারিয়েবল রি-অ্যাসাইন করলে Immer ট্র্যাক করতে পারে না, তাই নতুন অবজেক্ট রিটার্ন করতে হয়।*
4.  **নিচের কোন স্লাইস প্রপার্টিটি অন্যান্য স্লাইস অ্যাকশন হ্যান্ডেল করতে ব্যবহৃত হয়?**
    a) customReducers
    b) externalReducers
    c) extraReducers
    d) sideReducers
    *উত্তর: c) extraReducers। ব্যাখ্যা: extraReducers অন্য স্লাইসের অ্যাকশন বা অ্যাসিনক্রোনাস Thunks-এর ইভেন্ট লিসেন করতে সাহায্য করে।*
5.  **ভ্যানিলা রেডাক্সের কোন তিনটি উপাদান স্লাইসের মাধ্যমে এক ফাইলে চলে আসে?**
    a) Action Types, Action Creators, Reducers
    b) Store, Selectors, Middleware
    c) Provider, Consumer, Context
    d) Component, Hook, State
    *উত্তর: a) Action Types, Action Creators, Reducers। ব্যাখ্যা: স্লাইস এই তিনটি উপাদানকে একটি ফাইলে একীভূত করে।*

---

### 17. 5 Coding Exercises
1.  **Task:** `profileSlice` নামে একটি স্লাইস তৈরি করুন যার ইনিশিয়াল স্টেট `{ name: '', age: 0 }` এবং এতে `updateAge` নামের একটি রিডিউসার থাকবে।
    *Hint:* `updateAge` রিডিউসারে `state.age = action.payload` ব্যবহার করুন।
2.  **Task:** একটি স্লাইস তৈরি করুন যা একটি শপিং কার্ট থেকে আইটেমের আইডি সার্চ করে সেটি রিমুভ করবে।
3.  **Task:** একটি `settingsSlice` তৈরি করুন যেখানে `language` চেঞ্জ করার লজিক থাকবে এবং ডিফল্ট ল্যাঙ্গুয়েজ হবে 'en'।
4.  **Task:** এমন একটি স্লাইস তৈরি করুন যা স্টেট হিসেবে একটি নম্বর অ্যারে রাখবে এবং একটি রিডিউসার থাকবে যা শুধুমাত্র জোড় (even) নম্বরগুলো ফিল্টার করে রাখবে।
5.  **Task:** একটি `notificationsSlice` তৈরি করুন যা রানিং নোটিফিকেশন পুশ করবে এবং একটি নির্দিষ্ট টাইমার পর তা ক্লিয়ার করবে।

---
---

## Topic 3: What is a Selector?

### 1. Simple Definition (বাংলায়)
সিলেক্টর (Selector) হলো একটি সাধারণ জাভাস্ক্রিপ্ট ফাংশন যা রেডাক্স স্টোরের সম্পূর্ণ স্টেট অবজেক্ট থেকে নির্দিষ্ট কিছু প্রয়োজনীয় ডেটা খুঁজে বের বা ফিল্টার করে রিঅ্যাক্ট কম্পোনেন্টে সরবরাহ করে। সহজ কথায়, এটি স্টোর থেকে ডেটা পড়ার চাবিকাঠি।

---

### 2. Why This Concept Exists
রেডাক্স স্টোর সাধারণত অ্যাপ্লিকেশনের সব ডেটা ধারণকারী একটি জটিল এবং নেস্টেড অবজেক্ট। রিঅ্যাক্ট কম্পোনেন্টের ভেতরে সরাসরি এই জটিল অবজেক্ট অ্যাক্সেস করে ডেটা বের করা ভালো প্র্যাকটিস নয়। যদি কখনো স্টেটের স্ট্রাকচার পরিবর্তন হয়, তবে সরাসরি অ্যাক্সেস করা সমস্ত কম্পোনেন্ট ভেঙে যাবে। সিলেক্টর এই ডেটা তুলে আনার লজিককে এক জায়গায় কেন্দ্রীভূত করে এই সমস্যার সমাধান করে।

---

### 3. What Problem It Solves
*   **কোড ডুপ্লিকেশন হ্রাস:** একই ডেটা ফিল্টারিং লজিক একাধিক কম্পোনেন্টে বারবার লিখতে হয় না।
*   **ডিকাপলিং (Decoupling):** স্টেট স্ট্রাকচার পরিবর্তিত হলেও শুধুমাত্র সিলেক্টরটি আপডেট করলেই হয়, কম্পোনেন্টে কোনো কোড পরিবর্তন করতে হয় না।
*   **পারফরম্যান্স অপ্টিমাইজেশন:** মেমোইজড সিলেক্টর ব্যবহারের মাধ্যমে অপ্রয়োজনীয় রি-রেন্ডার কমানো যায়।

---

### 4. Real-life Analogy
একটি রেস্টুরেন্টের বড় মেনু কার্ডের কথা ভাবা যাক। মেনু কার্ডে নানা পদের খাবার সাজানো থাকে (সবজি, মাংস, পানীয় ইত্যাদি)। আপনি যদি নিরামিষভোজী হন, তবে আপনার পুরো মেনু খোঁজার দরকার নেই। আপনি ওয়েটারকে বলতে পারেন শুধুমাত্র "ভেজিটেরিয়ান খাবারের লিস্ট" দেখাতে। এখানে ওয়েটারটি হলো Selector, যে পুরো মেনু কার্ড (Store State) থেকে শুধুমাত্র নিরামিষ খাবারগুলো ফিল্টার করে আপনার সামনে উপস্থাপন করে।

---

### 5. How Redux/React Works Internally
1.  যখন আমরা রিঅ্যাক্ট কম্পোনেন্টে `useSelector(selectorFunction)` ব্যবহার করি, তখন React-Redux লাইব্রেরি আমাদের কম্পোনেন্টকে রেডাক্স স্টোরের সাথে সাবস্ক্রাইব করায়।
2.  প্রতিবার রেডাক্স স্টোরে কোনো অ্যাকশন ডিসপ্যাচ হওয়ার পর, `useSelector` সিলেক্টর ফাংশনটি পুনরায় রান করে।
3.  এটি সিলেক্টরের রিটার্ন করা নতুন ভ্যালুর সাথে আগের ভ্যালুর তুলনা করে (Strict Reference Equality - `===`)।
4.  যদি ভ্যালু অপরিবর্তিত থাকে, তবে কম্পোনেন্টটি রি-রেন্ডার হয় না। যদি সিলেক্টর একটি নতুন অবজেক্ট বা অ্যারে রিটার্ন করে, তবে কম্পোনেন্টটি রি-রেন্ডার হয়।
5.  `createSelector` ফাংশনটি (Reselect থেকে আনা) ইনপুট স্টেটের মান ট্র্যাক করে ক্যাশ (Cache) করে রাখে। যতক্ষণ ইনপুট ডেটা না বদলায়, এটি আগের হিসাব করা মান সরাসরি রিটার্ন করে (Memoization)।

---

### 6. Basic Example (English Code)
```javascript
// A simple selector extracting all users
export const selectAllUsers = (state) => state.users.list;

// A selector that retrieves only active users
export const selectActiveUsers = (state) => {
  return state.users.list.filter(user => user.status === 'active');
};
```

---

### 7. Step-by-step Explanation of the Code
*   `selectAllUsers` হলো একটি বেসিক সিলেক্টর যা পুরো রেডাক্স স্টেটের `state.users.list` থেকে সরাসরি ইউজারের তালিকা রিড করে।
*   `selectActiveUsers` সিলেক্টরটি প্রথমে সম্পূর্ণ ইউজারের লিস্ট অ্যাক্সেস করে এবং জাভাস্ক্রিপ্টের `.filter()` মেথড ব্যবহার করে শুধুমাত্র যাদের স্ট্যাটাস 'active' তাদের ছেঁকে নিয়ে আসে।
*   কম্পোনেন্টে এটি ব্যবহার করতে আমরা `const activeUsers = useSelector(selectActiveUsers)` কল করতে পারি।

---

### 8. Another Real-world Example (English Code)
**Memoized Selector using `createSelector`:**
```javascript
import { createSelector } from '@reduxjs/toolkit';

// Basic Input Selectors
const selectCartItems = (state) => state.cart.items;
const selectTaxRate = (state) => state.cart.taxRate;

// Memoized Selector
export const selectCartSubtotal = createSelector(
  [selectCartItems],
  (items) => items.reduce((total, item) => total + item.price * item.quantity, 0)
);

// Composed Memoized Selector using another memoized selector
export const selectCartTotalWithTax = createSelector(
  [selectCartSubtotal, selectTaxRate],
  (subtotal, taxRate) => subtotal + subtotal * taxRate
);
```

---

### 9. Common Mistakes Beginners Make
*   **ইনলাইন সিলেক্টরে নতুন অবজেক্ট তৈরি করা:** `useSelector(state => state.items.filter(i => i.active))` সরাসরি কম্পোনেন্টে লেখা। যেহেতু `.filter()` প্রতিবার নতুন অ্যারে রেফারেন্স তৈরি করে, তাই প্রতি অ্যাকশনে এই কম্পোনেন্ট অপ্রয়োজনীয়ভাবে রি-রেন্ডার হবে। এর সমাধান হলো `createSelector` ব্যবহার করা।
*   **নামকরণে অসঙ্গতি:** সিলেক্টরের নাম সাধারণ ফাংশনের মতো রাখা। বেস্ট প্র্যাকটিস হলো নামের শুরুতে `select` শব্দ যুক্ত করা (যেমন `selectProducts`)।

---

### 10. Interview Questions
1.  **Question:** What is a Selector in Redux and why should we use it?
    *   **Answer:** A selector is a function that extracts specific slices of state. We use it to centralize state retrieval logic and decouple UI components from the shape of the Redux state.
2.  **Question:** How does `useSelector` determine if a React component needs to re-render?
    *   **Answer:** It compares the previous result of the selector with the current result using strict reference equality (`===`). If the reference changes, the component re-renders.
3.  **Question:** What is a memoized selector, and how do you create one in RTK?
    *   **Answer:** A memoized selector caches its results. If its inputs haven't changed, it returns the cached result without recalculating. In RTK, it is created using `createSelector`.
4.  **Question:** Why does using `.map()` or `.filter()` inside a raw `useSelector` cause performance issues?
    *   **Answer:** Because both `.map()` and `.filter()` return a new array instance (new reference) every time they run, causing `useSelector` to think the state has changed and trigger a re-render.
5.  **Question:** How can you pass a dynamic parameter (like an item ID) to a selector?
    *   **Answer:** You can create a factory selector function, or return a function from the selector: `const selectItemById = (state, itemId) => state.items.find(item => item.id === itemId)`.

---

### 11. Best Practices
*   সিলেক্টর সবসময় স্লাইস ফাইলের নিচে অথবা একটি ডেডিকেটেড `selectors.js` ফাইলে ডিফাইন করুন।
*   যেকোনো ধরনের ডেটা সর্টিং, ফিল্টারিং বা জটিল ক্যালকুলেশনের জন্য `createSelector` দিয়ে মেমোইজেশন নিশ্চিত করুন।
*   সিলেক্টর ফাংশনের শুরুতে `select` প্রিফিক্স ব্যবহার করুন।

---

### 12. Performance Considerations
*   মেমোইজড সিলেক্টর ইনপুট আর্গুমেন্টগুলোর রেফারেন্স চেক করে। তাই ইনপুট সিলেক্টরগুলো যেন হালকা ও দ্রুতগতির হয় তা নিশ্চিত করা উচিত।

---

### 13. When NOT to Use It
*   যখন অ্যাপ্লিকেশনের স্টেট একদম রুট লেভেলে থাকে এবং কোনো ডেরিভেটিভ প্রসেসিং ছাড়াই সরাসরি রিড করা যায়, তখন অতিরিক্ত কাস্টম সিলেক্টর তৈরি না করে সরাসরি ইন্টিগ্রেটেড ইনলাইন কুয়েরি ব্যবহার করা যেতে পারে।

---

### 14. Comparison with Similar Concepts
| Approach | Selector (RTK) | In-Component Filtering | mapStateToProps (Legacy) |
| :--- | :--- | :--- | :--- |
| **Reusability** | Very High | Low | Medium |
| **Performance** | Excellent (with Memoization) | Poor (calculates on every render) | High |
| **Separation of Concerns** | Yes | No | Yes |

---

### 15. Summary (বাংলায়)
সিলেক্টর হলো এমন একটি কুয়েরি ফাংশন যা রেডাক্স স্টেট থেকে আমাদের প্রয়োজনীয় ডেটা ফিল্টার করে এনে দেয়। এটি ব্যবহারে আমাদের কম্পোনেন্ট সুন্দর ও ক্লিন থাকে এবং মেমোইজেশনের মাধ্যমে অ্যাপের পারফরম্যান্স বহুগুণ বেড়ে যায়।

---

### 16. 5 MCQ Questions with Explanations
1.  **নিচের কোনটি সিলেক্টর ফাংশনের প্রধান কাজ?**
    a) স্টেট পরিবর্তন করা
    b) এপিআই থেকে ডেটা আনা
    c) স্টোর স্টেট থেকে ডেটা রিড করা
    d) অ্যাকশন ডিসপ্যাচ করা
    *উত্তর: c) স্টোর স্টেট থেকে ডেটা রিড করা। ব্যাখ্যা: সিলেক্টর মূলত স্টেট পড়ার বা এক্সেস করার জন্য ব্যবহৃত হয়।*
2.  **মেমোইজড সিলেক্টর তৈরি করতে রেডাক্স টুলকিটের কোন ফাংশনটি ব্যবহৃত হয়?**
    a) createSlice
    b) configureStore
    c) createSelector
    d) createMemo
    *উত্তর: c) createSelector। ব্যাখ্যা: createSelector ফাংশনটি Reselect লাইব্রেরি ব্যবহার করে মেমোইজড সিলেক্টর তৈরি করে।*
3.  **`useSelector` হুক স্টেট পরিবর্তনের পর কীভাবে তুলনা করে?**
    a) Deep equality comparison
    b) Strict reference equality (`===`)
    c) JSON comparison
    d) Length comparison
    *উত্তর: b) Strict reference equality (`===`)। ব্যাখ্যা: useSelector আগের ও বর্তমান সিলেক্টরের ফলাফলের রেফারেন্সের তুলনা করে।*
4.  **সিলেক্টরের নামের শুরুতে কোন কনভেনশনটি ব্যবহার করা উচিত?**
    a) `get`
    b) `fetch`
    c) `select`
    d) `read`
    *উত্তর: c) `select`। ব্যাখ্যা: রেডাক্সে সিলেক্টরের নাম select দিয়ে শুরু করা বেস্ট প্র্যাকটিস (যেমন selectActiveUsers)।*
5.  **নিচের কোন মেথডটি সরাসরি সিলেক্টরে ব্যবহার করলে অপ্রয়োজনীয় রি-রেন্ডার হতে পারে?**
    a) `state.auth.name`
    b) `state.todos.list.map(...)`
    c) `state.counter.value`
    d) `state.theme`
    *উত্তর: b) `state.todos.list.map(...)`। ব্যাখ্যা: map মেথড প্রতিবার নতুন রেফারেন্সের অ্যারে রিটার্ন করে, যা রিঅ্যাক্টকে বারবার রি-রেন্ডার করতে বাধ্য করে।*

---

### 17. 5 Coding Exercises
1.  **Task:** একটি সিলেক্টর `selectUserName` লিখুন যা `state.user.profile.name` থেকে ইউজারের নাম রিটার্ন করবে।
    *Hint:* `(state) => state.user.profile.name` ব্যবহার করুন।
2.  **Task:** `createSelector` ব্যবহার করে এমন একটি সিলেক্টর তৈরি করুন যা কার্ট আইটেমগুলোর মধ্য থেকে শুধুমাত্র ডিসকাউন্টেড পণ্যগুলো ফিল্টার করবে।
3.  **Task:** এমন একটি সিলেক্টর লিখুন যা ইউজারের বয়স চেক করে দেখবে সে ১৮ বছরের ঊর্ধ্বে কিনা (রিটার্ন করবে true অথবা false)।
4.  **Task:** একটি স্লাইসে থাকা বুকমার্ক তালিকার দৈর্ঘ্য (length) বের করার জন্য একটি সিলেক্টর লিখুন।
5.  **Task:** একটি জটিল সিলেক্টর তৈরি করুন যা ইনপুট হিসেবে `userId` গ্রহণ করে স্টোর থেকে সেই নির্দিষ্ট ইউজারের সমস্ত তথ্য খুঁজে বের করবে।

---
---

## Topic 4: Explain the role of Provider and Reducers in connecting React with Redux.

### 1. Simple Definition (বাংলায়)
`Provider` এবং `Reducers` হলো রিঅ্যাক্ট এবং রেডাক্সের সংযোগকারী দুটি স্তম্ভ।
*   **Provider**: এটি React-Redux এর একটি রুট লেভেল কম্পোনেন্ট যা সম্পূর্ণ রিঅ্যাক্ট অ্যাপ্লিকেশনকে রেডাক্স স্টোরের সাথে যুক্ত করে এবং সমস্ত চাইল্ড কম্পোনেন্টকে স্টোর অ্যাক্সেস করার সুবিধা দেয়।
*   **Reducers**: এগুলো হলো বিশুদ্ধ ফাংশন (Pure Functions) যা নির্ধারণ করে যে একটি নির্দিষ্ট অ্যাকশনের পর অ্যাপের বর্তমান স্টেট কীভাবে পরিবর্তিত হবে।

---

### 2. Why This Concept Exists
রিঅ্যাক্ট এবং রেডাক্স সম্পূর্ণ ভিন্ন দুটি লাইব্রেরি। রিঅ্যাক্ট তার কম্পোনেন্ট ট্রির ভেতর দিয়ে ডেটা পাস করে এবং রেডাক্স তার গ্লোবাল স্টোরে ডেটা রাখে। এদের মধ্যে যোগাযোগের কোনো স্বয়ংক্রিয় পথ নেই। `Provider` কম্পোনেন্টটি রিঅ্যাক্ট ট্রির শীর্ষে বসে স্টোরকে সবার জন্য উন্মুক্ত করে এবং `Reducers` স্টোরের ভেতরের ডেটা পরিবর্তনের নিয়মগুলো পরিচালনা করে এদের মধ্যে সংযোগ স্থাপন করে।

---

### 3. What Problem It Solves
*   **Prop Drilling দূরীকরণ:** স্টোর বা স্টেট ডেটা প্রতিটি কম্পোনেন্টের প্রপস হিসেবে ম্যানুয়ালি নিচে পাস করতে হয় না।
*   **Separation of Concerns (কাজের বিভাজন):** ডেটা কীভাবে পরিবর্তিত হবে তার লজিক (Reducers) এবং কীভাবে ডেটা প্রদর্শিত হবে তার লজিক (React Components) সম্পূর্ণ আলাদা থাকে।
*   **স্টেট ট্র্যাকাবিলিটি:** রিডিউসারের মাধ্যমে স্টেট পরিবর্তন হওয়ায় যেকোনো সময় স্টেটের পূর্ববর্তী ও পরবর্তী অবস্থা সহজে ট্র্যাক করা যায়।

---

### 4. Real-life Analogy
একটি অ্যাপার্টমেন্ট বিল্ডিংয়ের কথা চিন্তা করা যাক:
*   **Provider (মূল বিদ্যুৎ সংযোগ বা মেইন গ্রিড):** অ্যাপার্টমেন্টের দেওয়ালে বসানো প্রধান বিদ্যুৎ সংযোগ যা পুরো বিল্ডিংয়ের প্রতিটি ফ্ল্যাটে বিদ্যুৎ পৌঁছে দেয়। এই সংযোগ না থাকলে কোনো ফ্ল্যাটেই আলো জ্বলবে না।
*   **Reducers (প্রতিটি ফ্ল্যাটের সুইচবোর্ড):** যখন আপনি কোনো সুইচ টেপেন (Action), তখন সুইচবোর্ডটি সিদ্ধান্ত নেয় কোন বাতিটি জ্বলবে বা ফ্যানটি ঘুরবে। অর্থাৎ সুইচবোর্ডটি ফ্ল্যাটের অবস্থা (State) পরিবর্তন করে।

---

### 5. How Redux/React Works Internally
1.  `<Provider store={store}>` কম্পোনেন্টটি রিঅ্যাক্টের **Context API** ব্যবহার করে রেডাক্স স্টোর অবজেক্টকে পুরো কম্পোনেন্ট ট্রির কন্টেক্সটে সেট করে দেয়।
2.  এর ফলে চাইল্ড কম্পোনেন্টে ব্যবহৃত `useSelector` এবং `useDispatch` হুকগুলো অভ্যন্তরীণভাবে রিঅ্যাক্ট কন্টেক্সট থেকে স্টোরের রেফারেন্স রিড করতে পারে।
3.  যখন একটি অ্যাকশন ডিসপ্যাচ করা হয়, স্টোর সরাসরি তার রেজিস্টার্ড **Root Reducer**-কে কল করে।
4.  রিডিউসার পিওর ফাংশন হওয়ায় এটি বর্তমান স্টেট এবং অ্যাকশন অবজেক্ট ইনপুট হিসেবে নেয় এবং সম্পূর্ণ নতুন একটি স্টেট অবজেক্ট রিটার্ন করে।
5.  নতুন স্টেট পাওয়ার সাথে সাথে স্টোর তার লিসেনারদের নোটিফাই করে এবং রিঅ্যাক্ট কম্পোনেন্টগুলো পরিবর্তিত স্টেটের ওপর ভিত্তি করে রি-রেন্ডার হয়।

---

### 6. Basic Example (English Code)
**Reducer Definition (`counterReducer.js`):**
```javascript
const initialState = { count: 0 };

export const counterReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'counter/increment':
      return { ...state, count: state.count + 1 }; // Return new state object
    default:
      return state;
  }
};
```

**React Connection (`index.js`):**
```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import App from './App';
import { counterReducer } from './counterReducer';

// Store setup
const store = configureStore({
  reducer: {
    counter: counterReducer
  }
});

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Provider store={store}>
    <App />
  </Provider>
);
```

---

### 7. Step-by-step Explanation of the Code
*   `counterReducer` হলো একটি স্ট্যান্ডার্ড রিডিউসার ফাংশন যা `state` এবং `action` গ্রহণ করে। যদি অ্যাকশন টাইপ `'counter/increment'` হয়, তবে এটি আগের স্টেটকে স্প্রেড (`...state`) করে নতুন কাউন্ট অবজেক্ট রিটার্ন করে।
*   `configureStore` দিয়ে এই রিডিউসারকে রেজিস্টার করে `store` অবজেক্ট তৈরি করা হয়েছে।
*   `<Provider store={store}>` দিয়ে `<App />` কে রুট লেভেলে মুড়িয়ে দেওয়া হয়েছে। এর ফলে `App` কম্পোনেন্ট এবং এর ভেতরের সকল চাইল্ড কম্পোনেন্ট রেডাক্স স্টোরের সাথে কানেক্টেড হয়ে গেছে।

---

### 8. Another Real-world Example (English Code)
**Multi-reducer Setup with RTK Slices:**
```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import { Provider } from 'react-redux';
import { configureStore, createSlice } from '@reduxjs/toolkit';

// 1. User Slice (Reducer 1)
const userSlice = createSlice({
  name: 'user',
  initialState: { name: 'Guest' },
  reducers: {
    setName: (state, action) => { state.name = action.payload; }
  }
});

// 2. Settings Slice (Reducer 2)
const settingsSlice = createSlice({
  name: 'settings',
  initialState: { theme: 'light' },
  reducers: {
    toggleTheme: (state) => { state.theme = state.theme === 'light' ? 'dark' : 'light'; }
  }
});

// 3. Combine in Store
const store = configureStore({
  reducer: {
    user: userSlice.reducer,
    settings: settingsSlice.reducer
  }
});

// 4. Connect using Provider
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <Provider store={store}>
    <App />
  </Provider>
);
```

---

### 9. Common Mistakes Beginners Make
*   **Provider দিয়ে র‍্যাপ না করা:** অ্যাপ্লিকেশনের রুট ফাইল (যেমন `main.jsx` বা `index.js`) Provider দিয়ে র‍্যাপ করতে ভুলে যাওয়া। এর ফলে `Could not find react-redux context value` এরর দেখা দেয়।
*   **রিডিউসারে সাইড-ইফেক্ট করা:** রিডিউসারের ভেতরে এপিআই কল করা, র্যান্ডম নাম্বার জেনারেট করা (`Math.random()`), বা সরাসরি লোকাল স্টোরেজ আপডেট করা। রিডিউসার সবসময় সাইড-ইফেক্ট মুক্ত বিশুদ্ধ ফাংশন হতে হবে।

---

### 10. Interview Questions
1.  **Question:** What happens if you forget to wrap your application with the `<Provider>` component?
    *   **Answer:** Any component trying to use Redux hooks (`useSelector` or `useDispatch`) will throw a runtime error saying they couldn't find the Redux store in the React context.
2.  **Question:** Why is a Reducer called a "Pure Function"?
    *   **Answer:** Because for the same input arguments, it always returns the exact same output, and it does not produce any side effects (like API requests or state modifications outside the function).
3.  **Question:** How does the `<Provider>` component make the Redux store available to all child components?
    *   **Answer:** It uses React's Context API under the hood to inject the store instance into the component tree.
4.  **Question:** What is the consequence of mutating the state directly in a classic Redux Reducer?
    *   **Answer:** Direct mutation will not change the object reference. Since React-Redux uses reference comparison to detect state changes, the UI will fail to re-render.
5.  **Question:** Can we have multiple `<Provider>` components in a single React application?
    *   **Answer:** Yes, but it is rarely needed. It is only done when you want to isolate different sub-trees of your application to use completely independent Redux stores.

---

### 11. Best Practices
*   সবসময় রিঅ্যাক্ট অ্যাপের রুট ফাইলে `Provider` ব্যবহার করুন যাতে পুরো অ্যাপ স্টোরের অ্যাক্সেস পায়।
*   রিডিউসারগুলোকে ছোট ছোট অর্থবহ ফাইলে ভাগ করুন এবং পরবর্তীতে সেগুলোকে রুট রিডিউসারে একত্রিত করুন।
*   রিডিউসার লজিককে সবসময় সিঙ্ক্রোনাস রাখুন।

---

### 12. Performance Considerations
*   যেহেতু `Provider` প্রতিটি চাইল্ডকে স্টোর রিসিভ করার সুযোগ দেয়, তাই অপ্রয়োজনীয় রেন্ডার এড়াতে `useSelector` এর ভেতর সঠিক এবং সুনির্দিষ্ট ডেটা সিলেক্ট করুন।

---

### 13. When NOT to Use It
*   যদি রিঅ্যাক্ট প্রজেক্টে স্টেট শেয়ারিং শুধুমাত্র দু-একটি কম্পোনেন্টের মধ্যে সীমাবদ্ধ থাকে, তবে কোনো গ্লোবাল রিডিউসার বা `Provider` সেটআপের প্রয়োজন নেই।

---

### 14. Comparison with Similar Concepts
| Concept | Provider (React-Redux) | React Context Provider | Reducer (Redux) | useReducer Hook |
| :--- | :--- | :--- | :--- | :--- |
| **Purpose** | Connects Redux Store | Shares custom values | Manages global state | Manages local state |
| **Performance** | Highly optimized | Causes full tree re-renders | High | Medium |
| **Scope** | Global | Custom / Local | Global | Component level |

---

### 15. Summary (বাংলায়)
`Provider` হলো এমন একটি গেটওয়ে বা মাধ্যম যা রিঅ্যাক্ট অ্যাপের সব কম্পোনেন্টকে রেডাক্স স্টোরের সাথে যুক্ত করে। আর `Reducers` হলো সেই চালিকাশক্তি যা অ্যাপের অ্যাকশন বুঝে স্টেট আপডেট করে। এই দুটি একসাথে রিঅ্যাক্ট ও রেডাক্সের সফল সংযোগ ঘটায়।

---

### 16. 5 MCQ Questions with Explanations
1.  **`<Provider>` কম্পোনেন্টে কোন প্রপটি পাঠানো বাধ্যতামূলক?**
    a) `reducer`
    b) `store`
    c) `state`
    d) `context`
    *উত্তর: b) `store`। ব্যাখ্যা: Provider-কে অবশ্যই store প্রপ হিসেবে পাস করতে হয় যাতে সে সেটি পুরো অ্যাপে শেয়ার করতে পারে।*
2.  **রিডিউসার ফাংশনটি অবশ্যই কেমন হতে হবে?**
    a) Asynchronous Function
    b) Impure Function
    c) Pure Function
    d) High-Order Component
    *উত্তর: c) Pure Function। ব্যাখ্যা: রিডিউসারকে সবসময় পিওর বা বিশুদ্ধ ফাংশন হতে হয় যাতে স্টেট পরিবর্তন অনুমানযোগ্য হয়।*
3.  **রিডিউসারের ইনপুট প্যারামিটার দুটি কী কী?**
    a) State and Selector
    b) Action and Store
    c) State and Action
    d) Dispatch and State
    *উত্তর: c) State and Action। ব্যাখ্যা: রিডিউসার ফাংশন বর্তমান স্টেট (state) এবং প্রেরিত অ্যাকশন (action) অবজেক্ট ইনপুট হিসেবে নেয়।*
4.  **Provider ব্যাকগ্রাউন্ডে রিঅ্যাক্টের কোন মেকানিজমটি ব্যবহার করে?**
    a) Reconciliation
    b) Context API
    c) Portal
    d) Ref
    *উত্তর: b) Context API। ব্যাখ্যা: Provider অভ্যন্তরীণভাবে Context API ব্যবহার করে স্টোর ট্রির নিচে পাঠিয়ে দেয়।*
5.  **রিডিউসারের ভেতরে নিচের কোনটি করা সম্পূর্ণ নিষিদ্ধ?**
    a) নতুন স্টেট রিটার্ন করা
    b) এপিআই (API) রিকোয়েস্ট পাঠানো
    c) অ্যাকশন টাইপ চেক করা
    d) সুইচ স্টেটমেন্ট ব্যবহার করা
    *উত্তর: b) এপিআই (API) রিকোয়েস্ট পাঠানো। ব্যাখ্যা: এপিআই রিকোয়েস্ট হলো একটি সাইড-ইফেক্ট, যা রিডিউসারের পিওরিটি নষ্ট করে। এটি থাঙ্ক বা মিডলওয়্যারে করা উচিত।*

---

### 17. 5 Coding Exercises
1.  **Task:** একটি সিম্পল রিডিউসার লিখুন যা `'todo/add'` অ্যাকশন টাইপ রিসিভ করলে স্টেটের `list` অ্যারেতে একটি নতুন টাস্ক যোগ করবে।
    *Hint:* `return { ...state, list: [...state.list, action.payload] }` ব্যবহার করুন।
2.  **Task:** একটি রিঅ্যাক্ট অ্যাপ্লিকেশনের `index.js` ফাইলে স্টোর তৈরি করে সেটি `Provider` দিয়ে কানেক্ট করার কোড লিখুন।
3.  **Task:** এমন একটি রিডিউসার লিখুন যা ইউজারের প্রোফাইল পিকচার রিসেট করার অ্যাকশন হ্যান্ডেল করবে।
4.  **Task:** একটি সুইচ কেস ছাড়া শুধুমাত্র `if/else` ব্যবহার করে একটি ভ্যালিড রেডাক্স রিডিউসার তৈরি করুন।
5.  **Task:** দুটি আলাদা রিডিউসার (`cartReducer` এবং `userReducer`) কে `configureStore` এর মাধ্যমে একত্রিত করার কোড লিখুন।

---
---

## Topic 5: What is the difference between useDispatch() and dispatch()?

### 1. Simple Definition (বাংলায়)
`dispatch` এবং `useDispatch` এর মধ্যে মূল পার্থক্য হলো:
*   **dispatch**: এটি রেডাক্স স্টোরের একটি মেথড যা কোনো অ্যাকশনকে স্টোরে পাঠানোর (বা ডিসপ্যাচ করার) জন্য ব্যবহৃত হয়, যাতে রিডিউসার সেই অনুযায়ী স্টেট আপডেট করতে পারে।
*   **useDispatch**: এটি React-Redux লাইব্রেরির একটি হুক (Hook) যা রিঅ্যাক্ট ফাংশনাল কম্পোনেন্টের ভেতরে স্টোরের সেই `dispatch` মেথডের অ্যাক্সেস পাওয়ার জন্য ব্যবহৃত হয়।

---

### 2. Why This Concept Exists
রেডাক্সের কোর আর্কিটেকচারে অ্যাকশন ট্রিগার করতে হলে `store.dispatch(action)` কল করতে হয়। কিন্তু রিঅ্যাক্ট অ্যাপ্লিকেশনে সরাসরি গ্লোবাল `store` অবজেক্ট ইমপোর্ট করে কাজ করা ভালো প্র্যাকটিস নয়, কারণ এটি টেস্টিং করা কঠিন করে এবং সার্ভার সাইড রেন্ডারিং (SSR) এ সমস্যা তৈরি করে। রিঅ্যাক্ট কম্পোনেন্টের ভেতরে স্টোরের ডিসপ্যাচ মেথডটি নিরাপদে ও সহজে পাওয়ার জন্য `useDispatch` হুকটি তৈরি করা হয়েছে।

---

### 3. What Problem It Solves
*   **গ্লোবাল স্টেট কাপলিং এড়ানো:** কম্পোনেন্টগুলোকে সরাসরি গ্লোবাল স্টোর অবজেক্টের ওপর নির্ভরশীল হতে দেয় না।
*   **ফাংশনাল হুক আর্কিটেকচার:** রিঅ্যাক্ট ফাংশনাল কম্পোনেন্টের স্ট্যান্ডার্ড হুক প্যাটার্নের সাথে সামঞ্জস্য বজায় রাখে।
*   **টেস্টেবল কোড:** টেস্ট করার সময় মক (Mock) ডিসপ্যাচ ব্যবহার করা সহজ করে তোলে।

---

### 4. Real-life Analogy
*   **dispatch (চিঠি পাঠানোর ডাকবাক্স বা মেলবক্স):** এটি হলো সেই ডাকবাক্স যেখানে আপনি চিঠি ফেললে তা গন্তব্যে পৌঁছায়। অর্থাৎ অ্যাকশন স্টোরে পৌঁছায়।
*   **useDispatch (ডাকবাক্সের চাবি বা ডাকপিয়ন):** এটি হলো সেই চাবি বা মাধ্যম যা রিঅ্যাক্ট আপনাকে দেয় যাতে আপনি আপনার ঘরের (Component) ভেতরে বসেই ডাকবাক্সে অ্যাক্সেস পেতে পারেন। হুকটি কল করে আপনি চাবিটি নিজের কাছে এনে রাখেন, তারপর সেই চাবি ব্যবহার করে মেইলবক্সে অ্যাকশন পাঠান।

---

### 5. How Redux/React Works Internally
1.  যখন রিঅ্যাক্ট অ্যাপে `useDispatch()` কল করা হয়, তখন এটি রিঅ্যাক্ট কনটেক্সট (যা `Provider` সেট করেছে) থেকে বর্তমান রেডাক্স স্টোর অবজেক্টটি খুঁজে নেয়।
2.  এরপর এটি স্টোরের নিজস্ব `store.dispatch` মেথডটির রেফারেন্স রিটার্ন করে।
3.  React-Redux গ্যারান্টি দেয় যে, `useDispatch` হুক দ্বারা রিটার্ন করা `dispatch` ফাংশনটির রেফারেন্স সম্পূর্ণ স্ট্যাবল (Stable)। অর্থাৎ কম্পোনেন্ট বারবার রি-রেন্ডার হলেও এই ফাংশনটির মেমোরি অ্যাড্রেস বা রেফারেন্স পরিবর্তিত হয় না।
4.  তাই একে অন্য কোনো হুকের (যেমন- `useEffect` বা `useCallback`) ডিপেন্ডেন্সি অ্যারেতে দিলেও তা কোনো রি-রান বা অতিরিক্ত অ্যাকশন ট্রিগার করে না।

---

### 6. Basic Example (English Code)
```javascript
import React from 'react';
import { useDispatch } from 'react-redux';
import { increment } from './counterSlice';

function CounterButton() {
  // 1. Get the dispatch function using the hook
  const dispatch = useDispatch();

  return (
    // 2. Execute the dispatch method with an action creator
    <button onClick={() => dispatch(increment())}>
      Increment Count
    </button>
  );
}

export default CounterButton;
```

---

### 7. Step-by-step Explanation of the Code
*   `import { useDispatch }` এর সাহায্যে React-Redux থেকে হুকটি আনা হয়েছে।
*   কম্পোনেন্টের ভেতরে `const dispatch = useDispatch()` কল করে স্টোরের ডিসপ্যাচ মেথডটি `dispatch` নামক কনস্ট্যান্টে স্টোর করা হয়েছে।
*   বাটনের `onClick` ইভেন্টে `dispatch(increment())` কল করা হয়েছে। এখানে `increment()` অ্যাকশন ক্রিয়েটরটি রান হয়ে একটি অ্যাকশন অবজেক্ট তৈরি করে এবং `dispatch` সেটি স্টোরে পাঠিয়ে দেয়।

---

### 8. Another Real-world Example (English Code)
**Direct Dispatch in Raw JS vs useDispatch in React:**

*Raw JavaScript File (No React, No Hooks):*
```javascript
import { configureStore, createSlice } from '@reduxjs/toolkit';

const authSlice = createSlice({
  name: 'auth',
  initialState: { user: null },
  reducers: {
    setUser: (state, action) => { state.user = action.payload; }
  }
});

const store = configureStore({ reducer: { auth: authSlice.reducer } });

// Direct dispatch using the store object method
store.dispatch(authSlice.actions.setUser('Rohit')); 
```

*React Functional Component (Using Hook):*
```javascript
import React from 'react';
import { useDispatch } from 'react-redux';
import { setUser } from './authSlice';

export function LoginButton() {
  const dispatch = useDispatch(); // Hook usage

  return (
    <button onClick={() => dispatch(setUser('Rohit'))}>
      Login
    </button>
  );
}
```

---

### 9. Common Mistakes Beginners Make
*   **হুকের নিয়ম লঙ্ঘন করা:** রিঅ্যাক্ট কম্পোনেন্টের বাইরে (যেমন কোনো কাস্টম সাধারণ জাভাস্ক্রিপ্ট হেল্পার ফাংশনে) `useDispatch` হুক কল করার চেষ্টা করা। হুক কেবল রিঅ্যাক্ট ফাংশনাল কম্পোনেন্ট বা কাস্টম হুকের ভেতরেই কল করা সম্ভব।
*   **কন্ডিশনাল বা লুপে কল করা:** `if` কন্ডিশনের ভেতরে `useDispatch` কল করা, যা রিঅ্যাক্ট হুকের মৌলিক নিয়ম ভঙ্গ করে।
*   **অ্যাকশন প্যারেন্থেসিস মিস করা:** `dispatch(increment)` লিখে ফেলা। ব্র্যাকেট ছাড়া এটি অ্যাকশন ক্রিয়েটর ফাংশনটি নিজেই পাঠিয়ে দেয়, যা কাজ করবে না। অবশ্যই `dispatch(increment())` লিখতে হবে।

---

### 10. Interview Questions
1.  **Question:** What is the fundamental difference between `useDispatch` and `dispatch`?
    *   **Answer:** `useDispatch` is a React Hook provided by `react-redux` to obtain the dispatch function inside React components. `dispatch` is the actual method of the Redux store used to send actions.
2.  **Question:** Can we call `useDispatch` inside a regular utility JavaScript function?
    *   **Answer:** No. React hooks can only be called inside React functional components or other custom hooks. In utility functions, you must pass the `dispatch` function as an argument.
3.  **Question:** Does the `dispatch` function returned by `useDispatch` change between renders?
    *   **Answer:** No, the reference of the dispatch function is stable and guaranteed not to change across renders by React-Redux.
4.  **Question:** Why is it not recommended to import the `store` object directly and call `store.dispatch()` inside components?
    *   **Answer:** Direct imports make testing difficult because you cannot easily mock the store. It also causes issues in server-side rendered (SSR) applications where multiple users might share the same store instance.
5.  **Question:** How does Thunk middleware interact with the `dispatch` method?
    *   **Answer:** Normally, `dispatch` only accepts plain objects. Thunk middleware intercepts the dispatch and allows it to accept functions (asynchronous actions), executing them and passing the `dispatch` method as their first argument.

---

### 11. Best Practices
*   সবসময় রিঅ্যাক্ট কম্পোনেন্টের শুরুতে `const dispatch = useDispatch()` ডিফাইন করে নিন।
*   যদি কোনো কাস্টম হ্যান্ডলার তৈরি করেন, তবে সেটির ভেতরে ইভেন্ট লজিক প্রসেস করার জন্য এটি ব্যবহার করুন।

---

### 12. Performance Considerations
*   যেহেতু `useDispatch` এর রিটার্ন করা ফাংশনের রেফারেন্স অপরিবর্তিত থাকে, তাই এটি ব্যবহারে অতিরিক্ত রি-রেন্ডার হওয়ার কোনো ঝুঁকি নেই।

---

### 13. When NOT to Use It
*   রিঅ্যাক্ট কম্পোনেন্টের বাইরে বা কোনো সাধারণ মিডলওয়্যারে `useDispatch` হুক ব্যবহার করা যাবে না। সেখানে সরাসরি প্যারামিটার হিসেবে পাস হওয়া `dispatch` বা স্টোর অবজেক্ট থেকে `store.dispatch` ব্যবহার করতে হবে।

---

### 14. Comparison with Similar Concepts
| Concept | useDispatch (Hook) | store.dispatch (Method) | useReducer's dispatch |
| :--- | :--- | :--- | :--- |
| **Origin** | React-Redux | Redux Core Store | React Core Hook |
| **Context** | React Functional Component | Any JS file | React Local Component |
| **Dependency** | Needs React `<Provider>` | None | None |

---

### 15. Summary (বাংলায়)
`useDispatch` হলো রিঅ্যাক্ট কম্পোনেন্টের জন্য তৈরি একটি হুক যা আমাদের রেডাক্সের `dispatch` ফাংশন ব্যবহার করার অনুমতি দেয়। আর `dispatch` হলো সেই মেথড যা স্টোরে অ্যাকশন পাঠিয়ে ডেটা পরিবর্তন বা আপডেট করতে সাহায্য করে।

---

### 16. 5 MCQ Questions with Explanations
1.  **`useDispatch` মূলত কী রিটার্ন করে?**
    a) রেডাক্স স্টেট অবজেক্ট
    b) স্টোরের ডিসপ্যাচ ফাংশন
    c) একটি নতুন স্লাইস
    d) এপিআই ডাটা
    *উত্তর: b) স্টোরের ডিসপ্যাচ ফাংশন। ব্যাখ্যা: useDispatch হুকটি রান করলে সেটি রেডাক্স স্টোরের dispatch মেথডের রেফারেন্স রিটার্ন করে।*
2.  **নিচের কোন স্থানে `useDispatch` হুক ব্যবহার করা অবৈধ?**
    a) রিঅ্যাক্ট ফাংশনাল কম্পোনেন্ট
    b) রিঅ্যাক্ট কাস্টম হুক
    c) একটি সাধারণ জাভাস্ক্রিপ্ট হেল্পার ফাংশন (.js)
    d) ইভেন্ট হ্যান্ডলার ফাংশনের ভেতরে (যা কম্পোনেন্টে আছে)
    *উত্তর: c) একটি সাধারণ জাভাস্ক্রিপ্ট হেল্পার ফাংশন (.js)। ব্যাখ্যা: রিঅ্যাক্ট হুক কোনো নন-রিঅ্যাক্ট জাভাস্ক্রিপ্ট ফাংশনে ব্যবহার করা যায় না।*
3.  **`useDispatch` থেকে প্রাপ্ত `dispatch` ফাংশনের রেফারেন্সিয়াল স্ট্যাবিলিটি কেমন?**
    a) এটি প্রতি রেন্ডারে পরিবর্তিত হয়
    b) এটি কখনো পরিবর্তিত হয় না (Stable)
    c) এটি শুধুমাত্র স্টেট আপডেট হলে পরিবর্তিত হয়
    d) এটি ম্যানুয়ালি পরিবর্তন করতে হয়
    *উত্তর: b) এটি কখনো পরিবর্তিত হয় না (Stable)। ব্যাখ্যা: React-Redux নিশ্চিত করে যে এই ফাংশনের রেফারেন্স সবসময় এক থাকে।*
4.  **অ্যাকশন ডিসপ্যাচ করার সঠিক সিনট্যাক্স কোনটি?**
    a) `dispatch(increment)`
    b) `dispatch(increment())`
    c) `useDispatch(increment())`
    d) `store.useDispatch(increment)`
    *উত্তর: b) `dispatch(increment())`। ব্যাখ্যা: অ্যাকশন ক্রিয়েটর ফাংশনটি কল করে তারপর ডিসপ্যাচ করতে হয়।*
5.  **কোর রেডাক্স স্টোরে সরাসরি অ্যাকশন পাঠাতে নিচের কোনটি ব্যবহৃত হয়?**
    a) `store.useDispatch()`
    b) `store.dispatch()`
    c) `store.reducer()`
    d) `store.getState()`
    *উত্তর: b) `store.dispatch()`। ব্যাখ্যা: রিঅ্যাক্ট ছাড়া সাধারণ জাভাস্ক্রিপ্ট ফাইলে স্টোর অবজেক্টের সরাসরি মেথড store.dispatch() ব্যবহার করা হয়।*

---

### 17. 5 Coding Exercises
1.  **Task:** একটি রিঅ্যাক্ট বাটনে ক্লিক করলে `toggleTheme()` অ্যাকশন ডিসপ্যাচ করার জন্য `useDispatch` ব্যবহার করে একটি কম্পোনেন্ট তৈরি করুন।
    *Hint:* `const dispatch = useDispatch();` এবং `onClick={() => dispatch(toggleTheme())}` ব্যবহার করুন।
2.  **Task:** একটি ইনপুট ফিল্ড তৈরি করুন যেখানে ইউজার কিছু টাইপ করে সাবমিট করলে `useDispatch` এর মাধ্যমে `addTodo(text)` ডিসপ্যাচ হবে।
3.  **Task:** এমন একটি কাস্টম রিঅ্যাক্ট হুক `useAuthActions` লিখুন যা অভ্যন্তরীণভাবে `useDispatch` ব্যবহার করে `login` এবং `logout` অ্যাকশন দুটি ডিসপ্যাচ করার ফাংশন রিটার্ন করবে।
4.  **Task:** একটি সাধারণ জাভাস্ক্রিপ্ট ফাংশন লিখুন যা আর্গুমেন্ট হিসেবে `dispatch` গ্রহণ করবে এবং একটি এপিআই সাকসেস অ্যাকশন ডিসপ্যাচ করবে।
5.  **Task:** একটি কম্পোনেন্ট তৈরি করুন যা মাউন্ট হওয়ার সময় (`useEffect` এর মাধ্যমে) `fetchUserData()` নামক থাঙ্ক অ্যাকশন ডিসপ্যাচ করবে।
