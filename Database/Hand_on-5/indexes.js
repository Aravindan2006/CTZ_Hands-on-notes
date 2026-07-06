// =====================================================================
// Hands-On 5 : Task 3 (Step 74)
// MongoDB Indexes on the feedback collection
// Run in mongosh:  load('indexes.js')
// =====================================================================

use("college_nosql");

// ---------------------------------------------------------------------
// Index on course_code -- speeds up the very common
// db.feedback.find({ course_code: '...' }) lookup pattern
// ---------------------------------------------------------------------
db.feedback.createIndex({ course_code: 1 }, { name: "idx_course_code" });

// ---------------------------------------------------------------------
// Compound index supporting the aggregation pipeline's $match on
// semester followed by grouping per course_code
// ---------------------------------------------------------------------
db.feedback.createIndex(
  { semester: 1, course_code: 1 },
  { name: "idx_semester_course_code" }
);

// ---------------------------------------------------------------------
// Index on rating -- speeds up "find all rating = 5" / range queries
// ---------------------------------------------------------------------
db.feedback.createIndex({ rating: 1 }, { name: "idx_rating" });

// List all indexes to confirm creation
print("--- Indexes on feedback collection ---");
db.feedback.getIndexes().forEach(printjson);

// Confirm the course_code index is actually used (IXSCAN, not COLLSCAN)
print("--- explain for course_code = 'CS101' ---");
printjson(
  db.feedback.find({ course_code: "CS101" }).explain("executionStats")
    .executionStats.executionStages.stage
);
