# Task 16 — Gherkin Acceptance Criteria

**User Story:** As a college admin, I want to create a new course, so that students can
enroll in it.

```gherkin
Feature: Course creation by admin

  Scenario: Successfully create a new course (happy path)
    Given I am logged in as a college admin
    And no course with code "CS-301" exists
    When I submit a new course with code "CS-301", title "Algorithms", and 4 credits
    Then the course should be created successfully
    And the course "CS-301" should appear in the course listing

  Scenario: Reject a duplicate course code
    Given I am logged in as a college admin
    And a course with code "CS-301" already exists
    When I submit a new course with code "CS-301", title "Algorithms II", and 3 credits
    Then I should see an error indicating the course code already exists
    And no duplicate course should be created

  Scenario: Reject a course with missing required fields
    Given I am logged in as a college admin
    When I submit a new course with title "Algorithms" but no course code
    Then I should see a validation error indicating "course code is required"
    And no course should be created
```
