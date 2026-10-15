
import argparse
import re


def classify_intent(question: str) -> str:
    """Classify a user's question about a video."""
    text = question.lower().strip()

    if not text:
        raise ValueError("Question cannot be empty.")

    frame_patterns = [
        r"\bthis frame\b",
        r"\bin this image\b",
        r"\bwhat is visible\b",
        r"\bat this moment\b",
    ]

    whole_video_patterns = [
        r"\bsummarize\b",
        r"\bsummary\b",
        r"\bentire video\b",
        r"\bwhole video\b",
        r"\boverall\b",
    ]

    if any(re.search(p, text) for p in frame_patterns):
        return "frame"

    if any(re.search(p, text) for p in whole_video_patterns):
        return "whole_video"

    return "clip"


def main():
    parser = argparse.ArgumentParser(
        description="Video question intent classifier"
    )
    parser.add_argument(
        "--question",
        help="Enter a question about a video",
    )
    args = parser.parse_args()

    if args.question is None:
        parser.print_help()
        return

    try:
        print(f"Intent: {classify_intent(args.question)}")
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
