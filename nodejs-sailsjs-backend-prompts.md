# Node.js Sails.js Backend Engineer Prompts Guide

A comprehensive collection of AI prompts specifically designed for Node.js backend engineers working with Sails.js framework to build scalable, maintainable, and robust web applications and APIs.

## Table of Contents
1. [Project Setup & Architecture](#project-setup--architecture)
2. [Sails.js Application Development](#sailsjs-application-development)
3. [Model & Database Integration](#model--database-integration)
4. [API Development & Controllers](#api-development--controllers)
5. [Authentication & Authorization](#authentication--authorization)
6. [Real-time Features with Sockets](#real-time-features-with-sockets)
7. [Middleware & Policies](#middleware--policies)
8. [Testing & Quality Assurance](#testing--quality-assurance)
9. [Performance & Optimization](#performance--optimization)
10. [Deployment & DevOps](#deployment--devops)

---

## Project Setup & Architecture

### 1. New Sails.js Project Setup

**Prompt Template:**
```
You are an expert Node.js backend developer. Set up a new Sails.js project with these requirements:
- Sails.js version: [specify version]
- Database: [MongoDB/PostgreSQL/MySQL]
- Authentication: [JWT/Passport/custom]
- Real-time features: [WebSocket requirements]
- API type: [REST/GraphQL/both]
- Environment setup: [development/staging/production]

Include:
- Project structure and configuration
- Database connection setup
- Environment variable management
- Package.json with necessary dependencies
- Basic security configurations
```

**Example:**
```
You are an expert Node.js backend developer. Set up a new Sails.js project with these requirements:
- Sails.js version: 1.5.x (latest stable)
- Database: PostgreSQL with Waterline ORM
- Authentication: JWT-based with Passport.js integration
- Real-time features: Socket.io for live notifications and chat
- API type: RESTful APIs with GraphQL endpoint
- Environment setup: Docker-ready for development and production

Include:
- Project structure with organized controllers, models, and services
- PostgreSQL connection with connection pooling
- Environment variables for different deployment stages
- Package.json with security, testing, and development dependencies
- CORS, helmet, and rate limiting configurations
```

### 2. Sails.js Architecture Design

**Prompt:**
```
Design a scalable Sails.js architecture for [application type] with:
- Modular controller organization
- Service layer for business logic
- Helper functions for utilities
- Policy-based authorization
- Hook system for custom functionality
- Configuration management strategy

Include:
- Directory structure and naming conventions
- Separation of concerns principles
- Dependency injection patterns
- Error handling strategy
- Logging and monitoring setup
```

### 3. Environment Configuration

**Prompt:**
```
Set up comprehensive environment configuration for Sails.js application with:
- Development, staging, and production environments
- Database configurations for each environment
- Security settings and secrets management
- Third-party service integrations
- Feature flags and environment-specific settings

Include:
- config/ directory structure
- Environment variable validation
- Configuration inheritance and overrides
- Secure credential management
- Docker and deployment configurations
```

---

## Sails.js Application Development

### 4. Controller Development

**Prompt Template:**
```
Create a Sails.js controller for [resource/feature] with these requirements:
- CRUD operations: [specify which operations]
- Input validation and sanitization
- Error handling and response formatting
- Pagination and filtering support
- Authentication and authorization checks
- [Additional specific requirements]

Include:
- RESTful action methods
- Request/response handling
- Waterline query optimization
- Proper HTTP status codes
- API documentation comments
```

**Example:**
```
Create a Sails.js controller for user management with these requirements:
- CRUD operations: Create, read, update, delete, and list users
- Input validation using joi or express-validator
- Password hashing and secure user creation
- Pagination with limit/offset and search functionality
- Role-based access control for admin operations
- Profile picture upload with file validation

Include:
- RESTful action methods (GET, POST, PUT, DELETE)
- Async/await error handling with try-catch blocks
- Waterline queries with population and associations
- Standardized JSON response format
- JSDoc comments for API documentation
```

### 5. Service Layer Implementation

**Prompt:**
```
Implement Sails.js services for [business domain] that:
- Encapsulate business logic separate from controllers
- Handle complex data operations and transformations
- Integrate with external APIs and services
- Provide reusable functionality across controllers
- Include proper error handling and logging

Create services for:
- [Service 1]: [specific functionality]
- [Service 2]: [specific functionality]
- [Service 3]: [specific functionality]

Include dependency injection and testing strategies.
```

### 6. Helper Functions Development

**Prompt:**
```
Create Sails.js helper functions for [utility purpose] that:
- Provide reusable utility functions
- Handle common operations like [specific operations]
- Include input validation and error handling
- Support both synchronous and asynchronous operations
- Are well-documented and testable

Include:
- Helper function definitions with proper inputs/outputs
- Error handling and validation
- Usage examples and documentation
- Unit tests for each helper
- Performance considerations
```

---

## Model & Database Integration

### 7. Waterline Model Definition

**Prompt Template:**
```
Create Waterline models for [domain/entity] with these requirements:
- Attributes: [list specific attributes and types]
- Associations: [relationships with other models]
- Validations: [validation rules and constraints]
- Lifecycle callbacks: [beforeCreate, afterUpdate, etc.]
- Custom methods: [model-specific functionality]

Include:
- Proper attribute types and validations
- Association definitions (one-to-one, one-to-many, many-to-many)
- Index definitions for performance
- Custom instance and class methods
- Migration considerations
```

**Example:**
```
Create Waterline models for an e-commerce system with these requirements:
- User model: email, password, profile info, roles
- Product model: name, description, price, inventory, categories
- Order model: user reference, products, status, payment info
- Associations: User has many Orders, Order has many Products (through OrderItems)
- Validations: Email format, price ranges, required fields

Include:
- Proper attribute types (string, number, boolean, json)
- Association definitions with foreign keys
- Unique indexes on email, SKU fields
- Password hashing in beforeCreate callback
- Custom methods for order calculations and user authentication
```

### 8. Database Migration Strategy

**Prompt:**
```
Design database migration strategy for Sails.js application with:
- Schema versioning and migration files
- Data migration for existing records
- Rollback procedures and safety measures
- Environment-specific migration handling
- Performance considerations for large datasets

Include:
- Migration file structure and naming
- Safe migration practices
- Data backup and recovery procedures
- Testing migration scripts
- Production deployment strategy
```

### 9. Advanced Waterline Queries

**Prompt:**
```
Implement advanced Waterline queries for [specific use case] that:
- Use complex filtering and sorting
- Include population of associations
- Implement aggregation and grouping
- Handle pagination efficiently
- Optimize for performance

Include:
- Query optimization techniques
- Index usage and performance monitoring
- Error handling for database operations
- Caching strategies for frequently accessed data
- Raw query integration when needed
```

---

## API Development & Controllers

### 10. RESTful API Design

**Prompt Template:**
```
Design and implement RESTful APIs for [resource] using Sails.js with:
- Standard HTTP methods and status codes
- Consistent request/response formats
- Input validation and sanitization
- Error handling and meaningful error messages
- API versioning strategy
- Documentation and examples

Include:
- Route definitions and controller actions
- Request/response schemas
- Validation middleware
- Error response standardization
- API documentation with examples
```

**Example:**
```
Design and implement RESTful APIs for blog management using Sails.js with:
- Posts: CRUD operations with author association
- Comments: Nested under posts with moderation
- Categories: Hierarchical structure with parent/child relationships
- Tags: Many-to-many relationship with posts
- Search and filtering capabilities across all resources

Include:
- Route definitions in config/routes.js
- Controller actions with proper HTTP methods
- JSON schema validation for request bodies
- Standardized error responses with error codes
- OpenAPI/Swagger documentation with examples
```

### 11. GraphQL Integration

**Prompt:**
```
Integrate GraphQL with Sails.js application for [use case] that:
- Defines GraphQL schema for existing models
- Implements resolvers with Waterline integration
- Handles authentication and authorization
- Supports real-time subscriptions
- Includes query optimization and N+1 prevention

Include:
- Schema definition and type resolvers
- Authentication middleware for GraphQL
- Subscription setup with Socket.io
- Query complexity analysis and rate limiting
- Integration with existing REST endpoints
```

### 12. API Versioning Strategy

**Prompt:**
```
Implement API versioning strategy for Sails.js application with:
- Version management approach: [URL path/header/query parameter]
- Backward compatibility maintenance
- Deprecation and sunset policies
- Documentation for multiple versions
- Migration guides for API consumers

Include:
- Routing configuration for versions
- Controller organization by version
- Shared code and DRY principles
- Version-specific middleware
- Client communication strategy
```

---

## Authentication & Authorization

### 13. JWT Authentication System

**Prompt:**
```
Implement JWT authentication system for Sails.js with:
- User registration and login endpoints
- JWT token generation and validation
- Refresh token mechanism
- Password reset functionality
- Account verification and activation
- Security best practices

Include:
- Passport.js integration with JWT strategy
- Secure password hashing with bcrypt
- Token expiration and refresh logic
- Email verification workflow
- Rate limiting for auth endpoints
- Security headers and CORS configuration
```

### 14. Role-Based Access Control (RBAC)

**Prompt:**
```
Implement RBAC system for Sails.js application with:
- User roles and permissions model
- Policy-based authorization
- Resource-level access control
- Dynamic permission checking
- Admin interface for role management

Include:
- Role and permission models with associations
- Policy functions for different access levels
- Middleware for route protection
- Helper functions for permission checking
- Admin dashboard for user and role management
```

### 15. OAuth2 and Social Authentication

**Prompt:**
```
Integrate OAuth2 and social authentication with [providers] using:
- Passport.js strategies for social providers
- Account linking and profile merging
- Secure token storage and management
- User profile synchronization
- Error handling for OAuth failures

Include:
- Provider configuration and setup
- Callback handling and user creation
- Profile data mapping and validation
- Account conflict resolution
- Security considerations and best practices
```

---

## Real-time Features with Sockets

### 16. Socket.io Integration

**Prompt Template:**
```
Implement real-time features using Sails.js sockets for [use case] with:
- Socket connection management
- Room-based messaging and broadcasting
- Authentication for socket connections
- Event handling and message routing
- Error handling and reconnection logic

Include:
- Socket event definitions and handlers
- Room management and user presence
- Message validation and sanitization
- Performance optimization for high concurrency
- Client-side integration examples
```

**Example:**
```
Implement real-time chat system using Sails.js sockets with:
- Multi-room chat with private and public rooms
- User presence indicators and typing notifications
- Message history and persistence
- File sharing and media upload
- Moderation tools and user management

Include:
- Socket event handlers for join/leave/message
- Room-based broadcasting with user lists
- Message validation and content filtering
- Database integration for message persistence
- React/Vue.js client integration examples
```

### 17. Real-time Notifications

**Prompt:**
```
Create real-time notification system with:
- Push notifications to connected clients
- Notification persistence and history
- User preference management
- Different notification types and priorities
- Integration with external push services

Include:
- Notification model and delivery system
- Socket broadcasting to specific users
- Preference-based filtering
- Mobile push notification integration
- Email fallback for offline users
```

### 18. Live Data Synchronization

**Prompt:**
```
Implement live data synchronization for [data type] that:
- Broadcasts model changes to connected clients
- Handles concurrent updates and conflicts
- Maintains data consistency across clients
- Supports offline/online synchronization
- Includes conflict resolution strategies

Include:
- Model lifecycle hooks for broadcasting
- Client-side state management
- Optimistic updates and rollback
- Conflict detection and resolution
- Performance optimization for large datasets
```

---

## Middleware & Policies

### 19. Custom Middleware Development

**Prompt:**
```
Create custom middleware for Sails.js that:
- [Specific middleware functionality]
- Integrates with Sails.js request/response cycle
- Handles errors gracefully
- Is configurable and reusable
- Includes proper logging and monitoring

Include:
- Middleware function implementation
- Configuration options and defaults
- Error handling and next() calls
- Integration with Sails.js hooks
- Testing and documentation
```

### 20. Policy Implementation

**Prompt:**
```
Implement Sails.js policies for [authorization scenario] that:
- Check user authentication and authorization
- Validate request parameters and headers
- Implement rate limiting and throttling
- Handle CORS and security headers
- Provide detailed error responses

Include:
- Policy function definitions
- Integration with controller actions
- Configuration in config/policies.js
- Error handling and response formatting
- Testing strategies for policies
```

### 21. Request Validation Middleware

**Prompt:**
```
Create request validation middleware using [validation library] that:
- Validates request body, query, and parameters
- Provides detailed validation error messages
- Supports custom validation rules
- Integrates with Sails.js error handling
- Includes sanitization and transformation

Include:
- Validation schema definitions
- Custom validator functions
- Error message formatting
- Integration with controllers
- Performance optimization
```

---

## Testing & Quality Assurance

### 22. Unit Testing Strategy

**Prompt:**
```
Create comprehensive unit testing strategy for Sails.js application using [testing framework] with:
- Controller action testing
- Model method and validation testing
- Service function testing
- Helper function testing
- Mock and stub strategies for external dependencies

Include:
- Test setup and teardown procedures
- Database testing with test fixtures
- Mocking external services and APIs
- Code coverage requirements and reporting
- Continuous integration setup
```

### 23. Integration Testing

**Prompt:**
```
Implement integration tests for [API endpoints/features] that:
- Test complete request/response cycles
- Validate database interactions
- Test authentication and authorization flows
- Include error scenario testing
- Test real-time socket functionality

Include:
- Test database setup and cleanup
- API endpoint testing with supertest
- Socket.io testing strategies
- Test data management and fixtures
- Performance and load testing basics
```

### 24. API Testing and Documentation

**Prompt:**
```
Create API testing suite and documentation for [API endpoints] that:
- Tests all CRUD operations and edge cases
- Validates request/response schemas
- Includes authentication testing
- Generates API documentation
- Supports automated testing in CI/CD

Include:
- Postman/Insomnia collection setup
- OpenAPI/Swagger documentation
- Automated schema validation
- Test data generation and management
- Documentation hosting and maintenance
```

---

## Performance & Optimization

### 25. Database Query Optimization

**Prompt:**
```
Optimize database queries for [specific use case] in Sails.js by:
- Analyzing slow queries and bottlenecks
- Implementing proper indexing strategies
- Using query optimization techniques
- Implementing caching layers
- Monitoring query performance

Include:
- Query analysis and profiling tools
- Index creation and maintenance
- Waterline query optimization
- Redis caching implementation
- Performance monitoring and alerting
```

### 26. Caching Implementation

**Prompt:**
```
Implement comprehensive caching strategy using [Redis/Memcached] with:
- API response caching
- Database query result caching
- Session and user data caching
- Cache invalidation strategies
- Performance monitoring and metrics

Include:
- Cache configuration and setup
- Cache key design and naming conventions
- TTL strategies for different data types
- Cache warming and preloading
- Fallback mechanisms for cache failures
```

### 27. Application Performance Monitoring

**Prompt:**
```
Set up application performance monitoring for Sails.js with:
- Request/response time tracking
- Database query performance monitoring
- Memory and CPU usage tracking
- Error rate and exception monitoring
- Custom business metrics tracking

Include:
- APM tool integration (New Relic, DataDog, etc.)
- Custom middleware for performance tracking
- Alerting and notification setup
- Performance dashboard creation
- Optimization recommendations based on metrics
```

---

## Deployment & DevOps

### 28. Docker Configuration

**Prompt:**
```
Create Docker configuration for Sails.js application with:
- Multi-stage build for optimization
- Development and production environments
- Database and Redis service integration
- Environment variable management
- Health checks and monitoring

Include:
- Dockerfile with best practices
- Docker Compose for local development
- Production-ready container configuration
- Security considerations and non-root user
- Volume management for persistent data
```

### 29. CI/CD Pipeline

**Prompt:**
```
Set up CI/CD pipeline for Sails.js application using [GitHub Actions/GitLab CI/Jenkins] with:
- Automated testing on multiple Node.js versions
- Code quality checks and linting
- Security vulnerability scanning
- Automated deployment to [cloud provider]
- Database migration handling

Include:
- Pipeline configuration files
- Test automation and reporting
- Deployment strategies (blue-green, rolling)
- Environment-specific configurations
- Rollback procedures and monitoring
```

### 30. Cloud Deployment

**Prompt:**
```
Deploy Sails.js application to [AWS/GCP/Azure/Heroku] with:
- Container orchestration or serverless deployment
- Database setup and connection management
- Load balancing and auto-scaling
- Environment variable and secrets management
- Monitoring and logging setup

Include:
- Infrastructure as code (Terraform/CloudFormation)
- Database migration and backup strategies
- SSL/TLS certificate management
- CDN setup for static assets
- Cost optimization strategies
```

---

## Advanced Patterns

### 31. Microservices Architecture

**Prompt:**
```
Design microservices architecture using Sails.js with:
- Service decomposition strategy
- Inter-service communication patterns
- Data consistency and transaction management
- Service discovery and load balancing
- Monitoring and observability

Include:
- Service boundary definitions
- API gateway configuration
- Event-driven communication
- Distributed tracing setup
- Fault tolerance and circuit breakers
```

### 32. Event-Driven Architecture

**Prompt:**
```
Implement event-driven architecture with:
- Event sourcing and CQRS patterns
- Message queue integration (RabbitMQ/Apache Kafka)
- Event handlers and processors
- Saga pattern for distributed transactions
- Event replay and recovery mechanisms

Include:
- Event schema design
- Message broker configuration
- Event handler implementation
- Error handling and dead letter queues
- Monitoring and alerting for events
```

### 33. API Gateway Integration

**Prompt:**
```
Integrate Sails.js application with API Gateway for:
- Request routing and load balancing
- Authentication and authorization
- Rate limiting and throttling
- Request/response transformation
- Monitoring and analytics

Include:
- Gateway configuration and setup
- Service registration and discovery
- Security policy implementation
- Performance optimization
- Monitoring and logging integration
```

---

## Best Practices Reminders

When using these prompts, remember to:

1. **Follow Node.js best practices** - Use async/await, proper error handling, and security measures
2. **Leverage Sails.js conventions** - Follow MVC patterns and use built-in features
3. **Include comprehensive testing** - Unit, integration, and API testing
4. **Implement proper security** - Authentication, authorization, input validation, and HTTPS
5. **Optimize for performance** - Database queries, caching, and monitoring
6. **Document thoroughly** - API documentation, code comments, and deployment guides
7. **Plan for scalability** - Database design, caching strategies, and load balancing

## Example Workflow

```
1. Start with Project Setup prompts for architecture
2. Use Model & Database prompts for data layer
3. Implement APIs using Controller Development prompts
4. Add Authentication & Authorization
5. Implement real-time features with Socket prompts
6. Add middleware and policies for security
7. Ensure quality with Testing prompts
8. Optimize with Performance prompts
9. Deploy using DevOps prompts
```

## Sails.js-Specific Tips

- **Use Waterline ORM effectively** - Leverage associations and lifecycle callbacks
- **Implement proper policies** - Use Sails.js policy system for authorization
- **Leverage built-in features** - Use Sails.js blueprints, hooks, and helpers
- **Follow conventions** - Use Sails.js naming conventions and directory structure
- **Optimize for real-time** - Use Socket.io integration for live features
- **Monitor performance** - Use Sails.js built-in logging and monitoring capabilities

---

*This guide is designed to help Node.js backend engineers build robust, scalable applications using Sails.js framework. Customize the prompts based on your specific project requirements and infrastructure needs.* 