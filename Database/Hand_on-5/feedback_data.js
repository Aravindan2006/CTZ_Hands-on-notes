// =====================================================================
// Hands-On 5 : Task 1
// Create the Collection and Insert Documents
// Run in mongosh:  load('feedback_data.js')
// Or paste directly into MongoDB Compass's shell tab.
// =====================================================================

// ---------------------------------------------------------------------
// 60. Switch to (create) the college_nosql database
// ---------------------------------------------------------------------
use("college_nosql");

// ---------------------------------------------------------------------
// 61-63. Create the feedback collection and insert 10+ documents.
// Document #10 intentionally omits the "attachments" field.
// ---------------------------------------------------------------------
db.feedback.insertMany([
  {
    student_id: 1,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 5,
    comments: "Excellent teaching. Would recommend.",
    tags: ["challenging", "well-structured", "good-examples"],
    submitted_at: new Date("2022-11-30T10:15:00Z"),
    attachments: [{ filename: "notes.pdf", size_kb: 240 }],
  },
  {
    student_id: 2,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 4,
    comments: "Good pace, but assignments were tough.",
    tags: ["challenging", "good-examples"],
    submitted_at: new Date("2022-12-01T09:30:00Z"),
    attachments: [{ filename: "assignment1.pdf", size_kb: 120 }],
  },
  {
    student_id: 5,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 3,
    comments: "Average. Could use more real-world examples.",
    tags: ["average-pace"],
    submitted_at: new Date("2022-12-02T14:00:00Z"),
    attachments: [],
  },
  {
    student_id: 1,
    course_code: "CS102",
    semester: "2022-ODD",
    rating: 5,
    comments: "Best DBMS course I have taken.",
    tags: ["well-structured", "good-examples", "engaging"],
    submitted_at: new Date("2022-12-05T11:00:00Z"),
    attachments: [{ filename: "erd_notes.png", size_kb: 340 }],
  },
  {
    student_id: 5,
    course_code: "CS102",
    semester: "2022-ODD",
    rating: 2,
    comments: "Too fast-paced, hard to keep up.",
    tags: ["challenging", "fast-paced"],
    submitted_at: new Date("2022-12-06T16:45:00Z"),
    attachments: [{ filename: "feedback_form.pdf", size_kb: 60 }],
  },
  {
    student_id: 2,
    course_code: "CS103",
    semester: "2022-ODD",
    rating: 4,
    comments: "Great use of live coding demos.",
    tags: ["engaging", "good-examples"],
    submitted_at: new Date("2022-12-07T13:20:00Z"),
    attachments: [{ filename: "demo_code.zip", size_kb: 512 }],
  },
  {
    student_id: 8,
    course_code: "CS103",
    semester: "2022-ODD",
    rating: 5,
    comments: "Loved the OOP project work.",
    tags: ["engaging", "well-structured"],
    submitted_at: new Date("2022-12-08T08:10:00Z"),
    attachments: [{ filename: "project_brief.pdf", size_kb: 95 }],
  },
  {
    student_id: 3,
    course_code: "EC101",
    semester: "2021-ODD",
    rating: 3,
    comments: "Circuit labs need more TA support.",
    tags: ["average-pace", "needs-lab-support"],
    submitted_at: new Date("2021-11-20T10:00:00Z"),
    attachments: [{ filename: "lab_manual.pdf", size_kb: 210 }],
  },
  {
    student_id: 6,
    course_code: "EC101",
    semester: "2021-EVEN",
    rating: 1,
    comments: "Rushed content, unclear explanations.",
    tags: ["challenging", "fast-paced"],
    submitted_at: new Date("2022-04-15T09:00:00Z"),
    attachments: [{ filename: "complaint.pdf", size_kb: 30 }],
  },
  {
    student_id: 4,
    course_code: "ME101",
    semester: "2023-ODD",
    rating: 4,
    comments: "Solid fundamentals, clear diagrams.",
    tags: ["well-structured", "good-examples"],
    submitted_at: new Date("2023-11-25T15:30:00Z"),
    // NOTE: attachments field intentionally omitted (step 63) --
    // MongoDB's schema-less design allows this document to still be
    // valid without every field present.
  },
  {
    student_id: 7,
    course_code: "ME101",
    semester: "2023-ODD",
    rating: 5,
    comments: "Best thermodynamics explanation I've seen.",
    tags: ["engaging", "well-structured", "good-examples"],
    submitted_at: new Date("2023-11-26T12:00:00Z"),
    attachments: [{ filename: "summary_sheet.pdf", size_kb: 80 }],
  },
]);

// ---------------------------------------------------------------------
// 64. Verify the inserts
// ---------------------------------------------------------------------
print("Total feedback documents:", db.feedback.countDocuments());
// Expected: 11 (>= 10 required by the exercise)

print(
  "Documents missing 'attachments':",
  db.feedback.countDocuments({ attachments: { $exists: false } })
);
// Expected: 1
