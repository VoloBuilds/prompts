# AI Coding 101: Ultimate Prompt Guide
This is a companion document to go along with my AI Coding 101 video. This document contains all the prompts discussed in the video - though I suggest you watch the video for all of the additional context and explanation that relates to these prompts and tips.

You can watch the full video here:

[![AI Coding 101: Ultimate Prompt Guide](https://img.youtube.com/vi/uwA3MMYBfAQ/0.jpg)](https://youtu.be/uwA3MMYBfAQ)
> 🎥 AI Coding 101: Ultimate Prompt Guide (37 tips)


# Writing New Code
#### 1. Specify technologies and frameworks

**Prompt**:
```
Please create [app/feature description] using [technology list]
```

**Example:**
```
Create a weather tracking app using React (vite), TypeScript, ShadCN, and Tailwind
```
---
#### 2. Choose Popular Technologies

**Recommendations:**
```
Frontend: TypeScript, React, Tailwind, ShadCN
Backend: TypeScript, Python, Express.js, FastAPI, Django
Databases: Postgres, MongoDB, Redis
Cloud: Cloud Storage (S3), Supabase Auth, Cloud/Edge Functions
```
---
#### 3. Design the solution, then implement with AI

**Prompt:**
```
I am building a [feature]. It should work like this: [list of requirements]
We should [implementation tips]. It should also handle these edge cases: [list]
```

**Example:**
```
We’re building a search feature. It should perform the search based on the product title and description.

Create a new component, SearchBar, and add it to the existing NavBar component. Also, create a new search endpoint in the @server.ts file.

When no results are found, we should display 'No Results' in place of the product list.
```
---
#### 4. Break things down, give the AI a list of tasks

**Prompt:**
```
Please implement the following:
1. [Requirement #1]
2. [Requirement #2]
3. [Requirement #3]
```
---
## 5. Find the right balance of task scope (not too big or small)

---
#### 6. Use examples in your prompts

**Prompt:**
```
Please create a [feature] that follows this example: [example]”
```

**Example:**
```
Create a date formatting function. It should work like this:
1.Input: '2024-02-07' → Output: 'Feb 7, 2024'
2.Input: '2024-02-07T15:30:00' → Output: 'Feb 7, 2024 3:30 PM'
```
---
#### 7. Provide sample code for the AI to follow

**Prompt:**
```
Please create a [feature]. Here is working sample code: [code]
```
---
#### 8. Use @Docs and @Web context utilities

**Prompt:**
```
Please build a [feature]. Reference the [@Docs / link] docs
```

```
Please build a [feature]. Find the best practices and examples for building this on the [@Web]”
```
---
#### 9. Make sure the code is secure and performs well

**Prompt:**
```
Please implement [feature]. Make sure to account for any potential security issues.
```

```
We just implemented [feature]. Can you check to make sure that it use the most efficient approach?
```
---
#### 10. Proactively check for additional considerations

**Prompt:**
```
Are there any additional considerations for building [feature]?
```
---
#### 11. Ask the AI to write tests & try Test-Driven Development

**Prompt:**
```
Please write the tests for the new feature we just implemented
```

**Test-Driven Development:**
```
We are building [feature]. Please write the tests to cover the following cases: [list]. Once complete, build the actual feature.
```
---
#### 12. Have AI generate your documentation

**Example:**
```
Please add an explanation of this code to our README
```
---
#### 13. Use precise naming

**Example:**
```
Please create a new csvParser method and add it to the dataParsers.ts file
```

---
# Modifying Existing Code
#### 14. Keep code organized by asking AI to refactor & simplify

**Prompt:**
```
Please refactor the code in [file / function] to split it up into [list of files / functions]
```

**Example:**
```
Please split up dataParser.ts into dedicated files including csvParser.ts, xmlParser.ts, and pdfParser.ts
```
---
## 15. Manage and balance the CONTEXT you give to the AI

---
#### 16. Tag specific relevant files as context

**Prompt:**
```
Please implement [feature]. You’ll need to modify [list of files]. Here are additional files for context: [list of files]
```
---
#### 17. Keep your files at 300 lines of code or less

---
#### 18. Keep in mind that the full conversation is used as context

---
#### 19. Start a new conversation for each new feature

---
#### 20. Tell the AI what works well and what needs to be changed

**Prompt:**
```
This was a good start. [list of features] are working well but [list of problems] still needs to be fixed. Can you fix that?
```

**Example:**
```
The new search feature is properly calling the API and showing results but it is not properly searching by product description. Can you please fix that?
```
---
#### 21. Ask AI to find edge cases or bugs

**Prompt:**
```
Are there any edge cases we should consider or handle?
```
---
#### 22. Ask AI to review the code

**Prompt:**
```
Now that we have finished building [feature], can you do a full review of the implementation and the new code?
```
---
#### 23. Ask AI about what the current code does

**Prompt:**
```
How does the code in [@file] work? Give a high level overview
```

```
How does the [function] work? Give a detailed description”
```

**Example:**
```
What does the code in @serverComm.ts do? How does it handle authentication?
```
---
# Troubleshooting
#### 24. Be specific about what is not working (and what is)

**Prompt:**
```
When I do [X], I see [Y], but when I do [Z], it seems to work.
```

```
Right now the [feature 1] is working correctly but [feature 2] is failing [failure description]. Can you fix that?
```

**Example:**
```
The buttons are visible now but when I click them nothing seems to happen. Can you fix that?
```
---
#### 25. Share screenshots to show what is wrong

**Example:**
```
The layout is still incorrect. Please see [@screenshot] and note how the sidebar is not properly expanding.
```
---
#### 26. Share the exact errors

**Prompt:**
```
It’s still failing - here are the errors: [full error logs]
```
---
## 27. The Beaver Method
The beaver method is a troubleshooting approach that works by asking AI to add logs throughout the code that you are troubleshooting, running the software, and feeding the logs back into the AI so that it can troubleshoot with all the relevant runtime context.

**Step 1 Prompt:**
```
Please add logs at every step of the process to make it easier to troubleshoot and figure out where the problem is.
```

**Step 2 Prompt:**
```
I ran the process and here is the result: [full logs generated from step 1]
```
---
#### 28. Ask AI to explain the code
Similar to #23 but in the context of troubleshooting to help bridge the disconnect between developer expectations and the way the code actually works (which the developer currently perceives as incorrect).

**Example:**
```
This code doesn’t convert dates correctly. Can you explain how it works?
```
---
#### 29. Ask AI to use a "radically different approach"

**Prompt:**
```
This still isn’t working. Let’s try a radically different approach.
```
---
## 30. Know when to stop asking AI and read the code yourself

---
# Learning To Code

The following tips match what was covered in the AI Coding 101 episode, but the [Learn To Code](https://github.com/VoloBuilds/prompts/blob/main/LearnToCode.md) page contains more detailed tips for learning to code specifically including a **technology glossary** that can help guide your exploration.

#### 31. Tell AI to keep it simple + that you are a new dev

**Example:**
```
I am learning how to code. Can you simply explain how the frontend connects to the backend?
```
---
#### 32. Ask AI to explain code "line by line"

**Prompt:**
```
Please add comments explaining [function] line by line
```

**Example:**
```
I am learning how to code. Can you explain the getContactDetails function line by line?
```
---
#### 33. Ask AI to explain specific technologies & concepts

**Prompt:**
```
Can you explain how [concept] works? What does [technology] do?
```

**Example:**
```
I'm a new dev. Can you explain what databases are for, when I should use them, and what Postgres is specifically?
```
---
#### 34. Ask AI how to build something

**Prompt:**
```
I want to build a [app/feature]. How would you approach this problem from a technical perspective?
```

**Example:**
```
I want to build a chat app. How would you architect this and what considerations do we need to take into account?
```
---
#### 35. Ask AI to show you examples

**Prompt:**
```
Can you show me a working example of a [concept] and explain it?
```

**Example:**
```
I am learning to code and want to understand how objects work. Can you create some examples and explain them?
```
---
#### 36. Tell the AI what you already know vs what is unclear

**Prompt:**
```
I know how [concept] works but can you explain how it relates to [concept 2]?
```

**Example:**
```
I have an API and understand how requests come in but can you explain how I could add authentication to my endpoints?
```
---
### 37. Focus on learning and understanding core concepts

---
