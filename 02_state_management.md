# React Mastery: Part 2 - State Management Patterns

স্বাগতম! এই গাইডে আমরা React-এর দুটি অত্যন্ত গুরুত্বপূর্ণ স্টেট ম্যানেজমেন্ট প্যাটার্ন—**Lifting State Up** এবং **Controlled vs Uncontrolled Components** সম্পর্কে বিস্তারিত জানব।

---

## ১. Lifting State Up

### ১. Simple definition (বাংলায়)
Lifting State Up হলো এমন একটি পদ্ধতি যেখানে দুটি বা তার বেশি চাইল্ড কম্পোনেন্টের একই সাধারণ ডেটার প্রয়োজন হলে, সেই স্টেটটিকে তাদের নিজেদের মধ্যে না রেখে তাদের সরাসরি কমন প্যারেন্ট (Common Parent) কম্পোনেন্টে নিয়ে যাওয়া হয় এবং প্রপসের (Props) মাধ্যমে চাইল্ডদের কাছে পাঠানো হয়।

### ২. Why this concept exists
React-এ ডেটা ফ্লো একমুখী (Unidirectional Data Flow), অর্থাৎ ডেটা শুধুমাত্র উপর থেকে নিচের দিকে (Parent to Child) যেতে পারে। কোনো সিবলিং (sibling/পাশাপাশি থাকা) কম্পোনেন্ট সরাসরি একে অপরকে ডেটা পাঠাতে পারে না। তাই যখন তাদের একই ডেটা শেয়ার বা সিঙ্ক (sync) করার দরকার হয়, তখন স্টেটটিকে তাদের উপরে কমন প্যারেন্টে তুলতে হয়।

### ৩. What problem it solves
যদি প্রতিটি চাইল্ডের নিজস্ব আলাদা স্টেট থাকত, তবে তাদের ডেটা সিঙ্ক করা অত্যন্ত জটিল হয়ে যেত। একটি চাইল্ডে কোনো পরিবর্তন হলে অন্য চাইল্ড তা জানতে পারত না, ফলে অ্যাপ্লিকেশনে ইনকনসিস্টেন্ট (inconsistent) ডেটা দেখা যেত। Lifting State Up ডেটার "Single Source of Truth" (একক সত্যের উৎস) নিশ্চিত করে এই সমস্যার সমাধান করে।

### ৪. Real-life analogy
একটি যৌথ পরিবারের কথা চিন্তা করুন যেখানে দুই ভাই (Sibling Components) আলাদা আলাদা রুমে থাকে। তাদের বাবা-মা (Common Parent) ড্রয়িং রুমে একটি এসি (Air Conditioner) লাগিয়েছেন এবং সেটার রিমোটও ড্রয়িং রুমে রেখেছেন। এখন দুই ভাই যদি এসির টেম্পারেচার দেখতে বা চেঞ্জ করতে চায়, তবে তারা ড্রয়িংルームের কমন স্ট্যাটাস দেখে এবং রিমোট দিয়ে পরিবর্তন করে। তাপমাত্রা বাড়ালে বা কমালে দুই ভাই-ই সেটা দেখতে পারে কারণ তাপমাত্রা নিয়ন্ত্রণ করার বিষয়টি সবার উপরে কমন স্থানে (Parent) রাখা হয়েছে।

### ৫. How React works internally regarding this concept
যখন আমরা স্টেটটিকে প্যারেন্ট কম্পোনেন্টে লিফট করি:
1. প্যারেন্ট কম্পোনেন্টে `useState` ডিফাইন করা হয়।
2. প্যারেন্ট থেকে চাইল্ড কম্পোনেন্টে স্টেট ভ্যালু (যেমন: `temp`) এবং স্টেট আপডেট করার হ্যান্ডলার ফাংশন (যেমন: `setTemp` বা `handleTempChange`) প্রপস হিসেবে পাঠানো হয়।
3. চাইল্ড কম্পোনেন্টে কোনো ইভেন্ট ঘটলে তা প্রপসের ফাংশনটিকে ট্রিগার করে।
4. এর ফলে প্যারেন্ট কম্পোনেন্টের স্টেট আপডেট হয়, যা প্যারেন্ট এবং তার চাইল্ড কম্পোনেন্টগুলোকে রি-রেন্ডার করে সম্পূর্ণ সাব-ট্রিকে সিঙ্কে নিয়ে আসে।

### ৬. Basic example (Temperature Converter - Celsius & Fahrenheit)
```jsx
import React, { useState } from 'react';

// Child Component 1
function TemperatureInput({ scale, temperature, onTemperatureChange }) {
  return (
    <fieldset>
      <legend>Enter temperature in {scale}:</legend>
      <input
        value={temperature}
        onChange={(e) => onTemperatureChange(e.target.value)}
      />
    </fieldset>
  );
}

// Parent Component
function Calculator() {
  const [temperature, setTemperature] = useState('');

  return (
    <div>
      <TemperatureInput
        scale="Celsius"
        temperature={temperature}
        onTemperatureChange={setTemperature}
      />
      <TemperatureInput
        scale="Fahrenheit"
        temperature={temperature}
        onTemperatureChange={setTemperature}
      />
    </div>
  );
}

export default Calculator;
```

### ৭. Step-by-step explanation of the code
* `Calculator` প্যারেন্ট কম্পোনেন্টটি `temperature` স্টেটটিকে নিজের কাছে রেখেছে।
* এটি দুটি `TemperatureInput` চাইল্ড তৈরি করেছে এবং উভয়কে একই `temperature` স্টেট এবং `setTemperature` আপডেট ফাংশনটি প্রপস (`temperature`, `onTemperatureChange`) হিসেবে পাস করেছে।
* যেকোনো একটি ইনপুট বক্সে টাইপ করলে `onTemperatureChange` অর্থাৎ প্যারেন্টের `setTemperature` ফাংশনটি কল হবে।
* প্যারেন্টের স্টেট চেঞ্জ হওয়া মাত্রই দুটি ইনপুট চাইল্ডই নতুন ভ্যালু দিয়ে সিঙ্কড হয়ে রেন্ডার হবে।

### ৮. Another real-world example (Cart Summary and Products)
```jsx
import React, { useState } from 'react';

// Sibling 1
function ProductList({ onAddToCart }) {
  const products = [
    { id: 1, name: 'Shoes', price: 50 },
    { id: 2, name: 'Bag', price: 30 }
  ];

  return (
    <div>
      <h3>Products</h3>
      {products.map(p => (
        <div key={p.id}>
          {p.name} - ${p.price}
          <button onClick={() => onAddToCart(p)}>Add to Cart</button>
        </div>
      ))}
    </div>
  );
}

// Sibling 2
function Cart({ cartItems }) {
  const total = cartItems.reduce((sum, item) => sum + item.price, 0);
  return (
    <div>
      <h3>Cart ({cartItems.length} items)</h3>
      <p>Total Price: ${total}</p>
    </div>
  );
}

// Parent
function Store() {
  const [cart, setCart] = useState([]);

  const handleAddToCart = (product) => {
    setCart([...cart, product]);
  };

  return (
    <div style={{ display: 'flex', gap: '50px' }}>
      <ProductList onAddToCart={handleAddToCart} />
      <Cart cartItems={cart} />
    </div>
  );
}
```

### ৯. Common mistakes beginners make
* **প্রপস সরাসরি মিউট করা:** চাইল্ডের ভেতর থেকে `props.temperature = value` করার চেষ্টা করা, যা কাজ করবে না এবং এরর ছুড়ে দেবে।
* **স্টেট ডুপ্লিকেশন:** প্যারেন্টেও স্টেট রাখা এবং একই সাথে চাইল্ডের লোকাল স্টেটেও তা কপি করে রাখা। এর ফলে সিঙ্ক নষ্ট হয়।
* **অতিরিক্ত ওপরে স্টেট লিফট করা:** দুটি কাছাকাছি চাইল্ডের জন্য পুরো অ্যাপের একদম রুট লেভেলে (যেমন `App` কম্পোনেন্টে) স্টেট তুলে ফেলা, যা অপ্রয়োজনীয় রি-রেন্ডার ঘটায়।

### ১০. Interview questions related to this topic
1. **Lifting State Up বলতে কী বোঝায়?**
   * উত্তর: সিবলিং কম্পোনেন্টগুলোর মধ্যে ডেটা শেয়ার করার জন্য তাদের স্টেটকে কমন প্যারেন্ট কম্পোনেন্টে নিয়ে যাওয়া এবং প্রপসের সাহায্যে একমুখী ডেটা ফ্লো বজায় রাখা।
2. **যদি দুইয়ের অধিক নেস্টেড লেভেলের নিচে স্টেট পাস করতে হয়, তবে কি Lifting State Up ভালো উপায়?**
   * উত্তর: না। অতিরিক্ত নেস্টেড লেভেলে প্রপস পাস করাকে Prop Drilling বলে যা মেইনটেইন করা কঠিন। সেক্ষেত্রে Context API বা Redux ব্যবহার করা ভালো।
3. **প্যারেন্ট থেকে চাইল্ডে ডেটা আপডেট ট্রিগার করার প্রসেসটি কী?**
   * উত্তর: প্যারেন্ট থেকে চাইল্ডে প্রপ হিসেবে একটি কলব্যাক ফাংশন (Callback function) পাস করতে হয়। চাইল্ডে কোনো ইন্টারঅ্যাকশন হলে সেই কলব্যাকটি কল করে ডেটা প্যারেন্টে পাঠানো হয়।

### ১১. Best practices
* স্টেটকে সবসময় তার নিকটতম কমন প্যারেন্টে (Closest Common Ancestor) লিফট করুন।
* চাইল্ড কম্পোনেন্টকে যতটা সম্ভব প্রেজেন্টেশনাল (Presentational) বা ডাম্ব (Dumb) রাখুন, অর্থাৎ সে কেবল প্রপস নেবে এবং দেখাবে, ডিসিশন নেবে প্যারেন্ট।

### ১২. Performance considerations
স্টেট ওপরে লিফট করার কারণে প্যারেন্ট রি-রেন্ডার হলে তার সব চাইল্ডও রি-রেন্ডার হয়। যদি কোনো চাইল্ডের প্রপস পরিবর্তন না হয়ে থাকে, তবে তাকে `React.memo` দিয়ে র্যাপ করে অপ্রয়োজনীয় রি-রেন্ডার বন্ধ করা যায়।

### ১৩. When NOT to use it
যদি কোনো স্টেট শুধুমাত্র একটি কম্পোনেন্টের ভেতরেই ইন্টারনাল কাজের জন্য লাগে (যেমন একটি ড্রপডাউন ওপেন আছে কিনা), তা কখনোই ওপরে লিফট করবেন না।

### ১৪. Comparison with similar concepts
* **Lifting State Up vs Context API:** Lifting State Up ভালো যখন চাইল্ডগুলো কাছাকাছি থাকে এবং ডেটা ফ্লো সহজ থাকে। Context API ভালো যখন গ্লোবাল ডেটা (যেমন থিম বা ইউজার অথরাইজেশন) অনেক গভীরে থাকা কম্পোনেন্টগুলোর প্রয়োজন হয়।

### ১৫. Summary in simple Bangla
Lifting State Up হলো একাধিক চাইল্ডের শেয়ার্ড ডেটাকে তাদের কমন প্যারেন্টে রেখে প্রপসের মাধ্যমে সবাইকে একই সাথে আপডেট রাখা।

### ১৬. 5 MCQ questions
1. React-এ সিবলিং কম্পোনেন্টগুলো কীভাবে সরাসরি একে অপরের সাথে ডেটা শেয়ার করে?
   * A) Direct memory access
   * B) Context API ছাড়া সরাসরি পারে না, Lifting state up করতে হয়
   * C) props.sibling দিয়ে
   * D) window.state দিয়ে
   * *উত্তর: B*
2. Lifting State Up মূলত কী নিশ্চিত করে?
   * A) Multi-directional flow
   * B) Two-way data binding
   * C) Single Source of Truth (একক সত্যের উৎস)
   * D) Global Routing
   * *উত্তর: C*
3. স্টেট ওপরে তোলার পর চাইল্ড থেকে প্যারেন্ট স্টেট কীভাবে আপডেট করা হয়?
   * A) চাইল্ড সরাসরি প্যারেন্টের স্টেট ওভাররাইট করে
   * B) প্যারেন্ট চাইল্ডকে একটি কলব্যাক ফাংশন প্রপ হিসেবে দেয়
   * C) চাইল্ড ইভেন্ট এমিট করে উইন্ডো লেভেলে
   * D) কোনোভাবেই সম্ভব নয়
   * *উত্তর: B*
4. স্টেটকে কোন প্যারেন্ট পর্যন্ত লিফট করা উচিত?
   * A) একদম রুট `App` কম্পোনেন্ট পর্যন্ত
   * B) নিকটতম কমন প্যারেন্ট (Closest Common Ancestor) পর্যন্ত
   * C) যেকোনো র্যান্ডম কম্পোনেন্টে
   * D) চাইল্ডের সাব-কম্পোনেন্টে
   * *উত্তর: B*
5. অতিরিক্ত ওপরে স্টেট লিফট করলে কী সমস্যা হতে পারে?
   * A) Props Drilling এবং অপ্রয়োজনীয় রি-রেন্ডারিং
   * B) মেমরি লিক
   * C) কম্পাইলার এরর
   * D) কোড রান হবে না
   * *উত্তর: A*

### ১৭. 5 Coding exercises
1. একটি পাসওয়ার্ড ফিল্ড ও কনফার্ম পাসওয়ার্ড ফিল্ড বানান। কমন প্যারেন্টে তাদের ভ্যালু সিঙ্ক করে দেখান যে তারা ম্যাচ করেছে কিনা।
2. একটি Accordion কম্পোনেন্ট তৈরি করুন যেখানে একাধিক AccordionItem চাইল্ড থাকবে। প্যারেন্টে স্টেট লিফট করে নিশ্চিত করুন যে একবারে কেবল একটি আইটেমই ওপেন থাকবে।
3. একটি সার্চবার (চাইল্ড ১) এবং একটি ডাটা টেবিল (চাইল্ড ২) তৈরি করুন। সার্চবারে টাইপ করলে প্যারেন্ট স্টেটের মাধ্যমে ডাটা টেবিলটি ফিল্টার করুন।
4. একটি সেটিংস প্যানেল বানান যেখানে দুটি সুইচ (ডার্ক মোড এবং নোটিফিকেশন) থাকবে। প্যারেন্ট কম্পোনেন্ট এই অপশনগুলো সিঙ্ক করে একটি স্ট্যাটাস মেসেজ দেখাবে।
5. একটি ইমেজ গ্যালারি তৈরি করুন যেখানে থাম্বনেইল লিস্ট (চাইল্ড ১) থেকে ইমেজে ক্লিক করলে বড় ইমেজ ভিউয়ার (চাইল্ড ২)-এ সেই ইমেজটি দেখাবে।

---

## ২. Controlled vs Uncontrolled Components

### ১. Simple definition (বাংলায়)
* **Controlled Component:** যে ফর্ম এলিমেন্টের (যেমন: `<input>`, `<textarea>`, `<select>`) ভ্যালু সম্পূর্ণভাবে React-এর স্টেট দ্বারা নিয়ন্ত্রিত হয়, তাকে Controlled Component বলে।
* **Uncontrolled Component:** যে ফর্ম এলিমেন্ট তার ভ্যালু নিজেই নিজের মেমরিতে (DOM-এর ভেতরে) ধরে রাখে এবং React স্টেট দিয়ে তা সরাসরি ট্র্যাক করে না, তাকে Uncontrolled Component বলে। এর ভ্যালু পাওয়ার জন্য DOM রেফ বা `useRef` ব্যবহার করা হয়।

### ২. Why this concept exists
HTML ফর্ম এলিমেন্টগুলো বাই-ডিফল্ট তাদের নিজস্ব ইন্টারনাল স্টেট বজায় রাখে। কিন্তু React-এর নীতি হলো সব স্টেট এক জায়গায় থাকবে। এই দুটি চিন্তাধারার মেলবন্ধন ঘটাতে এই দুটি ধারণার জন্ম হয়েছে।

### ৩. What problem it solves
* Controlled Component রিয়েল-টাইম ফর্ম ভ্যালিডেশন, ইনপুট ফিল্টারিং (যেমন টাইপ করার সময় শুধু নাম্বার অ্যালাউ করা) এবং কন্ডিশনাল বাটন সাবমিট সহজ করে দেয়।
* Uncontrolled Component বড় ও ট্র্যাডিশনাল ফর্মগুলোর ক্ষেত্রে কাজ সহজ করে যেখানে প্রতি ক্যারেক্টার টাইপিংয়ের জন্য রি-রেন্ডার করার প্রয়োজন নেই, কেবল সাবমিট করার সময় ভ্যালু পেলেই চলে।

### ৪. Real-life analogy
* **Controlled:** একটি ট্রামের (Tram) কথা ভাবুন। ট্রাম চালক (React State) যেভাবে ট্রামটিকে চালাবেন, ট্রামটি ঠিক সেভাবেই চলবে। এর নিজস্ব কোনো আলাদা অভিমুখ নেই।
* **Uncontrolled:** একটি সাধারণ সাইকেলের কথা ভাবুন। সাইকেল চালক যখন সাইকেল ব্রেক করবেন বা ডিরেকশন দেবেন কেবল তখনই ইন্টারঅ্যাকশন হবে, বাকি সময় সাইকেলের চাকা তার নিজস্ব গতিতে ও অবস্থানে ঘোরে।

### ৫. How React works internally regarding this concept
* **Controlled:** ইনপুটের `value` প্রপটি একটি React স্টেট ভ্যারিয়েবলের সাথে কানেক্ট থাকে। যখন ইউজার কিছু টাইপ করে, `onChange` ইভেন্ট ফায়ার হয় এবং React স্টেট আপডেট করে। স্টেট আপডেট হওয়ার কারণে কম্পোনেন্ট রি-রেন্ডার হয় এবং নতুন ভ্যালুটি ইনপুটের `value` হিসেবে পাস হয়। DOM সবসময় React স্টেটের নিয়ন্ত্রণে থাকে।
* **Uncontrolled:** ইনপুটের ভ্যালু DOM নোডের ভেতরেই সরাসরি স্টোরড থাকে। React কেবল `ref` (একটি রেফারেন্স অবজেক্ট) দিয়ে DOM নোডটিকে পয়েন্ট করে রাখে। যখন প্রয়োজন হয়, React সরাসরি DOM থেকে ভ্যালুটি রিড করে (`inputRef.current.value`).

### ৬. Basic example
**Controlled Component:**
```jsx
import React, { useState } from 'react';

function ControlledInput() {
  const [name, setName] = useState('');

  return (
    <div>
      <h3>Controlled Form</h3>
      <input 
        type="text" 
        value={name} 
        onChange={(e) => setName(e.target.value)} 
      />
      <p>Current Value: {name}</p>
    </div>
  );
}

export default ControlledInput;
```

**Uncontrolled Component:**
```jsx
import React, { useRef } from 'react';

function UncontrolledInput() {
  const inputRef = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    alert('Submitted Value: ' + inputRef.current.value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h3>Uncontrolled Form</h3>
      <input type="text" ref={inputRef} />
      <button type="submit">Submit</button>
    </form>
  );
}

export default UncontrolledInput;
```

### ৭. Step-by-step explanation of the code
* Controlled ইনপুটে `value={name}` এবং `onChange` ব্যবহারের মাধ্যমে প্রতিটি ক্যারেক্টার প্রেসের সাথে সাথে React স্টেটকে সিঙ্ক করা হচ্ছে।
* Uncontrolled ইনপুটে কোনো `value` বা `onChange` নেই। এখানে `ref={inputRef}` দিয়ে সরাসরি DOM নোডের রেফারেন্স নেওয়া হয়েছে এবং সাবমিটের সময় `inputRef.current.value` দিয়ে ডেটা অ্যাক্সেস করা হয়েছে।

### ৮. Another real-world example (Form Validation vs File Upload)
```jsx
// File input can only be Uncontrolled in React
import React, { useRef } from 'react';

function FileUpload() {
  const fileInputRef = useRef(null);

  const handleUpload = (e) => {
    e.preventDefault();
    const fileName = fileInputRef.current.files[0] 
      ? fileInputRef.current.files[0].name 
      : "No file selected";
    alert(`Uploading file: ${fileName}`);
  };

  return (
    <form onSubmit={handleUpload}>
      <input type="file" ref={fileInputRef} />
      <button type="submit">Upload</button>
    </form>
  );
}
```

### ৯. Common mistakes beginners make
* **value প্রপ দিয়ে onChange না দেওয়া:** Controlled ইনপুটে `value` প্রপ দিলে কিন্তু `onChange` হ্যান্ডলার না দিলে ইনপুট বক্সটি লক হয়ে যায়, সেখানে কিছু টাইপ করা যায় না।
* **Undefined ভ্যালু দেওয়া:** ইনিশিয়াল স্টেট `undefined` রাখা (যেমন `const [val, setVal] = useState()`)। এর ফলে React কনসোলে ওয়ার্নিং দেয় যে আপনি আনকন্ট্রোলড কম্পোনেন্টকে কন্ট্রোলড করতে চাচ্ছেন। ইনিশিয়াল ভ্যালু সবসময় খালি স্ট্রিং `''` হওয়া উচিত।

### ১০. Interview questions related to this topic
1. **Controlled এবং Uncontrolled কম্পোনেন্টের প্রধান পার্থক্য কী?**
   * উত্তর: Controlled কম্পোনেন্ট তার ডেটা React স্টেটে রাখে এবং প্রতিটি কি-স্ট্রোকে রেন্ডার হয়। Uncontrolled কম্পোনেন্ট ডেটা DOM-এ রাখে এবং কোনো রি-রেন্ডার ছাড়াই সরাসরি `ref` দিয়ে ডেটা পড়া যায়।
2. **ফাইল ইনপুট (`<input type="file" />`) কি কন্ট্রোলড করা সম্ভব?**
   * উত্তর: না, ফাইল ইনপুট সবসময় Uncontrolled কারণ ব্রাউজারের সিকিউরিটি পলিসির কারণে ফাইল ডেটা React স্টেট দিয়ে প্রোগ্রামেটিক্যালি সেট করা যায় না, এটি রিড-অনলি।
3. **কখন কোনটি ব্যবহার করা উচিত?**
   * উত্তর: রিয়েল-টাইম ভ্যালিডেশন, ইনপুট ফরম্যাটিং, বা কন্ডিশনাল বাটনের জন্য Controlled ব্যবহার করা উচিত। খুব সাধারণ ফর্ম, থার্ড-পার্টি নন-React লাইব্রেরি ইন্টিগ্রেশন বা ফাইল আপলোডের জন্য Uncontrolled ব্যবহার করা সুবিধাজনক।

### ১১. Best practices
* অধিকাংশ ক্ষেত্রে Controlled Component ব্যবহার করা উচিত কারণ এটি React-এর প্যাটার্ন মেনে চলে।
* ইনপুট স্টেটের ইনিশিয়াল ভ্যালু কখনো `null` বা `undefined` রাখবেন না, সবসময় `''` (খালি স্ট্রিং) ব্যবহার করবেন।
* যদি আনকন্ট্রোলড কম্পোনেন্টে ডিফল্ট ভ্যালু দিতে চান, তবে `value` প্রপের বদলে `defaultValue` ব্যবহার করুন।

### ১২. Performance considerations
Controlled কম্পোনেন্টে প্রতি কি-স্ট্রোকে রি-রেন্ডার হয়। ফর্ম যদি অনেক বড় হয় (যেমন ১০০টি ইনপুট ফিল্ড), তবে কি-স্ট্রোকে পারফরম্যান্স কিছুটা ড্রপ করতে পারে। সেক্ষেত্রে Uncontrolled কম্পোনেন্ট অথবা `React-Hook-Form` এর মতো লাইব্রেরি ব্যবহার করা অত্যন্ত কার্যকরী।

### ১৩. When NOT to use it
যদি পারফরম্যান্সের কারণে প্রতি কি-স্ট্রোকে রি-রেন্ডার এড়াতে চান, তবে Controlled এভয়েড করে Uncontrolled ব্যবহার করুন।

### ১৪. Comparison with similar concepts
* **Controlled vs Uncontrolled:** Controlled-এ "React state is the source of truth", Uncontrolled-এ "DOM is the source of truth"।

### ১৫. Summary in simple Bangla
Controlled কম্পোনেন্ট হলো যেগুলোর ইনপুট ভ্যালু React স্টেট দিয়ে কন্ট্রোল করা হয়। Uncontrolled কম্পোনেন্ট হলো যেগুলোর ইনপুট ভ্যালু সরাসরি DOM থেকে `useRef` দিয়ে রিড করা হয়।

### ১৬. 5 MCQ questions
1. Controlled Component-এ ইনপুটের ভ্যালু কোথা থেকে আসে?
   * A) ব্রাউজার মেমরি
   * B) DOM নোড
   * C) React State
   * D) LocalStorage
   * *উত্তর: C*
2. React-এ ফাইল আপলোড ইনপুট (`<input type="file" />`) সবসময় কেমন হয়?
   * A) Controlled
   * B) Uncontrolled
   * C) Higher-order
   * D) Virtualized
   * *উত্তর: B*
3. Uncontrolled Component-এ ইনিশিয়াল ভ্যালু দেওয়ার জন্য কোন প্রপটি ব্যবহার করা উচিত?
   * A) value
   * B) initValue
   * C) defaultValue
   * D) defaultText
   * *উত্তর: C*
4. Controlled ইনপুটে `value` প্রপ দিয়ে `onChange` না দিলে কী হবে?
   * A) এরর দিয়ে পেজ ক্র্যাশ করবে
   * B) ইনপুট বক্সটি লক হয়ে যাবে (টাইপ করা যাবে না)
   * C) ইনপুটটি আনকন্ট্রোলড হয়ে যাবে
   * D) কিছুই হবে না
   * *উত্তর: B*
5. Uncontrolled কম্পোনেন্ট থেকে ভ্যালু পাওয়ার জন্য React-এর কোন হুক ব্যবহার করা হয়?
   * A) useState
   * B) useEffect
   * C) useRef
   * D) useMemo
   * *উত্তর: C*

### ১৭. 5 Coding exercises
1. একটি Controlled Form তৈরি করুন যা রিয়েল-টাইমে পাসওয়ার্ডের লেন্থ চেক করে ৮ ক্যারেক্টারের কম হলে একটি লাল মেসেজ দেখাবে।
2. একটি Uncontrolled Form তৈরি করুন যাতে ৩টি ইনপুট ফিল্ড থাকবে এবং সাবমিট বাটনে ক্লিক করলে সমস্ত ডেটা একটি অবজেক্ট আকারে অ্যালার্ট করবে।
3. একটি Controlled Dropdown (`<select>`) তৈরি করুন। ড্রপডাউন থেকে সিলেক্ট করা অপশন অনুযায়ী নিচের টেক্সটের কালার পরিবর্তন করুন।
4. একটি Controlled Input ফিল্ড তৈরি করুন যা ইউজারকে শুধুমাত্র সংখ্যা (digits) টাইপ করতে দেবে, কোনো টেক্সট বা স্পেশাল ক্যারেক্টার টাইপ করতে দেবে না।
5. একটি সাইন-আপ ফর্ম তৈরি করুন যেখানে Controlled ইনপুট ব্যবহার করে নিশ্চিত করবেন যে "Submit" বাটনটি তখনই একটিভ হবে যখন ইমেইল ও পাসওয়ার্ড উভয় ফিল্ডেই ভ্যালু থাকবে।
