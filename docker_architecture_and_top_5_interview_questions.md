# Docker Architecture & Top 5 Technical Interview Questions

This guide provides a comprehensive breakdown of **How Docker Works Under the Hood** (Architecture, Engine, Linux Kernel Primitives) and the **Top 5 Popular Docker Interview Questions & Answers**, complete with technical explanations, code examples, and full **Bangla translations**.

---

## 🏗️ Part 1: How Docker Works Under the Hood

Docker is an open-source containerization platform that allows developers to package applications and their dependencies into lightweight, isolated containers that run consistently across any environment.

```
┌─────────────────────────┐           REST API            ┌──────────────────────────────────────────────┐
│      Docker Client      │ ────────────────────────────> │                 Docker Host                  │
│  (docker run / build)   │                               │                                              │
└─────────────────────────┘                               │   ┌──────────────────────────────────────┐   │
                                                          │   │    Docker Daemon (dockerd / Engine)   │   │
                                                          │   └──────────────────┬───────────────────┘   │
                                                          │                      │                       │
                                                          │                      ▼                       │
                                                          │   ┌──────────────────────────────────────┐   │
                                                          │   │              containerd              │   │
                                                          │   └──────────────────┬───────────────────┘   │
                                                          │                      │                       │
                                                          │                      ▼                       │
                                                          │   ┌──────────────────────────────────────┐   │
                                                          │   │                 runc                 │   │
                                                          │   └──────────────────┬───────────────────┘   │
                                                          │                      │                       │
                                                          │                      ▼                       │
                                                          │   ┌──────────────────────────────────────┐   │
                                                          │   │     Linux Kernel (cgroups & namespaces)│ │
                                                          │   └──────────────────────────────────────┘   │
                                                          └──────────────────────────────────────────────┘
```

### 1. The Core Components of Docker Architecture:
* **Docker Client:** The CLI interface (`docker build`, `docker run`, `docker push`) that sends commands via REST API / Unix Domain Socket to the Docker Daemon.
* **Docker Daemon (`dockerd`):** The background service listening for API requests, managing images, containers, networks, and volumes.
* **`containerd`:** High-level container runtime that handles container lifecycle (image pull, storage, execution supervision).
* **`runc`:** Low-level, OCI-compliant container runtime that interacts directly with the Linux Kernel to spawn containers.

### 2. The Linux Kernel Primitives (How Isolation Works):
Containers are **not** virtual machines. They are regular Linux processes isolated using two core Linux Kernel features:
* **Namespaces (Isolation):** Provide virtualized, isolated views of system resources per container:
  * `pid` (Process IDs): Container processes cannot see host processes.
  * `net` (Network Interfaces): Container gets its own virtual IP address and routing table.
  * `mnt` (Mount Points): Container has its own isolated file system root.
  * `ipc` (Inter-Process Communication): Prevents shared memory access between containers.
* **Control Groups / `cgroups` (Resource Limits):** Enforce strict hardware resource limits per container (e.g., max 512MB RAM, 1 CPU core).

### 3. Layered File System (Overlay2 & Copy-on-Write):
Docker images use a Union File System (**Overlay2**). Each `Dockerfile` instruction creates an immutable, read-only layer. When a container runs, Docker attaches a thin **Read-Write (R/W) Container Layer** on top. If a container modifies a file, Docker uses **Copy-on-Write (CoW)** to copy the file to the R/W layer without altering the underlying image layers.

---

### **বাংলা সংক্ষেপ (How Docker Works in Bangla):**
ডকার (Docker) মূলত ভার্চুয়াল মেশিনের মতো আলাদা অপারেটিং সিস্টেম তৈরি করে না। এটি লিনাক্স কার্নেলের (Linux Kernel) ২টি প্রধান ফিচার ব্যবহার করে কাজ করে:
১. **Namespaces (আইসোলেশন):** প্রতিটি কনটেইনারকে নেটওয়ার্ক, প্রসেস ও ফাইল সিস্টেমের দিক থেকে আলাদা করে রাখে।
২. **Control Groups / cgroups (রিসোর্স সীমা):** প্রতিটি কনটেইনার সর্বোচ্চ কতটুকু র্যাম (RAM) বা সিপিইউ (CPU) ব্যবহার করতে পারবে তা নিয়ন্ত্রণ করে।
ডকার ইমেজগুলো লেয়ার বাই লেয়ার (Overlay2) সেভ হয় এবং কনটেইনার রান করলে ওপরের পাতলা Read-Write লেয়ারে কোড এক্সিকিউট হয়।

---

## 🐳 Part 2: Top 5 Popular Docker Interview Questions & Answers

### **Q1: What is the difference between Virtual Machines (VMs) and Docker Containers? / ভার্চুয়াল মেশিন (VM) এবং ডকার কনটেইনারের মধ্যে মূল পার্থক্য কী?**

**Answer (English):**

| Feature | Virtual Machines (VMs) | Docker Containers |
| :--- | :--- | :--- |
| **Architecture** | Runs full Guest OS on Hypervisor | Shares Host OS Kernel via `cgroups` & `namespaces` |
| **Boot Time** | Minutes (Slow) | Milliseconds to Seconds (Ultra-Fast) |
| **Resource Usage** | Heavy (Requires dedicated GBs of RAM/CPU) | Ultra-lightweight (MBs of RAM) |
| **Storage Footprint** | Tens of GBs per VM | Tens to Hundreds of MBs per Container |
| **Isolation** | Hardware-level isolation (Very high) | OS Process-level isolation (High) |

**When to use which:** Use VMs when you need running completely different OS kernels (e.g., Windows on Linux host) or strict hardware compliance isolation. Use Docker Containers for microservices, CI/CD pipelines, rapid deployment, and high-density application scaling.

**অনুবাদ (Bangla Translation):**

| বৈশিষ্ট্য | Virtual Machines (VMs) | Docker Containers |
| :--- | :--- | :--- |
| **আর্কিটেকচার** | হাইপারভাইজারের ওপর পুরো Guest OS চালায় | মূল Host OS-এর কার্নেল শেয়ার করে চলে |
| **স্টার্ট হতে সময়** | কয়েক মিনিট (ধীরগতি) | মিলিমিটার থেকে ১-২ সেকেন্ড (দ্রুতগতি) |
| **রিসোর্স খরচ** | অনেক বেশি (জিবি পর্যন্ত র্যাম নেয়) | খুবই কম (এমবি পরিমাণ র্যাম নেয়) |
| **স্টোরেজ সাইজ** | ১০ থেকে ৫০ GB ফাইল সাইজ | ১০০ থেকে ৪০০ MB ফাইল সাইজ |
| **আইসোলেশন** | হার্ডওয়্যার লেভেল (উচ্চ নিরাপত্তা) | প্রসেস লেভেল (উচ্চ নিরাপত্তা) |

---

### **Q2: What is the difference between `CMD` and `ENTRYPOINT` in a Dockerfile? / Dockerfile-এ `CMD` এবং `ENTRYPOINT`-এর মধ্যে পার্থক্য কী?**

**Answer (English):**
* **`ENTRYPOINT`:** Defines the **default executable command** that will *always* run when the container boots up. It is difficult to override via `docker run` arguments unless `--entrypoint` is explicitly passed.
* **`CMD`:** Defines default parameters that can be passed into `ENTRYPOINT`, or provides a default executable command that can be **easily overridden** at runtime by appending arguments to `docker run`.

```dockerfile
# Example 1: CMD overrideable
FROM alpine
CMD ["echo", "Hello World"]
# Running `docker run my-image ping google.com` REPLACES CMD with `ping google.com`.

# Example 2: ENTRYPOINT + CMD combination
FROM alpine
ENTRYPOINT ["ping"]
CMD ["google.com"]
# Running `docker run my-image github.com` keeps `ping` and passes `github.com` as parameter.
```

**অনুবাদ (Bangla Translation):**
* **`ENTRYPOINT`:** কনটেইনার চালু হওয়ামাত্রই যে কমান্টটি **বাধ্যতামূলকভাবে রান হবে** তা নির্ধারণ করে। `docker run` দিয়ে এটি সহজে পাল্টানো যায় না।
* **`CMD`:** এটি ডিফোল্ট প্যারামিটার হিসেবে কাজ করে। `docker run` চালানোর সময় অতিরিক্ত কোনো নির্দেশ দিলে `CMD`-র কমান্ডের জায়গায় নতুন কমান্ড দিয়ে প্রতিস্থাপিত (Override) করা যায়।

---

### **Q3: What are Multi-Stage Builds in Docker and why are they critical for production Node/React applications? / Docker Multi-Stage Build কী এবং প্রোডাকশনে এটি কেন অত্যন্ত গুরুত্বপূর্ণ?**

**Answer (English):**
Multi-Stage builds allow using multiple `FROM` statements in a single `Dockerfile` to separate the heavy compilation/build environment from the lightweight production runtime environment.

```dockerfile
# Stage 1: Build Phase
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Stage 2: Production Runtime Phase
FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/package*.json ./
COPY --from=builder /app/dist ./dist
RUN npm ci --only=production
CMD ["node", "dist/main.js"]
```

* **Why it's Critical for Production:**
  1. **Shrinks Image Size:** Shaves off build tools (TypeScript compiler, Webpack, Vite, devDependencies), dropping production image size from ~1GB to ~100MB.
  2. **Enhanced Security:** Eliminates source code files, compilers, and internal build tooling from the running production container, reducing the attack surface.

**অনুবাদ (Bangla Translation):**
Multi-Stage Build হলো একটিমাত্র `Dockerfile`-এ একাধিক `FROM` ব্যবহার করে বিল্ড করার সময় (Compilation) এবং লাইভ চালানোর সময়কে (Production Runtime) আলাদা করা।
* **কেন জরুরি:** এটি দিয়ে TypeScript Compiler, Vite বা devDependencies-এর মতো ভারী টুলগুলো ফেলে দিয়ে কেবল ফাইনাল বিল্ড ফাইল নেওয়া হয়। ফলে ইমেজ সাইজ **১GB থেকে কমে ১০০MB** হয়ে যায় এবং নিরাপত্তা বৃদ্ধি পায়।

---

### **Q4: How do Docker Volumes, Bind Mounts, and `tmpfs` mounts differ, and when should you use which? / Docker Volumes, Bind Mounts এবং `tmpfs`-এর মধ্যে পার্থক্য কী?**

**Answer (English):**

```
 ┌──────────────────────────────────────────────────────────────────────────────────┐
 │                                   Host Machine                                   │
 │                                                                                  │
 │   ┌──────────────────────┐  ┌────────────────────────┐  ┌────────────────────┐   │
 │   │   Docker Volume      │  │      Bind Mount        │  │    tmpfs Mount     │   │
 │   │ (/var/lib/docker/...)│  │ (/home/user/mycode/...)│  │   (Host System RAM)│   │
 │   └──────────┬───────────┘  └───────────┬────────────┘  └─────────┬──────────┘   │
 └──────────────┼──────────────────────────┼─────────────────────────┼──────────────┘
                │                          │                         │
                ▼                          ▼                         ▼
 ┌──────────────────────────────────────────────────────────────────────────────────┐
 │                                 Docker Container                                 │
 └──────────────────────────────────────────────────────────────────────────────────┘
```

* **Volumes (`docker volume create`):** Managed entirely by Docker inside the host system file system (`/var/lib/docker/volumes/`). Persistent across container destructions. **Best for database storage (MongoDB/PostgreSQL).**
* **Bind Mounts:** Maps an exact directory from the host machine (e.g., `/home/user/app`) directly into the container. **Best for local development live-reloading (`nodemon`/Vite).**
* **`tmpfs` Mounts:** Stores data strictly in the host machine's RAM memory (never written to physical disk). **Best for non-persistent sensitive secrets and fast temporary tokens.**

**অনুবাদ (Bangla Translation):**
* **Volumes:** ডকার নিজে এটি পরিচালনা করে। কনটেইনার ডিলিট করলেও ডাটা হারিয়ে যায় না। (ডাটাবেজের ডাটা সেভ রাখার জন্য সেরা)।
* **Bind Mounts:** লোকাল কম্পিউটারের ফাইল সরাসরি কনটেইনারের ভেতরে কানেক্ট করা। (লোকাল কোড পরিবর্তনের সাথে সাথে লাইভ দেখার জন্য সেরা)।
* **`tmpfs`:** ডাটা ফিজিক্যাল ডিস্কে সেভ না হয়ে র‍্যামে (RAM) জমা থাকে। (সাময়িক ও অতিসংবেদনশীল গোপন তথ্যের জন্য সেরা)।

---

### **Q5: How does Docker Container Networking work under the hood (Bridge, Host, Overlay, None)? / Docker কন্টেইনার নেটওয়ার্কিং (Bridge, Host, Overlay, None) কীভাবে কাজ করে?**

**Answer (English):**
Docker uses network drivers to manage communication between containers and external networks:
1. **Bridge (Default):** Creates a virtual internal network interface bridge (`docker0`) on the host. Containers on the same bridge network get private IP addresses and communicate using service names as DNS hostnames (`http://mongodb:27017`).
2. **Host:** Removes network isolation between container and host machine. The container shares the host's exact IP address and ports directly (fastest performance, but no port isolation).
3. **Overlay:** Enables multi-host container networking across separate physical Docker Swarm / Kubernetes nodes using VXLAN encapsulation.
4. **None:** Disables all networking for the container (isolated loopback interface only).

**অনুবাদ (Bangla Translation):**
১. **Bridge (ডিফোল্ট):** একটি ভার্চুয়াল অভ্যন্তরীণ নেটওয়ার্ক ব্রিজ তৈরি করে। একই ব্রিজে থাকা কনটেইনারগুলো সার্ভিসের নাম (যেমন `mongodb:27017`) ধরে একে অপরের সাথে কথা বলতে পারে।
২. **Host:** কনটেইনার ও লোকাল কম্পিউটারের পোর্ট এক করে দেয়। (আইসোলেশন থাকে না কিন্তু গতি সবচেয়ে বেশি থাকে)।
৩. **Overlay:** একাধিক সার্ভারের কন্টেইনারগুলোর মধ্যে নেটওয়ার্কিং তৈরি করতে (Docker Swarm/Kubernetes)।
৪. **None:** কনটেইনারের সমস্ত নেটওয়ার্ক সংযোগ সম্পূর্ণ বন্ধ রাখা।
