# React.js Developer (Simbanic Software Services Role) Interview Questions & Answers

This guide contains 16 detailed, scenario-based interview questions tailored specifically to your experience as a **React.js Developer at Simbanic Software Services**. It covers key achievements such as shipping 3 production apps, boosting user retention by 25%, achieving 60 FPS rendering, reducing bundle size by 30%, enforcing Zod & React Hook Form security/validation, AI integrations, backend API performance, high-traffic management, HackerRank Top 1% React Certification, and deployments on VPS servers and AWS. Each question includes a comprehensive technical answer in English and a complete Bangla translation.

---

## Table of Contents
1. Shipping 3 Production React Apps & Increasing User Retention by 25%
2. Mentoring Junior Developers on Zustand & Clean Code Standards
3. Reducing Initial Bundle Size by 30% using `React.lazy()` & Code-Splitting
4. Achieving 60 FPS Rendering using Zustand Shallow Store Selectors
5. Optimizing Framer Motion Animations without Layout Thrashing
6. Form Management & Schema Validation with React Hook Form & Zod
7. Reinforcing Frontend Security: XSS Prevention & Secure External Navigation
8. Frontend AI Feature Integration (Connecting AI Services in React)
9. State Management Choice: Why Zustand over Redux/Context & Re-render Control
10. Backend API Integration & Performance Optimization (Eliminating Waterfalls)
11. High-Traffic Management & Frontend Resilience (Debouncing, Throttling & Optimistic UI)
12. Deploying React Applications to a VPS Server using Nginx & SSL
13. Deploying High-Performance React Apps on AWS (S3 + CloudFront CDN + Route 53)
14. Automating CI/CD Pipelines for React Deployments (GitHub Actions)
15. Cross-Functional QA Collaboration & Ensuring Zero-Regression Releases
16. HackerRank Top 1% React Certification & Advanced Frontend Assessment Mastery

---

### **Q1: As a React.js Developer at Simbanic, how did you collaborate with cross-functional product and QA teams to ship 3 production apps and increase user retention by 25%? / Simbanic-এ React.js ডেভেলপার হিসেবে প্রোডাক্ট ও QA টিমের সাথে একসাথে কাজ করে ৩টি প্রোডাকশন অ্যাপ রিলিজ দেওয়া এবং ইউজার রিটেনশন ২৫% বাড়ানোর অভিজ্ঞতাটি কীভাবে অর্জন করেছিলেন?**

**Answer (English):**
Shipping 3 production React.js applications successfully required structured collaboration and a focus on user experience (UX):
*   **Cross-Functional Alignment:** Worked in Agile sprints alongside Product Managers, UI/UX designers, and QA engineers. Participated in early feature breakdown sessions to align technical feasibility with product goals.
*   **UX & Performance Focus:** Improved retention by eliminating UI friction points. Identified drop-off pages using analytics, added smooth loading states (skeleton screens), optimized page load speed (sub-2s initial load), and ensured responsive mobile-first UI.
*   **QA & Quality Standards:** Established strict PR review standards, automated component testing using React Testing Library, and introduced staging preview environments for QA validation before every release.
*   **Result:** Reduced customer-reported bugs by 40% and delivered a fluid, bug-free experience that directly drove a 25% increase in 30-day user retention.

**অনুবাদ (Bangla Translation):**
প্রোডাক্ট ও QA টিমের সাথে সফলভাবে ৩টি অ্যাপ রিলিজ ও ২৫% রিটেনশন বাড়ানোর কৌশল:
*   **টিম সমন্বয়:** অ্যাজাইল (Agile) স্প্রিন্টে প্রোডাক্ট ম্যানেজার, ডিজাইনার ও টেস্টারের সাথে ফিচার ডিজাইনের শুরুতে কারিগরি দিক নির্ধারণ করা হতো।
*   **ইউজার রিটেনশন বৃদ্ধি:** পেজ লোডিং টাইম ২ সেকেন্ডের নিচে নামিয়ে আনা, স্কেলিটন স্ক্রিন (Skeleton screen) যোগ করা এবং মোবাইল রেসপনসিভনেস উন্নত করে ইউজারের ড্রপ-অফ পয়েন্ট কমানো হয়েছে।
*   **QA কোয়ালিটি:** PR রিভিউতে কঠোরতা, React Testing Library দিয়ে টেস্ট কেস এবং স্টেজিং সার্ভারে প্রিভিউ এনভায়রনমেন্ট তৈরি করা হয়েছিল।
*   **ফলাফল:** বাগ ৪০% কমে যায় এবং ব্যবহারকারীরা স্মুথ অভিজ্ঞতা পেয়ে ৩০-দিনের ইউজার রিটেনশন ২৫% বৃদ্ধি পায়।

---

### **Q2: How did you mentor junior developers on Zustand state management and clean code standards? / জুনিয়র ডেভেলপারদের Zustand স্টেট ম্যানেজমেন্ট এবং Clean Code স্ট্যান্ডার্ড নিয়ে কীভাবে মেন্টরিং করেছিলেন?**

**Answer (English):**
Mentoring junior engineers involves establishing clear architectural patterns and hands-on code reviews:
*   **Zustand Training:** Taught junior developers how Zustand simplifies state compared to Redux (no boilerplate actions/reducers). Guided them on creating modular stores (e.g., `useAuthStore`, `useCartStore`) and using **shallow selectors** (`useShallow`) to prevent unwanted component re-renders.
*   **Clean Code Guidelines:** Standardized project structure into modular folders (`components`, `hooks`, `services`, `types`, `utils`). Enforced SOLID principles, DRY (Don't Repeat Yourself), and small, single-responsibility functional components (<100 lines).
*   **Constructive Code Reviews:** Used GitHub PR reviews as a teaching tool, highlighting *why* a pattern (like extracting custom hooks or using Zod) was preferred rather than just requesting changes.

**অনুবাদ (Bangla Translation):**
জুনিয়রদের দক্ষ করে তোলার জন্য নেওয়া পদক্ষেপসমূহ:
*   **Zustand ট্রেনিং:** রেডাক্সের জটিলতা এড়িয়ে কীভাবে Zustand দিয়ে সহজে মডুলার স্টোর (`useAuthStore`) বানাতে হয় এবং `useShallow` দিয়ে অহেতুক রি-রেন্ডারিং বন্ধ করতে হয় তা শেখানো হয়েছে।
*   **Clean Code স্ট্যান্ডার্ড:** কোডের ফোল্ডার স্ট্রাকচার ঠিক করা, SOLID ও DRY নীতি মেনে ১০০ লাইনের নিচে সিঙ্গেল-রেসপন্সিবিলিটি কম্পোনেন্ট লেখার নিয়ম চালু করা হয়েছে।
*   **PR রিভিউ:** গিটহাবের PR রিভিউতে কেন কাস্টম হুক বা Zod ভ্যালিডেশন ব্যবহার করা ভালো তার ব্যাখ্যা দেওয়া হয়েছে।

---

### **Q3: How did you achieve a 30% reduction in initial bundle size using `React.lazy()` and code-splitting? / `React.lazy()` এবং কোড-স্প্লিটিং ব্যবহার করে প্রাথমিক বান্ডেল সাইজ (Bundle Size) ৩০% কমানোর কৌশলটি ব্যাখ্যা করুন।**

**Answer (English):**
Large single-page applications often suffer from slow initial load times due to massive JavaScript bundles.
*   **Bundle Analysis:** Used `webpack-bundle-analyzer` (or Vite `rollup-plugin-visualizer`) to identify large dependencies and route bundles.
*   **Route-Based Code Splitting:** Wrapped top-level route components with `React.lazy()` dynamic imports (e.g., `const Dashboard = React.lazy(() => import('./pages/Dashboard'))`) combined with `<React.Suspense fallback={<PageSpinner />}>`.
*   **Component-Level Lazy Loading:** Dynamically loaded heavy third-party modules (e.g., Chart.js, Rich Text Editors, Framer Motion, Modals) only when a user interacted with or scrolled to them.
*   **Tree Shaking & Dynamic Imports:** Replaced heavy libraries (like Moment.js with `date-fns` or native JS) and imported named exports dynamically.
*   **Result:** Reduced the main entry JavaScript bundle size from ~1.2MB to ~840KB (30% reduction), significantly improving First Contentful Paint (FCP).

**অনুবাদ (Bangla Translation):**
মেইন ফাইল সাইজ ৩০% কমিয়ে ওয়েবসাইট ফাস্ট করার পদ্ধতি:
*   **বান্ডেল অ্যানালাইসিস:** `webpack-bundle-analyzer` দিয়ে সবচেয়ে ভারী ফাইল ও ডিপেনডেন্সি খুঁজে বের করা হয়েছে।
*   **রাউট-বেসড কোড স্প্লিটিং:** প্রতিটি পেজের জন্য `React.lazy()` এবং `<React.Suspense>` দিয়ে ডায়নামিক ইমপোর্ট করা হয়েছে, যাতে ইউজার যে পেজে আছে কেবল সেই পেজের জাভাস্ক্রিপ্ট ডাউনলোড হয়।
*   **হেভি মডিউল লেজি লোডিং:** চার্ট (Chart.js) বা এডিটর ফাইলগুলো ইউজার যখন ক্লিকে বা স্ক্রলে মডাল খোলে তখন লোড করানো হয়েছে।
*   **ফলাফল:** মূল বান্ডেল ১.২MB থেকে কমে ৮৪০KB-তে নেমে আসে (৩০% হ্রাস) এবং পেজ লোড ফাস্ট হয়।

---

### **Q4: How did you achieve 60 FPS rendering performance using Zustand shallow store selectors? / Zustand-এর Shallow Store Selectors ব্যবহার করে ৬০ FPS রেন্ডারিং পারফরম্যান্স কীভাবে অর্জিত হয়েছিল?**

**Answer (English):**
By default, subscribing to a store object without selector optimization causes a component to re-render whenever *any* property inside the store mutates.
*   **The Problem:** In complex screens, updating an unrelated state property (e.g., user notification count) was triggering full tree re-renders of heavy list components, dropping frame rates to 30-40 FPS.
*   **Shallow Selectors Solution:** Implemented Zustand's `useShallow` comparator or targeted primitive selectors:
    ```typescript
    // Bad: Re-renders on any store change
    const { user, theme } = useUserStore();
    // Good: Subscribes ONLY to specific primitive values
    const user = useUserStore((state) => state.user);
    // Good: Uses useShallow for returning objects/arrays
    const { items, total } = useCartStore(useShallow((state) => ({ items: state.items, total: state.total })));
    ```
*   **Impact:** Isolated re-renders strictly to affected UI components, eliminating unnecessary DOM updates and locking layout performance to a silky-smooth 60 FPS.

**অনুবাদ (Bangla Translation):**
রেন্ডারিং স্পিড ৬০ FPS-এ লক করার উপায়:
*   **সমস্যা:** কোনো অপ্টিমাইজেশন ছাড়া Zustand স্টোর কল করলে স্টোরের যেকোনো প্রপার্টি পাল্টালে সম্পূর্ণ কম্পোনেন্ট রি-রেন্ডার হতো, ফলে রেন্ডারিং স্পিড কমে ৩০-৪০ FPS হয়ে যেত।
*   **Shallow Selector সমাধান:** `useShallow` এবং সুনির্দিষ্ট ফিল্ড সিলেক্টর ব্যবহার করা হয়েছে। এর ফলে স্টোরের অন্য উপাদান পাল্টালেও নির্দিষ্ট কম্পোনেন্টে অহেতুক রি-রেন্ডার হয় না।
*   **ফলাফল:** অপ্রয়োজনীয় ডম পরিবর্তন বন্ধ হয়ে রেন্ডারিং ৬০ FPS-এ স্থায়ী হয়।

---

### **Q5: How did you optimize Framer Motion animations to maintain 60 FPS without layout thrashing? / Framer Motion অ্যানিমেশন অপ্টিমাইজ করে লেআউট থ্র্যাশিং ছাড়া ৬০ FPS ধরে রাখার টেকনিকটি কী?**

**Answer (English):**
Framer Motion is powerful, but animating layout properties (like `width`, `height`, `top`, `margin`) triggers expensive browser Reflow/Repaint layout thrashing.
*   **GPU-Only Animation:** Restricted animations exclusively to GPU-accelerated CSS properties: `transform` (`scale`, `x`, `y`, `rotate`) and `opacity`.
*   **`layout` Prop & FLIP:** Used Framer Motion's `layout` prop for smooth list item transitions, which internally uses the FLIP (First, Last, Invert, Play) technique to calculate transforms without triggering layout re-calculations.
*   **`AnimatePresence` Optimization:** Ensured exiting list items were properly keyed and unmounted cleanly without memory leaks.
*   **Lazy Motion Component:** Wrapped animation trees in `<LazyMotion features={domAnimation}>` to dynamically load Framer Motion's animation features asynchronously, shaving ~30KB off the initial bundle.

**অনুবাদ (Bangla Translation):**
Framer Motion দিয়ে ৬০ FPS অ্যানিমেশন ধরে রাখার কৌশল:
*   **GPU-ভিত্তিক অ্যানিমেশন:** সিএসএস `width`, `height`, `margin` অ্যানিমেট না করে কেবল GPU সাপোর্ট দেওয়া `transform` (scale, x, y) এবং `opacity` ব্যবহার করা হয়েছে।
*   **FLIP লজিক:** তালিকায় উপাদান সরানোর সময় `layout` প্রপস ব্যবহার করা হয়েছে যা FLIP মেকানিজম মেনে ব্রাউজার রি-ফ্লো ছাড়াই অ্যানিমেশন দেখায়।
*   **Lazy Motion:** `<LazyMotion features={domAnimation}>` দিয়ে কেবল প্রয়োজনীয় অ্যানিমেশন কোড লোড করানো হয়েছে, যা ফাইল সাইজ ৩০KB কমিয়ে দেয়।

---

### **Q6: How did you implement form management and schema validation using React Hook Form and Zod? / React Hook Form এবং Zod ব্যবহার করে ফর্ম ম্যানেজমেন্ট এবং স্কিমা ভ্যালিডেশন কীভাবে ইমপ্লিমেন্ট করেছেন?**

**Answer (English):**
Combining React Hook Form (RHF) with Zod provides uncontrolled input efficiency with strict type-safe runtime validation:
*   **Why RHF + Zod:** Traditional controlled inputs re-render the entire component on every keystroke. RHF uses uncontrolled inputs via `ref`s, minimizing re-renders. Zod defines single-source-of-truth TypeScript schemas.
*   **Implementation:**
    ```typescript
    const loginSchema = z.object({
      email: z.string().email('Invalid email address'),
      password: z.string().min(8, 'Password must be at least 8 characters'),
    });
    type LoginFormValues = z.infer<typeof loginSchema>;

    const { register, handleSubmit, formState: { errors } } = useForm<LoginFormValues>({
      resolver: zodResolver(loginSchema),
      mode: 'onBlur',
    });
    ```
*   **Benefits:** Completely eliminated form re-render lag, provided instant inline error messages, and automatically inferred TypeScript types directly from validation schemas.

**অনুবাদ (Bangla Translation):**
React Hook Form এবং Zod-এর মাধ্যমে ফর্ম হ্যান্ডলিং:
*   **কেন এই কম্বিনেশন:** সাধারণ ইনপুটে প্রতি অক্ষরে ক্লিক করলে রিয়্যাক্ট রি-রেন্ডার হয়। RHF আনকন্ট্রোল্ড ইনপুট ও Ref ব্যবহার করায় রি-রেন্ডারিং হয় না। আর Zod টাইপ-সেফ ভ্যালিডেশন দেয়।
*   **বাস্তবায়ন:** `z.object()` দিয়ে স্কিমা ডিক্লেয়ার করে `zodResolver(schema)`-র মাধ্যমে `useForm`-এ কানেক্ট করা হয়।
*   **সুবিধা:** ইনপুট ল্যাগ দূর হয়, সাথে সাথে এরর মেসেজ দেখায় এবং টাইপস্ক্রিপ্ট টাইপ পেয়ে কোড এরর এড়ানো যায়।

---

### **Q7: How did you reinforce frontend security against XSS attacks and insecure external link navigation? / XSS অ্যাটাক প্রতিরোধ এবং বাহ্যিক লিংকের সুরক্ষায় ফ্রন্টএন্ড সিকিউরিটি কীভাবে জোরদার করেছিলেন?**

**Answer (English):**
Frontend security is essential for protecting user session data and preventing malicious code execution:
*   **XSS (Cross-Site Scripting) Prevention:** Avoided `dangerouslySetInnerHTML` across all components. When rendering user-generated rich text, passed the HTML through **DOMPurify** (`DOMPurify.sanitize(userContent)`) to strip malicious `<script>` tags and inline event handlers.
*   **Input Sanitization:** Used Zod schema validation to trim, sanitize, and validate all text fields before making API requests.
*   **Secure External Navigation:** Enforced strict rules for all external links (`<a href="..." target="_blank">`). Automatically appended `rel="noopener noreferrer"` to prevent **Tabnabbing attacks** (where the opened external page accesses `window.opener` to redirect the original tab to a phishing site).

**অনুবাদ (Bangla Translation):**
XSS অ্যাটাক ও সিকিউরিটি জোরদার করার পদক্ষেপসমূহ:
*   **XSS প্রতিরোধ:** `dangerouslySetInnerHTML` সরাসরি ব্যবহার না করে ইউজার কন্টেন্ট **DOMPurify** দিয়ে ফিল্টার (`DOMPurify.sanitize()`) করা হতো যাতে কোনো ক্ষতিকারক `<script>` ট্যাগ রান করতে না পারে।
*   **ইনপুট স্যানিটাইজেশন:** Zod স্কিমা দিয়ে এপিআইতে ডাটা পাঠানোর আগে ট্রিম ও ফিল্টার করা হতো।
*   **সিকিউর এক্সটার্নাল লিঙ্ক:** বাহিরের যেকোনো লিংকে (`target="_blank"`) বাধ্যতামূলকভাবে `rel="noopener noreferrer"` বসানো হতো যাতে **Tabnabbing** (যেখানে নতুন ট্যাব আগের ট্যাবের এক্সেস পেয়ে ভুয়া ফিফিং পেজে পাঠাতে পারে) ঠেকানো যায়।

---

### **Q8: What AI integration features did you build on the React frontend at Simbanic, and how did you connect them? / Simbanic-এ রিয়্যাক্ট ফ্রন্টএন্ডে আপনি কী কী AI ফিচার ইন্টিগ্রেট করেছিলেন এবং সেগুলো কীভাবে কানেক্ট করেছিলেন?**

**Answer (English):**
At Simbanic, I built interactive frontend interfaces that consumed AI services:
*   **AI Smart Suggestions & Auto-Complete:** Integrated real-time AI auto-suggestions in input forms and search bars. As users typed, requests were sent to the backend AI gateway (debounced by 300ms), and suggestions were rendered as an interactive dropdown.
*   **Streaming AI Chat Interface:** Built a responsive AI assistant widget. Used `fetch` with `ReadableStream` (or WebSockets) to stream text chunks from the Node.js backend. Updated a streaming buffer state to render a real-time typewriter effect.
*   **AI Match Feedback UI:** Designed visual match indicators (confidence score meters, recommendation reason tags) that displayed AI-generated dispatch scoring results clearly for end users.

**অনুবাদ (Bangla Translation):**
রিঅ্যাক্ট ফ্রন্টএন্ডে ইন্টিগ্রেট করা AI ফিচারসমূহ:
*   **AI অটো-সাজেশন:** ইনপুট ফর্মে টাইপ করার সময় ৩০০ms ডিবাউন্সড রিকোয়েস্টের মাধ্যমে AI সাজেশন ড্রপডাউন দেখানো।
*   **স্ট্রিমিং AI চ্যাট ইন্টারফেস:** AI চ্যাট উইজেট যেখানে `ReadableStream` বা WebSockets থেকে টোকেন নিয়ে টাইপরাইটার ইফেক্টের মতো রিয়েল-টাইম উত্তর প্রদর্শন।
*   **AI ম্যাচ ভিজ্যুয়ালাইজেশন:** AI-এর দেওয়া ম্যাচিং রেজাল্ট ও স্কোর দেখানোর জন্য গ্রাফিক্যাল মিটার ও ট্যাগ ডিজাইন।

---

### **Q9: Why did you choose Zustand over Redux or Context API at Simbanic, and how does it optimize re-renders? / Simbanic-এ Redux বা Context API-এর বদলে Zustand কেন বেছে নিয়েছিলেন এবং এটি কীভাবে রি-রেন্ডার অপ্টিমাইজ করে?**

**Answer (English):**
*   **Why Not Redux:** Redux requires significant boilerplate (actions, reducers, dispatch, slices), making codebase maintenance heavy for small-to-medium teams.
*   **Why Not Context API:** React Context re-renders **all** consuming components whenever any value in the provider object changes, causing major performance bottlenecks for frequently updating data.
*   **Why Zustand:**
    1.  Zero boilerplate—simple, readable store creation (`create()`).
    2.  Lives outside the React render tree (no Provider nesting required).
    3.  Native selector-based subscriptions: Components subscribe *only* to specific state slices, skipping re-renders completely when unrelated state changes.

**অনুবাদ (Bangla Translation):**
*   **Redux না নেওয়ার কারণ:** অতিরিক্ত বয়লারপ্লেট কোড (Actions, Reducers) যা প্রজেক্টের সাইজ বড় করে।
*   **Context API না নেওয়ার কারণ:** প্রোভাইডারের ভেতর সামান্য পরিবর্তন হলেও প্রোভাইডার ব্লকের **সমস্ত চাইল্ড** অহেতুক রি-রেন্ডার হয়।
*   **Zustand নেওয়ার কারণ:** বয়লারপ্লেট নেই, প্রোভাইডার দিয়ে র্যাপ করতে হয় না এবং সিলেক্টিভ সাবস্ক্রিপশনের মাধ্যমে কেবল কাজের অংশটুকু পরিবর্তন হলে সংশ্লিষ্ট কম্পোনেন্ট রেন্ডার হয়।

---

### **Q10: How did you optimize frontend-backend API integration to reduce response times and prevent waterfall requests? / ফ্রন্টএন্ড-ব্যাকএন্ড এপিআই ইন্টিগ্রেশন অপ্টিমাইজ করতে এবং Waterfall Requests রোধ করতে কী করেছিলেন?**

**Answer (English):**
Waterfall requests (where Component B waits for Component A's API call to finish before fetching) degrade user experience.
*   **Parallel Fetching (`Promise.all`):** Combined independent data fetches into parallel requests (`await Promise.all([fetchUser(), fetchSettings()])`) on initial load.
*   **TanStack Query (React Query):** Implemented React Query for caching, deduplication of identical requests, and background revalidation (`staleTime` tuning).
*   **Prefetching on Hover:** Prefetched page data when users hovered over navigation links (`queryClient.prefetchQuery()`), resulting in near-instantaneous page transitions.
*   **Payload Minimization:** Requested only required JSON fields from the REST API rather than bloated payloads.

**অনুবাদ (Bangla Translation):**
এপিআই ওয়াটারফল (একটি এপিআই শেষ হওয়ার পর আরেকটি চালু হওয়া) ঠেকানোর পদ্ধতি:
*   **প্যারালাল ফেচিং (`Promise.all`):** স্বাধীন এপিআই রিকোয়েস্টগুলোকে `Promise.all` দিয়ে একসাথে একই সময়ে পাঠানো।
*   **TanStack Query (React Query):** ডাটা ক্যাশ করা, একই রিকোয়েস্ট বারবার যাওয়া বন্ধ করা এবং ব্যাকগ্রাউন্ডে অটো-সিঙ্ক করা।
*   **হোভারে প্রি-ফেচিং:** ইউজার নেভিগেশন বাটনে কার্সার বা মাউস নেওয়া মাত্রই রুট পরিবর্তন হওয়ার আগেই `prefetchQuery()` দিয়ে ডাটা আগে নামিয়ে রাখা।

---

### **Q11: How do you handle high-traffic spikes, fast user typing, and network latency on the React frontend? / রিয়্যাক্ট ফ্রন্টএন্ডে হাই-ট্রাফিক, দ্রুত টাইপিং এবং নেটওয়ার্ক ল্যাটেন্সি কীভাবে সামলাবেন?**

**Answer (English):**
1.  **Debouncing Input Handlers:** Used `useDebounce` (300ms) for search inputs to prevent spamming the backend API on every keystroke.
2.  **Throttling Event Listeners:** Throttled window resize, scroll, and mousemove listeners (`lodash.throttle`) to 60 FPS (~16ms).
3.  **Optimistic UI Updates:** Immediately updated UI state on user action (e.g., toggling a Like button or adding a cart item) before the API response returned, rolling back state if the network request failed.
4.  **Skeleton Loaders:** Displayed layout skeletons instead of blank spinners to reduce perceived latency.

**অনুবাদ (Bangla Translation):**
১. **ডিবাউন্সিং (Debouncing):** সার্চ বক্সে টাইপ করার সময় প্রতি অক্ষরে এপিআই রিকোয়েস্ট না পাঠিয়ে টাইপ থামার ৩০০ms পর রিকোয়েস্ট পাঠানো।
২. **থ্রটলিং (Throttling):** স্ক্রলিং বা উইন্ডো রিসাইজ ইভেন্ট থ্রটল করে ৬০ FPS-এ নিয়ন্ত্রণ রাখা।
৩. **Optimistic UI:** লাইক বাটনে চাপ দেওয়া মাত্রই ইউআই আপডেট করে দেওয়া (সার্ভার রেসপন্সের অপেক্ষা না করে), ফেল করলে আগের স্টেটে ফিরিয়ে আনা।
৪. **স্কেলিটন লোডার:** ফাঁকা পেজ না দেখিয়ে লেআউট স্কেলিটন বা শিমার ভিউ দেখানো।

---

### **Q12: How did you deploy React production applications to a Virtual Private Server (VPS) using Nginx and SSL? / Nginx এবং SSL ব্যবহার করে একটি VPS (Virtual Private Server)-এ কীভাবে React প্রোডাকশন অ্যাপ ডিপ্লয় করেছিলেন?**

**Answer (English):**
Deploying a single-page React app (SPA) to a Linux VPS (Ubuntu/Debian) involves building production assets and configuring Nginx as a reverse proxy:
*   **Build Production Bundle:** Ran `npm run build` to generate static HTML/CSS/JS files in the `dist` or `build` folder.
*   **Upload Files to VPS:** Transferred build files to the VPS directory (e.g., `/var/www/my-react-app`) via SCP/SFTP or Git pull.
*   **Configure Nginx:** Created an Nginx server block to serve static files and handle Client-Side Routing fallback (`try_files $uri $uri/ /index.html`):
    ```nginx
    server {
        listen 80;
        server_name myapp.com;
        root /var/www/my-react-app;
        index index.html;

        location / {
            try_files $uri $uri/ /index.html;
        }
    }
    ```
*   **Enable SSL (HTTPS):** Installed Let's Encrypt SSL certificate using Certbot (`sudo certbot --nginx -d myapp.com`), ensuring encrypted HTTPS communication.

**অনুবাদ (Bangla Translation):**
Linux VPS (Ubuntu)-এ Nginx দিয়ে React অ্যাপ ডিপ্লয় করার ধাপসমূহ:
*   **প্রোডাকশন বিল্ড:** `npm run build` চালিয়ে ফাইলগুলো `dist` ফোল্ডারে জেনারেট করা।
*   **VPS-এ ফাইল আপলোড:** SCP/Git দিয়ে ফাইলগুলো VPS-এর `/var/www/my-react-app`-এ পাঠানো।
*   **Nginx কনফিগারেশন:** Client-side routing রিফ্রেশ করলে যেন ৪০৪ এরর না আসে সে জন্য Nginx কনফিগারেশনে `try_files $uri $uri/ /index.html` সেট করা।
*   **SSL ইন্সটল:** Certbot দিয়ে বিনামূল্যের Let's Encrypt SSL সার্টিফিকেট ইন্সটল করে ওয়েবসাইট HTTPS সিকিউর করা।

---

### **Q13: How did you deploy and host high-performance React frontend applications on AWS (S3 + CloudFront CDN + Route 53)? / AWS-এ (S3 + CloudFront CDN + Route 53) ব্যবহার করে কীভাবে উচ্চ পারফরম্যান্সের React অ্যাপ ডিপ্লয় এবং হোস্ট করেছিলেন?**

**Answer (English):**
Hosting a static React SPA on AWS using S3 and CloudFront delivers ultra-low latency globally:
1.  **Amazon S3 Bucket:** Created a private S3 bucket and uploaded the production build files (`dist/`). Configured bucket policy to grant read access strictly via CloudFront Origin Access Control (OAC).
2.  **Amazon CloudFront CDN:** Created a CloudFront Distribution pointing to the S3 bucket origin.
    *   Enabled **Gzip/Brotli compression** for JS/CSS assets.
    *   Configured **Custom Error Responses**: Redirected 403/404 HTTP errors to `/index.html` with 200 HTTP status (essential for React Router client-side routing).
    *   Set up edge caching headers (`Cache-Control: max-age=31536000` for hashed assets).
3.  **Amazon Route 53 & ACM:** Pointed domain DNS records to CloudFront distribution using Route 53 Alias records, securing it with a free SSL certificate from AWS Certificate Manager (ACM).

**অনুবাদ (Bangla Translation):**
AWS-এ S3 ও CloudFront দিয়ে বিশ্বমানের দ্রুতগতির রিয়্যাক্ট অ্যাপ হোস্ট করার নিয়ম:
1.  **Amazon S3 Bucket:** একটি S3 বাকেট বানিয়ে প্রজেক্ট বিল্ড ফাইলগুলো আপলোড করা।
2.  **Amazon CloudFront CDN:** S3-এর সাথে কন্টেন্ট ডেলিভারি নেটওয়ার্ক (CloudFront) কানেক্ট করা। ৪০৪ এরর এলে যেন `/index.html`-এ রিডাইরেক্ট হয় তার Custom Error Rule বসানো (React Router চলাতে আবশ্যক)।
3.  **Amazon Route 53 & ACM:** ডোমেইন কানেক্ট করার জন্য Route 53 এবং বিনামূল্যে HTTPS এর জন্য AWS Certificate Manager (ACM) যুক্ত করা।

---

### **Q14: How did you set up automated CI/CD pipelines for building, testing, and deploying React apps? / React অ্যাপ অটোমেটিক বিল্ড, টেস্ট এবং ডিপ্লয় করার জন্য CI/CD পাইপলাইন (GitHub Actions) কীভাবে সেটআপ করেছিলেন?**

**Answer (English):**
Automating deployments using **GitHub Actions** ensures every code push to `main` is tested and deployed without manual human error:
*   **Workflow Trigger:** Configured `.github/workflows/deploy.yml` to trigger on push to `main` branch.
*   **Pipeline Steps:**
    1.  **Checkout Code & Install Dependencies:** `actions/checkout@v3` and `npm ci`.
    2.  **Linting & Unit Testing:** Ran `npm run lint` and `npm run test` (Jest/RTL). Failed tests halt the pipeline.
    3.  **Build Production Bundle:** Ran `npm run build`.
    4.  **Deploy to AWS S3:** Used `aws-actions/configure-aws-credentials` and `aws s3 sync ./dist s3://my-app-bucket --delete`.
    5.  **Invalidate CloudFront Cache:** Executed `aws cloudfront create-invalidation` so users immediately receive the updated frontend bundle.

**অনুবাদ (Bangla Translation):**
GitHub Actions দিয়ে অটোমেটেড CI/CD সেটআপ করার ধাপসমূহ:
১. **ট্রিগার সেট করা:** `main` ব্রাঞ্চে কোড পুশ হওয়ামাত্রই পাইপলাইন চালু হওয়া।
২. **অটো টেস্ট ও বিল্ড:** ডিপেনডেন্সি ইন্সটল করে `npm test` চালানো। টেস্ট পাস করলে `npm run build` দিয়ে বিল্ড ফাইল প্রস্তুত করা।
৩. **AWS-এ আপলোড:** বিল্ড ফাইল সয়ংক্রিয়ভাবে AWS S3 বাকেটে পাঠাল (`aws s3 sync`)।
৪. **ক্যাশ ক্লিয়ার (Invalidation):** CloudFront ক্যাশ অটো ক্লিয়ার করে দেওয়া যাতে ইউজারের ব্রাউজারে সাথে সাথে নতুন কোড আপডেট হয়ে যায়।

---

### **Q15: How did you collaborate with QA and Product teams to ensure zero-regression releases and maintain high UI component quality? / জিরো-রিগ্রেশন রিলিজ (Zero-regression releases) এবং মানসম্পন্ন UI নিশ্চিত করতে QA ও প্রোডাক্ট টিমের সাথে কীভাবে কাজ করেছিলেন?**

**Answer (English):**
Maintaining high code quality across multiple production releases requires structured engineering practices:
*   **Component Storybook & Design System:** Built reusable UI components inside **Storybook**, allowing designers and product managers to review component states (hover, loading, disabled, error) in isolation before integration.
*   **Automated Testing:** Wrote unit tests for critical business utility functions and integration tests for key user flows (e.g., checkout, login) using **React Testing Library** and **Jest**.
*   **Staging Preview Environments:** Configured automated branch preview deployments (e.g., Vercel / Netlify preview URLs or AWS staging buckets) for every Pull Request, allowing QA engineers to perform manual and exploratory testing before merging.
*   **Post-Release Monitoring:** Integrated **Sentry** for real-time frontend error tracking and exception logging, allowing instant patch releases if unexpected bugs occurred in production.

**অনুবাদ (Bangla Translation):**
বাগ-মুক্ত ও মানসম্পন্ন কোড প্রোডাকশনে পাঠাতে প্রোডাক্ট ও QA টিমের সাথে কাজের প্রক্রিয়া:
*   **Storybook ডিজাইন সিস্টেম:** ইউআই উপাদানগুলো প্রথমে Storybook-এ তৈরি করা হতো, যাতে ডিজাইনার ও প্রোডাক্ট ম্যানেজাররা একা একা রিয়্যাক্ট কম্পোনেন্টের স্টেট টেস্ট করতে পারতেন।
*   **অটোমেটেড টেস্টিং:** গুরুত্বপূর্ণ কাজের টেস্ট কেস **React Testing Library** দিয়ে লিখে রাখা হতো যাতে পুরোনো ফিচার নতুন কোডে না ভাঙে (Zero Regression)।
*   **প্রিভিউ ইউআরএল:** প্রতিটি Pull Request-এর জন্য আলাদা স্টেজিং ইউআরএল অটোমেটিক জেনারেট হতো, যেখানে QA টিম মার্জ করার আগেই রিয়েল টেস্ট করে দেখতে পারত।
*   **Sentry এরর ট্র্যাকিং:** প্রোডাকশনে কোনো আনহ্যান্ডেলড এরর হলে তা সাথে সাথে **Sentry**-তে ধরা পড়ত এবং ফিক্স করা হতো।

---

### **Q16: How did you achieve ranking in the top 1% on HackerRank's Frontend Developer (React) Assessment, and what technical concepts were evaluated? / HackerRank-এর Frontend Developer (React) পরীক্ষায় শীর্ষ ১% স্থান কীভাবে অর্জন করেছিলেন এবং কী কী টেকনিক্যাল বিষয়ে মূল্যায়ন করা হয়েছিল?**

**Answer (English):**
Ranking in the top 1% globally on HackerRank's standardized React assessment verified deep mastery of React internals and performance patterns:
*   **Evaluated Concepts:**
    1.  **Complex State Management & Side Effects:** Asynchronous state batching, custom hooks architecture, and edge-case lifecycle cleanup (`useEffect`).
    2.  **Performance & Rendering Optimization:** Preventing unnecessary re-renders using `React.memo`, `useCallback`, `useMemo`, and key prop reconciliation.
    3.  **DOM Manipulation & Refs:** Accessing DOM nodes using `useRef` and ref forwarding with `forwardRef()`.
    4.  **Form Validation & State Integration:** Controlled components, input validation, and asynchronous form submission handling.
*   **Significance:** Demonstrates battle-tested expertise in writing clean, bug-free, high-performance React code under strict time constraints.

**অনুবাদ (Bangla Translation):**
HackerRank-এর রিয়্যাক্ট পরীক্ষায় বিশ্বের শীর্ষ ১%-এ স্থান অর্জনের বিবরণ:
*   **মূল্যায়ন হওয়া বিষয়সমূহ:**
    ১. **জটিল স্টেট ও সাইড এফেক্ট:** কাস্টম হুক আর্কিটেকচার এবং `useEffect`-এর লাইফসাইকেল মেমোরি ফিক্স করা।
    ২. **পারফরম্যান্স অপ্টিমাইজেশন:** `React.memo`, `useCallback`, `useMemo` দিয়ে অহেতুক রেন্ডারিং বন্ধ করা।
    ৩. **DOM ও Refs:** `useRef` এবং `forwardRef()` দিয়ে কাস্টম ডম অ্যাক্সেস করা।
    ৪. **ইনপুট ভ্যালিডেশন:** টাইপ-সেফ ফর্ম হ্যান্ডলিং।
*   **গুরুত্ব:** এর মাধ্যমে প্রমানিত হয় যে আমি প্রোডাকশন-গ্রেড ফাস্ট ও বাগ-মুক্ত রিয়্যাক্ট কোড লিখতে পারদর্শী।
