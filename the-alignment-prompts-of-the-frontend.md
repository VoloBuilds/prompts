# Frontend Alignment Prompts: Mastering Precision in UI Design

A comprehensive guide with AI prompts for frontend developers to tackle various alignment challenges, ensuring pixel-perfect and responsive user interfaces.

## Table of Contents
1. [Core CSS Alignment (Flexbox & Grid)](#core-css-alignment)
2. [Text & Typography Alignment](#text--typography-alignment)
3. [Icon & Media Alignment](#icon--media-alignment)
4. [Form Element Alignment](#form-element-alignment)
5. [Responsive Alignment Strategies](#responsive-alignment-strategies)
6. [Alignment in Complex Components](#alignment-in-complex-components)
7. [Debugging Alignment Issues](#debugging-alignment-issues)

---

## 1. Core CSS Alignment (Flexbox & Grid)

### 1.1 Flexbox Alignment

**Prompt Template:**
```
You are a CSS Flexbox expert. I need to align items within a container.
Container selector: `[containerSelector]`
Item selector(s): `[itemSelector]`
Desired alignment:
- Main-axis (justify-content): [e.g., space-between, center, flex-end]
- Cross-axis (align-items): [e.g., center, stretch, flex-start]
- Individual item alignment (align-self on specific items, if any): [e.g., item `.special-item` should be `flex-end`]
- Wrapping behavior: [e.g., wrap, nowrap]
Provide the necessary CSS for the container and any specific items. Explain the key Flexbox properties used.
Using [React/Vue/Angular/Vanilla JS] context if relevant for dynamic classes.
```

**Example:**
```
You are a CSS Flexbox expert. I need to align three `div` elements (`.item`) horizontally within a `nav` element (`.navbar`).
Desired alignment:
- Main-axis (justify-content): `space-around`
- Cross-axis (align-items): `center`
The navbar should have a fixed height of 60px.
Provide the CSS for `.navbar` and `.item`. Explain `display: flex`, `justify-content`, and `align-items`.
```

### 1.2 CSS Grid Alignment

**Prompt Template:**
```
You are a CSS Grid layout master. I need to align child elements within a grid container.
Container selector: `[containerSelector]`
Child element selector(s): `[childSelector]`
Grid structure:
- Columns: [e.g., `repeat(3, 1fr)`, `100px auto 1fr`]
- Rows: [e.g., `auto 1fr auto`, `minmax(100px, auto)`]
- Gaps: [e.g., `1rem`, `10px 20px`]
Alignment:
- Justify items (inline/row axis for all items): [e.g., start, end, center, stretch]
- Align items (block/column axis for all items): [e.g., start, end, center, stretch]
- Justify self (specific item, inline axis): `[itemSelector]` should be `[value]`
- Align self (specific item, block axis): `[itemSelector]` should be `[value]`
Provide the CSS for the container and any specific child elements. Explain the key Grid properties used.
```

**Example:**
```
You are a CSS Grid layout master. I have a `div` with class `.grid-container` and several `article` elements inside.
Grid structure:
- Columns: `repeat(auto-fit, minmax(250px, 1fr))`
- Rows: `auto`
- Gaps: `1.5rem`
Alignment:
- Align items (block/column axis for all items): `stretch`
I want one specific article with class `.featured-article` to span two columns and be centered within its grid area using `align-self` and `justify-self`.
Provide the CSS. Explain `grid-template-columns`, `gap`, `align-items`, `grid-column`, `justify-self`, `align-self`.
```

---

## 2. Text & Typography Alignment

### 2.1 Vertical Rhythm & Baseline Alignment

**Prompt Template:**
```
You are a typography and CSS expert. I want to establish consistent vertical rhythm and baseline alignment for text elements in my [React/Vue/Next.js/HTML] project.
Key text elements involved:
- Headers (e.g., `h1`, `h2`, `h3`)
- Paragraphs (`p`)
- Lists (`ul`, `ol`, `li`)
Base font size: `[e.g., 16px]`
Line height multiple: `[e.g., 1.5]`
Desired approach: [e.g., using margins, SASS mixins, CSS custom properties]
Generate the necessary CSS or SASS to ensure all text elements align to a common baseline grid. Explain how to apply this and verify the alignment.
```

**Example:**
```
You are a typography and CSS expert. I want to establish consistent vertical rhythm for my blog content area.
Base font size: `18px`
Line height multiple: `1.6`
Key text elements: `h2`, `h3`, `p`, `blockquote`.
Use CSS custom properties for defining font sizes and line heights based on the rhythm.
Show how to calculate and apply margins (top/bottom) to maintain the rhythm.
Explain how to debug baseline alignment issues using browser developer tools.
```

### 2.2 Text Alignment within Constrained Elements

**Prompt Template:**
```
You are a CSS expert. I have a text element `[textElementSelector]` inside a container `[containerSelector]` with specific dimensions or constraints (e.g., fixed width, max-lines with ellipsis).
Desired text alignment:
- Horizontal: [e.g., left, right, center, justify]
- Vertical (if applicable, e.g., within a fixed height button): [e.g., top, middle, bottom using flexbox/line-height]
- Handling overflow: [e.g., ellipsis, clip]
Provide the CSS to achieve this alignment. If using Flexbox or Grid for vertical alignment, explain why.
```

---

## 3. Icon & Media Alignment

### 3.1 Aligning Icons with Text

**Prompt Template:**
```
You are a UI and CSS expert. I need to align an icon (`[iconElementTagOrClass]`, e.g., `svg`, `.icon-font`) with adjacent text (`[textElementTagOrClass]`).
Desired vertical alignment: [e.g., middle of text, baseline of text, top of text cap height]
Icon library/type: [e.g., Font Awesome, SVG inline, Material Icons]
Provide CSS solutions (e.g., using Flexbox, `vertical-align`, adjusting line-height/padding) to achieve precise alignment. Include any necessary HTML structure. Explain trade-offs if multiple solutions exist.
```

### 3.2 Aligning Media (Images/Videos) with Captions or Other Elements

**Prompt Template:**
```
You are a CSS layout expert. I have an image/video element `[mediaElementSelector]` and a caption/text element `[captionElementSelector]` that need to be aligned.
Desired layout:
- Caption position: [e.g., below the media, overlaying bottom of media, to the side of media]
- Alignment of media and caption relative to each other: [e.g., caption text centered under media, media and caption block left-aligned]
Provide HTML structure and CSS (using Flexbox, Grid, or other techniques) to achieve this. Consider responsive behavior.
```

---

## 4. Form Element Alignment

### 4.1 Aligning Labels and Inputs

**Prompt Template:**
```
You are a CSS and Forms expert. I need to style a form and align its labels (`label`) with their corresponding input fields (`input`, `textarea`, `select`).
Alignment preference:
- Label position relative to input: [e.g., above, to the left, inline]
- Alignment of labels if they are in a column (e.g., all labels right-aligned for a consistent starting point for inputs).
- Alignment of inputs if they are in a column.
Provide clean CSS to achieve this. Consider using Flexbox or Grid for robust form layouts. Show how to handle different input types and potential for error messages.
```

### 4.2 Button Alignment in Forms or UI Groups

**Prompt Template:**
```
You are a CSS UI expert. I need to align multiple buttons (`button`, `.btn`) within a form, a modal footer, or a button group.
Desired alignment: [e.g., all buttons right-aligned, buttons spaced evenly, primary button on right and secondary on left]
Container element: `[containerSelector]`
Provide CSS using Flexbox or Grid to achieve the button alignment. Explain how to adjust spacing and order.
```

---

## 5. Responsive Alignment Strategies

**Prompt Template:**
```
You are a responsive design and CSS expert. I have a component `[componentSelector]` with several child elements `[childSelectors]` that need different alignment based on viewport size.
Alignment requirements:
- Mobile (`< [breakpoint1]px`): [Describe mobile alignment, e.g., items stacked vertically, centered]
- Tablet (`[breakpoint1]px` to `[breakpoint2]px`): [Describe tablet alignment, e.g., 2-column layout, items space-between]
- Desktop (`> [breakpoint2]px`): [Describe desktop alignment, e.g., horizontal layout, items aligned to start]
Provide CSS using media queries and appropriate layout techniques (Flexbox/Grid) to implement these responsive alignment changes.
```

---

## 6. Alignment in Complex Components

### 6.1 Navigation Bar Item Alignment

**Prompt Template:**
```
You are a CSS expert. I'm building a navigation bar `[navSelector]` with a logo `[logoSelector]`, a list of links `[linksListSelector]`, and a user profile section `[userProfileSelector]`.
Desired alignment:
- Logo: [e.g., aligned to the far left]
- Links list: [e.g., centered in the available space, or left-aligned next to logo]
- User profile section: [e.g., aligned to the far right]
- Vertical alignment for all items: [e.g., centered within the navbar height]
Provide HTML structure and CSS (likely Flexbox) to achieve this complex alignment. Ensure it's responsive.
```

### 6.2 Card Component Content Alignment

**Prompt Template:**
```
You are a CSS component design expert. I'm creating a card component `[cardSelector]` which contains an image `[imageSelector]`, a title `[titleSelector]`, a description `[descriptionSelector]`, and a footer with actions `[footerSelector]`.
Desired internal alignment:
- Image: [e.g., full-width at the top]
- Title and Description: [e.g., left-aligned, with specific spacing]
- Footer: [e.g., always at the bottom of the card, with action buttons right-aligned within it]
The card has a fixed or variable height. Provide robust CSS (Flexbox/Grid) to manage the internal alignment of these elements, especially ensuring the footer stays at the bottom if content is short.
```

---

## 7. Debugging Alignment Issues

**Prompt Template:**
```
You are a CSS debugging expert. I'm having trouble aligning `[problematicElementSelector]` within its parent `[parentElementSelector]`.
Current behavior: [Describe what's happening, e.g., "the element is pushed to the right", "it's not vertically centered"]
Desired behavior: [Describe what you want]
Relevant HTML structure:
\`\`\`html
[Paste relevant HTML snippet]
\`\`\`
Relevant CSS:
\`\`\`css
[Paste relevant CSS snippet for parent and child]
\`\`\`
What are common causes for this type of alignment issue? Suggest debugging steps using browser developer tools (e.g., inspecting box model, computed styles, Flexbox/Grid inspectors). Provide potential CSS fixes or properties to investigate.
```

---

*This guide provides prompts to generate solutions for common frontend alignment tasks. Customize them with your specific selectors, desired behaviors, and project context.* 