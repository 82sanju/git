# FinePrint  

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()  
[![License](https://img.shields.io/badge/license-Proprietary-red)]()  
[![Tech Stack](https://img.shields.io/badge/stack-React%20%7C%20Supabase%20%7C%20OpenAI-blue)]()  
[![Version](https://img.shields.io/badge/version-1.0.0-yellow)]()  

**AI-Powered Legal Document Analysis Platform**  

FinePrint is an AI-powered legal document analysis platform built on a Retrieval-Augmented Generation (RAG) architecture. It transforms how users interact with contracts, agreements, and other legal documents by providing **comprehensive analysis, risk identification, obligation tracking, and interactive Q&A** capabilities.  

---

## 📑 Table of Contents  
1. [Overview](#-overview)  
2. [Core Features](#-core-features)  
3. [Tech Stack](#-tech-stack)  
4. [Design Preferences](#-design-preferences)  
5. [Screens & Pages](#-screens--pages)  
6. [App Navigation](#-app-navigation)  
7. [User Flow](#-user-flow)  
8. [Installation & Setup](#-installation--setup)  
9. [License](#-license)  

---

## 📌 Overview  
- **App/Website Name:** FinePrint  
- **Target Users:** Legal professionals, business owners, entrepreneurs, contract managers, and individuals handling legal docs.  
- **Problem Solved:** Simplifies complex legal documents, making them **accessible, understandable, and actionable.**  

---

## 🚀 Core Features  
- 📂 **Document Upload & Processing** (PDF, DOCX, Text + OCR)  
- 🧠 **RAG-Powered Analysis** with knowledge base creation  
- 💬 **Interactive Q&A** for document-specific questions  
- ⚠️ **Risk Assessment** & red-flag detection  
- 📜 **Obligation Extraction** of rights, responsibilities, deadlines  
- 📑 **Clause-by-Clause Breakdown** with plain-English explanations  
- 📘 **Key Terms Glossary** with auto definitions  
- 🔍 **Comparative Analysis** between multiple contracts/versions  
- 🔔 **Alert System** for deadlines, renewals, risks  
- 📤 **Export Reports** to PDF  
- 🗂 **Document Management** with tagging & search  
- 🔒 **User Authentication** + privacy protection  
- 👥 **Collaboration Tools** for team analysis  

---

## 🛠 Tech Stack  

**Front-End:**  
- React + TypeScript  
- Tailwind CSS  
- Vite  
- React Query  

**Back-End:**  
- Supabase (Auth, PostgreSQL, Real-time)  
- Supabase Storage  
- Row Level Security (RLS)  

**AI Integration:**  
- OpenAI GPT-4o  
- Custom RAG with vector embeddings  
- OpenAI Embeddings API  

**APIs & Integrations:**  
- PDF.js / parsing libraries  
- OCR for scanned docs  
- Supabase email notifications  
- File compression utilities  

---

## 🎨 Design Preferences  

- **Interface:** Clean, professional, legal-tech aesthetic  
- **Colors:**  
  - Primary: Deep Navy Blue `#1E3A8A`  
  - Secondary: Warm Gray `#6B7280`  
  - Accent: Golden Yellow `#F59E0B`  
- **Typography:**  
  - Headings: *Inter*  
  - Body: *Source Sans Pro*  
- **Other:** Accessibility compliance, high contrast, white space  

---

## 📄 Screens & Pages  

- `/` → Landing Page  
- `/auth/login` → Login  
- `/auth/signup` → Registration  
- `/auth/forgot-password` → Password Reset  
- `/onboarding` → Onboarding wizard  
- `/dashboard` → Main dashboard  
- `/documents` → Document library  
- `/documents/upload` → Upload docs  
- `/documents/:id` → Document analysis  
- `/documents/:id/compare` → Compare contracts  
- `/analysis/:id` → Full analysis report  
- `/alerts` → Alerts & notifications  
- `/settings` → User settings  
- `/settings/team` → Team management  
- `/help` → Help center  

---


