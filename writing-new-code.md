 # AI Coding 101: Writing New Code

 #### 1. Robust feature prompt template

 **Prompt Template:**
 ```
 You are an expert [technology] developer. Implement [app/feature description] with these requirements:
   - [Requirement 1]
   - [Requirement 2]
   - [Requirement 3]
 Use [technology list], follow best practices, include error handling, and provide unit tests.
 ```

 **Example:**
 ```
 You are an expert full-stack developer. Implement a weather tracking app using React (Vite) and TypeScript with these requirements:
   - Fetch real-time data from the OpenWeather API.
   - Display temperature, humidity, and conditions.
   - Handle loading and error states gracefully.
   - Include unit tests for data-fetching functions.
 ```
---

 #### Next.js frontend prompt template

 **Prompt Template:**
 ```
 You are an expert Next.js developer. Implement [app/feature description] in a Next.js project with these requirements:
   - [Requirement 1]
   - [Requirement 2]
   - [Requirement 3]
 Fetch data using getStaticProps or getServerSideProps, set up dynamic routes with getStaticPaths, and style with [CSS framework]. Include error handling and unit tests.
 ```

 **Example:**
 ```
 You are an expert Next.js developer. Build a blog homepage in Next.js with these requirements:
   - Create a page at /blog.
   - Fetch posts from Contentful using getStaticProps.
   - Implement dynamic routes under /blog/[slug] with getStaticPaths.
   - Style with Tailwind CSS.
   - Handle loading, error, and fallback states.
   - Write unit tests for data fetching and page rendering.
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
 Please create a [feature] that follows this example: [example]
 ```

 **Example:**
 ```
 Create a date formatting function. It should work like this:
 1. Input: '2024-02-07' → Output: 'Feb 7, 2024'
 2. Input: '2024-02-07T15:30:00' → Output: 'Feb 7, 2024 3:30 PM'
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
 Please build a [feature]. Find the best practices and examples for building this on the [@Web]
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