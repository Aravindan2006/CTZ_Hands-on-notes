# MongoDB Design -- college_nosql.feedback

## Why MongoDB for feedback data
Course feedback varies wildly in shape from submission to submission:
some include attachments, some don't; tag lists vary in length; future
requirements might add new fields (e.g. `sentiment_score`,
`instructor_response`) without a schema migration. This variability,
combined with the fact that feedback is read far more often as
"whole documents" than joined against other tables, makes it a good
fit for a document store rather than a rigid relational table.

## Document shape
```js
{
  _id: ObjectId(),
  student_id: 1,            // references students.student_id (relational DB)
  course_code: 'CS101',     // references courses.course_code (relational DB)
  semester: '2022-ODD',
  rating: 4,                 // 1-5
  comments: 'Excellent teaching. Would recommend.',
  tags: ['challenging', 'well-structured', 'good-examples'],
  submitted_at: ISODate('2022-11-30T10:15:00Z'),
  attachments: [ { filename: 'notes.pdf', size_kb: 240 } ]  // optional
}
```

## Embedding vs Referencing
- **Referencing** `student_id` / `course_code` back to the relational
  database (rather than embedding student/course details) keeps
  feedback documents small and avoids duplicating data that changes
  independently (e.g. a student's name). This is the standard
  "polyglot persistence" pattern: relational DB owns the
  transactional, structured entities; MongoDB owns the loosely
  structured, high-volume feedback data.
- **Embedding** is used for `attachments`, since attachments are
  inherently owned by exactly one feedback document, are always read
  together with it, and never need to be queried independently across
  documents.

## Indexes (`indexes.js`)
| Index | Fields | Reason |
|---|---|---|
| `idx_course_code` | `course_code` | Most common filter -- "show feedback for course X" |
| `idx_semester_course_code` | `semester, course_code` | Supports the aggregation pipeline's `$match` + `$group` pattern |
| `idx_rating` | `rating` | Supports rating-based filters (e.g. `rating: 5`, or `$lt: 3`) |

`explain('executionStats')` is used to confirm queries on
`course_code` use `IXSCAN` rather than a full `COLLSCAN`.

## Aggregation highlights
- Per-course average rating and feedback count for a given semester
  (`$match` -> `$group` -> `$sort` -> `$project` with `$round`).
- A tag-frequency leaderboard via `$unwind` + `$group`, useful for
  identifying the most common feedback themes at a glance.
