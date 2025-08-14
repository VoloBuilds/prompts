# Test Engineer Pytest Prompts Guide

A comprehensive collection of AI prompts specifically designed for Test Engineers using pytest framework to build robust test automation suites, ensure software quality, and implement effective testing strategies.

## Table of Contents
1. [Test Framework Setup](#test-framework-setup)
2. [Unit Testing](#unit-testing)
3. [Integration Testing](#integration-testing)
4. [API Testing](#api-testing)
5. [Database Testing](#database-testing)
6. [UI/E2E Testing](#uie2e-testing)
7. [Test Data Management](#test-data-management)
8. [Test Fixtures & Configuration](#test-fixtures--configuration)
9. [Performance Testing](#performance-testing)
10. [Test Reporting & CI/CD](#test-reporting--cicd)

---

## Test Framework Setup

### 1. Pytest Project Setup

**Prompt Template:**
```
You are an expert test engineer. Set up a comprehensive pytest testing framework for [project type] with these requirements:
- Testing scope: [unit/integration/e2e/all]
- Application stack: [technology stack]
- Test environment: [local/CI/cloud]
- Reporting needs: [HTML/XML/dashboard/coverage]
- Integration requirements: [CI/CD tools, databases, APIs]

Include:
- Project structure and organization
- pytest.ini configuration
- conftest.py setup with fixtures
- Requirements and dependencies
- Test discovery and execution setup
```

**Example:**
```
You are an expert test engineer. Set up a comprehensive pytest testing framework for a Python web application with these requirements:
- Testing scope: Unit, integration, and API testing
- Application stack: Flask/Django, PostgreSQL, Redis, REST APIs
- Test environment: Local development and GitHub Actions CI
- Reporting needs: HTML reports, coverage reports, JUnit XML
- Integration requirements: Database fixtures, API mocking, Docker containers

Include:
- Organized test directory structure (tests/unit, tests/integration, tests/api)
- pytest.ini with markers, test paths, and coverage configuration
- conftest.py with database fixtures, API clients, and test data
- requirements-test.txt with pytest plugins and testing dependencies
- Makefile or scripts for running different test suites
```

### 2. Test Configuration Management

**Prompt:**
```
Create a test configuration management system for pytest that handles:
- Multiple test environments (dev, staging, prod)
- Environment-specific test data and settings
- Secure credential management for testing
- Feature flags and test toggles
- Database and service connection configurations

Include:
- Configuration file structure
- Environment variable management
- Fixture-based configuration injection
- Test environment isolation
- Configuration validation and error handling
```

### 3. Test Organization Strategy

**Prompt:**
```
Design a test organization strategy for [application type] using pytest that:
- Separates different types of tests logically
- Enables selective test execution
- Supports parallel test execution
- Facilitates test maintenance and updates
- Provides clear test categorization

Include:
- Directory structure and naming conventions
- Pytest markers for test categorization
- Test collection and filtering strategies
- Documentation and team guidelines
- Scalability considerations for large test suites
```

---

## Unit Testing

### 4. Unit Test Creation

**Prompt Template:**
```
Create comprehensive unit tests using pytest for [function/class/module] with these requirements:
- Code under test: [describe the functionality]
- Test scenarios: [happy path, edge cases, error conditions]
- Dependencies: [external services, databases, file systems]
- Coverage target: [percentage or specific areas]
- Testing approach: [TDD/BDD/traditional]

Include:
- Test class organization and naming
- Parametrized tests for multiple scenarios
- Mock and patch strategies for dependencies
- Assertion patterns and custom assertions
- Test documentation and comments
```

**Example:**
```
Create comprehensive unit tests using pytest for a user authentication service with these requirements:
- Code under test: User login, registration, password reset functionality
- Test scenarios: Valid credentials, invalid passwords, expired tokens, rate limiting
- Dependencies: Database ORM, email service, Redis cache, JWT tokens
- Coverage target: 95% line coverage with focus on security-critical paths
- Testing approach: TDD with security-focused test cases

Include:
- TestUserAuth class with logical test grouping
- Parametrized tests for different credential combinations
- Mock strategies for database, email, and cache dependencies
- Custom assertions for security validations
- Clear test documentation explaining security test rationale
```

### 5. Test-Driven Development (TDD)

**Prompt:**
```
Implement TDD approach using pytest for [feature/functionality] that:
- Starts with failing tests that define requirements
- Implements minimal code to pass tests
- Refactors code while maintaining test coverage
- Follows red-green-refactor cycle
- Ensures comprehensive test coverage

Include:
- Initial failing test cases
- Incremental implementation steps
- Refactoring opportunities and improvements
- Test evolution and maintenance
- Documentation of TDD process and decisions
```

### 6. Mock and Patch Strategies

**Prompt:**
```
Create effective mocking strategies using pytest for [system/component] that:
- Isolates units under test from dependencies
- Provides realistic mock behaviors
- Handles complex dependency chains
- Supports different testing scenarios
- Maintains test reliability and speed

Include:
- Mock object creation and configuration
- Patch decorators and context managers
- Side effects and return value management
- Mock assertion and verification patterns
- Best practices for mock maintenance
```

---

## Integration Testing

### 7. Integration Test Design

**Prompt Template:**
```
Design integration tests using pytest for [system integration] with these requirements:
- Integration scope: [components/services/systems involved]
- Test environment: [local/containerized/cloud]
- Data requirements: [test data setup and cleanup]
- External dependencies: [APIs, databases, message queues]
- Performance considerations: [execution time, resource usage]

Include:
- Test setup and teardown procedures
- Integration test scenarios and workflows
- Error handling and failure recovery
- Test data management strategies
- Environment configuration and isolation
```

**Example:**
```
Design integration tests using pytest for an e-commerce order processing system with these requirements:
- Integration scope: Order service, payment gateway, inventory system, notification service
- Test environment: Docker containers with test databases and mock services
- Data requirements: Customer data, product catalog, payment methods
- External dependencies: Stripe API, email service, inventory database
- Performance considerations: Tests should complete within 30 seconds

Include:
- Docker-compose setup for test environment
- End-to-end order processing test scenarios
- Payment gateway mock and real API testing
- Test data factories for orders, customers, and products
- Cleanup procedures for test data and external service calls
```

### 8. Service Integration Testing

**Prompt:**
```
Create service integration tests for [microservices/APIs] that:
- Test service-to-service communication
- Validate data flow and transformations
- Handle service failures and timeouts
- Test authentication and authorization
- Verify contract compliance

Include:
- Service mock and stub implementations
- Contract testing with schema validation
- Error scenario and resilience testing
- Authentication token management
- Service discovery and configuration testing
```

### 9. Database Integration Testing

**Prompt:**
```
Implement database integration tests using pytest that:
- Test database operations and transactions
- Validate data integrity and constraints
- Test migration and schema changes
- Handle concurrent access scenarios
- Verify performance characteristics

Include:
- Database fixture setup and cleanup
- Transaction isolation and rollback strategies
- Data validation and constraint testing
- Migration testing procedures
- Performance benchmarking and monitoring
```

---

## API Testing

### 10. REST API Testing

**Prompt Template:**
```
Create comprehensive REST API tests using pytest for [API/endpoint] with these requirements:
- API endpoints: [list specific endpoints to test]
- Authentication: [API keys, JWT, OAuth, etc.]
- Test scenarios: [CRUD operations, error cases, edge cases]
- Data validation: [request/response schema validation]
- Performance requirements: [response time, throughput]

Include:
- API client setup and configuration
- Request/response validation
- Authentication and authorization testing
- Error handling and status code verification
- Performance and load testing basics
```

**Example:**
```
Create comprehensive REST API tests using pytest for a blog management API with these requirements:
- API endpoints: /posts, /comments, /users, /auth endpoints
- Authentication: JWT tokens with role-based access control
- Test scenarios: CRUD for posts/comments, user registration/login, permission checks
- Data validation: JSON schema validation for all requests/responses
- Performance requirements: 95% of requests under 200ms response time

Include:
- API client with automatic JWT token management
- JSON schema validation for all endpoints
- Role-based permission testing (admin, author, reader)
- Comprehensive error response testing (400, 401, 403, 404, 500)
- Basic load testing with concurrent requests
```

### 11. GraphQL API Testing

**Prompt:**
```
Implement GraphQL API testing using pytest that covers:
- Query and mutation testing
- Schema validation and introspection
- Error handling and validation
- Authentication and authorization
- Performance and complexity analysis

Include:
- GraphQL client setup and query execution
- Schema introspection and validation
- Query complexity and depth limiting tests
- Authentication context and permission testing
- Error response format validation
```

### 12. API Contract Testing

**Prompt:**
```
Create API contract tests using pytest that:
- Validate API specification compliance
- Test backward compatibility
- Verify schema evolution
- Check breaking changes
- Ensure consumer-provider compatibility

Include:
- OpenAPI/Swagger specification validation
- Contract testing with Pact or similar tools
- Schema versioning and migration testing
- Consumer-driven contract testing
- Breaking change detection and reporting
```

---

## Database Testing

### 13. Database Test Fixtures

**Prompt:**
```
Create database test fixtures using pytest that:
- Provide clean test data for each test
- Handle database setup and teardown
- Support multiple database engines
- Enable test isolation and parallelization
- Manage test data relationships and constraints

Include:
- Database connection and session management
- Test data factory patterns
- Transaction isolation strategies
- Fixture scoping and lifecycle management
- Database migration and schema testing
```

### 14. ORM Testing

**Prompt:**
```
Implement ORM testing strategies using pytest for [ORM framework] that:
- Test model definitions and relationships
- Validate query generation and optimization
- Test data validation and constraints
- Handle migration and schema changes
- Verify performance characteristics

Include:
- Model factory and fixture creation
- Relationship and association testing
- Query optimization and N+1 problem testing
- Migration testing procedures
- Performance profiling and optimization
```

### 15. Data Migration Testing

**Prompt:**
```
Create data migration tests using pytest that:
- Validate migration scripts and procedures
- Test data transformation and integrity
- Handle large dataset migrations
- Verify rollback procedures
- Test migration performance

Include:
- Migration test data setup
- Before/after data validation
- Performance benchmarking
- Rollback and recovery testing
- Data integrity verification procedures
```

---

## UI/E2E Testing

### 16. Selenium Integration

**Prompt Template:**
```
Set up Selenium-based UI testing with pytest for [web application] with these requirements:
- Browser support: [Chrome, Firefox, Safari, Edge]
- Test scenarios: [user workflows to test]
- Page object model: [implementation approach]
- Test data: [user accounts, test data requirements]
- CI/CD integration: [headless execution, reporting]

Include:
- WebDriver setup and configuration
- Page Object Model implementation
- Test data management and cleanup
- Screenshot and video capture on failures
- Cross-browser testing strategies
```

**Example:**
```
Set up Selenium-based UI testing with pytest for an e-commerce web application with these requirements:
- Browser support: Chrome and Firefox with headless options for CI
- Test scenarios: User registration, product search, cart management, checkout process
- Page object model: Separate page classes with element locators and actions
- Test data: Test user accounts, product catalog, payment methods
- CI/CD integration: Headless execution with screenshot capture on failures

Include:
- WebDriver factory with browser selection and configuration
- Page Object classes for home, product, cart, and checkout pages
- Test user factory with different user types and permissions
- Automatic screenshot capture and HTML source saving on test failures
- Docker-based browser execution for CI environments
```

### 17. Playwright Integration

**Prompt:**
```
Implement Playwright-based testing with pytest that:
- Supports multiple browsers and devices
- Handles modern web application features
- Provides fast and reliable test execution
- Includes visual regression testing
- Supports API and UI testing combination

Include:
- Playwright setup and browser management
- Modern web feature testing (SPA, PWA)
- Visual comparison and screenshot testing
- API interception and mocking
- Mobile and responsive testing
```

### 18. Visual Regression Testing

**Prompt:**
```
Create visual regression testing suite using pytest that:
- Captures and compares screenshots
- Handles responsive design testing
- Manages baseline image updates
- Provides detailed diff reporting
- Integrates with CI/CD pipelines

Include:
- Screenshot capture and comparison logic
- Baseline image management
- Responsive breakpoint testing
- Visual diff reporting and analysis
- CI integration with artifact storage
```

---

## Test Data Management

### 19. Test Data Factories

**Prompt:**
```
Create test data factories using pytest that:
- Generate realistic test data
- Handle complex object relationships
- Support different data scenarios
- Provide data cleanup and isolation
- Enable parameterized testing

Include:
- Factory pattern implementation
- Relationship and dependency management
- Data variation and randomization
- Cleanup and teardown procedures
- Integration with test fixtures
```

### 20. Database Seeding

**Prompt:**
```
Implement database seeding strategies for pytest that:
- Provide consistent test data across environments
- Handle data dependencies and relationships
- Support incremental and full data refresh
- Manage sensitive and anonymized data
- Enable selective data loading

Include:
- Seed data definition and management
- Data loading and refresh procedures
- Dependency resolution and ordering
- Data anonymization and privacy protection
- Performance optimization for large datasets
```

### 21. Mock Data Generation

**Prompt:**
```
Create mock data generation system using pytest that:
- Generates realistic fake data
- Supports different data types and formats
- Handles localization and internationalization
- Provides consistent data across test runs
- Enables custom data patterns

Include:
- Faker integration and customization
- Custom data providers and generators
- Localization and cultural data variations
- Seed management for reproducible data
- Performance optimization for large datasets
```

---

## Test Fixtures & Configuration

### 22. Advanced Fixture Design

**Prompt:**
```
Design advanced pytest fixtures for [testing scenario] that:
- Provide efficient resource management
- Support different fixture scopes
- Handle complex setup and teardown
- Enable fixture composition and reuse
- Manage fixture dependencies

Include:
- Fixture hierarchy and dependency management
- Resource pooling and sharing strategies
- Error handling and cleanup procedures
- Fixture parameterization and customization
- Performance optimization techniques
```

### 23. Configuration Management

**Prompt:**
```
Implement test configuration management using pytest that:
- Handles multiple test environments
- Manages sensitive configuration data
- Supports configuration inheritance
- Enables runtime configuration changes
- Provides configuration validation

Include:
- Configuration file structure and formats
- Environment-specific overrides
- Secure credential management
- Configuration injection into tests
- Validation and error handling
```

### 24. Plugin Development

**Prompt:**
```
Create custom pytest plugins for [specific functionality] that:
- Extend pytest capabilities
- Provide reusable testing utilities
- Integrate with external tools
- Support team-specific workflows
- Maintain compatibility with pytest ecosystem

Include:
- Plugin architecture and hooks
- Custom markers and decorators
- Command-line option integration
- Configuration and setup procedures
- Documentation and usage examples
```

---

## Performance Testing

### 25. Load Testing Integration

**Prompt:**
```
Integrate load testing with pytest using [tool/framework] that:
- Tests application performance under load
- Validates response times and throughput
- Identifies performance bottlenecks
- Supports different load patterns
- Provides detailed performance reporting

Include:
- Load test scenario definition
- Performance metric collection
- Baseline and threshold management
- Result analysis and reporting
- CI/CD integration for performance gates
```

### 26. Stress Testing

**Prompt:**
```
Implement stress testing using pytest that:
- Tests system behavior under extreme conditions
- Identifies breaking points and limits
- Validates error handling and recovery
- Tests resource exhaustion scenarios
- Provides stability and reliability metrics

Include:
- Stress test scenario design
- Resource monitoring and measurement
- Failure detection and analysis
- Recovery testing procedures
- Performance degradation analysis
```

### 27. Performance Benchmarking

**Prompt:**
```
Create performance benchmarking suite using pytest that:
- Measures and tracks performance metrics
- Compares performance across versions
- Identifies performance regressions
- Provides statistical analysis
- Integrates with monitoring systems

Include:
- Benchmark test implementation
- Statistical analysis and reporting
- Performance trend tracking
- Regression detection algorithms
- Integration with monitoring and alerting
```

---

## Test Reporting & CI/CD

### 28. Test Reporting

**Prompt Template:**
```
Create comprehensive test reporting for pytest that includes:
- Test execution results and metrics
- Coverage reports and analysis
- Performance and timing data
- Error analysis and debugging information
- Historical trend analysis

Generate reports for:
- Development teams: [detailed technical reports]
- Management: [executive summaries and dashboards]
- CI/CD: [machine-readable formats]
- Quality assurance: [detailed test analysis]

Include multiple output formats and integration options.
```

**Example:**
```
Create comprehensive test reporting for pytest that includes:
- Test execution results with pass/fail rates and execution times
- Code coverage reports with line, branch, and function coverage
- Performance metrics with response times and resource usage
- Detailed error logs with stack traces and debugging information
- Historical trend analysis with regression detection

Generate reports for:
- Development teams: HTML reports with detailed coverage and error analysis
- Management: Executive dashboards with quality metrics and trends
- CI/CD: JUnit XML and JSON formats for pipeline integration
- Quality assurance: Detailed test case analysis with risk assessment

Include Allure reporting, coverage.py integration, and custom dashboard creation.
```

### 29. CI/CD Integration

**Prompt:**
```
Integrate pytest with CI/CD pipeline for [platform] that:
- Runs tests automatically on code changes
- Provides fast feedback to developers
- Manages test environments and dependencies
- Handles test result reporting and notifications
- Supports parallel test execution

Include:
- Pipeline configuration and setup
- Test environment provisioning
- Artifact management and storage
- Notification and alerting setup
- Performance optimization strategies
```

### 30. Quality Gates

**Prompt:**
```
Implement quality gates using pytest that:
- Define quality criteria and thresholds
- Block deployments on quality failures
- Provide clear feedback on quality issues
- Support different quality metrics
- Enable quality trend monitoring

Include:
- Quality metric definition and measurement
- Threshold configuration and management
- Gate evaluation and decision logic
- Reporting and notification systems
- Quality improvement recommendations
```

---

## Advanced Testing Patterns

### 31. Behavior-Driven Development (BDD)

**Prompt:**
```
Implement BDD testing using pytest with [pytest-bdd/behave] that:
- Translates business requirements into tests
- Enables collaboration between technical and non-technical stakeholders
- Provides living documentation
- Supports scenario-based testing
- Maintains traceability between requirements and tests

Include:
- Feature file creation and management
- Step definition implementation
- Scenario outline and data tables
- Background and hook management
- Reporting and documentation generation
```

### 32. Property-Based Testing

**Prompt:**
```
Implement property-based testing using pytest with Hypothesis that:
- Generates test cases automatically
- Finds edge cases and boundary conditions
- Validates system properties and invariants
- Provides shrinking and minimization
- Integrates with existing test suites

Include:
- Property definition and specification
- Custom data generation strategies
- Invariant testing and validation
- Integration with traditional unit tests
- Performance and execution optimization
```

### 33. Mutation Testing

**Prompt:**
```
Implement mutation testing using pytest that:
- Evaluates test suite effectiveness
- Identifies weak spots in test coverage
- Validates test quality and reliability
- Provides mutation score metrics
- Guides test improvement efforts

Include:
- Mutation testing setup and configuration
- Mutant generation and execution
- Survival analysis and reporting
- Test improvement recommendations
- Integration with quality metrics
```

---

## Best Practices Reminders

When using these prompts, remember to:

1. **Follow pytest conventions** - Use proper naming, fixtures, and markers
2. **Write maintainable tests** - Clear, readable, and well-documented test code
3. **Ensure test isolation** - Tests should not depend on each other
4. **Use appropriate test types** - Unit, integration, and E2E tests for different purposes
5. **Manage test data effectively** - Clean setup and teardown procedures
6. **Optimize test execution** - Parallel execution and efficient resource usage
7. **Integrate with CI/CD** - Automated testing and quality gates

## Example Workflow for Test Engineers

```
1. Start with Test Framework Setup for project foundation
2. Implement Unit Tests for individual components
3. Add Integration Tests for component interactions
4. Create API Tests for service interfaces
5. Implement Database Tests for data layer validation
6. Add UI/E2E Tests for user workflow validation
7. Set up Test Data Management for reliable test execution
8. Configure Test Reporting for visibility and tracking
9. Integrate with CI/CD for automated quality assurance
10. Implement Advanced Testing Patterns for comprehensive coverage
```

## Pytest-Specific Tips

- **Use fixtures effectively** - Leverage pytest's powerful fixture system for setup and teardown
- **Implement proper markers** - Organize tests with custom markers for selective execution
- **Utilize parametrization** - Test multiple scenarios with parametrized tests
- **Handle test discovery** - Follow pytest naming conventions for automatic test discovery
- **Optimize test execution** - Use pytest-xdist for parallel execution
- **Integrate plugins** - Leverage pytest ecosystem for extended functionality

## Integration with Development Teams

### Collaboration with Developers
- Use TDD prompts for collaborative test-first development
- Implement code review processes that include test quality
- Provide clear test documentation and examples

### Working with DevOps
- Integrate testing with CI/CD pipelines
- Implement infrastructure testing and monitoring
- Collaborate on test environment management

### Quality Assurance
- Implement comprehensive test coverage strategies
- Use reporting prompts for quality metrics and tracking
- Establish quality gates and standards

---

*This guide is designed to help Test Engineers build comprehensive, maintainable, and effective test suites using pytest. Customize the prompts based on your specific application requirements, testing strategy, and team needs.* 