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

### 13. Advanced Layout and Responsive Design

**Prompt (Mockup to Responsive Component):**
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

**Prompt Template (Complex Layout Implementation):**
```
You are a master of CSS and React. Create a Next.js component that implements a [specific complex layout, e.g., 'responsive masonry grid', 'sidebar layout with collapsible sections', 'dashboard with draggable and resizable widgets'].
Requirements:
- Use [CSS Grid / Flexbox / combination] for the primary layout structure.
- Implement advanced alignment techniques for [specific alignment challenge, e.g., 'vertically centering dynamic height content', 'justifying items in a complex grid'].
- Ensure the layout is fully responsive across [list breakpoints].
- [Optional: Add a specific feature like 'support for container queries for child elements' or 'integration with a state management solution for layout preferences'].
- Write clean, maintainable TypeScript and [CSS Modules / Tailwind CSS / Styled Components] for styling.
- Explain the rationale behind your layout choices and any trade-offs made.
```

**Example (Complex Layout Implementation):**
```
You are a master of CSS and React. Create a Next.js page component that implements a responsive dashboard layout.
Requirements:
- A fixed sidebar (250px width on desktop, collapsible on tablet/mobile).
- A main content area next to the sidebar.
- The main content area should use CSS Grid to display multiple info cards that automatically adjust their column span based on available width (e.g., 1 column on mobile, 2 on tablet, 3-4 on desktop).
- Cards should have consistent spacing and alignment.
- Implement this using Next.js, TypeScript, and Tailwind CSS.
- Ensure the sidebar collapse mechanism is accessible and clearly indicated.
```

**Prompt Template (Container Queries):**
```
You are a cutting-edge CSS and React developer. Create a Next.js component that demonstrates the use of CSS Container Queries to achieve a truly modular and responsive design.
Requirements:
- The component should adapt its internal layout or styling based on its allocated width, independent of the viewport.
- Provide at least two distinct visual states triggered by different container widths.
- Example scenario: A card component that switches from a vertical layout to a horizontal layout when its container is wide enough.
- Use modern CSS practices and TypeScript.
- Explain the setup for container queries (e.g., `container-type`, `container-name`) and how they are applied.
- Discuss current browser support and any necessary considerations for fallbacks or polyfills.
```

**Prompt Template (CSS Subgrid):**
```
You are a CSS Grid expert. Design a Next.js component that effectively utilizes CSS Subgrid to manage alignment and structure within a nested grid layout.
Requirements:
- The component should feature a parent grid and at least one child element that itself becomes a grid and uses `subgrid` for its rows and/or columns.
- Clearly demonstrate how subgrid helps align items in the nested grid with the main parent grid tracks.
- Provide a comparative explanation or example of how this layout might be more complex or less precise without subgrid.
- Use Next.js, TypeScript, and [CSS Modules / Tailwind CSS / Styled Components].
- Discuss browser support for subgrid and suggest fallback strategies for older browsers.
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

### 15. Advanced Animation and Micro-interactions

**Prompt Template:**
```
You are a UI animation specialist. Implement [specific advanced animation, e.g., 'a choreographed entrance animation for a list of items', 'a complex SVG path animation', 'physics-based micro-interactions on a button/card', 'a shared layout transition between routes'] in a React/Next.js component using [Framer Motion / GSAP / React Spring / Lottie].
Requirements:
- The animation should be [describe desired effect, e.g., 'smooth and performant (60fps)', 'triggered on scroll/hover/click/mount/route change', 'sequenced with precise timing and easing'].
- Address accessibility: ensure it respects `prefers-reduced-motion`.
- Optimize for performance, considering bundle size of the animation library and repaint/reflow costs.
- Provide clean, well-structured code with TypeScript, isolating animation logic where possible.
- Explain how to customize parameters (e.g., duration, delay, easing functions) or extend the animation.
```

**Example:**
```
You are a UI animation specialist using Framer Motion. Implement a 'staggered list item entrance' animation for a dynamically loaded list of items in a Next.js component.
Requirements:
- When the list items appear (e.g., on page load or after data fetching), they should animate in one by one with a slight delay between each.
- The entrance animation for each item should combine opacity (from 0 to 1) and a vertical slide (e.g., from 20px below to its final position).
- The animation should be smooth, engaging, and use appropriate easing functions.
- Ensure it respects the `prefers-reduced-motion` media query (e.g., by disabling or simplifying animations).
- The component should accept the list items as props and render them.
- Provide clean, well-structured code with TypeScript and Framer Motion.
- Include comments explaining the key parts of the animation setup (e.g., `staggerChildren`, `variants`).
```

**Prompt Template (Advanced Scroll-Triggered Animations):**
```
You are a web animation specialist. Implement sophisticated scroll-triggered animations for a section in a Next.js page using [Framer Motion / GSAP / Intersection Observer API with custom logic].
Choose one or combine the following effects:
- Parallax scrolling for background or foreground elements.
- Staggered reveal animations for a list of items as they enter the viewport.
- An element that animates along a path or changes properties (e.g., opacity, scale, rotation) based on scroll progress within its parent container.
Requirements:
- Animations must be smooth, performant (prioritizing `transform` and `opacity`), and avoid jank.
- Implement `prefers-reduced-motion` detection to disable or simplify animations.
- Ensure that the scroll listeners or observers are efficiently managed and cleaned up to prevent memory leaks.
- Provide well-structured TypeScript code, clearly separating animation logic.
- Explain any calculations or concepts used (e.g., normalizing scroll progress, setting up Intersection Observer thresholds).
```

### 16. Design System Development and Theming

**Prompt Template (Design Tokens):**
```
You are an expert React/Next.js developer specializing in scalable frontend architectures. Outline a strategy for establishing and managing design tokens for a new, large-scale Next.js project using [chosen technology, e.g., CSS Custom Properties, Tailwind CSS theme configuration, Styled System, Vanilla Extract].
Address the following:
- Token categories (e.g., colors, typography, spacing, radii, shadows, motion).
- Naming conventions and structure (e.g., global, alias, component-specific tokens).
- How to define and consume these tokens within React components.
- Strategy for theming (e.g., light/dark mode, brand themes) using these tokens.
- Tooling recommendations for managing and documenting tokens (e.g., Style Dictionary, Zeroheight).
- How TypeScript can be used to ensure type safety for tokens.
Provide a small code example of defining a few tokens and using them in a simple component.
```

**Example (Dynamic Theming):**
```
You are an expert React/Next.js developer. Implement a dynamic theming system (light and dark modes) for a Next.js application using [Context API and CSS Custom Properties / Styled Components' ThemeProvider / Tailwind CSS dark mode variant].
Requirements:
- Define a basic set of theme variables for colors (background, text, primary, secondary) for both light and dark themes.
- Create a mechanism to toggle between themes (e.g., a button or a hook `useTheme`).
- The selected theme should persist across page loads (e.g., using localStorage).
- Demonstrate the theming with a sample React component whose appearance changes based on the active theme.
- Ensure the solution is type-safe using TypeScript.
- Explain how new components can subscribe to theme changes.
```

**Prompt Template (Accessibility in Dynamic Theming):**
```
You are an accessibility (a11y) and UI design expert. For a Next.js application that supports dynamic theming (e.g., light, dark, high-contrast modes), provide comprehensive guidelines and a checklist to ensure the theming system is fully accessible.
Address the following critical areas:
- **Color Contrast:** Minimum WCAG AA/AAA contrast ratios for text, interactive elements, icons, and graphics across all themes. How to test and enforce this (e.g., tools, automated checks).
- **Focus Indicators:** Ensuring focus indicators are highly visible and adapt correctly to different themes.
- **Semantic HTML & ARIA:** How theming might impact ARIA attributes or semantic meaning, and how to ensure consistency.
- **User Preferences:** Respecting operating system level theme preferences (e.g., via `prefers-color-scheme`).
- **Testing Strategy:** Specific testing steps for theme-related accessibility, including keyboard navigation and screen reader checks across themes.
- Provide an example of a problematic CSS/style snippet in a multi-theme setup and how to fix it for accessibility.
```

---

## API Integration

### 17. Data Fetching with React Query

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

### 18. Real-time Data with WebSockets

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

### 19. Performance Debugging

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

### 20. Build Error Resolution

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

### 21. Runtime Error Debugging

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

### 22. Compound Component Pattern

**Prompt:**
```
Create a compound component for [UI element] that:
- Uses the compound component pattern
- Provides flexible composition
- Shares state between child components
- Includes proper TypeScript support
- Follows accessibility best practices
```

### 23. Render Props Pattern

**Prompt:**
```
Implement a render props component for [functionality] that:
- Encapsulates [specific logic]
- Provides flexible rendering options
- Includes proper TypeScript generics
- Handles loading and error states
- Is reusable across different UI implementations
```

### 24. Higher-Order Component (HOC)

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