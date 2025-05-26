# Rust Backend Engineer Prompts Guide (RIG + Actix-web)

A comprehensive collection of AI prompts specifically designed for Rust backend engineers working with RIG (Rust Intelligence Gateway) and Actix-web to build robust, performant, and secure backend systems.

## Table of Contents
1. [Project Setup & Architecture](#project-setup--architecture)
2. [Actix-web Server Development](#actix-web-server-development)
3. [RIG Integration & AI Features](#rig-integration--ai-features)
4. [Database Integration](#database-integration)
5. [Authentication & Authorization](#authentication--authorization)
6. [API Development](#api-development)
7. [Error Handling & Logging](#error-handling--logging)
8. [Testing & Quality Assurance](#testing--quality-assurance)
9. [Performance & Optimization](#performance--optimization)
10. [Deployment & DevOps](#deployment--devops)

---

## Project Setup & Architecture

### 1. New Rust Backend Project Setup

**Prompt Template:**
```
You are an expert Rust backend developer. Set up a new Rust project with these requirements:
- Use Actix-web as the web framework
- Integrate RIG for AI capabilities
- Include [database type] for data persistence
- Set up [authentication method]
- Configure logging and error handling
- Include Docker configuration
- Set up proper project structure with modules

Create the Cargo.toml, main.rs, and necessary module files with proper dependencies and versions.
```

**Example:**
```
You are an expert Rust backend developer. Set up a new Rust project with these requirements:
- Use Actix-web 4.x as the web framework
- Integrate RIG for LLM integration capabilities
- Include PostgreSQL with SQLx for data persistence
- Set up JWT-based authentication
- Configure structured logging with tracing
- Include Docker configuration for containerization
- Set up proper project structure with modules for handlers, models, services

Create the Cargo.toml, main.rs, and necessary module files with proper dependencies and versions.
```

### 2. Modular Architecture Setup

**Prompt:**
```
Design a modular Rust backend architecture for [application type] with:
- Clean separation of concerns (handlers, services, repositories)
- Dependency injection pattern
- Configuration management
- Error handling strategy
- Middleware organization
- Module structure for scalability

Include file structure and module declarations.
```

---

## Actix-web Server Development

### 3. Basic Actix-web Server

**Prompt Template:**
```
Create an Actix-web server with these features:
- [Feature 1]
- [Feature 2]
- [Feature 3]
- CORS configuration
- Request/response logging middleware
- Health check endpoint
- Graceful shutdown handling

Include proper error handling and configuration management.
```

**Example:**
```
Create an Actix-web server with these features:
- RESTful API endpoints for user management
- File upload capabilities with size limits
- Rate limiting middleware
- CORS configuration for frontend integration
- Request/response logging middleware
- Health check endpoint at /health
- Graceful shutdown handling

Include proper error handling and configuration management.
```

### 4. Custom Middleware Development

**Prompt:**
```
Create custom Actix-web middleware for [purpose] that:
- [Functionality 1]
- [Functionality 2]
- [Functionality 3]
- Handles errors gracefully
- Includes proper logging
- Is configurable and reusable

Include unit tests and documentation.
```

### 5. Request/Response Handling

**Prompt:**
```
Implement Actix-web handlers for [endpoint purpose] with:
- Input validation using serde and validator
- Proper HTTP status codes
- Error response formatting
- Request/response DTOs
- Async processing where appropriate
- Documentation with examples

Include both success and error scenarios.
```

---

## RIG Integration & AI Features

### 6. RIG Setup and Configuration

**Prompt:**
```
Set up RIG (Rust Intelligence Gateway) in an Actix-web application with:
- [LLM provider] integration (OpenAI/Anthropic/local models)
- Configuration for API keys and endpoints
- Error handling for AI service failures
- Rate limiting for AI requests
- Caching for repeated queries
- Proper async handling

Include environment configuration and fallback strategies.
```

### 7. AI-Powered API Endpoints

**Prompt Template:**
```
Create an AI-powered endpoint using RIG that:
- Accepts [input type] from users
- Processes data through [AI model/provider]
- Returns [output format]
- Handles streaming responses if applicable
- Includes proper error handling
- Implements request validation and sanitization

Use RIG's built-in features for [specific functionality].
```

**Example:**
```
Create an AI-powered endpoint using RIG that:
- Accepts text documents from users via POST /api/analyze
- Processes content through OpenAI GPT-4 for sentiment analysis
- Returns structured JSON with sentiment scores and key insights
- Handles streaming responses for real-time feedback
- Includes proper error handling for API failures
- Implements request validation and content sanitization

Use RIG's built-in features for prompt templating and response parsing.
```

### 8. RAG (Retrieval-Augmented Generation) Implementation

**Prompt:**
```
Implement a RAG system using RIG with:
- Vector database integration ([Qdrant/Pinecone/Weaviate])
- Document embedding and indexing
- Similarity search functionality
- Context retrieval and augmentation
- LLM integration for generation
- Caching strategies for performance

Include endpoints for document upload, indexing, and querying.
```

---

## Database Integration

### 9. SQLx Database Setup

**Prompt:**
```
Set up SQLx with [database type] for a Rust backend with:
- Connection pool configuration
- Migration system setup
- Model definitions with proper types
- Repository pattern implementation
- Transaction handling
- Error handling for database operations

Include CRUD operations for [entity type].
```

### 10. Database Models and Migrations

**Prompt:**
```
Create SQLx models and migrations for [domain] with:
- Proper table relationships (foreign keys, indexes)
- Data validation constraints
- Timestamp fields (created_at, updated_at)
- Soft delete functionality if needed
- Migration files for schema changes

Include both up and down migrations.
```

### 11. Repository Pattern Implementation

**Prompt:**
```
Implement the repository pattern for [entity] with:
- Trait definition for repository interface
- SQLx implementation with connection pool
- CRUD operations with proper error handling
- Query optimization and indexing
- Pagination support
- Transaction support for complex operations

Include unit tests with mock implementations.
```

---

## Authentication & Authorization

### 12. JWT Authentication System

**Prompt:**
```
Implement JWT authentication for Actix-web with:
- User registration and login endpoints
- JWT token generation and validation
- Refresh token mechanism
- Password hashing with bcrypt/argon2
- Middleware for protected routes
- Role-based access control (RBAC)

Include proper error handling and security best practices.
```

### 13. OAuth2 Integration

**Prompt:**
```
Integrate OAuth2 authentication with [provider] using:
- OAuth2 flow implementation
- State parameter for CSRF protection
- Token exchange and validation
- User profile retrieval
- Account linking functionality
- Session management

Include error handling for OAuth failures.
```

### 14. Authorization Middleware

**Prompt:**
```
Create authorization middleware that:
- Validates JWT tokens
- Extracts user claims and roles
- Implements permission checking
- Handles token expiration gracefully
- Supports role-based and resource-based permissions
- Includes audit logging

Integrate with Actix-web's middleware system.
```

---

## API Development

### 15. RESTful API Design

**Prompt Template:**
```
Design and implement RESTful APIs for [resource] with:
- Standard HTTP methods (GET, POST, PUT, DELETE)
- Proper status codes and error responses
- Input validation and sanitization
- Pagination for list endpoints
- Filtering and sorting capabilities
- API versioning strategy

Include OpenAPI/Swagger documentation.
```

**Example:**
```
Design and implement RESTful APIs for blog posts with:
- Standard HTTP methods (GET, POST, PUT, DELETE)
- Proper status codes and error responses
- Input validation using serde and validator
- Pagination for list endpoints with cursor-based pagination
- Filtering by author, tags, and date ranges
- API versioning strategy using URL prefixes

Include OpenAPI/Swagger documentation with examples.
```

### 16. GraphQL API Implementation

**Prompt:**
```
Implement a GraphQL API using async-graphql with:
- Schema definition for [domain models]
- Query and mutation resolvers
- Subscription support for real-time updates
- Authentication and authorization integration
- Error handling and validation
- Performance optimization (N+1 problem prevention)

Include integration with Actix-web.
```

### 17. WebSocket Implementation

**Prompt:**
```
Implement WebSocket functionality for [real-time feature] with:
- Connection management and authentication
- Message broadcasting and routing
- Room/channel management
- Heartbeat and reconnection handling
- Rate limiting and abuse prevention
- Integration with existing REST API

Use Actix-web's WebSocket support.
```

---

## Error Handling & Logging

### 18. Comprehensive Error Handling

**Prompt:**
```
Implement a comprehensive error handling system with:
- Custom error types for different error categories
- Error conversion and propagation
- User-friendly error responses
- Internal error logging with context
- Error codes for client identification
- Recovery strategies where possible

Include integration with Actix-web's error handling.
```

### 19. Structured Logging Setup

**Prompt:**
```
Set up structured logging using tracing with:
- Different log levels for various components
- Request tracing and correlation IDs
- Performance metrics logging
- Error tracking and alerting
- Log formatting for different environments
- Integration with external logging services

Include configuration for development and production.
```

### 20. Monitoring and Observability

**Prompt:**
```
Implement monitoring and observability with:
- Prometheus metrics collection
- Health check endpoints with detailed status
- Performance monitoring and profiling
- Distributed tracing setup
- Custom metrics for business logic
- Alerting configuration

Include dashboard configuration examples.
```

---

## Testing & Quality Assurance

### 21. Unit Testing Strategy

**Prompt:**
```
Create comprehensive unit tests for [component] with:
- Test fixtures and mock data
- Database testing with test containers
- HTTP client testing with mock servers
- Error scenario testing
- Performance benchmarks
- Property-based testing where applicable

Use tokio-test and mockall for async testing.
```

### 22. Integration Testing

**Prompt:**
```
Implement integration tests for [API endpoints] with:
- Test database setup and cleanup
- Full request/response cycle testing
- Authentication flow testing
- Error handling verification
- Performance testing under load
- Test data management

Include CI/CD pipeline integration.
```

### 23. Load Testing

**Prompt:**
```
Create load testing scenarios for [application] using:
- Realistic user behavior simulation
- Gradual load increase patterns
- Database connection pool testing
- Memory and CPU usage monitoring
- Bottleneck identification
- Performance regression detection

Include test scripts and result analysis.
```

---

## Performance & Optimization

### 24. Database Query Optimization

**Prompt:**
```
Optimize database queries for [specific use case] by:
- Analyzing query execution plans
- Adding appropriate indexes
- Implementing query result caching
- Using connection pooling effectively
- Optimizing N+1 query problems
- Implementing read replicas if needed

Include before/after performance metrics.
```

### 25. Caching Implementation

**Prompt:**
```
Implement caching strategy using [Redis/in-memory] with:
- Cache key design and naming conventions
- TTL strategies for different data types
- Cache invalidation patterns
- Cache warming strategies
- Fallback mechanisms for cache failures
- Performance monitoring and metrics

Include integration with existing API endpoints.
```

### 26. Async Processing and Queues

**Prompt:**
```
Implement background job processing with:
- Job queue system ([Redis/RabbitMQ/database])
- Worker process management
- Job retry and failure handling
- Priority queue implementation
- Job status tracking and monitoring
- Graceful shutdown handling

Include examples for common background tasks.
```

---

## Deployment & DevOps

### 27. Docker Configuration

**Prompt:**
```
Create Docker configuration for Rust backend with:
- Multi-stage build for optimization
- Security best practices (non-root user)
- Health check configuration
- Environment variable management
- Volume mounting for persistent data
- Docker Compose for local development

Include both development and production configurations.
```

### 28. CI/CD Pipeline

**Prompt:**
```
Set up CI/CD pipeline for Rust backend using [GitHub Actions/GitLab CI] with:
- Automated testing on multiple Rust versions
- Code quality checks (clippy, fmt)
- Security vulnerability scanning
- Docker image building and pushing
- Automated deployment to [cloud provider]
- Rollback strategies

Include environment-specific configurations.
```

### 29. Cloud Deployment

**Prompt:**
```
Deploy Rust backend to [AWS/GCP/Azure] with:
- Container orchestration ([Kubernetes/ECS])
- Load balancer configuration
- Database setup and connection
- Environment variable management
- Logging and monitoring setup
- Auto-scaling configuration

Include infrastructure as code (Terraform/CloudFormation).
```

---

## Advanced Patterns

### 30. Event-Driven Architecture

**Prompt:**
```
Implement event-driven architecture with:
- Event sourcing pattern
- CQRS (Command Query Responsibility Segregation)
- Event store implementation
- Event handlers and processors
- Saga pattern for distributed transactions
- Event replay and recovery mechanisms

Include integration with message brokers.
```

### 31. Microservices Communication

**Prompt:**
```
Implement microservices communication with:
- Service discovery mechanism
- Circuit breaker pattern
- Retry policies with exponential backoff
- Request/response correlation
- Distributed tracing
- API gateway integration

Include error handling and fallback strategies.
```

### 32. Security Hardening

**Prompt:**
```
Implement security hardening measures with:
- Input validation and sanitization
- SQL injection prevention
- XSS protection
- CSRF protection
- Rate limiting and DDoS protection
- Security headers configuration
- Dependency vulnerability scanning

Include security testing and audit procedures.
```

---

## Best Practices Reminders

When using these prompts, remember to:

1. **Specify Rust edition** - Use latest stable Rust features
2. **Include error handling** - Rust's Result type and proper error propagation
3. **Memory safety** - Leverage Rust's ownership system
4. **Async/await** - Use tokio for async operations
5. **Testing** - Include unit and integration tests
6. **Documentation** - Add rustdoc comments
7. **Performance** - Consider zero-cost abstractions
8. **Security** - Follow Rust security best practices

## Example Workflow

```
1. Start with Project Setup prompts for architecture
2. Use Actix-web prompts for server implementation
3. Integrate RIG for AI capabilities
4. Add Database Integration for persistence
5. Implement Authentication & Authorization
6. Build APIs using API Development prompts
7. Add comprehensive Error Handling & Logging
8. Ensure quality with Testing prompts
9. Optimize with Performance prompts
10. Deploy using DevOps prompts
```

## RIG-Specific Tips

- **Model Selection**: Choose appropriate LLM providers based on use case
- **Prompt Engineering**: Use RIG's prompt templating for consistency
- **Error Handling**: Implement fallbacks for AI service failures
- **Caching**: Cache AI responses to reduce costs and latency
- **Monitoring**: Track AI usage and performance metrics
- **Security**: Sanitize inputs before sending to AI models

---

*This guide is designed to help Rust backend engineers build robust, scalable, and AI-powered applications using RIG and Actix-web. Customize the prompts based on your specific project requirements and infrastructure.* 