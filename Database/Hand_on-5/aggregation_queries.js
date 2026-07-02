// =====================================================================
// Hands-On 5 : Task 3
// Aggregation Pipeline
// Run in mongosh:  load('feedback_data.js') first, then load('aggregation_queries.js')
// =====================================================================

use("college_nosql");

// ---------------------------------------------------------------------
// 71-72. Filter semester '2022-ODD' -> group by course_code (avg rating,
//         total feedback count) -> sort by avg rating desc -> project +
//         round to 1 decimal place
// ---------------------------------------------------------------------
print("--- Course rating summary (2022-ODD) ---");
db.feedback
  .aggregate([
    { $match: { semester: "2022-ODD" } },
    {
      $group: {
        _id: "$course_code",
        avg_rating: { $avg: "$rating" },
        total_feedback: { $sum: 1 },
      },
    },
    { $sort: { avg_rating: -1 } },
    {
      $project: {
        _id: 0,
        course_code: "$_id",
        average_rating: { $round: ["$avg_rating", 1] },
        total_feedback: 1,
      },
    },
  ])
  .forEach(printjson);

// ---------------------------------------------------------------------
// 73. Tag frequency leaderboard: $unwind tags -> group by tag -> count
//     -> sort descending
// ---------------------------------------------------------------------
print("--- Tag frequency leaderboard ---");
db.feedback
  .aggregate([
    { $unwind: "$tags" },
    { $group: { _id: "$tags", count: { $sum: 1 } } },
    { $sort: { count: -1 } },
  ])
  .forEach(printjson);

// ---------------------------------------------------------------------
// 74. Verify index usage on course_code lookups
//     (index itself is created in indexes.js)
// ---------------------------------------------------------------------
print("--- explain('executionStats') for course_code = 'CS101' ---");
printjson(
  db.feedback.find({ course_code: "CS101" }).explain("executionStats")
    .executionStats.executionStages.stage
);
// Expected (after running indexes.js): "IXSCAN", not "COLLSCAN"
