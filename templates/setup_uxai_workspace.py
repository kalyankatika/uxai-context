import os

print("🚀 Starting generation of your UXAI Context Brain Setup Toolkit...")

# Create the folder structure
folders = [".vscode", "brain", "research", "design", "src"]
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Created directory: {folder}/")

# 1. FOAM_README.md
foam_readme = """# UXAI Context Brain 🧠

Welcome to the central visual context hub for our project. This repo bridges the gap between **Dev** (code repositories & agents), **Design** (UI flows & canvases), and **Research** (user insight & AI behavioral patterns) using an asynchronous, graph-linked markdown layout powered by **Foam**.

---

## 🧭 The Core System Architecture

To avoid context fragmentation, our project memory is mapped out in a 3-layer timeline node hierarchy. Use double-bracket links `[[filename]]` to interconnect them.

```mermaid
graph TD
    A[CLAUDE.md / Router] --> B[now.md / Current Execution Focus]
    A --> C[outcome.md / Macro-Goals & Timeline]
    B -->|Tied to| D[src/ Codebase]
    C -->|Validated by| E[research/ Insights]
    B -->|References| F[design/ Wireframes]
    
    style A fill:#4F46E5,stroke:#fff,stroke-width:2px,color:#fff
    style B fill:#0EA5E9,stroke:#fff,stroke-width:1px,color:#fff
    style C fill:#10B981,stroke:#fff,stroke-width:1px,color:#fff
```

### 1. CLAUDE.md (The Router)
* **Purpose:** The system entry point. Defines our tech stack architecture, design philosophies, core APIs, and instructions for team onboarding or AI sub-agents. 
* **Action:** Check this file before starting any major architectural shift.

### 2. now.md (The Daily Timeline Node)
* **Purpose:** High-velocity working memory. Tracks what the team (and AI) is working on *right now*, immediate active blockers, and daily execution threads.
* **Action:** Updated daily. Think of it as an asynchronous daily standup log.

### 3. outcome.md (The Macro-Goals Engine)
* **Purpose:** Long-term timeline anchor. Captures your strategic milestones, user testing criteria, and technical outcomes.
* **Action:** Updated during sprint planning or milestone reflections to track ongoing results.

---

## 🚀 Setting Up Foam in VS Code

To view the live interactive node graph, follow-ups, and daily note connections, set up your local VS Code environment:

1. **Install Extensions:** Open VS Code (`Ctrl+Shift+X` / `Cmd+Shift+X`) and install the tools specified in your configuration.
2. **Launch the Graph:** Open your command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and trigger:
   * `Foam: Show Graph`
3. **Workspace Settings:** Ensure your workspace configuration allows file attachments and auto-completed links.

---

## 🛠️ Cross-Discipline Linking Examples (Copy & Use)

Use these semantic linking conventions inside your markdown files to bring code, mockups, and research into one conversation layer:

### Dev + Research Linkage
Inside your `now.md`:
> **Focus:** Resolving token budget constraints in the prompt engineering layer. Debugging `[[src/agents/ux-optimizer.ts]]`. We are modifying the system instructions to explicitly prioritize user goals captured in the `[[research/user-persona-beta.md]]` study.

### Design Embed Linkage
Inside your `outcome.md` or a design file using Markdown Preview Enhanced:
```html
## Target Layout: Interactive Canvas Dashboard
<!-- This renders a live Figma frame directly inside a VS Code tab -->
<iframe 
  style="border: 1px solid rgba(0, 0, 0, 0.1);" 
  width="100%" 
  height="450" 
  src="https://www.figma.com/embed?embed_host=share&url=YOUR_FIGMA_FRAME_URL" 
  allowfullscreen>
</iframe>

*Refers to flow documentation outlined in [[design/canvas-v1-specs.md]].*
```

---

## 📈 Contribution Rules for the Brain

* **Never Break the Graph:** Always link documents via lowercase file names within double brackets. Foam will handle paths dynamically.
* **Keep Text Punchy:** Treat your notes like building blocks. If a section gets too complex, spin it off into its own note (`[[new-subtopic]]`) to create a new cluster node in the graph.
* **Commit Chronologically:** Code extensions, design file updates, and markdown entries should be packaged into logical Git commits together so the repository timeline remains linearly aligned.
"""

with open("FOAM_README.md", "w", encoding="utf-8") as f:
    f.write(foam_readme.strip())
print("Created: FOAM_README.md")

# 2. .vscode/settings.json
settings_json = """{
  "foam.edit.linkReferenceDefinitions": "withoutPath",
  "markdown.links.openLocation": "currentGroup",
  "foam.openDailyNote.directory": "brain",
  "search.useIgnoreFiles": true,
  "editor.wordWrap": "on",
  "editor.quickSuggestions": {
    "comments": "on",
    "strings": "on",
    "other": "on"
  }
}"""

with open(".vscode/settings.json", "w", encoding="utf-8") as f:
    f.write(settings_json.strip())
print("Created: .vscode/settings.json")

# 3. .vscode/extensions.json
extensions_json = """{
  "recommendations": [
    "foam.foam-vscode",
    "tldraw-org.tldraw-vscode",
    "shd101wyy.markdown-preview-enhanced"
  ]
}"""

with open(".vscode/extensions.json", "w", encoding="utf-8") as f:
    f.write(extensions_json.strip())
print("Created: .vscode/extensions.json")

# 4. brain/now.md
now_md = """# 📍 Execution State: Now

## ⚡ Active Threads
* **Focus 1:** [Task Description] -> Links: [[CLAUDE.md]], [[design/architecture.tldraw]]
* **Focus 2:** [Task Description] -> Links: [[src/agents/ux-optimizer.ts]]

## 🛑 Blockers & Friction
* [Blocker 1] - Awaiting validation criteria from [[outcome.md]].

## 🪵 Log & Daily Nodes
* [[2026-11-09]]: Initial workspace stabilization and context porting.
"""

with open("brain/now.md", "w", encoding="utf-8") as f:
    f.write(now_md.strip())
print("Created: brain/now.md")

# 5. brain/outcome.md
outcome_md = """# 🎯 Macro-Goals & Strategic Timeline

## 🗺️ Milestone Tracking
* **Q4 Target - System Alpha:** Verification parameters tied to user studies in [[research/user-persona-beta.md]].
* **Ongoing Stream - Performance Optimization:** Mapping core execution requirements to [[CLAUDE.md]].

## 📋 Architecture Decision Records (ADRs)
### ADR-001: Graph-Linked Local Context Storage
* **Status:** Approved
* **Context:** Fragmented text files made it difficult for team members and external AI agents to maintain consistent project state.
* **Decision:** Implement plain-text markdown schemas backed by Foam visual graphs directly inside the core codebase repository.
"""

with open("brain/outcome.md", "w", encoding="utf-8") as f:
    f.write(outcome_md.strip())
print("Created: brain/outcome.md")

print("✅ All set! Run 'code .' in this folder to open your optimized workspace in VS Code.")