# User Intent Classifier

## Approach
The solution classifies a user's question about a video into one of three intent categories:

- **frame** — a question about a specific frame or what is visible at a particular moment.
- **whole_video** — a question requesting a summary or information about the entire video.
- **clip** — a question about a specific event or segment of the video that does not match the other categories.

## Implementation
The classifier converts the question to lowercase and uses regular-expression keyword patterns to identify the intent. Frame-related patterns are checked first, followed by whole-video patterns. If neither matches, the question is classified as `clip`.

An empty question raises a `ValueError`.

## Testing
Unit tests cover frame-related questions, whole-video summaries, clip-related questions, and empty input.

## Limitations
This is a rule-based baseline. It may misclassify questions that use unexpected wording or contain overlapping intent signals. Its accuracy should be evaluated against the task's labeled examples and requirements.
