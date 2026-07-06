// =====================================================================
// Hands-On 5 : Task 2
// CRUD Operations on the feedback collection
// Run in mongosh:  load('feedback_data.js') first, then load('crud_queries.js')
// =====================================================================

use("college_nosql");

// ---------------------------------------------------------------------
// 65. READ: all feedback documents where rating is 5
// ---------------------------------------------------------------------
print("--- Rating = 5 ---");
db.feedback.find({ rating: 5 }).forEach(printjson);

// ---------------------------------------------------------------------
// 66. READ: CS101 feedback where tags array contains 'challenging'
// ---------------------------------------------------------------------
print("--- CS101 feedback tagged 'challenging' ---");
db.feedback
  .find({
    course_code: "CS101",
    tags: "challenging", // simple value match against the array
  })
  .forEach(printjson);

// Equivalent using $elemMatch (needed when matching multiple conditions
// on the same array element, e.g. sub-documents rather than scalars):
db.feedback
  .find({
    course_code: "CS101",
    tags: { $elemMatch: { $eq: "challenging" } },
  })
  .forEach(printjson);

// ---------------------------------------------------------------------
// 67. READ: projection -- only student_id, course_code, rating (no _id)
// ---------------------------------------------------------------------
print("--- Projection: student_id, course_code, rating ---");
db.feedback
  .find({}, { student_id: 1, course_code: 1, rating: 1, _id: 0 })
  .forEach(printjson);

// ---------------------------------------------------------------------
// 68. UPDATE: add needs_review: true to all documents with rating < 3
// ---------------------------------------------------------------------
const updateResult1 = db.feedback.updateMany(
  { rating: { $lt: 3 } },
  { $set: { needs_review: true } }
);
print("Matched:", updateResult1.matchedCount, "Modified:", updateResult1.modifiedCount);

// ---------------------------------------------------------------------
// 69. UPDATE: push 'reviewed' tag into all needs_review documents
// ---------------------------------------------------------------------
const updateResult2 = db.feedback.updateMany(
  { needs_review: true },
  { $push: { tags: "reviewed" } }
);
print("Matched:", updateResult2.matchedCount, "Modified:", updateResult2.modifiedCount);

// ---------------------------------------------------------------------
// 70. DELETE: all documents where semester is '2021-EVEN'
// ---------------------------------------------------------------------
const deleteResult = db.feedback.deleteMany({ semester: "2021-EVEN" });
print("Deleted count:", deleteResult.deletedCount);

// Final verification
print("Remaining documents:", db.feedback.countDocuments());
