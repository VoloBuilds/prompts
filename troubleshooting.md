 # AI Coding 101: Troubleshooting

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
 The Beaver Method is a troubleshooting approach that works by asking AI to add logs throughout the code, running the software, and feeding the logs back to AI for context.

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
 Similar to #23 but in the context of troubleshooting to bridge the disconnect between expectations and reality.

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