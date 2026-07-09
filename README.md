# AI-Business-Document-Generator-Agent
# 🤖 AI Business Document Generator Agent

An autonomous AI-powered document generation system that converts a simple business request into a professionally structured Microsoft Word document.

The project uses Large Language Models (LLMs) to automatically understand the user's request, create a task execution plan, generate high-quality business content, and compile everything into a downloadable `.docx` file through a FastAPI backend.

---

# 📖 Overview

This project demonstrates how autonomous AI agents can automate the creation of business documents such as proposals, reports, project plans, and strategies.

Instead of following a fixed workflow, the system first analyzes the user's request, creates its own execution plan, completes each task individually using an LLM, and finally combines the generated content into a professionally formatted Microsoft Word document.

The project showcases concepts such as AI Agents, LLM integration, autonomous planning, task execution, API development, and document generation.

---

# ✨ Features

- AI-powered autonomous task planning
- Dynamic task generation using Gemini API
- Sequential task execution
- Professional Word (.docx) document generation
- FastAPI REST API
- Modular project architecture
- JSON-based planning workflow
- Automatic fallback handling for invalid LLM responses
- Retry mechanism for temporary API failures
- Easy to extend with new tools and agents

---

# 🏗️ Architecture

```
                User Request
                      │
                      ▼
              FastAPI Endpoint
                      │
                      ▼
             Planner Agent (LLM)
                      │
          Generates Task List (JSON)
                      │
                      ▼
             Executor Agent
                      │
      Executes each task individually
                      │
                      ▼
             Gemini LLM
                      │
        Generates business content
                      │
                      ▼
           Document Generator
                      │
               Creates DOCX File
                      │
                      ▼
             Final Business Proposal
```
---

# ⚙️ Tech Stack

- Python 3.13
- FastAPI
- Google Gemini API
- python-docx
- Uvicorn
- dotenv
- JSON
- Regular Expressions (Regex)

---

# 📂 Project Structure

```
project/
│
├── agent/
│   ├── planner.py
│   ├── executor.py
│
├── services/
│   ├── llm.py
│   ├── doc_generator.py
│
├── models/
│   ├── request.py
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

# 🚀 Workflow

### Step 1

The user submits a business request.

Example:

```
Create a business proposal for implementing a CRM system.
```

---

### Step 2

The Planner Agent sends the request to Gemini.

Gemini returns a structured task list like:

```
{
  "tasks":[
      "Analyze business requirements",
      "Create executive summary",
      "Generate implementation plan",
      "Create ROI analysis",
      "Finalize proposal"
  ]
}
```

---

### Step 3

The Executor Agent processes every task one by one.

Each task is sent to Gemini with its own prompt.

---

### Step 4

All generated content is collected.

---

### Step 5

The Document Generator formats the content and creates a professional Microsoft Word document.

---

# 📄 API Endpoint

### POST

```
/agent
```

Request

```json
{
    "request":"Create a business proposal for implementing a CRM system"
}
```

Response

```
Business_Proposal.docx
```

---

# 🧠 AI Agent Workflow

This project follows an autonomous agent architecture.

### Planner Agent

Responsible for:

- Understanding user intent
- Breaking complex requests into smaller tasks
- Returning structured JSON

---

### Executor Agent

Responsible for:

- Executing every planned task
- Calling Gemini API
- Collecting generated outputs

---

### Document Generator

Responsible for:

- Formatting headings
- Adding paragraphs
- Saving as `.docx`

---

# 📌 Challenges Faced

During development, several engineering challenges were encountered:

- Gemini occasionally returned Markdown instead of raw JSON.
- JSON parsing failed because of code block formatting.
- API quota limits caused request failures.
- Temporary server overload (503 errors).

Solutions included:

- Cleaning Markdown using Regex
- JSON validation with fallback responses
- Retry mechanism
- Exception handling
- Default task generation when parsing fails

---

# 💡 Engineering Tradeoff

This project uses an **Autonomous Planning** approach instead of a fixed deterministic workflow.

### Advantages

- Flexible
- Easily adaptable to different document types
- Minimal code changes for new requests

### Limitations

- LLM outputs can occasionally be inconsistent
- Requires response validation
- More debugging compared to rule-based workflows

---

# 🔮 Future Improvements

- Multi-Agent Architecture
- Human-in-the-loop approval
- PDF generation
- PowerPoint generation
- Vector Database integration
- RAG for company-specific knowledge
- Memory-enabled agents
- Web search tools
- Email integration
- Cloud deployment (AWS / Azure)

---

# 🎯 Learning Outcomes

Through this project, I gained hands-on experience with:

- AI Agents
- Autonomous Planning
- Prompt Engineering
- FastAPI Development
- Gemini API Integration
- LLM Workflow Design
- JSON Parsing
- Error Handling
- Document Automation
- Backend API Development

---

# 👨‍💻 Author

**Utkarsh Maurya**

This project was developed as a demonstration of autonomous AI agents capable of planning, executing, and generating professional business documents using Large Language Models.
