# Frontend React/Next.js Engineer Prompts Guide

A comprehensive collection of AI prompts specifically designed for Frontend React/Next.js engineers to accelerate development, solve common challenges, and follow best practices.

## Table of Contents
1. [Component Development](#component-development)
2. [State Management](#state-management)
3. [Next.js Specific Features](#nextjs-specific-features)
4. [Performance Optimization](#performance-optimization)
5. [Testing & Quality Assurance](#testing--quality-assurance)
6. [UI/UX Implementation](#uiux-implementation)
7. [API Integration](#api-integration)
8. [Debugging & Troubleshooting](#debugging--troubleshooting)

---

## Component Development

### 1. React Component Creation Template

**Prompt Template:**
```
You are an expert React developer. Create a [component type] component called [ComponentName] with these requirements:
- [Requirement 1]
- [Requirement 2]
- [Requirement 3]
Use TypeScript, follow React best practices, implement proper prop validation, and include JSDoc comments.
```

**Example:**
```
You are an expert React developer. Create a reusable Card component with these requirements:
- Accept title, description, and optional image props
- Support different card variants (default, outlined, elevated)
- Include hover animations and accessibility features
- Be responsive and work with Tailwind CSS
Use TypeScript, follow React best practices, implement proper prop validation, and include JSDoc comments.
```

### 2. Custom Hook Development

**Prompt Template:**
```
Create a custom React hook called use[HookName] that:
- [Functionality 1]
- [Functionality 2]
- [Functionality 3]
Include TypeScript types, error handling, and cleanup logic where needed.
```

**Example:**
```
Create a custom React hook called useLocalStorage that:
- Stores and retrieves values from localStorage
- Handles JSON serialization/deserialization automatically
- Provides loading and error states
- Syncs across multiple components using the same key
Include TypeScript types, error handling, and cleanup logic where needed.
```

---

## State Management

### 3. Context API Implementation

**Prompt:**
```
Create a React Context for [feature] management that includes:
- State interface with TypeScript
- Provider component with initial state
- Custom hook for consuming the context
- Actions for [list specific actions]
Follow the reducer pattern and include error boundaries.
```

### 4. Zustand Store Setup

**Prompt:**
```
Create a Zustand store for [feature] with these requirements:
- TypeScript interfaces for state shape
- Actions for [list actions]
- Persist middleware for localStorage
- DevTools integration for debugging
Include selectors and proper state immutability.
```

---

## Next.js Specific Features

### 5. Page with Data Fetching

**Prompt Template:**
```
Create a Next.js page at [route] that:
- Fetches data using [getStaticProps/getServerSideProps/App Router]
- Implements [specific functionality]
- Handles loading and error states
- Includes proper SEO meta tags
- Is fully responsive with [CSS framework]
```

**Example:**
```
Create a Next.js page at /products/[category] that:
- Fetches products using getStaticProps with ISR
- Implements filtering and sorting functionality
- Handles loading and error states gracefully
- Includes proper SEO meta tags and Open Graph data
- Is fully responsive with Tailwind CSS
```

### 6. API Route Implementation

**Prompt:**
```
Create a Next.js API route at /api/[endpoint] that:
- Handles [HTTP methods]
- Validates request data using [validation library]
- Connects to [database/external API]
- Implements proper error handling and status codes
- Includes rate limiting and authentication if needed
```

### 7. Middleware Setup

**Prompt:**
```
Create Next.js middleware that:
- [Functionality 1]
- [Functionality 2]
- Runs on specific routes: [route patterns]
- Handles redirects and rewrites appropriately
Include proper TypeScript types and error handling.
```

---

## Performance Optimization

### 8. Component Optimization

**Prompt:**
```
Optimize this React component for performance:
[paste component code]

Focus on:
- Memoization with React.memo, useMemo, useCallback
- Lazy loading and code splitting
- Bundle size optimization
- Render optimization techniques
```

### 9. Image Optimization

**Prompt:**
```
Implement an optimized image component using Next.js Image that:
- Supports responsive images with multiple breakpoints
- Includes lazy loading and blur placeholder
- Handles different image formats (WebP, AVIF)
- Provides fallback for unsupported formats
- Includes proper alt text and accessibility features
```

---

## Testing & Quality Assurance

### 10. Component Testing

**Prompt Template:**
```
Write comprehensive tests for this [component type] using React Testing Library and Jest:
[paste component code]

Include tests for:
- Rendering with different props
- User interactions and event handling
- Accessibility compliance
- Error states and edge cases
```

### 11. E2E Testing with Playwright

**Prompt:**
```
Create Playwright E2E tests for the [feature] workflow:
- [Step 1 of user journey]
- [Step 2 of user journey]
- [Step 3 of user journey]
Include proper page object models and test data setup.
```

### 12. Performance Testing

**Prompt:**
```
Create performance tests for [component/page] that measure:
- Core Web Vitals (LCP, FID, CLS)
- Bundle size impact
- Runtime performance metrics
- Memory usage patterns
Use appropriate testing tools and provide optimization recommendations.
```

---

## UI/UX Implementation

### 13. Responsive Design Implementation

**Prompt:**
```
Convert this design mockup to a responsive React component:
[describe design or paste image]

Requirements:
- Mobile-first approach
- Breakpoints: mobile (320px), tablet (768px), desktop (1024px)
- Use [CSS framework] for styling
- Ensure accessibility compliance (WCAG 2.1 AA)
- Include smooth animations and transitions
```

### 14. Form Implementation

**Prompt:**
```
Create a complex form component for [purpose] with:
- Form validation using [validation library]
- Multi-step wizard if applicable
- File upload capabilities
- Real-time validation feedback
- Accessibility features (ARIA labels, keyboard navigation)
- Loading states and error handling
Use React Hook Form and TypeScript.
```

### 15. Animation Implementation

**Prompt:**
```
Implement smooth animations for [component/interaction] using [animation library]:
- [Animation 1]
- [Animation 2]
- [Animation 3]
Ensure animations are performant, respect user preferences (prefers-reduced-motion), and enhance UX.
```

---

## API Integration

### 16. Data Fetching with React Query

**Prompt:**
```
Set up React Query (TanStack Query) for [API endpoint] with:
- Query and mutation hooks
- Caching strategies
- Error handling and retry logic
- Optimistic updates
- Background refetching
Include TypeScript types for API responses.
```

### 17. Real-time Data with WebSockets

**Prompt:**
```
Implement WebSocket connection for [real-time feature] that:
- Establishes connection on component mount
- Handles connection states (connecting, connected, disconnected)
- Processes incoming messages and updates UI
- Includes reconnection logic
- Properly cleans up on unmount
```

---

## Debugging & Troubleshooting

### 18. Performance Debugging

**Prompt:**
```
Help me debug performance issues in this React component:
[paste component code]

Analyze:
- Unnecessary re-renders
- Memory leaks
- Bundle size impact
- Runtime performance bottlenecks
Provide specific optimization recommendations.
```

### 19. Build Error Resolution

**Prompt:**
```
I'm getting this build error in my Next.js project:
[paste error message]

Help me:
- Understand the root cause
- Provide step-by-step solution
- Suggest preventive measures
- Update configuration if needed
```

### 20. Runtime Error Debugging

**Prompt:**
```
Debug this runtime error in my React application:
Error: [error message]
Component: [component name]
Context: [describe when error occurs]

Provide:
- Root cause analysis
- Step-by-step debugging approach
- Code fix with explanation
- Error boundary implementation if needed
```

---

## Advanced Patterns

### 21. Compound Component Pattern

**Prompt:**
```
Create a compound component for [UI element] that:
- Uses the compound component pattern
- Provides flexible composition
- Shares state between child components
- Includes proper TypeScript support
- Follows accessibility best practices
```

### 22. Render Props Pattern

**Prompt:**
```
Implement a render props component for [functionality] that:
- Encapsulates [specific logic]
- Provides flexible rendering options
- Includes proper TypeScript generics
- Handles loading and error states
- Is reusable across different UI implementations
```

### 23. Higher-Order Component (HOC)

**Prompt:**
```
Create a HOC called with[FeatureName] that:
- Adds [specific functionality] to wrapped components
- Preserves original component props and ref
- Includes proper TypeScript support
- Handles edge cases and error scenarios
- Provides debugging information in development
```

---

## Best Practices Reminders

When using these prompts, remember to:

1. **Always specify TypeScript** - Include type safety requirements
2. **Mention accessibility** - Ensure WCAG compliance
3. **Include error handling** - Handle edge cases and error states
4. **Request tests** - Ask for comprehensive test coverage
5. **Specify styling approach** - Mention CSS framework or styling method
6. **Consider performance** - Ask for optimization recommendations
7. **Include documentation** - Request JSDoc comments and README updates

## Example Workflow

```
1. Use Component Development prompts to create base components
2. Apply State Management prompts for complex state logic
3. Implement Next.js features using specific prompts
4. Optimize with Performance prompts
5. Ensure quality with Testing prompts
6. Debug issues using Troubleshooting prompts
```

---

*This guide is designed to help Frontend React/Next.js engineers work more efficiently with AI assistants. Customize the prompts based on your specific project requirements and tech stack.* 