# Job-Specific AI Prompts Guide

A comprehensive collection of AI prompts tailored for different software engineering roles and specializations. Each guide contains role-specific scenarios, best practices, and optimized prompts to accelerate development and solve common challenges.

## Foundational Communication Guide

### Essential for All Developers
- **[LLM Communication Techniques for Developers](llm-communication-techniques-for-developers.md)** - Master effective communication with AI assistants
  - CLEAR framework and STAR method for structured prompts
  - Context management and progressive disclosure techniques
  - Debugging and troubleshooting communication patterns
  - Architecture discussions and collaborative problem solving
  - Advanced techniques like Socratic method and rubber duck debugging

## Available Guides

### Frontend Development
- **[Frontend React/Next.js Engineer](frontend-react-nextjs-prompts.md)** - Complete guide for React and Next.js developers
  - Component development and custom hooks
  - State management (Context API, Zustand)
  - Next.js specific features (SSR, SSG, API routes)
  - Performance optimization and testing
  - UI/UX implementation and accessibility

### Backend Development
- **[Rust Backend Engineer (RIG + Actix-web)](rust-backend-engineer-prompts.md)** - Specialized guide for Rust backend developers
  - Actix-web server development
  - RIG integration for AI capabilities
  - Database integration with SQLx
  - Authentication, authorization, and security
  - Performance optimization and deployment

- **[Node.js Sails.js Backend Engineer](nodejs-sailsjs-backend-prompts.md)** - Comprehensive guide for Node.js Sails.js developers
  - Sails.js MVC architecture and conventions
  - Waterline ORM and database integration
  - Real-time features with Socket.io
  - RESTful API development and GraphQL
  - Authentication, middleware, and deployment

### Blockchain & Web3
- **[Blockchain Architect](blockchain-architect-prompts.md)** - Complete guide for Blockchain Architects and Web3 developers
  - Blockchain architecture design and technology stack selection
  - Smart contract architecture and DeFi protocol design
  - Consensus mechanisms and scalability solutions
  - Security, cryptography, and interoperability
  - Infrastructure, governance, and tokenomics

### Design & User Experience
- **[UI Designer (Figma)](ui-designer-figma-prompts.md)** - Complete guide for UI Designers using Figma
  - Interactive prototype creation and design systems
  - Component design and responsive layouts
  - Accessibility and usability testing
  - Design handoff and developer collaboration
  - Performance optimization and conversion rate optimization

### Quality Assurance & Testing
- **[Test Engineer (Pytest)](test-engineer-pytest-prompts.md)** - Comprehensive guide for Test Engineers using pytest
  - Test framework setup and organization
  - Unit, integration, and API testing
  - UI/E2E testing with Selenium and Playwright
  - Test data management and fixtures
  - Performance testing and CI/CD integration

### Product Management
- **[Product Manager](product-manager-prompts.md)** - Complete guide for Product Managers
  - Interactive prototype creation and MVP definition
  - User research, personas, and journey mapping
  - Feature planning and prioritization frameworks
  - Market research and competitive analysis
  - Product strategy, roadmapping, and go-to-market
  - Data analysis, metrics, and stakeholder communication

### Human Resources & Talent
- **[HR Manager (Hiring & Recruitment)](hr-manager-hiring-prompts.md)** - Comprehensive guide for HR Managers
  - Job description creation and optimization
  - Talent sourcing and recruitment strategies
  - Interview process design and candidate assessment
  - Employer branding and diversity initiatives
  - Compensation strategy and onboarding processes
  - Recruitment analytics and legal compliance

### Coming Soon
- **Python Backend Engineer** (Django/FastAPI)
- **DevOps Engineer** (Docker, Kubernetes, CI/CD)
- **Mobile Developer** (React Native/Flutter)
- **Data Engineer** (Python, SQL, ETL pipelines)
- **Machine Learning Engineer** (Python, TensorFlow, PyTorch)
- **UX Researcher** (User research, usability testing, analytics)

## How to Choose the Right Guide

### Start with Communication Fundamentals
**All developers should begin with**: [LLM Communication Techniques](llm-communication-techniques-for-developers.md)
- Learn to structure thoughts clearly and concisely
- Master prompt engineering for technical scenarios
- Understand context management strategies
- Practice effective debugging communication
- Develop collaborative problem-solving skills

### By Technology Stack
- **React/Next.js Frontend** → [Frontend React/Next.js Guide](frontend-react-nextjs-prompts.md)
- **Rust + Actix-web Backend** → [Rust Backend Guide](rust-backend-engineer-prompts.md)
- **Node.js + Sails.js Backend** → [Node.js Sails.js Guide](nodejs-sailsjs-backend-prompts.md)
- **Blockchain/Web3 Development** → [Blockchain Architect Guide](blockchain-architect-prompts.md)
- **Figma Design** → [UI Designer Figma Guide](ui-designer-figma-prompts.md)
- **Pytest Testing** → [Test Engineer Pytest Guide](test-engineer-pytest-prompts.md)
- **Product Management** → [Product Manager Guide](product-manager-prompts.md)
- **HR & Recruitment** → [HR Manager Guide](hr-manager-hiring-prompts.md)
- **Python Backend** → Coming soon

### By Role Responsibilities
- **Frontend Focus**: UI/UX, component development, state management
- **Backend Focus**: APIs, databases, authentication, performance
- **Blockchain Focus**: Smart contracts, DeFi protocols, consensus mechanisms
- **Design Focus**: Prototyping, design systems, user experience
- **Testing Focus**: Test automation, quality assurance, CI/CD
- **Product Management**: Strategy, research, prototyping, stakeholder communication
- **HR & Talent**: Hiring, recruitment, job descriptions, candidate assessment
- **Full-Stack**: Use both frontend and backend guides
- **DevOps Focus**: Infrastructure, deployment, monitoring

### By Experience Level
- **Junior Developers**: Start with basic setup and component/API development prompts
- **Mid-Level Developers**: Focus on architecture, testing, and optimization prompts
- **Senior Developers**: Use advanced patterns, performance, and system design prompts
- **Architects**: Use blockchain architecture and system design prompts
- **Designers**: Begin with prototype and component prompts, advance to design systems
- **Test Engineers**: Start with framework setup, progress to advanced testing patterns
- **Product Managers**: Begin with user research and prototype prompts, advance to strategy
- **HR Managers**: Start with job description creation, advance to analytics and compliance

## Universal Prompts for All Roles

### 1. Effective Communication Check
```
Using the CLEAR framework, help me structure this request:
Context: [Current situation and environment]
Language: [Technical terms and scope]
Expectations: [What I want as output]
Actions: [Specific things to do]
Results: [How I'll validate success]

My current request: [Your original question/need]
```

### 2. Progressive Problem Solving
```
Let's use progressive disclosure to solve this step by step:

High-level question: [Your main challenge]

Based on your response, I'll ask follow-up questions to drill down into:
- Implementation details
- Edge cases and error handling
- Testing and validation approaches
- Performance and optimization considerations
```

### 3. Context-Rich Code Review
```
CODE REVIEW REQUEST using structured communication:

PURPOSE: [What this code accomplishes]
CONTEXT: [Technology stack and constraints]
CHANGES: [Summary of modifications]
CONCERNS: [Specific areas of uncertainty]
FOCUS: [What to pay attention to]

[CODE BLOCK]

Specific questions:
1. [Technical concern #1]
2. [Performance/security question]
3. [Maintainability consideration]
```

### 4. Collaborative Architecture Discussion
```
COLLABORATIVE ARCHITECTURE SESSION:
Let's work together on: [System/component design challenge]

My current thinking:
- Approach: [How I'm considering solving it]
- Constraints: [Technical and business limitations]
- Concerns: [What worries me about this approach]
- Unknowns: [Areas where I need guidance]

Please:
- Challenge my assumptions
- Suggest alternative approaches
- Point out potential issues I haven't considered
- Help me think through edge cases and failure scenarios
```

### 5. Structured Debugging Session
```
DEBUGGING SESSION using systematic approach:

PROBLEM: [Clear problem statement]
ENVIRONMENT: [Technical context and setup]
SYMPTOMS: [What's actually happening]
EXPECTED: [What should happen instead]
INVESTIGATION: [What I've already tried]
HYPOTHESIS: [What I think might be wrong]

CODE CONTEXT:
[Relevant code sections]

ASSISTANCE NEEDED:
- Logic review and reasoning validation
- Alternative debugging strategies
- Tool recommendations
- Pattern recognition from similar issues
```

## Cross-Role Collaboration Prompts

### Frontend-Backend Integration
```
Design API contract between frontend and backend for [feature]:
Frontend needs: [list requirements]
Backend capabilities: [list what backend provides]

Include:
- API endpoint specifications
- Request/response schemas
- Error handling strategies
- Authentication requirements
```

### Design-Development Collaboration
```
Create design-to-development handoff documentation for [feature/component]:
Design specifications: [Figma designs and requirements]
Technical constraints: [development limitations]
Implementation timeline: [development schedule]

Include:
- Component specifications and measurements
- Asset export requirements
- Interaction and animation details
- Responsive behavior documentation
- Accessibility requirements
```

### Testing-Development Integration
```
Create testing strategy for [feature/component] that covers:
Development requirements: [functionality to test]
Quality standards: [coverage and performance targets]
Testing timeline: [when tests should be implemented]

Include:
- Unit test requirements and coverage targets
- Integration test scenarios
- UI/E2E test workflows
- Performance testing criteria
- CI/CD integration requirements
```

### Product-Engineering Collaboration
```
Create technical requirements document for [product feature] that bridges product and engineering:
Product requirements: [list product needs]
Technical constraints: [list technical limitations]
User experience goals: [list UX objectives]

Include:
- Feature specifications and acceptance criteria
- Technical implementation approach
- Timeline and resource estimates
- Risk assessment and mitigation strategies
```

### HR-Engineering Collaboration
```
Create technical hiring strategy for [engineering role] that aligns HR and engineering needs:
Role requirements: [technical skills and experience needed]
Team dynamics: [cultural fit and collaboration needs]
Growth trajectory: [career development and advancement]

Include:
- Technical assessment design and evaluation criteria
- Interview process with engineering team involvement
- Onboarding plan with technical mentorship
- Performance evaluation and career development framework
```

### Blockchain-Traditional Development Integration
```
Create integration strategy between blockchain and traditional systems for [use case]:
Blockchain requirements: [decentralization, security, transparency needs]
Traditional system constraints: [existing infrastructure, compliance, performance]
User experience goals: [seamless interaction, familiar interfaces]

Include:
- Hybrid architecture design with on-chain and off-chain components
- API design for blockchain integration
- User authentication and wallet management
- Data synchronization and consistency strategies
```

### DevOps-Development Integration
```
Create deployment strategy for [application] with:
Development requirements: [list dev needs]
Infrastructure constraints: [list limitations]
Performance targets: [specify metrics]

Include:
- CI/CD pipeline design
- Environment configuration
- Monitoring and alerting setup
- Rollback procedures
```

## Best Practices Across All Roles

### 1. Always Specify Context
- Mention your tech stack and versions
- Include project constraints and requirements
- Specify target environment (development, staging, production)

### 2. Include Quality Requirements
- Request error handling and edge case coverage
- Ask for security considerations
- Include performance requirements
- Specify testing needs

### 3. Ask for Documentation
- Request code comments and documentation
- Ask for README updates
- Include API documentation for backend work
- Request component documentation for frontend work

### 4. Consider Maintainability
- Ask for clean, readable code
- Request modular, reusable components
- Include refactoring suggestions
- Ask for code organization best practices

## Example Multi-Role Workflow

### Building a Full-Stack Feature
1. **Product Planning**: Use Product Manager prompts for user research and requirements
2. **Design Phase**: Use UI Designer prompts for prototypes and design systems
3. **Architecture Design**: Use universal architecture prompts
4. **Backend Development**: Use Rust/Node.js backend prompts for API development
5. **Frontend Development**: Use React/Next.js prompts for UI implementation
6. **Testing**: Use Test Engineer prompts for comprehensive testing
7. **Integration**: Use cross-role collaboration prompts
8. **Deployment**: Use DevOps prompts for deployment strategy

### Blockchain Product Development
1. **Research Phase**: Use Product Manager user research prompts
2. **Architecture Phase**: Use Blockchain Architect system design prompts
3. **Smart Contract Development**: Use Blockchain Architect smart contract prompts
4. **Frontend Integration**: Use Frontend development with Web3 integration
5. **Testing Phase**: Use Test Engineer prompts adapted for blockchain testing
6. **Security Audit**: Use Blockchain Architect security framework prompts
7. **Launch Phase**: Use Product Manager go-to-market prompts

### Hiring and Team Building
1. **Role Definition**: Use HR Manager job description prompts
2. **Technical Assessment**: Use role-specific technical prompts for evaluation
3. **Interview Process**: Use HR Manager interview design prompts
4. **Onboarding**: Use HR Manager onboarding prompts with technical mentorship
5. **Performance Management**: Use role-specific performance evaluation prompts

### Product Development Cycle
1. **Research Phase**: Use Product Manager user research prompts
2. **Strategy Phase**: Use Product Manager strategy and roadmap prompts
3. **Design Phase**: Use UI Designer prototype and design system prompts
4. **Development Phase**: Use appropriate engineering guides
5. **Testing Phase**: Use Test Engineer prompts for quality assurance
6. **Launch Phase**: Use Product Manager go-to-market prompts
7. **Optimization Phase**: Use data analysis and performance prompts

### Design-to-Development Workflow
1. **User Research**: Use Product Manager research prompts
2. **Prototype Creation**: Use UI Designer prototype prompts
3. **Design System**: Use UI Designer design system prompts
4. **Component Development**: Use Frontend development prompts
5. **Testing**: Use Test Engineer UI testing prompts
6. **Handoff**: Use design-development collaboration prompts

### Quality Assurance Process
1. **Test Planning**: Use Test Engineer framework setup prompts
2. **Unit Testing**: Use Test Engineer unit testing prompts
3. **Integration Testing**: Use Test Engineer integration prompts
4. **UI Testing**: Use Test Engineer UI/E2E testing prompts
5. **Performance Testing**: Use Test Engineer performance prompts
6. **Reporting**: Use Test Engineer reporting prompts

## Contributing New Role-Specific Guides

To contribute a new job-specific guide:

1. **Follow the established format**:
   - Clear table of contents
   - Categorized prompt sections
   - Template and example prompts
   - Best practices section

2. **Include role-specific scenarios**:
   - Common daily tasks
   - Technology-specific challenges
   - Industry best practices
   - Performance considerations

3. **Provide practical examples**:
   - Real-world use cases
   - Complete prompt templates
   - Expected outcomes
   - Integration guidelines

4. **Consider experience levels**:
   - Basic prompts for beginners
   - Advanced patterns for experienced professionals
   - Leadership prompts for senior roles

## Feedback and Updates

These guides are living documents that should evolve with:
- New technology releases
- Changing best practices
- Community feedback
- Real-world usage patterns

Please contribute improvements, new prompts, and additional role-specific guides to help the entire development community work more efficiently with AI assistants.

---

*Choose the guide that best matches your role and technology stack. For full-stack development or cross-functional teams, use multiple guides as needed. Remember to customize prompts based on your specific project requirements and constraints.* 