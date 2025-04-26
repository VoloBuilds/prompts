 # AI Coding 101: Modifying Existing Code

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
 How does the [function] work? Give a detailed description
 ```

 **Example:**
 ```
 What does the code in @serverComm.ts do? How does it handle authentication?
 ```